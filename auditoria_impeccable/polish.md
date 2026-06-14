# Impeccable Polish Report: Biblioteca

Below are the findings for microscopic alignments and polish across the HTML/CSS and JS files in the `biblioteca` project, checked against the "Impeccable Polish" heuristics.

## 1. Design System & Token Drift
- **Missing Tokens**: Both `keller-casamento.html` and `maquiavel-pedagogo.html` use `var(--text-muted)` for the back link color, and `var(--accent)` for the chapter navigation links. Neither of these tokens exist in `assets/style.css`. This causes them to fall back to the browser's default colors (or inherit black), breaking the intended color hierarchy. They should use `var(--gray-dark)` and `var(--green)` respectively, or the tokens should be formally added to `:root`.
- **Inline Style Sprawl**: The book detail pages (`keller-casamento.html`, `maquiavel-pedagogo.html`) contain massive amounts of inline styles for tables, lists, and links instead of abstracting these into the stylesheet. This makes the code harder to maintain and ensures inconsistent spacing/colors over time.
- **Hardcoded Colors**: In `script.js`, the error state uses `color: red;`. This bypasses the design system completely. If there is no `--error` token, one should be added, or it should leverage an existing brand color in a thoughtful way.

## 2. Micro-interactions & Transitions
- **Hover Jank on Index Cards**: In `style.css` (appended section), `a.card:hover` adds a `box-shadow` and `transform`. However, the transition defined on `.card` (line 155) only covers `background-color`, `border-color`, and `transform`. Because `box-shadow` is not transitioned, it snaps instantly on hover and mouse-out, causing a janky micro-interaction. You must add `box-shadow 200ms var(--ease-out-quart)` to the `.card` transition rule.
- **Dead Interactive Elements**: The chapter navigation links at the bottom of the book pages are styled inline with borders and backgrounds to look like clickable cards/buttons, but they lack any `:hover`, `:focus`, or `:active` states. This makes them feel completely "dead" to the user until clicked.

## 3. Information Architecture & Flow
- **Loading & Empty States**: The `script.js` handles loading and empty states by injecting a raw `<p>` tag. A polished experience should use a skeletal loading state (or a spinner aligned with the brand) and a welcoming empty state (perhaps with an icon or illustration) rather than bare, center-aligned text.

## 4. Accessibility & Focus
- **Focus Indicators**: The `a.card` on the index page and the chapter links on the detail pages do not have custom `:focus-visible` styles. While browsers provide a default, a polished product customizes the focus ring to match the brand (e.g., a `--green` outline with an offset) so it integrates seamlessly with the design system.

## Recommendations for Immediate Fixes
1. **Fix the Box-Shadow Transition**: Update `.card` in `style.css` to transition the box-shadow so the hover effect on the index page is buttery smooth.
2. **Resolve Missing Tokens**: Add `--text-muted` and `--accent` to `:root` in `style.css`, or replace them in the HTML with existing tokens like `--gray-dark` and `--green`.
3. **Extract Inline Styles**: Move the chapter links' inline styles to a class (e.g., `.chapter-link`) in `style.css` and give them a proper `:hover` state (like a slight background color shift or border color change).
4. **Tokenize Error States**: Change `color: red;` in `script.js` to a design system color or a new `--error-color` token.
