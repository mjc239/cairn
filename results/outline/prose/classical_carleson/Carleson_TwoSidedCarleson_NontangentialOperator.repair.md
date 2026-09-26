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

### `nontangential_from_simple`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) : HasBoundedStrongType (nontangentialOperator K) 2 2 volume volume ↑(C10_0_2 a)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {K : X → X → ℂ} [IsTwoSidedKernel a K], 4 ≤ a → (∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) → HasBoundedStrongType (nontangentialOperator K) 2 2 volume volume ↑(C10_0_2 a)`
Docstring: Lemma 10.0.2. The formal statement includes the measurability of the operator.
Previous English: (Lemma 10.0.2.) Let $a \ge 4$ and suppose that for every $r > 0$, $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$. Then the nontangential operator $\mathrm{nontangentialOperator}(K)$ has bounded strong type $(2,2)$ with constant $C_{10.0.2}(a)$ (including measurability of the operator).
Checker's issue: Omits the standing assumptions that X is a metric space with a doubling measure (DoublingMeasure X (defaultA a)) and that K is a two-sided Calderon-Zygmund kernel (IsTwoSidedKernel a K).

### `cotlar_estimate`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hg : BoundedFiniteSupport g volume) (hr : r ∈ Set.Ioc 0 R) : ‖czOperator K R g x‖ₑ ≤ 4 * globalMaximalFunction volume 1 (czOperator K r g) x + ↑(C10_1_5 a) * globalMaximalFunction volume 1 g x`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r R : ℝ} {K : X → X → ℂ} {x : X} [IsTwoSidedKernel a K], 4 ≤ a → (∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) → ∀ {g : X → ℂ}, BoundedFiniteSupport g volume → r ∈ Set.Ioc 0 R → ‖czOperator K R g x‖ₑ ≤ 4 * globalMaximalFunction volume 1 (czOperator K r g) x + ↑(C10_1_5 a) * globalMaximalFunction volume 1 g x`
Docstring: Lemma 10.1.5
Previous English: (Lemma 10.1.5, Cotlar's estimate.) Let $a \ge 4$, suppose $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$ for every $r > 0$, let $g$ be bounded with finite-measure support, and $r \in (0, R]$. Then $\|\mathrm{czOperator}(K, R)\, g(x)\| \le 4\, M(\mathrm{czOperator}(K, r)\, g)(x) + C_{10.1.5}(a)\, M g(x)$, where $M = \mathrm{globalMaximalFunction}(\mathrm{vol}, 1)$.
Checker's issue: Omits the standing assumptions that X is a metric space with a doubling measure (DoublingMeasure X (defaultA a)) and that K is a two-sided Calderon-Zygmund kernel (IsTwoSidedKernel a K).

### `cotlar_set_F₂`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hr : 0 < r) (hR : r ≤ R) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hg : BoundedFiniteSupport g volume) : (volume.restrict (Metric.ball x (R / 4))) {x' | ↑(C10_1_4 a) * globalMaximalFunction volume 1 g x < ‖czOperator K r ((Metric.ball x (R / 2)).indicator g) x'‖ₑ} ≤ volume (Metric.ball x (R / 4)) / 4`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r R : ℝ} {K : X → X → ℂ} {x : X} [IsTwoSidedKernel a K], 4 ≤ a → 0 < r → r ≤ R → (∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) → ∀ {g : X → ℂ}, BoundedFiniteSupport g volume → (volume.restrict (Metric.ball x (R / 4))) {x' | ↑(C10_1_4 a) * globalMaximalFunction volume 1 g x < ‖czOperator K r ((Metric.ball x (R / 2)).indicator g) x'‖ₑ} ≤ volume (Metric.ball x (R / 4)) / 4`
Docstring: Part 2 of Lemma 10.1.4 about `F₂`.
Previous English: (Lemma 10.1.4, part about $F_2$.) Let $a \ge 4$, $0 < r \le R$, suppose $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$ for every $r > 0$, and let $g$ be bounded with finite-measure support. Then $\mathrm{vol}\big(B(x, R/4) \cap \{x' : C_{10.1.4}(a)\, M g(x) < \|\mathrm{czOperator}(K, r)(\mathbf{1}_{B(x, R/2)} g)(x')\|\}\big) \le \mathrm{vol}(B(x, R/4))/4$, where $M = \mathrm{globalMaximalFunction}(\mathrm{vol}, 1)$.
Checker's issue: Omits the standing assumptions that X is a metric space with a doubling measure (DoublingMeasure X (defaultA a)) and that K is a two-sided Calderon-Zygmund kernel (IsTwoSidedKernel a K).

### `simple_nontangential_operator`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hr : 0 < r) : HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r : ℝ} {K : X → X → ℂ} [IsTwoSidedKernel a K], 4 ≤ a → (∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) → 0 < r → HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
Docstring: Lemma 10.1.6. The formal statement includes the measurability of the operator. See also `simple_nontangential_operator_le`
Previous English: (Lemma 10.1.6.) Let $a \ge 4$, suppose $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$ for every $r > 0$, and let $r > 0$. Then $\mathrm{simpleNontangentialOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{10.1.6}(a)$ (including measurability of the operator).
Checker's issue: Omits the standing assumptions that X is a metric space with a doubling measure (DoublingMeasure X (defaultA a)) and that K is a two-sided Calderon-Zygmund kernel (IsTwoSidedKernel a K).

### `simple_nontangential_operator_le`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hr : 0 ≤ r) : HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r : ℝ} {K : X → X → ℂ} [IsTwoSidedKernel a K], 4 ≤ a → (∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) → 0 ≤ r → HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
Docstring: This is the first step of the proof of Lemma 10.0.2, and should follow from 10.1.6 + monotone convergence theorem. (measurability should be proven without any restriction on `r`.)
Previous English: Let $a \ge 4$, suppose $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$ for every $r > 0$, and let $r \ge 0$. Then $\mathrm{simpleNontangentialOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{10.1.6}(a)$.
Checker's issue: Omits the standing assumptions that X is a metric space with a doubling measure (DoublingMeasure X (defaultA a)) and that K is a two-sided Calderon-Zygmund kernel (IsTwoSidedKernel a K).
