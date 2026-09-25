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

### `PreTileStructure.toGridStructure`
Lean (short): `(𝕜 : Type u_1) : GridStructure X D κ S o`
Lean (full): `(𝕜 : Type u_1) → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → GridStructure.{u_2, u} X D κ S o`
English: Let $\mathbb{k}$ be an RCLike field (i.e. $\mathbb{R}$ or $\mathbb{C}$), let $X$ be a pseudometric space carrying a doubling measure with doubling constant $A \in \mathbb{R}_{\ge 0}$ and a family of function distances $\mathrm{FunctionDistances}(\mathbb{k}, X)$ (a type $\Theta(X)$ of functions with associated local distances), and let $Q : X \to \Theta(X)$ be a simple function, $D \in \mathbb{N}$, $\kappa \in \mathbb{R}$, $S \in \mathbb{N}$ and $o \in X$, with a pre-tile structure $\mathrm{PreTileStructure}(Q, D, \kappa, S, o)$ on $X$. Definition: the grid structure $\mathrm{GridStructure}(X, D, \kappa, S, o)$ on $X$ underlying this pre-tile structure (the field $\mathbb{k}$ being an explicit parameter).

### `𝔓`
Lean (short): `(X : Type u) [FunctionDistances 𝕜 X] : Type u`
Lean (full): `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → (X : Type u) → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [PreTileStructure.{u, u_1, u_2} Q D κ S o] → Type u`
English: Let $\mathbb{k}$ be an RCLike field (i.e. $\mathbb{R}$ or $\mathbb{C}$), let $X$ be a pseudometric space carrying a doubling measure with doubling constant $A \in \mathbb{R}_{\ge 0}$ and a family of function distances $\mathrm{FunctionDistances}(\mathbb{k}, X)$ (a type $\Theta(X)$ of functions with associated local distances), and let $Q : X \to \Theta(X)$ be a simple function, $D \in \mathbb{N}$, $\kappa \in \mathbb{R}$, $S \in \mathbb{N}$ and $o \in X$, with a pre-tile structure $\mathrm{PreTileStructure}(Q, D, \kappa, S, o)$ on $X$. Definition: the type $\mathfrak{P}(X)$ of tiles of $X$ given by the pre-tile structure.

### `𝓘`
Lean (short): `[FunctionDistances 𝕜 X] (_ : 𝔓 X) : Grid X`
Lean (full): `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → Grid X`
English: Let $\mathbb{k}$ be an RCLike field (i.e. $\mathbb{R}$ or $\mathbb{C}$), let $X$ be a pseudometric space carrying a doubling measure with doubling constant $A \in \mathbb{R}_{\ge 0}$ and a family of function distances $\mathrm{FunctionDistances}(\mathbb{k}, X)$ (a type $\Theta(X)$ of functions with associated local distances), and let $Q : X \to \Theta(X)$ be a simple function, $D \in \mathbb{N}$, $\kappa \in \mathbb{R}$, $S \in \mathbb{N}$ and $o \in X$, with a pre-tile structure $\mathrm{PreTileStructure}(Q, D, \kappa, S, o)$ on $X$. Definition: for a tile $p \in \mathfrak{P}(X)$, its grid cube $\mathcal{I}(p) \in \mathrm{Grid}(X)$.

### `𝔠`
Lean (short): `[FunctionDistances 𝕜 X] (p : 𝔓 X) : X`
Lean (full): `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → X`
English: Let $\mathbb{k}$ be an RCLike field (i.e. $\mathbb{R}$ or $\mathbb{C}$), let $X$ be a pseudometric space carrying a doubling measure with doubling constant $A \in \mathbb{R}_{\ge 0}$ and a family of function distances $\mathrm{FunctionDistances}(\mathbb{k}, X)$ (a type $\Theta(X)$ of functions with associated local distances), and let $Q : X \to \Theta(X)$ be a simple function, $D \in \mathbb{N}$, $\kappa \in \mathbb{R}$, $S \in \mathbb{N}$ and $o \in X$, with a pre-tile structure $\mathrm{PreTileStructure}(Q, D, \kappa, S, o)$ on $X$. Definition: for a tile $p \in \mathfrak{P}(X)$, its center $\mathfrak{c}(p) \in X$.

