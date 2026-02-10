# Accessibility Guide

Accessibility standards and practices from the Springer Nature Frontend Playbook. Load this file when accessibility conformance, ARIA usage, or inclusive design guidance is needed.

## Table of Contents
- [Why Accessibility Matters](#why-accessibility-matters)
- [Standards](#standards)
- [ARIA Rules](#aria-rules)
- [VPATs](#vpats)
- [Testing](#testing)
- [Common Remediation Areas](#common-remediation-areas)
- [Resources](#resources)

## Why Accessibility Matters

- **It's the right thing to do.** Not making something accessible is knowingly contributing to the exclusion of people with disabilities.
- **It's a legal requirement.** WCAG 2.1 AA is referenced by UK Equality Act 2010, Americans with Disabilities Act, EU Accessibility Act, US Section 508, and UK Accessibility Regulations 2018.
- **It makes financial sense.** ~23% of working-age UK adults have a permanent disability; 57% of computer users 18–64 likely benefit from assistive technology. Temporary and situational disabilities affect everyone.
- **It's a technical requirement.** Accessibility complements progressive enhancement and broad browser support.

## Standards

**Target: WCAG 2.1 Level AA.**

All first and third party web products and components published MUST conform to WCAG 2.1 AA.

### The Four Principles (POUR)

1. **Perceivable** — Information must be presentable in ways all users can perceive.
2. **Operable** — UI components and navigation must be operable by all users.
3. **Understandable** — Information and UI operation must be understandable.
4. **Robust** — Content must be robust enough to work with diverse user agents and assistive technologies.

### Key WCAG Success Criteria to Watch

- 1.1.1 Non-text Content — alt text for images
- 1.3.1 Info and Relationships — semantic HTML structure
- 1.4.3 Contrast (Minimum) — 4.5:1 normal text, 3:1 large text
- 1.4.11 Non-text Contrast — 3:1 for UI components
- 2.1.1 Keyboard — all functionality via keyboard
- 2.4.7 Focus Visible — visible focus indicator
- 4.1.2 Name, Role, Value — proper labelling of interactive elements

## ARIA Rules

1. **Do not use ARIA to compensate for abused semantics.** Use the correct HTML element (`<a>` not `<div role="link">`).
2. **Do not use ARIA roles, properties, or design patterns without understanding what they do.**
3. **Do not use ARIA without testing with assistive technologies.**
4. Follow the [First and Second Rules of ARIA](https://www.w3.org/TR/using-aria/):
   - First Rule: Don't use ARIA if you can use a native HTML element with the semantics you need.
   - Second Rule: Don't change native semantics unless you really have to.

## VPATs

A Voluntary Product Accessibility Template (VPAT) MUST be produced for every product commercially available in the United States:
- Update VPATs when accessibility improves for a criteria.
- MUST NOT regress accessibility below the level detailed in the VPAT.

## Testing

### Automated Tools
- [pa11y](https://github.com/pa11y) — automated accessibility testing.
- [Lighthouse](https://developers.google.com/web/tools/lighthouse/) — auditing.
- Browser dev tools accessibility panels.

### Manual Testing
Automated tools can only catch ~30% of WCAG issues. Manual testing is essential:
- Keyboard navigation (Tab, Shift+Tab, Enter, Escape, Arrow keys).
- Screen reader testing (VoiceOver on macOS, NVDA/JAWS on Windows).
- High contrast mode.
- Zoom to 200%+.

### User Testing
Engage people with disabilities or specialist organisations like the [Digital Accessibility Centre](http://www.digitalaccessibilitycentre.org/).

## Common Remediation Areas

- Missing or poor alt text on images.
- Missing form labels.
- Insufficient colour contrast.
- Keyboard traps or unreachable interactive elements.
- Missing heading hierarchy (skipped levels).
- Missing or incorrect ARIA where needed.
- Focus not managed after dynamic content changes.

## Resources

### Practical Advice
- Writing better alt text.
- Creating accessible emails.
- Creating accessible PDFs.
- Effective colour contrast.

### Learning
- [WCAG 2.1 specification](https://www.w3.org/TR/WCAG21/)
- [Understanding WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/)
- [Techniques for WCAG 2.1](https://www.w3.org/WAI/WCAG21/Techniques/)
- [WAI-ARIA Authoring Practices](http://w3.org/TR/wai-aria-practices/)
- [Microsoft Inclusive Design Toolkit](https://inclusive.microsoft.design/)
