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

#### `MeasureTheory.cLpNorm` (def)
Lean: `{α : Type u_1} → {E : Type u_4} → [MeasurableSpace α] → [NormedAddCommGroup E] → ENNReal → (α → E) → ℝ`
Docstring: The Lp norm of a function with the compact normalisation.
Definition: `fun {α : Type u_1} {E : Type u_4} [inst : MeasurableSpace α] [NormedAddCommGroup E] (p : ENNReal) (f : α → E) => lpNorm (m0 := inst) f p (ProbabilityTheory.uniformOn Set.univ)`

#### `cft` (def)
Lean: `{G : Type u_1} → [inst : AddCommGroup G] → [Fintype G] → (G → ℂ) → AddChar G ℂ → ℂ`
Docstring: The discrete Fourier transform.
Definition: `fun {G : Type u_1} [AddCommGroup G] [Fintype G] (f : G → ℂ) (ψ : AddChar G ℂ) => ⟪⇑ψ, f⟫ₙ_[ℂ]`

## Translations

### `rudin_ineq`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hp : 2 ≤ p) (f : G → ℂ) (hf : AddDissociated (Function.support (cft f))) : ‖f‖ₙ_[↑p] ≤ 4 * Real.exp 2⁻¹ * √↑p * ‖f‖ₙ_[2]`
Lean (full): `∀ {G : Type u_1} [inst : Fintype G] [inst_1 : AddCommGroup G] {p : ℕ} [inst_2 : MeasurableSpace G] [DiscreteMeasurableSpace G], (2 : ℕ) ≤ p → ∀ (f : G → ℂ), AddDissociated (α := AddChar G ℂ) (Function.support (cft f)) → ‖f‖ₙ_[↑p] ≤ (4 : ℝ) * Real.exp (2 : ℝ)⁻¹ * √↑p * ‖f‖ₙ_[(2 : ENNReal)]`
Docstring: **Rudin's inequality**, usual form.
English: (Rudin's inequality, usual form, per the docstring.) Let $G$ be a finite additive commutative group equipped with a measurable space structure that is discrete (every subset is measurable). Let $p$ be a natural number with $p \ge 2$, and let $f : G \to \mathbb{C}$ be such that the support of $\mathrm{cft}(f)$ (APAP's compact Fourier transform `cft` of $f$, a function on the additive characters $G \to \mathbb{C}$) is an additively dissociated set of additive characters. Then $\|f\|_{p} \le 4\, e^{1/2} \sqrt{p}\, \|f\|_{2}$, where $\|\cdot\|_{p}$ and $\|\cdot\|_{2}$ are the compact $L^p$ and $L^2$ norms (written `‖·‖ₙ_[p]`, `‖·‖ₙ_[2]`) on functions $G \to \mathbb{C}$.
