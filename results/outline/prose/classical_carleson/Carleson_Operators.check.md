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
be supported by the docstring or the Lean. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `adjointCarleson`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
Docstring: The definition of `Tₚ*g(x)`, defined above Lemma 7.4.1
English: Let $X$ be a metric space, and assume the standing assumptions of the proof: `ProofData` with parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$, together with a tile structure on $X$ (with the frequency map $Q$, the default parameters $D$, $\kappa$, $S$ and the cancellation point). For a tile $\mathfrak p \in \mathfrak P(X)$, a complex-valued function $f : X \to \mathbb C$ and a point $x \in X$, this defines a complex number $T^*_{\mathfrak p} f(x)$; according to the docstring, it is the definition of $T_{\mathfrak p}^* g(x)$ given above Lemma 7.4.1.

### `adjointCarlesonSum`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → (X → ℂ) → X → ℂ`
Docstring: The definition of `T_ℭ*g(x)`, defined at the bottom of Section 7.4
English: Let $X$ be a metric space, and assume the standing assumptions of the proof: `ProofData` with parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$, together with a tile structure on $X$ (with the frequency map $Q$, the default parameters $D$, $\kappa$, $S$ and the cancellation point). For a set of tiles $\mathfrak C \subseteq \mathfrak P(X)$, a complex-valued function $f : X \to \mathbb C$ and a point $x \in X$, this defines a complex number $T^*_{\mathfrak C} f(x)$; according to the docstring, it is the definition of $T_{\mathfrak C}^* g(x)$ given at the bottom of Section 7.4.

### `carlesonOn`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
Docstring: The operator `T_𝔭` defined in Proposition 2.0.2.
English: Let $X$ be a pseudometric space, and assume the standing assumptions of the proof: `ProofData` with parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$, together with a tile structure on $X$ (with the frequency map $Q$, the default parameters $D$, $\kappa$, $S$ and the cancellation point). For a tile $\mathfrak p \in \mathfrak P(X)$ and a complex-valued function $f : X \to \mathbb C$, this defines a function $T_{\mathfrak p} f : X \to \mathbb C$; according to the docstring, it is the operator $T_{\mathfrak p}$ defined in Proposition 2.0.2.

### `carlesonSum`
Lean (short): `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → (X → ℂ) → X → ℂ`
Docstring: The operator `T_ℭ f` defined at the bottom of Section 7.4. We will use this in other places of the formalization as well.
English: Let $X$ be a pseudometric space, and assume the standing assumptions of the proof: `ProofData` with parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$, together with a tile structure on $X$ (with the frequency map $Q$, the default parameters $D$, $\kappa$, $S$ and the cancellation point). For a set of tiles $\mathfrak C \subseteq \mathfrak P(X)$, a complex-valued function $f : X \to \mathbb C$ and a point $x \in X$, this defines a complex number $T_{\mathfrak C} f(x)$; according to the docstring, it is the operator $T_{\mathfrak C} f$ defined at the bottom of Section 7.4, which is also used in other places of the formalization.

### `adjointCarlesonSum_adjoint`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (ℭ : Set (𝔓 X)) : ∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ℭ f x = ∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ℭ g x) * f x`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {f g : X → ℂ}, BoundedCompactSupport f volume → BoundedCompactSupport g volume → ∀ (ℭ : Set (𝔓 X)), Eq (α := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => HMul.hMul (α := ℂ) ((starRingEnd ℂ) (g x) : ℂ) (carlesonSum (F := F) (G := G) ℭ f x)) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => HMul.hMul (α := ℂ) ((starRingEnd ℂ) (adjointCarlesonSum (F := F) (G := G) ℭ g x) : ℂ) (f x))`
Docstring: `adjointCarlesonSum` is the adjoint of `carlesonSum`.
English: Let $X$ be a metric space and work under the standing assumptions of the proof: the data $a\in\mathbb N$, $q\in\mathbb R$, $K:X\times X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$, $F,G\subseteq X$ of `ProofData` (making $X$ a doubling metric measure space with measure $\mu$), together with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)` with set of tiles $\mathfrak P(X)$. Let $f,g:X\to\mathbb C$ be bounded with compact support and let $\mathfrak C\subseteq\mathfrak P(X)$ be a set of tiles. Then $$\int_X\overline{g(x)}\,T_{\mathfrak C}f(x)\,d\mu(x)=\int_X\overline{T^*_{\mathfrak C}g(x)}\,f(x)\,d\mu(x),$$ where $T_{\mathfrak C}$ is `carlesonSum` and $T^*_{\mathfrak C}$ is `adjointCarlesonSum`, i.e. $T^*_{\mathfrak C}$ is the adjoint of $T_{\mathfrak C}$.
