# Prompt Library

Prompts are instructions. A strong prompt gives the AI a role, context, task, constraints, and a verification step.

```text
Role + Context + Task + Constraints + Verification
```

## Prompt safety rules

Before using any AI tool:

- Do not paste passwords, tokens, private keys, private student data, or internal company information.
- Ask for explanation before edits.
- Ask for a small plan before a big change.
- Keep the AI focused on one job at a time.
- Verify output with tests, docs, or human review.

## 1. Codebase explorer

Use this before changing files.

```text
You are my engineering coach. I am new to this repository. Explain the project structure, the main entry point, how the app runs, where data is stored, and where tests live. Do not edit files. Use beginner-friendly language and end with three questions I should be able to answer.
```

## 2. Small change planner

Use this when you are ready to choose a safe improvement.

```text
Suggest one small improvement for this project that a beginner can understand. Do not edit files yet. Explain why the change is useful, which files would likely change, what could break, and what test or quality check I should run.
```

## 3. Builder prompt

Use this only after you understand and approve the plan.

```text
Implement only the approved change. Keep the change small. Do not add new dependencies unless you explain why they are necessary. After editing, summarize the files changed and tell me the exact command to verify the work.
```

## 4. Test helper

Use this when behavior changes.

```text
Help me add or improve one test for this behavior. First explain what the test should prove. Then show the smallest test change. Do not rewrite unrelated tests.
```

## 5. Error explainer

Use this when a command fails.

```text
Explain this error in beginner-friendly language. Tell me what command failed, what the error likely means, and the smallest next step to investigate. Do not suggest a large rewrite.
```

Paste the error below the prompt.

## 6. Diff reviewer

Use this before committing.

```text
Review this diff for correctness, readability, missing tests, and unexpected changes. Do not rewrite the project. Give me a short list of issues, then tell me whether the change is safe to commit.
```

## 7. Production-readiness reviewer

Use this near the end of the workshop.

```text
Review this project from a production-readiness perspective for a beginner. Do not edit files. Explain five practical risks in plain language and suggest one small improvement I can make today.
```

## 8. Reflection prompt

Use this to close your lab.

```text
Summarize what I changed, what I verified, what I still do not understand, and what I should learn next. Keep it concise and beginner-friendly.
```

## Prompt patterns by role

| Role | Use when | Starter phrase |
|---|---|---|
| Explorer | You are new to the repo. | “Explain the structure before edits.” |
| Planner | You need a safe path. | “Propose the smallest useful change.” |
| Builder | You approved the plan. | “Implement only the approved change.” |
| Tester | Behavior changed. | “What test proves this works?” |
| Reviewer | Before commit. | “Review this diff and risks.” |
| Ship Captain | Before sharing. | “What must be true before users depend on this?” |

## Weak prompt vs strong prompt

Weak:

```text
Fix this app.
```

Strong:

```text
You are my engineering coach. This is a beginner workshop project. Explain the issue, propose the smallest safe fix, wait for approval before editing, and include the command I should run to verify the change.
```

The strong prompt keeps you in control.
