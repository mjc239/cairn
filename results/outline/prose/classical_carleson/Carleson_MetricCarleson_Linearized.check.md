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

### `linearized_metric_carleson`
Lean (short): `[KernelProofData a K] [IsCancellative X (defaultτ a)] (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (hT : ∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, linearizedCarlesonOperator (⇑Q) K f x ≤ ↑(C1_0_2 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [inst_1 : KernelProofData a K] {Q : SimpleFunc X (Θ X)} {f : X → ℂ} [IsCancellative X (defaultτ a)], q ∈ Set.Ioc (1 : NNReal) (2 : NNReal) → q.HolderConjugate q' → MeasurableSet F → MeasurableSet G → Measurable f → (fun x => ‖f x‖) ≤ F.indicator (1 : X → ℝ) → (∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → ∫⁻ (x : X) in G, linearizedCarlesonOperator (⇑Q) K f x ≤ ↑(C1_0_2 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
English: (Theorem 1.1.2) Let $X$ be a metric space with $a \in \mathbb{N}$ and a kernel $K : X \times X \to \mathbb{C}$ satisfying the standing assumptions `KernelProofData a K` (in particular $X$ is a doubling metric measure space and $K$ is a Calderón–Zygmund kernel with parameter $a$), and assume the cancellative condition `IsCancellative X (defaultτ a)` for the family $\Theta(X)$ of frequency functions. Let $Q : X \to \Theta(X)$ be a simple function. Let $q, q' \in \mathbb{R}_{\ge 0}$ with $q\in(1,2]$ and $q'$ the Hölder conjugate of $q$, let $F,G\subseteq X$ be measurable, and let $f : X \to \mathbb{C}$ be measurable with $|f|\le\mathbf 1_F$ pointwise. Further, suppose that for every $\theta\in\Theta(X)$ the linearized nontangential operator associated with $Q$, $\theta$ and $K$ has bounded strong type $(2,2)$ with constant $C_{T_s}(a)$. Then $$\int_G T_{Q}^{\mathrm{lin}}f(x)\,dx\le C_{1.0.2}(a,q)\,\mu(G)^{1/q'}\,\mu(F)^{1/q},$$ where $T_Q^{\mathrm{lin}}$ is the linearized Carleson operator $\mathrm{linearizedCarlesonOperator}\,Q\,K$.
