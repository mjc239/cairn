You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `diff_rdist_le_3`
Lean: `[Finite G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) [IsProbabilityMeasure volume] (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂' : Measurable X₂') (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₂', X₁'] volume) [Module (ZMod 2) G] [IsProbabilityMeasure volume] : d[p.X₀₁ # X₁ | X₁ + X₂'] - d[p.X₀₁ # X₁] ≤ d[X₁ # X₂] / 2 + H[X₁] / 4 - H[X₂] / 4`
English: Let $p$ be a reference package with reference variables $X^0_1, X^0_2$ and parameter $\eta$, and let $X_1, X_2, \tilde X_1, \tilde X_2 : \Omega \to G$ be random variables with $X_1$ and $\tilde X_2$ measurable, $\tilde X_2$ distributed as $X_2$, and $X_1, X_2, \tilde X_2, \tilde X_1$ jointly independent. Then $$d[X^0_1; X_1 \mid X_1 + \tilde X_2] - d[X^0_1;X_1] \le \tfrac12 d[X_1;X_2] + \tfrac14 H[X_1] - \tfrac14 H[X_2].$$

### `diff_rdist_le_4`
Lean: `[Finite G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) [IsProbabilityMeasure volume] (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (h₁ : IdentDistrib X₁ X₁' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₂', X₁'] volume) [Module (ZMod 2) G] [IsProbabilityMeasure volume] : d[p.X₀₂ # X₂ | X₂ + X₁'] - d[p.X₀₂ # X₂] ≤ d[X₁ # X₂] / 2 + H[X₂] / 4 - H[X₁] / 4`
English: Let $p$ be a reference package with reference variables $X^0_1, X^0_2$ and parameter $\eta$, and let $X_1, X_2, \tilde X_1, \tilde X_2 : \Omega \to G$ be random variables with $X_2$ and $\tilde X_1$ measurable, $\tilde X_1$ distributed as $X_1$, and $X_1, X_2, \tilde X_2, \tilde X_1$ jointly independent. Then $$d[X^0_2; X_2 \mid X_2 + \tilde X_1] - d[X^0_2;X_2] \le \tfrac12 d[X_1;X_2] + \tfrac14 H[X_2] - \tfrac14 H[X_1].$$

### `rdist_add_rdist_add_condMutual_eq`
Lean: `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₂', X₁'] volume) [Module (ZMod 2) G] : d[X₁ + X₂' # X₂ + X₁'] + d[X₁ | X₁ + X₂' # X₂ | X₂ + X₁'] + I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂'] = 2 * d[X₁ # X₂]`
English: Let $X_1, X_2, \tilde X_1, \tilde X_2 : \Omega \to G$ be measurable random variables with $\tilde X_1$ distributed as $X_1$, $\tilde X_2$ distributed as $X_2$, and $X_1, X_2, \tilde X_2, \tilde X_1$ jointly independent. Then $$d[X_1+\tilde X_2;\ X_2+\tilde X_1] + d[X_1\mid X_1+\tilde X_2;\ X_2 \mid X_2+\tilde X_1] + I[X_1+X_2 : \tilde X_1 + X_2 \mid X_1+X_2+\tilde X_1+\tilde X_2] = 2\,d[X_1;X_2].$$

### `rdist_of_sums_ge`
Lean: `[Finite G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) [IsProbabilityMeasure volume] (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h_min : TauMinimizes p X₁ X₂) : d[X₁ + X₂' # X₂ + X₁'] ≥ d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁ + X₂'] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂ + X₁'] - d[p.X₀₂ # X₂])`
English: Let $p$ be a reference package with reference variables $X^0_1, X^0_2$ and parameter $\eta$, let $X_1, X_2, \tilde X_1, \tilde X_2 : \Omega \to G$ be measurable, and suppose $(X_1,X_2)$ minimizes $\tau$ for $p$. Then $$d[X_1+\tilde X_2;\ X_2+\tilde X_1] \ge d[X_1;X_2] - \eta\big(d[X^0_1; X_1+\tilde X_2] - d[X^0_1;X_1]\big) - \eta\big(d[X^0_2;X_2+\tilde X_1] - d[X^0_2;X_2]\big).$$

### `first_estimate`
Lean: `[Finite G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) [IsProbabilityMeasure volume] (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₂', X₁'] volume) (h_min : TauMinimizes p X₁ X₂) [Module (ZMod 2) G] [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] : I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂'] ≤ 2 * p.η * d[X₁ # X₂]`
English: Let $p$ be a reference package with reference variables $X^0_1, X^0_2$ and parameter $\eta$, let $X_1, X_2, \tilde X_1, \tilde X_2 : \Omega \to G$ be measurable random variables with $\tilde X_1$ distributed as $X_1$ and $\tilde X_2$ distributed as $X_2$, such that $X_1, X_2, \tilde X_2, \tilde X_1$ are jointly independent, and suppose $(X_1,X_2)$ minimizes $\tau$ for $p$. Write $k := d[X_1;X_2]$ and $I_1 := I[X_1+X_2 : \tilde X_1 + X_2 \mid X_1+X_2+\tilde X_1+\tilde X_2]$. Then $I_1 \le 2\eta k$.

### `ent_ofsum_le`
Lean: `[Finite G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) [IsProbabilityMeasure volume] (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₂', X₁'] volume) (h_min : TauMinimizes p X₁ X₂) [Module (ZMod 2) G] [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] : H[X₁ + X₂ + X₁' + X₂'] ≤ H[X₁] / 2 + H[X₂] / 2 + (2 + p.η) * d[X₁ # X₂] - I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂']`
English: Let $p$ be a reference package with reference variables $X^0_1, X^0_2$ and parameter $\eta$, let $X_1, X_2, \tilde X_1, \tilde X_2 : \Omega \to G$ be measurable random variables with $\tilde X_1$ distributed as $X_1$ and $\tilde X_2$ distributed as $X_2$, such that $X_1, X_2, \tilde X_2, \tilde X_1$ are jointly independent, and suppose $(X_1,X_2)$ minimizes $\tau$ for $p$. Write $k := d[X_1;X_2]$ and $I_1 := I[X_1+X_2 : \tilde X_1 + X_2 \mid X_1+X_2+\tilde X_1+\tilde X_2]$. Then $$H[X_1+X_2+\tilde X_1+\tilde X_2] \le \tfrac12 H[X_1] + \tfrac12 H[X_2] + (2+\eta)k - I_1.$$
