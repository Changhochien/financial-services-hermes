---
name: fsi-command-buyer-list
description: Use when financial-services work requires build a buyer universe for
  a sell-side process.
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
    - buyer-list
    - command
    - financial-services
    - investment-banking
    related_skills: []
---

# FSI Command: /buyer-list

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/buyer-list` from `investment-banking`. Invoke it explicitly with `/skill fsi-command-buyer-list` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/buyer-list` or a buyer list financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `buyer-list` skill and build a universe of potential strategic and financial acquirers.

If a company or sector is provided, use it. Otherwise ask the user for the target company details.

## Hermes Invocation
- Explicit: `/skill fsi-command-buyer-list`
- Natural language: “Use the buyer-list command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
