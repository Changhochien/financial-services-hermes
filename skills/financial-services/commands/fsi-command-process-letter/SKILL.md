---
name: fsi-command-process-letter
description: Use when financial-services work requires draft a process letter or bid
  instructions.
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
    - investment-banking
    - process-letter
    related_skills: []
---

# FSI Command: /process-letter

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/process-letter` from `investment-banking`. Invoke it explicitly with `/skill fsi-command-process-letter` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/process-letter` or a process letter financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `process-letter` skill and draft process correspondence.

If a letter type is specified (IOI, final bid, management meeting invite), use it. Otherwise ask the user what stage the process is in.

## Hermes Invocation
- Explicit: `/skill fsi-command-process-letter`
- Natural language: “Use the process-letter command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
