# Backend Architecture Patterns

## Table of Contents

- [API Design](#api-design)
- [Database Schema Patterns](#database-schema-patterns)
- [Service Layer Patterns](#service-layer-patterns)
- [Authentication & Authorization](#authentication--authorization)
- [Security Headers](#security-headers)
- [Performance Optimization](#performance-optimization)

## API Design

### RESTful Endpoint Structure

```typescript
// Standard CRUD endpoints
POST   /api/[resource]          // Create
GET    /api/[resource]          // List (with pagination)
GET    /api/[resource]/:id      // Get single
PUT    /api/[resource]/:id      // Update
DELETE /api/[resource]/:id      // Delete
```

### Request/Response Typing

```typescript
// Always type request and response shapes
interface CreateResourceRequest {
  name: string;
  description?: string;
  // ... fields based on domain
}

interface ResourceResponse {
  id: string;
  name: string;
  description?: string;
  createdAt: Date;
  updatedAt: Date;
}

// Paginated list response
interface PaginatedResponse<T> {
  data: T[];
  total: number;
  page: number;
  pageSize: number;
  hasMore: boolean;
}
```

### Validation at Boundaries

```typescript
// Use Zod for runtime validation at API boundaries
import { z } from 'zod';

const CreateResourceSchema = z.object({
  name: z.string().min(1).max(255),
  description: z.string().optional(),
});

// In route handler
const validated = CreateResourceSchema.parse(req.body);
const result = await resourceService.create(validated);
```

## Database Schema Patterns

### Standard Table Structure

```sql
-- Users table (foundation)
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Domain entity (pattern for any resource)
CREATE TABLE [entity_name] (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'active',
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Always add indexes for foreign keys and frequent queries
CREATE INDEX idx_[entity]_user_id ON [entity](user_id);
CREATE INDEX idx_[entity]_status ON [entity](status);
CREATE INDEX idx_[entity]_created_at ON [entity](created_at);
```

### Migration Conventions

- One migration per schema change
- Always include both `up` and `down` migrations
- Never modify a migration that has been applied to production
- Test rollback before deploying

## Service Layer Patterns

### Business Logic in Services

```typescript
// Services contain ALL business logic — controllers are thin
class ResourceService {
  constructor(
    private db: Database,
    private cache: CacheClient,
    private eventBus: EventBus,
  ) {}

  async create(data: CreateResourceDTO): Promise<Resource> {
    // 1. Validate business rules
    await this.validateBusinessRules(data);

    // 2. Persist
    const resource = await this.db.resource.create({ data });

    // 3. Side effects
    await this.eventBus.emit('resource.created', resource);

    return resource;
  }

  async findAll(filters: FilterDTO): Promise<PaginatedResult<Resource>> {
    // Check cache first
    const cacheKey = `resources:${JSON.stringify(filters)}`;
    const cached = await this.cache.get(cacheKey);
    if (cached) return cached;

    // Query with pagination
    const result = await this.db.resource.findMany({
      where: filters,
      take: filters.pageSize,
      skip: filters.page * filters.pageSize,
      orderBy: { created_at: 'desc' },
    });

    await this.cache.set(cacheKey, result, { ttl: 300 });
    return result;
  }
}
```

### Error Handling Pattern

```typescript
// Custom error classes with HTTP status
class AppError extends Error {
  constructor(
    public statusCode: number,
    message: string,
    public code?: string,
  ) {
    super(message);
  }
}

class NotFoundError extends AppError {
  constructor(resource: string, id: string) {
    super(404, `${resource} with id ${id} not found`, 'NOT_FOUND');
  }
}

class ValidationError extends AppError {
  constructor(message: string) {
    super(400, message, 'VALIDATION_ERROR');
  }
}

// Global error handler middleware
function errorHandler(err: Error, req: Request, res: Response, next: NextFunction) {
  if (err instanceof AppError) {
    return res.status(err.statusCode).json({
      error: { code: err.code, message: err.message },
    });
  }
  // Unknown errors → 500
  logger.error({ err }, 'Unhandled error');
  return res.status(500).json({
    error: { code: 'INTERNAL_ERROR', message: 'An unexpected error occurred' },
  });
}
```

## Authentication & Authorization

### JWT-Based Auth

```typescript
interface AuthStrategy {
  provider: 'local' | 'oauth';
  tokenExpiry: '1h';
  refreshExpiry: '7d';
  mfa: boolean;
}

// RBAC implementation
enum Role {
  USER = 'user',
  ADMIN = 'admin',
}

// Middleware chain
// authenticate() → validates JWT
// authorize(role) → checks permissions
// rateLimiter() → prevents abuse
```

## Security Headers

```javascript
// Helmet.js configuration
{
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      scriptSrc: ["'self'"],
      imgSrc: ["'self'", "data:", "https:"],
    }
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true
  }
}
```

## Performance Optimization

### Caching Strategy

| Layer | What to Cache | TTL |
|-------|--------------|-----|
| Browser | Static assets | 1 year |
| CDN | Images/media | CloudFront/Cloudflare |
| Application | Sessions, hot data | Redis, minutes-hours |
| Database | Query results | Seconds-minutes |

### Query Optimization

```javascript
// Only select needed fields
const results = await db.query({
  select: ['id', 'name'],
  where: { indexed_field: value },
  limit: 20,
  offset: page * 20,
});
```

### Key Principles

- Index all foreign keys and frequently filtered columns
- Use connection pooling
- Paginate all list endpoints
- Use database-level constraints (NOT NULL, UNIQUE, CHECK)
- Prefer database transactions for multi-step operations
