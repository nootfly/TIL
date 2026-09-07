I’m not currently inside a Herdr-managed pane, so I couldn’t verify the installed CLI version. Here’s the core cheatsheet from the Herdr workflow:

# Herdr Cheatsheet

## Discover commands

```bash
herdr --help
herdr agent
herdr pane
herdr workspace
herdr tab
herdr worktree
herdr terminal
herdr notification
herdr integration
herdr session
```

Avoid bare `herdr`; it launches or attaches the TUI.

## Current context

```bash
echo "$HERDR_WORKSPACE_ID"
echo "$HERDR_TAB_ID"
echo "$HERDR_PANE_ID"

herdr pane current --current
herdr pane layout --pane "$HERDR_PANE_ID"
```

## Inspect everything

```bash
herdr workspace list
herdr tab list --workspace "$HERDR_WORKSPACE_ID"
herdr pane list --workspace "$HERDR_WORKSPACE_ID"
herdr agent list
```

## Create layout

```bash
# Split right
herdr pane split --current --direction right --cwd "$PWD" --no-focus

# Split down
herdr pane split --current --direction down --cwd "$PWD" --no-focus
```

Read the new pane ID from:

```text
.result.pane.pane_id
```

## Start an agent

```bash
herdr agent start reviewer --kind codex --pane <pane-id>
```

Pass native agent arguments after `--`:

```bash
herdr agent start reviewer --kind codex --pane <pane-id> -- <agent-args>
```

Agent names must be unique and match:

```text
[a-z][a-z0-9_-]{0,31}
```

## Prompt and wait

```bash
herdr agent prompt reviewer \
  "Review the current diff and report actionable findings." \
  --wait \
  --timeout 120000
```

Wait on an existing task:

```bash
herdr agent wait reviewer --timeout 120000
```

Wait specifically for user input or approval:

```bash
herdr agent wait reviewer --until blocked --timeout 120000
```

## Inspect an agent

```bash
herdr agent get reviewer
herdr agent read reviewer --source recent-unwrapped --lines 120
```

## Send control keys

```bash
herdr agent send-keys reviewer esc
herdr agent send-keys reviewer ctrl+c
```

## Run an ordinary command

```bash
herdr pane run <pane-id> "just test"
```

Wait for output:

```bash
herdr pane wait-output <pane-id> \
  --match "test result" \
  --timeout 120000
```

Regex matching:

```bash
herdr pane wait-output <pane-id> \
  --regex "passed|failed" \
  --timeout 120000
```

## Read terminal output

```bash
herdr pane read <pane-id> --source visible
herdr pane read <pane-id> --source recent
herdr pane read <pane-id> --source recent-unwrapped --lines 120
herdr pane read <pane-id> --source detection
```

Use `recent-unwrapped` for logs and transcripts. Add `--format ansi` when colors matter.

## Agent states

```text
idle     Ready; its tab has been seen
working  Agent is active
blocked  Waiting for approval or an answer
done     Background work finished but is unseen
unknown  Agent detected, state uncertain
```

## Targeting rules

Prefer:

```bash
--current
--pane <pane-id>
<unique-agent-name>
```

IDs look like:

```text
Workspace: w1
Tab:       w1:t1
Pane:      w1:p1
```

Treat IDs as opaque—always copy them from command output.

## Safety rules

- Use `--no-focus` for background work.
- Preserve the working directory with `--cwd "$PWD"`.
- Don’t close panes, tabs, or workspaces you didn’t create.
- Don’t run `herdr server stop` unless intentionally stopping every pane process.
- Don’t kill the main Herdr process.
- Inspect `agent get` and `agent read` before responding to a blocked or failed wait.

To verify the installed syntax, run this from inside a Herdr pane:

```bash
test "${HERDR_ENV:-}" = 1 && herdr --help
```