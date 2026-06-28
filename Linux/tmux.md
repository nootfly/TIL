# tmux cheat sheet

tmux lets you keep terminal sessions running, split windows, and reconnect later.

Default prefix key:

```bash
Ctrl + b
```

After pressing `Ctrl + b`, release both keys, then press the command key.

---

## Sessions

Create a new session:

```bash
tmux
```

Create a named session:

```bash
tmux new -s myproject
```

List sessions:

```bash
tmux ls
```

Attach to a session:

```bash
tmux attach -t myproject
```

Detach from current session:

```text
Ctrl + b, then d
```

Kill a session:

```bash
tmux kill-session -t myproject
```

Rename current session:

```text
Ctrl + b, then $
```

---

## Windows

A tmux **window** is like a terminal tab.

Create new window:

```text
Ctrl + b, then c
```

Switch to next window:

```text
Ctrl + b, then n
```

Switch to previous window:

```text
Ctrl + b, then p
```

Switch to window by number:

```text
Ctrl + b, then 0
Ctrl + b, then 1
Ctrl + b, then 2
```

Rename current window:

```text
Ctrl + b, then ,
```

Close current window:

```text
Ctrl + b, then &
```

Show window list:

```text
Ctrl + b, then w
```

---

## Panes

A tmux **pane** is a split inside a window.

Split vertically, left/right:

```text
Ctrl + b, then %
```

Split horizontally, top/bottom:

```text
Ctrl + b, then "
```

Move between panes:

```text
Ctrl + b, then arrow key
```

Close current pane:

```text
Ctrl + b, then x
```

Zoom current pane fullscreen:

```text
Ctrl + b, then z
```

Resize pane:

```text
Ctrl + b, then hold Ctrl + arrow key
```

Show pane numbers:

```text
Ctrl + b, then q
```

Convert pane to new window:

```text
Ctrl + b, then !
```

---

## Copy and scroll

Enter scroll/copy mode:

```text
Ctrl + b, then [
```

Move around:

```text
Arrow keys
Page Up
Page Down
```

Quit copy mode:

```text
q
```

Search in scrollback:

```text
Ctrl + b, then [
/search-text
Enter
```

---

## Useful commands inside tmux

Show all key bindings:

```bash
tmux list-keys
```

Show all sessions:

```bash
tmux list-sessions
```

Show all windows:

```bash
tmux list-windows
```

Show all panes:

```bash
tmux list-panes
```

Reload tmux config:

```bash
tmux source-file ~/.tmux.conf
```

---

## Good daily workflow

For one project:

```bash
tmux new -s orderbuddy
```

Then use windows like this:

```text
Window 1: editor
Window 2: dev server
Window 3: tests
Window 4: logs
Window 5: git
```

Example:

```text
Ctrl + b, c    # new window
Ctrl + b, ,    # rename it
```

Names:

```text
code
server
tests
logs
git
```

Detach when finished:

```text
Ctrl + b, d
```

Later reconnect:

```bash
tmux attach -t orderbuddy
```

---

## Recommended `.tmux.conf`

Create or edit:

```bash
nano ~/.tmux.conf
```

Add:

```bash
# Use mouse for pane selection, resizing, and scrolling
set -g mouse on

# Start window and pane numbering at 1
set -g base-index 1
setw -g pane-base-index 1

# Larger scrollback history
set -g history-limit 50000

# Better colors
set -g default-terminal "screen-256color"

# Reload config with Prefix + r
bind r source-file ~/.tmux.conf \; display-message "tmux config reloaded"

# Easier pane splitting
bind | split-window -h
bind - split-window -v

# Move between panes using vim-style keys
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R

# Resize panes
bind -r H resize-pane -L 5
bind -r J resize-pane -D 5
bind -r K resize-pane -U 5
bind -r L resize-pane -R 5
```

Reload:

```bash
tmux source-file ~/.tmux.conf
```

Now you can use:

```text
Ctrl + b, |
Ctrl + b, -
Ctrl + b, h/j/k/l
Ctrl + b, r
```

---

## Best tips

Use **named sessions**. Instead of just running `tmux`, use:

```bash
tmux new -s appname
```

This makes it much easier to reconnect later.

Use **one session per project**. For example:

```bash
tmux new -s orderbuddy
tmux new -s ai-agent
tmux new -s firebase-test
```

Use tmux for long-running tasks:

```bash
npm run dev
npm test -- --watch
firebase emulators:start
docker compose up
tail -f app.log
```

Detach safely with:

```text
Ctrl + b, d
```

Your commands keep running.

For AI coding agents, tmux is very useful. Put the agent in one pane, tests in another pane, logs in another pane.

Example layout:

```text
+----------------------+----------------------+
| Claude / agent       | npm test --watch     |
|                      |                      |
+----------------------+----------------------+
| dev server logs      | git / terminal       |
+----------------------+----------------------+
```

Use zoom often:

```text
Ctrl + b, z
```

This makes one pane fullscreen temporarily.

---

## Common problems

### tmux mouse scroll does not work

Add this to `~/.tmux.conf`:

```bash
set -g mouse on
```

Reload:

```bash
tmux source-file ~/.tmux.conf
```

### I forgot the session name

```bash
tmux ls
```

Then:

```bash
tmux attach -t session-name
```

### Kill everything

```bash
tmux kill-server
```

Be careful. This closes all tmux sessions.

### Prefix key is annoying

Some developers change prefix from `Ctrl + b` to `Ctrl + a`:

```bash
unbind C-b
set -g prefix C-a
bind C-a send-prefix
```

Then use:

```text
Ctrl + a
```

instead of:

```text
Ctrl + b
```

---

## My suggested beginner setup

Start with only these commands:

```text
Ctrl + b, c      new window
Ctrl + b, n      next window
Ctrl + b, p      previous window
Ctrl + b, %      vertical split
Ctrl + b, "      horizontal split
Ctrl + b, arrow  move pane
Ctrl + b, z      zoom pane
Ctrl + b, d      detach
```

That is enough for 90% of daily use.
