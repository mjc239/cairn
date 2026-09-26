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

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

## Flagged translations

### `mu`
Lean (short): `(s : Finset α) (_ : α) : K`
Lean (full): `{K : Type u_1} → {α : Type u_3} → [DivisionSemiring K] → Finset α → α → K`
Definition: `fun {K : Type u_1} {α : Type u_3} [DivisionSemiring K] (s : Finset α) => HSMul.hSMul (α := K) (β := α → K) (↑s.card)⁻¹ ((↑s).indicator fun (x : α) => (1 : K))`
Docstring: The normalised indicator_one of a set.
Previous English: Definition. Let $K$ be a division semiring and $\alpha$ a type. For a finite set $s$ of elements of $\alpha$, $\mu_s : \alpha \to K$ is a $K$-valued function on $\alpha$; its docstring describes it as the normalised indicator_one of the set $s$.
Checker's issue: Definition body is shown but the English only paraphrases the docstring ('normalised indicator_one'). It should state the formula μ_s = (#s)⁻¹ • 1_s, i.e. μ_s(x) = (#s)⁻¹ for x ∈ s and 0 otherwise, computed in K (in particular μ_∅ = 0 because 0⁻¹ = 0).
