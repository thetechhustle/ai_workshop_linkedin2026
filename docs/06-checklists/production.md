# Production Awareness Checklist

Production means real people can depend on the app. This workshop does not require every student to deploy. It does require every student to understand that shipping software is a responsibility.

Beginner version:

> Can people depend on this, and do we know what to do when it fails?

## Run and setup

- [ ] The README explains how to install dependencies.
- [ ] The README explains how to start the app.
- [ ] The app can be started from the terminal.
- [ ] The required Python or Node version is documented.
- [ ] Environment variables are listed in an example file.

## Data

- [ ] I know where data is stored.
- [ ] I know whether data is temporary or persistent.
- [ ] I know whether the app uses SQLite, PostgreSQL, Redis, MongoDB, or another store.
- [ ] I know what data should not be stored.

## Testing and quality

- [ ] There is at least one test or written manual check.
- [ ] The test command is documented.
- [ ] The lint or style command is documented.
- [ ] CI exists or there is a plan to add it.
- [ ] Someone reviewed the diff before merging.

## Security and privacy basics

- [ ] No passwords, tokens, private keys, or private data are committed.
- [ ] Secrets are loaded through environment variables or a secure system.
- [ ] Error messages do not expose private data.
- [ ] AI tools were not given private data unnecessarily.

## Web and networking

- [ ] I know the local URL.
- [ ] I know the port.
- [ ] I understand the difference between localhost and a public domain.
- [ ] I know whether the app uses HTTP or HTTPS.
- [ ] I understand that opening a public tunnel should be controlled and temporary during demos.

## Ownership and operations

- [ ] Someone owns the next fix if the app breaks.
- [ ] There is a rollback or undo plan.
- [ ] Logs or error output can be inspected.
- [ ] Dependencies are tracked in a package file.
- [ ] The next improvement is written down.

## For the starter app

| Question | Answer |
|---|---|
| How do I start the workshop book? | `make run` |
| How do I start the API? | `make startapp` |
| What local API URL do I open? | `http://127.0.0.1:8000/docs` |
| What port does the API use? | `8000` |
| What database is used? | SQLite |
| What quality gate can I run? | `make test` |
| What stronger gate can I run? | `make check` |

## Reflection

Write one sentence:

> Before people rely on my project, I need to improve ________ because ________.
