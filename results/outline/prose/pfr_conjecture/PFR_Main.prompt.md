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

## Chapter (Lean module `PFR.Main`)

### `ProbabilityTheory.IsUniform.measureReal_preimage_sub_zero` (theorem)
Lean: `(Uunif : IsUniform (↑A) U volume) (Umeas : Measurable U) (Vunif : IsUniform (↑B) V volume) (Vmeas : Measurable V) (h_indep : IndepFun U V volume) : volume.real ((U - V) ⁻¹' {0}) = ↑(A ∩ B).card / (↑A.card * ↑B.card)`
Docstring: Given two independent random variables `U` and `V` uniformly distributed respectively on `A` and `B`, then `U = V` with probability `#(A ∩ B) / #A ⬝ #B`.
Proof uses:
- `ProbabilityTheory.IsUniform.measureReal_preimage_of_mem`: `(h : IsUniform (↑A) X μ) (hX : Measurable X) (hs : s ∈ A) : μ.real (X ⁻¹' {s}) = 1 / ↑A.card`
Helper lemmas folded into the proof: `ProbabilityTheory.IndepFun.measureReal_inter_preimage_eq_mul`, `ProbabilityTheory.IsUniform.measureReal_preimage_of_nmem`, `ProbabilityTheory.IsUniform.measure_preimage_compl`, `ProbabilityTheory.IsUniform.measure_preimage_of_nmem`

### `ProbabilityTheory.IsUniform.measureReal_preimage_sub` (theorem)
Lean: `(Uunif : IsUniform (↑A) U volume) (Umeas : Measurable U) (Vunif : IsUniform (↑B) V volume) (Vmeas : Measurable V) (h_indep : IndepFun U V volume) (x : G) : volume.real ((U - V) ⁻¹' {x}) = ↑(A ∩ (B + {x})).card / (↑A.card * ↑B.card)`
Docstring: Given two independent random variables `U` and `V` uniformly distributed respectively on `A` and `B`, then `U = V + x` with probability `# (A ∩ (B + x)) / #A ⬝ #B`.
Proof uses:
- `ProbabilityTheory.IsUniform.measureReal_preimage_sub_zero`: `(Uunif : IsUniform (↑A) U volume) (Umeas : Measurable U) (Vunif : IsUniform (↑B) V volume) (Vmeas : Measurable V) (h_indep : IndepFun U V volume) : volume.real ((U - V) ⁻¹' {0}) = ↑(A ∩ B).card / (↑A…`
Helper lemmas folded into the proof: `ProbabilityTheory.IsUniform.comp`, `ProbabilityTheory.IsUniform.eq_of_mem`, `ProbabilityTheory.IsUniform.measure_preimage_compl`

### `rdist_le_of_isUniform_of_card_sub_le` (theorem)
Lean: `(hA₀ : A.Nonempty) (hA : ↑(A - A).ncard ≤ K * ↑A.ncard) (U₀unif : IsUniform A U₀ volume) (U₀meas : Measurable U₀) : d[U₀ # U₀] ≤ Real.log K`
Docstring: A uniform distribution on a set whose difference set has relative size at most `K` has self Rusza distance at most `log K`.
Proof uses:
- `ProbabilityTheory.IsUniform.entropy_eq`: `(hX : IsUniform (↑H) X μ) (hX' : Measurable X) : H[X; μ] = Real.log ↑(Nat.card ↥H)`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
Helper lemmas folded into the proof: `PFR_conjecture_pos_aux`, `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IndepFun.rdist_eq`, `ProbabilityTheory.IsUniform.ae_mem`, `ProbabilityTheory.IsUniform.entropy_eq'`, `ProbabilityTheory.IsUniform.eq_of_mem`, `ProbabilityTheory.IsUniform.measure_preimage_compl`

