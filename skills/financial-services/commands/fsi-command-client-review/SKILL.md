---
name: fsi-command-client-review
description: Use when financial-services work requires prep for a client review meeting.
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
    - client-review
    - command
    - financial-services
    - wealth-management
    related_skills: []
---

# FSI Command: /client-review

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/client-review` from `wealth-management`. Invoke it explicitly with `/skill fsi-command-client-review` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/client-review` or a client review financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `client-review` skill and prepare a client meeting package with performance, allocation, and talking points.

If a client name is provided, use it. Otherwise ask who the meeting is with.

## Hermes Invocation
- Explicit: `/skill fsi-command-client-review`
- Natural language: “Use the client-review command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
