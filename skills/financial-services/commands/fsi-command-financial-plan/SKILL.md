---
name: fsi-command-financial-plan
description: Use when financial-services work requires build or update a financial
  plan.
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
    - financial-plan
    - financial-services
    - wealth-management
    related_skills: []
---

# FSI Command: /financial-plan

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/financial-plan` from `wealth-management`. Invoke it explicitly with `/skill fsi-command-financial-plan` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/financial-plan` or a financial plan financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `financial-plan` skill to create or update a comprehensive financial plan covering retirement, education, estate, and cash flow projections.

If a client name is provided, use it. Otherwise ask for client details.

## Hermes Invocation
- Explicit: `/skill fsi-command-financial-plan`
- Natural language: “Use the financial-plan command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
