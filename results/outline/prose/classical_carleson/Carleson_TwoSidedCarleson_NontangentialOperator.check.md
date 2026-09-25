You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption) and the English. Compare the English with the full statement.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `nontangential_from_simple`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) : HasBoundedStrongType (nontangentialOperator K) 2 2 volume volume ↑(C10_0_2 a)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {K : X → X → ℂ} [IsTwoSidedKernel a K], 4 ≤ a → (∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) → HasBoundedStrongType (nontangentialOperator K) 2 2 volume volume ↑(C10_0_2 a)`
English: (Lemma 10.0.2.) Let $a \ge 4$ and suppose that for every $r > 0$, $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$. Then the nontangential operator $\mathrm{nontangentialOperator}(K)$ has bounded strong type $(2,2)$ with constant $C_{10.0.2}(a)$ (including measurability of the operator).

### `cotlar_estimate`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hg : BoundedFiniteSupport g volume) (hr : r ∈ Set.Ioc 0 R) : ‖czOperator K R g x‖ₑ ≤ 4 * globalMaximalFunction volume 1 (czOperator K r g) x + ↑(C10_1_5 a) * globalMaximalFunction volume 1 g x`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r R : ℝ} {K : X → X → ℂ} {x : X} [IsTwoSidedKernel a K], 4 ≤ a → (∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) → ∀ {g : X → ℂ}, BoundedFiniteSupport g volume → r ∈ Set.Ioc 0 R → ‖czOperator K R g x‖ₑ ≤ 4 * globalMaximalFunction volume 1 (czOperator K r g) x + ↑(C10_1_5 a) * globalMaximalFunction volume 1 g x`
English: (Lemma 10.1.5, Cotlar's estimate.) Let $a \ge 4$, suppose $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$ for every $r > 0$, let $g$ be bounded with finite-measure support, and $r \in (0, R]$. Then $\|\mathrm{czOperator}(K, R)\, g(x)\| \le 4\, M(\mathrm{czOperator}(K, r)\, g)(x) + C_{10.1.5}(a)\, M g(x)$, where $M = \mathrm{globalMaximalFunction}(\mathrm{vol}, 1)$.

### `cotlar_set_F₂`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hr : 0 < r) (hR : r ≤ R) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hg : BoundedFiniteSupport g volume) : (volume.restrict (Metric.ball x (R / 4))) {x' | ↑(C10_1_4 a) * globalMaximalFunction volume 1 g x < ‖czOperator K r ((Metric.ball x (R / 2)).indicator g) x'‖ₑ} ≤ volume (Metric.ball x (R / 4)) / 4`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r R : ℝ} {K : X → X → ℂ} {x : X} [IsTwoSidedKernel a K], 4 ≤ a → 0 < r → r ≤ R → (∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) → ∀ {g : X → ℂ}, BoundedFiniteSupport g volume → (volume.restrict (Metric.ball x (R / 4))) {x' | ↑(C10_1_4 a) * globalMaximalFunction volume 1 g x < ‖czOperator K r ((Metric.ball x (R / 2)).indicator g) x'‖ₑ} ≤ volume (Metric.ball x (R / 4)) / 4`
English: (Lemma 10.1.4, part about $F_2$.) Let $a \ge 4$, $0 < r \le R$, suppose $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$ for every $r > 0$, and let $g$ be bounded with finite-measure support. Then $\mathrm{vol}\big(B(x, R/4) \cap \{x' : C_{10.1.4}(a)\, M g(x) < \|\mathrm{czOperator}(K, r)(\mathbf{1}_{B(x, R/2)} g)(x')\|\}\big) \le \mathrm{vol}(B(x, R/4))/4$, where $M = \mathrm{globalMaximalFunction}(\mathrm{vol}, 1)$.

### `simple_nontangential_operator`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hr : 0 < r) : HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r : ℝ} {K : X → X → ℂ} [IsTwoSidedKernel a K], 4 ≤ a → (∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) → 0 < r → HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
English: (Lemma 10.1.6.) Let $a \ge 4$, suppose $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$ for every $r > 0$, and let $r > 0$. Then $\mathrm{simpleNontangentialOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{10.1.6}(a)$ (including measurability of the operator).

### `simple_nontangential_operator_le`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hr : 0 ≤ r) : HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r : ℝ} {K : X → X → ℂ} [IsTwoSidedKernel a K], 4 ≤ a → (∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) → 0 ≤ r → HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
English: Let $a \ge 4$, suppose $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$ for every $r > 0$, and let $r \ge 0$. Then $\mathrm{simpleNontangentialOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{10.1.6}(a)$.
