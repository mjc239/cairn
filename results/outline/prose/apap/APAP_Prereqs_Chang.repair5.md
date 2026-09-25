You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring, and when no
docstring or Lean supports a description of an object, name it instead of describing it. Give every variable its
type, introduce every symbol, and never use one letter for two things.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

### `general_hoelder`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hη : 0 ≤ η) (ν : G → NNReal) (hfν : ∀ (x : G), f x ≠ 0 → 1 ≤ ν x) (hΔ : Δ ⊆ largeSpec f η) (hm : m ≠ 0) : ↑Δ.card ^ (2 * m) * (η ^ (2 * m) * (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2)) ≤ energy m Δ (dft fun a => ↑↑(ν a))`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {f : G → ℂ} {η : ℝ} {Δ : Finset (AddChar G ℂ)} {m : ℕ} [inst_1 : Fintype G] [inst_2 : MeasurableSpace G] [DiscreteMeasurableSpace G], (0 : ℝ) ≤ η → ∀ (ν : G → NNReal), (∀ (x : G), f x ≠ (0 : ℂ) → (1 : NNReal) ≤ ν x) → Δ ⊆ largeSpec f η → m ≠ (0 : ℕ) → HPow.hPow (α := ℝ) (↑Δ.card) ((2 : ℕ) * m) * (η ^ ((2 : ℕ) * m) * (‖f‖_[(1 : ENNReal)] ^ (2 : ℕ) / ‖f‖_[(2 : ENNReal)] ^ (2 : ℕ))) ≤ energy m Δ (dft fun a => ↑↑(ν a))`
Previous English: Let $G$ be a finite abelian group carrying the discrete measurable structure. Let $\eta \ge 0$, let $\nu : G \to \mathbb{R}_{\ge 0}$ satisfy $1 \le \nu(x)$ whenever $f(x) \ne 0$, let $\Delta \subseteq \operatorname{largeSpec}(f, \eta)$, and let $m \ne 0$. Then $|\Delta|^{2m}\left(\eta^{2m}\,\frac{\|f\|_1^2}{\|f\|_2^2}\right) \le \mathrm{energy}_m(\Delta, \widehat{\nu})$, where $\widehat{\nu}$ is the discrete Fourier transform of $\nu$.
Checker's issue: The natural-number type of m is left unstated (only 'm ≠ 0'), and f is never introduced as a function G → ℂ; Δ is implicitly a finite set of additive characters.

### `spec_hoelder`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hη : 0 ≤ η) (hΔ : Δ ⊆ largeSpec f η) (hm : m ≠ 0) : ↑Δ.card ^ (2 * m) * (η ^ (2 * m) * (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2 / ↑(Fintype.card G))) ≤ boringEnergy m Δ`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {f : G → ℂ} {η : ℝ} {Δ : Finset (AddChar G ℂ)} {m : ℕ} [inst_1 : Fintype G] [inst_2 : MeasurableSpace G] [DiscreteMeasurableSpace G], (0 : ℝ) ≤ η → Δ ⊆ largeSpec f η → m ≠ (0 : ℕ) → HPow.hPow (α := ℝ) (↑Δ.card) ((2 : ℕ) * m) * (η ^ ((2 : ℕ) * m) * (‖f‖_[(1 : ENNReal)] ^ (2 : ℕ) / ‖f‖_[(2 : ENNReal)] ^ (2 : ℕ) / ↑(Fintype.card G))) ≤ boringEnergy m Δ`
Previous English: Let $G$ be a finite abelian group carrying the discrete measurable structure. Let $\eta \ge 0$, $\Delta \subseteq \operatorname{largeSpec}(f, \eta)$ and $m \ne 0$. Then $|\Delta|^{2m}\left(\eta^{2m}\,\frac{\|f\|_1^2/\|f\|_2^2}{|G|}\right) \le \mathrm{boringEnergy}_m(\Delta)$.
Checker's issue: The natural-number type of m is left unstated (only 'm ≠ 0'), and f is never introduced as a function G → ℂ.

### `chang`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hf : f ≠ 0) (hη : 0 < η) : ∃ Δ ⊆ largeSpec f η, Δ.card ≤ ⌈changConst * Real.exp 1 * ↑⌈1 + Real.log (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2 / ↑(Fintype.card G))⁻¹⌉₊ / η ^ 2⌉₊ ∧ largeSpec f η ⊆ Δ.addSpan`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {f : G → ℂ} {η : ℝ} [inst_1 : Fintype G] [inst_2 : MeasurableSpace G] [DiscreteMeasurableSpace G], f ≠ (0 : G → ℂ) → (0 : ℝ) < η → ∃ Δ ⊆ largeSpec f η, Δ.card ≤ ⌈changConst * Real.exp (1 : ℝ) * ↑⌈(1 : ℝ) + Real.log (‖f‖_[(1 : ENNReal)] ^ (2 : ℕ) / ‖f‖_[(2 : ENNReal)] ^ (2 : ℕ) / ↑(Fintype.card G))⁻¹⌉₊ / η ^ (2 : ℕ)⌉₊ ∧ largeSpec f η ⊆ Δ.addSpan`
Docstring: **Chang's lemma**.
Previous English: (Chang's lemma.) Let $G$ be a finite abelian group carrying the discrete measurable structure. If $f \ne 0$ and $\eta > 0$, then there is a finite set $\Delta \subseteq \operatorname{largeSpec}(f, \eta)$ such that $|\Delta| \le \left\lceil \mathrm{changConst}\cdot e \cdot \left\lceil 1 + \log\Big(1 \big/ \big(\|f\|_1^2 / \|f\|_2^2 / |G|\big)\Big)\right\rceil / \eta^2 \right\rceil$ (both ceilings being natural-number ceilings) and $\operatorname{largeSpec}(f, \eta)$ is contained in the additive span of $\Delta$.
Checker's issue: f is never given a type (a function G → ℂ); same gap as general_hoelder/spec_hoelder.
