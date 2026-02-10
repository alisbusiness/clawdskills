---
name: research-and-development
description: >
  Intensive research and product planning skill for validating ideas before
  building. Use when: (1) the user has a new project idea that needs
  market/technical validation, (2) the user wants to research competitors,
  tools, or technical approaches, (3) the user needs a structured research
  plan or deep research prompt, (4) the user wants to evaluate feasibility
  before committing to code, (5) the user asks "should I build this?" or
  "what's already out there?", (6) the user needs to compare technologies,
  platforms, or market opportunities, (7) the user needs to create a Product
  Requirements Document (PRD), (8) the user needs to define features, user
  stories, success metrics, or launch strategy, or (9) the user is scoping
  an MVP and needs to prioritize what to build first.
---

# Research & Development

Validate ideas through intensive research, then define exactly what to build. This skill produces two kinds of artifacts:

1. **Research output** — market validation, competitor analysis, technical feasibility
2. **Product Requirements Document (PRD)** — features, user stories, success metrics, launch plan

Both inform all downstream decisions (architecture, implementation, deployment).

## When to Use

- **Before starting any new project** — validate the idea first
- **When evaluating a new technology** — compare options with evidence
- **When entering a new market** — understand competitors and users
- **When pivoting** — re-evaluate assumptions with fresh research
- **When scoping an MVP** — define features, priorities, and success criteria
- **When writing a PRD** — structure product requirements for the team or AI agent

## Phase 1: Deep Research

### Step 1: Assess the Researcher

Determine the user's technical level to calibrate depth and language:

| Level | Profile | Research Focus |
|-------|---------|---------------|
| **Vibe-coder** | Great ideas, limited coding experience | Simple insights, tool recommendations, cost estimates |
| **Developer** | Experienced programmer | Architecture patterns, trade-offs, benchmarks |
| **In-between** | Some coding knowledge, still learning | Balanced practical guidance + technical detail |

### Step 2: Gather Context (Ask One at a Time)

Core questions — adapt framing to user's level:

1. **What's the idea?** — Problem it solves, who it's for
2. **Who needs it most?** — Target users, their pain points
3. **What exists already?** — Competitors, current solutions
4. **What's the differentiator?** — Unique value proposition
5. **What are the must-haves?** — 3-5 essential features for launch
6. **Platform preference?** — Web, mobile, desktop, or undecided
7. **Timeline?** — Days, weeks, or months
8. **Budget?** — Free only, modest budget, or flexible

For developers, also ask:
- Specific technical questions the research must answer
- Scope boundaries (included vs. excluded)
- Depth needed per area (surface / deep / comprehensive)
- Technical constraints (languages, frameworks, compliance)

### Step 3: Verification Echo (Required)

Summarize understanding back to the user before proceeding:

> **Project:** [Name and one-line description]
> **Target Users:** [Who this is for]
> **Problem Solved:** [Core problem]
> **Key Features:** [3-5 must-haves]
> **Platform:** [Web/Mobile/Desktop]
> **Timeline:** [Their timeline]
> **Budget:** [Their constraints]
>
> Is this accurate?

**Wait for confirmation.** Update if they correct anything.

### Step 4: Research Plan (Complex Projects)

> **Research Areas:**
> 1. [Area] — [What we'll investigate]
> 2. [Area] — [What we'll investigate]
>
> **Sources to Check:** [Source types]
> **Expected Deliverables:** [What they'll get]

### Step 5: Execute Research

Generate a structured research output using the appropriate template.
For research prompt templates by user level → read `references/research-templates.md`.

### Step 6: Deliver & Advise

Provide:
1. The research document
2. A clear recommendation (build / don't build / pivot)
3. Next steps: proceed to Phase 2 (PRD) if building

## Phase 2: Product Requirements Document (PRD)

After research validates the idea, define exactly what to build.

### Inputs Required

- Research findings from Phase 1 (required)
- User's technical level (A/B/C from Phase 1)

### PRD Questions (Ask One at a Time)

**For all users:**

1. Product/app name
2. One-sentence problem statement
3. Launch goal (e.g., "100 users", "$1000 MRR", "learn to build apps")

**Then branch by level:**

- **Vibe-coders:** Target user description, user journey story, 3-5 must-have features, v2 features, 1-2 success metrics, design vibe (3-5 words), constraints
- **Developers:** Persona + jobs-to-be-done, user stories (primary + supporting), MoSCoW feature prioritization, success metrics (activation/engagement/retention/revenue), non-functional requirements, risk assessment, business model
- **In-between:** User profile + problem, main user flow, features with rationale, v2 features, success metrics (1-month + 3-month), design/UX direction, constraints

For complete PRD question paths and document templates → read `references/prd-templates.md`.

### Verification Echo (Required)

Before generating the PRD:

> **Product:** [Name] — [One-line description]
> **Target User:** [Primary persona]
> **Problem:** [Core problem]
> **Must-Have Features:**
> 1. [Feature 1]
> 2. [Feature 2]
> 3. [Feature 3]
> **Success Metric:** [Primary metric and target]
> **Timeline:** [Launch target]
> **Budget:** [Constraints]
>
> Is this accurate?

### Generate PRD

Create the PRD document using the appropriate template from `references/prd-templates.md`. The PRD should cover:

- Product overview and vision
- Target users and personas
- Problem statement and competitive landscape
- User journey / user stories
- Feature list with prioritization (must-have / nice-to-have / not-in-MVP)
- Success metrics
- UI/UX direction
- Technical considerations
- Quality standards
- Constraints, assumptions, and risks
- MVP definition of done

### PRD Quality Checklist

| Required Section | Check |
|-----------------|-------|
| Core problem clearly defined | ✓ |
| Target user well described | ✓ |
| 3-5 must-have features listed | ✓ |
| Each feature has user story | ✓ |
| Success metrics defined | ✓ |
| Constraints acknowledged | ✓ |
| NOT-in-MVP features listed | ✓ |

## Research Quality Standards

- **Cite sources** with URLs and access dates for major claims
- **Flag uncertainty** — distinguish sourced facts from model knowledge
- **Note conflicts** — when sources disagree, say so explicitly
- **Use tables** for comparisons (competitors, tools, costs)
- **Include pros/cons** for every major recommendation
- **Be honest** about limitations and risks

## Platform Recommendations

| Need | Best Choice | Why |
|------|-------------|-----|
| Large context (whole codebases) | Gemini | Largest context window |
| Technical accuracy | Claude | Strong code/architecture analysis |
| Quick iterations | ChatGPT | Fast responses, good reasoning |

**Pro tip:** Run research on 2 platforms and compare results to catch blind spots.
