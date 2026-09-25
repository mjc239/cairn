You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

### `rudin_ineq`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hp : 2 ≤ p) (f : G → ℂ) (hf : AddDissociated (Function.support (cft f))) : ‖f‖ₙ_[↑p] ≤ 4 * Real.exp 2⁻¹ * √↑p * ‖f‖ₙ_[2]`
Lean (full): `∀ {G : Type u_1} [inst : Fintype G] [inst_1 : AddCommGroup G] {p : ℕ} [inst_2 : MeasurableSpace G] [DiscreteMeasurableSpace G], (2 : ℕ) ≤ p → ∀ (f : G → ℂ), AddDissociated (α := AddChar G ℂ) (Function.support (cft f)) → ‖f‖ₙ_[↑p] ≤ (4 : ℝ) * Real.exp (2 : ℝ)⁻¹ * √↑p * ‖f‖ₙ_[(2 : ENNReal)]`
Docstring: **Rudin's inequality**, usual form.
Previous English: (Rudin's inequality.) Let $G$ be a finite abelian group carrying the discrete measurable structure. Let $p \ge 2$ and let $f : G \to \mathbb{C}$ be such that the support of its Fourier transform $\mathrm{cft}(f)$ is dissociated. Then $\|f\|_p \le 4\, e^{1/2} \sqrt{p}\, \|f\|_2$, with norms in the compact (expectation) normalisation.
Checker's issue: p is a natural number in the Lean, but the English leaves p untyped, reading as a real p ≥ 2 and so claiming more.
