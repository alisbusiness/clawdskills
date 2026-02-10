# CSS House Style

Detailed CSS rules from the Springer Nature Frontend Playbook. Load this file when writing or reviewing CSS/SCSS.

## Table of Contents
- [General Principles](#general-principles)
- [Code Style](#code-style)
- [Linting](#linting)
- [Preprocessors](#preprocessors)
- [Nesting Rules](#nesting-rules)

## General Principles

Write CSS using design patterns that maximise maintainability and reuse. Namespace CSS using the component namespace pattern (`.c-*` for components, `.u-*` for utilities).

## Code Style

### Avoid HTML tags in selectors — prefer classes

```scss
// ✗ Don't
div {}
div.c-modal {}

// ✓ Do
.c-modal {}
```

### Never use IDs in selectors

```scss
// ✗ Don't
#header {}

// ✓ Do
.c-header {}
```

### Avoid `margin-top` — vertical margins collapse

```scss
// ✗ Don't
.c-list__item {
    margin-top: 10px;
}

// ✓ Do
.c-list__item {
    padding-top: 10px;
}

// ✓ Also acceptable
.c-list__item {
    margin-bottom: 10px;
}
```

### Avoid shorthand properties unless setting all values

```scss
// ✗ Don't — overrides background-image and other values
.c-modal {
    background: $white;
    border: 1px;
}

// ✓ Do
.c-modal {
    background-color: $white;
    border-width: 1px;
}
```

### Never use `!important`

If you must, leave a comment explaining why, and prioritise fixing the specificity issue.

## Linting

- CSS (not compiled) → lint with [Stylelint](https://github.com/stylelint/stylelint).
- Sass → lint with [Stylelint](https://stylelint.io/) using the [Springer Nature `stylelint-config`](https://github.com/springernature/stylelint-config-springernature).

## Preprocessors

Preferred preprocessor: **Sass** using **SCSS syntax**.

## Nesting Rules

Nesting increases specificity and creates maintenance problems. Avoid nesting selectors more than **3 levels** deep.

**Only nest for these cases:**

### 1. Pseudo selectors and state selectors

```scss
a {
    &:hover {
        text-decoration: underline;
    }
    &:focus {
        outline: 1px dashed #000;
    }
}

span {
    &::before {
        content: '\2022';
    }
}
```

### 2. JavaScript-only style enhancements

```scss
.c-class {
    display: block;

    .js & {
        display: flex;
    }
}
```

### 3. Inline HTML tags within other elements

```scss
.c-class {
    span {}
    em {}
    small {}
}
```

### 4. Media queries (nested, placed after declarations)

```scss
// ✗ Don't — media queries before declarations
.c-header__journal-title {
    @include media-query('md') {
        font-size: 1.25rem;
    }
    font-size: 1rem;
    color: #000;
}

// ✓ Do — declarations first, then media queries
.c-header__journal-title {
    font-size: 1rem;
    color: #000;

    @include media-query('md') {
        font-size: 1.25rem;
    }

    @include media-query('lg') {
        font-size: 1.5rem;
    }
}
```
