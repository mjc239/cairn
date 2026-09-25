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

### `estimate_czOperator`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hr : 0 < r) (hf : BoundedFiniteSupport f volume) (hT : HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) : distribution (czOperator K r f) α volume ≤ ↑(C10_0_3 a) / α * eLpNorm f 1 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r : ℝ} {K : X → X → ℂ} [IsTwoSidedKernel a K] {f : X → ℂ} {α : ENNReal}, 4 ≤ a → 0 < r → BoundedFiniteSupport f volume → HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a) → distribution (czOperator K r f) α volume ≤ ↑(C10_0_3 a) / α * eLpNorm f 1 volume`
English: (Lemma 10.0.3.) Let $a \ge 4$, $r > 0$, let $f$ be bounded with finite-measure support, and suppose $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$. Then for every $\alpha$, the distribution function satisfies $\mathrm{vol}\{x : \|\mathrm{czOperator}(K, r) f(x)\| > \alpha\} \le \frac{C_{10.0.3}(a)}{\alpha} \|f\|_{L^1}$.
