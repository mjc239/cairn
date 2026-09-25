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
naturally. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `Grid.dist_strictMono`
Lean (short): `[GridStructure X (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hpq : I < J) : dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
Lean (full): `∀ {X : Type u_1} [inst : PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : GridStructure X (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {I J : Grid X}, I < J → ∀ {f g : Θ X}, dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
English: (Stronger version of Lemma 2.1.2) If $I<J$ are dyadic cubes, then for all $f,g$ $$d_{c(I),\,D^{s(I)}/4}(f,g)\le C_{2.1.2}(a)\,d_{c(J),\,D^{s(J)}/4}(f,g),$$ where $D=D(a)$ is the default doubling parameter and $d_{x,r}$ denotes the distance between functions on the ball $B(x,r)$.

### `Grid.succ`
Lean (short): `[GridStructure X (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (i : Grid X) : Grid X`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : GridStructure X (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → Grid X → Grid X`
English: For a dyadic cube $i\in\mathrm{Grid}(X)$, defines $\mathrm{succ}(i)$: if $i$ is not maximal, the unique minimal cube strictly greater than $i$ (its parent). This is not a successor order, since a cube can be the successor of several cubes.
