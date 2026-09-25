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

### `discrete_carleson`
Lean (short): `(X : Type u_1) [ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] : ∃ G', MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → ∫⁻ (x : X) in G \ G', ‖carlesonSum Set.univ f x‖ₑ ≤ ↑(C2_0_2 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ (X : Type u_1) {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)], ∃ G', MeasurableSet G' ∧ (2 : ENNReal) * volume G' ≤ volume G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → ∫⁻ (x : X) in G \ G', ‖carlesonSum Set.univ f x‖ₑ ≤ ↑(C2_0_2 a (nnq X)) * volume G ^ ((1 : ℝ) - q⁻¹) * volume F ^ q⁻¹`
English: In the given setting on $X$ (with the sets $F$, $G$ and exponent $q$ = `nnq X`), there exists a measurable set $G' \subseteq X$ with $2\mu(G') \le \mu(G)$ such that for every measurable $f : X \to \mathbb{C}$ with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$, $$\int_{G\setminus G'} \Big\|\sum_{p \in \mathfrak{P}} T_p f(x)\Big\|\,dx \le C_{2.0.2}(a,q)\, \mu(G)^{1-1/q}\, \mu(F)^{1/q},$$ where the sum is the Carleson sum over all tiles and $C_{2.0.2}$ is the constant `C2_0_2`.
