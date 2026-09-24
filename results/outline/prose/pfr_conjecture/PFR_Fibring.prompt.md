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

## Chapter (Lean module `PFR.Fibring`)

### `rdist_of_indep_eq_sum_fibre` (theorem)
Lean: `(π : H →+ H') (h : IndepFun Z_1 Z_2 μ) (h1 : Measurable Z_1) (h2 : Measurable Z_2) : d[Z_1; μ # Z_2; μ] = d[⇑π ∘ Z_1; μ # ⇑π ∘ Z_2; μ] + d[Z_1 | ⇑π ∘ Z_1 ; μ # Z_2 | ⇑π ∘ Z_2 ; μ] + I[Z_1 - Z_2 : ⟨⇑π ∘ Z_1, ⇑π ∘ Z_2⟩|⇑π ∘ (Z_1 - Z_2);μ]`
Docstring: If $Z_1, Z_2$ are independent, then $d[Z_1; Z_2]$ is equal to $$ d[\pi(Z_1);\pi(Z_2)] + d[Z_1|\pi(Z_1); Z_2 |\pi(Z_2)]$$ plus $$I( Z_1 - Z_2 : (\pi(Z_1), \pi(Z_2)) | \pi(Z_1 - Z_2) ).$$
Proof uses:
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `ProbabilityTheory.FiniteSupport`: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
- `ProbabilityTheory.Kernel.AEFiniteKernelSupport`: `(κ : Kernel T S) (μ : Measure T) : Prop`
- `ProbabilityTheory.Kernel.FiniteKernelSupport`: `(κ : Kernel T S) : Prop`
- `ProbabilityTheory.Kernel.chain_rule`: `(hκ : κ.AEFiniteKernelSupport μ) : Hk[κ , μ] = Hk[κ.fst , μ] + Hk[κ.condKernel , μ.compProd κ.fst]`
- `ProbabilityTheory.Kernel.entropy`: `(κ : Kernel T S) (μ : Measure T) : ℝ`
- `ProbabilityTheory.Kernel.entropy_prodMkLeft_unit`: `(κ : Kernel T S) : Hk[Kernel.prodMkLeft Unit κ , Measure.map (Prod.mk ()) μ] = Hk[κ , μ]`
- `ProbabilityTheory.condEntropy`: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) condEntropy._auto_1) : ℝ`
- `ProbabilityTheory.condEntropy_eq_kernel_entropy`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[X | Y ; μ] = Hk[condDistrib X Y μ , Measure.map Y μ]`
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.mem_iff`, `FiniteRange.null_of_compl`, `FiniteRange.range`, `FiniteRange.sub`, `MeasureTheory.Measure.ennreal_smul_real_apply`, `MeasureTheory.Measure.support`, `ProbabilityTheory.FiniteSupport.finite`

### `sum_of_rdist_eq_step_condMutualInfo` (theorem)
Lean: `(h_meas : ∀ (i : Fin 4), Measurable (Y i)) : I[⟨Y 0 - Y 1, Y 2 - Y 3⟩ : ⟨Y 0 - Y 2, Y 1 - Y 3⟩|Y 0 - Y 1 - (Y 2 - Y 3);μ] = I[Y 0 - Y 1 : Y 1 - Y 3|Y 0 - Y 1 - Y 2 + Y 3;μ]`
Docstring: The conditional mutual information step of `sum_of_rdist_eq`
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `ProbabilityTheory.condMutualInfo_of_inj_map`: `(hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (f : U → S → V) (hf : ∀ (t : U), Function.Injective (f t)) : I[fun ω => f (Z ω) (X ω) : Y|Z;μ] = I[X : Y|Z;μ]`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.sub`, `MeasureTheory.Measure.ennreal_smul_real_apply`, `ProbabilityTheory.condMutualInfo_comm`, `ProbabilityTheory.entropy_comm`, `ProbabilityTheory.entropy_comp_of_injective`, `ProbabilityTheory.entropy_def`, `ProbabilityTheory.measureEntropy_map_of_injective`

### `sum_of_rdist_eq_step_condRuzsaDist` (theorem)
Lean: `(h_indep : iIndepFun Y μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : d[⟨Y 0, Y 2⟩ | Y 0 - Y 2 ; μ # ⟨Y 1, Y 3⟩ | Y 1 - Y 3 ; μ] = d[Y 0 | Y 0 - Y 2 ; μ # Y 1 | Y 1 - Y 3 ; μ]`
Docstring: The conditional Ruzsa Distance step of `sum_of_rdist_eq`
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `condRuzsaDist_of_inj_map`: `(Y : Fin 4 → Ω → G) (h_indep : IndepFun (⟨Y 0, Y 2⟩) (⟨Y 1, Y 3⟩) μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) (π : G × G →+ G') (hπ : ∀ (h : G), Function.Injective fun g => π (g, h)) : d[⇑π ∘ ⟨Y 0,…`
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.sub`, `instFiniteRangeComp`, `instFiniteRangeOfFinite`, `instFiniteRangeProdMk`

### `sum_of_rdist_eq` (theorem)
Lean: `(Y : Fin 4 → Ω → G) (h_indep : iIndepFun Y μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : d[Y 0; μ # Y 1; μ] + d[Y 2; μ # Y 3; μ] = d[Y 0 - Y 2; μ # Y 1 - Y 3; μ] + d[Y 0 | Y 0 - Y 2 ; μ # Y 1 | Y 1 - Y 3 ; μ] + I[Y 0 - Y 1 : Y 1 - Y 3|Y 0 - Y 1 - Y 2 + Y 3;μ]`
Docstring: Let $Y_1,Y_2,Y_3$ and $Y_4$ be independent $G$-valued random variables. Then $$d[Y_1-Y_3; Y_2-Y_4] + d[Y_1|Y_1-Y_3; Y_2|Y_2-Y_4] $$ $$ + I[Y_1-Y_2 : Y_2 - Y_4 | Y_1-Y_2-Y_3+Y_4] = d[Y_1; Y_2] + d[Y_3; Y_4].$$
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `ProbabilityTheory.mutualInfo`: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) mutualInfo._auto_1) : ℝ`
- `ProbabilityTheory.mutualInfo_eq_zero`: `(hX : Measurable X) (hY : Measurable Y) : I[X : Y ; μ] = 0 ↔ IndepFun X Y μ`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
- `rdist_of_indep_eq_sum_fibre`: `(π : H →+ H') (h : IndepFun Z_1 Z_2 μ) (h1 : Measurable Z_1) (h2 : Measurable Z_2) : d[Z_1; μ # Z_2; μ] = d[⇑π ∘ Z_1; μ # ⇑π ∘ Z_2; μ] + d[Z_1 | ⇑π ∘ Z_1 ; μ # Z_2 | ⇑π ∘ Z_2 ; μ] + I[Z_1 - Z_2 : ⟨⇑π…`
- `sum_of_rdist_eq_step_condMutualInfo`: `(h_meas : ∀ (i : Fin 4), Measurable (Y i)) : I[⟨Y 0 - Y 1, Y 2 - Y 3⟩ : ⟨Y 0 - Y 2, Y 1 - Y 3⟩|Y 0 - Y 1 - (Y 2 - Y 3);μ] = I[Y 0 - Y 1 : Y 1 - Y 3|Y 0 - Y 1 - Y 2 + Y 3;μ]`
- `sum_of_rdist_eq_step_condRuzsaDist`: `(h_indep : iIndepFun Y μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : d[⟨Y 0, Y 2⟩ | Y 0 - Y 2 ; μ # ⟨Y 1, Y 3⟩ | Y 1 - Y 3 ; μ] = d[Y 0 | Y 0 - Y 2 ; μ # Y 1 | Y 1 - Y 3 ; μ]`
Helper lemmas folded into the proof: `FiniteRange.finite`, `FiniteRange.sub`, `ProbabilityTheory.IndepFun.rdist_eq`, `ProbabilityTheory.entropy_def`, `ProbabilityTheory.entropy_pair_eq_add`, `condRuzsaDist.congr_simp`, `instFiniteRangeComp`, `instFiniteRangeOfFinite`

### `sum_of_rdist_eq_char_2` (theorem)
Lean: `(Y : Fin 4 → Ω → G) (h_indep : iIndepFun Y μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : d[Y 0; μ # Y 1; μ] + d[Y 2; μ # Y 3; μ] = d[Y 0 + Y 2; μ # Y 1 + Y 3; μ] + d[Y 0 | Y 0 + Y 2 ; μ # Y 1 | Y 1 + Y 3 ; μ] + I[Y 0 + Y 1 : Y 1 + Y 3|Y 0 + Y 1 + Y 2 + Y 3;μ]`
Docstring: Let $Y_1,Y_2,Y_3$ and $Y_4$ be independent $G$-valued random variables. Then $$d[Y_1+Y_3; Y_2+Y_4] + d[Y_1|Y_1+Y_3; Y_2|Y_2+Y_4] $$ $$ + I[Y_1+Y_2 : Y_2 + Y_4 | Y_1+Y_2+Y_3+Y_4] = d[Y_1; Y_2] + d[Y_3; Y_4].$$
Proof uses:
- `sum_of_rdist_eq`: `(Y : Fin 4 → Ω → G) (h_indep : iIndepFun Y μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : d[Y 0; μ # Y 1; μ] + d[Y 2; μ # Y 3; μ] = d[Y 0 - Y 2; μ # Y 1 - Y 3; μ] + d[Y 0 | Y 0 - Y 2 ; μ # Y 1 | Y 1…`
Helper lemmas folded into the proof: `condRuzsaDist.congr_simp`
