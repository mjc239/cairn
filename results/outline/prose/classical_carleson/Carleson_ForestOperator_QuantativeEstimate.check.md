You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `TileStructure.Forest.density_tree_bound2`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (h2f : Function.support f ⊆ F) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_3_1_2 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * dens₂ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
English: (Lemma 7.3.1, second part) Let $f,g$ be bounded with compact support, with $\operatorname{supp} f\subseteq F$ and $\operatorname{supp} g\subseteq G$, and let $u\in t$. Then $$\Big\|\int_X\overline{g(x)}\,T_{\mathfrak T(u)}f(x)\,dx\Big\|\le C_{7.3.1.2}(a)\,\mathrm{dens}_1(\mathfrak T(u))^{1/2}\,\mathrm{dens}_2(\mathfrak T(u))^{1/2}\,\|f\|_{L^2}\,\|g\|_{L^2}.$$

### `TileStructure.Forest.density_tree_bound1`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
English: (Lemma 7.3.1, first part) Let $f,g$ be bounded with compact support, with $\operatorname{supp} g\subseteq G$, and let $u\in t$. Then $$\Big\|\int_X\overline{g(x)}\,T_{\mathfrak T(u)}f(x)\,dx\Big\|\le C_{7.3.1.1}(a)\,\mathrm{dens}_1(\mathfrak T(u))^{1/2}\,\|f\|_{L^2}\,\|g\|_{L^2}.$$

### `TileStructure.Forest.local_dens1_tree_bound`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) : volume (↑L ∩ G ∩ ⋃ p ∈ (fun x => t.𝔗 x) u, E p) ≤ ↑(Forest.C7_3_2 a) * dens₁ ((fun x => t.𝔗 x) u) * volume ↑L`
English: (Lemma 7.3.2) Let $u\in t$ and $L\in\mathcal L(\mathfrak T(u))$. Then $$\mu\Big(L\cap G\cap\bigcup_{\mathfrak p\in\mathfrak T(u)}E(\mathfrak p)\Big)\le C_{7.3.2}(a)\,\mathrm{dens}_1(\mathfrak T(u))\,\mu(L).$$
