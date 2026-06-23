# Lab 01 — Terminal tmux Cockpit

## Goal

Use the terminal without losing your place. tmux is optional, but the cockpit idea matters: keep the course book, app, tests, Git, and notes organized.

## Time box

15-20 minutes.

## Why this matters

When engineers work, they often need several things open at once:

- the app running,
- the test command ready,
- Git status visible,
- documentation nearby,
- AI prompts or notes in another window.

If everything is mixed into one terminal, it gets confusing fast. A cockpit helps you stay calm.

## Option A — Use normal terminal tabs

This is the easiest path.

Open four terminal tabs:

| Tab | Command |
|---|---|
| Course book | `make run` |
| Example app | `make startapp` |
| Tests | `make test` |
| Git | `git status` |

## Option B — Use tmux

Install tmux if needed:

```bash
brew install tmux
```

Start a tmux session:

```bash
make tmux
```

If the helper only opens a session, you can split panes manually.

## tmux survival keys

You press `Control-b` first, release it, then press the next key.

| Action | Keys |
|---|---|
| Split left/right | `Control-b` then `%` |
| Split top/bottom | `Control-b` then `"` |
| Move between panes | `Control-b` then arrow key |
| Detach from tmux | `Control-b` then `d` |
| Reattach | `make tmux` |

## Suggested cockpit

| Pane | Purpose | Command |
|---|---|---|
| Workshop book | Read instructions | `make run` |
| Example app | Run API when needed | `make startapp` |
| Tests | Verify changes | `make test` |
| Git | Inspect work | `git status` and `git diff` |
| Notes / AI | Copy prompts and write reflection | no required command |

## Activity

1. Start the workshop book.
2. Start the example app in another tab or pane.
3. Run tests in another tab or pane.
4. Run `git status` in another tab or pane.
5. Write down which tab or pane is responsible for each job.

## What good looks like

By the end, you should be able to say:

> I know where my docs are, where my app is running, where I run tests, and where I inspect Git changes.

## Troubleshooting

| Problem | What to do |
|---|---|
| tmux feels confusing | Use normal terminal tabs. That is completely fine. |
| I closed a terminal | Open a new one, `cd` into the repo, and restart the command. |
| I forgot where I am | Run `pwd` and `ls`. |
| App and docs both need a terminal | Use two tabs or two panes. |

## Checkpoint

You are done when you can see the workshop book, app, tests, and Git status without losing your place.
