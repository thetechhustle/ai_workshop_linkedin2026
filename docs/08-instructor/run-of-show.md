# Instructor Run of Show

This page is for Bobby D and any support team helping in the room. The audience is rising freshmen and early-career student engineers, so the delivery should protect confidence while still making the work feel real.

## Teaching stance

Lead with energy, but keep the technical steps grounded. The students should feel:

- welcomed,
- not judged for gaps,
- encouraged to ask questions,
- challenged to verify AI output,
- proud when they get a small thing working.

## Before students arrive

- Open the slide notes.
- Clone repo fresh.
- Run `make install`.
- Run `make test`.
- Run `make run` and open the workshop book.
- Run `make startapp` in another terminal when you need the local API.
- Open the local API docs.
- Confirm room Wi-Fi and projection.
- Confirm whether students have browser AI access, CLI agent access, or both.
- Decide whether Docker and deployment concepts will be demo-only or student stretch work.

## Opening script

Use this framing:

> We are no longer coding alone. But that does not mean we stop learning. Today you are going to practice how to guide AI, inspect what it gives you, verify the result, and explain your work like an engineer.

Then set expectations:

- You do not need to know everything today.
- You do need to ask questions.
- You do need to verify before trusting.
- Your win is one controlled next step.

## Live flow

| Segment | Instructor move | Watch for |
|---|---|---|
| Opening | Connect the slide deck to the repo. | Students may think this is only a motivational talk. Move quickly into hands-on work. |
| Setup | Have students clone, install, test, and run docs. | Installation errors. Pair students quickly. |
| Terminal | Normalize `pwd`, `ls`, `cd`, `make help`, `git status`. | Students hiding errors because they feel embarrassed. |
| Git | Demonstrate branch, diff, test, commit. | Students committing before reading the diff. |
| AI workflow | Show plan-first prompting. | Students asking AI to build everything at once. |
| Triage | Use the starter app if personal projects are not ready. | Students stuck deciding what to improve. Give them a menu. |
| Build | Keep changes small. | AI making broad changes. Stop and narrow the plan. |
| Quality | Run tests and review checklists. | Students thinking tests are only for advanced engineers. |
| Production | Keep vocabulary beginner-friendly. | Too much Docker/CI depth can overwhelm the room. |
| Showcase | Ask for what changed, verified, and comes next. | Celebrate small wins loudly. |

## Suggested language for common moments

When students are nervous:

> You are not behind. You are learning the real workflow.

When AI gives too much code:

> We are going to slow the tool down. First explain, then plan, then build.

When tests fail:

> This is useful. The system is talking to us. Let’s read what it says.

When students finish early:

> Move to Gold: add a test, improve docs, or explain one production risk.

## Support strategy

Use three lanes:

| Lane | Student signal | Facilitator move |
|---|---|---|
| Bronze | “I am still setting up.” | Help them run docs and app. Skip stretch work. |
| Silver | “I can run it and want to change it.” | Guide one small change and test. |
| Gold | “I finished the main lab.” | Send them to quality, Docker, CI, or production checklist. |

## Close

Ask every student or group:

- What did you change or understand?
- How did you verify it?
- What is one thing you still need to learn?
- What is your next step this week?

End with:

> Do not chase the tool. Chase the skill. Tools change. Skill compounds.
