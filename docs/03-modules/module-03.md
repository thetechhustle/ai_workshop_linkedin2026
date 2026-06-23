# Module 03 — AI Copilots and Agents

## Why this module matters

A lot of people use AI like a search box: they ask one question and copy the answer. Engineers need a stronger pattern. You want to give AI a role, enough context, clear boundaries, and a way to verify the work.

The slide deck explains the shift from “you ask, it answers” to “you assign, it executes.” That is agentic AI. The danger is giving an agent too much freedom before you understand the system. The skill is orchestration.

## Learning goals

By the end of this module, you should be able to:

1. Explain the difference between a co-pilot and an agent.
2. Break one large AI request into smaller roles.
3. Use AGENTS.md or CLAUDE.md to give project rules.
4. Ask AI for a plan before asking for edits.
5. Review AI output before trusting it.

## Co-pilot vs agent

| Pattern | What happens | Beginner-safe use |
|---|---|---|
| Co-pilot | You ask and it answers. | Explain code, summarize errors, suggest tests. |
| Agent | You assign and it may plan, edit, run tools, and report back. | Inspect repo, propose a plan, make a small approved change. |

## Agent roles

Instead of asking one giant prompt to do everything, assign one role at a time.

| Role | Job | Example prompt opening |
|---|---|---|
| Codebase Explorer | Explain what exists. | “Explain this repo structure like I am new.” |
| Planner | Propose the smallest safe plan. | “Suggest one small improvement and the files involved.” |
| Builder | Make a focused change. | “Implement only the approved change.” |
| Tester | Create or run a quality gate. | “What test proves this behavior works?” |
| Reviewer | Inspect the diff and risks. | “Review the diff for bugs and unnecessary changes.” |
| Ship Captain | Decide what must be true before release. | “What must be checked before this is public?” |

## The safe AI workflow

Use this sequence during the lab:

```text
1. Explain the project.
2. Propose one small plan.
3. Wait for approval.
4. Make the change.
5. Show the diff.
6. Run or recommend tests.
7. Summarize what changed.
```

## Project instruction files

This repo includes two instruction files:

- `AGENTS.md` for Codex-style project instructions.
- `CLAUDE.md` for Claude Code-style project instructions.

These files tell AI tools how to behave inside the project. They can include:

- setup commands,
- test commands,
- coding style,
- safety boundaries,
- what files not to touch,
- how to summarize changes.

## Beginner-safe prompt

Copy this during the workshop:

```text
You are my engineering coach. I am a beginner working in this repository. First explain the project structure, the entry point, and how to run the app. Then propose one small improvement. Do not edit files until I approve the plan. Include the test or quality check I should run.
```

## When to stop AI

Pause and ask for help if the AI:

- changes files you did not expect,
- deletes code without explaining why,
- suggests installing many new packages,
- skips tests,
- gives an answer you cannot explain,
- asks for private keys, tokens, passwords, or private data.

## Mini activity

Ask AI to play only the Codebase Explorer role. Your goal is not to change code yet. Your goal is to get a clear explanation.

After the answer, write:

- one file that seems important,
- one command that seems important,
- one question you still have.

## Checkpoint

You are ready when you can assign a task to the right agent role instead of asking one giant prompt to do everything.
