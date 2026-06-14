# Impeccable Shape Audit: Biblioteca Digital

**Date:** 2026-06-10
**Context:** Review of the HTML/CSS structure and UI uniformity across the `biblioteca` project, guided by the Impeccable `shape.md` heuristic.

## 1. Feature Summary & Purpose
The `biblioteca` project serves as an aggregator and display engine for book summaries (cheat sheets). Its primary user action is to allow users to browse available books on the index and dive deep into structured, expandable insights on individual book pages.

## 2. Design Direction
The project successfully establishes a clear visual lane:
* **Color Strategy:** Restrained / Committed (Productivity Infographic Clone). Uses a curated palette (`--green`, `--paper-bg`, `--gray-dark`).
* **Theme Scene:** "A premium, distraction-free study environment where insights are presented like a high-quality physical infographic on textured paper."
* **Typography:** `Hanken Grotesk` (Display) and `Literata` (Body).

**Verdict:** The visual language is strong, opinionated, and consistent in the CSS. However, the HTML implementation is beginning to fragment.

## 3. Layout Strategy & Wireframe Uniformity

The high-level spatial approach (a centered `.page` container, structured `<header>`, `.grid` for content, and a simple `<footer>`) is an excellent, scalable wireframe. However, a closer inspection of `index.html`, `keller-casamento.html`, and `maquiavel-pedagogo.html` reveals architectural drift.

### Successes
* **Grid System:** The 2-column `.grid` gracefully handles varied content chunks.
* **Component Reusability:** The `.card` component is the workhorse of the UI and handles the "Infographic" aesthetic perfectly with its dashed borders and SVG icons.
* **Animation:** `.animate-entrance` creates a smooth, unified loading experience across pages.

### Architectural Drift & Inconsistencies
1. **Asset Referencing (Critical):**
   * `keller-casamento.html` correctly points to the centralized `assets/style.css`.
   * `maquiavel-pedagogo.html` incorrectly points to `maquiavel-pedagogo/style.css` and its own local script. This breaks the single-source-of-truth architecture and prevents global updates from propagating.
2. **Inline Styles (High Priority):**
   * `maquiavel-pedagogo.html` contains significant inline CSS (`style="..."`), particularly for lists, tables, and typography colors inside the cards. This bypasses the design system and will make dark-mode or theme adjustments impossible later.
3. **Card Component Variants (Medium Priority):**
   * The project currently uses two distinct mental models for `.card`:
     * **Content Card (`article.card`):** Used in book pages. Contains SVGs, `.card-title`, `.card-body`, and expandable `.card-details`.
     * **Navigational Card (`a.card`):** Used in `index.html`. Contains a `.card-cover img`.
   * While CSS exists for both, the HTML structure differs enough that they should be formally documented as separate variants to avoid mixing their classes accidentally.
4. **Content Schema Discrepancies (Low Priority):**
   * `keller-casamento.html` ends with a `<section class="lessons">` (Aplicações Práticas). `maquiavel-pedagogo.html` lacks this section entirely.
   * `keller-casamento.html` uses `.card-tip` for secondary context. `maquiavel-pedagogo.html` does not utilize this typography token.

## 4. Key Recommendations for Implementation

To achieve true Impeccable uniformity, the following steps should be executed:

1. **Unify the Asset Pipeline:**
   * Update `maquiavel-pedagogo.html` (and any other book pages) to point to `assets/style.css` and the global `script.js` (or a centralized book-specific script) instead of local subfolder copies.
2. **Extract Inline Styles:**
   * Remove all `style="..."` attributes from `maquiavel-pedagogo.html`.
   * Create dedicated classes in `assets/style.css` for the data table (e.g., `.card-table`) and custom lists (e.g., `.card-list-disc`) that adhere to the existing color variables.
3. **Standardize the Content Schema:**
   * Define a strict template for "Book Cheat Sheets". Decide if the `.lessons` section is mandatory, optional, or irrelevant for certain types of books. If optional, ensure its absence doesn't break the bottom padding/margin of the `.page`.
4. **Consolidate Card Definitions:**
   * Ensure `a.card` and `article.card` have explicitly defined states in the CSS (Hover, Active, Expanded). The recent addition of `append.css` into `assets/style.css` was a good step, but maintaining a clear structural guideline for "Book Cover Cards" vs "Infographic Detail Cards" will prevent layout bugs as the library grows.

## 5. Interaction Model
The interaction model is solid: hovering over cards provides a subtle lift, and clicking expands the `.card-details`. 
* **Note:** Ensure that if `a.card` is ever used to expand details (instead of navigating to a new page), the JS event listeners are strictly bound to prevent default link behaviors. Currently, `a.card` acts as a pure router, and `article.card` acts as an accordion. Keep this separation clean.
