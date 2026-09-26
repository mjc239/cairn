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

Namespaces open (prefixes omitted): MeasureTheory, TileStructure, Antichain.

### `linearized_metric_carleson`
Lean (short): `[KernelProofData a K] [IsCancellative X (defaultτ a)] (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (hT : ∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, linearizedCarlesonOperator (⇑Q) K f x ≤ ↑(C1_0_2 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [inst_1 : KernelProofData a K] {Q : SimpleFunc X (Θ X)} {f : X → ℂ} [IsCancellative X (defaultτ a)], q ∈ Set.Ioc 1 2 → q.HolderConjugate q' → MeasurableSet F → MeasurableSet G → Measurable f → (fun x => ‖f x‖) ≤ F.indicator 1 → (∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) → ∫⁻ (x : X) in G, linearizedCarlesonOperator (⇑Q) K f x ≤ ↑(C1_0_2 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Docstring: Theorem 1.1.2
Previous English: (Theorem 1.1.2) Let $q\in(1,2]$ and let $q'$ be its Hölder conjugate, let $F,G\subseteq X$ be measurable, and let $f$ be measurable with $|f|\le\mathbf 1_F$ pointwise. Further, suppose that for every $\theta\in\Theta(X)$ the linearized nontangential operator associated with $Q$, $\theta$ and $K$ has bounded strong type $(2,2)$ with constant $C_{T_s}(a)$. Then $$\int_G T_{Q}^{\mathrm{lin}}f(x)\,dx\le C_{1.0.2}(a,q)\,\mu(G)^{1/q'}\,\mu(F)^{1/q},$$ where $T_Q^{\mathrm{lin}}$ is the linearized Carleson operator $\mathrm{linearizedCarlesonOperator}\,Q\,K$.
Checker's issue: Omits the standing assumptions (metric space X with KernelProofData a K) and the cancellativity assumption IsCancellative X (defaultτ a), and does not say Q is a simple function.
