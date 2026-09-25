You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one. For a definition, name the setting its signature assumes. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): MeasureTheory, TileStructure, Antichain.

### `TileStructure.Forest.tree_projection_estimate`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_2_1 a) * eLpNorm (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) fun x => ‖f x‖) 2 volume * eLpNorm (Forest.approxOnCube (Forest.𝓛 ((fun x => t.𝔗 x) u)) fun x => ‖g x‖) 2 volume`
Lean (full): `∀ {X : Type u_2} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {n : ℕ} {t : Forest X n} {u : 𝔓 X} {f g : X → ℂ}, BoundedCompactSupport f volume → BoundedCompactSupport g volume → u ∈ t → ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_2_1 a) * eLpNorm (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) fun x => ‖f x‖) 2 volume * eLpNorm (Forest.approxOnCube (Forest.𝓛 ((fun x => t.𝔗 x) u)) fun x => ‖g x‖) 2 volume`
Docstring: Lemma 7.2.1.
Previous English: (Lemma 7.2.1) Let $t$ be a forest, $u \in t$, and let $f, g$ be bounded with compact support. Then $$\Big|\int_X \overline{g(x)}\, \mathrm{carlesonSum}(\mathfrak{T}(u), f)(x)\,dx\Big| \le C_{7.2.1}(a)\, \big\|P_{\mathcal{J}(\mathfrak{T}(u))} |f|\big\|_{L^2}\, \big\|P_{\mathcal{L}(\mathfrak{T}(u))} |g|\big\|_{L^2},$$ where $P_{\mathcal{C}} h$ denotes `approxOnCube` $\mathcal{C}$ $h$ (the approximation of $h$ by its averages on the cubes of the collection $\mathcal{C}$), $\mathcal{J}$ and $\mathcal{L}$ are the cube collections `Forest.𝓙` and `Forest.𝓛`, and $C_{7.2.1}$ is `Forest.C7_2_1`.
Checker's issue: Omits the standing assumptions (ProofData and TileStructure instances) under which the lemma holds.

### `TileStructure.Forest.eLpNorm_MB_le`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) : eLpNorm (maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f) 2 volume ≤ ↑(CMB (↑(defaultA a)) 2) * eLpNorm f 2 volume`
Lean (full): `∀ {X : Type u_2} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {𝕜 : Type u_4} [inst_3 : RCLike 𝕜] {f : X → 𝕜}, BoundedCompactSupport f volume → eLpNorm (maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f) 2 volume ≤ ↑(CMB (↑(defaultA a)) 2) * eLpNorm f 2 volume`
Previous English: For $f$ bounded with compact support, the maximal function $M_{\mathcal{B}}$ associated with the ball family $\mathcal{B}$ = `Forest.𝓑`, centres `Forest.c𝓑` and radii `Forest.r𝓑` (with exponent $1$) satisfies $$\|M_{\mathcal{B}} f\|_{L^2} \le C_{M}(A, 2)\, \|f\|_{L^2},$$ where $A$ = `defaultA a` and $C_M$ is `CMB`.
Checker's issue: Omits the standing assumptions (ProofData and TileStructure instances) under which the lemma holds.

### `TileStructure.Forest.boundary_operator_bound`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) : eLpNorm (t.boundaryOperator u f) 2 volume ≤ ↑(Forest.C7_2_3 a) * eLpNorm f 2 volume`
Lean (full): `∀ {X : Type u_2} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {n : ℕ} {t : Forest X n} {u : 𝔓 X} {f : X → ℂ}, BoundedCompactSupport f volume → eLpNorm (t.boundaryOperator u f) 2 volume ≤ ↑(Forest.C7_2_3 a) * eLpNorm f 2 volume`
Docstring: Lemma 7.2.3.
Previous English: (Lemma 7.2.3) For a forest $t$, a tile $u$, and $f$ bounded with compact support, $$\|\mathrm{boundaryOperator}_t(u, f)\|_{L^2} \le C_{7.2.3}(a)\, \|f\|_{L^2},$$ where $C_{7.2.3}$ is `Forest.C7_2_3`.
Checker's issue: Omits the standing assumptions (ProofData and TileStructure instances) under which the lemma holds.

### `TileStructure.Forest.nontangential_operator_bound`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (θ : Θ X) : eLpNorm (Forest.nontangentialMaximalFunction θ f) 2 volume ≤ ↑(Forest.C7_2_2 a) * eLpNorm f 2 volume`
Lean (full): `∀ {X : Type u_2} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {f : X → ℂ}, BoundedCompactSupport f volume → ∀ (θ : Θ X), eLpNorm (Forest.nontangentialMaximalFunction θ f) 2 volume ≤ ↑(Forest.C7_2_2 a) * eLpNorm f 2 volume`
Docstring: Lemma 7.2.2.
Previous English: (Lemma 7.2.2) For $f$ bounded with compact support and $\theta \in \Theta(X)$, the nontangential maximal function satisfies $$\|T^{\theta}_{\mathrm{nt}} f\|_{L^2} \le C_{7.2.2}(a)\, \|f\|_{L^2},$$ where $T^{\theta}_{\mathrm{nt}}$ is `Forest.nontangentialMaximalFunction θ` and $C_{7.2.2}$ is `Forest.C7_2_2`.
Checker's issue: Omits the standing assumptions (ProofData and TileStructure instances) under which the lemma holds.
