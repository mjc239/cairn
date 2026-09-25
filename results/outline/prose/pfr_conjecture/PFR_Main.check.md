You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. A "Project
definitions" section first lists the project notions the statements refer to (statement, docstring, body,
fields). Compare the English with the full statement; anything the English attributes to the docstring must
actually be in it.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Definitions are held to the same standard: the English must name the setting the signature assumes
("for an abelian group $G$ and …, $\mathrm{rdist}$ is …"). Replacing an assumption by a stronger one (a metric
space where the Lean has a pseudometric space) is unfaithful too, and so is leaving a restrictive type unstated
(a natural number, a nonnegative real). Citations (theorem or lemma numbers) and remarks are claims too: each must
be supported by the docstring or the Lean. So is a formula or description of what a defined object is: a project
notion's description must agree with its entry under "Project definitions" (statement, docstring, definition body,
fields), and a library notion may only be given its standard mathematical meaning; otherwise flag it. Every variable
needs its type ("$f : G \to \mathbb{C}$", "$m$ a natural number"), every symbol must be introduced, by definition
or by name ("the Ruzsa distance $d[X;Y]$", "the maximal operator $M_{\mathcal B}$"), and no letter may mean two
things. When in doubt, flag it: a false alarm costs one repair, a missed error stays in the outline.
Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `ProbabilityTheory.IsUniform` (structure or class)
Lean: `{Ω : Type uΩ} → {S : Type uS} → [mΩ : MeasurableSpace Ω] → Set S → (Ω → S) → autoParam (Measure Ω) IsUniform._auto_1 → Prop`
Docstring: The assertion that the law of $X$ is the uniform probability measure on a finite set $H$. While in applications $H$ will be non-empty finite set, $X$ measurable, and and $μ$ a probability measure, it could be technically convenient to have a definition that works even without these hypotheses. (For instance, `isUniform` would be well-defined, but false, for infinite `H`). This should probably be refactored, requiring instead that `μ.map X = uniformOn H`.
Fields: `α`, `0`

#### `rdist` (def)
Lean: `{Ω : Type u_1} → {Ω' : Type u_2} → {G : Type u_5} → [mΩ : MeasurableSpace Ω] → [mΩ' : MeasurableSpace Ω'] → [hG : MeasurableSpace G] → [AddCommGroup G] → (Ω → G) → (Ω' → G) → autoParam (Measure Ω) rdist._auto_1 → autoParam (Measure Ω') rdist._auto_3 → ℝ`
Docstring: The Ruzsa distance `rdist X Y` or `d[X ; Y]` between two random variables is defined as `H[X'- Y'] - H[X']/2 - H[Y']/2`, where `X', Y'` are independent copies of `X, Y`.
Definition: `fun {Ω : Type u_1} {Ω' : Type u_2} {G : Type u_5} [MeasurableSpace Ω] [MeasurableSpace Ω'] [MeasurableSpace G] [AddCommGroup G] (X : Ω → G) (Y : Ω' → G) (μ : Measure Ω) (μ' : Measure Ω') => H[fun (x : G × G) => x.1 - x.2; Measure.prod (Measure.map X μ) (Measure.map Y μ')] - H[X; μ] / (2 : ℝ) - H[Y; μ'] / (2 : ℝ)`

#### `ProbabilityTheory.entropy` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
Definition: `fun {Ω : Type u_1} {S : Type u_2} [MeasurableSpace Ω] [MeasurableSpace S] (X : Ω → S) (μ : Measure Ω) => Hm[Measure.map X μ]`

## Translations

### `ProbabilityTheory.IsUniform.measureReal_preimage_sub_zero`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (Uunif : IsUniform (↑A) U volume) (Umeas : Measurable U) (Vunif : IsUniform (↑B) V volume) (Vmeas : Measurable V) (h_indep : IndepFun U V volume) : volume.real ((U - V) ⁻¹' {0}) = ↑(A ∩ B).card / (↑A.card * ↑B.card)`
Lean (full): `∀ {G : Type u_1} {Ω : Type u_2} [inst : AddCommGroup G] [Finite G] [inst_2 : MeasurableSpace G] [MeasurableSingletonClass G] {A B : Finset G} [inst_4 : MeasureSpace Ω] [IsProbabilityMeasure.{u_2} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] {U V : Ω → G} [inst_6 : DecidableEq G], IsUniform (↑A) U volume → Measurable U → IsUniform (↑B) V volume → Measurable V → IndepFun (_mΩ := MeasureSpace.toMeasurableSpace) U V volume → Measure.real (m := MeasureSpace.toMeasurableSpace) volume ((U - V) ⁻¹' {(0 : G)}) = ↑(A ∩ B).card / HMul.hMul (α := ℝ) ↑A.card ↑B.card`
Docstring: Given two independent random variables `U` and `V` uniformly distributed respectively on `A` and `B`, then `U = V` with probability `#(A ∩ B) / #A ⬝ #B`.
English: Let $G$ be a finite abelian group, equipped with a measurable structure in which singletons are measurable, let $\Omega$ be a measure space whose measure $P$ is a probability measure, and let $A, B$ be finite subsets of $G$. Let $U, V : \Omega \to G$ be measurable, independent random variables, with $U$ uniformly distributed on $A$ and $V$ uniformly distributed on $B$. Then $P[U-V=0]=\dfrac{|A\cap B|}{|A|\cdot|B|}$.

