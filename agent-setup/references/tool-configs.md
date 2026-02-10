# Tool Configuration Templates

## Claude Code — CLAUDE.md

```markdown
# CLAUDE.md — Claude Code Configuration for [App Name]

## Project Context
**App:** [App Name]
**Stack:** [Tech Stack]
**Stage:** MVP Development
**User Level:** [Level]

## Directives
1. **Master Plan:** Always read `AGENTS.md` first — it has the current phase and tasks.
2. **Documentation:** Refer to `agent_docs/` for tech stack, code patterns, and testing guides.
3. **Plan-First:** Propose a brief plan and wait for approval before coding.
4. **Incremental Build:** Build one small feature at a time. Test frequently.
5. **Pre-Commit:** If hooks exist, run them before commits; fix failures.
6. **No Linting:** Do not act as a linter. Use `npm run lint` if needed.
7. **Communication:** Be concise. Ask clarifying questions when needed.

## Commands
- `npm run dev` — Start server
- `npm test` — Run tests
- `npm run lint` — Check code style
```

## Cursor — .cursorrules

```markdown
# Cursor Rules for [App Name]

## Project Context
**App:** [App Name]
**Stack:** [Tech Stack]
**Stage:** MVP Development
**User Level:** [Level]

## Directives
1. **Master Plan:** Always read `AGENTS.md` first — it has the current phase and tasks.
2. **Documentation:** Refer to `agent_docs/` for tech stack, code patterns, and testing guides.
3. **Plan-First:** Propose a brief plan and wait for approval before coding.
4. **Incremental Build:** Build one small feature at a time. Test frequently.
5. **Pre-Commit:** If hooks exist, run them before commits; fix failures.
6. **No Linting:** Do not act as a linter. Use `npm run lint` if needed.
7. **Communication:** Be concise. Ask clarifying questions when needed.

## Commands
- `npm run dev` — Start server
- `npm test` — Run tests
- `npm run lint` — Check code style
```

## Gemini CLI / Antigravity — GEMINI.md

```markdown
# GEMINI.md — Gemini Configuration for [App Name]

## Project Context
**App:** [App Name]
**Stack:** [Tech Stack]
**Stage:** MVP Development
**User Level:** [Level]

## Directives
1. **Master Plan:** Always read `AGENTS.md` first — it has the current phase and tasks.
2. **Documentation:** Refer to `agent_docs/` for tech stack, code patterns, and testing guides.
3. **Plan-First:** Propose a brief plan and wait for approval before coding.
4. **Incremental Build:** Build one small feature at a time. Test frequently.
5. **Pre-Commit:** If hooks exist, run them before commits; fix failures.
6. **No Linting:** Do not act as a linter. Use `npm run lint` if needed.
7. **Communication:** Be concise. Ask clarifying questions when needed.

## Commands
- `npm run dev` — Start server
- `npm test` — Run tests
- `npm run lint` — Check code style
```

## GitHub Copilot — .github/copilot-instructions.md

```markdown
# GitHub Copilot Instructions for [App Name]

## Project Context
**App:** [App Name]
**Stack:** [Tech Stack]
**Stage:** MVP Development

## Directives
1. Read `AGENTS.md` for the current phase and tasks.
2. Refer to `agent_docs/` for tech stack details and code patterns.
3. Follow existing code conventions in the repository.
4. Write tests for new functionality.
5. Keep changes incremental and focused.

## Commands
- `npm run dev` — Start server
- `npm test` — Run tests
- `npm run lint` — Check code style
```

## Useful First Prompts by Level

| Level | First Prompt |
|-------|-------------|
| **Vibe-coder** | "Read AGENTS.md and agent_docs. Propose a plan first, wait for approval, then build step by step." |
| **Developer** | "Review AGENTS.md and architecture. Propose a Phase 1 plan, get approval, then implement with proper patterns." |
| **In-between** | "Read AGENTS.md. Show me the plan for Phase 1, explain the approach, then build one feature at a time." |

## Troubleshooting

| Problem | Fix |
|---------|-----|
| AI ignores docs | Start with: "First read AGENTS.md, PRD, and TechDesign. Summarize key requirements before coding." |
| Code doesn't match PRD | "Re-read the PRD section on [feature], list acceptance criteria, then refactor accordingly." |
| AI overcomplicates | "Prioritize MVP scope. Give me the simplest working implementation." |
| AI skips steps | "Let's go slower. Implement just [specific feature] and show me how to test it." |
