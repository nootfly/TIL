Herdr is useful when you run several coding agents—such as Codex, Claude Code or Gemini CLI—and want to see them in one persistent terminal workspace. It is essentially **tmux designed for AI agents**, showing whether each agent is working, idle, blocked or finished. 

### 1. Start with one project per workspace

From your project folder:

```bash
cd ~/Projects/MyApp
herdr
```

Create a workspace for each project rather than mixing unrelated repositories together.

A practical structure might be:

```text
ReflectMind
├── Agent: feature development
├── Agent: tests
├── Terminal: build/run
└── Terminal: git status
```

This makes it much easier to understand which agent changed which files.

### 2. Learn only five shortcuts initially

Herdr uses a tmux-style prefix: press `Ctrl+B`, release it, then press the next key.

```text
Ctrl+B, Shift+N   Create a workspace
Ctrl+B, W         Open workspace navigation
Ctrl+B, V         Split the current pane
Ctrl+B, -         Split in the other direction
Ctrl+B, C         Create another tab
Ctrl+B, Q         Detach while processes continue
```

You can later run `herdr` again to reconnect to the existing session. Detached panes and agents continue running in the background. 

### 3. Give agents clearly separated responsibilities

Avoid asking three agents to edit the same feature simultaneously.

A better division is:

```text
Agent 1: Implement the feature
Agent 2: Write and run tests
Agent 3: Review the diff and identify problems
Agent 4: Research an API without modifying code
```

This reduces merge conflicts and duplicated work.

### 4. Use Git worktrees for parallel coding

When two agents need to modify the same repository, give each agent its own Git worktree:

```bash
git worktree add ../myapp-feature feature/login
git worktree add ../myapp-tests test/login-tests
```

Then open each worktree in a separate Herdr workspace or pane.

This is much safer than having several agents write into the same working directory. Recent Herdr releases also include built-in worktree commands such as `herdr worktree create`, `open`, `list` and `remove`. 

### 5. Keep a supervising pane

Reserve one pane for yourself:

```bash
git status
git diff --stat
```

Use it to regularly check:

```bash
git diff
git log --oneline --decorate -10
```

Do not rely only on an agent saying “done.” Review the actual diff and run the tests yourself.

### 6. Make agents stop at clear checkpoints

Good prompts include explicit stopping rules:

```text
Implement this feature and run the relevant unit tests.

Do not commit or push.
Stop and ask me before changing the database schema.
At the end, report:
1. Files changed
2. Tests run
3. Remaining risks
```

Herdr is especially helpful here because its sidebar lets you notice agents waiting for approval or input.

### 7. Use persistence for long-running work

You can leave builds, tests or agents running and detach:

```text
Ctrl+B, Q
```

Reconnect later:

```bash
herdr
```

Only use this when you genuinely want to terminate all panes:

```bash
herdr server stop
```

Stopping the server ends the session and its pane processes. 

### 8. Use your Mac mini as an agent machine

For your setup, a useful pattern would be:

```bash
ssh mac-mini
herdr
```

Run the coding agents on the Mac mini, detach, and reconnect from your MacBook later. You can also attach directly from your local terminal with:

```bash
herdr --remote mac-mini
```

Herdr supports persistent remote sessions through normal SSH, including reconnecting from another computer or an SSH client on a phone. 

### 9. Be cautious with plugins

Herdr plugins execute ordinary code with your user permissions. They are not sandboxed. Review the plugin manifest and scripts before installing them, and only install plugins from authors you trust. 

### A good first workflow for you

```text
Workspace: iOS App
├── Pane 1: Codex implementing the feature
├── Pane 2: Claude reviewing architecture
├── Pane 3: xcodebuild unit/UI tests
└── Pane 4: Your shell for git diff and commits
```

Start with only **two agents plus one test pane**. Adding five or ten agents immediately usually creates more coordination work than useful output.