# GitHub Setup

GitHub is where we practice controlled change. In class, GitHub is less about looking fancy and more about showing your work clearly.

## What Git and GitHub do

| Tool | Plain-English meaning |
|---|---|
| Git | Tracks changes to files over time on your laptop. |
| GitHub | Hosts repositories online so people can share and review code. |
| Commit | A saved checkpoint. |
| Branch | A safe workspace for a change. |
| Diff | The exact lines that changed. |
| Pull request | A review conversation around a proposed change. |

## Before class

Confirm you can log in to GitHub. Then set your name and email locally:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Check your configuration:

```bash
git config --global --list
```

## The core Git loop

Use this loop every time you make a change:

```bash
git status
git checkout -b lab/my-small-change
git status
# edit files
git diff
make test
git add .
git commit -m "Add my small verified change"
```

## What each command teaches you

| Command | What it tells you |
|---|---|
| `git status` | Which files changed and which branch you are on. |
| `git checkout -b ...` | Creates a new branch for your work. |
| `git diff` | Shows the exact change before you save it as a commit. |
| `git add .` | Stages files for the next commit. |
| `git commit -m ...` | Saves the checkpoint with a message. |

## How to write a useful commit message

A good commit message finishes this sentence:

> This change will...

Examples:

```bash
git commit -m "Add status update test"
git commit -m "Document local API startup"
git commit -m "Improve opportunity validation message"
```

Avoid messages like:

```bash
git commit -m "stuff"
git commit -m "changes"
git commit -m "fix"
```

Those do not help your future self or your teammates.

## AI and Git

AI can help you write code, but Git helps you stay in control. Before accepting AI-generated changes, always ask:

- What files changed?
- Do I understand why they changed?
- Did the change touch more than expected?
- Did I run a quality gate?
- Can I explain this diff to another student?

## Checkpoint

You are ready when you can explain the difference between:

- a branch and a commit,
- a changed file and a staged file,
- a diff and a test.