### `ProbabilityTheory.IsUniform.measureReal_preimage_sub`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (Uunif : IsUniform (↑A) U volume) (Umeas : Measurable U) (Vunif : IsUniform (↑B) V volume) (Vmeas : Measurable V) (h_indep : IndepFun U V volume) (x : G) : volume.real ((U - V) ⁻¹' {x}) = ↑(A ∩ (B + {x})).card / (↑A.card * ↑B.card)`
Lean (full): `∀ {G : Type u_1} {Ω : Type u_2} [inst : AddCommGroup G] [Finite G] [inst_2 : MeasurableSpace G] [MeasurableSingletonClass G] {A B : Finset G} [inst_4 : MeasureSpace Ω] [IsProbabilityMeasure.{u_2} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] {U V : Ω → G} [inst_6 : DecidableEq G], IsUniform (↑A) U volume → Measurable U → IsUniform (↑B) V volume → Measurable V → IndepFun (_mΩ := MeasureSpace.toMeasurableSpace) U V volume → ∀ (x : G), Measure.real (m := MeasureSpace.toMeasurableSpace) volume ((U - V) ⁻¹' {x}) = ↑(A ∩ (B + {x})).card / HMul.hMul (α := ℝ) ↑A.card ↑B.card`
Docstring: Given two independent random variables `U` and `V` uniformly distributed respectively on `A` and `B`, then `U = V + x` with probability `# (A ∩ (B + x)) / #A ⬝ #B`.
English: Let $G$ be a finite abelian group, equipped with a measurable structure in which singletons are measurable, let $\Omega$ be a measure space whose measure $P$ is a probability measure, and let $A, B$ be finite subsets of $G$. Let $U, V : \Omega \to G$ be measurable, independent random variables, with $U$ uniformly distributed on $A$ and $V$ uniformly distributed on $B$. Then for every $x\in G$, $P[U-V=x]=\dfrac{|A\cap (B+\{x\})|}{|A|\cdot|B|}$.

