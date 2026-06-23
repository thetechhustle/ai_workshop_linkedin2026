# Module 02 — Terminal, tmux, and Git

## Why this module matters

The terminal can feel intimidating because it gives you fewer visual hints than an app. But the terminal is also where engineers run projects, read errors, start servers, run tests, use Git, and work with AI coding agents.

You do not need to become a command-line wizard today. You need a few reliable moves.

## Learning goals

By the end of this module, you should be able to:

1. Run basic terminal commands without panic.
2. Explain what `make` does for this workshop.
3. Use tmux as a cockpit for docs, app, tests, and Git.
4. Use Git to inspect changes before committing.

## The beginner terminal map

| Command | Meaning | Why we use it |
|---|---|---|
| `pwd` | Print working directory. | Shows where you are. |
| `ls` | List files. | Shows what is in the current folder. |
| `cd folder` | Change directory. | Moves into another folder. |
| `cd ..` | Move up one folder. | Gets you out of a folder. |
| `clear` | Clean the terminal screen. | Reduces visual noise. |
| `make help` | Show workshop shortcuts. | Tells you what commands exist. |
| `git status` | Show Git state. | Tells you what changed. |
| `git diff` | Show line-by-line changes. | Lets you review before saving. |

## Why make exists

Without `make`, you would need to remember long commands like:

```bash
.venv/bin/python -m pytest starter_app/tests -q
```

Instead, you run:

```bash
make test
```

That is the point of the Makefile: simple commands that work the same for everyone.

## Workshop cockpit layout

Use multiple terminal tabs or tmux panes:

| Pane | What runs there | Why it matters |
|---|---|---|
| Course book | `make run` | Keeps the instructions open. |
| Example app | `make startapp` | Runs the local API. |
| Tests | `make test` | Verifies behavior. |
| Git | `git status` and `git diff` | Shows what changed. |
| Notes / AI | Prompts and reflection | Keeps your thinking visible. |

## tmux basics

Start the session:

```bash
make tmux
```

Useful keys:

| Action | Keys |
|---|---|
| Create a new pane | `Control-b` then `%` |
| Split vertically | `Control-b` then `"` |
| Move between panes | `Control-b` then arrow key |
| Detach from session | `Control-b` then `d` |
| Reattach later | `make tmux` |

If tmux is too much today, use normal terminal tabs. The learning goal is organization, not tmux perfection.

## Git controlled-change flow

```bash
git status
git checkout -b lab/my-change
# edit one small thing
git diff
make test
git add .
git commit -m "Describe the verified change"
```

This is how you avoid mystery changes. You make one branch, one small change, one reviewable diff.

## Mini activity

Run these commands and write down what each one tells you:

```bash
pwd
ls
make help
git status
```

Then answer:

- What folder am I in?
- What files or folders do I see?
- What make command starts the workshop book?
- What does Git say about my working tree?

## Checkpoint

You are ready when you can keep the course book, app, tests, and Git status visible without losing your place.
