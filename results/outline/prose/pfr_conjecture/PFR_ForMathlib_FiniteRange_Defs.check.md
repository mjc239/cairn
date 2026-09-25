You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. Compare the
English with the full statement; anything the English attributes to the docstring must actually be in it.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Definitions are held to the same standard: the English must name the setting the signature assumes
("for an abelian group $G$ and …, $\mathrm{rdist}$ is …"). Replacing an assumption by a stronger one (a metric
space where the Lean has a pseudometric space) is unfaithful too, and so is leaving a restrictive type unstated
(a natural number, a nonnegative real). Citations (theorem or lemma numbers) and remarks are claims too: each must
be supported by the docstring or the Lean. So is a formula or description of what a defined object is: when the
prompt shows neither its definition nor a docstring saying it, the English must not supply one. Every variable
needs its type ("$f : G \to \mathbb{C}$", "$m$ a natural number"), every symbol must be introduced (notation such
as $M_{\mathcal B}$ included), and no letter may mean two things. When in doubt, flag it: a false alarm costs one
repair, a missed error stays in the outline. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `FiniteRange`
Lean (short): `(X : Ω → G) : Prop`
Lean (full): `{Ω : Type u_1} → {G : Type u_2} → (Ω → G) → Prop`
Docstring: The property of having a finite range.
English: For arbitrary types $\Omega$ and $G$ and a map $X : \Omega \to G$, $\mathrm{FiniteRange}(X)$ is a proposition about $X$; according to its docstring, it is the property of $X$ having a finite range.

### `FiniteRange.fintype`
Lean (short): `(X : Ω → G) [FiniteRange X] : Fintype ↑(Set.range X)`
Lean (full): `{Ω : Type u_1} → {G : Type u_2} → (X : Ω → G) → [hX : FiniteRange X] → Fintype ↑(Set.range X)`
Docstring: fintype structure on the range of a finite range map.
English: For a map $X:\Omega\to G$ with finite range, the Fintype structure (an explicit finite enumeration) on its range $\mathrm{range}(X)$.

### `FiniteRange.toFinset`
Lean (short): `(X : Ω → G) [FiniteRange X] : Finset G`
Lean (full): `{Ω : Type u_1} → {G : Type u_2} → (X : Ω → G) → [hX : FiniteRange X] → Finset G`
Docstring: The range of a finite range map, as a finset.
English: For arbitrary types $\Omega$ and $G$ and a map $X : \Omega \to G$ satisfying $\mathrm{FiniteRange}(X)$, $\mathrm{FiniteRange.toFinset}(X)$ is a finite set (Finset) of elements of $G$; according to its docstring, it is the range of $X$, viewed as a finset.
