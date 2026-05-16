---
name: fsi-command-debug-model
description: Use when financial-services work requires debug and audit a financial
  model for errors.
version: 0.1.0
author: Changhochien
license: MIT
platforms:
- linux
- macos
- windows
metadata:
  hermes:
    tags:
    - command
    - debug-model
    - financial-analysis
    - financial-services
    related_skills: []
---

# FSI Command: /debug-model

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/debug-model` from `financial-analysis`. Invoke it explicitly with `/skill fsi-command-debug-model` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/debug-model` or a debug model financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `audit-xls` skill with scope **model** and audit the specified financial model for broken formulas, balance sheet imbalances, hardcoded overrides, circular references, and logic errors — including the full model-integrity checks (BS balance, cash tie-out, roll-forwards, model-type-specific bugs).

If a file path is provided, use it. Otherwise ask the user for the model to review.

## Hermes Invocation
- Explicit: `/skill fsi-command-debug-model`
- Natural language: “Use the debug-model command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
