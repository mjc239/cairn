You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `tau_strictly_decreases`
Lean: `[IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [Module (ZMod 2) G] [Finite G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (h_min : TauMinimizes p X₁ X₂) (hpη : p.η = 1 / 9) : d[X₁ # X₂] = 0`
English: Let $G$ be a finite elementary abelian 2-group (i.e. a finite vector space over $\mathbb{F}_2$) with measurable singletons, and suppose the measures on $\Omega_{01}$, $\Omega_{02}$ and $\Omega$ are probability measures. Let $p$ be a reference package with parameter $\eta$, and let $X_1, X_2 : \Omega \to G$ be measurable random variables such that $(X_1,X_2)$ minimizes $\tau$ for $p$. If $\eta = 1/9$, then $d[X_1;X_2] = 0$. (This is the contrapositive of: if $d[X_1;X_2] > 0$ then there are $G$-valued $X_1', X_2'$ with $\tau[X_1';X_2'] < \tau[X_1;X_2]$.)

### `entropic_PFR_conjecture`
Lean: `[IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [Module (ZMod 2) G] [Finite G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) (hpη : p.η = 1 / 9) : ∃ H Ω mΩ U, IsProbabilityMeasure volume ∧ Measurable U ∧ IsUniform (↑H) U volume ∧ d[p.X₀₁ # U] + d[p.X₀₂ # U] ≤ 11 * d[p.X₀₁ # p.X₀₂]`
English: Let $G$ be a finite elementary abelian 2-group (i.e. a finite vector space over $\mathbb{F}_2$) with measurable singletons, and suppose the measures on $\Omega_{01}$ and $\Omega_{02}$ are probability measures. Let $p$ be a reference package with reference random variables $X^0_1, X^0_2$ (valued in $G$) and parameter $\eta = 1/9$. Then there exist a subgroup $H \le G$, a probability space $\Omega$ and a measurable random variable $U : \Omega \to G$ uniformly distributed on $H$ such that $$d[X^0_1;U] + d[X^0_2;U] \le 11\, d[X^0_1;X^0_2].$$
