---
name: fsi-command-returns
description: Use when financial-services work requires build IRR/MOIC sensitivity
  tables.
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
    - financial-services
    - private-equity
    - returns
    related_skills: []
---

# FSI Command: /returns

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/returns` from `private-equity`. Invoke it explicitly with `/skill fsi-command-returns` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/returns` or a returns financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `returns-analysis` skill and model PE returns with sensitivity across entry multiple, leverage, exit multiple, and growth scenarios.

If deal parameters are provided, use them. Otherwise ask the user for entry EBITDA, valuation, and financing assumptions.

## Hermes Invocation
- Explicit: `/skill fsi-command-returns`
- Natural language: “Use the returns command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
