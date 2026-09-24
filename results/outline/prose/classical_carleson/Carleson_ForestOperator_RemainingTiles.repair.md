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

### `TileStructure.Forest.e764_preCS`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf : BoundedCompactSupport f volume) : eLpNorm (Forest.approxOnCube (t.𝓙₆ u₁) fun x => ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) f x‖) 2 volume ≤ ↑(C2_1_3 a) * 2 ^ (4 * a) * ∑ k ∈ Finset.Icc ⌊Forest.C7_6_3 a n⌋ (2 * ↑(defaultS X)), (∑ J ∈ (t.𝓙₆ u₁).toFinset, (volume ↑J)⁻¹ * (∑ I with s I = s J - k ∧ Disjoint ↑I ↑(𝓘 u₁) ∧ ¬Disjoint (↑J) (Metric.ball (c I) (8 * ↑(defaultD a) ^ s I)), ∫⁻ (y : X) in ↑J, (Metric.ball (c I) (8 * ↑(defaultD a) ^ s I)).indicator 1 y * maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f y) ^ 2) ^ 2⁻¹`
Docstring: Equation (7.6.4) of Lemma 7.6.2 (before applying Cauchy–Schwarz).
Previous English: (Equation (7.6.4) of Lemma 7.6.2, before Cauchy–Schwarz) Let $u_1,u_2\in t$ with $u_1\ne u_2$ and $\mathcal I(u_1)\le\mathcal I(u_2)$, and let $f$ be bounded with compact support. Then $\big\|P_{\mathcal J_6(u_1)}|T^*_{\mathfrak T(u_2)\setminus\mathfrak S_0(u_1,u_2)}f|\big\|_{L^2}$ is at most $$C_{2.1.3}(a)\,2^{4a}\sum_{k=\lfloor C_{7.6.3}(a,n)\rfloor}^{2S}\Bigg(\sum_{J\in\mathcal J_6(u_1)}\mu(J)^{-1}\Big(\sum_{I}\int_J\mathbf 1_{B(c(I),8D^{s(I)})}(y)\,M_{\mathcal B}f\cdots\Big)\cdots\Bigg)\cdots,$$ where $I$ ranges over cubes with $s(I)=s(J)-k$, $I$ disjoint from $\mathcal I(u_1)$, and $J$ meeting $B(c(I),8D^{s(I)})$; $M_{\mathcal B}$ is the maximal function (exponent 1) over the balls $\mathcal B$. (The remainder of the Lean statement is truncated in the source.)
Checker's issue: The English claims the Lean statement is truncated and elides the end of the bound (the square of the inner sum over I and the outer square root), although the Lean shown is complete.
