You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `linearized_metric_carleson`
Lean: `[KernelProofData a K] [IsCancellative X (defaultτ a)] (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (hT : ∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, linearizedCarlesonOperator (⇑Q) K f x ≤ ↑(C1_0_2 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
English: (Theorem 1.1.2) Let $q\in(1,2]$ and let $q'$ be its Hölder conjugate, let $F,G\subseteq X$ be measurable, and let $f$ be measurable with $|f|\le\mathbf 1_F$ pointwise. Further, suppose that for every $\theta\in\Theta(X)$ the linearized nontangential operator associated with $Q$, $\theta$ and $K$ has bounded strong type $(2,2)$ with constant $C_{T_s}(a)$. Then $$\int_G T_{Q}^{\mathrm{lin}}f(x)\,dx\le C_{1.0.2}(a,q)\,\mu(G)^{1/q'}\,\mu(F)^{1/q},$$ where $T_Q^{\mathrm{lin}}$ is the linearized Carleson operator $\mathrm{linearizedCarlesonOperator}\,Q\,K$.
