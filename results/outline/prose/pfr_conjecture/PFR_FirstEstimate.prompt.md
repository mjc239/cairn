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

## Chapter (Lean module `PFR.FirstEstimate`)

### `diff_rdist_le_3` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂' : Measurable X₂') (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₂', X₁'] volume) : d[p.X₀₁ # X₁ | X₁ + X₂'] - d[p.X₀₁ # X₁] ≤ d[X₁ # X₂] / 2 + H[X₁] / 4 - H[X₂] / 4`
Docstring: $$ d[X_1^0;X_1|X_1+\tilde X_2] - d[X_1^0;X_1] \leq \tfrac{1}{2} k + \tfrac{1}{4} \mathbb{H}[X_1] - \tfrac{1}{4} \mathbb{H}[X_2].$$
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `ProbabilityTheory.entropy_add_right`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨X, X + Y⟩; μ] = H[⟨X, Y⟩; μ]`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `ProbabilityTheory.mutualInfo`: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) mutualInfo._auto_1) : ℝ`
- `ProbabilityTheory.mutualInfo_eq_zero`: `(hX : Measurable X) (hY : Measurable Y) : I[X : Y ; μ] = 0 ↔ IndepFun X Y μ`
- `comparison_of_ruzsa_distances`: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun Y Z μ') : d[X; μ # Y + Z; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z; μ'] - H[Y; μ']) / 2 ∧ ∀ (a : Module (ZMod 2) G), …`
- `condRuzsaDist`: `(X : Ω → G) (Z : Ω → S) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist._auto_3) : ℝ`
- `condRuzsaDist_le`: `(μ : Measure Ω) (μ' : Measure Ω') (hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) : d[X | Z ; μ # Y | W ; μ'] ≤ d[X; μ # Y; μ'] + I[X : Z ; μ] / 2 + I[Y : W ; μ'] / 2`
- `condRuzsaDist_of_const`: `(hX : Measurable X) (Y : Ω' → G) (W : Ω' → T) (c : S) : d[X | fun x => c ; μ # Y | W ; μ'] = d[X ; μ # Y | W ; μ']`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
Helper lemmas folded into the proof: `FiniteRange.add`, `FiniteRange.finite`, `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr_right`, `ProbabilityTheory.IndepFun.entropy_pair_eq_add`, `ProbabilityTheory.IndepFun.mutualInfo_eq_zero`, `ProbabilityTheory.entropy_pair_eq_add`

### `diff_rdist_le_4` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (h₁ : IdentDistrib X₁ X₁' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₂', X₁'] volume) : d[p.X₀₂ # X₂ | X₂ + X₁'] - d[p.X₀₂ # X₂] ≤ d[X₁ # X₂] / 2 + H[X₂] / 4 - H[X₁] / 4`
Docstring: $$ d[X_2^0; X_2|X_2+\tilde X_1] - d[X_2^0; X_2] \leq \tfrac{1}{2}k + \tfrac{1}{4} \mathbb{H}[X_2] - \tfrac{1}{4} \mathbb{H}[X_1].$$
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `ProbabilityTheory.entropy_add_right`: `(hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨X, X + Y⟩; μ] = H[⟨X, Y⟩; μ]`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `ProbabilityTheory.mutualInfo`: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) mutualInfo._auto_1) : ℝ`
- `ProbabilityTheory.mutualInfo_eq_zero`: `(hX : Measurable X) (hY : Measurable Y) : I[X : Y ; μ] = 0 ↔ IndepFun X Y μ`
- `comparison_of_ruzsa_distances`: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun Y Z μ') : d[X; μ # Y + Z; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z; μ'] - H[Y; μ']) / 2 ∧ ∀ (a : Module (ZMod 2) G), …`
- `condRuzsaDist`: `(X : Ω → G) (Z : Ω → S) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist._auto_3) : ℝ`
- `condRuzsaDist_le`: `(μ : Measure Ω) (μ' : Measure Ω') (hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) : d[X | Z ; μ # Y | W ; μ'] ≤ d[X; μ # Y; μ'] + I[X : Z ; μ] / 2 + I[Y : W ; μ'] / 2`
- `condRuzsaDist_of_const`: `(hX : Measurable X) (Y : Ω' → G) (W : Ω' → T) (c : S) : d[X | fun x => c ; μ # Y | W ; μ'] = d[X ; μ # Y | W ; μ']`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
Helper lemmas folded into the proof: `FiniteRange.add`, `FiniteRange.finite`, `MeasureTheory.Measure.ennreal_smul_real_apply`, `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr_right`, `ProbabilityTheory.IndepFun.entropy_pair_eq_add`, `ProbabilityTheory.IndepFun.mutualInfo_eq_zero`

### `rdist_add_rdist_add_condMutual_eq` (theorem)
Lean: `(X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₂', X₁'] volume) : d[X₁ + X₂' # X₂ + X₁'] + d[X₁ | X₁ + X₂' # X₂ | X₂ + X₁'] + I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂'] = 2 * d[X₁ # X₂]`
Docstring: The sum of $$ d[X_1+\tilde X_2;X_2+\tilde X_1] + d[X_1|X_1+\tilde X_2; X_2|X_2+\tilde X_1] $$ and $$ I[X_1+ X_2 : \tilde X_1 + X_2 \,|\, X_1 + X_2 + \tilde X_1 + \tilde X_2] $$ is equal to $2k$.
Proof uses:
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `sum_of_rdist_eq_char_2`: `(Y : Fin 4 → Ω → G) (h_indep : iIndepFun Y μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : d[Y 0; μ # Y 1; μ] + d[Y 2; μ # Y 3; μ] = d[Y 0 + Y 2; μ # Y 1 + Y 3; μ] + d[Y 0 | Y 0 + Y 2 ; μ # Y 1 | Y 1…`
Helper lemmas folded into the proof: `MeasureTheory.Measure.ennreal_smul_real_apply`, `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.entropy_comp_of_injective`, `ProbabilityTheory.entropy_def`, `ProbabilityTheory.entropy_neg`, `ProbabilityTheory.measureEntropy_map_of_injective`, `rdist_def`

