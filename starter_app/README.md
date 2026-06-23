# Opportunity Tracker API

A small FastAPI and SQLite app for the LinkedIn AI Workshop.

Students can use this when they do not have a project ready or when the room needs a common lab environment.

## What it tracks

- internships,
- project ideas,
- mentors,
- campus organizations,
- deadlines,
- next actions.

## Run from repo root

```bash
make install
make startapp
```

You can also use the alias:

```bash
make example-app
```

Open <http://127.0.0.1:8000/docs>.

## Workshop book

From the repo root, `make run` starts the MkDocs workshop book at <http://127.0.0.1:8001>.

## Run tests

```bash
make test
```

## API endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/health` | Check if the app is alive. |
| GET | `/opportunities` | List opportunities. |
| POST | `/opportunities` | Create an opportunity. |
| GET | `/opportunities/{id}` | Fetch one opportunity. |
| PATCH | `/opportunities/{id}/status` | Update status. |

## Extension ideas

- Add a `priority` field.
- Add a `category` field.
- Add a due-soon filter.
- Add a delete endpoint.
- Add a README section explaining how the app works.
