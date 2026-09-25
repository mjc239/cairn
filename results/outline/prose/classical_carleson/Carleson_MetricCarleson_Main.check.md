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

### `metric_carleson`
Lean (short): `[KernelProofData a K] [IsCancellative X (defaultτ a)] (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (hT : HasBoundedStrongType (fun x1 x2 => nontangentialOperator K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, carlesonOperator K f x ≤ ↑(C1_0_2 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [inst_1 : KernelProofData a K] {f : X → ℂ} [IsCancellative X (defaultτ a)], q ∈ Set.Ioc (1 : NNReal) (2 : NNReal) → q.HolderConjugate q' → MeasurableSet F → MeasurableSet G → Measurable f → (fun (x : X) => ‖f x‖) ≤ F.indicator (1 : X → ℝ) → HasBoundedStrongType (ε₁ := ℂ) (ε₂ := ENNReal) (α := X) (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (fun (x1 : X → ℂ) (x2 : X) => nontangentialOperator K x1 x2) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a) → ∫⁻ (x : X) in G, carlesonOperator K f x ≤ ↑(C1_0_2 a q) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) (↑q')⁻¹ * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (↑q)⁻¹`
Docstring: Theorem 1.1.1
English: (Theorem 1.1.1) Let $X$ be a metric space, $a\in\mathbb N$, and $K : X\times X\to\mathbb C$ a kernel satisfying the standing assumptions `KernelProofData a K` (so $X$ carries a doubling measure $\mu$ with parameter depending on $a$ and $K$ satisfies the kernel bounds), and assume the cancellative property `IsCancellative X (defaultτ a)` holds. Let $q,q'$ be nonnegative reals with $q\in(1,2]$ and $q'$ its Hölder conjugate, let $F,G\subseteq X$ be measurable, and let $f:X\to\mathbb C$ be measurable with $|f|\le\mathbf 1_F$ pointwise. Suppose that the nontangential operator associated with $K$ has bounded strong type $(2,2)$ (with respect to $\mu$) with constant $C_{T_s}(a)$. Then $$\int_G T f(x)\,d\mu(x)\le C_{1.0.2}(a,q)\,\mu(G)^{1/q'}\,\mu(F)^{1/q},$$ where $T$ is the Carleson operator $\mathrm{carlesonOperator}\,K$.
