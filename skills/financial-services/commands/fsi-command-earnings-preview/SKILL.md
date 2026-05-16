---
name: fsi-command-earnings-preview
description: Use when financial-services work requires build a pre-earnings preview
  with scenarios.
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
    - earnings-preview
    - equity-research
    - financial-services
    related_skills: []
---

# FSI Command: /earnings-preview

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/earnings-preview` from `equity-research`. Invoke it explicitly with `/skill fsi-command-earnings-preview` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/earnings-preview` or a earnings preview financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `earnings-preview` skill and build a pre-earnings analysis with consensus estimates, key metrics to watch, and bull/base/bear scenarios.

If a ticker is provided, use it. Otherwise ask the user which company is reporting.

## Hermes Invocation
- Explicit: `/skill fsi-command-earnings-preview`
- Natural language: “Use the earnings-preview command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
