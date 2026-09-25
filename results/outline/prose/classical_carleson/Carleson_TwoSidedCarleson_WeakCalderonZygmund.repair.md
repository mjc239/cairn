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

### `estimate_czOperator`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hr : 0 < r) (hf : BoundedFiniteSupport f volume) (hT : HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) : distribution (czOperator K r f) α volume ≤ ↑(C10_0_3 a) / α * eLpNorm f 1 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r : ℝ} {K : X → X → ℂ} [IsTwoSidedKernel a K] {f : X → ℂ} {α : ENNReal}, 4 ≤ a → 0 < r → BoundedFiniteSupport f volume → HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a) → distribution (czOperator K r f) α volume ≤ ↑(C10_0_3 a) / α * eLpNorm f 1 volume`
Docstring: Lemma 10.0.3, blueprint form.
Previous English: (Lemma 10.0.3.) Let $a \ge 4$, $r > 0$, let $f$ be bounded with finite-measure support, and suppose $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$. Then for every $\alpha$, the distribution function satisfies $\mathrm{vol}\{x : \|\mathrm{czOperator}(K, r) f(x)\| > \alpha\} \le \frac{C_{10.0.3}(a)}{\alpha} \|f\|_{L^1}$.
Checker's issue: Omits that X is a metric space with a doubling measure (DoublingMeasure X (defaultA a)) and that K is a two-sided Calderon-Zygmund kernel (IsTwoSidedKernel a K).
