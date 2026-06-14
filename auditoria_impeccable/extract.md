# Auditoria Impeccable: Component & Token Extraction

## 1. Discovery
- **Design System Location**: `assets/style.css` serves as the global stylesheet and design system.
- **Current State**: The CSS uses custom properties (tokens) and has predefined classes (e.g., `.card`, `.header`). However, HTML files contain numerous inline styles that duplicate functionality, use undefined tokens, and violate the DRY principle.

## 2. Patterns Identified

1. **Chapter Navigation Links**:
   Used 24+ times across `keller-casamento.html` and `maquiavel-pedagogo.html`.
   *Inline style*: `style="text-decoration: none; padding: 0.5rem 1rem; border: 1px solid var(--border); border-radius: 4px; color: var(--accent); font-weight: bold; background: rgba(0,0,0,0.02); margin-bottom: 0.5rem; display: block;"`

2. **Back Link Override**:
   Used in both overview HTML files.
   *Inline style*: `style="display:inline-block; margin-bottom: 1.5rem; color: var(--text-muted); text-decoration: none; font-weight: 500;"` overrides the existing `.back-link` class.

3. **List Styling**:
   Used repeatedly in `maquiavel-pedagogo.html` for unordered lists inside cards.
   *Inline style*: `style="list-style-type: disc; margin-left: 1.5rem; color: var(--gray-dark); font-size: 0.95rem; margin-top: 0.5rem; margin-bottom: 1rem;"`

4. **Data Table Styling**:
   Used in `maquiavel-pedagogo.html`.
   *Inline style*: Multiple inline styles for `table`, `th`, `tr`, `td` representing a data table with borders.

## 3. Extraction Plan

### Tokens to Create / Fix
Several inline styles reference undefined CSS variables that need to be added to `:root` in `assets/style.css` (or mapped to existing ones):
- `var(--accent)` -> Map to `var(--green)` or create new.
- `var(--border)` -> Map to `var(--gray-light)` or create new.
- `var(--text-muted)` -> Map to `var(--gray-dark)` or create new.
- `var(--bg-subtle)` -> Extract `rgba(0,0,0,0.02)` as a new background color token.

### Components to Extract
1. **Chapter Nav Link (`.chapter-link`)**:
   Create a CSS class to replace the heavily inline-styled navigation links.
2. **Content List (`.content-list`)**:
   Standardize the `ul` styles used for bullet points inside cards.
3. **Data Table (`.data-table`)**:
   Extract table, header, row, and cell inline styles into a reusable `.data-table` class.

## 4. Migration Path

1. **Update `assets/style.css`**:
   - Add missing tokens or map them correctly.
   - Add `.chapter-link`, `.content-list`, and `.data-table` classes.

2. **Refactor HTML Files**:
   - `keller-casamento.html` & `maquiavel-pedagogo.html`: Remove inline styles from `<a>` tags inside the chapter navigation and apply `class="chapter-link"`.
   - Remove the `style` attribute from the `.back-link` anchors. The CSS class already handles this, and the inline `color: var(--text-muted)` is currently breaking the CSS hover effect.
   - Replace inline styled `<ul>` and `<li>` with the new `.content-list` class.
   - Replace the inline styled `<table>` with the new `.data-table` class.
