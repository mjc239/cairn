You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption) and the English. Compare the English with the full statement.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Definitions are held to the same standard: the English must name the setting the signature assumes
("for an abelian group $G$ and …, $\mathrm{rdist}$ is …"). Replacing an assumption by a stronger one (a metric
space where the Lean has a pseudometric space) is unfaithful too. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `hasStrongType_maximalFunction`
Lean (short): `[μ.IsDoubling A] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] (hp₁ : 0 < p₁) (hp₁₂ : p₁ < p₂) : HasStrongType (maximalFunction μ 𝓑 c r ↑p₁) (↑p₂) (↑p₂) μ μ ↑(C2_0_6 A p₁ p₂)`
Lean (full): `∀ {X : Type u_1} {ε' : Type u_3} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : MeasurableSpace X] {μ : Measure X} [μ.IsDoubling A] {ι : Type u_4} {𝓑 : Set ι} {c : ι → X} {r : ι → ℝ} [inst_3 : TopologicalSpace ε'] [inst_4 : ContinuousENorm ε'] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] {p₁ p₂ : NNReal}, (0 : NNReal) < p₁ → p₁ < p₂ → HasStrongType (maximalFunction μ 𝓑 c r ↑p₁) (↑p₂) (↑p₂) μ μ ↑(C2_0_6 A p₁ p₂)`
English: Let $X$ be a proper pseudometric space with its Borel $\sigma$-algebra, and let $\mu$ be a measure on $X$ that is doubling with constant $A \ge 0$, finite on compact sets, and positive on nonempty open sets. Let $\mathcal{B}$ be a set of indices $i \in \iota$ with centers $c : \iota \to X$ and radii $r : \iota \to \mathbb{R}$. Let $\varepsilon'$ be a topological space with a continuous extended norm $\|\cdot\|_e$. If $p_1, p_2 \in \mathbb{R}_{\ge 0}$ satisfy $0 < p_1 < p_2$, then the maximal function $\mathrm{maximalFunction}(\mu, \mathcal{B}, c, r, p_1)$ (acting on $\varepsilon'$-valued functions) has strong type $(p_2, p_2)$ with respect to $\mu$ and $\mu$, with constant $C_{2.0.6}(A, p_1, p_2)$.

### `hasStrongType_maximalFunction_one`
Lean (short): `[μ.IsDoubling A] [SMul NNReal ε'] [ENormSMulClass NNReal ε'] [TopologicalSpace.PseudoMetrizableSpace ε'] [BorelSpace ε'] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] (hp : 1 < p) : HasStrongType (maximalFunction μ 𝓑 c r 1) (↑p) (↑p) μ μ ↑(CMB A p)`
Lean (full): `∀ {X : Type u_1} {ε' : Type u_3} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : MeasurableSpace X] {μ : Measure X} [μ.IsDoubling A] {ι : Type u_4} {𝓑 : Set ι} {c : ι → X} {r : ι → ℝ} [inst_3 : TopologicalSpace ε'] [inst_4 : ESeminormedAddMonoid ε'] [inst_5 : SMul NNReal ε'] [ENormSMulClass NNReal ε'] [TopologicalSpace.PseudoMetrizableSpace ε'] [inst_8 : MeasurableSpace ε'] [BorelSpace ε'] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] {p : NNReal}, (1 : NNReal) < p → HasStrongType (maximalFunction μ 𝓑 c r (1 : ℝ)) (↑p) (↑p) μ μ ↑(CMB A p)`
English: Let $X$ be a proper pseudometric space with its Borel $\sigma$-algebra, and let $\mu$ be a measure on $X$ that is doubling with constant $A \ge 0$, finite on compact sets, and positive on nonempty open sets. Let $\mathcal{B}$ be a set of indices $i \in \iota$ with centers $c : \iota \to X$ and radii $r : \iota \to \mathbb{R}$. Let the target space $\varepsilon'$ be an extended-seminormed additive monoid (with its topology), which is pseudo-metrizable, carries its Borel $\sigma$-algebra, and has a scalar action of $\mathbb{R}_{\ge 0}$ compatible with the extended norm ($\|c\cdot x\|_e = c\,\|x\|_e$). If $p \in \mathbb{R}_{\ge 0}$ satisfies $p > 1$, then the maximal function $\mathrm{maximalFunction}(\mu, \mathcal{B}, c, r, 1)$ (acting on $\varepsilon'$-valued functions) has strong type $(p, p)$ with respect to $\mu$ and $\mu$, with constant $C_{MB}(A, p)$ (a special case of (2.0.44)).
