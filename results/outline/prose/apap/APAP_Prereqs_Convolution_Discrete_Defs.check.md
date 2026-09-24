You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ddconv`
Lean: `(f : G → R) (g : G → R) (_ : G) : R`
English: For $f, g : G \to R$, defines their (discrete) convolution $f * g : G \to R$.

### `ddconv_eq_sum_sub`
Lean: `(f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
English: For $f, g : G \to R$ and $a \in G$, $(f * g)(a) = \sum_t f(a - t)\, g(t)$.

### `trivChar`
Lean: `(_ : G) : R`
English: Defines $\mathrm{trivChar} : G \to R$, the trivial character.

### `iterConv`
Lean: `(f : G → R) (_ : ℕ) (_ : G) : R`
English: For $f : G \to R$ and $n \in \mathbb{N}$, defines the $n$-fold iterated convolution $f^{*n} : G \to R$.

### `dddconv`
Lean: `[StarRing R] (f : G → R) (g : G → R) (_ : G) : R`
English: For a star ring $R$ and $f, g : G \to R$, defines their difference convolution $f \circ g : G \to R$.
