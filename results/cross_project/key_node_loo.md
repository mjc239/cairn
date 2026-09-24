# Key-declaration model: leave one project out

Each training project is scored by a model trained on the other training projects; held-out projects by a model trained on all of them. *Baseline*: trained on PFR and Carleson only (minus the project itself). P@k: precision among the top k, k = the number of blueprint-named declarations.

| Project | Role | Decls | Named | Base rate | AUROC | P@k | Baseline AUROC | Baseline P@k |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| PFR | train | 1395 | 248 | 17.8% | 0.82 | 57% | 0.79 | 50% |
| Carleson | train | 3422 | 236 | 6.9% | 0.86 | 34% | 0.85 | 30% |
| brownian_motion | train | 2222 | 325 | 14.6% | 0.70 | 30% | 0.68 | 28% |
| testing_lower_bounds | train | 1035 | 126 | 12.2% | 0.67 | 26% | 0.63 | 24% |
| sphere_packing | train | 1468 | 100 | 6.8% | 0.79 | 33% | 0.74 | 30% |
| flt3 | train | 235 | 90 | 38.3% | 0.73 | 57% | 0.68 | 54% |
| sphere_eversion | train | 1378 | 80 | 5.8% | 0.86 | 32% | 0.82 | 30% |
| abc_exceptions | train | 248 | 49 | 19.8% | 0.81 | 49% | 0.77 | 43% |
| apap | train | 769 | 34 | 4.4% | 0.93 | 65% | 0.89 | 68% |
| formal_book | held out | 507 | 68 | 13.4% | 0.56 | 16% | 0.60 | 18% |
| semicircle | held out | 229 | 59 | 25.8% | 0.68 | 44% | 0.72 | 51% |
| con_nf | held out | 1998 | 57 | 2.9% | 0.81 | 9% | 0.71 | 2% |
| toric | held out | 276 | 29 | 10.5% | 0.71 | 28% | 0.55 | 14% |
| chandra_furst_lipton | held out | 29 | 15 | 51.7% | 0.91 | 80% | 0.68 | 60% |
| flt_regular | held out | 295 | 12 | 4.1% | 0.73 | 17% | 0.65 | 8% |
| iwasawa | held out | 950 | 10 | 1.1% | 0.83 | 10% | 0.55 | 0% |
| bonn_analysis | held out | 393 | 8 | 2.0% | 0.81 | 12% | 0.78 | 25% |
| clt | held out | 26 | 7 | 26.9% | 0.67 | 29% | 0.75 | 43% |
