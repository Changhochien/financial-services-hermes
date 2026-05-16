---
name: fsi-command-proposal
description: Use when financial-services work requires create an investment proposal
  for a prospect.
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
    - proposal
    - wealth-management
    related_skills: []
---

# FSI Command: /proposal

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/proposal` from `wealth-management`. Invoke it explicitly with `/skill fsi-command-proposal` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/proposal` or a proposal financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `investment-proposal` skill to create a personalized investment proposal for a prospective client.

If a prospect name is provided, use it. Otherwise ask for prospect details.

## Hermes Invocation
- Explicit: `/skill fsi-command-proposal`
- Natural language: “Use the proposal command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
