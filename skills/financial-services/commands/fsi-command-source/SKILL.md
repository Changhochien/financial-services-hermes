---
name: fsi-command-source
description: Use when financial-services work requires source deals — discover companies
  and draft founder outreach.
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
    - private-equity
    - source
    related_skills: []
---

# FSI Command: /source

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/source` from `private-equity`. Invoke it explicitly with `/skill fsi-command-source` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/source` or a source financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `deal-sourcing` skill and run the sourcing pipeline: discover target companies, check CRM for existing relationships, and draft personalized founder outreach emails.

If criteria are provided, use them. Otherwise ask the user for sector, size, geography, and deal parameters.

## Hermes Invocation
- Explicit: `/skill fsi-command-source`
- Natural language: “Use the source command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
