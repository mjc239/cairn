You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. Compare the
English with the full statement; anything the English attributes to the docstring must actually be in it.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Definitions are held to the same standard: the English must name the setting the signature assumes
("for an abelian group $G$ and …, $\mathrm{rdist}$ is …"). Replacing an assumption by a stronger one (a metric
space where the Lean has a pseudometric space) is unfaithful too, and so is leaving a restrictive type unstated
(a natural number, a nonnegative real). Citations (theorem or lemma numbers) and remarks are claims too: each must
be supported by the docstring or the Lean. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `rudin_ineq`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hp : 2 ≤ p) (f : G → ℂ) (hf : AddDissociated (Function.support (cft f))) : ‖f‖ₙ_[↑p] ≤ 4 * Real.exp 2⁻¹ * √↑p * ‖f‖ₙ_[2]`
Lean (full): `∀ {G : Type u_1} [inst : Fintype G] [inst_1 : AddCommGroup G] {p : ℕ} [inst_2 : MeasurableSpace G] [DiscreteMeasurableSpace G], (2 : ℕ) ≤ p → ∀ (f : G → ℂ), AddDissociated (α := AddChar G ℂ) (Function.support (cft f)) → ‖f‖ₙ_[↑p] ≤ (4 : ℝ) * Real.exp (2 : ℝ)⁻¹ * √↑p * ‖f‖ₙ_[(2 : ENNReal)]`
Docstring: **Rudin's inequality**, usual form.
English: (Rudin's inequality, usual form, per the docstring.) Let $G$ be a finite abelian group with a measurable-space structure that is discrete (every set is measurable). Let $p$ be a natural number with $p \ge 2$, and let $f : G \to \mathbb{C}$ be such that the support of its discrete Fourier transform $\mathrm{cft}(f)$ (a set of additive characters $G \to \mathbb{C}$) is dissociated. Then $\|f\|_p \le 4\, e^{1/2} \sqrt{p}\, \|f\|_2$, where the norms are the normalised (expectation) $L^p$ and $L^2$ norms on $G$.
