You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. Compare the
English with the full statement; anything the English attributes to the docstring must actually be in it.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Definitions are held to the same standard: the English must name the setting the signature assumes
("for an abelian group $G$ and …, $\mathrm{rdist}$ is …"). Replacing an assumption by a stronger one (a metric
space where the Lean has a pseudometric space) is unfaithful too, and so is leaving a restrictive type unstated
(a natural number, a nonnegative real). Citations (theorem or lemma numbers) and remarks are claims too: each must
be supported by the docstring or the Lean. So is a formula or description of what a defined object is: when the
prompt shows neither its definition nor a docstring saying it, the English must not supply one. Every variable
needs its type ("$f : G \to \mathbb{C}$", "$m$ a natural number"), every symbol must be introduced (notation such
as $M_{\mathcal B}$ included), and no letter may mean two things. When in doubt, flag it: a false alarm costs one
repair, a missed error stays in the outline. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `discrete_carleson`
Lean (short): `(X : Type u_1) [ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] : ∃ G', MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → ∫⁻ (x : X) in G \ G', ‖carlesonSum Set.univ f x‖ₑ ≤ ↑(C2_0_2 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ (X : Type u_1) {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)], ∃ (G' : Set X), MeasurableSet G' ∧ HMul.hMul (β := ENNReal) (2 : ENNReal) ((volume : Measure X) G' : ENNReal) ≤ (volume : Measure X) G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → ∫⁻ (x : X) in G \ G', ‖carlesonSum (F := F) (G := G) Set.univ f x‖ₑ ≤ ↑(C2_0_2 a (nnq X (F := F) (G := G))) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) ((1 : ℝ) - q⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) q⁻¹`
English: Let $X$ be a metric space, let $a$ be a natural number, $q$ a real number, $K : X \times X \to \mathbb{C}$ a kernel, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ functions and $F, G \subseteq X$ sets, such that $(a, q, K, \sigma_1, \sigma_2, F, G)$ satisfy the standing assumptions `ProofData` of the Carleson project, and suppose $X$ carries a tile structure (`TileStructure`) with respect to $Q$ and the default parameters $D = $ `defaultD a`, $\kappa = $ `defaultκ a`, $S = $ `defaultS X` and cancellation point `cancelPt X`. Then there exists a measurable set $G' \subseteq X$ with $2\,\mu(G') \le \mu(G)$ such that for every measurable $f : X \to \mathbb{C}$ with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$, $$\int_{G\setminus G'} \Big\|\sum_{p \in \mathfrak{P}} T_p f(x)\Big\|\,d\mu(x) \le C_{2.0.2}(a, \mathrm{nnq})\, \mu(G)^{1-q^{-1}}\, \mu(F)^{q^{-1}},$$ where $\mu$ is the volume measure on $X$, the sum is the Carleson sum `carlesonSum` over all tiles, the norm on the left is the extended nonnegative norm, $\mathrm{nnq}$ is `nnq X` (the exponent $q$ as a nonnegative real, used only in the constant), and $C_{2.0.2}$ is the constant `C2_0_2`; the powers are taken in the extended nonnegative reals with the real exponent $q$.
