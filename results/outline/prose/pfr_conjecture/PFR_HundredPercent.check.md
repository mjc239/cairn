You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. Compare the
English with the full statement; anything the English attributes to the docstring must actually be in it.

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
be supported by the docstring or the Lean. So is a formula or description of what a defined object is: when the
prompt shows neither its definition nor a docstring saying it, the English must not supply one. Every variable
needs its type ("$f : G \to \mathbb{C}$", "$m$ a natural number"), every symbol must be introduced (notation such
as $M_{\mathcal B}$ included), and no letter may mean two things. When in doubt, flag it: a false alarm costs one
repair, a missed error stays in the outline. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `symmGroup`
Lean (short): `[MeasurableAdd₂ G] (X : Ω → G) (hX : Measurable X) : AddSubgroup G`
Lean (full): `{Ω : Type u_1} → {G : Type u_2} → [inst : MeasureSpace Ω] → [inst_1 : MeasurableSpace G] → [inst_2 : AddCommGroup G] → [MeasurableAdd₂ G] → (X : Ω → G) → Measurable X → AddSubgroup G`
Docstring: The symmetry group Sym of $X$: the set of all $h ∈ G$ such that $X + h$ has an identical distribution to $X$.
English: Let $\Omega$ be a measure space and let $G$ be an abelian group with a measurable space structure for which addition $G\times G\to G$ is measurable. For a measurable random variable $X:\Omega\to G$, this defines an additive subgroup $\mathrm{Sym}[X]$ of $G$. According to its docstring, it is the symmetry group of $X$: the set of all $h\in G$ such that $X+h$ has an identical distribution to $X$.

### `sub_mem_symmGroup`
Lean (short): `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X) (hdist : d[X # X] = 0) (hx : volume (X ⁻¹' {x}) ≠ 0) (hy : volume (X ⁻¹' {y}) ≠ 0) : x - y ∈ symmGroup X hX`
Lean (full): `∀ {Ω : Type u_1} {G : Type u_2} [inst : MeasureSpace Ω] [inst_1 : MeasurableSpace G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableAdd₂ G] {X : Ω → G} [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure.{u_1} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] (hX : Measurable X), d[X # X] = (0 : ℝ) → ∀ {x y : G}, (volume : Measure Ω) (X ⁻¹' {x}) ≠ (0 : ENNReal) → (volume : Measure Ω) (X ⁻¹' {y}) ≠ (0 : ENNReal) → Membership.mem (γ := AddSubgroup G) (symmGroup X hX) (x - y)`
Docstring: If $d[X ;X]=0$, and $x,y \in G$ are such that $P[X=x], P[X=y]>0$, then $x-y \in \mathrm{Sym}[X]$.
English: Let $G$ be a finite abelian group with measurable singletons and measurable addition, and let $\Omega$ be a probability space (its measure $P$ is a probability measure). Let $X:\Omega\to G$ be a measurable random variable with $d[X;X]=0$, and let $x,y\in G$ satisfy $P[X=x]\neq 0$ and $P[X=y]\neq 0$. Then $x-y\in\mathrm{Sym}[X]$.

### `isUniform_sub_const_of_rdist_eq_zero`
Lean (short): `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X) (hdist : d[X # X] = 0) (hx₀ : volume (X ⁻¹' {x₀}) ≠ 0) : IsUniform (↑(symmGroup X hX)) (fun ω => X ω - x₀) volume`
Lean (full): `∀ {Ω : Type u_1} {G : Type u_2} [inst : MeasureSpace Ω] [inst_1 : MeasurableSpace G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableAdd₂ G] {X : Ω → G} [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure.{u_1} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] (hX : Measurable X), d[X # X] = (0 : ℝ) → ∀ {x₀ : G}, (volume : Measure Ω) (X ⁻¹' {x₀}) ≠ (0 : ENNReal) → IsUniform (↑(symmGroup X hX)) (fun (ω : Ω) => X ω - x₀) volume`
Docstring: If `d[X # X] = 0`, then `X - x₀` is the uniform distribution on the subgroup of `G` stabilizing the distribution of `X`, for any `x₀` of positive probability.
English: Let $G$ be a finite abelian group with measurable singletons and measurable addition, and let $\Omega$ be a probability space (its measure $P$ is a probability measure). Let $X:\Omega\to G$ be a measurable random variable with $d[X;X]=0$, and let $x_0\in G$ satisfy $P[X=x_0]\neq 0$. Then $X-x_0$ is uniformly distributed on the subgroup $\mathrm{Sym}[X]$ of $G$.

### `exists_isUniform_of_rdist_self_eq_zero`
Lean (short): `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X) (hdist : d[X # X] = 0) : ∃ H U, Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = 0`
Lean (full): `∀ {Ω : Type u_1} {G : Type u_2} [inst : MeasureSpace Ω] [inst_1 : MeasurableSpace G] [inst_2 : AddCommGroup G] [MeasurableAdd₂ G] {X : Ω → G} [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure.{u_1} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume], Measurable X → d[X # X] = (0 : ℝ) → ∃ (H : AddSubgroup G) (U : Ω → G), Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = (0 : ℝ)`
Docstring: If $d[X ;X]=0$, then there exists a subgroup $H \leq G$ such that $d[X ;U_H] = 0$.
English: Let $G$ be a finite additive commutative group equipped with a measurable space structure in which singletons are measurable and addition $G\times G\to G$ is measurable. Let $\Omega$ be a measure space whose measure $\mu$ is a probability measure, and let $X:\Omega\to G$ be a measurable function whose Ruzsa distance to itself is $d[X;X]=0$. Then there exist an additive subgroup $H\le G$ and a measurable function $U:\Omega\to G$ that is uniformly distributed on $H$ with respect to $\mu$, such that $d[X;U]=0$.

### `exists_isUniform_of_rdist_eq_zero`
Lean (short): `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] (hX : Measurable X) (hX' : Measurable X') (hdist : d[X # X'] = 0) : ∃ H U, Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = 0 ∧ d[X' # U] = 0`
Lean (full): `∀ {Ω : Type u_1} {G : Type u_2} [inst : MeasureSpace Ω] [inst_1 : MeasurableSpace G] [inst_2 : AddCommGroup G] [MeasurableAdd₂ G] {X : Ω → G} [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure.{u_1} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] {Ω' : Type u_3} [inst_7 : MeasureSpace Ω'] [IsProbabilityMeasure.{u_3} (α := Ω') (m0 := MeasureSpace.toMeasurableSpace) volume] {X' : Ω' → G}, Measurable X → Measurable X' → d[X # X'] = (0 : ℝ) → ∃ (H : AddSubgroup G) (U : Ω → G), Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = (0 : ℝ) ∧ d[X' # U] = (0 : ℝ)`
Docstring: If $d[X_1;X_2]=0$, then there exists a subgroup $H \leq G$ such that $d[X_1;U_H] = d[X_2;U_H] = 0$. Follows from the preceding claim by the triangle inequality.
English: Let $G$ be a finite additive commutative group equipped with a measurable space structure in which singletons are measurable and addition $G\times G\to G$ is measurable. Let $\Omega$ and $\Omega'$ be measure spaces whose measures $\mu$ and $\mu'$ are probability measures, and let $X:\Omega\to G$ and $X':\Omega'\to G$ be measurable functions with Ruzsa distance $d[X;X']=0$. Then there exist an additive subgroup $H\le G$ and a measurable function $U:\Omega\to G$ that is uniformly distributed on $H$ with respect to $\mu$, such that $d[X;U]=0$ and $d[X';U]=0$.
