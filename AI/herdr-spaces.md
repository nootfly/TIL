In Herdr, a “Space” is a workspace: the top-level container for a repo, task, or investigation. Each workspace contains tabs, and each tab contains terminal panes. [Herdr concepts](https://herdr.dev/docs/concepts/)

### Rename a Space

Using the keyboard:

1. Press `Ctrl+B`, then release.
2. Press `Shift+W`.
3. Enter the new name.

From a terminal inside that Space:

```bash
herdr workspace rename "$HERDR_WORKSPACE_ID" "New Name"
```

Or list IDs and rename a specific Space:

```bash
herdr workspace list
herdr workspace rename w1 "New Name"
```

### Use Spaces

Useful shortcuts:

- `Ctrl+B`, then `W` — open Space navigation
- `Ctrl+B`, then `Shift+N` — create a Space
- `Ctrl+B`, then `Shift+W` — rename the selected Space
- `Ctrl+B`, then `Shift+D` — close the selected Space
- `Ctrl+B`, then `B` — toggle the sidebar
- `Ctrl+B`, then `G` — open the global picker

“Prefix” means pressing `Ctrl+B`, releasing it, and then pressing the action key. [Herdr keyboard reference](https://herdr.dev/docs/keyboard/)

A sensible organization is:

```text
Space: backend-api
├── Tab: agent
├── Tab: server
└── Tab: tests

Space: frontend
├── Tab: agent
└── Tab: dev-server
```

Use one Space per project or major work context. Use tabs for roles such as agents, logs, servers, and reviews; split panes when you need multiple terminals visible together.