# Style sweep: testing_lower_bounds

*RemyDegenne/testing-lower-bounds @ da2cf0bfba77 (2026-09-24)*

Chapter averages over chapters with at least 8 results; 5 arrangements per style. τ = Kendall correlation with the human event order; motivated = lemmas stated after a goal they serve; mean open = working-memory load (lower is better).

**Human:** motivated 36%, mean open 5.71.

**Best τ:** top_down=0, definitions=upfront (τ +0.31).

**Closest (motivated, load) profile:** top_down=0 (motivated 32%, mean open 5.84, τ +0.31).

| Style | τ | motivated | mean open |
|---|---:|---:|---:|
| top_down=0, definitions=upfront | +0.31 | 32% | 6.09 |
| top_down=0 | +0.31 | 32% | 5.84 |
| top_down=0.2, goals by key | +0.29 | 44% | 5.98 |
| top_down=0.2, definitions=upfront, goals by key | +0.27 | 44% | 6.24 |
| top_down=0.4 | +0.27 | 59% | 6.07 |
| top_down=0.2, definitions=upfront, goals by support | +0.27 | 47% | 6.29 |
| top_down=0.2, definitions=upfront | +0.27 | 48% | 6.26 |
| top_down=0.4, goals by support | +0.27 | 60% | 6.05 |
| top_down=0.4, definitions=upfront, goals by key | +0.26 | 56% | 6.35 |
| top_down=0.4, definitions=upfront | +0.26 | 58% | 6.33 |
| top_down=0.4, definitions=upfront, goals by support | +0.26 | 59% | 6.34 |
| top_down=0.6, definitions=upfront, goals by key | +0.25 | 70% | 6.42 |
| top_down=0.6, goals by support | +0.25 | 70% | 6.17 |
| top_down=0.6 | +0.25 | 72% | 6.17 |
| top_down=0.6, definitions=upfront, goals by support | +0.25 | 69% | 6.43 |
| top_down=0.6, definitions=upfront | +0.25 | 70% | 6.43 |
| top_down=0.8, definitions=upfront, goals by key | +0.24 | 78% | 6.50 |
| top_down=0.8, definitions=upfront | +0.24 | 77% | 6.47 |
| top_down=0.8, goals by key | +0.24 | 80% | 6.24 |
| top_down=0.8, definitions=upfront, goals by support | +0.24 | 77% | 6.47 |
| top_down=0.8 | +0.24 | 78% | 6.23 |
| top_down=0.8, goals by support | +0.24 | 78% | 6.23 |
| top_down=1, definitions=upfront | +0.23 | 85% | 6.54 |
| top_down=1, definitions=upfront, goals by support | +0.23 | 85% | 6.54 |
| top_down=1, definitions=upfront, goals by key | +0.23 | 85% | 6.54 |
| top_down=0.2, goals by support | +0.23 | 50% | 5.90 |
| top_down=1 | +0.23 | 87% | 6.30 |
| top_down=1, goals by support | +0.23 | 87% | 6.30 |
| top_down=1, goals by key | +0.23 | 87% | 6.30 |
| top_down=0.2 | +0.23 | 51% | 5.90 |
| top_down=0.4, goals by key | +0.22 | 60% | 5.98 |
| top_down=0, chapter roadmap, definitions=upfront | +0.21 | 67% | 10.96 |
| top_down=0.2, chapter roadmap, definitions=upfront, goals by support | +0.20 | 70% | 11.01 |
| top_down=0.2, chapter roadmap, definitions=upfront | +0.20 | 71% | 10.98 |
| top_down=0.2, chapter roadmap, definitions=upfront, goals by key | +0.19 | 72% | 10.99 |
| top_down=0.6, goals by key | +0.19 | 72% | 6.09 |
| top_down=0.4, chapter roadmap, definitions=upfront | +0.19 | 73% | 11.02 |
| top_down=0.4, chapter roadmap, definitions=upfront, goals by key | +0.19 | 77% | 11.03 |
| top_down=0.4, chapter roadmap, definitions=upfront, goals by support | +0.19 | 75% | 11.02 |
| top_down=0.2, chapter roadmap, goals by support | +0.19 | 71% | 11.21 |
| top_down=0.2, chapter roadmap | +0.19 | 72% | 11.19 |
| top_down=0.6, chapter roadmap, definitions=upfront | +0.19 | 80% | 11.04 |
| top_down=0.6, chapter roadmap, definitions=upfront, goals by support | +0.19 | 80% | 11.04 |
| top_down=0.8, chapter roadmap, definitions=upfront | +0.19 | 80% | 11.04 |
| top_down=0.8, chapter roadmap, definitions=upfront, goals by support | +0.19 | 81% | 11.05 |
| top_down=0.6, chapter roadmap, definitions=upfront, goals by key | +0.18 | 81% | 11.06 |
| top_down=0.4, chapter roadmap | +0.18 | 74% | 11.22 |
| top_down=0.8, chapter roadmap, definitions=upfront, goals by key | +0.18 | 81% | 11.08 |
| top_down=0.2, chapter roadmap, goals by key | +0.18 | 72% | 11.20 |
| top_down=0.4, chapter roadmap, goals by key | +0.18 | 78% | 11.25 |
| top_down=1, chapter roadmap, definitions=upfront | +0.18 | 85% | 11.09 |
| top_down=1, chapter roadmap, definitions=upfront, goals by support | +0.18 | 85% | 11.09 |
| top_down=1, chapter roadmap, definitions=upfront, goals by key | +0.18 | 85% | 11.09 |
| top_down=0.4, chapter roadmap, goals by support | +0.18 | 75% | 11.23 |
| top_down=0, chapter roadmap | +0.18 | 68% | 11.19 |
| top_down=0.6, chapter roadmap | +0.17 | 81% | 11.25 |
| top_down=0.6, chapter roadmap, goals by support | +0.17 | 81% | 11.25 |
| top_down=0.8, chapter roadmap | +0.17 | 81% | 11.26 |
| top_down=0.6, chapter roadmap, goals by key | +0.17 | 81% | 11.27 |
| top_down=0.8, chapter roadmap, goals by support | +0.17 | 81% | 11.26 |
| top_down=0.8, chapter roadmap, goals by key | +0.17 | 82% | 11.29 |
| top_down=1, chapter roadmap | +0.17 | 86% | 11.31 |
| top_down=1, chapter roadmap, goals by support | +0.17 | 86% | 11.31 |
| top_down=1, chapter roadmap, goals by key | +0.17 | 86% | 11.31 |

