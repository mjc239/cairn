You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption) and the English. Compare the English with the full statement.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Definitions are held to the same standard: the English must name the setting the signature assumes
("for an abelian group $G$ and …, $\mathrm{rdist}$ is …"). Replacing an assumption by a stronger one (a metric
space where the Lean has a pseudometric space) is unfaithful too. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.IsUniform.measureReal_preimage_sub_zero`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (Uunif : IsUniform (↑A) U volume) (Umeas : Measurable U) (Vunif : IsUniform (↑B) V volume) (Vmeas : Measurable V) (h_indep : IndepFun U V volume) : volume.real ((U - V) ⁻¹' {0}) = ↑(A ∩ B).card / (↑A.card * ↑B.card)`
Lean (full): `∀ {G : Type u_1} {Ω : Type u_2} [inst : AddCommGroup G] [Finite G] [inst_2 : MeasurableSpace G] [MeasurableSingletonClass G] {A B : Finset G} [inst_4 : MeasureSpace Ω] [IsProbabilityMeasure volume] {U V : Ω → G} [inst_6 : DecidableEq G], IsUniform (↑A) U volume → Measurable U → IsUniform (↑B) V volume → Measurable V → IndepFun U V volume → volume.real ((U - V) ⁻¹' {(0 : G)}) = ↑(A ∩ B).card / (↑A.card * ↑B.card)`
English: Let $G$ be a finite abelian group, equipped with a measurable structure in which singletons are measurable, let $\Omega$ be a measure space whose measure $P$ is a probability measure, and let $A, B$ be finite subsets of $G$. Let $U, V : \Omega \to G$ be measurable, independent random variables, with $U$ uniformly distributed on $A$ and $V$ uniformly distributed on $B$. Then $P[U-V=0]=\dfrac{|A\cap B|}{|A|\cdot|B|}$.

### `ProbabilityTheory.IsUniform.measureReal_preimage_sub`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (Uunif : IsUniform (↑A) U volume) (Umeas : Measurable U) (Vunif : IsUniform (↑B) V volume) (Vmeas : Measurable V) (h_indep : IndepFun U V volume) (x : G) : volume.real ((U - V) ⁻¹' {x}) = ↑(A ∩ (B + {x})).card / (↑A.card * ↑B.card)`
Lean (full): `∀ {G : Type u_1} {Ω : Type u_2} [inst : AddCommGroup G] [Finite G] [inst_2 : MeasurableSpace G] [MeasurableSingletonClass G] {A B : Finset G} [inst_4 : MeasureSpace Ω] [IsProbabilityMeasure volume] {U V : Ω → G} [inst_6 : DecidableEq G], IsUniform (↑A) U volume → Measurable U → IsUniform (↑B) V volume → Measurable V → IndepFun U V volume → ∀ (x : G), volume.real ((U - V) ⁻¹' {x}) = ↑(A ∩ (B + {x})).card / (↑A.card * ↑B.card)`
English: Let $G$ be a finite abelian group, equipped with a measurable structure in which singletons are measurable, let $\Omega$ be a measure space whose measure $P$ is a probability measure, and let $A, B$ be finite subsets of $G$. Let $U, V : \Omega \to G$ be measurable, independent random variables, with $U$ uniformly distributed on $A$ and $V$ uniformly distributed on $B$. Then for every $x\in G$, $P[U-V=x]=\dfrac{|A\cap (B+\{x\})|}{|A|\cdot|B|}$.

