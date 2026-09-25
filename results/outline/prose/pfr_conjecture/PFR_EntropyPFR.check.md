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
be supported by the docstring or the Lean. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `tau_strictly_decreases`
Lean (short): `[IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [Module (ZMod 2) G] [Finite G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (h_min : TauMinimizes p X₁ X₂) (hpη : p.η = 1 / 9) : d[X₁ # X₂] = 0`
Lean (full): `∀ {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [inst : MeasureSpace Ω₀₁] [inst_1 : MeasureSpace Ω₀₂] {Ω : Type u_3} [mΩ : MeasureSpace Ω] [IsProbabilityMeasure.{u_3} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] [IsProbabilityMeasure.{u_1} (α := Ω₀₁) (m0 := MeasureSpace.toMeasurableSpace) volume] [IsProbabilityMeasure.{u_2} (α := Ω₀₂) (m0 := MeasureSpace.toMeasurableSpace) volume] {G : Type uG} [inst_5 : AddCommGroup G] [Module (ZMod (2 : ℕ)) G] [Finite G] [inst_8 : MeasurableSpace G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) {X₁ X₂ : Ω → G}, Measurable X₁ → Measurable X₂ → TauMinimizes p X₁ X₂ → p.η = (1 / 9 : ℝ) → d[X₁ # X₂] = (0 : ℝ)`
Docstring: If $d[X_1;X_2] > 0$ then there are $G$-valued random variables $X'_1, X'_2$ such that $\tau[X'_1;X'_2] < \tau[X_1;X_2]$. Phrased in the contrapositive form for convenience of proof.
English: Let $G$ be a finite elementary abelian 2-group (i.e. a finite vector space over $\mathbb{F}_2$) with measurable singletons, and suppose the measures on $\Omega_{01}$, $\Omega_{02}$ and $\Omega$ are probability measures. Let $p$ be a reference package with parameter $\eta$, and let $X_1, X_2 : \Omega \to G$ be measurable random variables such that $(X_1,X_2)$ minimizes $\tau$ for $p$. If $\eta = 1/9$, then $d[X_1;X_2] = 0$. (This is the contrapositive of: if $d[X_1;X_2] > 0$ then there are $G$-valued $X_1', X_2'$ with $\tau[X_1';X_2'] < \tau[X_1;X_2]$.)

### `entropic_PFR_conjecture`
Lean (short): `[IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [Module (ZMod 2) G] [Finite G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) (hpη : p.η = 1 / 9) : ∃ H Ω mΩ U, IsProbabilityMeasure volume ∧ Measurable U ∧ IsUniform (↑H) U volume ∧ d[p.X₀₁ # U] + d[p.X₀₂ # U] ≤ 11 * d[p.X₀₁ # p.X₀₂]`
Lean (full): `∀ {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [inst : MeasureSpace Ω₀₁] [inst_1 : MeasureSpace Ω₀₂] [IsProbabilityMeasure.{u_1} (α := Ω₀₁) (m0 := MeasureSpace.toMeasurableSpace) volume] [IsProbabilityMeasure.{u_2} (α := Ω₀₂) (m0 := MeasureSpace.toMeasurableSpace) volume] {G : Type uG} [inst_4 : AddCommGroup G] [inst_5 : Module (ZMod (2 : ℕ)) G] [Finite G] [inst_7 : MeasurableSpace G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G), p.η = (1 / 9 : ℝ) → ∃ H Ω mΩ U, IsProbabilityMeasure.{uG} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume ∧ Measurable U ∧ IsUniform (↑H) U volume ∧ d[p.X₀₁ # U] + d[p.X₀₂ # U] ≤ (11 : ℝ) * d[p.X₀₁ # p.X₀₂]`
Docstring: `entropic_PFR_conjecture`: For two $G$-valued random variables $X^0_1, X^0_2$, there is some subgroup $H \leq G$ such that $d[X^0_1;U_H] + d[X^0_2;U_H] \le 11 d[X^0_1;X^0_2]$.
English: Let $G$ be a finite elementary abelian 2-group (i.e. a finite vector space over $\mathbb{F}_2$) with measurable singletons, and suppose the measures on $\Omega_{01}$ and $\Omega_{02}$ are probability measures. Let $p$ be a reference package with reference random variables $X^0_1, X^0_2$ (valued in $G$) and parameter $\eta = 1/9$. Then there exist a subgroup $H \le G$, a probability space $\Omega$ and a measurable random variable $U : \Omega \to G$ uniformly distributed on $H$ such that $$d[X^0_1;U] + d[X^0_2;U] \le 11\, d[X^0_1;X^0_2].$$
