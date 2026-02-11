---
name: frontend-playbook
description: Frontend development practices, architecture patterns, design systems, and quality standards. Use when writing, reviewing, or architecting frontend code. Covers house style (code formatting, naming, linting), component architecture, design system implementation, accessibility (WCAG 2.1 AA), progressive enhancement, browser support, visual verification, responsive design, performance optimization, and code review. Triggers on frontend code generation, review, refactoring, component architecture decisions, design system setup, or when the user asks about frontend best practices, coding standards, or accessibility compliance.
---

# Frontend Playbook

Production frontend standards distilled from the [Springer Nature Frontend Playbook](https://github.com/springernature/frontend-playbook). Apply these rules whenever generating, reviewing, or refactoring frontend code.

## Core Constraints

1. Products are used globally, across infinite device/OS/network/browser/screen/interface combinations.
2. All output MUST conform to **WCAG 2.1 AA**.
3. All output MUST use **progressive enhancement**, not graceful degradation.

## House Style — General Principles

### Indentation

- Use **tabs** for indentation (accessibility: users set their own render width).
- Exception: YAML files and `package.json` use **2 spaces** (tool compatibility).

### Linting

- CSS → [Stylelint](https://stylelint.io/) with `stylelint-config-springernature`.
- JavaScript → [ESLint](https://eslint.org/) with `eslint-config-springernature`.

### Accessibility

Target: **WCAG 2.1 AA**. Meets EU EN 301 549, US Section 508, UK Equality Act 2010.

Key rules:
- Semantic HTML first; never use ARIA to compensate for abused semantics.
- Every `<img>` needs meaningful `alt` text (or `alt=""` if decorative).
- All interactive elements must be keyboard-operable with visible focus.
- Colour contrast ≥ 4.5:1 for normal text, ≥ 3:1 for large text.
- Do not use ARIA roles/properties without testing with assistive tech.

For detailed guidance → read `references/accessibility.md`.

### Progressive Enhancement & Browser Support

- Start with semantic HTML that works without CSS or JS.
- Layer CSS for visual enhancement; layer JS for behavioural enhancement.
- Use feature detection, not browser sniffing.
- "Core" = server-rendered HTML + minimal CSS for all browsers.
- "Enhanced" = full CSS + JS for modern/evergreen browsers (detected via CSS media query, not JS).

For full details → read `references/progressive-enhancement.md`.

### Code Review Checklist

When reviewing frontend code, check for:

| Category | Look for |
|---|---|
| **Accessibility** | WCAG violations, missing alt text, keyboard traps, colour contrast |
| **Complexity** | Over-engineering, unnecessary dependencies, outdated deps |
| **Performance** | Premature optimisation, non-performant patterns (use Lighthouse) |
| **Scope** | Non-atomic PRs that mix concerns; code that should be a reusable module |
| **Security** | Dependencies with known vulnerabilities (`npm audit`) |
| **Syntax** | Style violations the linter didn't catch |

## Architecture & Design Systems

For frontend project structure, component architecture, design system setup (CSS variables, tokens, typography), responsive design implementation, and visual verification workflow → read `references/architecture-and-design.md`.

### Key Architecture Principles

- **Component-driven**: Small, single-purpose, testable components
- **Design tokens over raw values**: Never use raw hex/pixel values — use CSS variables
- **Mobile-first responsive**: Start mobile, enhance for larger viewports
- **Performance budget**: Core Web Vitals in green zone

## Quality Standards

### Design Quality Requirements

- Use design tokens only — no raw hex/pixel values in component code
- WCAG 2.1 AA verified on every component
- Core Web Vitals in green zone
- Test on mobile before desktop

### What Frontend Code Will NOT Accept

- Placeholder content ("Lorem ipsum") in production
- Skipped accessibility testing
- Skipped mobile testing
- Features outside current phase scope
- Deprecated patterns when modern alternatives exist

## Technology-Specific Guides

Load the relevant reference file based on the code being written or reviewed:

- **CSS** → `references/css-house-style.md` — selectors, naming, nesting, preprocessors, shorthand avoidance.
- **JavaScript** → `references/javascript-house-style.md` — module architecture, variables, functions, async patterns, DOM binding, directory structure.
- **Accessibility** → `references/accessibility.md` — WCAG conformance, ARIA usage, testing, VPATs.
- **Progressive Enhancement** → `references/progressive-enhancement.md` — implementation strategy, browser support tiers, CTM technique.
- **Architecture & Design** → `references/architecture-and-design.md` — project structure, component patterns, design systems, visual verification, performance.
- **Icons** → `references/icons.md` — no-emoji rule, Lucide installation, usage patterns, accessibility, common icon mappings, troubleshooting.

## Quick-Reference Rules (Always Apply)

### HTML / Markup
- Use HTML5 semantic elements (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<footer>`).
- One `<h1>` per page; heading hierarchy must not skip levels.
- Ordered lists: always use `1.` (auto-numbering); unordered lists: use `-`.

### CSS
- Never use IDs in selectors → use classes with component namespace (`.c-*`).
- Never use HTML tag selectors alone → always prefer a class.
- Avoid `margin-top` → use `padding-top` or `margin-bottom` on preceding elements.
- Avoid shorthand properties unless setting all values (`background-color` not `background`).
- Never use `!important` without a comment and prior attempt to fix specificity.
- Nest selectors max **3 levels** deep; nest only for pseudo/state selectors, `.js &` enhancements, inline tags, and media queries.
- Place media queries **after** the CSS declarations for that block.

### JavaScript
- Progressively enhance — JS is an enhancement layer, not a requirement.
- Code for humans — descriptive names, self-documenting code, no clever hacks.
- Modules over monoliths — small, single-purpose, testable modules.
- KISS — `Math.floor(n)` not `~~n`; `% 2` not bitwise `& 1`.
- Use `const` by default; `let` only when mutation is needed; avoid `var`.
- Use strict equality (`===`, `!==`), never loose equality.
- Use named exports (`export {init}`), not default exports.
- Use `async/await` over callbacks; use `Promise.all` for parallel.
- DOM binding via `data-component-*` attributes, not classes or IDs.
- Test hooks via `data-test="component-name"` attributes.
- Keep pure functions where possible.
- Directory structure: `components/` (DOM-binding), `utils/` (pure logic), `vendor/` (third-party), `main.js` (orchestrator).
- Be careful with transpiling — profile bundle size impact (e.g., avoid `for...of`).

### Written Communication
- Use inclusive language in all documentation and open-source writing.

## Icons

For full icon rules, installation guides, usage patterns per framework, accessibility, styling, a common icon mapping table, and troubleshooting → read `references/icons.md`.

### No Emojis as Icons

- **MUST NOT** use emojis (e.g. 📁, ✏️, ❌, ➕) as icons, buttons, or UI indicators. Emojis render inconsistently across platforms, are not stylable, and lack proper accessibility semantics.
- Emojis MAY only be used in **prose text** where they serve a communicative purpose (e.g., a chat message or a friendly greeting), never as functional UI elements.
- All icons MUST come from the **[Lucide](https://lucide.dev/icons/)** icon library.

### Why Lucide

- Open-source, consistent 24×24 SVG icon set with 1,500+ icons.
- Fully tree-shakable — only the icons you import are bundled.
- Framework-specific packages for React, Vue, Svelte, Angular, Solid, Preact, and Astro.
- Stylable via standard CSS/SVG attributes (`color`, `size`, `strokeWidth`).
- Accessible — renders inline `<svg>` elements that support `aria-label` and `role` attributes.

### Installation

Choose the package that matches your project's stack:

| Stack | Package | Install |
|---|---|---|
| Vanilla HTML/JS | `lucide` | `npm install lucide` |
| React | `lucide-react` | `npm install lucide-react` |
| Vue 3 | `lucide-vue-next` | `npm install lucide-vue-next` |
| Svelte | `lucide-svelte` | `npm install lucide-svelte` |
| Angular | `lucide-angular` | `npm install lucide-angular` |
| Solid | `lucide-solid` | `npm install lucide-solid` |
| Preact | `lucide-preact` | `npm install lucide-preact` |
| Astro | `@lucide/astro` | `npm install @lucide/astro` |

For CDN usage (no bundler), include via unpkg:

```html
<script src="https://unpkg.com/lucide@latest"></script>
```

### Usage

#### Vanilla HTML/JS

Add `data-lucide` attributes to elements in your HTML, then call `createIcons()`:

```html
<!-- In your HTML -->
<i data-lucide="menu"></i>
<i data-lucide="search"></i>
<i data-lucide="x"></i>

<!-- Before closing </body> -->
<script src="https://unpkg.com/lucide@latest"></script>
<script>
  lucide.createIcons();
</script>
```

With ES Modules (recommended — enables tree-shaking):

```js
// Only import the icons you actually use
import { createIcons, Menu, Search, X } from 'lucide';

createIcons({
  icons: { Menu, Search, X }
});
```

#### React

Import icons as components. Each icon is individually tree-shaken:

```jsx
import { Camera, Trash2, Plus } from 'lucide-react';

const App = () => (
  <div>
    <Camera size={24} color="currentColor" />
    <Trash2 size={20} strokeWidth={1.5} />
    <Plus size={16} />
  </div>
);
```

Available props: `size` (number, default 24), `color` (string, default `currentColor`), `strokeWidth` (number, default 2), `absoluteStrokeWidth` (boolean).

#### Vue 3

```vue
<script setup>
import { Camera, Trash2, Plus } from 'lucide-vue-next';
</script>

<template>
  <Camera :size="24" color="currentColor" />
  <Trash2 :size="20" :stroke-width="1.5" />
  <Plus :size="16" />
</template>
```

### Icon Best Practices

- **Always tree-shake**: Import individual icons, not the entire library.
  - ✅ `import { Menu, X } from 'lucide-react';`
  - ❌ `import * as icons from 'lucide-react';`
- **Use `currentColor`** for icon colour so they inherit from the parent's CSS `color` property.
- **Pair icons with accessible labels**: If an icon is the only content of a button, add `aria-label` to the button.
  ```html
  <button aria-label="Close"><i data-lucide="x"></i></button>
  ```
- **Consistent sizing**: Stick to the design system's size scale (e.g. 16, 20, 24) rather than arbitrary pixel values.
- **Browse available icons** at [lucide.dev/icons](https://lucide.dev/icons/) — use the search to find the right icon by name or keyword.

## RFC 2119 Key Words

The words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, NOT RECOMMENDED, MAY, and OPTIONAL follow [BCP 14](https://www.rfc-editor.org/info/bcp14) when in ALL CAPS.