### `rdist_le_of_isUniform_of_card_sub_le`
Lean (short): `[Countable G] [Finite ↑A] [MeasurableSingletonClass G] (hA₀ : A.Nonempty) (hA : ↑(A - A).ncard ≤ K * ↑A.ncard) [IsProbabilityMeasure volume] (U₀unif : IsUniform A U₀ volume) (U₀meas : Measurable U₀) : d[U₀ # U₀] ≤ Real.log K`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {A : Set G} {K : ℝ} [Countable G] [A_fin : Finite ↑A] [inst_2 : MeasurableSpace G] [MeasurableSingletonClass G], A.Nonempty → ↑(A - A).ncard ≤ K * ↑A.ncard → ∀ {Ω : Type u_2} [inst_4 : MeasureSpace Ω] [IsProbabilityMeasure volume] {U₀ : Ω → G}, IsUniform A U₀ volume → Measurable U₀ → d[U₀ # U₀] ≤ Real.log K`
English: Let $G$ be a countable abelian group, equipped with a measurable structure in which singletons are measurable, let $K\in\mathbb R$, and let $A\subseteq G$ be a finite nonempty set with $|A-A|\le K|A|$. Let $\Omega$ be a measure space whose measure is a probability measure, and let $U_0 : \Omega \to G$ be a measurable random variable uniformly distributed on $A$. Then $d[U_0;U_0]\le \log K$.

### `PFR_conjecture_aux`
Lean (short): `[Countable G] [Module (ZMod 2) G] [Finite G] (hA₀ : A.Nonempty) (hA : ↑(A + A).ncard ≤ K * ↑A.ncard) : ∃ H c, ↑(Nat.card ↑c) ≤ K ^ (13 / 2) * ↑A.ncard ^ (1 / 2) * ↑(↑H).ncard ^ (-1 / 2) ∧ ↑(↑H).ncard ≤ K ^ 11 * ↑A.ncard ∧ ↑A.ncard ≤ K ^ 11 * ↑(↑H).ncard ∧ A ⊆ c + ↑H`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {A : Set G} {K : ℝ} [Countable G] [inst_2 : Module (ZMod (2 : ℕ)) G] [Finite G], A.Nonempty → ↑(A + A).ncard ≤ K * ↑A.ncard → ∃ H c, ↑(Nat.card ↑c) ≤ K ^ (13 / 2 : ℝ) * ↑A.ncard ^ (1 / 2 : ℝ) * ↑(↑H).ncard ^ (-1 / 2 : ℝ) ∧ ↑(↑H).ncard ≤ K ^ (11 : ℝ) * ↑A.ncard ∧ ↑A.ncard ≤ K ^ (11 : ℝ) * ↑(↑H).ncard ∧ A ⊆ c + ↑H`
English: Let $G$ be a finite (in particular countable) elementary abelian $2$-group, i.e. a finite vector space over $\mathbb{F}_2$. Let $A$ be a nonempty subset of $G$ with $|A+A|\le K|A|$. Then there exist a subgroup $H\le G$ and a set $c\subseteq G$ such that $|c|\le K^{13/2}|A|^{1/2}|H|^{-1/2}$, $|H|\le K^{11}|A|$, $|A|\le K^{11}|H|$, and $A\subseteq c+H$.

### `PFR_conjecture`
Lean (short): `[Countable G] [Module (ZMod 2) G] [Finite G] (hA₀ : A.Nonempty) (hA : ↑(A + A).ncard ≤ K * ↑A.ncard) : ∃ H c, ↑(Nat.card ↑c) < 2 * K ^ 12 ∧ (↑H).ncard ≤ A.ncard ∧ A ⊆ c + ↑H`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {A : Set G} {K : ℝ} [Countable G] [inst_2 : Module (ZMod (2 : ℕ)) G] [Finite G], A.Nonempty → ↑(A + A).ncard ≤ K * ↑A.ncard → ∃ H c, ↑(Nat.card ↑c) < (2 : ℝ) * K ^ (12 : ℝ) ∧ (↑H).ncard ≤ A.ncard ∧ A ⊆ c + ↑H`
English: Let $G$ be a finite (in particular countable) elementary abelian $2$-group, i.e. a finite vector space over $\mathbb{F}_2$. Let $A$ be a nonempty subset of $G$ with $|A+A|\le K|A|$. Then there exist a subgroup $H\le G$ and a set $c\subseteq G$ with $|c|<2K^{12}$, $|H|\le|A|$, and $A\subseteq c+H$.
