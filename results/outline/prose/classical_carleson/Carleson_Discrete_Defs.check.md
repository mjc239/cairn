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

### `aux𝓒`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) : Set (Grid X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → Set (Grid X)`
English: Let $X$ be a metric space, and assume the standing assumptions of the proof: `ProofData` with parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$, together with a tile structure on $X$ (with the frequency map $Q$, the default parameters $D$, $\kappa$, $S$ and the cancellation point). For a natural number $k$, $\operatorname{aux}\mathcal{C}(k)$ is a set of dyadic cubes, i.e. a subset of the grid $\mathcal{D}$ of $X$.

### `dens'`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (P' : Set (𝔓 X)) : ENNReal`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → Set (𝔓 X) → ENNReal`
Docstring: The definition `dens'_k(𝔓')` given in (5.1.6).
English: Let $X$ be a metric space, and assume the standing assumptions of the proof: `ProofData` with parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$, together with a tile structure on $X$ (with the frequency map $Q$, the default parameters $D$, $\kappa$, $S$ and the cancellation point). For a natural number $k$ and a set of tiles $\mathfrak{P}' \subseteq \mathfrak{P}(X)$, $\operatorname{dens}'_k(\mathfrak{P}')$ is an extended nonnegative real number in $[0,\infty]$; according to the docstring, it is the definition $\operatorname{dens}'_k(\mathfrak{P}')$ given in (5.1.6).

### `ℭ`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → Set (𝔓 X)`
Docstring: The partition `ℭ(k, n)` of `𝔓(k)` by density, given in (5.1.7).
English: Let $X$ be a metric space, and assume the standing assumptions of the proof: `ProofData` with parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$, together with a tile structure on $X$ (with the frequency map $Q$, the default parameters $D$, $\kappa$, $S$ and the cancellation point). For natural numbers $k, n$, $\mathfrak{C}(k, n)$ is a set of tiles in $\mathfrak{P}(X)$; according to the docstring, it is the partition $\mathfrak{C}(k, n)$ of $\mathfrak{P}(k)$ by density, given in (5.1.7).

### `𝔐`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → Set (𝔓 X)`
Docstring: The definition `𝔐(k, n)` given in (5.1.4) and (5.1.5).
English: Let $X$ be a metric space, and assume the standing assumptions of the proof: `ProofData` with parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$, together with a tile structure on $X$ (with the frequency map $Q$, the default parameters $D$, $\kappa$, $S$ and the cancellation point). For natural numbers $k, n$, $\mathfrak{M}(k, n)$ is a set of tiles in $\mathfrak{P}(X)$; according to the docstring, it is the definition $\mathfrak{M}(k, n)$ given in (5.1.4) and (5.1.5).

### `𝔅`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (p : 𝔓 X) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → 𝔓 X → Set (𝔓 X)`
Docstring: The subset `𝔅(p)` of `𝔐(k, n)`, given in (5.1.8).
English: Let $X$ be a metric space, and assume the standing assumptions of the proof: `ProofData` with parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$, together with a tile structure on $X$ (with the frequency map $Q$, the default parameters $D$, $\kappa$, $S$ and the cancellation point). For natural numbers $k, n$ and a tile $p \in \mathfrak{P}(X)$, $\mathfrak{B}(p)$ is a set of tiles in $\mathfrak{P}(X)$; according to the docstring, it is the subset $\mathfrak{B}(p)$ of $\mathfrak{M}(k, n)$ given in (5.1.8).

### `ℭ₁`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `ℭ₁(k, n, j)` of `ℭ(k, n)`, given in (5.1.9). Together with `𝔏₀(k, n)` this forms a partition.
English: Let $X$ be a metric space, and assume the standing assumptions of the proof: `ProofData` with parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$, together with a tile structure on $X$ (with the frequency map $Q$, the default parameters $D$, $\kappa$, $S$ and the cancellation point). For natural numbers $k, n, j$, $\mathfrak{C}_1(k, n, j)$ is a set of tiles in $\mathfrak{P}(X)$; according to the docstring, it is the subset $\mathfrak{C}_1(k, n, j)$ of $\mathfrak{C}(k, n)$ given in (5.1.9), and together with $\mathfrak{L}_0(k, n)$ these sets form a partition.

### `ℭ₂`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `ℭ₂(k, n, j)` of `ℭ₁(k, n, j)`, given in (5.1.13).
English: Let $X$ be a metric space, and assume the standing assumptions of the proof: `ProofData` with parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$, together with a tile structure on $X$ (with the frequency map $Q$, the default parameters $D$, $\kappa$, $S$ and the cancellation point). For natural numbers $k, n, j$, $\mathfrak{C}_2(k, n, j)$ is a set of tiles in $\mathfrak{P}(X)$; according to the docstring, it is the subset $\mathfrak{C}_2(k, n, j)$ of $\mathfrak{C}_1(k, n, j)$ given in (5.1.13).

### `𝔘₁`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `𝔘₁(k, n, j)` of `ℭ₁(k, n, j)`, given in (5.1.14).
English: Let $X$ be a metric space, and assume the standing assumptions of the proof: `ProofData` with parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$, together with a tile structure on $X$ (with the frequency map $Q$, the default parameters $D$, $\kappa$, $S$ and the cancellation point). For natural numbers $k, n, j$, $\mathfrak{U}_1(k, n, j)$ is a set of tiles in $\mathfrak{P}(X)$; according to the docstring, it is the subset $\mathfrak{U}_1(k, n, j)$ of $\mathfrak{C}_1(k, n, j)$ given in (5.1.14).

### `ℭ₅`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `ℭ₅(k, n, j)` of `ℭ₄(k, n, j)`, given in (5.1.23).
English: Let $X$ be a metric space, and assume the standing assumptions of the proof: `ProofData` with parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$, together with a tile structure on $X$ (with the frequency map $Q$, the default parameters $D$, $\kappa$, $S$ and the cancellation point). For natural numbers $k, n, j$, $\mathfrak{C}_5(k, n, j)$ is a set of tiles in $\mathfrak{P}(X)$; according to the docstring, it is the subset $\mathfrak{C}_5(k, n, j)$ of $\mathfrak{C}_4(k, n, j)$ given in (5.1.23).
