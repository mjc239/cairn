# Blueprint-free outlines of the 9 training projects

Each project is outlined with a key-declaration model trained on the *other* 8 projects, at the blueprint's own level of detail (the share of declarations it names), in the style fitted to its blueprint. *Baseline*: model trained on PFR and Carleson only (minus the project). Precision is over named theorems, recall over the declarations the blueprint names.

| Project | Detail | Style | Named (theorems) | Theorem precision | Recall | Nodes covered | Chapter NMI | τ within chapters | Baseline precision | Baseline recall |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [PFR](pfr.md) | 0.178 | top_down=0 | 282 (213) | 60% | 60% | 66% | 0.85 | +0.68 | 50% | 59% |
| [Carleson](carleson.md) | 0.069 | top_down=0.2, chapter roadmap | 537 (192) | 40% | 35% | 47% | 0.72 | +0.26 | 46% | 31% |
| [brownian_motion](brownian_motion.md) | 0.146 | top_down=0 | 426 (263) | 29% | 39% | 39% | 0.78 | +0.58 | 25% | 39% |
| [testing_lower_bounds](testing_lower_bounds.md) | 0.122 | top_down=0 | 157 (116) | 26% | 33% | 33% | 0.63 | +0.54 | 24% | 33% |
| [sphere_packing](sphere_packing.md) | 0.068 | top_down=0 | 204 (81) | 28% | 54% | 53% | 0.82 | +0.89 | 28% | 55% |
| [flt3](flt3.md) | 0.383 | top_down=0 | 101 (60) | 78% | 58% | 58% | 1.00 | +0.28 | 61% | 57% |
| [sphere_eversion](sphere_eversion.md) | 0.058 | top_down=0.2 | 188 (42) | 48% | 62% | 65% | 0.62 | +0.51 | 34% | 61% |
| [abc_exceptions](abc_exceptions.md) | 0.198 | top_down=0.2, chapter roadmap | 78 (43) | 49% | 71% | 91% | 0.92 | +0.67 | 44% | 71% |
| [apap](apap.md) | 0.044 | top_down=0 | 46 (27) | 78% | 74% | 76% | 0.83 | +0.64 | 67% | 76% |
