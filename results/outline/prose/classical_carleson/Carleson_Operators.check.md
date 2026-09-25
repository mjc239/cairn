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

### `adjointCarleson`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
English: For a tile $\mathfrak p$ and $f:X\to\mathbb C$, defines the adjoint operator $T^*_{\mathfrak p}f:X\to\mathbb C$, as defined above Lemma 7.4.1.

### `adjointCarlesonSum`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → Set (𝔓 X) → (X → ℂ) → X → ℂ`
English: For a set of tiles $\mathfrak C$ and $f:X\to\mathbb C$, defines $T^*_{\mathfrak C}f:X\to\mathbb C$, as defined at the end of Section 7.4.

### `carlesonOn`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
English: For a tile $\mathfrak p$ and $f:X\to\mathbb C$, defines the function $T_{\mathfrak p}f:X\to\mathbb C$, the operator of Proposition 2.0.2.

### `carlesonSum`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → Set (𝔓 X) → (X → ℂ) → X → ℂ`
English: For a set of tiles $\mathfrak C$ and $f:X\to\mathbb C$, defines $T_{\mathfrak C}f:X\to\mathbb C$, the operator defined at the end of Section 7.4.

### `adjointCarlesonSum_adjoint`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (ℭ : Set (𝔓 X)) : ∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ℭ f x = ∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ℭ g x) * f x`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {f g : X → ℂ}, BoundedCompactSupport f volume → BoundedCompactSupport g volume → ∀ (ℭ : Set (𝔓 X)), ∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ℭ f x = ∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ℭ g x) * f x`
English: Let $f,g$ be bounded with compact support and let $\mathfrak C$ be a set of tiles. Then $$\int_X\overline{g(x)}\,T_{\mathfrak C}f(x)\,dx=\int_X\overline{T^*_{\mathfrak C}g(x)}\,f(x)\,dx,$$ i.e. $T^*_{\mathfrak C}$ is the adjoint of $T_{\mathfrak C}$.
