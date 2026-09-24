You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `balance_dddconv`
Lean: `[Fintype G] [CharZero R] [StarRing R] (f : G → R) (g : G → R) : Fintype.balance (f ○ᵈ g) = Fintype.balance f ○ᵈ Fintype.balance g`
English: Let $G$ be a finite abelian group and let $R$ have characteristic zero and a star operation. For $f, g : G \to R$, the balanced (mean-subtracted) version of the difference convolution is the difference convolution of the balanced functions: $\operatorname{balance}(f \circ g) = \operatorname{balance}(f) \circ \operatorname{balance}(g)$, where $\circ$ is the discrete difference convolution and $\operatorname{balance}(h) = h - \mathbb{E}\,h$.

### `balance_ddconv`
Lean: `[Fintype G] [CharZero R] (f : G → R) (g : G → R) : Fintype.balance (f ∗ᵈ g) = Fintype.balance f ∗ᵈ Fintype.balance g`
English: Let $G$ be a finite abelian group and let $R$ have characteristic zero. For $f, g : G \to R$, $\operatorname{balance}(f \ast g) = \operatorname{balance}(f) \ast \operatorname{balance}(g)$, where $\ast$ is discrete convolution and $\operatorname{balance}(h) = h - \mathbb{E}\,h$.
