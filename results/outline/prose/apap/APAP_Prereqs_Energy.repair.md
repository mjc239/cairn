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

### `cLpNorm_dft_indicator_one_pow`
Lean: `[Fintype G] [DiscreteMeasurableSpace G] (n : ℕ) (s : Finset G) : ‖dft ((↑s).indicator fun x => 1)‖ₙ_[↑(2 * n)] ^ (2 * n) = boringEnergy n s`
Previous English: $G$ carries the discrete measurable structure. For every $n \in \mathbb{N}$ and finite $s \subseteq G$, $\|\widehat{1_s}\|_{2n}^{2n} = \mathrm{boringEnergy}_n(s)$, where $\widehat{1_s}$ is the discrete Fourier transform of the indicator of $s$ and the norm is taken with the compact (expectation) normalisation.
Checker's issue: The English omits the [Fintype G] hypothesis that G is finite.

### `cL2Norm_dft_indicator_one`
Lean: `[Fintype G] [DiscreteMeasurableSpace G] (s : Finset G) : ‖dft ((↑s).indicator fun x => 1)‖ₙ_[2] = √↑s.card`
Previous English: $G$ carries the discrete measurable structure. For every finite $s \subseteq G$, $\|\widehat{1_s}\|_2 = \sqrt{|s|}$, with the compact normalisation on the norm.
Checker's issue: The English omits the [Fintype G] hypothesis that G is finite.
