You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ddconv`
Lean: `[Fintype G] (f : G → R) (g : G → R) (_ : G) : R`
English: Let $G$ be a finite type (with its additive group structure). For $f, g : G \to R$, $\mathrm{ddconv}(f, g)$ is a function $G \to R$; according to its docstring, it is the convolution $f * g$ of $f$ and $g$.

### `ddconv_eq_sum_sub`
Lean: `[Fintype G] (f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
English: Let $G$ be a finite abelian group. For $f, g : G \to R$ and $a \in G$, $(f * g)(a) = \sum_{t \in G} f(a - t)\, g(t)$, where $*$ is discrete convolution.

### `trivChar`
Lean: `(_ : G) : R`
English: Defines $\mathrm{trivChar} : G \to R$, the trivial character.

### `iterConv`
Lean: `[Fintype G] (f : G → R) (_ : ℕ) (_ : G) : R`
English: Let $G$ be a finite type (with its additive group structure). For $f : G \to R$ and $n \in \mathbb{N}$, $\mathrm{iterConv}(f, n)$ is a function $G \to R$; according to its docstring, it is the ($n$-fold) iterated convolution of $f$.

### `dddconv`
Lean: `[Fintype G] [StarRing R] (f : G → R) (g : G → R) (_ : G) : R`
English: Let $G$ be a finite type (with its additive group structure) and $R$ a star ring. For $f, g : G \to R$, $\mathrm{dddconv}(f, g)$ is a function $G \to R$; according to its docstring, it is the difference convolution $f \circ g$ of $f$ and $g$.
