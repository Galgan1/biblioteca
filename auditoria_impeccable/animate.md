# Impeccable Motion & Transitions Audit

## Overview
This report evaluates the digital library project against the Impeccable `animate.md` heuristic, focusing on performance, easing, accessibility, and purpose-driven motion.

## 🏆 What's Working Well (The Good)

*   **Smart Staggering:** The `.animate-entrance` class excellently implements sibling stagger with a built-in cap: `animation-delay: calc(min(var(--i, 0) * 80ms, 600ms))`. This prevents the "long list takes forever to load" anti-pattern.
*   **Layout Safety (FLIP-style alternative):** The expandable details section in the cheat sheets (`.card-details`) elegantly uses `grid-template-rows: 0fr` to `1fr` to expand content. This avoids animating `height` directly, which is a major performance win.
*   **Custom Easing:** Proper usage of the custom bezier curves (`--ease-out-quart` and `--ease-out-quint`) for most UI transitions, completely avoiding the tacky `bounce` or `elastic` defaults.
*   **Duration Rules:** Timing feels natural and respects the 100/300/500 rule (e.g., 200ms for hover states, 600ms-800ms for page and entrance choreographies).
*   **Accessibility:** The `@media (prefers-reduced-motion: reduce)` block is robustly implemented to zero out durations.

## 🛠️ Recommendations for Polish (The Fixes)

**1. Eradicate Default Easings**
The heuristic strictly forbids CSS default easing curves (like `ease`).
*   **Location:** `assets/style.css` line 482 (`.card-cover img`).
*   **Current:** `transition: transform 0.3s ease;`
*   **Fix:** Use the custom variables: `transition: transform 300ms var(--ease-out-quart);`.
*   **Location:** `assets/style.css` line 236 (`.card-details-inner`).
*   **Current:** `transition: margin-top 300ms, padding-top 300ms, border-color 300ms;` (implicit `ease`).

**2. Stop Animating Layout-Driving Properties**
*   **Location:** `.card-details-inner` in `assets/style.css`.
*   **Issue:** The element transitions `margin-top` and `padding-top`. The heuristic explicitly warns against animating layout-driving properties (margins, top/left, etc.) because it causes layout thrashing and jank.
*   **Fix:** Remove the transition on the margins/padding. Allow the `grid-template-rows` transition on the parent (`.card-details`) to be the sole driver of the layout expansion. You can set the inner paddings to be static, or handle spacing via a `gap` on the parent.

**3. Add Tactile Click Feedback**
*   **Location:** `.card` / `a.card` components.
*   **Issue:** The cards have a great hover state (translateY and shadow), but no `:active` click state.
*   **Fix:** The heuristic recommends: "Click: Quick scale down then up (0.95 → 1)". Add an `:active` selector (e.g., `a.card:active { transform: translateY(-2px) scale(0.98); }`) to provide that physical, snappy confirmation when a user clicks a card before navigation occurs.
