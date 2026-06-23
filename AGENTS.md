# AGENTS.md

## Mission

Help students improve this repository while learning the engineering concept underneath the change.

This workshop is CLI-first, beginner-aware, and culture-forward. Optimize for clarity, small safe changes, student confidence, and verification.

## Student context

Assume many students are early in their engineering journey. Some may have personal projects. Some may only have class assignments or app ideas. Explain concepts plainly and keep changes small enough that a student can describe them back.

## Working agreement

1. Explain the current structure before editing.
2. Propose a small plan before making multi-file changes.
3. Name the files you expect to touch.
4. Make the smallest useful change.
5. Run or recommend the relevant quality gate.
6. Summarize the diff in plain language.
7. Do not hide errors. Error messages are learning artifacts.

## Commands

- Install everything: `make install`
- Serve workshop book: `make run`
- Run starter app: `make startapp`
- Run tests: `make test`
- Run lint: `make lint`
- Run full check: `make check`
- Serve course site: `make serve`

## Code standards

- Prefer readable code over clever code.
- Use descriptive names.
- Keep functions small.
- Follow the existing project structure.
- Add or update tests when behavior changes.
- Do not introduce a new framework without explaining why.
- Avoid broad rewrites during workshop labs.

## Documentation standards

- Write for beginners first.
- Define jargon before using it heavily.
- Include commands students can copy.
- Explain what each command proves.
- Include checkpoints and reflection questions.
- Provide Bronze, Silver, and Gold paths when possible.

## Safety boundaries

- Do not commit credentials or private student data.
- Do not delete files unless explicitly asked.
- Do not make production deployment changes.
- Do not publish SOW/proposal/private business docs.
- Do not assume every student has paid AI tool access; keep fallback paths available.

## Preferred response pattern

When helping with this repo, respond with:

1. What I inspected.
2. What I plan to change.
3. What changed.
4. How to verify it.
5. What the student should understand.
