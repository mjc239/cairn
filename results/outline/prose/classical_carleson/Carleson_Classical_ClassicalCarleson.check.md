You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `classical_carleson`
Lean: `(cont_f : Continuous f) (periodic_f : Function.Periodic f (2 * Real.pi)) : ∀ᵐ (x : ℝ), Filter.Tendsto (fun x_1 => partialFourierSum x_1 f x) Filter.atTop (nhds (f x))`
English: Let $f : \mathbb{R} \to \mathbb{C}$ be continuous and $2\pi$-periodic. Then for almost every $x \in \mathbb{R}$ the partial Fourier sums converge to $f(x)$: $\lim_{N \to \infty} S_N f(x) = f(x)$, where $S_N f$ denotes `partialFourierSum N f`.
