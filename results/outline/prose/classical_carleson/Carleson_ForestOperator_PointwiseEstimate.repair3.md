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

### `TileStructure.Forest.first_tree_pointwise`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) (hx : x ∈ L) (hx' : x' ∈ L) (hf : BoundedCompactSupport f volume) : ‖∑ i ∈ t.σ u x, ∫ (y : X), (Complex.exp (Complex.I * (-↑((𝒬 u) y) + ↑((Q x) y) + ↑((𝒬 u) x) - ↑((Q x) x))) - 1) * Ks i x y * f y‖ₑ ≤ ↑(Forest.C7_1_4 a) * maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) fun x => ‖f x‖) x'`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u : 𝔓 X} {x x' : X} {f : X → ℂ} {L : Grid X}, u ∈ t → Membership.mem (γ := Set (Grid X)) (Forest.𝓛 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) L → x ∈ L → x' ∈ L → BoundedCompactSupport f volume → enorm (E := ℂ) (∑ i ∈ t.σ (F := F) (G := G) u x, @integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => (Complex.exp (Complex.I * (-↑((𝒬 u) y) + ↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y) + ↑((𝒬 u) x) - ↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) x))) - (1 : ℂ)) * Ks i x y * f y) ≤ ↑(Forest.C7_1_4 a) * maximalFunction (ε := ℝ) volume (Forest.𝓑 (F := F) (G := G)) (Forest.c𝓑 (F := F) (G := G)) (Forest.r𝓑 (F := F) (G := G)) (1 : ℝ) (Forest.approxOnCube (F := F) (G := G) (Forest.𝓙 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) fun x => ‖f x‖) x'`
Docstring: Lemma 7.1.4
Previous English: Let $X$ be a metric space and work under the standing assumptions of the proof: the data $a\in\mathbb N$, $q\in\mathbb R$, $K:X\times X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$, $F,G\subseteq X$ of `ProofData` (making $X$ a doubling metric measure space with measure $\mu$), together with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)` with set of tiles $\mathfrak P(X)$ and grid cubes $\mathrm{Grid}(X)$. Let $n\in\mathbb N$, let $t$ be an $n$-forest, and let $f:X\to\mathbb C$. (Lemma 7.1.4) Let $u\in t$, let $L\in\mathrm{Grid}(X)$ with $L\in\mathcal L(\mathfrak T(u))$, and let $x,x'\in L$, and let $f$ be bounded with compact support. Then $$\Big\|\sum_{i\in\sigma(u,x)}\int_X\Big(e^{i(-\mathcal Q(u)(y)+Q(x)(y)+\mathcal Q(u)(x)-Q(x)(x))}-1\Big)K_i(x,y)f(y)\,d\mu(y)\Big\|\le C_{7.1.4}(a)\,M_{\mathcal B}\big(P_{\mathcal J(\mathfrak T(u))}|f|\big)(x'),$$ where $\sigma(u,x)$ is the set of scales $t.\sigma(u,x)$, $K_i$ are the kernel pieces, $P_{\mathcal J}$ is `approxOnCube` and $M_{\mathcal B}$ is the maximal function with respect to $\mu$ (exponent $1$) over the balls $\mathcal B$ with centers $c_{\mathcal B}$ and radii $r_{\mathcal B}$.
Checker's issue: The letter i is used both as the imaginary unit and as a summation index; rename the index.
