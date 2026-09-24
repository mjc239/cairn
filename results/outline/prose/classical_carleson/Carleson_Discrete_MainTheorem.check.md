You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `discrete_carleson`
Lean: `(X : Type u_1) [ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] : ∃ G', MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → ∫⁻ (x : X) in G \ G', ‖carlesonSum Set.univ f x‖ₑ ≤ ↑(C2_0_2 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
English: In the given setting on $X$ (with the sets $F$, $G$ and exponent $q$ = `nnq X`), there exists a measurable set $G' \subseteq X$ with $2\mu(G') \le \mu(G)$ such that for every measurable $f : X \to \mathbb{C}$ with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$, $$\int_{G\setminus G'} \Big\|\sum_{p \in \mathfrak{P}} T_p f(x)\Big\|\,dx \le C_{2.0.2}(a,q)\, \mu(G)^{1-1/q}\, \mu(F)^{1/q},$$ where the sum is the Carleson sum over all tiles and $C_{2.0.2}$ is the constant `C2_0_2`.
