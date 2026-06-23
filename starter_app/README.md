# Opportunity Tracker API

A small FastAPI and SQLite app for the LinkedIn AI Workshop.

Students can use this when they do not have a personal project ready or when the room needs a common lab environment. The app is intentionally small so you can understand it in one workshop.

## What problem does it solve?

Students often track opportunities in messy notes: internships, project ideas, mentors, campus organizations, deadlines, and next actions. This API gives us a simple way to store and update those opportunities.

## What you will learn from it

| Concept | Where it appears |
|---|---|
| API endpoints | `starter_app/src/opportunity_tracker/app.py` |
| Data models | `starter_app/src/opportunity_tracker/models.py` |
| SQLite database access | `starter_app/src/opportunity_tracker/db.py` |
| Tests | `starter_app/tests/test_api.py` |
| Container packaging | `starter_app/Dockerfile` |

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

## Try the API in your browser

After running `make startapp`, open <http://127.0.0.1:8000/docs>.

Try this flow:

1. Run `GET /health`.
2. Run `POST /opportunities` with a new opportunity.
3. Run `GET /opportunities` to see the saved item.
4. Run `PATCH /opportunities/{id}/status` to update it.
5. Run `GET /opportunities/{id}` to confirm the update.

## Example opportunity JSON

```json
{
  "title": "Apply for summer internship",
  "source": "LinkedIn",
  "status": "idea",
  "deadline": "2026-07-15",
  "notes": "Ask mentor to review resume first."
}
```

## How the app works

Plain-English flow:

```text
Browser/API docs -> FastAPI route -> Pydantic model -> SQLite helper -> local database file
```

When you create an opportunity:

1. FastAPI receives the request.
2. Pydantic checks the input shape.
3. The database helper inserts a row into SQLite.
4. The API returns the saved opportunity as JSON.

## Extension ideas

Pick only one during the workshop:

- Add a `priority` field.
- Add a `category` field.
- Add a due-soon filter.
- Add a delete endpoint.
- Add a README section explaining how the app works.
- Add a test for a missing or invalid status.

## Beginner-safe AI prompt

```text
You are my engineering coach. Explain how this FastAPI app works, including the route file, model file, database file, and test file. Do not edit files. Then suggest one small improvement that a beginner can understand.
```

## What to verify after any change

```bash
make test
git diff
```

If you can explain the diff and the tests pass, you are moving like an engineer.
