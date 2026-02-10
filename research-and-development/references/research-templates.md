# Research Prompt Templates

## Table of Contents

- [Vibe-Coder Template](#vibe-coder-template)
- [Developer Template](#developer-template)
- [In-Between Template](#in-between-template)

## Vibe-Coder Template

Use this template for users with limited coding experience who need beginner-friendly research with actionable insights.

```markdown
## Deep Research Request: [App Name]

<context>
I'm a non-technical founder building [description]. I need beginner-friendly research with actionable insights.
</context>

<instructions>
### Key Questions to Answer:
1. What similar apps exist and what features do they have?
2. What do users love/hate about existing solutions?
3. What's the simplest way to build an MVP?
4. What no-code/low-code tools are best for this?
5. How do similar apps monetize and what can I realistically charge?
6. What AI tools or APIs can accelerate development or differentiate the MVP?

### Research Focus:
- Simple, actionable insights with examples
- Current tool recommendations (prioritize newest/best)
- Step-by-step implementation guidance
- Cost estimates with free/paid options
- Examples of similar successful projects

### Required Deliverables:
1. **Competitor Table** — Features, pricing, user count, reviews
2. **Tech Stack** — Recommended tools for beginners
3. **MVP Features** — Must-have vs nice-to-have prioritization
4. **Development Roadmap** — With AI assistance strategy
5. **Budget Breakdown** — Tools, services, deployment costs
</instructions>

<output_format>
- Explain everything in plain English with examples
- **Include source URLs with access dates** for each major recommendation
- Use tables for comparisons
- Highlight any conflicting information between sources
</output_format>
```

## Developer Template

Use this template for experienced programmers who need comprehensive technical research.

```markdown
## Deep Research Request: [Project Name]

<context>
I need comprehensive technical research on [topic] for [context].

**Technical Context:**
- Constraints: [Their constraints]
- Preferred Stack: [If specified]
- Compliance: [Any requirements]
</context>

<instructions>
### Research Objectives:
[Based on their answers]

### Specific Questions:
[Their detailed questions]

### Scope Definition:
- **Include:** [Their specifications]
- **Exclude:** [Their exclusions]
- **Depth Requirements:** [Their requirements per area]

### Sources Priority:
[Their ranked preferences]

### Required Analysis:
- Technical architecture patterns (current best practices)
- Performance benchmarks with latest frameworks
- Security considerations for AI-integrated apps
- Scalability approaches with modern infrastructure
- AI tool/API integration strategies (include sources and current pricing)
- Cost optimization with current cloud pricing
- Development velocity estimates with AI assistance

### Premium UI/Design Research:
- Design system generators and component libraries
- Figma-to-code tools
- Generative UI approaches
- Design token standardization patterns

### Agent Architecture Research:
- Planner-Executor-Reviewer (PER) loop patterns
- MCP (Model Context Protocol) integration options
- Self-healing code and test strategies
- Visual verification workflows
</instructions>

<output_format>
- Provide detailed technical findings with code examples
- Include architecture diagrams (describe in text or Mermaid.js)
- **Cite sources with URLs and access dates** for each major finding
- Use tables for comparisons
- **Explicitly note where sources disagree** or data is uncertain
- Include pros/cons for each major recommendation
</output_format>
```

## In-Between Template

Use this template for users with some technical knowledge who need a balance of practical guidance and technical detail.

```markdown
## Deep Research Request: [Project Name]

<context>
I'm building [description] with some technical knowledge. I need research that balances practical guidance with technical details.

**My Skills:** [Languages/frameworks they know]
**Learning Preference:** [Familiar vs optimal]
</context>

<instructions>
### Core Questions:
[Mix of technical and non-technical based on their needs]

### Research Areas:
- Market validation and competitor analysis
- Technical approach recommendations
- AI tools/APIs relevant to this product and my skill level
- Learning resources for required technologies
- MVP development strategy with AI assistance
- No-code vs low-code vs full-code trade-offs

### Specific Focus:
- Implementation complexity with each approach
- Time to market with different tools
- Cost comparison (development and running)
- Skill requirements and learning curves

### Required Deliverables:
1. **Feature Matrix** — MVP prioritization
2. **Tech Stack** — Recommended with alternatives
3. **AI Tool Guide** — Which tool for what task
4. **Roadmap** — Development with skill milestones
5. **Resources** — Learning materials (prioritized)
6. **Budget** — Forecast with tool subscriptions
</instructions>

<output_format>
- Assume basic programming knowledge, explain advanced concepts
- **Include source URLs with access dates** for recommendations
- Use tables for comparisons
- **Note any conflicting information** between sources
- Provide pros/cons for major decisions
</output_format>
```
