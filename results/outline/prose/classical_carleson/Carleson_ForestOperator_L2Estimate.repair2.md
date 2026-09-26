You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring, and when no
docstring or Lean supports a description of an object, name it instead of describing it. Give every variable its
type, introduce every symbol, and never use one letter for two things.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): TileStructure, MeasureTheory, Antichain.

### `TileStructure.Forest.tree_projection_estimate`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_2_1 a) * eLpNorm (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) fun x => ‖f x‖) 2 volume * eLpNorm (Forest.approxOnCube (Forest.𝓛 ((fun x => t.𝔗 x) u)) fun x => ‖g x‖) 2 volume`
Lean (full): `∀ {X : Type u_2} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u : 𝔓 X} {f g : X → ℂ}, BoundedCompactSupport f volume → BoundedCompactSupport g volume → u ∈ t → enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => HMul.hMul (α := ℂ) ((starRingEnd ℂ) (g x) : ℂ) (carlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) f x)) ≤ ↑(Forest.C7_2_1 a) * @eLpNorm _ ℝ _ MeasureSpace.toMeasurableSpace (Forest.approxOnCube (F := F) (G := G) (Forest.𝓙 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) fun x => ‖f x‖) (2 : ENNReal) volume * @eLpNorm _ ℝ _ MeasureSpace.toMeasurableSpace (Forest.approxOnCube (F := F) (G := G) (Forest.𝓛 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) fun x => ‖g x‖) (2 : ENNReal) volume`
Docstring: Lemma 7.2.1.
Previous English: (Lemma 7.2.1) Let $X$ be a metric space, and assume the standing assumptions of the proof: the data $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \times X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$, $F, G \subseteq X$ satisfy `ProofData` (so that $X$ is a doubling metric measure space with measure `volume`), and $X$ carries a tile structure (`TileStructure` with $Q$, $D$ = `defaultD a`, $\kappa$ = `defaultκ a`, $S$ = `defaultS X` and the point `cancelPt X`), with tiles $\mathfrak{P}(X)$ and dyadic grid cubes. Let $n \in \mathbb{N}$ and let $t$ be an $n$-forest, $u \in t$, and let $f, g$ be bounded with compact support. Then $$\Big|\int_X \overline{g(x)}\, \mathrm{carlesonSum}(\mathfrak{T}(u), f)(x)\,dx\Big| \le C_{7.2.1}(a)\, \big\|P_{\mathcal{J}(\mathfrak{T}(u))} |f|\big\|_{L^2}\, \big\|P_{\mathcal{L}(\mathfrak{T}(u))} |g|\big\|_{L^2},$$ where $P_{\mathcal{C}} h$ denotes `approxOnCube` $\mathcal{C}$ $h$ (the approximation of $h$ by its averages on the cubes of the collection $\mathcal{C}$), $\mathcal{J}$ and $\mathcal{L}$ are the cube collections `Forest.𝓙` and `Forest.𝓛`, and $C_{7.2.1}$ is `Forest.C7_2_1`.
Checker's issue: Never says the functions f (and g) are complex-valued, as the Lean requires; state their types.

### `TileStructure.Forest.boundary_operator_bound`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) : eLpNorm (t.boundaryOperator u f) 2 volume ≤ ↑(Forest.C7_2_3 a) * eLpNorm f 2 volume`
Lean (full): `∀ {X : Type u_2} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u : 𝔓 X} {f : X → ℂ}, BoundedCompactSupport f volume → @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace (t.boundaryOperator (F := F) (G := G) u f) (2 : ENNReal) volume ≤ ↑(Forest.C7_2_3 a) * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f (2 : ENNReal) volume`
Docstring: Lemma 7.2.3.
Previous English: (Lemma 7.2.3) Let $X$ be a metric space, and assume the standing assumptions of the proof: the data $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \times X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$, $F, G \subseteq X$ satisfy `ProofData` (so that $X$ is a doubling metric measure space with measure `volume`), and $X$ carries a tile structure (`TileStructure` with $Q$, $D$ = `defaultD a`, $\kappa$ = `defaultκ a`, $S$ = `defaultS X` and the point `cancelPt X`), with tiles $\mathfrak{P}(X)$ and dyadic grid cubes. For $n \in \mathbb{N}$, an $n$-forest $t$, a tile $u$, and $f$ bounded with compact support, $$\|\mathrm{boundaryOperator}_t(u, f)\|_{L^2} \le C_{7.2.3}(a)\, \|f\|_{L^2},$$ where $C_{7.2.3}$ is `Forest.C7_2_3`.
Checker's issue: Never says the functions f (and g) are complex-valued, as the Lean requires; state their types.
