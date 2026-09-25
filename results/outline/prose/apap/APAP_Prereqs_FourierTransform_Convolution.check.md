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

### `cLpNorm_conv_le_cLpNorm_dconv`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hn₀ : n ≠ 0) (hn : Even n) (f : G → ℂ) : ‖f ∗ f‖ₙ_[↑n] ≤ ‖f ○ f‖ₙ_[↑n]`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : Fintype G] [inst_2 : DecidableEq G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G] {n : ℕ}, n ≠ (0 : ℕ) → Even n → ∀ (f : G → ℂ), ‖f ∗ f‖ₙ_[↑n] ≤ ‖f ○ f‖ₙ_[↑n]`
English: Let $G$ be a finite additive commutative group equipped with a measurable space structure that is discrete (every subset is measurable). Let $n$ be a natural number with $n \ne 0$ and $n$ even, and let $f : G \to \mathbb{C}$. Then $\|f \ast f\|_{n} \le \|f \circ f\|_{n}$, where $\ast$ is the convolution (written `∗`), $\circ$ is the difference convolution (written `○`), and $\|\cdot\|_{n}$ is the compact $L^n$ norm (written `‖·‖ₙ_[n]`).

### `dLpNorm_ddconv_le_dLpNorm_dddconv`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hn₀ : n ≠ 0) (hn : Even n) (f : G → ℂ) : ‖f ∗ᵈ f‖_[↑n] ≤ ‖f ○ᵈ f‖_[↑n]`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : Fintype G] [inst_2 : DecidableEq G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G] {n : ℕ}, n ≠ (0 : ℕ) → Even n → ∀ (f : G → ℂ), ‖f ∗ᵈ f‖_[↑n] ≤ ‖f ○ᵈ f‖_[↑n]`
English: Let $G$ be a finite additive commutative group equipped with a measurable space structure that is discrete (every subset is measurable). Let $n$ be a natural number with $n \ne 0$ and $n$ even, and let $f : G \to \mathbb{C}$. Then $\|f \ast_d f\|_{n} \le \|f \circ_d f\|_{n}$, where $\ast_d$ is the discrete convolution (written `∗ᵈ`), $\circ_d$ is the discrete difference convolution (written `○ᵈ`), and $\|\cdot\|_{n}$ is the $L^n$ norm (written `‖·‖_[n]`).
