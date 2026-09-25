You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. A "Project
definitions" section first lists the project notions the statements refer to (statement, docstring, body,
fields). Compare the English with the full statement; anything the English attributes to the docstring must
actually be in it.

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
be supported by the docstring or the Lean. So is a formula or description of what a defined object is: a project
notion's description must agree with its entry under "Project definitions" (statement, docstring, definition body,
fields), and a library notion may only be given its standard mathematical meaning; otherwise flag it. Every variable
needs its type ("$f : G \to \mathbb{C}$", "$m$ a natural number"), every symbol must be introduced, by definition
or by name ("the Ruzsa distance $d[X;Y]$", "the maximal operator $M_{\mathcal B}$"), and no letter may mean two
things. When in doubt, flag it: a false alarm costs one repair, a missed error stays in the outline.
Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `BohrSet.ewidth` (def)
Lean: `{G : Type u_1} → [inst : AddCommGroup G] → BohrSet G → AddChar G ℂ → ENNReal`
Docstring: The width of a Bohr set at a frequency. Note that this width corresponds to chord-length.
Definition: `fun (G : Type u_1) [AddCommGroup G] (self : BohrSet G) => self.2`

#### `BohrSet.frequencies` (def)
Lean: `{G : Type u_1} → [inst : AddCommGroup G] → BohrSet G → Finset (AddChar G ℂ)`
Definition: `fun (G : Type u_1) [AddCommGroup G] (self : BohrSet G) => self.1`

## Translations

### `BohrSet`
Lean (short): `(G : Type u_1) : Type u_1`
Lean (full): `(G : Type u_1) → [AddCommGroup G] → Type u_1`
Docstring: A *Bohr set* `B` on an additive group `G` is a finite set of characters of `G`, called the *frequencies*, along with an extended non-negative real number for each frequency `ψ`, called the *width of `B` at `ψ`*. A Bohr set `B` is thought of as the set `{x | ∀ ψ ∈ B.frequencies, ‖1 - ψ x‖ ≤ B.width ψ}`. This is the *chord-length* convention. The arc-length convention would instead be `{x | ∀ ψ ∈ B.frequencies, |arg (ψ x)| ≤ B.width ψ}`. Note that this set **does not** uniquely determine `B` (in particular, it does not uniquely determine either `B.frequencies` or `B.width`).
English: For an abelian group $G$ (an additive commutative group), $\mathrm{BohrSet}(G)$ is a type (in the same universe as $G$). According to its docstring, a Bohr set $B$ on $G$ is a finite set of characters of $G$ (the frequencies) together with an extended nonnegative real number for each frequency $\psi$ (the width of $B$ at $\psi$); $B$ is thought of as the set $\{x : \|1 - \psi(x)\| \le \mathrm{width}_B(\psi) \text{ for all frequencies } \psi\}$ (the chord-length convention, as opposed to the arc-length convention $|\arg \psi(x)| \le \mathrm{width}_B(\psi)$), and this set does not uniquely determine $B$ (neither its frequencies nor its widths).
