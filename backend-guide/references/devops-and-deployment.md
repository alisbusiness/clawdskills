# DevOps & Deployment

## Table of Contents

- [CI/CD Pipeline](#cicd-pipeline)
- [Git Workflow](#git-workflow)
- [Pre-Commit Hooks](#pre-commit-hooks)
- [Testing Strategy](#testing-strategy)
- [Deployment](#deployment)
- [Monitoring & Observability](#monitoring--observability)
- [Cost Analysis](#cost-analysis)
- [Scaling Path](#scaling-path)
- [Maintenance](#maintenance)

## CI/CD Pipeline

```yaml
# .github/workflows/deploy.yml
name: Deploy
on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run lint
      - run: npm test
      - run: npm run build

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci --production
      - uses: [deploy-action]
```

## Git Workflow

```
main
├── develop
│   ├── feature/[feature-name]
│   ├── fix/[bug-fix]
│   └── chore/[maintenance]
└── release/[version]
```

- Feature branches off `develop`
- PRs require passing tests + review
- Squash merge into `develop`
- Release branches for production cuts

## Pre-Commit Hooks

- Run format/lint/tests before every commit
- Use git hooks or a hook manager appropriate for your stack (Husky, lint-staged, pre-commit)
- Update hooks as the project scales

Example checks:
1. Lint (ESLint / Stylelint)
2. Format (Prettier)
3. Type check (tsc --noEmit)
4. Unit tests on changed files

## Testing Strategy

### Coverage Targets

| Type | Coverage | Focus |
|------|----------|-------|
| Unit Tests | 80% | Business logic in services |
| Integration Tests | Critical paths | API endpoints, database operations |
| E2E Tests | Main journeys | Complete user flows |

### Test Patterns

```javascript
// Unit testing (Vitest/Jest)
describe('ResourceService', () => {
  it('should create resource', async () => {
    const result = await service.create(mockData);
    expect(result).toMatchObject(expected);
  });
});

// E2E testing (Playwright)
test('user can complete main flow', async ({ page }) => {
  await page.goto('/');
  await page.click('[data-testid=start]');
  // ... test steps
  await expect(page).toHaveURL('/success');
});
```

### Self-Healing Test Pattern

When tests fail, capture context for repair:

```javascript
const failureContext = {
  error: error.message,
  codeSnippet: testCode,
  ariaSnapshot: await page.accessibility.snapshot(),
};
// Fix selector using getByRole or getByText
```

### Verification Loop

After every feature implementation:
1. Run unit tests
2. Run integration tests
3. Run linter
4. Fix any failures before proceeding

## Deployment

### Environment Configuration

```bash
# .env.production
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
JWT_SECRET=...
SENTRY_DSN=...
```

- Never commit `.env` files — only `.env.sample` with placeholders
- Use platform-specific env variable management in production
- Validate all required env vars at startup

### Infrastructure as Code

```terraform
resource "aws_ecs_service" "app" {
  name            = var.app_name
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = var.app_count

  load_balancer {
    target_group_arn = aws_alb_target_group.app.arn
    container_name   = var.app_name
    container_port   = var.app_port
  }
}
```

### Deployment Platforms

| Platform | Best For | Free Tier |
|----------|----------|-----------|
| **Vercel** | Next.js, frontend apps | ✓ |
| **Railway** | Full-stack, databases | Limited |
| **Cloudflare** | Edge functions, static | ✓ |
| **AWS ECS/Fargate** | Production scale | Pay-as-you-go |

## Monitoring & Observability

### Metrics to Track

| Category | Metrics |
|----------|---------|
| Application | Response time, error rate, throughput |
| Business | User signups, feature adoption, retention |
| Infrastructure | CPU, memory, disk, network |

### Structured Logging

```typescript
// Use Pino or similar structured logger
logger.info({
  event: 'user_action',
  userId: user.id,
  action: 'feature_used',
  metadata: { feature: 'name', duration: 123 },
});
```

### Alerting

- Set up alerts for error rate spikes, response time degradation, and uptime
- Use Sentry for error tracking, Datadog/New Relic for APM
- Configure PagerDuty or similar for on-call

## Cost Analysis

### Typical Monthly Costs

| Service | Free Tier | At 1K Users | At 10K Users |
|---------|-----------|-------------|--------------|
| Hosting | $0 | $20 | $50-100 |
| Database | $0 | $25 | $50-100 |
| Cache (Redis) | $0 | $10 | $25 |
| Monitoring | $0 | $26 | $50 |
| Email | $0 | $20 | $40 |
| **Total** | **$0** | **~$101** | **~$265-315** |

Set up billing alerts at 50%, 80%, and 100% of budget thresholds.

## Scaling Path

### Phase 1: MVP (0–1K users)

- Current architecture handles fine
- Monitor performance metrics
- Gather user feedback

### Phase 2: Growth (1K–10K users)

- Add Redis caching layer
- Implement CDN for assets
- Database read replicas
- Consider paid monitoring tiers

### Phase 3: Scale (10K+ users)

- Microservices migration if needed
- Multi-region deployment
- Advanced monitoring and observability
- Dedicated SRE/DevOps

## Maintenance

- Prefer stable dependencies; avoid unnecessary churn
- Review release notes regularly and adjust when needed
- Update CI/CD configs, pre-commit hooks, and documentation as the project scales
- Schedule regular dependency audits (`npm audit`, Dependabot)
