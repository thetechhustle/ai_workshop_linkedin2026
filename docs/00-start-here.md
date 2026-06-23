# Start Here

Welcome in. This is the page you open when you first sit down.

## The only commands you need at first

```bash
git clone https://github.com/thetechhustle/ai_workshop_linkedin2026.git
cd ai_workshop_linkedin2026
make install
make test
make run
```

`make run` starts the workshop book. Open <http://127.0.0.1:8001>.

When it is time to start the example app, run:

```bash
make startapp
# or
make example-app
```

Then open the API docs at <http://127.0.0.1:8000/docs>.

## How to use this repo

| Area | Why it exists |
|---|---|
| `docs/` | The workshop book: modules, labs, checklists, and resources. |
| `starter_app/` | A small FastAPI + SQLite app you can inspect and improve. |
| `templates/` | Copy/paste project instruction files and review templates. |
| `slides/` | Bobby D's AI Workshop presenter notes. |
| `Makefile` | One-command workflow so you do not memorize everything. |

## The rules of the room

- Ask questions early.
- Copy commands carefully.
- Do not paste secrets into AI tools.
- Do not let AI change a project before you understand the plan.
- Every error message is evidence. Do not panic. Inspect it.

## Your win condition

Pick your path:

- **Bronze:** clone the repo, open the workshop book, run the app, and explain what it does.
- **Silver:** make one small change and verify it.
- **Gold:** add a test, Docker step, CI edit, or production-readiness note.
