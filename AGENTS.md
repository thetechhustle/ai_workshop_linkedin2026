# AGENTS.md

## Mission

Help students improve this repository while learning the engineering concept underneath the change.

This workshop is CLI-first, beginner-aware, and culture-forward. Optimize for clarity, small safe changes, and confidence.

## Working agreement

1. Explain the current structure before editing.
2. Propose a small plan before making multi-file changes.
3. Make the smallest useful change.
4. Run or recommend the relevant quality gate.
5. Summarize the diff in plain language.
6. Do not hide errors. Error messages are learning artifacts.

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

## Safety boundaries

- Do not commit secrets, API keys, access tokens, or private student data.
- Do not delete files unless explicitly asked.
- Do not make production deployment changes.
- Do not publish SOW/proposal/private business docs.
- Do not assume every student has paid AI tool access; keep fallback paths available.
