You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Keep every
hypothesis the Lean shows, including instance assumptions such as `[Finite G]` or `[IsProbabilityMeasure μ]`
(say them in words: "$G$ is finite", "$\mu$ is a probability measure"), and the exact conclusion. Do not add
claims the Lean does not make. Purely structural instances (e.g. `[AddCommGroup G]`) and implicit arguments are not
shown and may stay implicit.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

### `PFR_conjecture_aux`
Lean: `[Countable G] [Module (ZMod 2) G] [Finite G] (hA₀ : A.Nonempty) (hA : ↑(A + A).ncard ≤ K * ↑A.ncard) : ∃ H c, ↑(Nat.card ↑c) ≤ K ^ (13 / 2) * ↑A.ncard ^ (1 / 2) * ↑(↑H).ncard ^ (-1 / 2) ∧ ↑(↑H).ncard ≤ K ^ 11 * ↑A.ncard ∧ ↑A.ncard ≤ K ^ 11 * ↑(↑H).ncard ∧ A ⊆ c + ↑H`
Docstring: Auxiliary statement towards the polynomial Freiman-Ruzsa (PFR) conjecture: if `A` is a subset of an elementary abelian 2-group of doubling constant at most $K$, then there exists a subgroup `H` such that `A` can be covered by at most `K^(13/2) |A|^(1/2) / |H|^(1/2)` cosets of `H`, and `H` has the same cardinality as `A` up to a multiplicative factor `K^11`.
Previous English: Let $A$ be a nonempty subset of $G$ (an elementary abelian $2$-group, per the docstring) with $|A+A|\le K|A|$. Then there exist a subgroup $H\le G$ and a set $c\subseteq G$ such that $|c|\le K^{13/2}|A|^{1/2}|H|^{-1/2}$, $|H|\le K^{11}|A|$, $|A|\le K^{11}|H|$, and $A\subseteq c+H$.
Checker's issue: Drops the hypothesis [Finite G]; English does not say G is finite.

### `PFR_conjecture`
Lean: `[Countable G] [Module (ZMod 2) G] [Finite G] (hA₀ : A.Nonempty) (hA : ↑(A + A).ncard ≤ K * ↑A.ncard) : ∃ H c, ↑(Nat.card ↑c) < 2 * K ^ 12 ∧ (↑H).ncard ≤ A.ncard ∧ A ⊆ c + ↑H`
Docstring: The polynomial Freiman-Ruzsa (PFR) conjecture: if `A` is a subset of an elementary abelian 2-group of doubling constant at most `K`, then `A` can be covered by at most `2 * K ^ 12` cosets of a subgroup of cardinality at most `|A|`.
Previous English: Let $A$ be a nonempty subset of $G$ (an elementary abelian $2$-group, per the docstring) with $|A+A|\le K|A|$. Then there exist a subgroup $H\le G$ and a set $c\subseteq G$ with $|c|<2K^{12}$, $|H|\le|A|$, and $A\subseteq c+H$.
Checker's issue: Drops the hypothesis [Finite G]; English does not say G is finite.
