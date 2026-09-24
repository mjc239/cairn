You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `hasStrongType_maximalFunction`
Lean: `[μ.IsDoubling A] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] (hp₁ : 0 < p₁) (hp₁₂ : p₁ < p₂) : HasStrongType (maximalFunction μ 𝓑 c r ↑p₁) (↑p₂) (↑p₂) μ μ ↑(C2_0_6 A p₁ p₂)`
English: If $0 < p_1 < p_2$, then the maximal function $\mathrm{maximalFunction}(\mu, \mathcal{B}, c, r, p_1)$ has strong type $(p_2, p_2)$ with respect to $\mu$ and $\mu$, with constant $C_{2.0.6}(A, p_1, p_2)$.

### `hasStrongType_maximalFunction_one`
Lean: `[μ.IsDoubling A] [SMul NNReal ε'] [ENormSMulClass NNReal ε'] [TopologicalSpace.PseudoMetrizableSpace ε'] [BorelSpace ε'] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] (hp : 1 < p) : HasStrongType (maximalFunction μ 𝓑 c r 1) (↑p) (↑p) μ μ ↑(CMB A p)`
English: If $p > 1$, then the maximal function $\mathrm{maximalFunction}(\mu, \mathcal{B}, c, r, 1)$ has strong type $(p, p)$ with respect to $\mu$ and $\mu$, with constant $C_{MB}(A, p)$ (a special case of (2.0.44)).
