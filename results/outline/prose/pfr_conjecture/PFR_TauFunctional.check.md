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
naturally. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `refPackage`
Lean (short): `(Ω₀₁ : Type u_1) (Ω₀₂ : Type u_2) (G : Type uG) : Type (max (max uG u_1) u_2)`
Lean (full): `(Ω₀₁ : Type u_1) → (Ω₀₂ : Type u_2) → [MeasureSpace Ω₀₁] → [MeasureSpace Ω₀₂] → (G : Type uG) → [MeasurableSpace G] → Type (max (max uG u_1) u_2)`
English: Defines, for types $\Omega_{01},\Omega_{02}$ and $G$, the structure of a reference package: it bundles the fixed data of the main argument (reference spaces and measures, the two reference random variables, and the parameter $\eta$), so that the $\tau$ functional can refer to a single package.

### `tau`
Lean (short): `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω₁ → G) (X₂ : Ω₂ → G) (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) : ℝ`
Lean (full): `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [AddCommGroup G] → [inst_3 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → {Ω₁ : Type u_11} → {Ω₂ : Type u_12} → [inst : MeasurableSpace Ω₁] → [inst_4 : MeasurableSpace Ω₂] → (Ω₁ → G) → (Ω₂ → G) → Measure Ω₁ → Measure Ω₂ → ℝ`
English: For a reference package $p$ and $G$-valued random variables $X_1:\Omega_1\to G$, $X_2:\Omega_2\to G$ with measures $\mu_1,\mu_2$, defines $$\tau[X_1;\mu_1\,\#\,X_2;\mu_2\mid p]:=d[X_1;X_2]+\eta\, d[X^0_1;X_1]+\eta\, d[X^0_2;X_2],$$ where $X^0_1,X^0_2$ and $\eta$ come from $p$.

### `TauMinimizes`
Lean (short): `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) : Prop`
Lean (full): `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [AddCommGroup G] → [inst_3 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → {Ω : Type u_11} → [MeasureSpace Ω] → (Ω → G) → (Ω → G) → Prop`
English: For a reference package $p$ and random variables $X_1,X_2:\Omega\to G$, defines the property that $(X_1,X_2)$ minimizes the $\tau$ functional; it is expressed by comparison with pairs of measures on $G$ (rather than quantifying over all probability spaces).

### `distance_ge_of_min`
Lean (short): `(p : refPackage Ω₀₁ Ω₀₂ G) [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] (h : TauMinimizes p X₁ X₂) (h1 : Measurable X₁') (h2 : Measurable X₂') : d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁'] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂'] - d[p.X₀₂ # X₂]) ≤ d[X₁' # X₂']`
Lean (full): `∀ {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [inst : MeasureSpace Ω₀₁] [inst_1 : MeasureSpace Ω₀₂] {G : Type uG} [inst_2 : AddCommGroup G] [inst_3 : MeasurableSpace G] (p : refPackage Ω₀₁ Ω₀₂ G) {Ω : Type u_3} {Ω'₁ : Type u_7} {Ω'₂ : Type u_8} [inst_4 : MeasureSpace Ω] [hΩ₁ : MeasureSpace Ω'₁] [hΩ₂ : MeasureSpace Ω'₂] [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] {X₁ X₂ : Ω → G} {X₁' : Ω'₁ → G} {X₂' : Ω'₂ → G}, TauMinimizes p X₁ X₂ → Measurable X₁' → Measurable X₂' → d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁'] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂'] - d[p.X₀₂ # X₂]) ≤ d[X₁' # X₂']`
English: Let $p$ be a reference package with reference random variables $X^0_1, X^0_2$ and parameter $\eta$, let $(X_1,X_2)$ minimize $\tau$ for $p$, and let $X_1',X_2'$ be measurable $G$-valued random variables defined on spaces whose ambient measures are probability measures. Then $$d[X_1;X_2]-\eta\left(d[X^0_1;X_1']-d[X^0_1;X_1]\right)-\eta\left(d[X^0_2;X_2']-d[X^0_2;X_2]\right)\le d[X_1';X_2'].$$

### `condRuzsaDistance_ge_of_min`
Lean (short): `[Finite G] (p : refPackage Ω₀₁ Ω₀₂ G) [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [MeasurableSingletonClass G] [Finite S] [MeasurableSingletonClass S] [Finite T] [MeasurableSingletonClass T] (h : TauMinimizes p X₁ X₂) (h1 : Measurable X₁') (h2 : Measurable X₂') (Z : Ω'₁ → S) (W : Ω'₂ → T) (hZ : Measurable Z) (hW : Measurable W) : d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁' | Z] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂' | W] - d[p.X₀₂ # X₂]) ≤ d[X₁' | Z # X₂' | W]`
Lean (full): `∀ {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [inst : MeasureSpace Ω₀₁] [inst_1 : MeasureSpace Ω₀₂] {G : Type uG} [inst_2 : AddCommGroup G] [inst_3 : Finite G] [inst_4 : MeasurableSpace G] (p : refPackage Ω₀₁ Ω₀₂ G) {Ω : Type u_3} {Ω'₁ : Type u_7} {Ω'₂ : Type u_8} {S : Type u_9} {T : Type u_10} [inst_5 : MeasureSpace Ω] [hΩ₁ : MeasureSpace Ω'₁] [hΩ₂ : MeasureSpace Ω'₂] [inst_6 : IsProbabilityMeasure volume] [inst_7 : IsProbabilityMeasure volume] {X₁ X₂ : Ω → G} {X₁' : Ω'₁ → G} {X₂' : Ω'₂ → G} [inst_8 : MeasurableSingletonClass G] [Finite S] [inst_10 : MeasurableSpace S] [MeasurableSingletonClass S] [Finite T] [inst_13 : MeasurableSpace T] [MeasurableSingletonClass T], TauMinimizes p X₁ X₂ → Measurable X₁' → Measurable X₂' → ∀ (Z : Ω'₁ → S) (W : Ω'₂ → T), Measurable Z → Measurable W → d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁' | Z] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂' | W] - d[p.X₀₂ # X₂]) ≤ d[X₁' | Z # X₂' | W]`
English: Let $G$ be a finite abelian group with measurable singletons, and let $S$ and $T$ be finite types with measurable singletons. Let $p$ be a reference package with parameter $\eta$ and reference variables $X^0_1, X^0_2$, and let $(X_1,X_2)$ minimize $\tau$ for $p$. Let $\Omega_1'$ and $\Omega_2'$ be spaces whose measures are probability measures, let $X_1':\Omega_1'\to G$ and $X_2':\Omega_2'\to G$ be measurable, and let $Z:\Omega_1'\to S$ and $W:\Omega_2'\to T$ be measurable. Then $$d[X_1;X_2]-\eta\left(d[X^0_1;X_1'\mid Z]-d[X^0_1;X_1]\right)-\eta\left(d[X^0_2;X_2'\mid W]-d[X^0_2;X_2]\right)\le d[X_1'\mid Z;X_2'\mid W].$$

### `tau_minimizer_exists`
Lean (short): `[IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [Finite G] (p : refPackage Ω₀₁ Ω₀₂ G) [MeasurableSingletonClass G] : ∃ Ω x X₁ X₂, Measurable X₁ ∧ Measurable X₂ ∧ IsProbabilityMeasure volume ∧ TauMinimizes p X₁ X₂`
Lean (full): `∀ {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [inst : MeasureSpace Ω₀₁] [inst_1 : MeasureSpace Ω₀₂] [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] {G : Type uG} [inst_4 : AddCommGroup G] [Finite G] [inst_6 : MeasurableSpace G] (p : refPackage Ω₀₁ Ω₀₂ G) [MeasurableSingletonClass G], ∃ Ω x X₁ X₂, Measurable X₁ ∧ Measurable X₂ ∧ IsProbabilityMeasure volume ∧ TauMinimizes p X₁ X₂`
English: Let $G$ be a finite abelian group with measurable singletons, and let $p$ be a reference package on $G$ whose underlying spaces $\Omega_{01},\Omega_{02}$ carry probability measures. Then there exist a measure space $\Omega$ whose measure is a probability measure and measurable random variables $X_1,X_2:\Omega\to G$ such that $(X_1,X_2)$ minimizes $\tau$ for $p$.
