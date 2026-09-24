You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `rudin_ineq`
Lean: `[Fintype G] [DiscreteMeasurableSpace G] (hp : 2 ≤ p) (f : G → ℂ) (hf : AddDissociated (Function.support (cft f))) : ‖f‖ₙ_[↑p] ≤ 4 * Real.exp 2⁻¹ * √↑p * ‖f‖ₙ_[2]`
English: (Rudin's inequality.) Let $G$ be a finite abelian group carrying the discrete measurable structure. Let $p \ge 2$ and let $f : G \to \mathbb{C}$ be such that the support of its Fourier transform $\mathrm{cft}(f)$ is dissociated. Then $\|f\|_p \le 4\, e^{1/2} \sqrt{p}\, \|f\|_2$, with norms in the compact (expectation) normalisation.
