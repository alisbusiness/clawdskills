# Progressive Enhancement & Browser Support

Progressive enhancement and graded browser support practices from the Springer Nature Frontend Playbook. Load this file when implementing browser support tiers, feature detection, or progressive enhancement strategies.

## Table of Contents
- [What Is Progressive Enhancement?](#what-is-progressive-enhancement)
- [Why We Use It](#why-we-use-it)
- [Implementation](#implementation)
- [Browser Support Tiers](#browser-support-tiers)
- [Cutting the Mustard Technique](#cutting-the-mustard-technique)
- [Browserslist Config](#browserslist-config)
- [Common Concerns](#common-concerns)

## What Is Progressive Enhancement?

A design and development practice that delivers the basic essentials first, then builds layers of refinement on top for clients that can receive them:

1. **HTML layer** — logical, semantic, fully functional without CSS or JS.
2. **CSS layer** — aesthetic enhancement using the cascade, specificity, and `@supports`.
3. **JavaScript layer** — behavioural enhancement using feature detection.

**This is NOT graceful degradation.** Graceful degradation starts from the full-fat experience and patches failures after the fact. Progressive enhancement builds resilience in from the start.

## Why We Use It

- **Rule of Least Power** — solve problems with the simplest tool in the stack (HTML > CSS > JS > ARIA).
- **Fault tolerance by design** — JS fails for ~1.1–1.3% of page visits (not users), for reasons mostly outside user control.
- **Lean delivery** — core content loads and works even on slow networks or low-powered devices.
- **Encourages testable MVPs** — core functionality can be validated before layering enhancements.

## Implementation

### CSS Level
Build basic implementations first with primitive CSS. Enhance in advanced browsers using:
- The cascade and specificity.
- Source order.
- Feature queries (`@supports`).

### JavaScript Level
- Support ES5 browsers via transpiling.
- Use **feature detection** to offer more capabilities as the browser supports them.
- JavaScript is always an enhancement, never a requirement.

## Browser Support Tiers

### Core (Universal)
- Server-side rendered semantic HTML + minimal CSS.
- All essential user journeys MUST be accessible at this level.
- Only normalisation CSS and basic branding (max-width layout, colours, logo).

### Enhanced (Modern/Evergreen)
- Full CSS + JavaScript.
- More interactive and visually rich experience.
- Classified via CSS media query detection (not JS-based).

## Cutting the Mustard Technique

Based on BBC's technique. Uses CSS media queries to detect capable browsers, not JavaScript:

### CSS Loading (Enhanced stylesheet)
```html
<link rel="stylesheet" href="enhanced.css"
      media="only print, only all and (prefers-color-scheme: no-preference), only all and (prefers-color-scheme: light), only all and (prefers-color-scheme: dark)"
      id="enhanced-stylesheet">
```

### JS Loading (Coupled to CSS)
```javascript
(function() {
  var linkEl = document.getElementById('enhanced-stylesheet');
  if (window.matchMedia && window.matchMedia(linkEl.media).matches) {
    var script = document.createElement('script');
    script.src = 'enhanced-script.js';
    script.async = true;
    document.body.appendChild(script);
  }
})();
```

This ensures JavaScript only loads when the enhanced CSS also loads — keeping the two in sync.

## Browserslist Config

Use [Autoprefixer](https://github.com/postcss/autoprefixer) for vendor prefixes. Recommended `.browserslistrc`:

```
defaults
not ie 11
ff > 66
chrome > 75
safari > 11
edge > 78
opera > 61
```

## Common Concerns

### "How many users turn JavaScript off?"
The real question is "how many users don't have JavaScript *available*?" JS fails for all kinds of reasons beyond user choice: network failures, ISP injection, browser extensions, corporate proxies, timeouts. ~1.1–1.3% of visits lose JS.

### "So I can't use JavaScript?"
No. Use JavaScript — but use it defensively, assuming it will frequently be unavailable. Many features (like `aria-expanded`) *require* JS. Progressive enhancement means core functionality works without it, and JS adds the enhanced experience.

### "YAGNI — do we really need this?"
Robustness is a core requirement, not an optional feature. JS failure affects a percentage of *visits*, not *users* — it happens to everyone eventually.
