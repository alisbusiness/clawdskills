# PRD Templates

## Table of Contents

- [Vibe-Coder PRD Template](#vibe-coder-prd-template)
- [Developer PRD Template](#developer-prd-template)
- [In-Between PRD Template](#in-between-prd-template)

---

## Vibe-Coder PRD Template

Generate as `PRD-[AppName]-MVP.md`:

```markdown
# Product Requirements Document: [App Name] MVP

## Product Overview

**App Name:** [Name]
**Tagline:** [Catchy one-liner]
**Launch Goal:** [What success looks like]
**Target Launch:** [Date or "6-8 weeks"]

## Who It's For

### Primary User: [Persona Name]
[User description in conversational language]

**Their Current Pain:**
- [Pain point 1]
- [Pain point 2]

**What They Need:**
- [Need 1]
- [Need 2]

### Example User Story
"Meet [persona], a [description] who struggles with [problem]. Every day they [current situation]. They need [solution] so they can [desired outcome]."

## The Problem We're Solving

[Problem statement with context — why it matters and why now]

**Why Existing Solutions Fall Short:**
- [Competitor]: [Why it's not enough]
- [Competitor]: [Why it's not enough]

## User Journey

### Discovery → First Use → Success

1. **Discovery** — How they find us, what catches attention, decision trigger
2. **Onboarding (First 5 Minutes)** — First screen, first action, quick win
3. **Core Usage Loop** — Trigger, action, reward, investment
4. **Success Moment** — "Aha!" moment, share trigger

## MVP Features

### Must Have for Launch

#### 1. [Feature Name]
- **What:** [Simple description]
- **User Story:** As a [user], I want to [action] so that [benefit]
- **Success Criteria:**
  - [ ] [Measurable outcome]
  - [ ] [Measurable outcome]
- **Priority:** P0 (Critical)

[Repeat for all must-have features]

### Nice to Have (If Time Allows)
- **[Feature]**: [Description]

### NOT in MVP (Saving for Later)
- **[Feature]**: Will add after [milestone]

## How We'll Know It's Working

| Metric | Target | How to Measure |
|--------|--------|----------------|
| [Metric] | [Target] | [Method] |

## Look & Feel

**Design Vibe:** [3-5 words]
**Visual Principles:**
1. [Principle]
2. [Principle]

**Key Screens:**
1. **[Screen]**: [Purpose]
2. **[Screen]**: [Purpose]

## Technical Considerations

**Platform:** [Web/Mobile/Both]
**Responsive:** Yes, mobile-first
**Performance:** Page load < 3 seconds
**Accessibility:** WCAG 2.1 AA minimum

## Budget & Constraints

**Development Budget:** [Amount]
**Monthly Operating:** [Estimate]
**Timeline:** [Weeks to launch]

## Definition of Done for MVP

- [ ] All P0 features functional
- [ ] Basic error handling works
- [ ] Works on mobile and desktop
- [ ] One complete user journey works end-to-end
- [ ] Basic analytics tracking
- [ ] Friends/family test complete

---
*Status: Draft — Ready for Technical Design*
```

---

## Developer PRD Template

Generate as `PRD-[AppName]-MVP.md`:

```markdown
# Product Requirements Document: [App Name] MVP

## Executive Summary

**Product:** [Name]
**Version:** MVP (1.0)
**Status:** [Draft/Final]
**Last Updated:** [Date]

### Product Vision
[Expanded vision statement]

### Success Criteria
[High-level success metrics and targets]

## Problem Statement

### Problem Definition
[Detailed problem analysis with market context]

### Impact Analysis
- **User Impact:** [Quantified where possible]
- **Market Impact:** [Size and opportunity]
- **Business Impact:** [Revenue/growth potential]

## Target Audience

### Primary Persona: [Name]
**Demographics:** [Details]
**Psychographics:** [Behaviors, values]
**Jobs to Be Done:**
1. [Functional job]
2. [Emotional job]
3. [Social job]

**Current Solutions & Pain Points:**
| Current Solution | Pain Points | Our Advantage |
|-----------------|-------------|---------------|
| [Solution] | [Problems] | [How we're better] |

## User Stories

### Epic: [Core Epic]

**Primary:** "As a [user], I want to [action] so that [benefit]"

**Acceptance Criteria:**
- [ ] [Criterion]
- [ ] [Criterion]

### Supporting Stories
1. "As a [user], I want to [action] so that [benefit]"
2. "As a [user], I want to [action] so that [benefit]"

## Functional Requirements

### Core Features (P0)

#### Feature 1: [Name]
- **Description:** [Detailed]
- **User Value:** [Why users need this]
- **Business Value:** [Why business needs this]
- **Acceptance Criteria:**
  - [ ] [Criterion]
- **Dependencies:** [Dependencies]
- **Estimated Effort:** [T-shirt size]

### Should Have (P1)
[Brief list with rationale]

### Could Have (P2)
[Brief list]

### Out of Scope
- [Feature]: [Why excluded]

## Non-Functional Requirements

### Performance
- Page Load: < 2 seconds (p95)
- API Response: < 200ms (p95)
- Concurrent Users: Support 1,000
- Uptime: 99.9%

### Security
- Authentication: [Method]
- Authorization: [RBAC/ACL]
- Data Protection: [Encryption]
- Compliance: [GDPR/CCPA/etc.]

### Usability
- Accessibility: WCAG 2.1 AA
- Browser: Chrome, Safari, Firefox, Edge (latest 2)
- Mobile: iOS 14+, Android 10+

## Quality Standards

### Code Quality
- Strict TypeScript, no `any` types
- Thin controllers — logic in services only
- Explicit error types, no swallowed exceptions
- 80% coverage minimum on critical paths

### Design Quality
- Design tokens only — no raw hex/pixel values
- WCAG 2.1 AA verified
- Core Web Vitals in green zone

## UI/UX Requirements

### Design Principles
1. [Principle]
2. [Principle]

### Information Architecture
```
├── Landing Page
├── Authentication
├── Dashboard
├── [Core Feature Area]
└── Settings/Profile
```

### Key User Flows
[Mermaid diagrams for 2-3 critical flows]

## Success Metrics

### North Star Metric
[Single most important metric]

### OKRs (First 90 Days)
**Objective 1:** [Objective]
- KR1: [Measurable result]
- KR2: [Measurable result]

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk] | H/M/L | H/M/L | [Strategy] |

## MVP Definition of Done

### Feature Complete
- [ ] All P0 features implemented
- [ ] All acceptance criteria met

### Quality
- [ ] Unit test coverage > 80%
- [ ] Integration tests passing
- [ ] Performance benchmarks met

### Release Ready
- [ ] Staging validated
- [ ] Monitoring configured
- [ ] Rollback plan documented

---
*Version: 1.0 | Next Review: [Date]*
```

---

## In-Between PRD Template

Generate as `PRD-[AppName]-MVP.md`:

```markdown
# Product Requirements Document: [App Name] MVP

## Overview

**Product Name:** [Name]
**Problem Statement:** [Expanded]
**MVP Goal:** [Clear, measurable]
**Target Launch:** [Timeframe]

## Target Users

### Primary User Profile
**Who:** [Description]
**Problem:** [What they struggle with]
**Current Solution:** [What they use now]
**Why They'll Switch:** [Unique value]

### User Persona: [Name]
- **Demographics:** [Age, location, profession]
- **Tech Level:** [Beginner/Intermediate/Advanced]
- **Goals:** [What they want]
- **Frustrations:** [Current pain points]

## User Journey

### Key Touchpoints
1. **Discovery:** [How they find you]
2. **First Contact:** [Landing page/app store]
3. **Onboarding:** [First experience]
4. **Core Loop:** [Regular usage]
5. **Retention:** [What brings them back]

## MVP Features

### Core Features (Must Have)

#### 1. [Feature Name]
- **Description:** [What it does]
- **User Value:** [Why users need it]
- **Success Criteria:**
  - Users can [action]
  - System [behavior]
- **Priority:** Critical

### Future Features (Not in MVP)
| Feature | Why Wait | Planned For |
|---------|----------|-------------|
| [Feature] | [Reason] | Version 2 |

## Success Metrics

### Primary
1. **[Metric]:** [Target] by [Date]
   - How to measure: [Method]

### Secondary
- [Metric]: [Target]

## UI/UX Direction

**Design Feel:** [Descriptive words]

### Key Screens
1. **[Screen]** — Purpose, key elements, user actions
2. **[Screen]** — Purpose, key elements, user actions

## Technical Considerations

**Platform:** [Web/Mobile/Both]
**Responsive:** [Yes/Mobile-first]
**Performance:** Load time < 3 seconds
**Security/Privacy:** [Requirements]

## Constraints

### Budget
- Development tools: $[X]/month
- Hosting: $[X]/month
- Third-party services: $[X]/month

### Timeline
- MVP Development: [X weeks]
- Beta Testing: [X weeks]
- Launch Target: [Date]

## Quality Standards

**Code Quality:**
- TypeScript when possible
- Handle errors explicitly
- Test important paths before launch

**Design Quality:**
- Consistent colors and spacing (design tokens)
- Test on mobile before desktop
- Check accessibility basics

## Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| [Risk] | H/M/L | [Strategy] |

## MVP Completion Checklist

- [ ] All core features working
- [ ] Basic error handling
- [ ] Mobile responsive
- [ ] Cross-browser tested
- [ ] Analytics configured
- [ ] Core journey works end-to-end

---
*Status: Ready for Technical Design*
```
