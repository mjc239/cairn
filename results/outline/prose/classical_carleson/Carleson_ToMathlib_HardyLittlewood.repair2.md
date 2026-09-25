You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one. For a definition, name the setting its signature assumes. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): MeasureTheory, TileStructure, Antichain.

### `hasStrongType_maximalFunction`
Lean (short): `[μ.IsDoubling A] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] (hp₁ : 0 < p₁) (hp₁₂ : p₁ < p₂) : HasStrongType (maximalFunction μ 𝓑 c r ↑p₁) (↑p₂) (↑p₂) μ μ ↑(C2_0_6 A p₁ p₂)`
Lean (full): `∀ {X : Type u_1} {ε' : Type u_3} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : MeasurableSpace X] {μ : Measure X} [μ.IsDoubling A] {ι : Type u_4} {𝓑 : Set ι} {c : ι → X} {r : ι → ℝ} [inst_3 : TopologicalSpace ε'] [inst_4 : ContinuousENorm ε'] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] {p₁ p₂ : NNReal}, 0 < p₁ → p₁ < p₂ → HasStrongType (maximalFunction μ 𝓑 c r ↑p₁) (↑p₂) (↑p₂) μ μ ↑(C2_0_6 A p₁ p₂)`
Docstring: The `maximalFunction` has strong type when `p₁ < p₂`.
Previous English: Let $X$ be a proper metric space with its Borel $\sigma$-algebra, and let $\mu$ be a doubling measure on $X$ with doubling constant $A$ which is finite on compact sets and positive on nonempty open sets. If $0 < p_1 < p_2$, then the maximal function $\mathrm{maximalFunction}(\mu, \mathcal{B}, c, r, p_1)$ has strong type $(p_2, p_2)$ with respect to $\mu$ and $\mu$, with constant $C_{2.0.6}(A, p_1, p_2)$.
Checker's issue: Says 'metric space' but the Lean only assumes X is a pseudometric space, so the English strengthens the hypothesis.

### `hasStrongType_maximalFunction_one`
Lean (short): `[μ.IsDoubling A] [SMul NNReal ε'] [ENormSMulClass NNReal ε'] [TopologicalSpace.PseudoMetrizableSpace ε'] [BorelSpace ε'] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] (hp : 1 < p) : HasStrongType (maximalFunction μ 𝓑 c r 1) (↑p) (↑p) μ μ ↑(CMB A p)`
Lean (full): `∀ {X : Type u_1} {ε' : Type u_3} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : MeasurableSpace X] {μ : Measure X} [μ.IsDoubling A] {ι : Type u_4} {𝓑 : Set ι} {c : ι → X} {r : ι → ℝ} [inst_3 : TopologicalSpace ε'] [inst_4 : ESeminormedAddMonoid ε'] [inst_5 : SMul NNReal ε'] [ENormSMulClass NNReal ε'] [TopologicalSpace.PseudoMetrizableSpace ε'] [inst_8 : MeasurableSpace ε'] [BorelSpace ε'] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] {p : NNReal}, 1 < p → HasStrongType (maximalFunction μ 𝓑 c r 1) (↑p) (↑p) μ μ ↑(CMB A p)`
Docstring: Special case of equation (2.0.44). The proof is given between (9.0.12) and (9.0.34). Use the real interpolation theorem instead of following the blueprint.
Previous English: Let $X$ be a proper metric space with its Borel $\sigma$-algebra, and let $\mu$ be a doubling measure on $X$ with doubling constant $A$ which is finite on compact sets and positive on nonempty open sets. Let the target space $\varepsilon'$ be pseudo-metrizable with its Borel $\sigma$-algebra and carry a scalar action of $\mathbb{R}_{\ge 0}$ compatible with the extended norm ($\|c\cdot x\|_e = c\,\|x\|_e$). If $p > 1$, then the maximal function $\mathrm{maximalFunction}(\mu, \mathcal{B}, c, r, 1)$ has strong type $(p, p)$ with respect to $\mu$ and $\mu$, with constant $C_{MB}(A, p)$ (a special case of (2.0.44)).
Checker's issue: Says 'metric space' where the Lean only assumes a pseudometric space, and omits that the target space is an extended-seminormed additive monoid (ESeminormedAddMonoid).