### `rdist_of_sums_ge` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h_min : TauMinimizes p X₁ X₂) : d[X₁ + X₂' # X₂ + X₁'] ≥ d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁ + X₂'] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂ + X₁'] - d[p.X₀₂ # X₂])`
Docstring: The distance $d[X_1+\tilde X_2; X_2+\tilde X_1]$ is at least $$k - \eta (d[X^0_1; X_1+\tilde X_2] - d[X^0_1; X_1]) - \eta (d[X^0_2; X_2+\tilde X_1] - d[X^0_2; X_2]).$$
Proof uses:
- `distance_ge_of_min`: `(p : refPackage Ω₀₁ Ω₀₂ G) (h : TauMinimizes p X₁ X₂) (h1 : Measurable X₁') (h2 : Measurable X₂') : d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁'] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂'] - d[p.X₀₂ # X₂]) ≤ d[X₁…`

### `first_estimate` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₂', X₁'] volume) (h_min : TauMinimizes p X₁ X₂) : I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂'] ≤ 2 * p.η * d[X₁ # X₂]`
Docstring: We have $I_1 \leq 2 \eta k$
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `comparison_of_ruzsa_distances`: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun Y Z μ') : d[X; μ # Y + Z; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z; μ'] - H[Y; μ']) / 2 ∧ ∀ (a : Module (ZMod 2) G), …`
- `condRuzsaDist`: `(X : Ω → G) (Z : Ω → S) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist._auto_3) : ℝ`
- `condRuzsaDist'`: `(X : Ω → G) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist'._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist'._auto_3) : ℝ`
- `condRuzsaDist_diff_le`: `(μ : Measure Ω) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun Y Z μ') : d[X; μ # Y + Z; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z; μ'] - H[Y; μ']) / 2`
- `condRuzsaDistance_ge_of_min`: `(p : refPackage Ω₀₁ Ω₀₂ G) (h : TauMinimizes p X₁ X₂) (h1 : Measurable X₁') (h2 : Measurable X₂') (Z : Ω'₁ → S) (W : Ω'₂ → T) (hZ : Measurable Z) (hW : Measurable W) : d[X₁ # X₂] - p.η * (d[p.X₀₁ # X…`
- `diff_rdist_le_3`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂' : Measurable X₂') (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, …`
- `diff_rdist_le_4`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (h₁ : IdentDistrib X₁ X₁' volume volume) (h_indep : iIndepFun ![X₁, X₂, …`
Helper lemmas folded into the proof: `MeasureTheory.Measure.ennreal_smul_real_apply`, `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr_right`, `ProbabilityTheory.entropy_comp_of_injective`, `ProbabilityTheory.entropy_def`, `ProbabilityTheory.entropy_neg`, `ProbabilityTheory.measureEntropy_map_of_injective`

### `ent_ofsum_le` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₂', X₁'] volume) (h_min : TauMinimizes p X₁ X₂) : H[X₁ + X₂ + X₁' + X₂'] ≤ H[X₁] / 2 + H[X₂] / 2 + (2 + p.η) * d[X₁ # X₂] - I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂']`
Docstring: $$\mathbb{H}[X_1+X_2+\tilde X_1+\tilde X_2] \le \tfrac{1}{2} \mathbb{H}[X_1]+\tfrac{1}{2} \mathbb{H}[X_2] + (2 + \eta) k - I_1.$$
Proof uses:
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `condRuzsaDist`: `(X : Ω → G) (Z : Ω → S) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist._auto_3) : ℝ`
- `condRuzsaDist'`: `(X : Ω → G) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist'._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist'._auto_3) : ℝ`
- `condRuzsaDistance_ge_of_min`: `(p : refPackage Ω₀₁ Ω₀₂ G) (h : TauMinimizes p X₁ X₂) (h1 : Measurable X₁') (h2 : Measurable X₂') (Z : Ω'₁ → S) (W : Ω'₂ → T) (hZ : Measurable Z) (hW : Measurable W) : d[X₁ # X₂] - p.η * (d[p.X₀₁ # X…`
- `diff_rdist_le_3`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂' : Measurable X₂') (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, …`
- `diff_rdist_le_4`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (h₁ : IdentDistrib X₁ X₁' volume volume) (h_indep : iIndepFun ![X₁, X₂, …`
- `prod`: `(X : Ω → S) (Y : Ω → T) (ω : Ω) : S × T`
- `rdist_add_rdist_add_condMutual_eq`: `(X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h₂ : IdentD…`
- `refPackage.X₀₁`: `(self : refPackage Ω₀₁ Ω₀₂ G) (_ : Ω₀₁) : G`
- `refPackage.X₀₂`: `(self : refPackage Ω₀₁ Ω₀₂ G) (_ : Ω₀₂) : G`
Helper lemmas folded into the proof: `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr_left`, `ProbabilityTheory.IdentDistrib.rdist_congr_right`, `ProbabilityTheory.IndepFun.rdist_eq`, `ProbabilityTheory.entropy_def`, `condRuzsaDist_of_sums_ge`, `rdist_def`
