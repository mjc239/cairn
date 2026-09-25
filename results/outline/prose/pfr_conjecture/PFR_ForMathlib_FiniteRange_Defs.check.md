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
naturally. Definitions are held to the same standard: the English must name the setting the signature assumes
("for an abelian group $G$ and …, $\mathrm{rdist}$ is …"). Replacing an assumption by a stronger one (a metric
space where the Lean has a pseudometric space) is unfaithful too. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `FiniteRange`
Lean (short): `(X : Ω → G) : Prop`
Lean (full): `{Ω : Type u_1} → {G : Type u_2} → (Ω → G) → Prop`
English: A map $X:\Omega\to G$ has finite range if its range $X(\Omega)$ is a finite set.

### `FiniteRange.fintype`
Lean (short): `(X : Ω → G) [FiniteRange X] : Fintype ↑(Set.range X)`
Lean (full): `{Ω : Type u_1} → {G : Type u_2} → (X : Ω → G) → [hX : FiniteRange X] → Fintype ↑(Set.range X)`
English: For a map $X:\Omega\to G$ with finite range, the Fintype structure (an explicit finite enumeration) on its range $\mathrm{range}(X)$.

### `FiniteRange.toFinset`
Lean (short): `(X : Ω → G) [FiniteRange X] : Finset G`
Lean (full): `{Ω : Type u_1} → {G : Type u_2} → (X : Ω → G) → [hX : FiniteRange X] → Finset G`
English: For a map $X:\Omega\to G$ with finite range, its range $\mathrm{range}(X)$ viewed as a finite set (Finset) of $G$.
