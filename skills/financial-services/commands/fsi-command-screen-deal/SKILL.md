---
name: fsi-command-screen-deal
description: Use when financial-services work requires screen an inbound deal (CIM
  or teaser).
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
    - screen-deal
    related_skills: []
---

# FSI Command: /screen-deal

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/screen-deal` from `private-equity`. Invoke it explicitly with `/skill fsi-command-screen-deal` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/screen-deal` or a screen deal financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `deal-screening` skill and quickly evaluate an inbound deal against the fund's investment criteria.

If a file path is provided, use it. Otherwise ask the user for the deal materials or description.

## Hermes Invocation
- Explicit: `/skill fsi-command-screen-deal`
- Natural language: “Use the screen-deal command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
