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

## Flagged translations

### `ProbabilityTheory.CondIndepFun`
Lean (short): `(f : Ω → α) (g : Ω → β) (h : Ω → γ) (μ : autoParam (Measure Ω) CondIndepFun._auto_1) : Prop`
Lean (full): `{Ω : Type u_1} → {α : Type u_3} → {β : Type u_4} → {γ : Type u_5} → [inst : MeasurableSpace Ω] → [MeasurableSpace α] → [MeasurableSpace β] → [MeasurableSpace γ] → (Ω → α) → (Ω → β) → (Ω → γ) → autoParam (Measure Ω) CondIndepFun._auto_1 → Prop`
Definition: `fun {Ω : Type u_1} {α : Type u_3} {β : Type u_4} {γ : Type u_5} [MeasurableSpace Ω] [MeasurableSpace α] [MeasurableSpace β] [MeasurableSpace γ] (f : Ω → α) (g : Ω → β) (h : Ω → γ) (μ : Measure Ω) => ∀ᵐ (z : γ) ∂Measure.map h μ, IndepFun f g μ[|h ⁻¹' {z}]`
Docstring: The assertion that `f` and `g` are conditionally independent relative to `h`.
Previous English: Let $\Omega$, $\alpha$, $\beta$, $\gamma$ be types, each equipped with a measurable-space structure. Given functions (random variables) $f : \Omega \to \alpha$, $g : \Omega \to \beta$, $h : \Omega \to \gamma$ and a measure $\mu$ on $\Omega$ (an auto-filled argument that, when omitted, is supplied by Lean's default tactic, i.e. the ambient measure $\mathrm{volume}$ on $\Omega$), $\mathrm{CondIndepFun}\ f\ g\ h\ \mu$ is the proposition that $f$ and $g$ are conditionally independent relative to $h$ with respect to $\mu$.
Checker's issue: Says the default measure is `volume`, which the prompt does not show; state only what the Lean/docstring shows.
