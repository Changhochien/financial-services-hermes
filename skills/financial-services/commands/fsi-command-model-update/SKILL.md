---
name: fsi-command-model-update
description: Use when financial-services work requires update a financial model with
  new data.
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
    - model-update
    related_skills: []
---

# FSI Command: /model-update

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/model-update` from `equity-research`. Invoke it explicitly with `/skill fsi-command-model-update` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/model-update` or a model update financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `model-update` skill and plug in new earnings, guidance, or revised assumptions.

If a ticker is provided, use it. Otherwise ask the user which model to update and what changed.

## Hermes Invocation
- Explicit: `/skill fsi-command-model-update`
- Natural language: “Use the model-update command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
