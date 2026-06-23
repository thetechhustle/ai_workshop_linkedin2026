# Lab 02 — Git + AI Change

## Goal

Use AI to plan one small change, then use Git to control it.

## Commands

```bash
git status
git checkout -b lab/my-small-change
```

## Prompt

```text
You are my engineering coach. Inspect this project and suggest one small improvement. Do not write code yet. First explain the plan and the files you expect to touch.
```

## After editing

```bash
make test
git diff
git status
```

Commit only when you understand the diff:

```bash
git add .
git commit -m "Add small verified project improvement"
```

## Checkpoint

You can explain what changed, why it changed, and how you verified it.
