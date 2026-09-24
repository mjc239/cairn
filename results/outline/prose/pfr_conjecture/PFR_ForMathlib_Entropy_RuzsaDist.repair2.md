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

### `condRuzsaDist`
Lean: `[Countable G] [MeasurableSingletonClass G] (X : Ω → G) (Z : Ω → S) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist._auto_1) [IsFiniteMeasure μ] (μ' : autoParam (Measure Ω') condRuzsaDist._auto_3) [IsFiniteMeasure μ'] : ℝ`
Docstring: The conditional Ruzsa distance `d[X|Z ; Y|W]`.
Previous English: For random variables $X:\Omega\to G$, $Z:\Omega\to S$ on $(\Omega,\mu)$ and $Y:\Omega'\to G$, $W:\Omega'\to T$ on $(\Omega',\mu')$, with $G$ an abelian group, the conditional Ruzsa distance $d[X|Z \,;\, Y|W]$ (with respect to $\mu,\mu'$) is the kernel Ruzsa distance between the conditional distribution of $X$ given $Z$ and that of $Y$ given $W$, averaged against the laws of $Z$ and $W$.
Checker's issue: The English drops the hypotheses that G is countable with measurable singletons and that mu and mu' are finite measures.

### `condRuzsaDist'`
Lean: `[Countable G] [MeasurableSingletonClass G] (X : Ω → G) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist'._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist'._auto_3) [IsFiniteMeasure μ'] : ℝ`
Docstring: The conditional Ruzsa distance `d[X ; Y|W]`.
Previous English: For $X:\Omega\to G$ on $(\Omega,\mu)$ and $Y:\Omega'\to G$, $W:\Omega'\to T$ on $(\Omega',\mu')$, the conditional Ruzsa distance $d[X \,;\, Y|W]$ (with respect to $\mu,\mu'$) is the kernel Ruzsa distance between the (constant) law of $X$ and the conditional distribution of $Y$ given $W$, averaged against the law of $W$.
Checker's issue: The English drops the hypotheses that G is countable with measurable singletons and that mu' is a finite measure.
