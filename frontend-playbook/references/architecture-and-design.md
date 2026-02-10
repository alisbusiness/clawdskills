# Frontend Architecture & Design Systems

## Table of Contents

- [Project Structure](#project-structure)
- [Component Architecture](#component-architecture)
- [Design System Setup](#design-system-setup)
- [Responsive Design](#responsive-design)
- [Visual Verification](#visual-verification)
- [Performance Optimization](#performance-optimization)

## Project Structure

### Standard Frontend Layout

```
src/
├── app/                 # App router / pages
├── components/
│   ├── ui/              # Base UI components (Button, Card, Input)
│   ├── features/        # Feature-specific components
│   └── layouts/         # Layout components (Header, Footer, Sidebar)
├── lib/
│   ├── api/             # API client / data fetching
│   ├── hooks/           # Custom React/framework hooks
│   ├── utils/           # Pure utility functions
│   └── stores/          # State management (Zustand, etc.)
├── styles/              # Global styles, design tokens
└── types/               # TypeScript type definitions
```

### Key Conventions

- Components are PascalCase (`Button.tsx`, `UserProfile.tsx`)
- Utilities and hooks are camelCase (`useAuth.ts`, `formatDate.ts`)
- One component per file
- Co-locate tests with components (`Button.test.tsx`)
- Co-locate component-specific styles with components

## Component Architecture

### Component Principles

1. **Single responsibility**: Each component does one thing well
2. **Composable**: Build complex UIs from simple, reusable pieces
3. **Prop-driven**: Components are configured via props, not internal state
4. **Testable**: Pure rendering logic, side effects in hooks

### Component Pattern

```tsx
// components/ui/Card.tsx
interface CardProps {
  title: string;
  children: React.ReactNode;
  variant?: 'default' | 'elevated' | 'outlined';
  className?: string;
}

export function Card({ title, children, variant = 'default', className }: CardProps) {
  return (
    <div className={`c-card c-card--${variant} ${className ?? ''}`}>
      <h3 className="c-card__title">{title}</h3>
      <div className="c-card__body">{children}</div>
    </div>
  );
}
```

### State Management

- **Local state**: `useState` for component-specific state
- **Shared state**: Zustand or Context for cross-component state
- **Server state**: TanStack Query for API data (not `useEffect` + `fetch`)
- **URL state**: Search params for filterable/shareable state

## Design System Setup

### CSS Variables (Design Tokens)

```css
:root {
  /* Colors — curated palette, not raw values */
  --color-primary: hsl(230, 75%, 55%);
  --color-primary-hover: hsl(230, 75%, 45%);
  --color-secondary: hsl(280, 60%, 50%);
  --color-surface: hsl(0, 0%, 100%);
  --color-surface-elevated: hsl(0, 0%, 98%);
  --color-text: hsl(0, 0%, 12%);
  --color-text-muted: hsl(0, 0%, 45%);
  --color-border: hsl(0, 0%, 88%);
  --color-error: hsl(0, 70%, 55%);
  --color-success: hsl(145, 65%, 40%);

  /* Typography */
  --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
  --font-heading: 'Outfit', var(--font-sans);
  --font-mono: 'JetBrains Mono', monospace;

  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 2rem;

  /* Spacing scale */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;

  /* Border radius */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
  --radius-xl: 1rem;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.07);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.15);

  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-base: 250ms ease;
  --transition-slow: 350ms ease;
}

/* Dark mode variant */
@media (prefers-color-scheme: dark) {
  :root {
    --color-surface: hsl(0, 0%, 10%);
    --color-surface-elevated: hsl(0, 0%, 14%);
    --color-text: hsl(0, 0%, 92%);
    --color-text-muted: hsl(0, 0%, 60%);
    --color-border: hsl(0, 0%, 25%);
  }
}
```

### Template Selection

When starting a new project, choose a UI component library or template that matches the design vibe:

| Style | Libraries |
|-------|-----------|
| Minimal / Clean | Shadcn/ui, Radix UI |
| Material / Professional | Material UI, Mantine |
| Rich / Premium | Custom with design tokens |
| Rapid Prototype | DaisyUI, Chakra UI |

## Responsive Design

### Mobile-First Breakpoints

```css
/* Mobile first — styles apply to all sizes */
.c-layout { padding: var(--space-4); }

/* Tablet — 768px+ */
@media (min-width: 48rem) {
  .c-layout { padding: var(--space-8); }
}

/* Desktop — 1024px+ */
@media (min-width: 64rem) {
  .c-layout { padding: var(--space-12); max-width: 80rem; margin: 0 auto; }
}
```

### Testing Checklist

- [ ] Works on iPhone SE (375px)
- [ ] Works on standard mobile (390px)
- [ ] Works on tablet (768px)
- [ ] Works on laptop (1024px)
- [ ] Works on desktop (1440px)
- [ ] Touch targets ≥ 44px × 44px
- [ ] No horizontal scrolling on any viewport

## Visual Verification

### Generate-Render-Inspect-Refine Loop

When building or modifying UI components:

1. **Generate**: AI produces component code
2. **Render**: Preview in dev server or headless browser
3. **Inspect**: Screenshot capture + design principle check
4. **Refine**: Fix visual regressions before committing

### Verification Checks

- [ ] Component matches design intent
- [ ] Colors use design tokens, not raw values
- [ ] Typography follows the type scale
- [ ] Spacing is consistent with the spacing scale
- [ ] Hover/focus states are present and visible
- [ ] Animations are smooth (60fps target)
- [ ] Dark mode renders correctly (if applicable)
- [ ] Accessible contrast ratios met

## Performance Optimization

### Code Splitting

```javascript
// Lazy-load non-critical components
const Feature = dynamic(() => import('./Feature'), {
  loading: () => <Skeleton />,
  ssr: false,
});
```

### Core Web Vitals Targets

| Metric | Target | Measures |
|--------|--------|----------|
| LCP (Largest Contentful Paint) | < 2.5s | Loading performance |
| INP (Interaction to Next Paint) | < 200ms | Interactivity |
| CLS (Cumulative Layout Shift) | < 0.1 | Visual stability |

### Performance Checklist

- [ ] Images use modern formats (WebP, AVIF) with `srcset`
- [ ] Fonts preloaded with `font-display: swap`
- [ ] Critical CSS inlined or prioritized
- [ ] Non-critical JS deferred or lazy-loaded
- [ ] No layout shifts from dynamically loaded content
- [ ] Bundle size monitored (use `size-limit` or similar)
