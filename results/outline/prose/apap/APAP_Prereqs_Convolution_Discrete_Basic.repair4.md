You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring, and when no
docstring, definition body (under "Project definitions") or Lean supports a description of an object, name it
instead of describing it. Give every variable its
type, introduce every symbol, and never use one letter for two things. When a definition's body is shown, say what
it defines, in words or a formula that agrees with the body.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `dddconv` (def)
Lean: `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [Fintype G] → [inst : CommSemiring R] → [StarRing R] → (G → R) → (G → R) → G → R`
Docstring: Difference convolution
Definition: `fun {G : Type u_1} {R : Type u_3} [DecidableEq G] [AddCommGroup G] [Fintype G] [CommSemiring R] [StarRing R] (f g : G → R) (a : G) => ∑ x : G × G with x.1 - x.2 = a, HMul.hMul (β := R) (f x.1) ((starRingEnd (G → R)) g x.2 : R)`

#### `ddconv` (def)
Lean: `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [Fintype G] → [CommSemiring R] → (G → R) → (G → R) → G → R`
Docstring: Convolution
Definition: `fun {G : Type u_1} {R : Type u_3} [DecidableEq G] [AddCommGroup G] [Fintype G] [CommSemiring R] (f g : G → R) (a : G) => ∑ x : G × G with x.1 + x.2 = a, f x.1 * g x.2`

## Flagged translations

### `balance_dddconv`
Lean (short): `[Fintype G] [CharZero R] [StarRing R] (f : G → R) (g : G → R) : Fintype.balance (f ○ᵈ g) = Fintype.balance f ○ᵈ Fintype.balance g`
Lean (full): `∀ {G : Type u_1} {R : Type u_2} [inst : Fintype G] [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : Field R] [inst_4 : CharZero R] [inst_5 : StarRing R] (f g : G → R), Fintype.balance (f ○ᵈ g) = Fintype.balance f ○ᵈ Fintype.balance g`
Previous English: Let $G$ be a finite additive commutative group and let $R$ be a field of characteristic zero equipped with a star ring structure. For functions $f, g : G \to R$, $\operatorname{balance}(f \circ_d g) = \operatorname{balance}(f) \circ_d \operatorname{balance}(g)$, where $\circ_d$ is APAP's discrete difference convolution (written `○ᵈ`) and $\operatorname{balance}$ is the operator `Fintype.balance`.
Checker's issue: The operators are introduced only via Lean identifiers: the difference convolution (f ○ᵈ g)(a) = Σ_{x-y=a} f(x)·conj(g(y)) (project def dddconv, body shown) is not described, and 'balance' is only named as `Fintype.balance` without its meaning (f minus its average), so the statement is not readable as mathematics.

### `balance_ddconv`
Lean (short): `[Fintype G] [CharZero R] (f : G → R) (g : G → R) : Fintype.balance (f ∗ᵈ g) = Fintype.balance f ∗ᵈ Fintype.balance g`
Lean (full): `∀ {G : Type u_1} {R : Type u_2} [inst : Fintype G] [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : Field R] [inst_4 : CharZero R] (f g : G → R), Fintype.balance (f ∗ᵈ g) = Fintype.balance f ∗ᵈ Fintype.balance g`
Previous English: Let $G$ be a finite additive commutative group and let $R$ be a field of characteristic zero. For functions $f, g : G \to R$, $\operatorname{balance}(f \ast_d g) = \operatorname{balance}(f) \ast_d \operatorname{balance}(g)$, where $\ast_d$ is APAP's discrete convolution (written `∗ᵈ`) and $\operatorname{balance}$ is the operator `Fintype.balance`.
Checker's issue: The operators are introduced only via Lean identifiers: the convolution (f ∗ᵈ g)(a) = Σ_{x+y=a} f(x)g(y) (project def ddconv, body shown) is not described, and 'balance' is only named as `Fintype.balance` without its meaning (f minus its average).
