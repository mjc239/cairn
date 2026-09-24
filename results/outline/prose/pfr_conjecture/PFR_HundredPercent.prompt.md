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

## Chapter (Lean module `PFR.HundredPercent`)

### `symmGroup` (definition)
Lean: `(X : Ω → G) (hX : Measurable X) : AddSubgroup G`
Docstring: The symmetry group Sym of $X$: the set of all $h ∈ G$ such that $X + h$ has an identical distribution to $X$.

### `sub_mem_symmGroup` (theorem)
Lean: `(hX : Measurable X) (hdist : d[X # X] = 0) (hx : volume (X ⁻¹' {x}) ≠ 0) (hy : volume (X ⁻¹' {y}) ≠ 0) : x - y ∈ symmGroup X hX`
Docstring: If $d[X ;X]=0$, and $x,y \in G$ are such that $P[X=x], P[X=y]>0$, then $x-y \in \mathrm{Sym}[X]$.
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `ProbabilityTheory.IndepFun.condEntropy_eq_entropy`: `(h : IndepFun X Y μ) (hX : Measurable X) (hY : Measurable Y) : H[X | Y ; μ] = H[X; μ]`
- `ProbabilityTheory.condEntropy`: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) condEntropy._auto_1) : ℝ`
- `ProbabilityTheory.condEntropy_of_injective`: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (f : T → S → U) (hf : ∀ (t : T), Function.Injective (f t)) : H[fun ω => f (Y ω) (X ω) | Y ; μ] = H[X | Y ; μ]`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `ProbabilityTheory.mutualInfo`: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) mutualInfo._auto_1) : ℝ`
- `ProbabilityTheory.mutualInfo_eq_entropy_sub_condEntropy`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : I[X : Y ; μ] = H[X; μ] - H[X | Y ; μ]`
- `ProbabilityTheory.mutualInfo_eq_zero`: `(hX : Measurable X) (hY : Measurable Y) : I[X : Y ; μ] = 0 ↔ IndepFun X Y μ`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.sub`, `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IdentDistrib.symmGroup_eq`, `ProbabilityTheory.IndepFun.rdist_eq`, `ProbabilityTheory.condEntropy_sub_right`, `ProbabilityTheory.entropy_def`

### `isUniform_sub_const_of_rdist_eq_zero` (theorem)
Lean: `(hX : Measurable X) (hdist : d[X # X] = 0) (hx₀ : volume (X ⁻¹' {x₀}) ≠ 0) : IsUniform (↑(symmGroup X hX)) (fun ω => X ω - x₀) volume`
Docstring: If `d[X # X] = 0`, then `X - x₀` is the uniform distribution on the subgroup of `G` stabilizing the distribution of `X`, for any `x₀` of positive probability.
Proof uses:
- `sub_mem_symmGroup`: `(hX : Measurable X) (hdist : d[X # X] = 0) (hx : volume (X ⁻¹' {x}) ≠ 0) (hy : volume (X ⁻¹' {y}) ≠ 0) : x - y ∈ symmGroup X hX`
Helper lemmas folded into the proof: `mem_symmGroup`

### `exists_isUniform_of_rdist_self_eq_zero` (theorem)
Lean: `(hX : Measurable X) (hdist : d[X # X] = 0) : ∃ H U, Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = 0`
Docstring: If $d[X ;X]=0$, then there exists a subgroup $H \leq G$ such that $d[X ;U_H] = 0$.
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `isUniform_sub_const_of_rdist_eq_zero`: `(hX : Measurable X) (hdist : d[X # X] = 0) (hx₀ : volume (X ⁻¹' {x₀}) ≠ 0) : IsUniform (↑(symmGroup X hX)) (fun ω => X ω - x₀) volume`
- `rdist_add_const`: `(hX : Measurable X) (hY : Measurable Y) : d[X; μ # Y + fun x => c; μ'] = d[X; μ # Y; μ']`
- `symmGroup`: `(X : Ω → G) (hX : Measurable X) : AddSubgroup G`
Helper lemmas folded into the proof: `instFiniteRangeOfFinite`

### `exists_isUniform_of_rdist_eq_zero` (theorem)
Lean: `(hX : Measurable X) (hX' : Measurable X') (hdist : d[X # X'] = 0) : ∃ H U, Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = 0 ∧ d[X' # U] = 0`
Docstring: If $d[X_1;X_2]=0$, then there exists a subgroup $H \leq G$ such that $d[X_1;U_H] = d[X_2;U_H] = 0$. Follows from the preceding claim by the triangle inequality.
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `diff_ent_le_rdist`: `(hX : Measurable X) (hY : Measurable Y) : |H[X; μ] - H[Y; μ']| ≤ 2 * d[X; μ # Y; μ']`
- `exists_isUniform_of_rdist_self_eq_zero`: `(hX : Measurable X) (hdist : d[X # X] = 0) : ∃ H U, Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = 0`
- `rdist_triangle`: `(hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) : d[X; μ # Z; μ''] ≤ d[X; μ # Y; μ'] + d[Y; μ' # Z; μ'']`
Helper lemmas folded into the proof: `MeasureTheory.Measure.ennreal_smul_real_apply`, `ProbabilityTheory.entropy_comp_of_injective`, `ProbabilityTheory.entropy_def`, `ProbabilityTheory.entropy_neg`, `ProbabilityTheory.measureEntropy_map_of_injective`, `instFiniteRangeOfFinite`, `rdist_def`, `rdist_nonneg`
