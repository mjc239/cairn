You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.IsUniform.measureReal_preimage_sub_zero`
Lean: `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (Uunif : IsUniform (↑A) U volume) (Umeas : Measurable U) (Vunif : IsUniform (↑B) V volume) (Vmeas : Measurable V) (h_indep : IndepFun U V volume) : volume.real ((U - V) ⁻¹' {0}) = ↑(A ∩ B).card / (↑A.card * ↑B.card)`
English: Let $U$ and $V$ be measurable, independent random variables, with $U$ uniformly distributed on the finite set $A$ and $V$ uniformly distributed on the finite set $B$. Then $P[U-V=0]=\dfrac{|A\cap B|}{|A|\cdot|B|}$.

### `ProbabilityTheory.IsUniform.measureReal_preimage_sub`
Lean: `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (Uunif : IsUniform (↑A) U volume) (Umeas : Measurable U) (Vunif : IsUniform (↑B) V volume) (Vmeas : Measurable V) (h_indep : IndepFun U V volume) (x : G) : volume.real ((U - V) ⁻¹' {x}) = ↑(A ∩ (B + {x})).card / (↑A.card * ↑B.card)`
English: Let $U$ and $V$ be measurable, independent random variables, with $U$ uniformly distributed on the finite set $A$ and $V$ uniformly distributed on the finite set $B$. Then for every $x\in G$, $P[U-V=x]=\dfrac{|A\cap (B+\{x\})|}{|A|\cdot|B|}$.

### `rdist_le_of_isUniform_of_card_sub_le`
Lean: `[Countable G] [Finite ↑A] [MeasurableSingletonClass G] (hA₀ : A.Nonempty) (hA : ↑(A - A).ncard ≤ K * ↑A.ncard) [IsProbabilityMeasure volume] (U₀unif : IsUniform A U₀ volume) (U₀meas : Measurable U₀) : d[U₀ # U₀] ≤ Real.log K`
English: Let $A\subseteq G$ be nonempty with $|A-A|\le K|A|$, and let $U_0$ be a measurable random variable uniformly distributed on $A$. Then $d[U_0;U_0]\le \log K$.

### `PFR_conjecture_aux`
Lean: `[Countable G] [Module (ZMod 2) G] [Finite G] (hA₀ : A.Nonempty) (hA : ↑(A + A).ncard ≤ K * ↑A.ncard) : ∃ H c, ↑(Nat.card ↑c) ≤ K ^ (13 / 2) * ↑A.ncard ^ (1 / 2) * ↑(↑H).ncard ^ (-1 / 2) ∧ ↑(↑H).ncard ≤ K ^ 11 * ↑A.ncard ∧ ↑A.ncard ≤ K ^ 11 * ↑(↑H).ncard ∧ A ⊆ c + ↑H`
English: Let $A$ be a nonempty subset of $G$ (an elementary abelian $2$-group, per the docstring) with $|A+A|\le K|A|$. Then there exist a subgroup $H\le G$ and a set $c\subseteq G$ such that $|c|\le K^{13/2}|A|^{1/2}|H|^{-1/2}$, $|H|\le K^{11}|A|$, $|A|\le K^{11}|H|$, and $A\subseteq c+H$.

### `PFR_conjecture`
Lean: `[Countable G] [Module (ZMod 2) G] [Finite G] (hA₀ : A.Nonempty) (hA : ↑(A + A).ncard ≤ K * ↑A.ncard) : ∃ H c, ↑(Nat.card ↑c) < 2 * K ^ 12 ∧ (↑H).ncard ≤ A.ncard ∧ A ⊆ c + ↑H`
English: Let $A$ be a nonempty subset of $G$ (an elementary abelian $2$-group, per the docstring) with $|A+A|\le K|A|$. Then there exist a subgroup $H\le G$ and a set $c\subseteq G$ with $|c|<2K^{12}$, $|H|\le|A|$, and $A\subseteq c+H$.
