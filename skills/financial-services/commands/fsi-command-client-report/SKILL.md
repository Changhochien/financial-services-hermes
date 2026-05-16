---
name: fsi-command-client-report
description: Use when financial-services work requires generate a client performance
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
    - client-report
    - command
    - financial-services
    - wealth-management
    related_skills: []
---

# FSI Command: /client-report

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/client-report` from `wealth-management`. Invoke it explicitly with `/skill fsi-command-client-report` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/client-report` or a client report financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `client-report` skill to generate a professional client-facing performance report.

If a client and period are provided, use them. Otherwise ask for client details and reporting period.

## Hermes Invocation
- Explicit: `/skill fsi-command-client-report`
- Natural language: “Use the client-report command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
