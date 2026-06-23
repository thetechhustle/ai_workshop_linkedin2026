# Lab 02 — Git + AI Change

## Goal

Use AI to plan one small improvement, then use Git to keep the change controlled and reviewable.

This lab is not about making the biggest change. It is about making a change you understand.

## Time box

30-40 minutes.

## Choose your track

| Track | Best for | Change idea |
|---|---|---|
| Bronze | Newer students | Ask AI to explain the app and improve a README section. |
| Silver | Some coding comfort | Add one small API behavior or validation improvement. |
| Gold | Stronger students | Add a test first, then implement the behavior. |

## Step 1 — Check your starting point

```bash
git status
make test
```

You want a clean starting point before changing anything. If `git status` says files are already modified, ask for help before continuing.

## Step 2 — Create a branch

```bash
git checkout -b lab/my-small-change
```

A branch is a safe workspace. If your change goes sideways, main is still safe.

## Step 3 — Ask AI for a plan, not code

Copy this prompt into your approved AI tool:

```text
You are my engineering coach. I am working in this workshop repo. Inspect the project and suggest one small improvement that a beginner can understand. Do not edit files yet. First explain the current structure, the plan, the files you expect to touch, and the test or quality check I should run.
```

Read the answer. Do not accept a plan you cannot explain.

## Step 4 — Pick one small improvement

Good beginner improvements:

- improve the starter app README,
- add a clearer error message,
- add a simple `priority` or `category` idea as a documented stretch goal,
- add or improve one test,
- add comments explaining the API flow.

Avoid for now:

- replacing the framework,
- adding authentication,
- adding multiple new packages,
- changing many files at once,
- deploying to the internet.

## Step 5 — Make the change

Use AI help if approved, but keep the change small. After editing, run:

```bash
git diff
```

Read the diff. Ask yourself:

- Did only the expected files change?
- Do I understand every changed line?
- Did AI add anything unrelated?

## Step 6 — Verify

Run:

```bash
make test
```

If tests fail, do not immediately ask AI to rewrite everything. First copy the error and ask:

```text
Explain this test failure in beginner-friendly language. Do not change code yet. Tell me the most likely cause and the smallest fix to investigate.
```

## Step 7 — Commit

Only commit when you understand the diff and have run a quality check.

```bash
git add .
git commit -m "Add small verified project improvement"
```

## Reflection

Write three sentences:

1. I changed ________.
2. I verified it by ________.
3. I still want to understand ________.

## Checkpoint

You are done when you can explain what changed, why it changed, and how you verified it.
