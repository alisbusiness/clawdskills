---
name: agent-setup
description: >
  AI agent configuration and project bootstrapping skill. Use when:
  (1) setting up AGENTS.md or tool-specific config files for a new project,
  (2) configuring Claude Code (CLAUDE.md), Cursor (.cursorrules), Gemini CLI
  (GEMINI.md), or GitHub Copilot (copilot-instructions.md),
  (3) creating the agent_docs/ progressive disclosure documentation system,
  (4) the user wants to prepare a project for AI-assisted development,
  (5) the user asks how to structure instructions for an AI coding agent,
  or (6) bootstrapping a new project with plan-execute-verify workflows.
---

# Agent Setup

Configure AI coding assistants to build your project effectively. This skill creates the instruction files and documentation structure that guide AI agents during development.

## What This Produces

1. **`AGENTS.md`** — Universal master plan (works with any AI tool)
2. **`agent_docs/`** — Progressive disclosure documentation
3. **Tool-specific configs** — CLAUDE.md, .cursorrules, GEMINI.md, etc.

## Prerequisites

Before running this skill, you should have:
- A **PRD** (product requirements) — what to build
- A **Technical Design** — how to build it
- A chosen **AI tool** (Claude Code, Cursor, Gemini CLI, etc.)

## Setup Workflow

### Step 1: Identify Tool(s)

| Tool | Config File | Auto-Reads |
|------|------------|------------|
| Claude Code | `CLAUDE.md` | Yes, at project root |
| Cursor | `.cursorrules` | Yes, at project root |
| Gemini CLI / Antigravity | `GEMINI.md` | Yes, at project root |
| GitHub Copilot | `.github/copilot-instructions.md` | Yes |
| Any tool | `AGENTS.md` | Must be told to read it |

### Step 2: Extract from Source Documents

**From PRD (must extract):**
- Product name and one-line description
- Primary user story
- All must-have features (exact list)
- Nice-to-have and NOT-in-MVP features
- Success metrics
- UI/UX requirements
- Timeline and constraints

**From Technical Design (must extract):**
- Complete tech stack (frontend, backend, database, deployment)
- Project structure (folder layout)
- Database schema (if provided)
- Implementation approach per feature
- Deployment platform and steps
- Budget constraints

### Step 3: Generate AGENTS.md

Create in the project root. This is the single source of truth for project status and goals.

```markdown
# AGENTS.md — Master Plan for [App Name]

## Project Overview
**App:** [App Name]
**Goal:** [One-line description]
**Stack:** [Tech Stack]
**Current Phase:** Phase 1 — Foundation

## How I Should Think
1. **Understand Intent First**: Before answering, identify what the user actually needs
2. **Ask If Unsure**: If critical information is missing, ask before proceeding
3. **Plan Before Coding**: Propose a plan, ask for approval, then implement
4. **Verify After Changes**: Run tests/linters or manual checks after each change
5. **Explain Trade-offs**: When recommending something, mention alternatives

## Plan → Execute → Verify
1. **Plan:** Outline a brief approach and ask for approval before coding
2. **Execute:** Implement one feature at a time
3. **Verify:** Run tests/linters after each feature; fix before moving on

## Context & Memory
- Treat `AGENTS.md` and `agent_docs/` as living docs
- Use persistent tool configs for project rules
- Update these files as the project scales

## Context Files
Refer to these for details (load only when needed):
- `agent_docs/tech_stack.md`: Tech stack & libraries
- `agent_docs/code_patterns.md`: Code style & patterns
- `agent_docs/project_brief.md`: Persistent project rules
- `agent_docs/product_requirements.md`: Full PRD
- `agent_docs/testing.md`: Verification strategy and commands

## Current State (Update This!)
**Last Updated:** [Date]
**Working On:** [Current task]
**Recently Completed:** [Last completed item]
**Blocked By:** [Any blockers, or "None"]

## Roadmap
### Phase 1: Foundation
- [ ] Initialize project
- [ ] Setup database
- [ ] Set up pre-commit hooks

### Phase 2: Core Features
- [ ] [Feature 1]
- [ ] [Feature 2]

## What NOT To Do
- Do NOT delete files without explicit confirmation
- Do NOT modify database schemas without backup plan
- Do NOT add features not in the current phase
- Do NOT skip tests for "simple" changes
- Do NOT bypass failing tests or pre-commit hooks
- Do NOT use deprecated libraries or patterns
```

### Step 4: Create agent_docs/ Directory

Create these files, filled with detail from the source documents:

#### `agent_docs/tech_stack.md`
Tech stack, libraries, versions, setup commands, example component code.

#### `agent_docs/code_patterns.md`
Code style, naming conventions, error handling patterns, example code.

#### `agent_docs/project_brief.md`
Product vision, coding conventions, quality gates, key commands, update cadence.

#### `agent_docs/product_requirements.md`
Core requirements, user stories, and success metrics from the PRD.

#### `agent_docs/testing.md`
Testing tools, strategies, pre-commit hooks, verification loop.

### Step 5: Generate Tool-Specific Configs

Each config file should be concise — point to `AGENTS.md` and `agent_docs/` rather than duplicating content.

For complete config templates → read `references/tool-configs.md`.

## Engineering Constraints (Include in Configs)

### For Developer-Level Projects

```markdown
## Engineering Constraints

### Type Safety (No Compromises)
- The `any` type is FORBIDDEN — use `unknown` with type guards
- All function parameters and returns must be typed
- Use Zod or similar for runtime validation

### Architectural Sovereignty
- Routes/controllers handle request/response ONLY
- All business logic in `services/` or `core/`
- No database calls from route handlers

### Library Governance
- Check existing `package.json` before adding dependencies
- Prefer native APIs over libraries (fetch over axios)
- No deprecated patterns

### Workflow Discipline
- Pre-commit hooks must pass before commits
- If verification fails, fix issues before continuing
```

## Anti-Patterns (Include in All Configs)

```markdown
## What NOT To Do
- Do NOT delete files without explicit confirmation
- Do NOT modify database schemas without backup plan
- Do NOT add features not in the current phase
- Do NOT skip tests for "simple" changes
- Do NOT bypass failing tests or pre-commit hooks
- Do NOT generate filler text — fix errors immediately
- If context is missing, ask ONE specific clarifying question
```

## Progressive Disclosure Principle

Keep configs lean. Put detailed content in `agent_docs/`, not in tool configs.

| Content | Where It Goes |
|---------|--------------|
| Current phase, roadmap, state | `AGENTS.md` |
| Tech stack details, code examples | `agent_docs/tech_stack.md` |
| Code style, patterns | `agent_docs/code_patterns.md` |
| Full PRD requirements | `agent_docs/product_requirements.md` |
| Test strategy, commands | `agent_docs/testing.md` |
| Tool-specific behavior | `CLAUDE.md` / `.cursorrules` / `GEMINI.md` |
