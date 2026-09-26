You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one. For a definition, name the setting its signature assumes. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

### `balance_dddconv`
Lean (short): `[Fintype G] [CharZero R] [StarRing R] (f : G → R) (g : G → R) : Fintype.balance (f ○ᵈ g) = Fintype.balance f ○ᵈ Fintype.balance g`
Lean (full): `∀ {G : Type u_1} {R : Type u_2} [inst : Fintype G] [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : Field R] [inst_4 : CharZero R] [inst_5 : StarRing R] (f g : G → R), Fintype.balance (f ○ᵈ g) = Fintype.balance f ○ᵈ Fintype.balance g`
Previous English: Let $G$ be a finite abelian group and let $R$ have characteristic zero and a star operation. For $f, g : G \to R$, the balanced (mean-subtracted) version of the difference convolution is the difference convolution of the balanced functions: $\operatorname{balance}(f \circ g) = \operatorname{balance}(f) \circ \operatorname{balance}(g)$, where $\circ$ is the discrete difference convolution and $\operatorname{balance}(h) = h - \mathbb{E}\,h$.
Checker's issue: Omits that R is a field (Field R), stating only characteristic zero and a star operation.

### `balance_ddconv`
Lean (short): `[Fintype G] [CharZero R] (f : G → R) (g : G → R) : Fintype.balance (f ∗ᵈ g) = Fintype.balance f ∗ᵈ Fintype.balance g`
Lean (full): `∀ {G : Type u_1} {R : Type u_2} [inst : Fintype G] [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : Field R] [inst_4 : CharZero R] (f g : G → R), Fintype.balance (f ∗ᵈ g) = Fintype.balance f ∗ᵈ Fintype.balance g`
Previous English: Let $G$ be a finite abelian group and let $R$ have characteristic zero. For $f, g : G \to R$, $\operatorname{balance}(f \ast g) = \operatorname{balance}(f) \ast \operatorname{balance}(g)$, where $\ast$ is discrete convolution and $\operatorname{balance}(h) = h - \mathbb{E}\,h$.
Checker's issue: Omits that R is a field (Field R), stating only characteristic zero.
