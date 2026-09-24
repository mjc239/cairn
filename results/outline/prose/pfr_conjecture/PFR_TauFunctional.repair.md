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

### `condRuzsaDistance_ge_of_min`
Lean: `[Finite G] (p : refPackage Ω₀₁ Ω₀₂ G) [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [MeasurableSingletonClass G] [Finite S] [MeasurableSingletonClass S] [Finite T] [MeasurableSingletonClass T] (h : TauMinimizes p X₁ X₂) (h1 : Measurable X₁') (h2 : Measurable X₂') (Z : Ω'₁ → S) (W : Ω'₂ → T) (hZ : Measurable Z) (hW : Measurable W) : d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁' | Z] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂' | W] - d[p.X₀₂ # X₂]) ≤ d[X₁' | Z # X₂' | W]`
Docstring: For any $G$-valued random variables $X'_1,X'_2$ and random variables $Z,W$, one can lower bound $d[X'_1|Z;X'_2|W]$ by $$k - \eta (d[X^0_1;X'_1|Z] - d[X^0_1;X_1] ) - \eta (d[X^0_2;X'_2|W] - d[X^0_2;X_2] ).$$
Previous English: Let $p$ be a reference package with parameter $\eta$, let $(X_1,X_2)$ minimize $\tau$ for $p$, let $X_1',X_2'$ be measurable $G$-valued random variables, and let $Z:\Omega_1'\to S$ and $W:\Omega_2'\to T$ be measurable random variables. Then $$d[X_1;X_2]-\eta\left(d[X^0_1;X_1'\mid Z]-d[X^0_1;X_1]\right)-\eta\left(d[X^0_2;X_2'\mid W]-d[X^0_2;X_2]\right)\le d[X_1'\mid Z;X_2'\mid W].$$
Checker's issue: The English drops the hypotheses [Finite G], [Finite S] and [Finite T] (with their measurable-singleton instances), stating the result for arbitrary codomains.

### `tau_minimizer_exists`
Lean: `[IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [Finite G] (p : refPackage Ω₀₁ Ω₀₂ G) [MeasurableSingletonClass G] : ∃ Ω x X₁ X₂, Measurable X₁ ∧ Measurable X₂ ∧ IsProbabilityMeasure volume ∧ TauMinimizes p X₁ X₂`
Docstring: A pair of random variables minimizing $τ$ exists.
Previous English: For every reference package $p$ there exist a measurable space $\Omega$ with a probability measure and measurable random variables $X_1,X_2:\Omega\to G$ such that $(X_1,X_2)$ minimizes $\tau$ for $p$.
Checker's issue: The English drops the hypothesis [Finite G] (and MeasurableSingletonClass G), claiming existence of a minimizer for every reference package without finiteness of G.
