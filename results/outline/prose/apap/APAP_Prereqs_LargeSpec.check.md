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

### `largeSpec`
Lean (short): `[Fintype G] (f : G → ℂ) (η : ℝ) : Finset (AddChar G ℂ)`
Lean (full): `{G : Type u_1} → [inst : AddCommGroup G] → [Fintype G] → [MeasurableSpace G] → (G → ℂ) → ℝ → Finset (AddChar G ℂ)`
English: Let $G$ be a finite type (with its additive group structure). For $f : G \to \mathbb{C}$ and $\eta \in \mathbb{R}$, $\mathrm{largeSpec}(f, \eta)$ is a finite set of additive characters $G \to \mathbb{C}$; according to its docstring, it is the $\eta$-large spectrum of $f$.
