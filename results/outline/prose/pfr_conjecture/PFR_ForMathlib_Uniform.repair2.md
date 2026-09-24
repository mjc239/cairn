You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Keep every
hypothesis the Lean shows, including instance assumptions such as `[Finite G]` or `[IsProbabilityMeasure μ]`
(say them in words: "$G$ is finite", "$\mu$ is a probability measure"), and the exact conclusion. Do not add
claims the Lean does not make. Purely structural instances (e.g. `[AddCommGroup G]`) and implicit arguments are not
shown and may stay implicit.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

### `ProbabilityTheory.IsUniform`
Lean: `(H : Set S) (X : Ω → S) (μ : autoParam (Measure Ω) IsUniform._auto_1) : Prop`
Docstring: The assertion that the law of $X$ is the uniform probability measure on a finite set $H$. While in applications $H$ will be non-empty finite set, $X$ measurable, and and $μ$ a probability measure, it could be technically convenient to have a definition that works even without these hypotheses. (For instance, `isUniform` would be well-defined, but false, for infinite `H`). This should probably be …
Previous English: For a set $H\subseteq S$, a random variable $X:\Omega\to S$ and a measure $\mu$ on $\Omega$ (by default the ambient measure), defines the predicate $\mathrm{IsUniform}(H,X,\mu)$ asserting that the law of $X$ under $\mu$ is the uniform probability measure on the finite set $H$. The predicate makes sense without assuming $H$ nonempty and finite, $X$ measurable or $\mu$ a probability measure (e.g. it is well-defined but false for infinite $H$).
Checker's issue: The English says the law of X is the uniform probability measure on H and that the predicate is false for infinite H, but the signature supports neither claim, and with no probability or nonzero-measure assumption they are doubtful.

### `ProbabilityTheory.exists_isUniform_measureSpace`
Lean: `[MeasurableSingletonClass S] (H : Finset S) (h : H.Nonempty) : ∃ Ω mΩ U, IsProbabilityMeasure volume ∧ Measurable U ∧ IsUniform (↑H) U volume ∧ (∀ (ω : Ω), U ω ∈ H) ∧ FiniteRange U`
Docstring: Uniform distributions exist, version giving a measure space
Previous English: Let $H$ be a nonempty finite subset of $S$. Then there exist a type $\Omega$ with a measurable-space structure and a random variable $U:\Omega\to S$ such that the ambient measure on $\Omega$ is a probability measure, $U$ is measurable, $U$ is uniformly distributed on $H$, $U(\omega)\in H$ for every $\omega\in\Omega$, and $U$ has finite range.
Checker's issue: The English drops the hypothesis that S has measurable singletons.
