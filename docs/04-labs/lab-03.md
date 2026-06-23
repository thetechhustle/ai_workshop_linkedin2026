# Lab 03 — Quality Gate and Production Awareness

## Goal

Run tests, inspect supporting project files, and explain what should be checked before an app is shared with other people.

This lab connects the workshop to the real engineering world: code, tests, containers, CI, and responsible release thinking.

## Time box

25-35 minutes.

## Step 1 — Run the quality gate

```bash
make test
make lint
```

What these mean:

| Command | What it checks |
|---|---|
| `make test` | The app behaves the way the tests expect. |
| `make lint` | The code follows basic readability and style rules. |

If lint or tests fail, capture the error. Do not hide it. The error is part of the lab.

## Step 2 — Inspect the tests

Open the test file:

```bash
cat starter_app/tests/test_api.py
```

Look for these ideas:

- health check,
- create an opportunity,
- list opportunities,
- update status,
- handle a missing opportunity.

Answer:

> Which test seems easiest to understand, and why?

## Step 3 — Inspect the Dockerfile

```bash
cat starter_app/Dockerfile
```

A Dockerfile is a recipe for packaging the app. You do not need to master Docker today. Just identify:

- the Python version,
- the app folder,
- the exposed port,
- the command that starts the app.

## Step 4 — Inspect GitHub Actions

```bash
cat .github/workflows/tests.yml
```

This workflow tells GitHub how to run checks automatically. Look for:

- checkout,
- Python setup,
- dependency install,
- pytest command.

Answer:

> What would GitHub check if this workflow runs?

## Step 5 — Production awareness questions

Discuss with a partner:

1. What URL opens the local API docs?
2. What port does the app use?
3. Where does the app store data?
4. What tests exist today?
5. What tests are missing?
6. What would need to be true before users depend on this?

## Beginner production checklist

Before sharing an app widely, ask:

- Can another person install and run it?
- Is there a README with clear setup steps?
- Are tests passing?
- Are errors understandable?
- Are private keys and tokens kept out of code?
- Do we understand where data is stored?
- Do we know who owns the next fix if it breaks?

## Stretch challenge

Ask AI:

```text
Review this project from a production-readiness perspective for a beginner. Do not edit files. Give me five practical risks, explain each in plain language, and suggest one small improvement I could make today.
```

Pick one suggestion and add it to your notes or README.

## Reflection

Fill this out:

```text
The quality gate I ran was:
The result was:
The production risk I understand better now is:
The next thing I would improve is:
```

## Checkpoint

You can explain why local success is the beginning of the work, not the finish line.
