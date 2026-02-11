# Icons Reference

Detailed icon rules and Lucide usage guide. Load this file when writing or reviewing any frontend code that involves icons or visual indicators.

## Table of Contents
- [Core Rule: No Emojis as Icons](#core-rule-no-emojis-as-icons)
- [Lucide Overview](#lucide-overview)
- [Installation by Framework](#installation-by-framework)
- [Usage Patterns](#usage-patterns)
- [Styling Icons](#styling-icons)
- [Accessibility](#accessibility)
- [Common Icon Mappings](#common-icon-mappings)
- [Troubleshooting](#troubleshooting)

---

## Core Rule: No Emojis as Icons

Emojis MUST NOT be used as icons, buttons, indicators, or any functional UI element. This is a hard rule with no exceptions.

### Why emojis fail as UI icons

| Problem | Detail |
|---|---|
| **Inconsistent rendering** | Emojis look different on macOS, Windows, Android, and Linux. A 📁 on Safari is a completely different shape/colour on Chrome for Windows. |
| **Not stylable** | You cannot change an emoji's colour, stroke width, or size independently. They don't respond to CSS `color` or `fill`. |
| **Inaccessible** | Screen readers may announce emojis inconsistently or not at all. There is no reliable way to provide semantic meaning. |
| **Unprofessional** | Emojis carry an informal tone that undermines UI credibility in production applications. |
| **No dark-mode support** | Emojis don't invert or adapt to colour schemes — they stay the same regardless of theme. |

### When emojis ARE acceptable

- In **user-generated content** (chat messages, comments, posts).
- In **informal prose** within documentation where they add personality (e.g. "Welcome back! 👋").
- **Never** in navigation, buttons, toolbars, sidebars, status indicators, form labels, or any interactive/functional element.

---

## Lucide Overview

[Lucide](https://lucide.dev) is an open-source icon library forked from Feather Icons. It provides:

- **1,500+ icons** in a consistent 24×24 SVG grid.
- **Fully tree-shakable** — only imported icons are bundled.
- **Framework packages** for React, Vue, Svelte, Angular, Solid, Preact, and Astro.
- **Customisable** via props: `size`, `color`, `strokeWidth`, `absoluteStrokeWidth`.
- **MIT licensed** — free for commercial use.

Browse all icons: [lucide.dev/icons](https://lucide.dev/icons/)

---

## Installation by Framework

### Vanilla HTML/JS

```bash
npm install lucide
```

Or via CDN (no build step):

```html
<script src="https://unpkg.com/lucide@latest"></script>
```

### React

```bash
npm install lucide-react
```

### Vue 3

```bash
npm install lucide-vue-next
```

### Vue 2

```bash
npm install lucide-vue
```

### Svelte

```bash
npm install lucide-svelte
```

### Angular

```bash
npm install lucide-angular
```

### Solid

```bash
npm install lucide-solid
```

### Preact

```bash
npm install lucide-preact
```

### Astro

```bash
npm install @lucide/astro
```

---

## Usage Patterns

### Vanilla HTML/JS — CDN

Place `data-lucide` attributes in your HTML, then initialise:

```html
<!DOCTYPE html>
<html lang="en">
<body>
  <button aria-label="Open menu">
    <i data-lucide="menu"></i>
  </button>
  <button aria-label="Search">
    <i data-lucide="search"></i>
  </button>

  <script src="https://unpkg.com/lucide@latest"></script>
  <script>
    lucide.createIcons();
  </script>
</body>
</html>
```

### Vanilla HTML/JS — ES Modules (tree-shaken)

```js
import { createIcons, Menu, Search, X, ChevronDown } from 'lucide';

// Only these four icons will be bundled
createIcons({
  icons: { Menu, Search, X, ChevronDown }
});
```

```html
<i data-lucide="menu"></i>
<i data-lucide="search"></i>
<i data-lucide="x"></i>
<i data-lucide="chevron-down"></i>
```

### React

Each icon is a standalone component:

```jsx
import { Menu, Search, X, ChevronDown, Plus, Trash2 } from 'lucide-react';

function Toolbar() {
  return (
    <nav>
      <button aria-label="Menu">
        <Menu size={20} />
      </button>
      <button aria-label="Search">
        <Search size={20} />
      </button>
      <button aria-label="Add item">
        <Plus size={16} strokeWidth={2.5} />
      </button>
      <button aria-label="Delete">
        <Trash2 size={16} color="var(--color-danger)" />
      </button>
    </nav>
  );
}
```

**Available props:**

| Prop | Type | Default | Description |
|---|---|---|---|
| `size` | `number` | `24` | Width and height in pixels |
| `color` | `string` | `currentColor` | Stroke colour |
| `strokeWidth` | `number` | `2` | Stroke width |
| `absoluteStrokeWidth` | `boolean` | `false` | If true, stroke width doesn't scale with size |

### Vue 3

```vue
<script setup>
import { Menu, Search, X, Plus } from 'lucide-vue-next';
</script>

<template>
  <nav>
    <button aria-label="Menu">
      <Menu :size="20" />
    </button>
    <button aria-label="Search">
      <Search :size="20" />
    </button>
    <button aria-label="Add">
      <Plus :size="16" :stroke-width="2.5" />
    </button>
  </nav>
</template>
```

### Svelte

```svelte
<script>
  import { Menu, Search, X } from 'lucide-svelte';
</script>

<button aria-label="Menu">
  <Menu size={20} />
</button>
<button aria-label="Search">
  <Search size={20} />
</button>
```

---

## Styling Icons

### Inherit colour from parent

Lucide icons default to `currentColor`, so they inherit from the parent's CSS `color`:

```css
.c-sidebar__link {
  color: var(--color-text-secondary);
}

.c-sidebar__link:hover {
  color: var(--color-text-primary);
}
/* The Lucide icon inside will automatically follow these colours */
```

### Sizing with design tokens

Stick to the design system's size scale — don't use arbitrary values:

```jsx
// ✅ Do — consistent scale
<Menu size={16} />   // small
<Menu size={20} />   // default
<Menu size={24} />   // large

// ❌ Don't — arbitrary sizes
<Menu size={17} />
<Menu size={22} />
```

### Adding transitions

```css
.c-icon {
  transition: color 150ms ease, transform 150ms ease;
}

.c-icon:hover {
  transform: scale(1.1);
}
```

### Dark mode

Since icons use `currentColor` by default, they adapt automatically when your colour variables change:

```css
:root {
  --color-icon: #1a1a2e;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-icon: #e0e0e0;
  }
}
```

---

## Accessibility

### Icon-only buttons MUST have `aria-label`

If a button contains only an icon and no visible text, it MUST have an `aria-label`:

```html
<!-- ✅ Accessible -->
<button aria-label="Close dialog">
  <i data-lucide="x"></i>
</button>

<!-- ❌ Inaccessible — screen reader announces nothing meaningful -->
<button>
  <i data-lucide="x"></i>
</button>
```

### Decorative icons

If an icon appears alongside visible text and is purely decorative, hide it from screen readers:

```jsx
<button>
  <Trash2 size={16} aria-hidden="true" />
  <span>Delete</span>
</button>
```

### Focus visibility

Ensure icon buttons have visible focus indicators:

```css
.c-icon-button:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}
```

---

## Common Icon Mappings

Use this table as a quick reference when choosing icons for standard UI actions. Search for more at [lucide.dev/icons](https://lucide.dev/icons/).

| Action / Concept | Lucide Icon Name | Import Name |
|---|---|---|
| Menu / hamburger | `menu` | `Menu` |
| Close / dismiss | `x` | `X` |
| Search | `search` | `Search` |
| Settings / gear | `settings` | `Settings` |
| User / profile | `user` | `User` |
| Home | `home` | `Home` |
| Add / create | `plus` | `Plus` |
| Delete / remove | `trash-2` | `Trash2` |
| Edit / pencil | `pencil` | `Pencil` |
| Save | `save` | `Save` |
| Copy | `copy` | `Copy` |
| Download | `download` | `Download` |
| Upload | `upload` | `Upload` |
| Share | `share-2` | `Share2` |
| Link | `link` | `Link` |
| External link | `external-link` | `ExternalLink` |
| Expand / chevron down | `chevron-down` | `ChevronDown` |
| Collapse / chevron up | `chevron-up` | `ChevronUp` |
| Back / chevron left | `chevron-left` | `ChevronLeft` |
| Forward / chevron right | `chevron-right` | `ChevronRight` |
| Arrow right | `arrow-right` | `ArrowRight` |
| Arrow left | `arrow-left` | `ArrowLeft` |
| Check / success | `check` | `Check` |
| Warning / alert | `alert-triangle` | `AlertTriangle` |
| Error / circle alert | `circle-alert` | `CircleAlert` |
| Info | `info` | `Info` |
| Help / question | `circle-help` | `CircleHelp` |
| Eye / show | `eye` | `Eye` |
| Eye off / hide | `eye-off` | `EyeOff` |
| Lock | `lock` | `Lock` |
| Unlock | `unlock` | `Unlock` |
| Calendar | `calendar` | `Calendar` |
| Clock / time | `clock` | `Clock` |
| Mail / email | `mail` | `Mail` |
| Phone | `phone` | `Phone` |
| Image / photo | `image` | `Image` |
| File | `file` | `File` |
| Folder | `folder` | `Folder` |
| Star / favourite | `star` | `Star` |
| Heart / like | `heart` | `Heart` |
| Bell / notifications | `bell` | `Bell` |
| Filter | `filter` | `Filter` |
| Sort | `arrow-up-down` | `ArrowUpDown` |
| Refresh / reload | `refresh-cw` | `RefreshCw` |
| Undo | `undo-2` | `Undo2` |
| Redo | `redo-2` | `Redo2` |
| More options (horizontal) | `more-horizontal` | `MoreHorizontal` |
| More options (vertical) | `more-vertical` | `MoreVertical` |
| Drag handle | `grip-vertical` | `GripVertical` |
| Loading / spinner | `loader-2` | `Loader2` |
| Moon / dark mode | `moon` | `Moon` |
| Sun / light mode | `sun` | `Sun` |
| Log out | `log-out` | `LogOut` |
| Log in | `log-in` | `LogIn` |

---

## Troubleshooting

### Icons not rendering (vanilla JS)

- Ensure `lucide.createIcons()` is called **after** the DOM is loaded.
- Verify the `data-lucide` attribute matches a valid icon name (use kebab-case: `chevron-down`, not `ChevronDown`).
- If using ES Modules, confirm the icon is included in the `icons` object passed to `createIcons()`.

```js
// ✅ Correct
document.addEventListener('DOMContentLoaded', () => {
  lucide.createIcons();
});
```

### Icons not rendering (React/Vue)

- Verify the package is installed: `npm ls lucide-react` or `npm ls lucide-vue-next`.
- Import names use **PascalCase**: `ChevronDown`, not `chevron-down`.
- Ensure you are importing from the correct package (`lucide-react`, not `lucide`).

### Icons look blurry

- Avoid scaling icons to non-standard sizes. Lucide icons are designed on a 24×24 grid — use multiples or the standard sizes (16, 20, 24, 32).
- If using CSS transforms like `scale()`, make sure the base size is correct first.

### Icons not adapting to dark mode

- Ensure icons use `currentColor` (the default) and are not hardcoded with a colour value.
- Verify your CSS custom properties update correctly in dark mode.

### Bundle size too large

- You are likely importing the entire library. Always import individual icons:

```js
// ❌ Imports everything (~200KB+)
import { createIcons, icons } from 'lucide';
createIcons({ icons });

// ✅ Imports only what you need (~2KB)
import { createIcons, Menu, X } from 'lucide';
createIcons({ icons: { Menu, X } });
```
