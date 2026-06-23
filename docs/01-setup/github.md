# GitHub Setup

GitHub is where we practice controlled change.

## Before class

1. Confirm you can log in to GitHub.
2. Set your name and email locally:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

3. Check your configuration:

```bash
git config --global --list
```

## The core Git loop

```bash
git status
git checkout -b lab/my-small-change
git diff
git add .
git commit -m "Add my small verified change"
```

## What matters

Git is not just a tool. Git is how you show your thinking:

- What changed?
- Why did it change?
- How did you verify it?
- What should someone review?
