---
target: cheatsheet-cap5/index.html
total_score: 20
p0_count: 0
p1_count: 2
timestamp: 2026-06-10T18-08-23Z
slug: cheatsheet-cap5-index-html
---
## Design Health Score

| # | Heuristic | Score | Key Issue |
|---|-----------|-------|-----------|
| 1 | Visibility of System Status | 2 | No scroll progress indicator; no TOC showing position in page |
| 2 | Match System / Real World | 3 | "Antipadrão" is dev jargon; target audience is church readers |
| 3 | User Control and Freedom | 2 | No in-page navigation; connection tags look clickable but aren't |
| 4 | Consistency and Standards | 3 | Clean internal system; antipadrão cards thinner than others |
| 5 | Error Prevention | 1 | Static page; connection tags create click-trap |
| 6 | Recognition Rather Than Recall | 3 | Color-coded accents aid scanning; bold keywords help |
| 7 | Flexibility and Efficiency | 1 | No keyboard shortcuts, TOC, search, or anchor links |
| 8 | Aesthetic and Minimalist Design | 3 | Clean dark UI, restrained color; 8 cards + 5 lessons is dense |
| 9 | Error Recovery | 1 | Static page; non-interactive tags give no feedback |
| 10 | Help and Documentation | 1 | No intro paragraph, no glossary, no links to book/chapters |
| **Total** | | **20/40** | **Acceptable** |

## Anti-Patterns Verdict

**LLM assessment**: Mostly clean. 6/8 AI slop checks pass clearly. Two borderline flags: (1) card homogeneity — all 8 cards follow icon → h2 → body → optional extra, triggering mild "AI template" pattern; (2) Geist font is increasingly Vercel/AI-associated. No gradient text, no side-stripe borders, no glassmorphism, no numbered section markers, no uppercase tracked eyebrows. The author actively avoids known AI slop patterns with visible intent (CSS comments, full-border blockquotes).

**Deterministic scan**: 1 finding.
- `single-font` (warning) at index.html:10 — "Only one font family is used for the entire page." The detector is correct: **Geist is not available on Google Fonts** and silently fails to load. Only Literata actually renders. The page falls back to `system-ui` for body text, which means the intended font pairing doesn't exist in practice. This is a real bug, not a false positive.

## Overall Impression

A thoughtfully crafted dark-mode cheat sheet with genuine content care and disciplined anti-slop awareness. The theological content is well-distilled, the color system is sophisticated, and accessibility handling (prefers-reduced-motion, aria attributes) is above average. However, it's designed for the designer, not the reader. The target audience (Portuguese-speaking Christian couples) would benefit from lighter mode support, simpler vocabulary ("Antipadrão" → "Armadilha"), actual chapter navigation, and a warmer emotional ending. The broken font pairing is a P1 bug — the intended typographic hierarchy doesn't render.

## What's Working

1. **Disciplined color semantics**: Each card accent maps to a conceptual category — warm tones (rose, amber, orange) for relational concepts, cool tones (blue, emerald, violet) for structural processes, red for warnings. This creates an unconscious taxonomy without explaining it.

2. **Accessibility-first animation**: The `prefers-reduced-motion` handling is exemplary. JS checks it first and skips observer setup entirely. CSS applies `!important` removal. Cards start visible without JS. The animation begins at `opacity: 0.4`, not 0, so content is never fully hidden during transitions.

3. **Content editorial quality**: Cards genuinely distill complex theology into scannable chunks. Bold keywords as entry points, the practical "Fraldas & Café" example, the Tolkien quote, and the Cycle of Reconciliation flow diagram all show editorial care, not template-filling.

## Priority Issues

### [P1] Geist font doesn't load — typographic hierarchy is broken
**What**: Geist is a Vercel-proprietary font not available on Google Fonts. The Google Fonts URL silently fails. Body text falls back to `system-ui`, destroying the intended Literata + Geist contrast.
**Why it matters**: Typography IS the design on a text-heavy page. Without the body font, the page renders with a system fallback that wasn't tested or intended. The entire type scale, weight contrast, and reading experience is accidental.
**Fix**: Replace Geist with a Google Fonts alternative that provides similar geometric sans contrast with Literata. Options: Hanken Grotesk, General Sans (via CDN), or Manrope.
**Suggested command**: `/impeccable typeset cheatsheet-cap5/index.html`

