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

### `ProbabilityTheory.prob_ge_exp_neg_entropy`
Lean: `[MeasurableSingletonClass S] [Nonempty S] (X : Ω → S) (μ : Measure Ω) (hX : Measurable X) [FiniteRange X] : ∃ s, μ Set.univ * ↑(Real.exp (-H[X; μ])).toNNReal ≤ (Measure.map X μ) {s}`
Docstring: If `X` is an `S`-valued random variable, then there exists `s ∈ S` such that `P[X = s] ≥ \exp(- H[X])`.
Previous English: Let $X : \Omega \to S$ be a measurable random variable and $\mu$ a measure on $\Omega$. Then there exists $s \in S$ such that $\mu(\Omega)\cdot e^{-H[X;\mu]} \le X_*\mu(\{s\})$; in particular (for a probability measure) $\mathbb{P}[X = s] \ge e^{-H[X]}$.
Checker's issue: The English drops the hypotheses that S has measurable singletons, S is nonempty, and X has finite range.

### `ProbabilityTheory.mutualInfo_nonneg`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) [FiniteRange X] [FiniteRange Y] : 0 ≤ I[X : Y ; μ]`
Docstring: Mutual information is non-negative.
Previous English: Let $X, Y$ be measurable random variables and $\mu$ a measure. Then $0 \le I[X : Y;\mu]$.
Checker's issue: The English drops the hypotheses that S and T have measurable singletons and that X and Y have finite range.
