---
name: fsi-command-value-creation
description: Use when financial-services work requires build a post-acquisition value
  creation plan.
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
    - value-creation
    related_skills: []
---

# FSI Command: /value-creation

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/value-creation` from `private-equity`. Invoke it explicitly with `/skill fsi-command-value-creation` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/value-creation` or a value creation financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `value-creation-plan` skill and structure a value creation roadmap with EBITDA bridge, 100-day plan, and KPI dashboard.

If a company name is provided, use it. Otherwise ask the user for the target company details.

## Hermes Invocation
- Explicit: `/skill fsi-command-value-creation`
- Natural language: “Use the value-creation command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
