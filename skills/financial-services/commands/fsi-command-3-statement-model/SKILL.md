---
name: fsi-command-3-statement-model
description: Use when financial-services work requires fill out a 3-statement financial
  model template.
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
    - 3-statement-model
    - command
    - financial-analysis
    - financial-services
    related_skills: []
---

# FSI Command: /3-statement-model

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/3-statement-model` from `financial-analysis`. Invoke it explicitly with `/skill fsi-command-3-statement-model` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/3-statement-model` or a 3 statement model financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `3-statement-model` skill and populate a 3-statement financial model (Income Statement, Balance Sheet, Cash Flow Statement).

If a file path is provided, use it as the template. Otherwise ask the user for their model template.

## Hermes Invocation
- Explicit: `/skill fsi-command-3-statement-model`
- Natural language: “Use the 3-statement-model command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
