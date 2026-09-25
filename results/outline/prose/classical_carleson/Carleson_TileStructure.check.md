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

### `PreTileStructure.toGridStructure`
Lean (short): `(𝕜 : Type u_1) : GridStructure X D κ S o`
Lean (full): `(𝕜 : Type u_1) → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (Θ X))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure Q D κ S o] → GridStructure X D κ S o`
English: Definition: the grid structure on $X$ with parameters $D, \kappa, S, o$ underlying a pre-tile structure (with the field $\mathbb{k}$ as parameter).

### `𝔓`
Lean (short): `(X : Type u) [FunctionDistances 𝕜 X] : Type u`
Lean (full): `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → (X : Type u) → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (Θ X)} → [PreTileStructure Q D κ S o] → Type u`
English: Definition: the type $\mathfrak{P}(X)$ of tiles of $X$ (given by the tile structure).

### `𝓘`
Lean (short): `[FunctionDistances 𝕜 X] (_ : 𝔓 X) : Grid X`
Lean (full): `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (Θ X)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → Grid X`
English: Definition: for a tile $p \in \mathfrak{P}(X)$, its grid cube $\mathcal{I}(p) \in \mathrm{Grid}(X)$.

### `𝔠`
Lean (short): `[FunctionDistances 𝕜 X] (p : 𝔓 X) : X`
Lean (full): `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (Θ X)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → X`
English: Definition: for a tile $p \in \mathfrak{P}(X)$, its center $\mathfrak{c}(p) \in X$.

### `𝔰`
Lean (short): `[FunctionDistances 𝕜 X] (p : 𝔓 X) : ℤ`
Lean (full): `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (Θ X)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → ℤ`
English: Definition: for a tile $p \in \mathfrak{P}(X)$, its scale $\mathfrak{s}(p) \in \mathbb{Z}$.

### `TileStructure`
Lean (short): `[FunctionDistances ℝ X] (Q : outParam (SimpleFunc X (Θ X))) (D : outParam ℕ) (κ : outParam ℝ) (S : outParam ℕ) (o : outParam X) : Type (u + 1)`
Lean (full): `{X : Type u} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → [inst_2 : FunctionDistances ℝ X] → outParam (SimpleFunc X (Θ X)) → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (u + 1)`
English: Definition: a tile structure on $X$ with data $Q$ (a simple function $X \to \Theta(X)$), $D \in \mathbb{N}$, $\kappa \in \mathbb{R}$, $S \in \mathbb{N}$ and base point $o \in X$.

### `TileStructure.toPreTileStructure`
Lean (short): `PreTileStructure Q D κ S o`
Lean (full): `{X : Type u} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {inst_2 : FunctionDistances ℝ X} → {Q : outParam (SimpleFunc X (Θ X))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : TileStructure Q D κ S o] → PreTileStructure Q D κ S o`
English: Definition: the pre-tile structure (with data $Q, D, \kappa, S, o$) underlying a tile structure.

### `TileLike`
Lean (short): `(X : Type u_1) [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] : Type u_1`
Lean (full): `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → Type u_1`
English: Definition: the type $\mathrm{TileLike}(X)$ of tile-like objects over $X$.

### `toTileLike`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (p : 𝔓 X) : TileLike X`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → 𝔓 X → TileLike X`
English: Definition: the tile-like object associated with a tile $p \in \mathfrak{P}(X)$.

### `stackSize`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (C : Set (𝔓 X)) (x : X) : ℕ`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → Set (𝔓 X) → X → ℕ`
English: Definition: for a set $C$ of tiles and $x \in X$, $\mathrm{stackSize}(C, x) \in \mathbb{N}$ is the number of tiles $p \in C$ whose cube $\mathcal{I}(p)$ contains $x$.

### `smul`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (l : ℝ) (p : 𝔓 X) : TileLike X`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → ℝ → 𝔓 X → TileLike X`
English: Definition: for $l \in \mathbb{R}$ and a tile $p$, the tile-like object $\mathrm{smul}(l, p)$ (the dilate $l p$), so that the relation $\lambda p \lesssim \lambda' p'$ can be written as $\mathrm{smul}(l, p) \le \mathrm{smul}(l', p')$. Note that $\mathrm{smul}(1, p)$ is very different from $\mathrm{toTileLike}(p)$.

### `E₂`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (l : ℝ) (p : 𝔓 X) : Set X`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → ℝ → 𝔓 X → Set X`
English: Definition: for $l \in \mathbb{R}$ and a tile $p$, the set $E_2(l, p) \subseteq X$.

### `dens₁`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔓' : Set (𝔓 X)) : ENNReal`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → Set (𝔓 X) → ENNReal`
English: Definition: for a set $\mathfrak{P}'$ of tiles, the density $\mathrm{dens}_1(\mathfrak{P}') \in [0, \infty]$.

### `exists_maximal_disjoint_covering_subfamily`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (A : Set (𝔓 X)) : ∃ B, (B.PairwiseDisjoint fun p => ↑(𝓘 p)) ∧ B ⊆ A ∧ ∀ a_1 ∈ A, ∃ b ∈ B, ↑(𝓘 a_1) ⊆ ↑(𝓘 b)`
Lean (full): `∀ {X : Type u_1} [inst : PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (A : Set (𝔓 X)), ∃ B, (B.PairwiseDisjoint fun p => ↑(𝓘 p)) ∧ B ⊆ A ∧ ∀ a_1 ∈ A, ∃ b ∈ B, ↑(𝓘 a_1) ⊆ ↑(𝓘 b)`
English: For every set $A$ of tiles there is a set $B$ of tiles such that the cubes $\mathcal{I}(p)$, $p \in B$, are pairwise disjoint, $B \subseteq A$, and for every $a \in A$ there is $b \in B$ with $\mathcal{I}(a) \subseteq \mathcal{I}(b)$.

### `iteratedMaximalSubfamily`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (A : Set (𝔓 X)) (n : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → Set (𝔓 X) → ℕ → Set (𝔓 X)`
English: Definition: for a set $A$ of tiles and $n \in \mathbb{N}$, the $n$-th disjoint subfamily of $A$ obtained by iterating the choice of a maximal disjoint subfamily.

### `dens₂`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔓' : Set (𝔓 X)) : ENNReal`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → Set (𝔓 X) → ENNReal`
English: Definition: for a set $\mathfrak{P}'$ of tiles, the density $\mathrm{dens}_2(\mathfrak{P}') \in [0, \infty]$.

### `E`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (p : 𝔓 X) : Set X`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → 𝔓 X → Set X`
English: Definition: for a tile $p \in \mathfrak{P}(X)$, the set $E(p) \subseteq X$ defined in Proposition 2.0.2.
