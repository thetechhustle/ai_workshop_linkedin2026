# Prompt Library

Use this structure: role, context, task, constraints, verification.

## Triage

Ask the assistant to inspect the project, explain the entry point, database layer, tests, and one small improvement. Ask it not to edit files until the plan is clear.

## Change plan

Ask for a small safe plan, the files likely to change, and the test that should be added.

## Review

Ask for review feedback on correctness, readability, and missing tests.

## Reflection

Ask for a summary of what changed, what was verified, and what to learn next.
