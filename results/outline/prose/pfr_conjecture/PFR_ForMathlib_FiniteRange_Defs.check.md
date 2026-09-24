You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `FiniteRange`
Lean: `(X : Ω → G) : Prop`
English: A map $X:\Omega\to G$ has finite range if its range $X(\Omega)$ is a finite set.

### `FiniteRange.fintype`
Lean: `(X : Ω → G) [FiniteRange X] : Fintype ↑(Set.range X)`
English: For a map $X:\Omega\to G$ with finite range, the Fintype structure (an explicit finite enumeration) on its range $\mathrm{range}(X)$.

### `FiniteRange.toFinset`
Lean: `(X : Ω → G) [FiniteRange X] : Finset G`
English: For a map $X:\Omega\to G$ with finite range, its range $\mathrm{range}(X)$ viewed as a finite set (Finset) of $G$.
