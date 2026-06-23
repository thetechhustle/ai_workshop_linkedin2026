# Student-Friendly Engineering Glossary

Use this page when a word sounds familiar but still feels fuzzy. You are not expected to memorize everything today. You are expected to recognize the words and know where to look them up.

## AI terms

| Term | Beginner explanation | Workshop example |
|---|---|---|
| AI co-pilot | A tool that helps you think, code, debug, or explain. You still drive. | Asking ChatGPT to explain a file before you edit it. |
| Agent | AI that can plan steps, use tools, take actions, and report back. | Asking a coding agent to inspect the repo, propose a plan, and run tests. |
| Prompt | The instruction you give the AI. | “Explain this project structure before making changes.” |
| Context | The information the AI needs to answer well. | The repo files, goal, constraints, and test command. |
| Verification | Evidence that the AI output works or makes sense. | Tests pass, diff is reviewed, docs match the behavior. |
| Guardrail | A rule that keeps AI from going too far. | “Do not edit files until I approve the plan.” |

## Terminal and project terms

| Term | Beginner explanation | Workshop example |
|---|---|---|
| Terminal | A text interface for running commands. | Running `make test`. |
| Shell | The program inside your terminal that reads commands. | zsh on most modern Macs. |
| Command | A line of text that asks your computer to do something. | `git status`. |
| Directory | A folder. | `docs/` or `starter_app/`. |
| Path | The address of a file or folder. | `starter_app/src/opportunity_tracker/app.py`. |
| tmux | A terminal cockpit that lets you keep multiple panes open. | One pane for docs, one for app, one for tests, one for Git. |
| Makefile | A file that stores shortcuts for common commands. | `make run` starts the workshop book. |

## Git and GitHub terms

| Term | Beginner explanation | Workshop example |
|---|---|---|
| Git | Version control. It tracks changes over time. | Seeing which files changed after AI edits. |
| GitHub | A website for hosting and reviewing Git repositories. | Sharing a project with classmates or reviewers. |
| Repository | A project folder tracked by Git. | This workshop repo. |
| Branch | A safe workspace for changes before they merge. | `lab/my-small-change`. |
| Diff | The exact lines that changed. | Reading `git diff` before committing. |
| Commit | A saved checkpoint with a message. | `Add status update test`. |
| Pull request | A proposed change for review. | Asking teammates to review your branch. |
| CI | Continuous integration. Automatic checks that run in GitHub. | GitHub Actions running tests after a push. |

## App and web terms

| Term | Beginner explanation | Workshop example |
|---|---|---|
| API | A way for software to talk to software. | The Opportunity Tracker API. |
| Endpoint | A specific API path. | `/health` or `/opportunities`. |
| Request | A message sent to an API. | Browser asks `GET /health`. |
| Response | What the API sends back. | `{ "status": "ok" }`. |
| Localhost | Your own computer, usually reached at `127.0.0.1`. | `http://127.0.0.1:8000/docs`. |
| Port | A numbered door where a service listens. | `8000` for the API and `8001` for docs. |
| HTTP | The protocol browsers and APIs use to communicate. | `http://127.0.0.1:8000`. |
| HTTPS | HTTP with encryption. | Most public websites use HTTPS. |

## Database and production terms

| Term | Beginner explanation | Workshop example |
|---|---|---|
| Database | A place where an app stores data. | Opportunities saved by the API. |
| SQLite | A lightweight database stored in a local file. | Great for this workshop and prototypes. |
| PostgreSQL | A production-grade relational database. | Useful when apps have more users and data. |
| Redis | A fast in-memory key-value store. | Useful for caching and queues. |
| MongoDB | A document database for JSON-like data. | Useful for flexible document-style apps. |
| Container | A packaged app environment that runs consistently. | Docker can run the API in a repeatable way. |
| Dockerfile | Instructions for building a container image. | `starter_app/Dockerfile`. |
| Quality gate | A test, lint check, review, or checklist that protects the project. | `make test` before a commit. |
| Production | The real environment users depend on. | A public app with real users. |

## Phrase to remember

> A project is stronger when someone else can run it, test it, understand it, and safely improve it.