## Whole document

Chapters kept intact, in the human order of each result's home chapter (where it is proved). Every promise counts, including goals announced in one chapter and proved in another.

**Human:** motivated 28%, mean open 30.7. **Closest profile:** top_down=0 (motivated 25%, mean open 31.3).

| Style | τ | motivated | mean open |
|---|---:|---:|---:|
| top_down=0 | +0.86 | 25% | 31.3 |
| top_down=0, chapter roadmap | +0.84 | 61% | 37.4 |
| top_down=0, document roadmap | +0.42 | 54% | 66.5 |
| top_down=0.2 | +0.86 | 43% | 31.1 |
| top_down=0.2, chapter roadmap | +0.84 | 66% | 37.4 |
| top_down=0.2, document roadmap | +0.42 | 57% | 66.6 |
| top_down=0.4 | +0.86 | 53% | 31.1 |
| top_down=0.4, chapter roadmap | +0.84 | 68% | 37.4 |
| top_down=0.4, document roadmap | +0.42 | 61% | 66.5 |
| top_down=0.6 | +0.85 | 65% | 31.1 |
| top_down=0.6, chapter roadmap | +0.84 | 72% | 37.4 |
| top_down=0.6, document roadmap | +0.42 | 63% | 66.5 |
| top_down=0.8 | +0.85 | 71% | 31.2 |
| top_down=0.8, chapter roadmap | +0.84 | 73% | 37.5 |
| top_down=0.8, document roadmap | +0.42 | 64% | 66.6 |
| top_down=1 | +0.85 | 78% | 31.3 |
| top_down=1, chapter roadmap | +0.84 | 76% | 37.6 |
| top_down=1, document roadmap | +0.42 | 65% | 66.6 |
