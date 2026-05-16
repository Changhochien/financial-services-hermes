---
name: fsi-command-dd-prep
description: Use when financial-services work requires prep for a diligence meeting
  or expert call.
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
    - dd-prep
    - financial-services
    - private-equity
    related_skills: []
---

# FSI Command: /dd-prep

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/dd-prep` from `private-equity`. Invoke it explicitly with `/skill fsi-command-dd-prep` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/dd-prep` or a dd prep financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

Load the `dd-meeting-prep` skill and generate targeted questions, benchmarks, and red flags to probe.

If details are provided, use them. Otherwise ask for the company, meeting type (management presentation, expert call, customer reference), and topic focus.

## Hermes Invocation
- Explicit: `/skill fsi-command-dd-prep`
- Natural language: “Use the dd-prep command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
