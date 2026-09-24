You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `cLpNorm_conv_le_cLpNorm_dconv`
Lean: `[DiscreteMeasurableSpace G] (hn₀ : n ≠ 0) (hn : Even n) (f : G → ℂ) : ‖f ∗ f‖ₙ_[↑n] ≤ ‖f ○ f‖ₙ_[↑n]`
English: $G$ carries the discrete measurable structure. If $n \ne 0$ is even and $f : G \to \mathbb{C}$, then $\|f * f\|_n \le \|f \circ f\|_n$, where $*$ and $\circ$ are the compact convolution and difference convolution and the norms have the compact (expectation) normalisation.

### `dLpNorm_ddconv_le_dLpNorm_dddconv`
Lean: `[DiscreteMeasurableSpace G] (hn₀ : n ≠ 0) (hn : Even n) (f : G → ℂ) : ‖f ∗ᵈ f‖_[↑n] ≤ ‖f ○ᵈ f‖_[↑n]`
English: $G$ carries the discrete measurable structure. If $n \ne 0$ is even and $f : G \to \mathbb{C}$, then $\|f * f\|_n \le \|f \circ f\|_n$ for the discrete convolution, difference convolution and discrete $L^n$ norm.
