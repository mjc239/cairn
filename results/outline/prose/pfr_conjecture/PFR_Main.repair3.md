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

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

### `ProbabilityTheory.IsUniform.measureReal_preimage_sub_zero`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (Uunif : IsUniform (↑A) U volume) (Umeas : Measurable U) (Vunif : IsUniform (↑B) V volume) (Vmeas : Measurable V) (h_indep : IndepFun U V volume) : volume.real ((U - V) ⁻¹' {0}) = ↑(A ∩ B).card / (↑A.card * ↑B.card)`
Lean (full): `∀ {G : Type u_1} {Ω : Type u_2} [inst : AddCommGroup G] [Finite G] [inst_2 : MeasurableSpace G] [MeasurableSingletonClass G] {A B : Finset G} [inst_4 : MeasureSpace Ω] [IsProbabilityMeasure volume] {U V : Ω → G} [inst_6 : DecidableEq G], IsUniform (↑A) U volume → Measurable U → IsUniform (↑B) V volume → Measurable V → IndepFun U V volume → volume.real ((U - V) ⁻¹' {0}) = ↑(A ∩ B).card / (↑A.card * ↑B.card)`
Docstring: Given two independent random variables `U` and `V` uniformly distributed respectively on `A` and `B`, then `U = V` with probability `#(A ∩ B) / #A ⬝ #B`.
Previous English: Let $G$ be a finite additive group in which singletons are measurable, let the ambient measure $P$ on $\Omega$ be a probability measure, and let $A, B$ be finite subsets of $G$. Let $U, V : \Omega \to G$ be measurable, independent random variables, with $U$ uniformly distributed on $A$ and $V$ uniformly distributed on $B$. Then $P[U-V=0]=\dfrac{|A\cap B|}{|A|\cdot|B|}$.
Checker's issue: Says 'additive group' but Lean requires an abelian (AddCommGroup) group.

### `ProbabilityTheory.IsUniform.measureReal_preimage_sub`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (Uunif : IsUniform (↑A) U volume) (Umeas : Measurable U) (Vunif : IsUniform (↑B) V volume) (Vmeas : Measurable V) (h_indep : IndepFun U V volume) (x : G) : volume.real ((U - V) ⁻¹' {x}) = ↑(A ∩ (B + {x})).card / (↑A.card * ↑B.card)`
Lean (full): `∀ {G : Type u_1} {Ω : Type u_2} [inst : AddCommGroup G] [Finite G] [inst_2 : MeasurableSpace G] [MeasurableSingletonClass G] {A B : Finset G} [inst_4 : MeasureSpace Ω] [IsProbabilityMeasure volume] {U V : Ω → G} [inst_6 : DecidableEq G], IsUniform (↑A) U volume → Measurable U → IsUniform (↑B) V volume → Measurable V → IndepFun U V volume → ∀ (x : G), volume.real ((U - V) ⁻¹' {x}) = ↑(A ∩ (B + {x})).card / (↑A.card * ↑B.card)`
Docstring: Given two independent random variables `U` and `V` uniformly distributed respectively on `A` and `B`, then `U = V + x` with probability `# (A ∩ (B + x)) / #A ⬝ #B`.
Previous English: Let $G$ be a finite additive group in which singletons are measurable, let the ambient measure $P$ on $\Omega$ be a probability measure, and let $A, B$ be finite subsets of $G$. Let $U, V : \Omega \to G$ be measurable, independent random variables, with $U$ uniformly distributed on $A$ and $V$ uniformly distributed on $B$. Then for every $x\in G$, $P[U-V=x]=\dfrac{|A\cap (B+\{x\})|}{|A|\cdot|B|}$.
Checker's issue: Says 'additive group' but Lean requires an abelian (AddCommGroup) group.

### `rdist_le_of_isUniform_of_card_sub_le`
Lean (short): `[Countable G] [Finite ↑A] [MeasurableSingletonClass G] (hA₀ : A.Nonempty) (hA : ↑(A - A).ncard ≤ K * ↑A.ncard) [IsProbabilityMeasure volume] (U₀unif : IsUniform A U₀ volume) (U₀meas : Measurable U₀) : d[U₀ # U₀] ≤ Real.log K`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {A : Set G} {K : ℝ} [Countable G] [A_fin : Finite ↑A] [inst_2 : MeasurableSpace G] [MeasurableSingletonClass G], A.Nonempty → ↑(A - A).ncard ≤ K * ↑A.ncard → ∀ {Ω : Type u_2} [inst_4 : MeasureSpace Ω] [IsProbabilityMeasure volume] {U₀ : Ω → G}, IsUniform A U₀ volume → Measurable U₀ → d[U₀ # U₀] ≤ Real.log K`
Docstring: A uniform distribution on a set whose difference set has relative size at most `K` has self Rusza distance at most `log K`.
Previous English: Let $G$ be a countable additive group in which singletons are measurable, and let $A\subseteq G$ be a finite nonempty set with $|A-A|\le K|A|$. Suppose the ambient measure on $\Omega$ is a probability measure, and let $U_0 : \Omega \to G$ be a measurable random variable uniformly distributed on $A$. Then $d[U_0;U_0]\le \log K$.
Checker's issue: Says 'additive group' but Lean requires an abelian (AddCommGroup) group.
