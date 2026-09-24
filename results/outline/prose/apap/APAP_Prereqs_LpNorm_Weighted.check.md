You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `wLpNorm`
Lean: `(p : ENNReal) (w : α → NNReal) (f : α → E) : ℝ`
English: For $p \in [0, \infty]$, a weight $w : \alpha \to \mathbb{R}_{\ge 0}$ and $f : \alpha \to E$, defines the weighted $L^p$ norm $\|f\|_{p, w}$ of $f$.
