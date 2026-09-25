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

### `symmGroup`
Lean (short): `[MeasurableAdd₂ G] (X : Ω → G) (hX : Measurable X) : AddSubgroup G`
Lean (full): `{Ω : Type u_1} → {G : Type u_2} → [inst : MeasureSpace Ω] → [inst_1 : MeasurableSpace G] → [inst_2 : AddCommGroup G] → [MeasurableAdd₂ G] → (X : Ω → G) → Measurable X → AddSubgroup G`
English: For a measurable random variable $X:\Omega\to G$, defines the symmetry group $\mathrm{Sym}[X]$: the additive subgroup of $G$ consisting of all $h\in G$ such that $X+h$ has the same distribution as $X$.

### `sub_mem_symmGroup`
Lean (short): `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X) (hdist : d[X # X] = 0) (hx : volume (X ⁻¹' {x}) ≠ 0) (hy : volume (X ⁻¹' {y}) ≠ 0) : x - y ∈ symmGroup X hX`
Lean (full): `∀ {Ω : Type u_1} {G : Type u_2} [inst : MeasureSpace Ω] [inst_1 : MeasurableSpace G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableAdd₂ G] {X : Ω → G} [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X), d[X # X] = (0 : ℝ) → ∀ {x y : G}, volume (X ⁻¹' {x}) ≠ (0 : ENNReal) → volume (X ⁻¹' {y}) ≠ (0 : ENNReal) → x - y ∈ symmGroup X hX`
English: Let $G$ be a finite abelian group with measurable singletons and measurable addition, and let $\Omega$ be a probability space (its measure $P$ is a probability measure). Let $X:\Omega\to G$ be a measurable random variable with $d[X;X]=0$, and let $x,y\in G$ satisfy $P[X=x]\neq 0$ and $P[X=y]\neq 0$. Then $x-y\in\mathrm{Sym}[X]$.

### `isUniform_sub_const_of_rdist_eq_zero`
Lean (short): `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X) (hdist : d[X # X] = 0) (hx₀ : volume (X ⁻¹' {x₀}) ≠ 0) : IsUniform (↑(symmGroup X hX)) (fun ω => X ω - x₀) volume`
Lean (full): `∀ {Ω : Type u_1} {G : Type u_2} [inst : MeasureSpace Ω] [inst_1 : MeasurableSpace G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableAdd₂ G] {X : Ω → G} [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X), d[X # X] = (0 : ℝ) → ∀ {x₀ : G}, volume (X ⁻¹' {x₀}) ≠ (0 : ENNReal) → IsUniform (↑(symmGroup X hX)) (fun ω => X ω - x₀) volume`
English: Let $G$ be a finite abelian group with measurable singletons and measurable addition, and let $\Omega$ be a probability space (its measure $P$ is a probability measure). Let $X:\Omega\to G$ be a measurable random variable with $d[X;X]=0$, and let $x_0\in G$ satisfy $P[X=x_0]\neq 0$. Then $X-x_0$ is uniformly distributed on the subgroup $\mathrm{Sym}[X]$ of $G$.

### `exists_isUniform_of_rdist_self_eq_zero`
Lean (short): `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X) (hdist : d[X # X] = 0) : ∃ H U, Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = 0`
Lean (full): `∀ {Ω : Type u_1} {G : Type u_2} [inst : MeasureSpace Ω] [inst_1 : MeasurableSpace G] [inst_2 : AddCommGroup G] [MeasurableAdd₂ G] {X : Ω → G} [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume], Measurable X → d[X # X] = (0 : ℝ) → ∃ H U, Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = (0 : ℝ)`
English: Let $G$ be a finite abelian group with measurable singletons and measurable addition, and let $\Omega$ be a probability space (its measure is a probability measure). Let $X:\Omega\to G$ be a measurable random variable with $d[X;X]=0$. Then there exist a subgroup $H\le G$ and a measurable random variable $U$, uniformly distributed on $H$, such that $d[X;U]=0$.

### `exists_isUniform_of_rdist_eq_zero`
Lean (short): `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] (hX : Measurable X) (hX' : Measurable X') (hdist : d[X # X'] = 0) : ∃ H U, Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = 0 ∧ d[X' # U] = 0`
Lean (full): `∀ {Ω : Type u_1} {G : Type u_2} [inst : MeasureSpace Ω] [inst_1 : MeasurableSpace G] [inst_2 : AddCommGroup G] [MeasurableAdd₂ G] {X : Ω → G} [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] {Ω' : Type u_3} [inst_7 : MeasureSpace Ω'] [IsProbabilityMeasure volume] {X' : Ω' → G}, Measurable X → Measurable X' → d[X # X'] = (0 : ℝ) → ∃ H U, Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = (0 : ℝ) ∧ d[X' # U] = (0 : ℝ)`
English: Let $G$ be a finite abelian group with measurable singletons and measurable addition. Let $X:\Omega\to G$ and $X':\Omega'\to G$ be measurable random variables on probability spaces $\Omega$ and $\Omega'$ (both underlying measures being probability measures) with $d[X;X']=0$. Then there exist a subgroup $H\le G$ and a measurable random variable $U$, uniformly distributed on $H$, such that $d[X;U]=0$ and $d[X';U]=0$.
