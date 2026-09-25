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

### `BohrSet`
Lean (short): `(G : Type u_1) : Type u_1`
Lean (full): `(G : Type u_1) → [AddCommGroup G] → Type u_1`
English: For a type $G$, $\mathrm{BohrSet}(G)$ is a type (in the same universe as $G$), the type of Bohr sets on $G$. According to its docstring, a Bohr set on an additive group $G$ consists of a finite set of characters of $G$ (the frequencies) together with an extended nonnegative real width for each frequency $\psi$, and is thought of as the set $\{x : \|1 - \psi(x)\| \le \text{width}(\psi) \text{ for all frequencies } \psi\}$ (the chord-length convention).
