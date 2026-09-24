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

### `chang`
Lean: `[DiscreteMeasurableSpace G] (hf : f ≠ 0) (hη : 0 < η) : ∃ Δ ⊆ largeSpec f η, Δ.card ≤ ⌈changConst * Real.exp 1 * ↑⌈1 + Real.log (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2 / ↑(Fintype.card G))⁻¹⌉₊ / η ^ 2⌉₊ ∧ largeSpec f η ⊆ Δ.addSpan`
Docstring: **Chang's lemma**.
Previous English: (Chang's lemma.) $G$ carries the discrete measurable structure. If $f \ne 0$ and $\eta > 0$, then there is $\Delta \subseteq \operatorname{largeSpec}(f, \eta)$ with $|\Delta| \le \left\lceil \mathrm{changConst}\cdot e \cdot \left\lceil 1 + \log\left(\frac{\|f\|_1^2/\|f\|_2^2}{|G|}\right)^{-1}\right\rceil / \eta^2 \right\rceil$ (natural-number ceilings) such that $\operatorname{largeSpec}(f, \eta)$ is contained in the additive span of $\Delta$.
Checker's issue: Lean has `Real.log (X)⁻¹`, i.e. log of the inverse, but the English writes `\log\left(X\right)^{-1}`, which reads as the reciprocal of the logarithm.