### `𝔰`
Lean (short): `[FunctionDistances 𝕜 X] (p : 𝔓 X) : ℤ`
Lean (full): `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → ℤ`
English: Let $\mathbb{k}$ be an RCLike field (i.e. $\mathbb{R}$ or $\mathbb{C}$), let $X$ be a pseudometric space carrying a doubling measure with doubling constant $A \in \mathbb{R}_{\ge 0}$ and a family of function distances $\mathrm{FunctionDistances}(\mathbb{k}, X)$ (a type $\Theta(X)$ of functions with associated local distances), and let $Q : X \to \Theta(X)$ be a simple function, $D \in \mathbb{N}$, $\kappa \in \mathbb{R}$, $S \in \mathbb{N}$ and $o \in X$, with a pre-tile structure $\mathrm{PreTileStructure}(Q, D, \kappa, S, o)$ on $X$. Definition: for a tile $p \in \mathfrak{P}(X)$, its scale $\mathfrak{s}(p) \in \mathbb{Z}$.

### `TileStructure`
Lean (short): `[FunctionDistances ℝ X] (Q : outParam (SimpleFunc X (Θ X))) (D : outParam ℕ) (κ : outParam ℝ) (S : outParam ℕ) (o : outParam X) : Type (u + 1)`
Lean (full): `{X : Type u} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → [inst_2 : FunctionDistances ℝ X] → outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _)) → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (u + 1)`
Docstring: A tile structure.
English: Let $X$ be a pseudometric space carrying a doubling measure with doubling constant $A \in \mathbb{R}_{\ge 0}$ and a family of real function distances $\mathrm{FunctionDistances}(\mathbb{R}, X)$ (a type $\Theta(X)$ of functions with associated local distances). Definition (docstring: \"A tile structure\"): the type of tile structures on $X$ with data $Q$ (a simple function $X \to \Theta(X)$), $D \in \mathbb{N}$, $\kappa \in \mathbb{R}$, $S \in \mathbb{N}$ and base point $o \in X$.

### `TileStructure.toPreTileStructure`
Lean (short): `PreTileStructure Q D κ S o`
Lean (full): `{X : Type u} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {inst_2 : FunctionDistances ℝ X} → {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : TileStructure Q D κ S o] → PreTileStructure Q D κ S o`
English: Let $X$ be a pseudometric space carrying a doubling measure with doubling constant $A \in \mathbb{R}_{\ge 0}$ and a family of real function distances $\mathrm{FunctionDistances}(\mathbb{R}, X)$ (a type $\Theta(X)$ of functions with associated local distances). Let $Q : X \to \Theta(X)$ be a simple function, $D \in \mathbb{N}$, $\kappa \in \mathbb{R}$, $S \in \mathbb{N}$ and $o \in X$. Definition: the pre-tile structure $\mathrm{PreTileStructure}(Q, D, \kappa, S, o)$ underlying a tile structure $\mathrm{TileStructure}(Q, D, \kappa, S, o)$.

### `TileLike`
Lean (short): `(X : Type u_1) [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] : Type u_1`
Lean (full): `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Type u_1`
English: Let $X$ be a pseudometric space equipped with the standing Carleson data $\mathrm{ProofData}(a, q, K, \sigma_1, \sigma_2, F, G)$ (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a kernel $K : X \times X \to \mathbb{C}$, functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and with a tile structure $\mathrm{TileStructure}(Q, \mathrm{defaultD}(a), \mathrm{default}\kappa(a), \mathrm{defaultS}(X), \mathrm{cancelPt}(X))$ on $X$, where $Q$ is the function $X \to \Theta(X)$ given by the proof data. Definition: the type $\mathrm{TileLike}(X)$ of tile-like objects over $X$.

### `toTileLike`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (p : 𝔓 X) : TileLike X`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → TileLike X (F := F) (G := G)`
English: Let $X$ be a pseudometric space equipped with the standing Carleson data $\mathrm{ProofData}(a, q, K, \sigma_1, \sigma_2, F, G)$ (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a kernel $K : X \times X \to \mathbb{C}$, functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and with a tile structure $\mathrm{TileStructure}(Q, \mathrm{defaultD}(a), \mathrm{default}\kappa(a), \mathrm{defaultS}(X), \mathrm{cancelPt}(X))$ on $X$, where $Q$ is the function $X \to \Theta(X)$ given by the proof data. Definition: the tile-like object $\mathrm{toTileLike}(p) \in \mathrm{TileLike}(X)$ associated with a tile $p \in \mathfrak{P}(X)$.

### `stackSize`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (C : Set (𝔓 X)) (x : X) : ℕ`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → X → ℕ`
Docstring: The number of tiles `p` in `s` whose underlying cube `𝓘 p` contains `x`.
English: Let $X$ be a pseudometric space equipped with the standing Carleson data $\mathrm{ProofData}(a, q, K, \sigma_1, \sigma_2, F, G)$ (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a kernel $K : X \times X \to \mathbb{C}$, functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and with a tile structure $\mathrm{TileStructure}(Q, \mathrm{defaultD}(a), \mathrm{default}\kappa(a), \mathrm{defaultS}(X), \mathrm{cancelPt}(X))$ on $X$, where $Q$ is the function $X \to \Theta(X)$ given by the proof data. Definition: for a set $C \subseteq \mathfrak{P}(X)$ of tiles and $x \in X$, $\mathrm{stackSize}(C, x) \in \mathbb{N}$ is (per the docstring) the number of tiles $p \in C$ whose underlying cube $\mathcal{I}(p)$ contains $x$.

### `smul`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (l : ℝ) (p : 𝔓 X) : TileLike X`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℝ → 𝔓 X → TileLike X (F := F) (G := G)`
Docstring: This is not defined as such in the blueprint, but `λp ≲ λ'p'` can be written using `smul l p ≤ smul l' p'`. Beware: `smul 1 p` is very different from `toTileLike p`.
English: Let $X$ be a pseudometric space equipped with the standing Carleson data $\mathrm{ProofData}(a, q, K, \sigma_1, \sigma_2, F, G)$ (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a kernel $K : X \times X \to \mathbb{C}$, functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and with a tile structure $\mathrm{TileStructure}(Q, \mathrm{defaultD}(a), \mathrm{default}\kappa(a), \mathrm{defaultS}(X), \mathrm{cancelPt}(X))$ on $X$, where $Q$ is the function $X \to \Theta(X)$ given by the proof data. Definition: for $l \in \mathbb{R}$ and a tile $p \in \mathfrak{P}(X)$, the tile-like object $\mathrm{smul}(l, p) \in \mathrm{TileLike}(X)$. According to the docstring, this is not defined as such in the blueprint, but the relation $\lambda p \lesssim \lambda' p'$ can be written as $\mathrm{smul}(l, p) \le \mathrm{smul}(l', p')$; and $\mathrm{smul}(1, p)$ is very different from $\mathrm{toTileLike}(p)$.

### `E₂`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (l : ℝ) (p : 𝔓 X) : Set X`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℝ → 𝔓 X → Set X`
English: Let $X$ be a pseudometric space equipped with the standing Carleson data $\mathrm{ProofData}(a, q, K, \sigma_1, \sigma_2, F, G)$ (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a kernel $K : X \times X \to \mathbb{C}$, functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and with a tile structure $\mathrm{TileStructure}(Q, \mathrm{defaultD}(a), \mathrm{default}\kappa(a), \mathrm{defaultS}(X), \mathrm{cancelPt}(X))$ on $X$, where $Q$ is the function $X \to \Theta(X)$ given by the proof data. Definition: for $l \in \mathbb{R}$ and a tile $p \in \mathfrak{P}(X)$, the set $E_2(l, p) \subseteq X$.

### `dens₁`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔓' : Set (𝔓 X)) : ENNReal`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ENNReal`
Docstring: This density is defined to live in `ℝ≥0∞`. Use `ENNReal.toReal` to get a real number.
English: Let $X$ be a pseudometric space equipped with the standing Carleson data $\mathrm{ProofData}(a, q, K, \sigma_1, \sigma_2, F, G)$ (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a kernel $K : X \times X \to \mathbb{C}$, functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and with a tile structure $\mathrm{TileStructure}(Q, \mathrm{defaultD}(a), \mathrm{default}\kappa(a), \mathrm{defaultS}(X), \mathrm{cancelPt}(X))$ on $X$, where $Q$ is the function $X \to \Theta(X)$ given by the proof data. Definition: for a set $\mathfrak{P}' \subseteq \mathfrak{P}(X)$ of tiles, the density $\mathrm{dens}_1(\mathfrak{P}') \in [0, \infty]$ (per the docstring, defined to live in the extended nonnegative reals).

### `exists_maximal_disjoint_covering_subfamily`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (A : Set (𝔓 X)) : ∃ B, (B.PairwiseDisjoint fun p => ↑(𝓘 p)) ∧ B ⊆ A ∧ ∀ a_1 ∈ A, ∃ b ∈ B, ↑(𝓘 a_1) ⊆ ↑(𝓘 b)`
Lean (full): `∀ {X : Type u_1} [inst : PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (A : Set (𝔓 X)), ∃ (B : Set (𝔓 X)), (B.PairwiseDisjoint (α := Set X) fun (p : 𝔓 X) => ↑(𝓘 p)) ∧ B ⊆ A ∧ ∀ a_1 ∈ A, ∃ b ∈ B, ↑(𝓘 a_1) ⊆ ↑(𝓘 b)`
Docstring: Given any family of tiles, one can extract a maximal disjoint subfamily, covering everything.
English: Let $X$ be a pseudometric space, and assume the standing assumptions of the proof: the data $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \times X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$, $F, G \subseteq X$ satisfy `ProofData`, and $X$ carries a tile structure (`TileStructure` with $Q$, $D$ = `defaultD a`, $\kappa$ = `defaultκ a`, $S$ = `defaultS X` and the point `cancelPt X`). Then for every set $A$ of tiles there is a set $B$ of tiles such that the cubes $\mathcal{I}(p)$, $p \in B$, are pairwise disjoint, $B \subseteq A$, and for every $a \in A$ there is $b \in B$ with $\mathcal{I}(a) \subseteq \mathcal{I}(b)$.

### `iteratedMaximalSubfamily`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (A : Set (𝔓 X)) (n : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ℕ → Set (𝔓 X)`
Docstring: Iterating `maximalSubfamily` to obtain disjoint subfamilies of `A`.
English: Let $X$ be a pseudometric space equipped with the standing Carleson data $\mathrm{ProofData}(a, q, K, \sigma_1, \sigma_2, F, G)$ (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a kernel $K : X \times X \to \mathbb{C}$, functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and with a tile structure $\mathrm{TileStructure}(Q, \mathrm{defaultD}(a), \mathrm{default}\kappa(a), \mathrm{defaultS}(X), \mathrm{cancelPt}(X))$ on $X$, where $Q$ is the function $X \to \Theta(X)$ given by the proof data. Definition: for a set $A \subseteq \mathfrak{P}(X)$ of tiles and $n \in \mathbb{N}$, the set of tiles $\mathrm{iteratedMaximalSubfamily}(A, n) \subseteq \mathfrak{P}(X)$; per the docstring, it is obtained by iterating the choice of a maximal subfamily, producing disjoint subfamilies of $A$.

### `dens₂`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔓' : Set (𝔓 X)) : ENNReal`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ENNReal`
Docstring: This density is defined to live in `ℝ≥0∞`. Use `ENNReal.toReal` to get a real number.
English: Let $X$ be a pseudometric space equipped with the standing Carleson data $\mathrm{ProofData}(a, q, K, \sigma_1, \sigma_2, F, G)$ (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a kernel $K : X \times X \to \mathbb{C}$, functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and with a tile structure $\mathrm{TileStructure}(Q, \mathrm{defaultD}(a), \mathrm{default}\kappa(a), \mathrm{defaultS}(X), \mathrm{cancelPt}(X))$ on $X$, where $Q$ is the function $X \to \Theta(X)$ given by the proof data. Definition: for a set $\mathfrak{P}' \subseteq \mathfrak{P}(X)$ of tiles, the density $\mathrm{dens}_2(\mathfrak{P}') \in [0, \infty]$ (per the docstring, defined to live in the extended nonnegative reals).

### `E`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (p : 𝔓 X) : Set X`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → Set X`
Docstring: The set `E` defined in Proposition 2.0.2.
English: Let $X$ be a pseudometric space equipped with the standing Carleson data $\mathrm{ProofData}(a, q, K, \sigma_1, \sigma_2, F, G)$ (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a kernel $K : X \times X \to \mathbb{C}$, functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and with a tile structure $\mathrm{TileStructure}(Q, \mathrm{defaultD}(a), \mathrm{default}\kappa(a), \mathrm{defaultS}(X), \mathrm{cancelPt}(X))$ on $X$, where $Q$ is the function $X \to \Theta(X)$ given by the proof data. Definition: for a tile $p \in \mathfrak{P}(X)$, the set $E(p) \subseteq X$, which according to the docstring is the set $E$ defined in Proposition 2.0.2.
