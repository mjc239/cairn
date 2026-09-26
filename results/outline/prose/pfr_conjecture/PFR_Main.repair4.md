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
type, introduce every symbol, and never use one letter for two things.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

## Flagged translations

### `PFR_conjecture_aux`
Lean (short): `[Countable G] [Module (ZMod 2) G] [Finite G] (hA₀ : A.Nonempty) (hA : ↑(A + A).ncard ≤ K * ↑A.ncard) : ∃ H c, ↑(Nat.card ↑c) ≤ K ^ (13 / 2) * ↑A.ncard ^ (1 / 2) * ↑(↑H).ncard ^ (-1 / 2) ∧ ↑(↑H).ncard ≤ K ^ 11 * ↑A.ncard ∧ ↑A.ncard ≤ K ^ 11 * ↑(↑H).ncard ∧ A ⊆ c + ↑H`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {A : Set G} {K : ℝ} [Countable G] [inst_2 : Module (ZMod (2 : ℕ)) G] [Finite G], A.Nonempty → ↑(A + A).ncard ≤ K * ↑A.ncard → ∃ (H : Submodule (ZMod (2 : ℕ)) G) (c : Set G), ↑(Nat.card.{u_1} ↑c) ≤ K ^ (13 / 2 : ℝ) * HPow.hPow (α := ℝ) ↑A.ncard (1 / 2 : ℝ) * HPow.hPow (α := ℝ) ↑(↑H).ncard (-1 / 2 : ℝ) ∧ ↑(↑H).ncard ≤ K ^ (11 : ℝ) * ↑A.ncard ∧ ↑A.ncard ≤ K ^ (11 : ℝ) * ↑(↑H).ncard ∧ A ⊆ c + ↑H`
Docstring: Auxiliary statement towards the polynomial Freiman-Ruzsa (PFR) conjecture: if `A` is a subset of an elementary abelian 2-group of doubling constant at most $K$, then there exists a subgroup `H` such that `A` can be covered by at most `K^(13/2) |A|^(1/2) / |H|^(1/2)` cosets of `H`, and `H` has the same cardinality as `A` up to a multiplicative factor `K^11`.
Previous English: Let $G$ be a finite (in particular countable) elementary abelian $2$-group, i.e. a finite vector space over $\mathbb{F}_2$. Let $A$ be a nonempty subset of $G$ with $|A+A|\le K|A|$. Then there exist a subgroup $H\le G$ and a set $c\subseteq G$ such that $|c|\le K^{13/2}|A|^{1/2}|H|^{-1/2}$, $|H|\le K^{11}|A|$, $|A|\le K^{11}|H|$, and $A\subseteq c+H$.
Checker's issue: K is never given a type (K is a real number in Lean).

### `PFR_conjecture`
Lean (short): `[Countable G] [Module (ZMod 2) G] [Finite G] (hA₀ : A.Nonempty) (hA : ↑(A + A).ncard ≤ K * ↑A.ncard) : ∃ H c, ↑(Nat.card ↑c) < 2 * K ^ 12 ∧ (↑H).ncard ≤ A.ncard ∧ A ⊆ c + ↑H`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {A : Set G} {K : ℝ} [Countable G] [inst_2 : Module (ZMod (2 : ℕ)) G] [Finite G], A.Nonempty → ↑(A + A).ncard ≤ K * ↑A.ncard → ∃ (H : Submodule (ZMod (2 : ℕ)) G) (c : Set G), ↑(Nat.card.{u_1} ↑c) < (2 : ℝ) * K ^ (12 : ℝ) ∧ (↑H).ncard ≤ A.ncard ∧ A ⊆ c + ↑H`
Docstring: The polynomial Freiman-Ruzsa (PFR) conjecture: if `A` is a subset of an elementary abelian 2-group of doubling constant at most `K`, then `A` can be covered by at most `2 * K ^ 12` cosets of a subgroup of cardinality at most `|A|`.
Previous English: Let $G$ be a finite (in particular countable) elementary abelian $2$-group, i.e. a finite vector space over $\mathbb{F}_2$. Let $A$ be a nonempty subset of $G$ with $|A+A|\le K|A|$. Then there exist a subgroup $H\le G$ and a set $c\subseteq G$ with $|c|<2K^{12}$, $|H|\le|A|$, and $A\subseteq c+H$.
Checker's issue: K is never given a type (K is a real number in Lean).
