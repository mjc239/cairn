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

## Chapter (Lean module `PFR.Endgame`)

### `construct_good` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (h_min : TauMinimizes p X₁ X₂) (hT : T₁ + T₂ + T₃ = 0) (hT₁ : Measurable T₁) (hT₂ : Measurable T₂) (hT₃ : Measurable T₃) : d[X₁ # X₂] ≤ I[T₁ : T₂] + I[T₂ : T₃] + I[T₃ : T₁] + p.η / 3 * (I[T₁ : T₂] + I[T₂ : T₃] + I[T₃ : T₁] + (d[p.X₀₁ # T₁] - d[p.X₀₁ # X₁] + (d[p.X₀₂ # T₁] - d[p.X₀₂ # X₂])) + (d[p.X₀₁ # T₂] - d[p.X₀₁ # X₁] + (d[p.X₀₂ # T₂] - d[p.X₀₂ # X₂])) + (d[p.X₀₁ # T₃] - d[p.X₀₁ # X₁] + (d[p.X₀₂ # T₃] - d[p.X₀₂ # X₂])))`
Docstring: If $T_1, T_2, T_3$ are $G$-valued random variables with $T_1+T_2+T_3=0$ holds identically and - $$ \delta := \sum_{1 \leq i < j \leq 3} I[T_i;T_j]$$ Then there exist random variables $T'_1, T'_2$ such that $$ d[T'_1;T'_2] + \eta (d[X_1^0;T'_1] - d[X_1^0;X _1]) + \eta(d[X_2^0;T'_2] - d[X_2^0;X_2])$$ is at most $$\delta + \frac{\eta}{3} \biggl( \delta + \sum_{i=1}^2 \sum_{j = 1}^3 (d[X^0_i;T_j] - d…
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.entropy_add_left`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨Y + X, Y⟩; μ] = H[⟨X, Y⟩; μ]`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `ProbabilityTheory.mutualInfo_eq_zero`: `(hX : Measurable X) (hY : Measurable Y) : I[X : Y ; μ] = 0 ↔ IndepFun X Y μ`
- `condRuzsaDist`: `(X : Ω → G) (Z : Ω → S) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist._auto_3) : ℝ`
- `condRuzsaDist'`: `(X : Ω → G) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist'._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist'._auto_3) : ℝ`
- `condRuzsaDist'_eq_sum`: `(hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (μ' : Measure Ω') : d[X ; μ # Y | W ; μ'] = ∑ w ∈ FiniteRange.toFinset W, μ'.real (W ⁻¹' {w}) * d[X; μ # Y; μ'[|W ⁻¹' {w}]]`
Helper lemmas folded into the proof: `FiniteRange.ae_mem_toFinset`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `MeasureTheory.Measure.ennreal_smul_real_apply`, `ProbabilityTheory.IndepFun.mutualInfo_eq_zero`, `ProbabilityTheory.entropy_add_right'`, `ProbabilityTheory.entropy_comm`

### `cond_construct_good` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (h_min : TauMinimizes p X₁ X₂) (hT : T₁ + T₂ + T₃ = 0) (hT₁ : Measurable T₁) (hT₂ : Measurable T₂) (hT₃ : Measurable T₃) (hR : Measurable R) : d[X₁ # X₂] ≤ I[T₁ : T₂|R] + I[T₂ : T₃|R] + I[T₃ : T₁|R] + p.η / 3 * (I[T₁ : T₂|R] + I[T₂ : T₃|R] + I[T₃ : T₁|R] + (d[p.X₀₁ # T₁ | R] - d[p.X₀₁ # X₁] + (d[p.X₀₂ # T₁ | R] - d[p.X₀₂ # X₂])) + (d[p.X₀₁ # T₂ | R] - d[p.X₀₁ # X₁] + (d[p.X₀₂ # T₂ | R] - d[p.X₀₂ # X₂])) + (d[p.X₀₁ # T₃ | R] - d[p.X₀₁ # X₁] + (d[p.X₀₂ # T₃ | R] - d[p.X₀₂ # X₂])))`
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `ProbabilityTheory.mutualInfo`: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) mutualInfo._auto_1) : ℝ`
- `condRuzsaDist'_eq_integral`: `(X : Ω → G) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (μ' : Measure Ω') : d[X ; μ # Y | W ; μ'] = ∫ (x : T), (fun w => d[X; μ # Y; μ'[|W ⁻¹' {w}]]) x ∂Measure.map W μ'`
- `construct_good`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (h_min : TauMinimizes p X₁ X₂) (hT : T₁ + T₂ + T₃ = 0) (hT₁ : Measurable T₁) (hT₂ : Measurable T₂) (hT₃ : Measurable T₃) : d[X₁ # X₂] ≤ I[T₁ : T₂]…`
Helper lemmas folded into the proof: `cond_c_eq_integral`, `construct_good'`, `delta'_eq_integral`, `instFiniteRangeOfFinite`

### `I₃_eq` (theorem)
Lean: `(X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₁', X₂'] volume) : I[X₁' + X₂ : X₁' + X₁|X₁ + X₂ + X₁' + X₂'] = I[X₁ + X₂ : X₁' + X₁|X₁ + X₂ + X₁' + X₂']`
Docstring: The quantity `I_3 = I[V:W|S]` is equal to `I_2`.
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.Kernel.AEFiniteKernelSupport`: `(κ : Kernel T S) (μ : Measure T) : Prop`
- `ProbabilityTheory.Kernel.FiniteKernelSupport`: `(κ : Kernel T S) : Prop`
- `ProbabilityTheory.Kernel.chain_rule`: `(hκ : κ.AEFiniteKernelSupport μ) : Hk[κ , μ] = Hk[κ.fst , μ] + Hk[κ.condKernel , μ.compProd κ.fst]`
- `ProbabilityTheory.Kernel.entropy`: `(κ : Kernel T S) (μ : Measure T) : ℝ`
- `ProbabilityTheory.Kernel.entropy_prodMkLeft_unit`: `(κ : Kernel T S) : Hk[Kernel.prodMkLeft Unit κ , Measure.map (Prod.mk ()) μ] = Hk[κ , μ]`
- `ProbabilityTheory.condEntropy`: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) condEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `FiniteRange.add`, `FiniteRange.finite`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `MeasureTheory.Measure.ennreal_smul_real_apply`, `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`

### `sum_condMutual_le` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₁', X₂'] volume) (h_min : TauMinimizes p X₁ X₂) : I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂'] + I[X₁' + X₂ : X₁' + X₁|X₁ + X₂ + X₁' + X₂'] + I[X₁' + X₁ : X₁ + X₂|X₁ + X₂ + X₁' + X₂'] ≤ 6 * p.η * d[X₁ # X₂] - (1 - 5 * p.η) / (1 - p.η) * (2 * p.η * d[X₁ # X₂] - I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂'])`
Docstring: `I[U : V | S] + I[V : W | S] + I[W : U | S]` is less than or equal to `6 * η * k - (1 - 5 * η) / (1 - η) * (2 * η * k - I₁)`.
Proof uses:
- `I₃_eq`: `(X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h_indep : i…`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
- `second_estimate`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' …`
Helper lemmas folded into the proof: `MeasureTheory.Measure.ennreal_smul_real_apply`, `ProbabilityTheory.condMutualInfo_comm`, `ProbabilityTheory.entropy_comm`, `ProbabilityTheory.entropy_comp_of_injective`, `ProbabilityTheory.entropy_def`, `ProbabilityTheory.measureEntropy_map_of_injective`, `refPackage.hη'`

### `sum_dist_diff_le` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₁', X₂'] volume) (h_min : TauMinimizes p X₁ X₂) : d[p.X₀₁ # X₁ + X₂ | X₁ + X₂ + X₁' + X₂'] - d[p.X₀₁ # X₁] + (d[p.X₀₂ # X₁ + X₂ | X₁ + X₂ + X₁' + X₂'] - d[p.X₀₂ # X₂]) + (d[p.X₀₁ # X₁' + X₂ | X₁ + X₂ + X₁' + X₂'] - d[p.X₀₁ # X₁] + (d[p.X₀₂ # X₁' + X₂ | X₁ + X₂ + X₁' + X₂'] - d[p.X₀₂ # X₂])) + (d[p.X₀₁ # X₁' + X…`
Docstring: $$ \sum_{i=1}^2 \sum_{A\in\{U,V,W\}} \big(d[X^0_i;A|S] - d[X^0_i;X_i]\big)$$ is less than or equal to $$ \leq (6 - 3\eta) k + 3(2 \eta k - I_1).$$
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `ProbabilityTheory.iIndepFun.apply_two_last`: `(h_indep : iIndepFun ![Z₁, Z₂, Z₃, Z₄] volume) (hZ₁ : Measurable Z₁) (hZ₂ : Measurable Z₂) (hZ₃ : Measurable Z₃) (hZ₄ : Measurable Z₄) (hphi : Measurable (Function.uncurry phi)) : iIndepFun ![Z₁, Z₂,…`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `condRuzsaDist'_of_inj_map'`: `(hA : Measurable A) (hB : Measurable B) (hC : Measurable C) : d[A ; μ'' # B | B + C ; μ] = d[A ; μ'' # C | B + C ; μ]`
- `condRuzsaDist_diff_ofsum_le`: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (hZ' : Measurable Z') (h : iIndepFun ![Y, Z, Z'] μ') : d[X ; μ # Y + Z | Y + Z + Z' ; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z + Z'…`
- `ent_ofsum_le`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' …`
Helper lemmas folded into the proof: `FiniteRange.add`, `FiniteRange.finite`, `ProbabilityTheory.IdentDistrib.add`, `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.prodMk`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr_right`, `ProbabilityTheory.iIndepFun.reindex_four_acbd`

### `tau_strictly_decreases_aux` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₁', X₂'] volume) (h_min : TauMinimizes p X₁ X₂) (hpη : p.η = 1 / 9) : d[X₁ # X₂] = 0`
Docstring: If `d[X₁ ; X₂] > 0` then there are `G`-valued random variables `X₁', X₂'` such that Phrased in the contrapositive form for convenience of proof.
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `ProbabilityTheory.condMutualInfo`: `(X : Ω → S) (Y : Ω → T) (Z : Ω → U) (μ : autoParam (Measure Ω) condMutualInfo._auto_1) : ℝ`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `condRuzsaDist'`: `(X : Ω → G) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist'._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist'._auto_3) : ℝ`
- `cond_construct_good`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (h_min : TauMinimizes p X₁ X₂) (hT : T₁ + T₂ + T₃ = 0) (hT₁ : Measurable T₁) (hT₂ : Measurable T₂) (hT₃ : Measurable T₃) (hR : Measurable R) : d[X…`
- `diff_ent_le_rdist`: `(hX : Measurable X) (hY : Measurable Y) : |H[X; μ] - H[Y; μ']| ≤ 2 * d[X; μ # Y; μ']`
- `first_estimate`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' …`
- `refPackage.X₀₁`: `(self : refPackage Ω₀₁ Ω₀₂ G) (_ : Ω₀₁) : G`
- `refPackage.X₀₂`: `(self : refPackage Ω₀₁ Ω₀₂ G) (_ : Ω₀₂) : G`
- `sum_condMutual_le`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' …`
Helper lemmas folded into the proof: `instFiniteRangeOfFinite`, `rdist_nonneg`, `sum_uvw_eq_zero`
