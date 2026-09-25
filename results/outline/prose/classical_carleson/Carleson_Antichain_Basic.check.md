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
be supported by the docstring or the Lean. So is a formula or description of what a defined object is: when the
prompt shows neither its definition nor a docstring saying it, the English must not supply one. Every variable
needs its type ("$f : G \to \mathbb{C}$", "$m$ a natural number"), every symbol must be introduced (notation such
as $M_{\mathcal B}$ included), and no letter may mean two things. When in doubt, flag it: a false alarm costs one
repair, a missed error stays in the outline. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `dens2_antichain`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (hfF : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hf : Measurable f) (hgG : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) (hg : Measurable g) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum 𝔄 f x‖ₑ ≤ ↑(C6_1_3 a (nnq X)) * dens₂ 𝔄 ^ ((2 * ↑(nnq X) / (↑(nnq X) + 1))⁻¹ - 2⁻¹) * eLpNorm f 2 volume * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {𝔄 : Set (𝔓 X)}, IsAntichain (fun (x1 x2 : 𝔓 X) => x1 ≤ x2) 𝔄 → ∀ {f : X → ℂ}, (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → Measurable f → ∀ {g : X → ℂ}, (∀ (x : X), ‖g x‖ ≤ G.indicator (1 : X → ℝ) x) → Measurable g → enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => HMul.hMul (α := ℂ) ((starRingEnd ℂ) (g x) : ℂ) (carlesonSum (F := F) (G := G) 𝔄 f x)) ≤ ↑(C6_1_3 a (nnq X (F := F) (G := G))) * dens₂ (F := F) (G := G) 𝔄 ^ (((2 : ℝ) * ↑(nnq X (F := F) (G := G)) / (↑(nnq X (F := F) (G := G)) + (1 : ℝ)))⁻¹ - (2 : ℝ)⁻¹) * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f (2 : ENNReal) volume * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace g (2 : ENNReal) volume`
Docstring: Lemma 6.1.3 (inequality 6.1.11).
English: Under the standing assumptions of the proof (the data $a\in\mathbb N$, $q$, $K$, $\sigma_1$, $\sigma_2$, $F$, $G$ of `ProofData` on the metric space $X$, which is then a doubling metric measure space, and a tile structure `TileStructure` on $X$ with the default parameters $D(a)$, $\kappa(a)$, $S(X)$), (Lemma 6.1.3, inequality (6.1.11).) let $\mathfrak{A} \subseteq \mathfrak{P}(X)$ be an antichain with respect to the order $\le$ on tiles. Let $f, g : X \to \mathbb{C}$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ and $\|g(x)\| \le \mathbf{1}_G(x)$ for all $x \in X$. Then, writing $q$ for `nnq X` (the parameter $q$ as a nonnegative real), $$\Big| \int_X \overline{g(x)}\, T_{\mathfrak{A}} f(x)\,dx \Big| \le C_{6.1.3}(a, q)\, \operatorname{dens}_2(\mathfrak{A})^{\frac{q+1}{2q} - \frac12}\, \|f\|_{L^2}\, \|g\|_{L^2},$$ where $T_{\mathfrak{A}} f = \sum_{p \in \mathfrak{A}} T_p f$ is the Carleson sum `carlesonSum 𝔄 f`.

### `Lemma6_1_3.eLpNorm_𝓜p_le`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔄 : Set (𝔓 X)) (hf : MemLp f 2 volume) : eLpNorm (Lemma6_1_3.𝓜p 𝔄 (Lemma6_1_3.p X) f) 2 volume ≤ ↑(C2_0_6 (↑(defaultA a)) (Lemma6_1_3.p X).toNNReal 2) * eLpNorm f 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔄 : Set (𝔓 X)) {f : X → ℂ}, MemLp (m0 := MeasureSpace.toMeasurableSpace) f (2 : ENNReal) volume → @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace (Lemma6_1_3.𝓜p (F := F) (G := G) 𝔄 (Lemma6_1_3.p X (F := F) (G := G)) f) (2 : ENNReal) volume ≤ ↑(C2_0_6 (↑(defaultA a)) Lemma6_1_3.p X (F := F) (G := G).toNNReal (2 : NNReal)) * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f (2 : ENNReal) volume`
Docstring: Maximal function bound needed in the proof
English: Under the standing assumptions of the proof (the data $a\in\mathbb N$, $q$, $K$, $\sigma_1$, $\sigma_2$, $F$, $G$ of `ProofData` on the metric space $X$, which is then a doubling metric measure space, and a tile structure `TileStructure` on $X$ with the default parameters $D(a)$, $\kappa(a)$, $S(X)$), (maximal function bound used in the proof of Lemma 6.1.3) for every set of tiles $\mathfrak{A} \subseteq \mathfrak{P}(X)$ and every $f : X\to\mathbb C$ in $L^2(X)$, with $p$ = `Lemma6_1_3.p X`, the maximal operator $\mathcal{M}_{\mathfrak{A}, p}$ = `Lemma6_1_3.𝓜p 𝔄 p` satisfies $\|\mathcal{M}_{\mathfrak{A}, p} f\|_{L^2} \le C_{2.0.6}(A, p, 2)\, \|f\|_{L^2}$, where $A$ = `defaultA a`.
