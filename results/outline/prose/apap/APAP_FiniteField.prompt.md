You are writing the text of a mathematical outline generated from a verified Lean formalisation.
Below are the results of one chapter, in the order the outline presents them. For each you get its Lean name, its
statement in Lean (explicit hypotheses and meaningful instance assumptions such as `[Finite G]` are shown; implicit
arguments and purely structural instances such as `[AddCommGroup G]` are omitted), its
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

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

## Chapter (Lean module `APAP.FiniteField`)

### `ap_in_ff` (theorem)
Lean: `[Module (ZMod q) G] (S : Finset G) (hq : Nat.Prime q) (hα₀ : 0 < α) (hα₂ : α ≤ 2⁻¹) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (hαA₁ : α ≤ ↑A₁.dens) (hαA₂ : α ≤ ↑A₂.dens) : ∃ V x, ↑(Module.finrank (ZMod q) G - Module.finrank (ZMod q) ↥V) ≤ 2 ^ 32 * (1 + Real.log α⁻¹) ^ 2 * (1 + Real.log (ε * α)⁻¹) ^ 2 * ε⁻¹ ^ 2 ∧ |∑ x_1 ∈ S, (mu (↑V).toFinset ∗ᵈ mu A₁ ∗ᵈ mu A₂) x_1 - ∑ x ∈ S, (mu A₁ ∗ᵈ mu A₂) x| ≤ ε`
Proof uses:
- `AlmostPeriodicity.linfty_almost_periodicity_boosted`: `[DiscreteMeasurableSpace G] (ε : ℝ) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (k : ℕ) (hk : k ≠ 0) (hK₂ : 2 ≤ K) (hK : ↑(A.addConst S) ≤ K) (hS : S.Nonempty) (B : Finset G) (C : Finset G) (hB : B.Nonempty) (hC : C.Nonempty) : ∃ T, K ^ (-4096 * ↑⌈1 + Real.log (min 1 (↑C.card / ↑B.card))⁻¹⌉ * ↑k ^ 2 / ε ^ 2) * ↑S.card ≤ ↑T.card ∧ ‖mu T ∗ᵈ^ k ∗ᵈ ((mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C) - (mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C‖_[⊤] ≤ ε`
- `MeasureTheory.cLpNorm`: `(p : ENNReal) (f : α → E) : ℝ`
- `MeasureTheory.dLpNorm`: `(p : ENNReal) (f : α → E) : ℝ`
- `chang`: `[DiscreteMeasurableSpace G] (hf : f ≠ 0) (hη : 0 < η) : ∃ Δ ⊆ largeSpec f η, Δ.card ≤ ⌈changConst * Real.exp 1 * ↑⌈1 + Real.log (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2 / ↑(Fintype.card G))⁻¹⌉₊ / η ^ 2⌉₊ ∧ largeSpec f η ⊆ Δ.addSpan`
- `changConst`: `ℝ`
- `ddconv_eq_sum_sub`: `(f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
- `dddconv`: `[StarRing R] (f : G → R) (g : G → R) (_ : G) : R`
- `dft`: `(f : G → ℂ) (_ : AddChar G ℂ) : ℂ`
- `iterConv`: `(f : G → R) (_ : ℕ) (_ : G) : R`
- `largeSpec`: `(f : G → ℂ) (η : ℝ) : Finset (AddChar G ℂ)`
Helper lemmas folded into the proof: `AddChar.codim_iInf_ker_le_finsetCard`, `AddChar.codim_iInf_ker_le_fintypeCard`, `AddChar.expect_iInf_ker_eq_one_of_mem_closure`, `AddChar.expect_iInf_ker_eq_zero_of_not_mem_closure`, `AddChar.ker_toZModLinearMap`, `AddChar.map_doubleDualEquiv_symm`, `AddChar.map_eq_one_of_mem_closure`, `AddChar.map_zmod_smul`

### `global_dichotomy` (theorem)
Lean: `[DiscreteMeasurableSpace G] (hA : A.Nonempty) (hγC : γ ≤ ↑C.dens) (hγ : 0 < γ) (hAC : ε ≤ |↑(Fintype.card G) * ⟪mu A ∗ᵈ mu A, mu C⟫_[ℝ] - 1|) : ε / (2 * ↑(Fintype.card G)) ≤ ‖Fintype.balance (mu A) ○ᵈ Fintype.balance (mu A)‖_[↑(2 * ⌈1 + Real.log γ⁻¹⌉₊), mu Finset.univ]`
Proof uses:
- `MeasureTheory.dLpNorm`: `(p : ENNReal) (f : α → E) : ℝ`
- `balance_ddconv`: `[CharZero R] (f : G → R) (g : G → R) : Fintype.balance (f ∗ᵈ g) = Fintype.balance f ∗ᵈ Fintype.balance g`
- `dLpNorm_ddconv_le_dLpNorm_dddconv`: `[DiscreteMeasurableSpace G] (hn₀ : n ≠ 0) (hn : Even n) (f : G → ℂ) : ‖f ∗ᵈ f‖_[↑n] ≤ ‖f ○ᵈ f‖_[↑n]`
- `ddconv_eq_sum_sub`: `(f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
Helper lemmas folded into the proof: `Complex.ofReal_comp_ddconv`, `Complex.ofReal_comp_dddconv`, `Complex.ofReal_ddconv`, `Complex.ofReal_dddconv`, `MeasureTheory.Complex.dLpNorm_coe_comp`, `MeasureTheory.RCLike.dLpNorm_coe_comp`, `MeasureTheory.abs_wInner_one_le_dLpNorm_mul_dLpNorm`, `MeasureTheory.dL1Norm_eq_sum_norm`

### `di_in_ff` (theorem)
Lean: `[Module (ZMod q) G] [DiscreteMeasurableSpace G] (hq : Nat.Prime q) (hε₀ : 0 < ε) (hε₁ : ε < 1) (hγC : γ ≤ ↑C.dens) (hγ : 0 < γ) (hAC : ε ≤ |↑(Fintype.card G) * ⟪mu A ∗ᵈ mu A, mu C⟫_[ℝ] - 1|) : ∃ V x, ↑(Module.finrank (ZMod q) G - Module.finrank (ZMod q) ↥V) ≤ 2 ^ 128 * (1 + Real.log (↑A.dens)⁻¹) ^ 4 * (1 + Real.log γ⁻¹) ^ 4 / ε ^ 12 ∧ (1 + ε / 32) * ↑A.dens ≤ ‖((↑A).indicator fun x => 1) ∗ᵈ mu (↑V).toFinset‖_[⊤]`
Proof uses:
- `ap_in_ff`: `[Module (ZMod q) G] (S : Finset G) (hq : Nat.Prime q) (hα₀ : 0 < α) (hα₂ : α ≤ 2⁻¹) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (hαA₁ : α ≤ ↑A₁.dens) (hαA₂ : α ≤ ↑A₂.dens) : ∃ V x, ↑(Module.finrank (ZMod q) G - Module.finrank (ZMod q) ↥V) ≤ 2 ^ 32 * (1 + Real.log α⁻¹) ^ 2 * (1 + Real.log (ε * α)⁻¹) ^ 2 * ε⁻¹ ^ 2 ∧ |∑ x_1 ∈ S, (mu (↑V).toFinset ∗ᵈ mu A₁ ∗ᵈ mu A₂) x_1 - ∑ x ∈ S, (mu A₁ ∗ᵈ mu A₂) x| ≤ ε`
- `balance_dddconv`: `[CharZero R] [StarRing R] (f : G → R) (g : G → R) : Fintype.balance (f ○ᵈ g) = Fintype.balance f ○ᵈ Fintype.balance g`
- `ddconv_eq_sum_sub`: `(f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
- `global_dichotomy`: `[DiscreteMeasurableSpace G] (hA : A.Nonempty) (hγC : γ ≤ ↑C.dens) (hγ : 0 < γ) (hAC : ε ≤ |↑(Fintype.card G) * ⟪mu A ∗ᵈ mu A, mu C⟫_[ℝ] - 1|) : ε / (2 * ↑(Fintype.card G)) ≤ ‖Fintype.balance (mu A) ○ᵈ Fintype.balance (mu A)‖_[↑(2 * ⌈1 + Real.log γ⁻¹⌉₊), mu Finset.univ]`
- `sifting_cor`: `[DiscreteMeasurableSpace G] (hε : 0 < ε) (hε₁ : ε ≤ 1) (hδ : 0 < δ) (hp : Even p) (hp₀ : p ≠ 0) (hpε : ε⁻¹ * Real.log (2 / δ) ≤ ↑p) (hA : A.Nonempty) : ∃ A₁ A₂, 1 - δ ≤ ∑ x ∈ s (↑p) ε Finset.univ Finset.univ A, (mu A₁ ○ᵈ mu A₂) x ∧ 4⁻¹ * ↑A.dens ^ (2 * p) ≤ ↑A₁.dens ∧ 4⁻¹ * ↑A.dens ^ (2 * p) ≤ ↑A₂.dens`
- `unbalancing`: `[DiscreteMeasurableSpace G] (p : ℕ) (hp : p ≠ 0) (ε : ℝ) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (f : G → ℝ) (g : G → ℂ) (h : G → ℂ) (hf : g ○ᵈ g = Complex.ofReal ∘ f) (hh : h ○ᵈ h = mu Finset.univ) (hε : ε ≤ ‖f‖_[↑p, mu Finset.univ]) : ∃ p', ↑p' ≤ 2 ^ 10 * ε⁻¹ ^ 2 * ↑p ∧ 1 + ε / 2 ≤ ‖f + 1‖_[↑p', mu Finset.univ]`
Helper lemmas folded into the proof: `Complex.ofReal_comp_mu`, `Complex.ofReal_dddconv`, `Complex.ofReal_mu`, `MeasureTheory.dL1Norm_eq_sum_norm`, `MeasureTheory.dL1Norm_mu`, `MeasureTheory.dLinftyNorm_eq_iSup_norm`, `MeasureTheory.dLpNorm_conj`, `MeasureTheory.dLpNorm_conjneg`

### `ff` (theorem)
Lean: `[Module (ZMod q) G] (hq₃ : 3 ≤ q) (hq : Nat.Prime q) (hA₀ : A.Nonempty) (hA : ThreeAPFree ↑A) : ↑(Module.finrank (ZMod q) G) ≤ 2 ^ 148 * (1 + Real.log (↑A.dens)⁻¹) ^ 9`
Proof uses:
- `MeasureTheory.dLpNorm`: `(p : ENNReal) (f : α → E) : ℝ`
- `ddconv`: `(f : G → R) (g : G → R) (_ : G) : R`
- `ddconv_eq_sum_sub`: `(f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
- `di_in_ff`: `[Module (ZMod q) G] [DiscreteMeasurableSpace G] (hq : Nat.Prime q) (hε₀ : 0 < ε) (hε₁ : ε < 1) (hγC : γ ≤ ↑C.dens) (hγ : 0 < γ) (hAC : ε ≤ |↑(Fintype.card G) * ⟪mu A ∗ᵈ mu A, mu C⟫_[ℝ] - 1|) : ∃ V x, ↑(Module.finrank (ZMod q) G - Module.finrank (ZMod q) ↥V) ≤ 2 ^ 128 * (1 + Real.log (↑A.dens)⁻¹) ^ 4 * (1 + Real.log γ⁻¹) ^ 4 / ε ^ 12 ∧ (1 + ε / 32) * ↑A.dens ≤ ‖((↑A).indicator fun x => 1) ∗ᵈ mu (↑V).toFinset‖_[⊤]`
- `mu`: `(s : Finset α) (_ : α) : K`
Helper lemmas folded into the proof: `Finset.dens_addSubgroup_preimage_vadd_eq_indicator_one_ddconv_mu`, `MeasureTheory.dLinftyNorm_eq_iSup_norm`, `ThreeAPFree.wInner_one_mu_ddconv_mu_mu_two_smul_mu`, `curlog_pos`, `ddconv_apply_nonneg`, `ddconv_comm`, `ddconv_eq_sum_sub'`, `ddconv_indicator_one`
