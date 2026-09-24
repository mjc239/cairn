You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `Tile.correlation_le`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hle : 𝔰 p' ≤ 𝔰 p) (hg : Measurable g) (hg1 : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (y : X), adjointCarleson p' g y * (starRingEnd ℂ) (adjointCarleson p g y)‖ₑ ≤ (↑(Tile.C6_1_5 a) * (1 + edist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / 4} (𝒬 p') (𝒬 p)) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) / volume ↑(𝓘 p) * ∫⁻ (y : X) in E p', ‖g y‖ₑ) * ∫⁻ (y : X) in E p, ‖g y‖ₑ`
English: (Lemma 6.1.5, part 1, eq. (6.1.43).) Let $p, p' \in \mathfrak{P}(X)$ be tiles with $s(p') \le s(p)$, and let $g : X \to \mathbb{C}$ be measurable with $\|g(x)\| \le \mathbf{1}_G(x)$ for all $x$. Then
$$\Big| \int_X T_{p'}^* g(y)\, \overline{T_p^* g(y)}\,dy \Big| \le \frac{C_{6.1.5}(a)\,\big(1 + d_{\mathfrak{c}(p'),\, D^{s(p')}/4}(\mathcal{Q}(p'), \mathcal{Q}(p))\big)^{-1/(2a^2 + a^3)}}{\mu(I(p))} \int_{E(p')} |g| \int_{E(p)} |g|,$$
where $T_p^*$ is `adjointCarleson p`, $D$ = `defaultD a`, $I(p)$ is the grid cube of $p$, and $d_{c, r}$ denotes the distance `edist_{c, r}` on the frequency functions.

### `Tile.I12_le`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (ha : 4 ≤ a) (hle : 𝔰 p' ≤ 𝔰 p) (hinter : (Metric.ball (𝔠 p') (5 * ↑(defaultD a) ^ 𝔰 p') ∩ Metric.ball (𝔠 p) (5 * ↑(defaultD a) ^ 𝔰 p)).Nonempty) (x1 : ↑(E p')) (x2 : ↑(E p)) : Tile.I12 p p' g ↑x1 ↑x2 ≤ 2 ^ ((2 * 𝕔 + 6 + 𝕔 / 4) * a ^ 3 + 8 * a + 1) * (1 + edist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / 4} (𝒬 p') (𝒬 p)) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) / volume (Metric.ball (↑x2) (↑(defaultD a) ^ 𝔰 p)) * ‖g ↑x1‖ₑ * ‖g ↑x2‖ₑ`
English: (Inequality (6.2.29).) Assume $a \ge 4$, $s(p') \le s(p)$, and that $B(\mathfrak{c}(p'), 5D^{s(p')}) \cap B(\mathfrak{c}(p), 5D^{s(p)})$ is nonempty, where $D$ = `defaultD a`. Then for all $x_1 \in E(p')$ and $x_2 \in E(p)$,
$$I_{12}(p, p', g)(x_1, x_2) \le \frac{2^{(2\mathfrak{c} + 6 + \mathfrak{c}/4)a^3 + 8a + 1}\,\big(1 + d_{\mathfrak{c}(p'),\, D^{s(p')}/4}(\mathcal{Q}(p'), \mathcal{Q}(p))\big)^{-1/(2a^2 + a^3)}}{\mu(B(x_2, D^{s(p)}))}\, |g(x_1)|\, |g(x_2)|,$$
where $I_{12}$ is `Tile.I12` and $\mathfrak{c}$ (in the exponent) is the constant `𝕔` (with natural-number division $\mathfrak{c}/4$).

### `Tile.I12_le'`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hle : 𝔰 p' ≤ 𝔰 p) (x1 : ↑(E p')) (x2 : ↑(E p)) : Tile.I12 p p' g ↑x1 ↑x2 ≤ 2 ^ ((2 * 𝕔 + 6 + 𝕔 / 4) * a ^ 3 + 8 * a) * (1 + edist_{↑x1, ↑(defaultD a) ^ 𝔰 p'} (Q ↑x1) (Q ↑x2)) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) / volume (Metric.ball (↑x2) (↑(defaultD a) ^ 𝔰 p)) * ‖g ↑x1‖ₑ * ‖g ↑x2‖ₑ`
English: (Inequality (6.2.28).) Assume $s(p') \le s(p)$. Then for all $x_1 \in E(p')$ and $x_2 \in E(p)$,
$$I_{12}(p, p', g)(x_1, x_2) \le \frac{2^{(2\mathfrak{c} + 6 + \mathfrak{c}/4)a^3 + 8a}\,\big(1 + d_{x_1,\, D^{s(p')}}(Q(x_1), Q(x_2))\big)^{-1/(2a^2 + a^3)}}{\mu(B(x_2, D^{s(p)}))}\, |g(x_1)|\, |g(x_2)|,$$
where $I_{12}$ is `Tile.I12`, $D$ = `defaultD a`, and $\mathfrak{c}$ (in the exponent) is the constant `𝕔`.

### `Tile.correlation_le_of_nonempty_inter`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (ha : 4 ≤ a) (hle : 𝔰 p' ≤ 𝔰 p) (hg : Measurable g) (hg1 : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) (hinter : (Metric.ball (𝔠 p') (5 * ↑(defaultD a) ^ 𝔰 p') ∩ Metric.ball (𝔠 p) (5 * ↑(defaultD a) ^ 𝔰 p)).Nonempty) : ‖∫ (y : X), adjointCarleson p' g y * (starRingEnd ℂ) (adjointCarleson p g y)‖ₑ ≤ (↑(Tile.C6_1_5 a) * (1 + edist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / 4} (𝒬 p') (𝒬 p)) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) / volume ↑(𝓘 p) * ∫⁻ (y : X) in E p', ‖g y‖ₑ) * ∫⁻ (y : X) in E p, ‖g y‖ₑ`
English: Assume $a \ge 4$ and $s(p') \le s(p)$, let $g : X \to \mathbb{C}$ be measurable with $\|g(x)\| \le \mathbf{1}_G(x)$ for all $x$, and assume $B(\mathfrak{c}(p'), 5D^{s(p')}) \cap B(\mathfrak{c}(p), 5D^{s(p)})$ is nonempty, where $D$ = `defaultD a`. Then
$$\Big| \int_X T_{p'}^* g(y)\, \overline{T_p^* g(y)}\,dy \Big| \le \frac{C_{6.1.5}(a)\,\big(1 + d_{\mathfrak{c}(p'),\, D^{s(p')}/4}(\mathcal{Q}(p'), \mathcal{Q}(p))\big)^{-1/(2a^2 + a^3)}}{\mu(I(p))} \int_{E(p')} |g| \int_{E(p)} |g|.$$
