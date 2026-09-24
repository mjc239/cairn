You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Keep every
hypothesis the Lean shows, including instance assumptions such as `[Finite G]` or `[IsProbabilityMeasure μ]`
(say them in words: "$G$ is finite", "$\mu$ is a probability measure"), and the exact conclusion. Do not add
claims the Lean does not make. Purely structural instances (e.g. `[AddCommGroup G]`) and implicit arguments are not
shown and may stay implicit.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

### `rudin_ineq`
Lean: `[Fintype G] [DiscreteMeasurableSpace G] (hp : 2 ≤ p) (f : G → ℂ) (hf : AddDissociated (Function.support (cft f))) : ‖f‖ₙ_[↑p] ≤ 4 * Real.exp 2⁻¹ * √↑p * ‖f‖ₙ_[2]`
Docstring: **Rudin's inequality**, usual form.
Previous English: (Rudin's inequality.) $G$ carries the discrete measurable structure. Let $p \ge 2$ and let $f : G \to \mathbb{C}$ be such that the support of its Fourier transform $\mathrm{cft}(f)$ is dissociated. Then $\|f\|_p \le 4\, e^{1/2} \sqrt{p}\, \|f\|_2$, with norms in the compact (expectation) normalisation.
Checker's issue: The English omits the [Fintype G] hypothesis that G is finite.
