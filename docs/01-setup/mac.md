# Mac Setup

Most students will use a Mac. This guide keeps setup lightweight and explains what each tool is doing.

## The short version

You need four things:

1. **Git** to download and track code.
2. **Python** to run the workshop site and example API.
3. **make** to run simple commands like `make test` instead of memorizing long commands.
4. **tmux** if you want a terminal cockpit with multiple panes.

## Step 1 — Open Terminal

Press `Command + Space`, type `Terminal`, and press Enter.

Run:

```bash
pwd
```

You should see the folder your terminal is currently inside. `pwd` means “print working directory.” It answers: where am I?

## Step 2 — Install Apple command line tools

```bash
xcode-select --install
```

This gives your Mac basic developer tools. If your Mac says the tools are already installed, that is fine.

## Step 3 — Install Homebrew if needed

Check whether Homebrew is installed:

```bash
brew --version
```

If that command works, continue. If it does not work, ask the instructor or a TA before installing anything new.

## Step 4 — Install workshop tools

```bash
brew install git python tmux
```

Check the tools:

```bash
git --version
python3 --version
make --version
tmux -V
```

You do not need to memorize the version numbers. You only need to see that each command responds.

## Step 5 — Optional tools

These are helpful but not required for the main path:

```bash
brew install node
brew install --cask docker
```

- **Node.js** is useful for many JavaScript projects and some AI CLI tools.
- **Docker Desktop** is useful for the production-readiness demo, but the core workshop does not depend on it.

## Step 6 — AI tools

Use the AI tool LinkedIn or the instructor has approved. You can complete the core lab with browser-based ChatGPT or Claude if CLI access is not available.

Optional CLI installs, only when approved:

```bash
npm install -g @openai/codex
npm install -g @anthropic-ai/claude-code
```

If those commands fail, do not panic. The workshop has browser-based fallback prompts.

## Step 7 — Clone the workshop repo

```bash
git clone https://github.com/thetechhustle/ai_workshop_linkedin2026.git
cd ai_workshop_linkedin2026
make install
make test
make run
```

`make run` opens the workshop book at <http://127.0.0.1:8001>.

Later, when the lab calls for the example API:

```bash
make startapp
```

Open <http://127.0.0.1:8000/docs>.

## Common Mac issues

| Symptom | What to try |
|---|---|
| `brew: command not found` | Homebrew is not installed or not on your path. Ask for help before continuing. |
| `python3: command not found` | Run `brew install python`, then open a new terminal. |
| `make: command not found` | Run `xcode-select --install`, then open a new terminal. |
| Port already in use | Another app is using the same port. Try `PORT=8002 make startapp` or `DOCS_PORT=8003 make run`. |
| Permission error | Do not use `sudo` unless the instructor tells you. Ask for help first. |

## Checkpoint

You are ready when you can run:

```bash
make help
make test
```

and see a list of commands plus passing tests.
