You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `iterCConv`
Lean: `[CharZero R] (f : G → R) (_ : ℕ) (_ : G) : R`
English: For $R$ of characteristic zero, $f : G \to R$ and $n \in \mathbb{N}$, defines the $n$-fold iterated convolution of $f$ with respect to the compact (expectation-normalised) convolution.
