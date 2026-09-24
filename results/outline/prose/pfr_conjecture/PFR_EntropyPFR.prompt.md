You are writing the text of a mathematical outline generated from a verified Lean formalisation.
Below are the results of one chapter, in the order the outline presents them. For each you get its Lean name, its
statement in Lean (only explicit hypotheses are shown; implicit and type-class assumptions are omitted), its
docstring if there is one, and, for theorems, the named results its proof uses (with their statements) and the
helper lemmas folded into the proof.

Write:
1. `title`: a short chapter title (at most 8 words), as a mathematician would name this material.
2. For every result, `statement`: the statement in clear mathematical English, using LaTeX between $...$ for
   formulas. Be faithful: keep every hypothesis and the exact conclusion; do not add, drop, strengthen or weaken
   anything. If some notation's meaning is unclear, keep the notation rather than guessing. For a definition, say
   what is being defined.
3. For every theorem, `sketch`: one or two sentences on how the proof goes, based only on the listed results it
   uses and their statements. Do not invent steps; if the structure is not clear, just say which results it
   combines.

Reply with only a JSON object:
{"title": "...", "results": {"<lean name>": {"statement": "...", "sketch": "..."}}}
(omit "sketch" for definitions). Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

## Chapter (Lean module `PFR.EntropyPFR`)

### `tau_strictly_decreases` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (h_min : TauMinimizes p X₁ X₂) (hpη : p.η = 1 / 9) : d[X₁ # X₂] = 0`
Docstring: If $d[X_1;X_2] > 0$ then there are $G$-valued random variables $X'_1, X'_2$ such that $\tau[X'_1;X'_2] < \tau[X_1;X_2]$. Phrased in the contrapositive form for convenience of proof.
Proof uses:
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.independent_copies4_nondep`: `(hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₃ : Measurable X₃) (hX₄ : Measurable X₄) (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) (μ₃ : Measure Ω₃) (μ₄ : Measure Ω₄) : ∃ A x μA X₁' X₂' X₃' X₄', IsProbabili…`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `refPackage.X₀₁`: `(self : refPackage Ω₀₁ Ω₀₂ G) (_ : Ω₀₁) : G`
- `refPackage.X₀₂`: `(self : refPackage Ω₀₁ Ω₀₂ G) (_ : Ω₀₂) : G`
- `tau`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω₁ → G) (X₂ : Ω₂ → G) (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) : ℝ`
- `tau_strictly_decreases_aux`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' …`
Helper lemmas folded into the proof: `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr_right`, `ProbabilityTheory.IdentDistrib.tauMinimizes`, `ProbabilityTheory.IdentDistrib.tau_eq`, `refPackage.hmeas1`, `refPackage.hmeas2`

### `entropic_PFR_conjecture` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (hpη : p.η = 1 / 9) : ∃ H Ω mΩ U, IsProbabilityMeasure volume ∧ Measurable U ∧ IsUniform (↑H) U volume ∧ d[p.X₀₁ # U] + d[p.X₀₂ # U] ≤ 11 * d[p.X₀₁ # p.X₀₂]`
Docstring: `entropic_PFR_conjecture`: For two $G$-valued random variables $X^0_1, X^0_2$, there is some subgroup $H \leq G$ such that $d[X^0_1;U_H] + d[X^0_2;U_H] \le 11 d[X^0_1;X^0_2]$.
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `TauMinimizes`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) : Prop`
- `exists_isUniform_of_rdist_eq_zero`: `(hX : Measurable X) (hX' : Measurable X') (hdist : d[X # X'] = 0) : ∃ H U, Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = 0 ∧ d[X' # U] = 0`
- `rdist_triangle`: `(hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) : d[X; μ # Z; μ''] ≤ d[X; μ # Y; μ'] + d[Y; μ' # Z; μ'']`
- `tau`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω₁ → G) (X₂ : Ω₂ → G) (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) : ℝ`
- `tau_minimizer_exists`: `(p : refPackage Ω₀₁ Ω₀₂ G) : ∃ Ω x X₁ X₂, Measurable X₁ ∧ Measurable X₂ ∧ IsProbabilityMeasure volume ∧ TauMinimizes p X₁ X₂`
- `tau_strictly_decreases`: `(p : refPackage Ω₀₁ Ω₀₂ G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (h_min : TauMinimizes p X₁ X₂) (hpη : p.η = 1 / 9) : d[X₁ # X₂] = 0`
Helper lemmas folded into the proof: `MeasureTheory.Measure.ennreal_smul_real_apply`, `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr_right`, `ProbabilityTheory.IdentDistrib.tau_eq`, `ProbabilityTheory.entropy_comp_of_injective`, `ProbabilityTheory.entropy_def`, `ProbabilityTheory.entropy_neg`