### [P1] Connection tags are deceptive non-links
**What**: Footer `connection-tag` elements are `<span>` tags with hover transitions (background + border-color changes), pill-shaped styling, and chapter names — but they're not `<a>` tags and go nowhere. They sit inside a `<nav aria-label="Capítulos relacionados">` element, which is semantically misleading.
**Why it matters**: Users will click them expecting to navigate to chapter 2, 4, 6, or 8. Nothing happens. A `<nav>` landmark with no links confuses screen readers. This damages trust at the page's only navigation-adjacent element.
**Fix**: Either make them real `<a>` links to other cheat sheet pages, or remove hover effects, drop the `<nav>` wrapper, and style them as inert tags (no transitions, muted color).
**Suggested command**: `/impeccable harden cheatsheet-cap5/index.html`

### [P2] "Antipadrão" jargon alienates the target audience
**What**: The term "Antipadrão" (anti-pattern) is software engineering vocabulary. The target audience is Portuguese-speaking Christian couples studying marriage.
**Why it matters**: Readers in a church small group will not recognize "Antipadrão." It creates a jargon barrier and signals this was built for developers, not for them.
**Fix**: Replace with "Armadilha" (trap), "Erro Comum" (common mistake), or "Cuidado" (caution).
**Suggested command**: `/impeccable clarify cheatsheet-cap5/index.html`

### [P2] Dark-mode-only with no alternative
**What**: The page is hardcoded dark. The CSS has a no-op `prefers-color-scheme: light` media query. No toggle exists.
**Why it matters**: The target demographic (Christian marriage study participants) often skews older and more traditional. Many readers may find dark backgrounds straining. Users who want to print the page will get a mostly-black printout.
**Fix**: Add a full `prefers-color-scheme: light` media query, or implement a manual toggle.
**Suggested command**: `/impeccable colorize cheatsheet-cap5/index.html`

### [P3] No page introduction or navigation structure
**What**: 8 cards + 5 lessons with no intro paragraph explaining what this page is, no table of contents, no section grouping headers, no back-to-top link. Card IDs exist in HTML but aren't surfaced in UI.
**Why it matters**: A first-time visitor from a shared link has zero context. Users on mobile must scroll through 13 content blocks with no orientation. The page front-loads all cognitive weight with no progressive disclosure.
**Fix**: Add a 1-2 sentence intro paragraph. Add a minimal anchor-linked TOC. Group cards visually (e.g., "Entendendo" / "Praticando" / "Evitando").
**Suggested command**: `/impeccable layout cheatsheet-cap5/index.html`

## Persona Red Flags

**Jordan (First-Timer)**: No introductory paragraph explaining what this page is or who it's for. No reading order guidance — wide cards break the left-to-right flow. Connection tags suggest other chapters exist but lead nowhere. "Antipadrão" is unexplained jargon. Will say "what is this?" and leave.

**Sam (Accessibility)**: `aria-hidden` on icons and `aria-labelledby` on sections are correct. But: OKLCH colors have no hex fallbacks for older browsers. `<nav>` wraps non-interactive `<span>` elements — semantically misleading. No skip-to-content link. No `:focus-visible` styles defined. Emoji markers (💡, 🔄) may not be announced consistently by screen readers.

**Casey (Mobile)**: Single-column responsive layout works. But: 13 content blocks in one column = heavy scrolling with no progress indicator or jump nav. Card hover effects (lift, glow, icon rotate) trigger sticky hover bugs on touch. Tip/callout text at 0.82rem may be too small on mobile. No `@media (hover: none)` to disable hover effects on touch devices.

## Minor Observations

1. **`max-width: 65ch` on `.card-body`** — smart typographic constraint but never active within ~400px card widths. Dead code.
2. **No `<meta theme-color>`** — mobile browser chrome won't match the dark background.
3. **No OpenGraph/social meta** — shared links won't generate preview cards.
4. **Emoji as semantic markers** — platform-dependent rendering; consider SVG or `aria-label` augmentation.
5. **Fixed ambient glow** — `position: fixed` at 50vh height means the pink tint follows the viewport, not the header. Distracting when scrolled far down.
6. **Print: SVG icons use `currentColor`** — will render as `#111` on white paper, which works, but untested.

## Questions to Consider

1. **Is the 2-column grid earning its complexity?** Cards of varying heights create ragged bottoms. A single-column layout with generous whitespace might better serve contemplative theological content. Would a linear reading flow match the emotional weight of forgiveness and reconciliation better than a dashboard grid?

2. **Who is the actual reader?** The visual design (dark mode, OKLCH, Geist font) is tuned for a tech/design audience. The content is tuned for church small groups. These audiences want different things. Which reader are you building for?

3. **Should the antipadrão cards look different?** Both use identical card structure with only a red accent bar. A distinct visual treatment (dimmed background, warning icon, different shape) would strengthen the "do this" vs "don't do this" contrast.
