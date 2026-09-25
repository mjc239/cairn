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
A definition whose body is shown must be described by what it defines (in words or a formula that agrees with the
body), not only by a paraphrase of its docstring. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `rdist` (def)
Lean: `{Ω : Type u_1} → {Ω' : Type u_2} → {G : Type u_5} → [mΩ : MeasurableSpace Ω] → [mΩ' : MeasurableSpace Ω'] → [hG : MeasurableSpace G] → [AddCommGroup G] → (Ω → G) → (Ω' → G) → autoParam (Measure Ω) rdist._auto_1 → autoParam (Measure Ω') rdist._auto_3 → ℝ`
Docstring: The Ruzsa distance `rdist X Y` or `d[X ; Y]` between two random variables is defined as `H[X'- Y'] - H[X']/2 - H[Y']/2`, where `X', Y'` are independent copies of `X, Y`.
Definition: `fun {Ω : Type u_1} {Ω' : Type u_2} {G : Type u_5} [MeasurableSpace Ω] [MeasurableSpace Ω'] [MeasurableSpace G] [AddCommGroup G] (X : Ω → G) (Y : Ω' → G) (μ : Measure Ω) (μ' : Measure Ω') => H[fun (x : G × G) => x.1 - x.2; Measure.prod (Measure.map X μ) (Measure.map Y μ')] - H[X; μ] / (2 : ℝ) - H[Y; μ'] / (2 : ℝ)`

#### `ProbabilityTheory.IsUniform` (structure or class)
Lean: `{Ω : Type uΩ} → {S : Type uS} → [mΩ : MeasurableSpace Ω] → Set S → (Ω → S) → autoParam (Measure Ω) IsUniform._auto_1 → Prop`
Docstring: The assertion that the law of $X$ is the uniform probability measure on a finite set $H$. While in applications $H$ will be non-empty finite set, $X$ measurable, and and $μ$ a probability measure, it could be technically convenient to have a definition that works even without these hypotheses. (For instance, `isUniform` would be well-defined, but false, for infinite `H`). This should probably be refactored, requiring instead that `μ.map X = uniformOn H`.
Constructor (every field with its type): `∀ {Ω : Type uΩ} {S : Type uS} [mΩ : MeasurableSpace Ω] {H : Set S} {X : Ω → S} {μ : autoParam (Measure Ω) IsUniform._auto_1}, (∀ ⦃x : S⦄, x ∈ H → ∀ ⦃y : S⦄, y ∈ H → Eq (α := ENNReal) (μ (X ⁻¹' {x}) : ENNReal) (μ (X ⁻¹' {y}) : ENNReal)) → μ (X ⁻¹' Hᶜ) = (0 : ENNReal) → IsUniform H X μ`

#### `ProbabilityTheory.entropy` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
Definition: `fun {Ω : Type u_1} {S : Type u_2} [MeasurableSpace Ω] [MeasurableSpace S] (X : Ω → S) (μ : Measure Ω) => Hm[Measure.map X μ]`

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

## Translations

### `symmGroup`
Lean (short): `[MeasurableAdd₂ G] (X : Ω → G) (hX : Measurable X) : AddSubgroup G`
Lean (full): `{Ω : Type u_1} → {G : Type u_2} → [inst : MeasureSpace Ω] → [inst_1 : MeasurableSpace G] → [inst_2 : AddCommGroup G] → [MeasurableAdd₂ G] → (X : Ω → G) → Measurable X → AddSubgroup G`
Definition: `fun {Ω : Type u_1} {G : Type u_2} [MeasureSpace Ω] [MeasurableSpace G] [AddCommGroup G] [MeasurableAdd₂ G] (X : Ω → G) (hX : Measurable X) => { carrier := {x : G | IdentDistrib X (fun (ω : Ω) => X ω + x) volume volume}, add_mem' := ⋯, zero_mem' := ⋯, neg_mem' := ⋯ }`
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
