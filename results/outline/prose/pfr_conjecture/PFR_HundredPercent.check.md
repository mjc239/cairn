You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `symmGroup`
Lean: `[MeasurableAdd₂ G] (X : Ω → G) (hX : Measurable X) : AddSubgroup G`
English: For a measurable random variable $X:\Omega\to G$, defines the symmetry group $\mathrm{Sym}[X]$: the additive subgroup of $G$ consisting of all $h\in G$ such that $X+h$ has the same distribution as $X$.

### `sub_mem_symmGroup`
Lean: `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X) (hdist : d[X # X] = 0) (hx : volume (X ⁻¹' {x}) ≠ 0) (hy : volume (X ⁻¹' {y}) ≠ 0) : x - y ∈ symmGroup X hX`
English: Let $X$ be a measurable $G$-valued random variable with $d[X;X]=0$, and let $x,y\in G$ satisfy $P[X=x]\neq 0$ and $P[X=y]\neq 0$. Then $x-y\in\mathrm{Sym}[X]$.

### `isUniform_sub_const_of_rdist_eq_zero`
Lean: `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X) (hdist : d[X # X] = 0) (hx₀ : volume (X ⁻¹' {x₀}) ≠ 0) : IsUniform (↑(symmGroup X hX)) (fun ω => X ω - x₀) volume`
English: Let $X$ be a measurable $G$-valued random variable with $d[X;X]=0$, and let $x_0\in G$ satisfy $P[X=x_0]\neq 0$. Then $X-x_0$ is uniformly distributed on the subgroup $\mathrm{Sym}[X]$.

### `exists_isUniform_of_rdist_self_eq_zero`
Lean: `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X) (hdist : d[X # X] = 0) : ∃ H U, Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = 0`
English: Let $X$ be a measurable $G$-valued random variable with $d[X;X]=0$. Then there exist a subgroup $H\le G$ and a measurable random variable $U$, uniformly distributed on $H$, such that $d[X;U]=0$.

### `exists_isUniform_of_rdist_eq_zero`
Lean: `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] (hX : Measurable X) (hX' : Measurable X') (hdist : d[X # X'] = 0) : ∃ H U, Measurable U ∧ IsUniform (↑H) U volume ∧ d[X # U] = 0 ∧ d[X' # U] = 0`
English: Let $X$ and $X'$ be measurable $G$-valued random variables with $d[X;X']=0$. Then there exist a subgroup $H\le G$ and a measurable random variable $U$, uniformly distributed on $H$, such that $d[X;U]=0$ and $d[X';U]=0$.
