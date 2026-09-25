You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): TileStructure, MeasureTheory, Antichain.

### `adjointCarleson`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
Docstring: The definition of `Tₚ*g(x)`, defined above Lemma 7.4.1
Previous English: For a tile $\mathfrak p$ and $f:X\to\mathbb C$, defines the adjoint operator $T^*_{\mathfrak p}f:X\to\mathbb C$, as defined above Lemma 7.4.1.
Checker's issue: Omits the setting the signature assumes (metric space X, ProofData and TileStructure bundles), and the gloss about where it is defined in the blueprint is not attributed to the docstring.

### `adjointCarlesonSum`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → (X → ℂ) → X → ℂ`
Docstring: The definition of `T_ℭ*g(x)`, defined at the bottom of Section 7.4
Previous English: For a set of tiles $\mathfrak C$ and $f:X\to\mathbb C$, defines $T^*_{\mathfrak C}f:X\to\mathbb C$, as defined at the end of Section 7.4.
Checker's issue: Omits the setting the signature assumes (metric space X, ProofData and TileStructure bundles), and the gloss about where it is defined in the blueprint is not attributed to the docstring.

### `carlesonOn`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
Docstring: The operator `T_𝔭` defined in Proposition 2.0.2.
Previous English: For a tile $\mathfrak p$ and $f:X\to\mathbb C$, defines the function $T_{\mathfrak p}f:X\to\mathbb C$, the operator of Proposition 2.0.2.
Checker's issue: Omits the setting the signature assumes (pseudometric space X, ProofData and TileStructure bundles), and the blueprint gloss is not attributed to the docstring.

### `carlesonSum`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → (X → ℂ) → X → ℂ`
Docstring: The operator `T_ℭ f` defined at the bottom of Section 7.4. We will use this in other places of the formalization as well.
Previous English: For a set of tiles $\mathfrak C$ and $f:X\to\mathbb C$, defines $T_{\mathfrak C}f:X\to\mathbb C$, the operator defined at the end of Section 7.4.
Checker's issue: Omits the setting the signature assumes (pseudometric space X, ProofData and TileStructure bundles), and the blueprint gloss is not attributed to the docstring.
