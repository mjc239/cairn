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

### `grid_existence`
Lean (short): `(X : Type u_1) : GridStructure X (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`
Lean (full): `(X : Type u_1) → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → GridStructure X (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)`
Docstring: Proof that there exists a grid structure.
English: Let $X$ be a pseudometric space, let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\to X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume the standing hypotheses `ProofData a q K σ₁ σ₂ F G` (which supply, among other things, the function $Q$ used below). Write $D=\mathrm{defaultD}(a)$, $\kappa=\mathrm{default}\kappa(a)$, $S=\mathrm{defaultS}(X)$ and $o=\mathrm{cancelPt}(X)$. Definition (construction): a grid structure `GridStructure X D κ S o` on $X$ with parameters $D,\kappa,S$ and point $o$. Its docstring describes it as the proof that there exists a grid structure.

### `tileData_existence`
Lean (short): `[GridStructure X (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] : PreTileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [GridStructure X (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → PreTileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)`
English: Let $X$ be a pseudometric space, let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\to X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume the standing hypotheses `ProofData a q K σ₁ σ₂ F G` (which supply, among other things, the function $Q$ used below). Write $D=\mathrm{defaultD}(a)$, $\kappa=\mathrm{default}\kappa(a)$, $S=\mathrm{defaultS}(X)$ and $o=\mathrm{cancelPt}(X)$. Assume moreover a grid structure `GridStructure X D κ S o` on $X$. Definition (construction): a pre-tile structure `PreTileStructure Q D κ S o` on $X$ for $Q$ with parameters $D,\kappa,S$ and point $o$.

### `Construction.Ω`
Lean (short): `[GridStructure X (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (p : 𝔓 X) : Set (Θ X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : GridStructure X (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → Set (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)`
English: Let $X$ be a pseudometric space, let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\to X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume the standing hypotheses `ProofData a q K σ₁ σ₂ F G` (which supply, among other things, the function $Q$ used below). Write $D=\mathrm{defaultD}(a)$, $\kappa=\mathrm{default}\kappa(a)$, $S=\mathrm{defaultS}(X)$ and $o=\mathrm{cancelPt}(X)$. Assume moreover a grid structure `GridStructure X D κ S o` on $X$. Let $\mathfrak P(X)$ denote the tiles `𝔓 X` and $\Theta(X)$ the space `Θ X`. Definition: for a tile $p\in\mathfrak P(X)$, a set $\Omega(p)\subseteq\Theta(X)$ (named `Construction.Ω p`).

### `tile_existence`
Lean (short): `(X : Type u_1) [GridStructure X (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`
Lean (full): `(X : Type u_1) → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [GridStructure X (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)`
English: Let $X$ be a pseudometric space, let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\to X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume the standing hypotheses `ProofData a q K σ₁ σ₂ F G` (which supply, among other things, the function $Q$ used below). Write $D=\mathrm{defaultD}(a)$, $\kappa=\mathrm{default}\kappa(a)$, $S=\mathrm{defaultS}(X)$ and $o=\mathrm{cancelPt}(X)$. Assume moreover a grid structure `GridStructure X D κ S o` on $X$. Definition (construction): a tile structure `TileStructure Q D κ S o` on $X$ for $Q$ with parameters $D,\kappa,S$ and point $o$.
