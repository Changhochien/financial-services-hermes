---
name: fsi-command-initiate
description: Use when financial-services work requires create an initiating coverage
  report.
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
    - equity-research
    - financial-services
    - initiate
    related_skills: []
---

# FSI Command: /initiate

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/initiate` from `equity-research`. Invoke it explicitly with `/skill fsi-command-initiate` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/initiate` or a initiate financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `initiating-coverage` skill and begin the 5-task workflow to create an institutional-quality initiation report.

If a ticker is provided, use it. Otherwise ask the user which company to initiate on.

## Hermes Invocation
- Explicit: `/skill fsi-command-initiate`
- Natural language: “Use the initiate command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
