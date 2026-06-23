# Module 01 — The AI-Era Engineer

## Why this module matters

AI can generate code quickly, but speed without judgment creates messy projects. This workshop starts with the mindset shift: the future engineer is not only someone who writes syntax. The future engineer can understand a system, communicate clearly with tools and teammates, verify output, and decide what should ship.

The slide deck opens with the line “We are no longer coding alone” and frames engineers as orchestrators. That is the core idea for this module.

## Learning goals

By the end of this module, you should be able to:

1. Explain why AI is a co-pilot, not a shortcut.
2. Describe the difference between asking AI to do work and using AI to learn work.
3. Name the five parts of the AI engineer loop.
4. Explain why verification matters before trusting generated code.

## The AI engineer loop

```text
Understand -> Plan -> Build -> Verify -> Ship Mindfully
```

| Step | Student version | Example question |
|---|---|---|
| Understand | What is this project and how does it run? | “Explain the folder structure and entry point.” |
| Plan | What is the smallest useful change? | “Suggest one safe improvement and the files involved.” |
| Build | Make the change carefully. | “Add this field without changing unrelated behavior.” |
| Verify | Prove it works. | “What test should I run? What could break?” |
| Ship Mindfully | Think beyond your laptop. | “What would need to be true before users depend on this?” |

## Key idea: AI predicts, engineers decide

A language model predicts likely output based on your prompt and context. That can be powerful, but it can also be wrong, incomplete, or overconfident. Your job is to guide it and check it.

A strong student prompt sounds like:

```text
You are my engineering coach. I am new to this repo. Explain the project structure and the main entry point. Do not edit files yet. After explaining, suggest one small safe improvement and the test I should run.
```

A weaker prompt sounds like:

```text
Build the whole thing for me.
```

The first prompt keeps you in the driver’s seat. The second prompt gives up too much control.

## Discussion prompt

Write a one-sentence answer:

> What does “engineers are becoming orchestrators” mean to me?

Then share with a partner. Keep it simple. You are trying to build language for the idea, not sound perfect.

## Mini activity

Open the repo root and run:

```bash
make help
```

Find three commands that look important. Write what you think each one does before you run it.

## Checkpoint

You are ready for the next module when you can explain:

- why AI can help you move faster,
- why AI output still needs review,
- why “I understand and verified this” is stronger than “AI wrote this.”
