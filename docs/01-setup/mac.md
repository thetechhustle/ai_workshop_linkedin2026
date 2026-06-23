# Mac Setup

Most students will be on a Mac. This path keeps setup lightweight.

## Required

```bash
xcode-select --install
```

If you have Homebrew:

```bash
brew install git python tmux
```

Check your tools:

```bash
git --version
python3 --version
make --version
tmux -V
```

## Optional but helpful

```bash
brew install node
brew install --cask docker
```

Docker is optional for the main lab. It is useful for the production-readiness demo.

## AI tools

Use the tool LinkedIn or your instructor has approved. You can complete the core lab with browser-based ChatGPT or Claude if CLI access is not available.

Optional CLI installs, only when approved:

```bash
npm install -g @openai/codex
npm install -g @anthropic-ai/claude-code
```

## Workshop repo

```bash
git clone https://github.com/thetechhustle/ai_workshop_linkedin2026.git
cd ai_workshop_linkedin2026
make install
make test
```
