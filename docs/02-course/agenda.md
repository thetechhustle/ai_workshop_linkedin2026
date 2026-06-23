# 4-Hour Workshop Agenda

This agenda is designed for rising freshmen and early-career student engineers. The pacing assumes mixed experience: some students may have personal projects, some may only have class assignments, and some may be running a local API for the first time.

## Big picture

The workshop has one promise:

> You will leave knowing how to use AI to understand, improve, and verify a project without giving up your own engineering judgment.

## Agenda

| Time | Segment | What happens | Student checkpoint |
|---:|---|---|---|
| 0:00-0:15 | Opening | Frame AI as a learning accelerator, not a shortcut. Introduce the loop: Understand, Plan, Build, Verify, Ship Mindfully. | I know why we are using a repo and not just slides. |
| 0:15-0:35 | Repo orientation | Clone the repo, install dependencies, run tests, and start the workshop book with `make run`. | I can open the course locally. |
| 0:35-0:55 | Terminal cockpit | Explain Terminal, tmux, panes, `pwd`, `ls`, `cd`, `make help`, and how to keep app/tests/Git visible. | I can move around the project without panic. |
| 0:55-1:20 | Git workflow | Create a branch, inspect status, read a diff, and explain why controlled change matters. | I can tell what changed before I commit. |
| 1:20-1:45 | AI workflow demo | Show how to ask AI to inspect a project, propose a plan, and wait before editing. | I can ask AI for a plan instead of a mystery code dump. |
| 1:45-2:00 | Break / checkpoint | Reset machines, catch up, and help anyone stuck. | I know my current status: ready, stuck, or need a partner. |
| 2:00-2:35 | Project triage | Run the example app or a student project, inspect structure, find entry point, identify one small improvement. | I can explain what the project does. |
| 2:35-3:10 | Build lab | Make a small change: feature, bug fix, refactor, or documentation improvement. | I have a small change I can explain. |
| 3:10-3:35 | Quality gates | Run tests, lint, review checklists, and use AGENTS.md / CLAUDE.md to define project standards. | I have evidence that my change is safe enough to discuss. |
| 3:35-3:50 | Production awareness | Explain localhost, ports, databases, containers, CI/CD, and deployment as responsibility. | I understand why local success is not the finish line. |
| 3:50-4:00 | Showcase | Students share what changed, what they verified, and what they will do next. | I can explain my next step. |

## Instructor pacing notes

If the room is nervous, slow down during setup and Git. If the room is advanced, use the starter app as the shared baseline and let stronger students take Gold stretch challenges.

Do not force every student to reach Docker, CI, or deployment. Every student should leave with one controlled next step.

## Student outcome levels

| Level | Best for | Outcome |
|---|---|---|
| Bronze | Newer students | Run the repo, open the app, explain the structure. |
| Silver | Students with some coding experience | Make one small change and verify it. |
| Gold | Stronger or returning students | Improve a test, workflow, Docker note, or production-readiness checklist. |

## What to say when students are overwhelmed

You are not behind. You are learning the real workflow. Real engineers also read docs, run commands twice, search error messages, and ask teammates for help. The skill is not avoiding confusion. The skill is knowing how to move through it.