### `rdist_le_of_isUniform_of_card_sub_le`
Lean (short): `[Countable G] [Finite ↑A] [MeasurableSingletonClass G] (hA₀ : A.Nonempty) (hA : ↑(A - A).ncard ≤ K * ↑A.ncard) [IsProbabilityMeasure volume] (U₀unif : IsUniform A U₀ volume) (U₀meas : Measurable U₀) : d[U₀ # U₀] ≤ Real.log K`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {A : Set G} {K : ℝ} [Countable G] [A_fin : Finite.{u_1 + 1} ↑A] [inst_2 : MeasurableSpace G] [MeasurableSingletonClass G], A.Nonempty → ↑(A - A).ncard ≤ K * ↑A.ncard → ∀ {Ω : Type u_2} [inst_4 : MeasureSpace Ω] [IsProbabilityMeasure.{u_2} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] {U₀ : Ω → G}, IsUniform A U₀ volume → Measurable U₀ → d[U₀ # U₀] ≤ Real.log K`
Docstring: A uniform distribution on a set whose difference set has relative size at most `K` has self Rusza distance at most `log K`.
English: Let $G$ be a countable abelian group, equipped with a measurable structure in which singletons are measurable, let $K\in\mathbb R$, and let $A\subseteq G$ be a finite nonempty set with $|A-A|\le K|A|$. Let $\Omega$ be a measure space whose measure is a probability measure, and let $U_0 : \Omega \to G$ be a measurable random variable uniformly distributed on $A$. Then $d[U_0;U_0]\le \log K$.

### `PFR_conjecture_aux`
Lean (short): `[Countable G] [Module (ZMod 2) G] [Finite G] (hA₀ : A.Nonempty) (hA : ↑(A + A).ncard ≤ K * ↑A.ncard) : ∃ H c, ↑(Nat.card ↑c) ≤ K ^ (13 / 2) * ↑A.ncard ^ (1 / 2) * ↑(↑H).ncard ^ (-1 / 2) ∧ ↑(↑H).ncard ≤ K ^ 11 * ↑A.ncard ∧ ↑A.ncard ≤ K ^ 11 * ↑(↑H).ncard ∧ A ⊆ c + ↑H`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {A : Set G} {K : ℝ} [Countable G] [inst_2 : Module (ZMod (2 : ℕ)) G] [Finite G], A.Nonempty → ↑(A + A).ncard ≤ K * ↑A.ncard → ∃ (H : Submodule (ZMod (2 : ℕ)) G) (c : Set G), ↑(Nat.card.{u_1} ↑c) ≤ K ^ (13 / 2 : ℝ) * HPow.hPow (α := ℝ) ↑A.ncard (1 / 2 : ℝ) * HPow.hPow (α := ℝ) ↑(↑H).ncard (-1 / 2 : ℝ) ∧ ↑(↑H).ncard ≤ K ^ (11 : ℝ) * ↑A.ncard ∧ ↑A.ncard ≤ K ^ (11 : ℝ) * ↑(↑H).ncard ∧ A ⊆ c + ↑H`
Docstring: Auxiliary statement towards the polynomial Freiman-Ruzsa (PFR) conjecture: if `A` is a subset of an elementary abelian 2-group of doubling constant at most $K$, then there exists a subgroup `H` such that `A` can be covered by at most `K^(13/2) |A|^(1/2) / |H|^(1/2)` cosets of `H`, and `H` has the same cardinality as `A` up to a multiplicative factor `K^11`.
English: Let $G$ be an additive commutative group which is countable and finite, and which carries a module structure over $\mathbb{Z}/2\mathbb{Z}$ (i.e. $G$ is an elementary abelian $2$-group, viewed as a vector space over $\mathbb{F}_2$). Let $A \subseteq G$ be a nonempty subset and let $K$ be a real number such that $|A+A| \le K\,|A|$ (cardinalities as real numbers). Then there exist an $\mathbb{F}_2$-submodule (subgroup) $H$ of $G$ and a subset $c \subseteq G$ such that $|c| \le K^{13/2}\,|A|^{1/2}\,|H|^{-1/2}$, $|H| \le K^{11}\,|A|$, $|A| \le K^{11}\,|H|$, and $A \subseteq c + H$. Here all powers are real powers of real numbers.

### `PFR_conjecture`
Lean (short): `[Countable G] [Module (ZMod 2) G] [Finite G] (hA₀ : A.Nonempty) (hA : ↑(A + A).ncard ≤ K * ↑A.ncard) : ∃ H c, ↑(Nat.card ↑c) < 2 * K ^ 12 ∧ (↑H).ncard ≤ A.ncard ∧ A ⊆ c + ↑H`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {A : Set G} {K : ℝ} [Countable G] [inst_2 : Module (ZMod (2 : ℕ)) G] [Finite G], A.Nonempty → ↑(A + A).ncard ≤ K * ↑A.ncard → ∃ (H : Submodule (ZMod (2 : ℕ)) G) (c : Set G), ↑(Nat.card.{u_1} ↑c) < (2 : ℝ) * K ^ (12 : ℝ) ∧ (↑H).ncard ≤ A.ncard ∧ A ⊆ c + ↑H`
Docstring: The polynomial Freiman-Ruzsa (PFR) conjecture: if `A` is a subset of an elementary abelian 2-group of doubling constant at most `K`, then `A` can be covered by at most `2 * K ^ 12` cosets of a subgroup of cardinality at most `|A|`.
English: Let $G$ be an additive commutative group which is countable and finite, and which carries a module structure over $\mathbb{Z}/2\mathbb{Z}$ (i.e. $G$ is an elementary abelian $2$-group, viewed as a vector space over $\mathbb{F}_2$). Let $A \subseteq G$ be a nonempty subset and let $K$ be a real number such that $|A+A| \le K\,|A|$ (cardinalities as real numbers). Then there exist an $\mathbb{F}_2$-submodule (subgroup) $H$ of $G$ and a subset $c \subseteq G$ such that $|c| < 2K^{12}$ (a real power), $|H| \le |A|$, and $A \subseteq c + H$.
