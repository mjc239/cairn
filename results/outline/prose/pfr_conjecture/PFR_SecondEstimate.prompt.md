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

## Chapter (Lean module `PFR.SecondEstimate`)

### `second_estimate_aux` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₁', X₂'] volume) (h_min : TauMinimizes p X₁ X₂) : d[X₁ # X₁] + d[X₂ # X₂] ≤ 2 * (d[X₁ # X₂] + (2 * p.η * d[X₁ # X₂] - I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂']) / (1 - p.η))`
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `comparison_of_ruzsa_distances`: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun Y Z μ') : d[X; μ # Y + Z; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z; μ'] - H[Y; μ']) / 2 ∧ ∀ (a : Module (ZMod 2) G), …`
- `condRuzsaDist_diff_le`: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun Y Z μ') : d[X; μ # Y + Z; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z; μ'] - H[Y; μ']) / 2`
- `distance_ge_of_min`: `(p : refPackage Ω₀₁ Ω₀₂ G) (h : TauMinimizes p X₁ X₂) (h1 : Measurable X₁') (h2 : Measurable X₂') : d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁'] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂'] - d[p.X₀₂ # X₂]) ≤ d[X₁…`
- `ent_ofsum_le`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' …`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
- `refPackage.X₀₁`: `(self : refPackage Ω₀₁ Ω₀₂ G) (_ : Ω₀₁) : G`
- `refPackage.X₀₂`: `(self : refPackage Ω₀₁ Ω₀₂ G) (_ : Ω₀₂) : G`
Helper lemmas folded into the proof: `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IndepFun.rdist_eq`, `ProbabilityTheory.entropy_def`, `ProbabilityTheory.iIndepFun.reindex_four_abdc`, `condRuzsaDist_diff_le'`, `entropy_sub_entropy_eq_condRuzsaDist_add`, `instFiniteRangeOfFinite`

### `second_estimate` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₁', X₂'] volume) (h_min : TauMinimizes p X₁ X₂) : I[X₁ + X₂ : X₁' + X₁|X₁ + X₂ + X₁' + X₂'] ≤ 2 * p.η * d[X₁ # X₂] + 2 * p.η * (2 * p.η * d[X₁ # X₂] - I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂']) / (1 - p.η)`
Docstring: $$ I_2 \leq 2 \eta k + \frac{2 \eta (2 \eta k - I_1)}{1 - \eta}.$$
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.Kernel.rdist`: `(κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') : ℝ`
- `ProbabilityTheory.Kernel.rdist_symm`: `dk[κ ; μ # η ; ν] = dk[η ; ν # κ ; μ]`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.entropy_add_right`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨X, X + Y⟩; μ] = H[⟨X, Y⟩; μ]`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `ProbabilityTheory.mutualInfo`: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) mutualInfo._auto_1) : ℝ`
Helper lemmas folded into the proof: `FiniteRange.add`, `FiniteRange.finite`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `MeasureTheory.Measure.ennreal_smul_real_apply`, `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr`
