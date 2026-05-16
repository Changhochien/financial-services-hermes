---
name: fsi-command-thesis
description: Use when financial-services work requires create or update an investment
  thesis.
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
    - thesis
    related_skills: []
---

# FSI Command: /thesis

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/thesis` from `equity-research`. Invoke it explicitly with `/skill fsi-command-thesis` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/thesis` or a thesis financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `thesis-tracker` skill to create a new thesis or update an existing one with new data points.

If a ticker is provided, use it. Otherwise ask the user which position to review.

## Hermes Invocation
- Explicit: `/skill fsi-command-thesis`
- Natural language: “Use the thesis command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
