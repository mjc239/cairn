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

### `cLpNorm_conv_le_cLpNorm_dconv`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hn₀ : n ≠ 0) (hn : Even n) (f : G → ℂ) : ‖f ∗ f‖ₙ_[↑n] ≤ ‖f ○ f‖ₙ_[↑n]`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : Fintype G] [inst_2 : DecidableEq G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G] {n : ℕ}, n ≠ 0 → Even n → ∀ (f : G → ℂ), ‖f ∗ f‖ₙ_[↑n] ≤ ‖f ○ f‖ₙ_[↑n]`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. If $n \ne 0$ is even and $f : G \to \mathbb{C}$, then $\|f * f\|_n \le \|f \circ f\|_n$, where $*$ and $\circ$ are the compact convolution and difference convolution and the norms have the compact (expectation) normalisation.

### `dLpNorm_ddconv_le_dLpNorm_dddconv`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hn₀ : n ≠ 0) (hn : Even n) (f : G → ℂ) : ‖f ∗ᵈ f‖_[↑n] ≤ ‖f ○ᵈ f‖_[↑n]`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : Fintype G] [inst_2 : DecidableEq G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G] {n : ℕ}, n ≠ 0 → Even n → ∀ (f : G → ℂ), ‖f ∗ᵈ f‖_[↑n] ≤ ‖f ○ᵈ f‖_[↑n]`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. If $n \ne 0$ is even and $f : G \to \mathbb{C}$, then $\|f * f\|_n \le \|f \circ f\|_n$ for the discrete convolution $*$, discrete difference convolution $\circ$ and discrete $L^n$ norm.
