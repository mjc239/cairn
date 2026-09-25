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

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

### `mu`
Lean (short): `(s : Finset α) (_ : α) : K`
Lean (full): `{K : Type u_1} → {α : Type u_3} → [DivisionSemiring K] → Finset α → α → K`
Docstring: The normalised indicator_one of a set.
Previous English: For a finite set $s$, $\mu_s : \alpha \to K$ is the normalised indicator function of $s$, i.e. $\mu_s(x) = 1_s(x)/|s|$.
Checker's issue: Never says what K is; the Lean requires K to be a division semiring (DivisionSemiring K).
