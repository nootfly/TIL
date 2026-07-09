# Generate a git commit message from staged changes using Apple's on-device Foundation Models framework (macOS 26+)
```
#!/usr/bin/env swift

// git-ai-commit — generate a git commit message from staged changes using
// Apple's on-device Foundation Models framework (macOS 26+).
//
// Usage:
//   git-ai-commit                 Stage everything (git add .) and print a suggested message
//   git-ai-commit --commit        Stage everything, generate the message, and commit
//   git-ai-commit --commit --push Stage everything, commit, then push to the upstream branch
//   git-ai-commit --help          Show this help
//
// All changes are staged with `git add .` before the message is generated.
// The model runs entirely on-device — no diff ever leaves the machine.

import Foundation
import FoundationModels

// MARK: - Shell helpers

@discardableResult
func run(_ args: [String], quiet: Bool = false) -> (status: Int32, out: String) {
    let task = Process()
    task.executableURL = URL(fileURLWithPath: "/usr/bin/env")
    task.arguments = args
    let pipe = Pipe()
    task.standardOutput = pipe
    if quiet { task.standardError = Pipe() }
    do {
        try task.run()
    } catch {
        FileHandle.standardError.write("error: failed to run \(args.first ?? "?"): \(error)\n".data(using: .utf8)!)
        exit(1)
    }
    let data = pipe.fileHandleForReading.readDataToEndOfFile()
    task.waitUntilExit()
    let out = String(data: data, encoding: .utf8) ?? ""
    return (task.terminationStatus, out.trimmingCharacters(in: .whitespacesAndNewlines))
}

func die(_ message: String) -> Never {
    FileHandle.standardError.write("git-ai-commit: \(message)\n".data(using: .utf8)!)
    exit(1)
}

// MARK: - Structured commit message

@Generable
struct CommitMessage {
    @Guide(description: "A Conventional Commits type: feat, fix, docs, refactor, test, chore, perf, build, or ci")
    let type: String

    @Guide(description: "Optional scope in parentheses, e.g. the component or file area. Empty string if none.")
    let scope: String

    @Guide(description: "Imperative, lower-case summary under 60 characters. No trailing period.")
    let summary: String

    @Guide(description: "1-3 short bullet points explaining what changed and why. Empty array for tiny changes.")
    let bullets: [String]
}

extension CommitMessage {
    var formatted: String {
        let scopePart = scope.isEmpty ? "" : "(\(scope))"
        var text = "\(type)\(scopePart): \(summary)"
        if !bullets.isEmpty {
            text += "\n\n" + bullets.map { "- \($0)" }.joined(separator: "\n")
        }
        return text
    }
}

// MARK: - Argument parsing

let arguments = Array(CommandLine.arguments.dropFirst())
if arguments.contains("--help") || arguments.contains("-h") {
    print("""
    git-ai-commit — generate commit messages with Apple Foundation Models

    Usage:
      git-ai-commit                  Stage everything (git add .) and print a message
      git-ai-commit --commit         Stage everything, generate the message, and commit
      git-ai-commit --commit --push  Stage everything, commit, then push
      git-ai-commit --help           Show this help
    """)
    exit(0)
}
let doCommit = arguments.contains("--commit")
let doPush = arguments.contains("--push")

// MARK: - Gather the diff

guard run(["git", "rev-parse", "--is-inside-work-tree"], quiet: true).status == 0 else {
    die("not inside a git repository")
}

// Stage all changes up front so the message reflects the full working tree.
run(["git", "add", "."])

let diff = run(["git", "diff", "--cached", "--no-color"]).out
if diff.isEmpty {
    die("no changes to commit")
}

let stat = run(["git", "diff", "--cached", "--stat"]).out

// Keep the prompt within the model's context window.
let maxDiffChars = 12_000
let trimmedDiff = diff.count > maxDiffChars
    ? String(diff.prefix(maxDiffChars)) + "\n… [diff truncated]"
    : diff

// MARK: - Model availability

let model = SystemLanguageModel.default
switch model.availability {
case .available:
    break
case .unavailable(let reason):
    die("Foundation Models unavailable: \(reason). Check Apple Intelligence is enabled in System Settings.")
@unknown default:
    die("Foundation Models unavailable for an unknown reason")
}

// MARK: - Generate

let instructions = """
You are an expert software engineer writing a git commit message.
Follow the Conventional Commits style. Be concise and specific.
Describe what changed and why, not a play-by-play of every line.
Base the message only on the provided diff.
"""

let prompt = """
Summarize the following staged git changes as a commit message.

Files changed:
\(stat)

Diff:
\(trimmedDiff)
"""

// Generate with a few retries — some failures (asset warm-up, rate limiting,
// transient ModelManager errors) clear on a second attempt. A fresh session per
// attempt avoids reusing a transcript left in a bad state.
func generateMessage() async -> String {
    let maxAttempts = 3
    var lastError: Error?
    for attempt in 1...maxAttempts {
        let session = LanguageModelSession(model: model, instructions: instructions)
        do {
            let response = try await session.respond(to: prompt, generating: CommitMessage.self)
            return response.content.formatted
        } catch let error as LanguageModelSession.GenerationError {
            switch error {
            case .guardrailViolation:
                die("the on-device safety guardrail blocked this diff. This is usually a false positive on code; try committing a smaller/related subset of the changes.")
            case .exceededContextWindowSize:
                die("the diff is too large for the model's context window. Commit fewer files at a time.")
            case .unsupportedLanguageOrLocale:
                die("the diff's language isn't supported by the on-device model.")
            case .rateLimited, .concurrentRequests, .assetsUnavailable:
                lastError = error  // transient — retry
            default:
                die("generation failed: \(error.localizedDescription)")
            }
        } catch {
            lastError = error  // unknown/transient — retry
        }
        if attempt < maxAttempts {
            FileHandle.standardError.write("git-ai-commit: attempt \(attempt) failed, retrying…\n".data(using: .utf8)!)
            try? await Task.sleep(for: .seconds(1))  // brief backoff for asset warm-up
        }
    }
    die("generation failed after \(maxAttempts) attempts: \(lastError.map { String(describing: $0) } ?? "unknown error")")
}

let message = await generateMessage()

// MARK: - Output / commit / push

if doCommit {
    let result = run(["git", "commit", "-m", message])
    print(result.out)
    guard result.status == 0 else { exit(result.status) }

    if doPush {
        let push = run(["git", "push"])
        print(push.out)
        exit(push.status)
    }
} else {
    print(message)
}
```