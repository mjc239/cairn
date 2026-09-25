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

### `TileStructure.Forest.density_tree_bound2`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (h2f : Function.support f ⊆ F) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_3_1_2 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * dens₂ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {n : ℕ} {t : Forest X n} {u : 𝔓 X} {f g : X → ℂ}, BoundedCompactSupport f volume → Function.support f ⊆ F → BoundedCompactSupport g volume → Function.support g ⊆ G → u ∈ t → ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_3_1_2 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * dens₂ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Docstring: Second part of Lemma 7.3.1.
Previous English: (Lemma 7.3.1, second part) Let $f,g$ be bounded with compact support, with $\operatorname{supp} f\subseteq F$ and $\operatorname{supp} g\subseteq G$, and let $u\in t$. Then $$\Big\|\int_X\overline{g(x)}\,T_{\mathfrak T(u)}f(x)\,dx\Big\|\le C_{7.3.1.2}(a)\,\mathrm{dens}_1(\mathfrak T(u))^{1/2}\,\mathrm{dens}_2(\mathfrak T(u))^{1/2}\,\|f\|_{L^2}\,\|g\|_{L^2}.$$
Checker's issue: Omits the standing assumptions (metric space X, ProofData and TileStructure instances) under which the statement is proved.

### `TileStructure.Forest.density_tree_bound1`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {n : ℕ} {t : Forest X n} {u : 𝔓 X} {f g : X → ℂ}, BoundedCompactSupport f volume → BoundedCompactSupport g volume → Function.support g ⊆ G → u ∈ t → ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Docstring: First part of Lemma 7.3.1.
Previous English: (Lemma 7.3.1, first part) Let $f,g$ be bounded with compact support, with $\operatorname{supp} g\subseteq G$, and let $u\in t$. Then $$\Big\|\int_X\overline{g(x)}\,T_{\mathfrak T(u)}f(x)\,dx\Big\|\le C_{7.3.1.1}(a)\,\mathrm{dens}_1(\mathfrak T(u))^{1/2}\,\|f\|_{L^2}\,\|g\|_{L^2}.$$
Checker's issue: Omits the standing assumptions (metric space X, ProofData and TileStructure instances) under which the statement is proved.

### `TileStructure.Forest.local_dens1_tree_bound`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) : volume (↑L ∩ G ∩ ⋃ p ∈ (fun x => t.𝔗 x) u, E p) ≤ ↑(Forest.C7_3_2 a) * dens₁ ((fun x => t.𝔗 x) u) * volume ↑L`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {n : ℕ} {t : Forest X n} {u : 𝔓 X} {L : Grid X}, u ∈ t → L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u) → volume (↑L ∩ G ∩ ⋃ p ∈ (fun x => t.𝔗 x) u, E p) ≤ ↑(Forest.C7_3_2 a) * dens₁ ((fun x => t.𝔗 x) u) * volume ↑L`
Docstring: Lemma 7.3.2.
Previous English: (Lemma 7.3.2) Let $u\in t$ and $L\in\mathcal L(\mathfrak T(u))$. Then $$\mu\Big(L\cap G\cap\bigcup_{\mathfrak p\in\mathfrak T(u)}E(\mathfrak p)\Big)\le C_{7.3.2}(a)\,\mathrm{dens}_1(\mathfrak T(u))\,\mu(L).$$
Checker's issue: Omits the standing assumptions (metric space X, ProofData and TileStructure instances) under which the statement is proved.
