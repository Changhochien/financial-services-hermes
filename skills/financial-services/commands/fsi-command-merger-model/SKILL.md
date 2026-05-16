---
name: fsi-command-merger-model
description: Use when financial-services work requires build an accretion/dilution
  merger model.
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
    - merger-model
    related_skills: []
---

# FSI Command: /merger-model

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/merger-model` from `investment-banking`. Invoke it explicitly with `/skill fsi-command-merger-model` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/merger-model` or a merger model financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `merger-model` skill and build a merger consequences analysis.

If acquirer and target are provided, use them. Otherwise ask the user for deal details.

## Hermes Invocation
- Explicit: `/skill fsi-command-merger-model`
- Natural language: “Use the merger-model command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
