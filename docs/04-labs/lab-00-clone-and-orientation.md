# Lab 00 — Clone and Orientation

## Goal

Get the repo on your laptop, install dependencies, run tests, and open the workshop book. This lab is about proving that your environment is ready.

## Time box

15-20 minutes.

## Before you start

You need:

- a Mac laptop,
- Terminal open,
- Git installed,
- internet access,
- a GitHub account is helpful but not required just to clone this public repo.

## Step 1 — Clone the repo

```bash
git clone https://github.com/thetechhustle/ai_workshop_linkedin2026.git
```

What this does: downloads the workshop files to your laptop.

If it says the folder already exists, you probably cloned it already. Move into it:

```bash
cd ai_workshop_linkedin2026
```

## Step 2 — Move into the project

```bash
cd ai_workshop_linkedin2026
```

Check where you are:

```bash
pwd
ls
```

You should see files like `README.md`, `Makefile`, `docs`, and `starter_app`.

## Step 3 — Install dependencies

```bash
make install
```

This creates a local Python environment and installs the tools for the workshop site and example app. The first install can take a few minutes.

## Step 4 — Run tests

```bash
make test
```

You should see output ending with something like:

```text
4 passed
```

If tests fail, do not panic. Copy the last 10 lines of the error and ask for help.

## Step 5 — Start the workshop book

```bash
make run
```

Open <http://127.0.0.1:8001>.

This starts the documentation site, not the example app. Keep it running in this terminal tab.

## Step 6 — Start the example app when asked

Open a second terminal tab, move into the repo again, and run:

```bash
cd ai_workshop_linkedin2026
make startapp
```

Open <http://127.0.0.1:8000/docs>.

You should see interactive API docs for the Opportunity Tracker app.

## What to write in your notes

Answer these in your own words:

1. What does this repository contain?
2. What command starts the workshop book?
3. What command starts the example app?
4. What command runs tests?
5. What URL opens the API docs?

## Bronze, Silver, Gold

| Level | Completion target |
|---|---|
| Bronze | I cloned the repo, ran `make test`, and opened the workshop book. |
| Silver | I also started the example app and opened `/docs`. |
| Gold | I can explain what `make install`, `make test`, `make run`, and `make startapp` do. |

## Troubleshooting

| Problem | Try this |
|---|---|
| `git: command not found` | Install Git with Homebrew or ask for help. |
| `make: command not found` | Run `xcode-select --install`. |
| `Address already in use` | Try `DOCS_PORT=8003 make run` or `PORT=8002 make startapp`. |
| Browser does not open | Copy and paste the local URL manually. |

## Explain it back

Why are we using a repository instead of only slides?

A strong answer sounds like: “Because the repo lets us read, run, test, and change a real project while keeping the course materials in one place.”
