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

### `sub_mem_symmGroup`
Lean: `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X) (hdist : d[X # X] = 0) (hx : volume (X ⁻¹' {x}) ≠ 0) (hy : volume (X ⁻¹' {y}) ≠ 0) : x - y ∈ symmGroup X hX`
Docstring: If $d[X ;X]=0$, and $x,y \in G$ are such that $P[X=x], P[X=y]>0$, then $x-y \in \mathrm{Sym}[X]$.
Previous English: Let $X$ be a measurable $G$-valued random variable with $d[X;X]=0$, and let $x,y\in G$ satisfy $P[X=x]\neq 0$ and $P[X=y]\neq 0$. Then $x-y\in\mathrm{Sym}[X]$.
Checker's issue: The English drops the hypotheses [Finite G] and that volume is a probability measure.

### `isUniform_sub_const_of_rdist_eq_zero`
Lean: `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X) (hdist : d[X # X] = 0) (hx₀ : volume (X ⁻¹' {x₀}) ≠ 0) : IsUniform (↑(symmGroup X hX)) (fun ω => X ω - x₀) volume`
Docstring: If `d[X # X] = 0`, then `X - x₀` is the uniform distribution on the subgroup of `G` stabilizing the distribution of `X`, for any `x₀` of positive probability.
Previous English: Let $X$ be a measurable $G$-valued random variable with $d[X;X]=0$, and let $x_0\in G$ satisfy $P[X=x_0]\neq 0$. Then $X-x_0$ is uniformly distributed on the subgroup $\mathrm{Sym}[X]$.
Checker's issue: The English drops the hypotheses [Finite G] and that volume is a probability measure.

### `exists_isUniform_of_rdist_self_eq_zero`
Lean: `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X) (hdist : d[X # X] = 0) : ∃ H U, Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = 0`
Docstring: If $d[X ;X]=0$, then there exists a subgroup $H \leq G$ such that $d[X ;U_H] = 0$.
Previous English: Let $X$ be a measurable $G$-valued random variable with $d[X;X]=0$. Then there exist a subgroup $H\le G$ and a measurable random variable $U$, uniformly distributed on $H$, such that $d[X;U]=0$.
Checker's issue: The English drops the hypotheses [Finite G] and that volume is a probability measure.

### `exists_isUniform_of_rdist_eq_zero`
Lean: `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] (hX : Measurable X) (hX' : Measurable X') (hdist : d[X # X'] = 0) : ∃ H U, Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = 0 ∧ d[X' # U] = 0`
Docstring: If $d[X_1;X_2]=0$, then there exists a subgroup $H \leq G$ such that $d[X_1;U_H] = d[X_2;U_H] = 0$. Follows from the preceding claim by the triangle inequality.
Previous English: Let $X$ and $X'$ be measurable $G$-valued random variables with $d[X;X']=0$. Then there exist a subgroup $H\le G$ and a measurable random variable $U$, uniformly distributed on $H$, such that $d[X;U]=0$ and $d[X';U]=0$.
Checker's issue: The English drops the hypotheses [Finite G] and that the measures are probability measures.
