# Impeccable Typeset Audit: Biblioteca Project

Based on the Impeccable Typeset heuristic, here is a detailed review of the typography in the `biblioteca` project.

## 1. Font Choices & Pairing
**Current State:** The project pairs `Hanken Grotesk` (sans-serif display) with `Literata` (serif body).
**Analysis:** This is a strong choice. It avoids invisible defaults (like Inter or Roboto) and provides genuine structural contrast (Serif + Sans). It successfully matches the "library/book" and "infographic" aesthetic.
**Recommendation:** Keep these fonts. They are well-chosen and give the project a distinct personality.

## 2. Type Scale & Hierarchy
**Current State:** Font sizes are arbitrarily hardcoded across classes (e.g., `0.85rem`, `0.9rem`, `0.95rem`, `1rem`, `1.2rem`, `1.4rem`, `4rem`).
**Analysis:** The scale lacks a consistent mathematical foundation. Values like `0.9rem` and `0.95rem` are too close together, leading to a muddy hierarchy. Furthermore, sizing values are applied directly to classes instead of using a token system.
**Recommendations:**
- **Establish a Modular Scale:** Adopt a consistent ratio (e.g., 1.25 - Major Third) for the type ramp (e.g., `0.8rem` [xs], `1rem` [base], `1.25rem` [md], `1.56rem` [lg], `1.95rem` [xl], `2.44rem` [2xl]).
- **Semantic Tokens:** Define semantic CSS variables (e.g., `--text-caption`, `--text-body`, `--text-subheading`, `--text-heading`) in `:root` and map them to the scale.
- **Fluid Typography:** For the large `.header-title`, replace the media query jump (from `4rem` to `2.5rem`) with a fluid `clamp()` function. Example: `font-size: clamp(2.5rem, 5vw + 1rem, 4rem);`. Keep body text at fixed `rem` sizes.

## 3. Readability & Measure (Line Length)
**Current State:** The layout uses pixel-based max-widths (`max-width: 950px` for the page, `max-width: 750px` for `.header-intro`).
**Analysis:** Pixel-based widths for text containers ignore the font's actual metrics, often pushing line lengths well beyond the comfortable reading range. `750px` of a standard font can easily exceed 90 characters.
**Recommendations:**
- **Use `ch` units:** Bound text containers using character units to maintain the ideal 45–75 character measure. Change the `.header-intro` width to something like `max-width: 65ch;`.
- **Apply to Cards:** Ensure paragraphs inside `.card-details-inner` also respect a comfortable measure if the cards expand.

## 4. Spacing, Rhythm & Polish
**Current State:** 
- Uppercase text uses pixel-based tracking (`letter-spacing: 1px;` or `-1.5px;`).
- Vertical spacing uses mixed arbitrary `rem` margins.
- Standard text rendering rules.
**Analysis:** Pixel-based letter spacing breaks down if the font size scales. Vertical rhythm is close, but not strictly tied to the line-height base unit.
**Recommendations:**
- **Relative Tracking:** Use `em` for letter-spacing so it scales with the font. For all-caps labels (like `.header-subtitle` and `.footer-label`), use `letter-spacing: 0.05em;` to `0.12em;`. For tight display headings, use `letter-spacing: -0.02em;`.
- **Vertical Rhythm:** Since body `line-height` is `1.5` (24px at 16px base), try to make vertical margins/paddings multiples of this base (e.g., `1.5rem`, `3rem`) to create subconscious harmony.
- **Rendering Polish:** Add `font-kerning: normal;` and `font-optical-sizing: auto;` to the `body` rule to ensure variable fonts and glyphs render optimally.

## 5. Web Font Loading
**Current State:** Standard `<link>` tags with Google Fonts and `display=swap`.
**Analysis:** This is an acceptable baseline, but it will cause FOUT (Flash of Unstyled Text), leading to layout shifts.
**Recommendation:** 
- To prevent layout jumping when fonts load, define metric-matched `@font-face` fallbacks utilizing `size-adjust`, `ascent-override`, and `descent-override` so the fallback `system-ui` occupies the exact same dimensions as `Literata` and `Hanken Grotesk`.
