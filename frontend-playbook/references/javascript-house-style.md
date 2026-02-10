# JavaScript House Style

Detailed JavaScript rules from the Springer Nature Frontend Playbook. Load this file when writing or reviewing JavaScript.

## Table of Contents
- [General Principles](#general-principles)
- [Code Style](#code-style)
- [Client-Side Architecture](#client-side-architecture)
- [DOM Binding](#dom-binding)
- [Directory Structure](#directory-structure)
- [Transpiling Caveats](#transpiling-caveats)

## General Principles

### Progressively enhance
JavaScript MUST exist purely as a progressive enhancement of existing functionality.

### Code for humans
Optimise for readability first. Use descriptive method names and variables. Assume no prior knowledge from contributors.

```js
// ✗ Don't
function load(file, cb) {
    fs.readFile(file, function(e, config) {
        if (e) return cb(e);
        cb(null, process(config));
    });
}

// ✓ Do
function loadConfigFile(filePath, callback) {
    fs.readFile(filePath, function(error, fileContents) {
        if (error) {
            return callback(error);
        }
        const config = processConfig(fileContents);
        callback(null, config);
    });
}
```

### Modules over monoliths
Think in small, single-purpose modules. Break generic/reusable code into separate npm-managed modules. Prefer installing a dependency over reinventing the wheel.

### Keep it simple (KISS)
Duplication is far cheaper than the wrong abstraction.

```js
// ✗ Don't
~~number;
// ✓ Do
Math.floor(number);

// ✗ Don't
function isOdd(number) { return !!(number & 1); }
// ✓ Do
function isOdd(number) { const mod = number % 2; return (mod !== 0); }
```

### Performant code
Write fast code, but not at the expense of readability. Don't optimise unless profiling shows you need to.

## Code Style

### Linting
Use [ESLint](https://eslint.org/) with [eslint-config-springernature](https://github.com/springernature/eslint-config-springernature).

### Comments
Code should be self-documenting. Keep comments succinct and factual. Explain *intent*, not *mechanics*.

```js
// ✓ Do — extract to a named variable
const isVisible = el.offsetWidth && el.offsetHeight;
if (isVisible) {}

// ✗ Don't — opaque condition
if (el.offsetWidth && el.offsetHeight) {}
```

Leave comments only for magic numbers or workarounds:
```js
// 42 is the only value the server can handle
fetch('https://example.com/?number=42');
```

Use **JSDoc** for functions with non-obvious parameters:
```js
/**
 * Get a list of book ids from a given library.
 *
 * @param {number} library - Id of the library.
 * @param {number} [limit=10] - Optional max books, defaults to 10.
 * @param {object} [filters={}] - Optional filters.
 * @param {string} [filters.subject] - Subject match string.
 * @returns {number[]} List of book ids.
 */
function getListOfBookIdsFromLibrary(library, limit = 10, filters = {}) {}
```

### Indentation
- Use **tabs** (except `package.json` which uses 2 spaces).
- Follow **BSD-KNF** indent style:

```js
// ✓ Do
if (foo) {
    console.log(foo);
} else {
    console.log(bar);
}
```

### White space
Use white space liberally. Remove trailing white space.

### Variables

Use separate `const`/`let` statements per variable:

```js
// ✓ Do
const foo = 1;
const bar = 2;

// ✗ Don't
const foo = 1,
      bar = 2;
```

Use `const` by default. Use `let` only when reassignment is needed:

```js
// ✓ Do — array mutation doesn't need let
const foo = [1, 2];
if (bar) { foo.push(3); }

// ✗ Don't — unnecessary let
let foo = [1, 2];
if (bar) { foo.push(3); }
```

### Functions

- Use lowerCamelCase naming.
- Never write functions on a single line.

```js
// ✓ Do
function loadConfig(filePaths, callback) { /* ... */ }

// ✗ Don't
function loadconfig(filePaths, callback) { /* ... */ }
```

#### Pure functions
Prefer pure functions — no external state:

```js
// ✓ Do
function greet(greeting, subject) {
    return `${greeting}, ${subject}`;
}

// ✗ Don't
const greeting = 'Hello';
function greet(subject) {
    return `${greeting}, ${subject}`;
}
```

### Operators
Use strict equality only:

```js
// ✓ Do
foo === bar;
foo !== bar;

// ✗ Don't
foo == bar;
foo != bar;
```

### Loops
In `for...in`, always guard with `hasOwnProperty`:

```js
for (const prop in obj) {
    if (Object.prototype.hasOwnProperty.call(obj, prop)) {
        // ...
    }
}
```

### Strict mode
Use `'use strict';` — in Node.js at file top; in browsers inside an IIFE, never globally:

```js
(function () {
    'use strict';
    // ...
})();
```

### Asynchronicity
Prefer `async/await` over callbacks. Use `Promise.all` for parallel operations:

```js
const [response1, response2] = await Promise.all([promise1, promise2]);
```

All `async` functions return promises — you can still chain with `.then()` outside `async` contexts.

## Client-Side Architecture

### Module architecture
Each module has a single purpose and exposes an `init` method. Use **named exports**:

```js
// my-module.js
function init(config) { /* ... */ }
export { init };

// main.js — orchestrator, no logic
import { module1 } from './my-module-1.js';
document.addEventListener('DOMContentLoaded', () => {
    module1.init();
});
```

Pass configuration as objects with defaults:

```js
function module({ url = 'https://...', animate = false }) { /* ... */ }
export { module };
```

### Imports
Import only what you need (tree-shaking ready):

```js
// ✓ Do
import { flatten, merge } from 'lodash';

// ✗ Don't
import _ from 'lodash';
```

### Events

**Related modules** → expose and consume an API directly.

**Unrelated modules** → use custom events dispatched on DOM elements; let the application orchestrate listeners between modules (modules stay isolated).

## DOM Binding

Bind JS to DOM via `data-component-*` attributes, not classes or IDs:

```html
<!-- ✓ Do -->
<button class="c-button" data-component-collapse-activator="header-menu">Menu</button>
<nav class="c-header-menu u-hidden" data-component-collapse-target="header-menu">…</nav>

<!-- ✗ Don't -->
<button class="c-button" data-component="collapse" data-target="header-menu">Menu</button>
```

### Test hooks
Use `data-test="component-name"` for test selectors — never couple tests to CSS classes or IDs.

### Client-side templating
Avoid client-side templating. Prefer rendering HTML server-side and returning fragments via AJAX. `innerHTML` is more efficient than templating a JSON response.

### Polyfills
- MUST NOT override native browser functionality.
- MUST match native browser functionality exactly.
- MUST be served from own domain, never third-party CDNs.
- May be third-party or in-house.

## Directory Structure

```
<root>
  ├── components/     # DOM-binding JS (autocomplete, tabs, spinner)
  ├── utils/          # Pure logic, no DOM (string helpers, formatters)
  ├── vendor/         # Third-party code (versioned filename, source link, unmodified)
  ├── main.js         # Entry point / orchestrator
  └── vendor.js       # Optional — separate bundle for third-party (better caching)
```

File names: lower-case, words separated by dashes.

## Transpiling Caveats

Transpiling can bloat bundle size. Monitor with [Babel REPL](https://babeljs.io/repl/).

```js
// ✗ Don't — for...of transpiles to ~23 lines
const list = document.querySelectorAll('input[type=checkbox]');
for (let checkbox of list) { /* .. */ }

// ✓ Do — transpiles to ~5 lines
const list = document.querySelectorAll('input[type=checkbox]');
Array.prototype.forEach.call(list, function (checkbox) { /* ... */ });
```
