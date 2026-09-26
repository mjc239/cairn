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

#### `FiniteRange.fintype` (def)
Lean: `{Ω : Type u_1} → {G : Type u_2} → (X : Ω → G) → [hX : FiniteRange X] → Fintype ↑(Set.range X)`
Docstring: fintype structure on the range of a finite range map.
Definition: `fun {Ω : Type u_1} {G : Type u_2} (X : Ω → G) [FiniteRange X] => Set.Finite.fintype (s := Set.range X) ⋯`

## Flagged translations

### `FiniteRange`
Lean (short): `(X : Ω → G) : Prop`
Lean (full): `{Ω : Type u_1} → {G : Type u_2} → (Ω → G) → Prop`
Constructor (every field with its type): `∀ {Ω : Type u_1} {G : Type u_2} {X : Ω → G}, (Set.range X).Finite → FiniteRange X`
Docstring: The property of having a finite range.
Previous English: For arbitrary types $\Omega$ and $G$ and a map $X : \Omega \to G$, $\mathrm{FiniteRange}(X)$ is a proposition about $X$; according to its docstring, it is the property of $X$ having a finite range.
Checker's issue: This is a structure whose constructor field is shown ((Set.range X).Finite). The English only says it is a proposition and attributes the meaning to the docstring; it does not itself state that FiniteRange X holds iff the range of X is finite.

### `FiniteRange.toFinset`
Lean (short): `(X : Ω → G) [FiniteRange X] : Finset G`
Lean (full): `{Ω : Type u_1} → {G : Type u_2} → (X : Ω → G) → [hX : FiniteRange X] → Finset G`
Definition: `fun {Ω : Type u_1} {G : Type u_2} (X : Ω → G) [FiniteRange X] => (Set.range X).toFinset`
Docstring: The range of a finite range map, as a finset.
Previous English: For arbitrary types $\Omega$ and $G$ and a map $X : \Omega \to G$ satisfying $\mathrm{FiniteRange}(X)$, $\mathrm{FiniteRange.toFinset}(X)$ is a finite set (Finset) of elements of $G$; according to its docstring, it is the range of $X$, viewed as a finset.
Checker's issue: The definition body is shown ((Set.range X).toFinset), but the English only attributes 'the range of X as a finset' to the docstring. It does not itself state what the object is.
