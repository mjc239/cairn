You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

### `FiniteRange`
Lean (short): `(X : Ω → G) : Prop`
Lean (full): `{Ω : Type u_1} → {G : Type u_2} → (Ω → G) → Prop`
Docstring: The property of having a finite range.
Previous English: A map $X:\Omega\to G$ has finite range if its range $X(\Omega)$ is a finite set.
Checker's issue: The characterization 'its range X(Omega) is a finite set' goes beyond the signature (Omega -> G) -> Prop and is not attributed to the docstring.

### `FiniteRange.toFinset`
Lean (short): `(X : Ω → G) [FiniteRange X] : Finset G`
Lean (full): `{Ω : Type u_1} → {G : Type u_2} → (X : Ω → G) → [hX : FiniteRange X] → Finset G`
Docstring: The range of a finite range map, as a finset.
Previous English: For a map $X:\Omega\to G$ with finite range, its range $\mathrm{range}(X)$ viewed as a finite set (Finset) of $G$.
Checker's issue: The claim that the resulting Finset is the range of X goes beyond the signature and is not attributed to the docstring.
