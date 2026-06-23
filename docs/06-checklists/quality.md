# Quality Checklist

A quality gate is anything that helps you decide whether a change is safe enough to keep. In this workshop, the goal is not perfection. The goal is to build the habit of checking your work.

## Minimum quality gate

Run:

```bash
make test
```

A passing test does not prove the app is perfect. It proves the checked behaviors still work.

## Stronger quality gate

Run:

```bash
make lint
make test
make docs-build
```

Use this when you have time or when your change touches code and docs.

## Before you call a change done

Check each item:

- [ ] I can explain the goal of the change.
- [ ] I know which files changed.
- [ ] I inspected the diff with `git diff`.
- [ ] I ran `make test` or wrote down why I could not.
- [ ] I updated or added a test if behavior changed.
- [ ] I checked for unrelated AI-generated changes.
- [ ] I did not add private keys, tokens, passwords, or private data.
- [ ] I can explain what I would do next.

## Diff review questions

Before committing, ask:

1. Did the change solve the original goal?
2. Did it change more files than expected?
3. Are names readable?
4. Are errors handled clearly?
5. Is there a test, manual check, or written reason for confidence?

## Beginner test thinking

| Question | Example |
|---|---|
| What should work? | Creating an opportunity returns a new record. |
| What should fail clearly? | Looking up a missing opportunity returns 404. |
| What should not change? | Existing endpoints still respond. |

## AI review prompt

```text
Review this diff for a beginner. Look for correctness, readability, missing tests, and unexpected changes. Do not rewrite the project. Tell me whether this is safe to commit and what one small improvement I should make first.
```

## Commit readiness

You are ready to commit when you can say:

> I know what changed, why it changed, and what evidence I have that it still works.
