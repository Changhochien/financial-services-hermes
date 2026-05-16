---
name: fsi-command-deal-tracker
description: Use when financial-services work requires track and review live deal
  pipeline.
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
    - deal-tracker
    - financial-services
    - investment-banking
    related_skills: []
---

# FSI Command: /deal-tracker

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/deal-tracker` from `investment-banking`. Invoke it explicitly with `/skill fsi-command-deal-tracker` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/deal-tracker` or a deal tracker financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `deal-tracker` skill to review deal status, update milestones, and manage action items across live deals.

## Hermes Invocation
- Explicit: `/skill fsi-command-deal-tracker`
- Natural language: “Use the deal-tracker command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
