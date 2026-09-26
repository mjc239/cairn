You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring, and when no
docstring, definition body (under "Project definitions") or Lean supports a description of an object, name it
instead of describing it. Give every variable its
type, introduce every symbol, and never use one letter for two things. When a definition's body is shown, say what
it defines, in words or a formula that agrees with the body.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `ProbabilityTheory.Kernel.entropy` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → ℝ`
Docstring: Entropy of a kernel with respect to a measure.
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) (μ : Measure T) => ∫ (x : T), (fun (y : T) => measureEntropy.{u_2} (S := S) (κ y)) x ∂μ`

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

## Flagged translations

### `ProbabilityTheory.Kernel.mutualInfo`
Lean (short): `(κ : Kernel T (S × U)) (μ : Measure T) : ℝ`
Lean (full): `{S : Type u_2} → {T : Type u_3} → {U : Type u_4} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → [inst_2 : MeasurableSpace U] → Kernel T (S × U) → Measure T → ℝ`
Definition: `fun {S : Type u_2} {T : Type u_3} {U : Type u_4} [MeasurableSpace S] [MeasurableSpace T] [MeasurableSpace U] (κ : Kernel T (S × U)) (μ : Measure T) => Hk[κ.fst , μ] + Hk[κ.snd , μ] - Hk[κ , μ]`
Docstring: Mutual information of a kernel into a product space with respect to a measure.
Previous English: Definition. Let $S$, $T$ and $U$ be measurable spaces. For a kernel $\kappa$ from $T$ to the product space $S\times U$ and a measure $\mu$ on $T$, $I_k[\kappa,\mu]\in\mathbb R$ is the mutual information of the kernel $\kappa$ with respect to $\mu$ (as its docstring describes it).
Checker's issue: Definition body is shown (Hk[κ.fst, μ] + Hk[κ.snd, μ] − Hk[κ, μ]) but the English only paraphrases the docstring ('the mutual information ... as its docstring describes it') instead of giving this formula.
