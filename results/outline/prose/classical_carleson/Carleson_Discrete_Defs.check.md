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

### `aux𝓒`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) : Set (Grid X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → ℕ → Set (Grid X)`
English: For $k \in \mathbb{N}$, we define an auxiliary collection $\operatorname{aux}\mathcal{C}(k)$ of dyadic cubes, a subset of $\mathcal{D}$ (the grid of $X$).

### `dens'`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (P' : Set (𝔓 X)) : ENNReal`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → ℕ → Set (𝔓 X) → ENNReal`
English: For $k \in \mathbb{N}$ and a set of tiles $\mathfrak{P}' \subseteq \mathfrak{P}(X)$, we define the density $\operatorname{dens}'_k(\mathfrak{P}') \in [0, \infty]$ as in (5.1.6).

### `ℭ`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → ℕ → ℕ → Set (𝔓 X)`
English: Assume the standing data of the proof (ProofData with parameters $a, q, K, \sigma_1, \sigma_2, F, G$) and a tile structure on $X$ with the default parameters $D$, $\kappa$, $S$ and cancellation point. For $k, n \in \mathbb{N}$, we define the set of tiles $\mathfrak{C}(k, n) \subseteq \mathfrak{P}(X)$ as in (5.1.7): the tiles of $\mathfrak{P}(k)$ selected according to their density, indexed by $n$.

### `𝔐`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → ℕ → ℕ → Set (𝔓 X)`
English: For $k, n \in \mathbb{N}$, we define the set of tiles $\mathfrak{M}(k, n) \subseteq \mathfrak{P}(X)$ as in (5.1.4) and (5.1.5).

### `𝔅`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (p : 𝔓 X) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → ℕ → ℕ → 𝔓 X → Set (𝔓 X)`
English: For $k, n \in \mathbb{N}$ and a tile $p \in \mathfrak{P}(X)$, we define the subset $\mathfrak{B}(p)$ of $\mathfrak{M}(k, n)$ as in (5.1.8).

### `ℭ₁`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
English: Assume the standing data of the proof (ProofData with parameters $a, q, K, \sigma_1, \sigma_2, F, G$) and a tile structure on $X$ with the default parameters $D$, $\kappa$, $S$ and cancellation point. For $k, n, j \in \mathbb{N}$, we define the set of tiles $\mathfrak{C}_1(k, n, j) \subseteq \mathfrak{P}(X)$, the subset of $\mathfrak{C}(k, n)$ given in (5.1.9).

### `ℭ₂`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
English: For $k, n, j \in \mathbb{N}$, we define the subset $\mathfrak{C}_2(k, n, j)$ of $\mathfrak{C}_1(k, n, j)$ as in (5.1.13).

### `𝔘₁`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
English: For $k, n, j \in \mathbb{N}$, we define the subset $\mathfrak{U}_1(k, n, j)$ of $\mathfrak{C}_1(k, n, j)$ as in (5.1.14).

### `ℭ₅`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
English: For $k, n, j \in \mathbb{N}$, we define the subset $\mathfrak{C}_5(k, n, j)$ of $\mathfrak{C}_4(k, n, j)$ as in (5.1.23).
