# Module 04 — Production Readiness

## Why this module matters

A project is stronger when it can be run, tested, reviewed, and explained. “It works on my laptop” is a good start, but engineering teams need more than that. They need to know how the app runs, where data lives, how changes are checked, and what could break when real users depend on it.

This module gives you production vocabulary without trying to turn one afternoon into a full DevOps course.

## Learning goals

By the end of this module, you should be able to:

1. Explain localhost and ports in plain language.
2. Explain what a database does.
3. Explain why containers help projects run consistently.
4. Explain what CI checks before code merges.
5. Name one thing your project needs before people depend on it.

## Localhost and ports

When you run the example app with:

```bash
make startapp
```

it starts a service on your own laptop. You open it at:

```text
http://127.0.0.1:8000/docs
```

Breakdown:

| Piece | Meaning |
|---|---|
| `http` | The browser/API communication protocol. |
| `127.0.0.1` | Your own machine. This is localhost. |
| `8000` | The port where the API is listening. |
| `/docs` | The path for the interactive API docs. |

The workshop book runs separately on port `8001`:

```bash
make run
```

## Databases without fear

A database stores information so the app can remember it after a request ends.

| Database | Plain-English version | Good first use |
|---|---|---|
| SQLite | A small database in one local file. | Prototypes and workshops. |
| PostgreSQL | A serious relational database. | Real apps with users and growth. |
| Redis | A fast memory-based store. | Caches, sessions, queues. |
| MongoDB | A document database. | Flexible JSON-like records. |

The starter app uses SQLite because it is simple and local. That is the right tool for learning.

## Containers in one paragraph

A container packages an app and its dependencies so it can run more consistently across machines. The beginner question is not “Can I master Docker today?” The beginner question is:

> Can someone else run this project the same way I did?

That is why this repo includes `starter_app/Dockerfile` as a teaching artifact.

## CI in one paragraph

CI means continuous integration. In GitHub, a workflow can run checks automatically when code changes. That can include tests, lint checks, docs builds, or other quality gates.

The beginner question is:

> What should GitHub check before this change is trusted?

## Production-readiness checklist

Before real users depend on an app, ask:

- Can someone else install and run it?
- Are required environment variables documented?
- Is there a test or review checklist?
- Do we know where data is stored?
- Do we know what port the app uses?
- Do we know how to restart it?
- Do we know what to do if it fails?

## Mini activity

With the example app running, answer:

1. What URL opens the API docs?
2. What port is the app using?
3. What database does the app use?
4. What command runs tests?
5. What would you want to check before sharing this app with someone else?

## Checkpoint

You are ready when you can explain why local success is only the beginning and name one quality gate your project should have.
