---
name: backend-guide
description: >
  Production-grade backend development guide covering architecture patterns,
  API design, database selection, security hardening, testing strategy,
  environment setup, deployment, and operational readiness. Use when:
  (1) building a new backend API or service, (2) choosing a database or
  persistence layer, (3) designing API endpoints or service architecture,
  (4) reviewing or implementing backend security, (5) setting up CI/CD,
  deployment, or monitoring, (6) preparing release or responsibility checklists,
  (7) making infrastructure architecture decisions, or (8) establishing backend
  code quality standards.
---

# Backend Guide

## Core Commandments

1. Keep `README.md` in the repo root as the single source of truth for docs
2. Enable single-command run (`npm start`, `docker compose up`, etc.)
3. Enable single-command deploy
4. Ensure repeatable, re-creatable builds
5. Bundle a [Bill of Materials](#bill-of-materials) with every build artifact
6. Use **UTC** as the timezone everywhere — servers, databases, logs, timestamps
7. **Commit to git after every meaningful change** — no exceptions

## Git Discipline (Mandatory)

**Always commit to git.** Every unit of work must be captured in version control.

### When to Commit

- After completing any feature, fix, or refactor
- After updating configuration or environment setup
- After modifying documentation or checklists
- After resolving a bug — even a one-line fix
- Before switching context to a different task
- When leaving work in a known-broken state, commit with a `WIP:` prefix

### Commit Message Format

Use clear, imperative-tense messages:

```
feat: add user authentication endpoint
fix: resolve race condition in payment processing
docs: update API documentation for v2 endpoints
chore: update dependencies to patch security vulnerabilities
wip: partial migration to new database schema
```

### Tracking Future Work

1. Add `TODO` or `FIXME` comments in the code at the relevant location
2. Commit them immediately with a descriptive message
3. For larger planned work, create tickets/issues and reference the ticket ID in code comments

> **Rule:** Never leave uncommitted changes. If you made a change, it goes into git — period.

## Architecture Principles

### Architectural Sovereignty

- Routes/controllers handle request/response ONLY — no business logic
- All business logic lives in `services/` or `core/`
- No database calls from route handlers
- Thin controllers, fat services

### Backend Project Structure

```
src/
├── api/
│   ├── routes/        # Route handlers (thin controllers)
│   ├── middleware/     # Express/Fastify middleware
│   └── validators/    # Request validation (Zod/Joi)
├── services/
│   ├── auth/          # Authentication logic
│   ├── [feature]/     # Feature-specific business logic
│   └── external/      # Third-party integrations
├── models/            # Data models / ORM entities
├── db/
│   ├── migrations/    # Database migrations
│   └── seeds/         # Seed data
├── utils/             # Shared utilities
└── config/            # Configuration management
```

### API Design Conventions

For detailed API design patterns, endpoint structure, and request/response typing → read `references/architecture-patterns.md`.

## Engineering Constraints (Non-Negotiable)

### Type Safety

- The `any` type is **FORBIDDEN** — use `unknown` with type guards
- All function parameters and returns must be typed
- Use Zod or similar for runtime validation at API boundaries

### Library Governance

- Check existing `package.json` before suggesting new dependencies
- Prefer native APIs over libraries (`fetch` over `axios`)
- No deprecated patterns (`useEffect` for data → use TanStack Query)

### Error Handling

- Explicit error types — no swallowed exceptions
- All API endpoints return structured error responses
- Use custom error classes with HTTP status codes

### The "No Apologies" Rule

- Do NOT generate filler text before providing solutions
- If context is missing, ask ONE specific clarifying question
- Fix errors immediately — don't explain what went wrong at length

## Project Scoping

Before beginning backend implementation, determine:

- Expected life-span (one-off vs. continuous development)
- Release cycle (weekly, biweekly, on-demand)
- Required environments (dev, test, staging, prod)
- Downtime tolerance for production
- Technology maturity constraints and backward-compatibility expectations

## Environment Setup

- Use identical setup and versions across all environments
- Cover: database, application server, proxy, SDK versions, all dependencies
- Prefer **Docker Compose** for development and production
- Store SHA-1 checksums of all external packages; verify on install
- Use `docker export` to snapshot working environments for disaster recovery

## Database Selection

| Requirement | Solution | Go-To Choice | When to Avoid |
|-------------|----------|--------------|---------------|
| ACID compliance, complex joins, analytics | RDBMS | **PostgreSQL** | Massive horizontal scale with simple lookups |
| Flexible schema, full-text search | Document store | **Elasticsearch**, CouchDB | Strict transactional integrity needed |
| High-speed lookups, caching, sessions | Key-value store | **Redis**, Cassandra | Complex querying or relationships |
| Relationship traversal, network analysis | Graph database | **Neo4j** | Simple tabular data |

> **Note:** PostgreSQL 9.4+ supports native JSON storage — consider it before adding a separate document store.

### Persistence Checklist

- [ ] Verified, tested backups (test restoration regularly)
- [ ] Scripts for copying data between environments
- [ ] Plan for rolling out persistence layer updates
- [ ] Plan for scaling (read replicas, sharding, vertical scaling)
- [ ] Schema migration tooling (Flyway, Alembic, Knex migrations)
- [ ] Health monitoring and alerting

### Hosting Model

| Model | Pros | Cons |
|-------|------|------|
| **SaaS** (managed) | Fast setup, auto-scaling, minimal ops | Less tuning control, vendor lock-in |
| **Cloud self-hosted** | Full tuning control, cost-effective at scale | More operational burden |
| **On-premise** | Complete control including physical security | Most expensive, most labor-intensive |

## Bill of Materials

Include in every build artifact:

1. SDK and critical tool versions used to build it
2. Full dependency list with versions
3. Globally unique build revision (git SHA-1 hash)
4. Environment variables and build configuration used
5. List of any failed tests or checks at build time

## Security

### Mandatory Practices

#### Credentials & Secrets

- **Never** transmit credentials over unencrypted channels — always HTTPS/TLS
- **Never** store secrets in version control
- Store secrets in environment variables or separate config files excluded from VCS
- Keep a `.env.sample` with placeholder values
- Consider a secrets manager (Vault, AWS Secrets Manager) for production

#### Password Storage

- **Never** store passwords in plaintext or reversible encryption
- Use **bcrypt, scrypt, or Argon2** with a random salt
- Do **not** use SHA-1 or MD5 for password hashing

#### Authentication & Authorization

- Limit login attempts per client per time window
- Lock accounts after repeated failures
- Apply throttling to any sensitive action

For detailed JWT/RBAC patterns and security headers → read `references/architecture-patterns.md`.

#### Suspicious Action Throttling

- Monitor for abnormal data access patterns
- Throttle or block bulk operations exceeding expected usage
- Distinguish sequential requests from single bulk-export requests

### Audit Logging

```
<timestamp> <originator> <action>
2024-09-13 03:00:05 Job:daily_cleanup "deleted 847 expired sessions"
2024-09-13 12:47:23 User:admin "deleted item #123"
```

- Include exact timestamp, originator, and action
- Make the audit log tamper-proof via a dedicated logging service
- Store separately from application logs

### Data Anonymization

- Strip PII from exports — names, addresses, emails
- Replace real IDs with opaque identifiers
- Avoid logging PII; if unavoidable, hash it first

### File System & Docker Security

- Temp files: mode `600`, dedicated temp directory
- Application source/data/config/logs: restricted permissions
- Docker: never run as root, restrict capabilities, apply network isolation, rebuild with updated base images regularly

## Testing Strategy

- **Unit Tests:** 80% coverage minimum on critical paths
- **Integration Tests:** Cover all critical API paths
- **E2E Tests:** Main user journeys
- **Pre-commit hooks:** Run format/lint/tests before every commit

For test patterns, self-healing tests, and verification workflows → read `references/devops-and-deployment.md`.

## DevOps & Deployment

For CI/CD pipelines, deployment strategies, monitoring, scaling paths, and cost analysis → read `references/devops-and-deployment.md`.

## Checklists

### Responsibility Checklist

Before launch, explicitly assign ownership for:

- [ ] Incident response and on-call rotation
- [ ] Monitoring and alerting setup
- [ ] Backup verification schedule
- [ ] Dependency update cadence
- [ ] Security patch application process
- [ ] Log rotation and retention policy

### Release Checklist

Before each release, verify:

- [ ] All tests pass
- [ ] Bill of materials is generated and included
- [ ] Database migrations run cleanly (forward and rollback)
- [ ] Environment variables are documented and set
- [ ] Secrets are not committed to VCS
- [ ] Monitoring and alerting covers new functionality
- [ ] Rollback procedure is documented and tested

## Recommended CLI Tools

| Tool | Purpose |
|------|---------|
| [HTTPie](https://github.com/jakubroztocil/httpie) | Human-friendly HTTP client for API testing |
| [jq](https://stedolan.github.io/jq/) | CLI JSON processor for filtering and transforming API responses |
