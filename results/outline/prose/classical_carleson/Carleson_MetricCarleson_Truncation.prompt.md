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

Namespaces open (prefixes omitted): TileStructure, MeasureTheory, Antichain.

## Chapter (Lean module `Carleson.MetricCarleson.Truncation`)

### `R_truncation` (theorem)
Lean: `(hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (hR : R = 2 ^ n) (BST_T_Q : ∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, ⨆ R₁ ∈ Set.Ioo R⁻¹ R, ⨆ R₂ ∈ Set.Ioo R₁ R, ‖T_R K Q R₁ R₂ R f x‖ₑ ≤ ↑(C1_0_2 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Docstring: Lemma 3.0.2.
Proof uses:
- `R_truncation'`: `(hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (hR : R = 2 ^ n) (sF : F ⊆ Metric.ball (…`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `BoundedFiniteSupport`, `C1_0_2`, `C_K`, `C_Ts`, `CompatibleFunctions`, `CoveredByBalls`

### `R_truncation'` (theorem)
Lean: `(hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (hR : R = 2 ^ n) (sF : F ⊆ Metric.ball (cancelPt X) (2 * R)) (sG : G ⊆ Metric.ball (cancelPt X) R) (BST_T_Q : ∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, ⨆ R₁ ∈ Set.Ioo R⁻¹ R, ⨆ R₂ ∈ Set.Ioo R₁ R, ‖T_R K Q R₁ R₂ R f x‖ₑ ≤ ↑(C1_0_2 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Proof uses:
- `P304.succ`: `(P : P304 q q' F f σ₁ σ₂) : P304 q q' F f σ₁ σ₂`
- `S_truncation`: `(hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (bF : Bornology.IsBounded F) (bG : Bornology.IsBounded G) (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖)…`
- `enorm_carlesonOperatorIntegrand_le_T_S`: `(hR₁ : 0 < R₁) (hR₂ : R₁ < R₂) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) : ‖carlesonOperatorIntegrand K (Q x) R₁ R₂ f x‖ₑ ≤ ‖T_S Q (L302 a R₁) (U302 a R₂) f x‖ₑ + 4 * ↑(C2_1_3 a) * …`
- `hasStrongType_maximalFunction`: `(hp₁ : 0 < p₁) (hp₁₂ : p₁ < p₂) : HasStrongType (maximalFunction μ 𝓑 c r ↑p₁) (↑p₂) (↑p₂) μ μ ↑(C2_0_6 A p₁ p₂)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `finitary_carleson_step` (theorem)
Lean: `(CP : CP304 q q' F f σ₁ σ₂) (bG : Bornology.IsBounded G) (mG : MeasurableSet G) : ∃ G' ⊆ G, Bornology.IsBounded G' ∧ MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∫⁻ (x : X) in G \ G', ‖T_lin CP.Q σ₁ σ₂ f x‖ₑ ≤ ↑(C2_0_1 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Proof uses:
- `ProofData`: `(a : outParam ℕ) (q : outParam ℝ) (K : outParam (X → X → ℂ)) (σ₁ : outParam (X → ℤ)) (σ₂ : outParam (X → ℤ)) (F : outParam (Set X)) (G : outParam (Set X)) : Type (u_1 + 1)`
- `ProofData.Q`: `SimpleFunc X (Θ X)`
- `ProofData.toKernelProofData`: `KernelProofData a K`
- `finitary_carleson`: `(X : Type u_1) : ∃ G', MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → ∫⁻ (x : X) in G \ G', ‖∑ s ∈ (Set.Icc (σ₁ x) (σ₂ x)).toFinset…`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `BoundedFiniteSupport`, `C2_0_1`, `C2_0_2`, `CP304`, `CP304.Q`, `C_K`

### `P304.succ` (definition)
Lean: `(P : P304 q q' F f σ₁ σ₂) : P304 q q' F f σ₁ σ₂`
Docstring: Construct `G_{n+1}` given `G_n`.

### `enorm_carlesonOperatorIntegrand_le_T_S` (theorem)
Lean: `(hR₁ : 0 < R₁) (hR₂ : R₁ < R₂) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) : ‖carlesonOperatorIntegrand K (Q x) R₁ R₂ f x‖ₑ ≤ ‖T_S Q (L302 a R₁) (U302 a R₂) f x‖ₑ + 4 * ↑(C2_1_3 a) * globalMaximalFunction volume 1 (F.indicator 1) x`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `linearized_truncation` (theorem)
Lean: `(hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (bF : Bornology.IsBounded F) (bG : Bornology.IsBounded G) (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (mσ₁ : Measurable σ₁) (mσ₂ : Measurable σ₂) (rσ₁ : (Set.range σ₁).Finite) (rσ₂ : (Set.range σ₂).Finite) (lσ : σ₁ ≤ σ₂) (BST_T_Q : ∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, ‖T_lin Q σ₁ σ₂ f x‖ₑ ≤ ↑(C3_0_4 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Docstring: Lemma 3.0.4.
Proof uses:
- `slice_G_subset`: `(slice CP bG mG (n + 1)).G ⊆ (slice CP bG mG n).G`
- `slice_integral_bound_sum`: `∫⁻ (x : X), (G \ (slice CP bG mG (n + 1)).G).indicator (fun x => ‖T_lin CP.Q σ₁ σ₂ f x‖ₑ) x ≤ (↑(C2_0_1 a q) * ∑ i ∈ Finset.range (n + 1), (2⁻¹ ^ i) ^ (↑q')⁻¹) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
- `volume_slice`: `2 * volume (slice CP bG mG (n + 1)).G ≤ volume (slice CP bG mG n).G`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `volume_slice` (theorem)
Lean: `2 * volume (slice CP bG mG (n + 1)).G ≤ volume (slice CP bG mG n).G`
Proof uses:
- `finitary_carleson_step`: `(CP : CP304 q q' F f σ₁ σ₂) (bG : Bornology.IsBounded G) (mG : MeasurableSet G) : ∃ G' ⊆ G, Bornology.IsBounded G' ∧ MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∫⁻ (x : X) in G \ G', ‖T_lin CP.Q σ₁…`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `BoundedFiniteSupport`, `C2_0_1`, `C2_0_2`, `CP304`, `CP304.Q`, `C_K`

### `slice_G_subset` (theorem)
Lean: `(slice CP bG mG (n + 1)).G ⊆ (slice CP bG mG n).G`
Proof uses:
- `finitary_carleson_step`: `(CP : CP304 q q' F f σ₁ σ₂) (bG : Bornology.IsBounded G) (mG : MeasurableSet G) : ∃ G' ⊆ G, Bornology.IsBounded G' ∧ MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∫⁻ (x : X) in G \ G', ‖T_lin CP.Q σ₁…`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `BoundedFiniteSupport`, `C2_0_1`, `C2_0_2`, `CP304`, `CP304.Q`, `C_K`

### `slice_integral_bound` (theorem)
Lean: `∫⁻ (x : X) in (slice CP bG mG n).G \ (slice CP bG mG (n + 1)).G, ‖T_lin CP.Q σ₁ σ₂ f x‖ₑ ≤ ↑(C2_0_1 a q) * volume (slice CP bG mG n).G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Proof uses:
- `finitary_carleson_step`: `(CP : CP304 q q' F f σ₁ σ₂) (bG : Bornology.IsBounded G) (mG : MeasurableSet G) : ∃ G' ⊆ G, Bornology.IsBounded G' ∧ MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∫⁻ (x : X) in G \ G', ‖T_lin CP.Q σ₁…`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `BoundedFiniteSupport`, `C2_0_1`, `C2_0_2`, `CP304`, `CP304.Q`, `C_K`

### `slice_integral_bound_sum` (theorem)
Lean: `∫⁻ (x : X), (G \ (slice CP bG mG (n + 1)).G).indicator (fun x => ‖T_lin CP.Q σ₁ σ₂ f x‖ₑ) x ≤ (↑(C2_0_1 a q) * ∑ i ∈ Finset.range (n + 1), (2⁻¹ ^ i) ^ (↑q')⁻¹) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Docstring: The slightly unusual way of writing the integrand is to facilitate applying the monotone convergence theorem.
Proof uses:
- `slice_G_subset`: `(slice CP bG mG (n + 1)).G ⊆ (slice CP bG mG n).G`
- `slice_integral_bound`: `∫⁻ (x : X) in (slice CP bG mG n).G \ (slice CP bG mG (n + 1)).G, ‖T_lin CP.Q σ₁ σ₂ f x‖ₑ ≤ ↑(C2_0_1 a q) * volume (slice CP bG mG n).G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
- `volume_slice`: `2 * volume (slice CP bG mG (n + 1)).G ≤ volume (slice CP bG mG n).G`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `BoundedFiniteSupport`, `C2_0_1`, `C2_0_2`, `CP304`, `CP304.Q`, `C_K`

### `S_truncation` (theorem)
Lean: `(hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (bF : Bornology.IsBounded F) (bG : Bornology.IsBounded G) (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (BST_T_Q : ∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, ⨆ s₁ ∈ Finset.Icc (-↑B) ↑B, ⨆ s₂ ∈ Finset.Icc s₁ ↑B, ‖T_S Q s₁ s₂ f x‖ₑ ≤ ↑(C3_0_4 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Docstring: Lemma 3.0.3. `B` is the blueprint's `S`.
Proof uses:
- `linearized_truncation`: `(hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (bF : Bornology.IsBounded F) (bG : Bornology.IsBounded G) (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖)…`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`
