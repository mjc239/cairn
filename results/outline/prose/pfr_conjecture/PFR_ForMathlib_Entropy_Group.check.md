You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.entropy_add_right`
Lean: `[Countable G] [MeasurableSingletonClass G] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨X, X + Y⟩; μ] = H[⟨X, Y⟩; μ]`
English: Let $X, Y$ be measurable random variables with values in an additive group, and $\mu$ a measure. Then $H[(X, X+Y)] = H[(X, Y)]$ (entropies with respect to $\mu$).

### `ProbabilityTheory.entropy_add_left`
Lean: `[Countable G] [MeasurableSingletonClass G] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨Y + X, Y⟩; μ] = H[⟨X, Y⟩; μ]`
English: Let $X, Y$ be measurable random variables with values in an additive group, and $\mu$ a measure. Then $H[(Y+X, Y)] = H[(X, Y)]$ (entropies with respect to $\mu$).

### `ProbabilityTheory.entropy_sub_mutualInfo_le_entropy_sub`
Lean: `[Countable G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] (hX : Measurable X) (hY : Measurable Y) : H[X; μ] - I[X : Y ; μ] ≤ H[X - Y; μ]`
English: Let $X, Y$ be measurable random variables with values in an additive group. Then $H[X] - I[X:Y] \le H[X - Y]$ (with respect to $\mu$).
