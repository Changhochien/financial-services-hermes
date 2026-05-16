---
name: fsi-command-tlh
description: Use when financial-services work requires identify tax-loss harvesting
  opportunities.
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
    - tlh
    - wealth-management
    related_skills: []
---

# FSI Command: /tlh

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/tlh` from `wealth-management`. Invoke it explicitly with `/skill fsi-command-tlh` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/tlh` or a tlh financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `tax-loss-harvesting` skill to scan taxable accounts for harvestable losses, suggest replacement securities, and manage wash sale windows.

If a client or account is provided, use it. Otherwise ask for the portfolio to scan.

## Hermes Invocation
- Explicit: `/skill fsi-command-tlh`
- Natural language: “Use the tlh command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
