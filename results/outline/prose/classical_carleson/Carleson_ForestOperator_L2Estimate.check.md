You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `TileStructure.Forest.tree_projection_estimate`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_2_1 a) * eLpNorm (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) fun x => ‖f x‖) 2 volume * eLpNorm (Forest.approxOnCube (Forest.𝓛 ((fun x => t.𝔗 x) u)) fun x => ‖g x‖) 2 volume`
English: (Lemma 7.2.1) Let $t$ be a forest, $u \in t$, and let $f, g$ be bounded with compact support. Then $$\Big|\int_X \overline{g(x)}\, \mathrm{carlesonSum}(\mathfrak{T}(u), f)(x)\,dx\Big| \le C_{7.2.1}(a)\, \big\|P_{\mathcal{J}(\mathfrak{T}(u))} |f|\big\|_{L^2}\, \big\|P_{\mathcal{L}(\mathfrak{T}(u))} |g|\big\|_{L^2},$$ where $P_{\mathcal{C}} h$ denotes `approxOnCube` $\mathcal{C}$ $h$ (the approximation of $h$ by its averages on the cubes of the collection $\mathcal{C}$), $\mathcal{J}$ and $\mathcal{L}$ are the cube collections `Forest.𝓙` and `Forest.𝓛`, and $C_{7.2.1}$ is `Forest.C7_2_1`.

### `TileStructure.Forest.eLpNorm_MB_le`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) : eLpNorm (maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f) 2 volume ≤ ↑(CMB (↑(defaultA a)) 2) * eLpNorm f 2 volume`
English: For $f$ bounded with compact support, the maximal function $M_{\mathcal{B}}$ associated with the ball family $\mathcal{B}$ = `Forest.𝓑`, centres `Forest.c𝓑` and radii `Forest.r𝓑` (with exponent $1$) satisfies $$\|M_{\mathcal{B}} f\|_{L^2} \le C_{M}(A, 2)\, \|f\|_{L^2},$$ where $A$ = `defaultA a` and $C_M$ is `CMB`.

### `TileStructure.Forest.boundary_operator_bound`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) : eLpNorm (t.boundaryOperator u f) 2 volume ≤ ↑(Forest.C7_2_3 a) * eLpNorm f 2 volume`
English: (Lemma 7.2.3) For a forest $t$, a tile $u$, and $f$ bounded with compact support, $$\|\mathrm{boundaryOperator}_t(u, f)\|_{L^2} \le C_{7.2.3}(a)\, \|f\|_{L^2},$$ where $C_{7.2.3}$ is `Forest.C7_2_3`.

### `TileStructure.Forest.nontangential_operator_bound`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (θ : Θ X) : eLpNorm (Forest.nontangentialMaximalFunction θ f) 2 volume ≤ ↑(Forest.C7_2_2 a) * eLpNorm f 2 volume`
English: (Lemma 7.2.2) For $f$ bounded with compact support and $\theta \in \Theta(X)$, the nontangential maximal function satisfies $$\|T^{\theta}_{\mathrm{nt}} f\|_{L^2} \le C_{7.2.2}(a)\, \|f\|_{L^2},$$ where $T^{\theta}_{\mathrm{nt}}$ is `Forest.nontangentialMaximalFunction θ` and $C_{7.2.2}$ is `Forest.C7_2_2`.
