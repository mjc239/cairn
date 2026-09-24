You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `cft`
Lean: `[Fintype G] (f : G → ℂ) (_ : AddChar G ℂ) : ℂ`
English: Let $G$ be a finite type (with its additive group structure). For $f : G \to \mathbb{C}$, $\mathrm{cft}(f)$ assigns to each additive character $\psi : G \to \mathbb{C}$ a complex number $\mathrm{cft}(f)(\psi)$; according to its docstring, it is the discrete Fourier transform of $f$.