### `PFR_conjecture_aux` (theorem)
Lean: `(hA₀ : A.Nonempty) (hA : ↑(A + A).ncard ≤ K * ↑A.ncard) : ∃ H c, ↑(Nat.card ↑c) ≤ K ^ (13 / 2) * ↑A.ncard ^ (1 / 2) * ↑(↑H).ncard ^ (-1 / 2) ∧ ↑(↑H).ncard ≤ K ^ 11 * ↑A.ncard ∧ ↑A.ncard ≤ K ^ 11 * ↑(↑H).ncard ∧ A ⊆ c + ↑H`
Docstring: Auxiliary statement towards the polynomial Freiman-Ruzsa (PFR) conjecture: if `A` is a subset of an elementary abelian 2-group of doubling constant at most $K$, then there exists a subgroup `H` such that `A` can be covered by at most `K^(13/2) |A|^(1/2) / |H|^(1/2)` cosets of `H`, and `H` has the same cardinality as `A` up to a multiplicative factor `K^11`.
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `ProbabilityTheory.IsUniform`: `(H : Set S) (X : Ω → S) (μ : autoParam (Measure Ω) IsUniform._auto_1) : Prop`
- `ProbabilityTheory.IsUniform.entropy_eq`: `(hX : IsUniform (↑H) X μ) (hX' : Measurable X) : H[X; μ] = Real.log ↑(Nat.card ↥H)`
- `ProbabilityTheory.IsUniform.measureReal_preimage_sub`: `(Uunif : IsUniform (↑A) U volume) (Umeas : Measurable U) (Vunif : IsUniform (↑B) V volume) (Vmeas : Measurable V) (h_indep : IndepFun U V volume) (x : G) : volume.real ((U - V) ⁻¹' {x}) = ↑(A ∩ (B + …`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.exists_isUniform_measureSpace`: `(H : Finset S) (h : H.Nonempty) : ∃ Ω mΩ U, IsProbabilityMeasure volume ∧ Measurable U ∧ IsUniform (↑H) U volume ∧ (∀ (ω : Ω), U ω ∈ H) ∧ FiniteRange U`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `ProbabilityTheory.prob_ge_exp_neg_entropy`: `(X : Ω → S) (μ : Measure Ω) (hX : Measurable X) : ∃ s, μ Set.univ * ↑(Real.exp (-H[X; μ])).toNNReal ≤ (Measure.map X μ) {s}`
- `diff_ent_le_rdist`: `(hX : Measurable X) (hY : Measurable Y) : |H[X; μ] - H[Y; μ']| ≤ 2 * d[X; μ # Y; μ']`
- `entropic_PFR_conjecture`: `(p : refPackage Ω₀₁ Ω₀₂ G) (hpη : p.η = 1 / 9) : ∃ H Ω mΩ U, IsProbabilityMeasure volume ∧ Measurable U ∧ IsUniform (↑H) U volume ∧ d[p.X₀₁ # U] + d[p.X₀₂ # U] ≤ 11 * d[p.X₀₁ # p.X₀₂]`
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.sub`, `PFR_conjecture_pos_aux`, `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IndepFun.rdist_eq`, `ProbabilityTheory.IsUniform.entropy_eq'`, `ProbabilityTheory.IsUniform.eq_of_mem`

### `PFR_conjecture` (theorem)
Lean: `(hA₀ : A.Nonempty) (hA : ↑(A + A).ncard ≤ K * ↑A.ncard) : ∃ H c, ↑(Nat.card ↑c) < 2 * K ^ 12 ∧ (↑H).ncard ≤ A.ncard ∧ A ⊆ c + ↑H`
Docstring: The polynomial Freiman-Ruzsa (PFR) conjecture: if `A` is a subset of an elementary abelian 2-group of doubling constant at most `K`, then `A` can be covered by at most `2 * K ^ 12` cosets of a subgroup of cardinality at most `|A|`.
Proof uses:
- `PFR_conjecture_aux`: `(hA₀ : A.Nonempty) (hA : ↑(A + A).ncard ≤ K * ↑A.ncard) : ∃ H c, ↑(Nat.card ↑c) ≤ K ^ (13 / 2) * ↑A.ncard ^ (1 / 2) * ↑(↑H).ncard ^ (-1 / 2) ∧ ↑(↑H).ncard ≤ K ^ 11 * ↑A.ncard ∧ ↑A.ncard ≤ K ^ 11 * ↑(…`
Helper lemmas folded into the proof: `PFR_conjecture_pos_aux'`
