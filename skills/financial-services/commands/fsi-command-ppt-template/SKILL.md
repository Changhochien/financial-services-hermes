---
name: fsi-command-ppt-template
description: Use when financial-services work requires create a reusable PPT template
  skill from a PowerPoint template file.
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
    - financial-analysis
    - financial-services
    - ppt-template
    related_skills: []
---

# FSI Command: /ppt-template

## Overview
This is the Hermes profile equivalent of the original Cowork slash command `/ppt-template` from `financial-analysis`. Invoke it explicitly with `/skill fsi-command-ppt-template` or ask in natural language for this workflow.

## When to Use
- Use when the user asks for `/ppt-template` or a ppt template financial-services workflow.
- Use when the user wants the command procedure rather than a free-form answer.

## Command Procedure

# PPT Template Creator Command

Create a self-contained PPT template skill from a user-provided PowerPoint template.

## Instructions

1. **Ask for the template file** if not provided:
   - "Please provide the path to your PowerPoint template file (.pptx or .potx)"
   - The template should contain the slide layouts and branding you want to use

2. **Load the ppt-template-creator skill**:
   - Use the `skill: "ppt-template-creator"` tool to load the full skill instructions
   - Follow the workflow in the skill to analyze the template and generate a new skill

3. **Gather additional info**:
   - Company/template name (for naming the skill)
   - Primary use cases (pitch decks, board materials, client presentations, etc.)

4. **Execute the skill workflow**:
   - Analyze template structure (layouts, placeholders, dimensions)
   - Generate skill directory with assets/ and SKILL.md
   - Create example presentation to validate
   - Package the skill

5. **Deliver the packaged skill** to the user

## Hermes Invocation
- Explicit: `/skill fsi-command-ppt-template`
- Natural language: “Use the ppt-template command workflow for ...”

## Verification Checklist
- [ ] The command intent, inputs, and output format are confirmed.
- [ ] The output cites sources or clearly labels assumptions.
- [ ] The final artifact is marked draft / for human review when appropriate.
