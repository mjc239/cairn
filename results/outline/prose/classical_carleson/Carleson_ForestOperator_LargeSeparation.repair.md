You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Keep every
hypothesis the Lean shows, including instance assumptions such as `[Finite G]` or `[IsProbabilityMeasure μ]`
(say them in words: "$G$ is finite", "$\mu$ is a probability measure"), and the exact conclusion. Do not add
claims the Lean does not make. Purely structural instances (e.g. `[AddCommGroup G]`) and implicit arguments are not
shown and may stay implicit.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): TileStructure, MeasureTheory, Antichain.

### `TileStructure.Forest.global_tree_control1_edist_part1`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ t) (hℭ : ℭ ⊆ (fun x => t.𝔗 x) u) (hf : BoundedCompactSupport f volume) (hs : ∀ p ∈ ℭ, ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) → s J ≤ 𝔰 p) (hx : x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) (hx' : x' ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) : edist (Complex.exp (Complex.I * ↑((𝒬 u) x)) * adjointCarlesonSum ℭ f x) (Complex.exp (Complex.I * ↑((𝒬 u) x')) * adjointCarlesonSum ℭ f x') ≤ ↑(Forest.C7_5_5 a) * 2 ^ (4 * a) * edist x x' ^ (↑a)⁻¹ * ∑ k ∈ Finset.Icc (s J) ↑(defaultS X), ↑(defaultD a) ^ (-↑k / ↑a) * ⨍⁻ (x : X) in Metric.ball (c J) (32 * ↑(defaultD a) ^ k), ‖f x‖ₑ ∂volume`
Docstring: Part 1 of equation (7.5.18) of Lemma 7.5.9.
Previous English: (Part 1 of (7.5.18) in Lemma 7.5.9) Let $t$ be a forest, $u \in t$, $\mathfrak{C} \subseteq \mathfrak{T}(u)$, $f$ bounded with compact support, and suppose that every $p \in \mathfrak{C}$ with $B(c(p), 8D^{s(p)}) \cap B(c(J), 16 D^{s(J)}) \ne \emptyset$ satisfies $s(J) \le s(p)$. Then for $x, x' \in B(c(J), 16D^{s(J)})$, $$\big|e^{i\mathcal{Q}(u)(x)} T^*_{\mathfrak{C}} f(x) - e^{i\mathcal{Q}(u)(x')} T^*_{\mathfrak{C}} f(x')\big| \le C_{7.5.5}(a)\, 2^{4a}\, d(x,x')^{1/a} \sum_{k = s(J)}^{S} D^{-k/a}\, ⨍ \cdots,$$ where $S$ = `defaultS X` and the last factor is a lower average (the remainder of the Lean statement is truncated in the source).
Checker's issue: The English claims the Lean statement is truncated, but it is complete, and the English omits the final factor: the lower average of ‖f‖ over the ball B(c(J), 32 D^k).

### `TileStructure.Forest.global_tree_control1_edist_part2`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ t) (hℭ : ℭ ⊆ (fun x => t.𝔗 x) u) (hf : BoundedCompactSupport f volume) (hs : ∀ p ∈ ℭ, ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) → s J ≤ 𝔰 p) (hx : x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) (hx' : x' ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) : edist (Complex.exp (Complex.I * ↑((𝒬 u) x)) * adjointCarlesonSum ℭ f x) (Complex.exp (Complex.I * ↑((𝒬 u) x')) * adjointCarlesonSum ℭ f x') ≤ ↑(Forest.C7_5_9d a) * (edist x x' / ↑(defaultD a) ^ s J) ^ (↑a)⁻¹ * ⨅ x ∈ J, maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f x`
Docstring: Part 2 of equation (7.5.18) of Lemma 7.5.9.
Previous English: (Part 2 of (7.5.18) in Lemma 7.5.9) Under the same hypotheses as part 1 (a forest $t$, $u \in t$, $\mathfrak{C} \subseteq \mathfrak{T}(u)$, $f$ bounded with compact support, every $p \in \mathfrak{C}$ with $B(c(p), 8D^{s(p)}) \cap B(c(J), 16 D^{s(J)}) \ne \emptyset$ has $s(J) \le s(p)$, and $x, x' \in B(c(J), 16D^{s(J)})$), $$\big|e^{i\mathcal{Q}(u)(x)} T^*_{\mathfrak{C}} f(x) - e^{i\mathcal{Q}(u)(x')} T^*_{\mathfrak{C}} f(x')\big| \le C_{7.5.9d}(a) \Big(\frac{d(x,x')}{D^{s(J)}}\Big)^{1/a} \inf_{y \in J} M_{\mathcal{B}} \cdots,$$ where $M_{\mathcal{B}}$ is the maximal function over the ball family `Forest.𝓑` (centres `Forest.c𝓑`, radii `Forest.r𝓑`) and $C_{7.5.9d}$ is `Forest.C7_5_9d` (the end of the Lean statement is truncated in the source).
Checker's issue: The English claims the Lean statement is truncated, but it is complete, and the English leaves the final factor as 'M_B ⋯' instead of stating inf over x ∈ J of the maximal function M_B (exponent 1) of f at x.
