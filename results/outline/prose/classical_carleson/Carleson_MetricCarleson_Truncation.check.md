You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `R_truncation`
Lean: `[KernelProofData a K] [IsCancellative X (defaultτ a)] (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (hR : R = 2 ^ n) (BST_T_Q : ∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, ⨆ R₁ ∈ Set.Ioo R⁻¹ R, ⨆ R₂ ∈ Set.Ioo R₁ R, ‖T_R K Q R₁ R₂ R f x‖ₑ ≤ ↑(C1_0_2 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
English: (Lemma 3.0.2) Let $q\in(1,2]$ and let $q'$ be its Hölder conjugate, let $F,G\subseteq X$ be measurable, and let $f$ be measurable with $|f|\le\mathbf 1_F$ pointwise. Let $R=2^n$, and suppose that for every $\theta\in\Theta(X)$ the linearized nontangential operator associated with $Q$, $\theta$ and $K$ has bounded strong type $(2,2)$ with constant $C_{T_s}(a)$. Then $$\int_G\sup_{R^{-1}<R_1<R}\ \sup_{R_1<R_2<R}\big\|T_R(K,Q,R_1,R_2,R)f(x)\big\|\,dx\le C_{1.0.2}(a,q)\,\mu(G)^{1/q'}\,\mu(F)^{1/q}.$$

### `R_truncation'`
Lean: `[KernelProofData a K] [IsCancellative X (defaultτ a)] (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (hR : R = 2 ^ n) (sF : F ⊆ Metric.ball (cancelPt X) (2 * R)) (sG : G ⊆ Metric.ball (cancelPt X) R) (BST_T_Q : ∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, ⨆ R₁ ∈ Set.Ioo R⁻¹ R, ⨆ R₂ ∈ Set.Ioo R₁ R, ‖T_R K Q R₁ R₂ R f x‖ₑ ≤ ↑(C1_0_2 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
English: Let $q\in(1,2]$ and let $q'$ be its Hölder conjugate, let $F,G\subseteq X$ be measurable, and let $f$ be measurable with $|f|\le\mathbf 1_F$ pointwise. Let $R=2^n$, assume $F\subseteq B(o,2R)$ and $G\subseteq B(o,R)$ where $o=\mathrm{cancelPt}(X)$, and suppose that for every $\theta\in\Theta(X)$ the linearized nontangential operator associated with $Q$, $\theta$ and $K$ has bounded strong type $(2,2)$ with constant $C_{T_s}(a)$. Then $$\int_G\sup_{R^{-1}<R_1<R}\ \sup_{R_1<R_2<R}\big\|T_R(K,Q,R_1,R_2,R)f(x)\big\|\,dx\le C_{1.0.2}(a,q)\,\mu(G)^{1/q'}\,\mu(F)^{1/q}.$$

### `finitary_carleson_step`
Lean: `[KernelProofData a K] [IsCancellative X (defaultτ a)] (CP : CP304 q q' F f σ₁ σ₂) (bG : Bornology.IsBounded G) (mG : MeasurableSet G) : ∃ G' ⊆ G, Bornology.IsBounded G' ∧ MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∫⁻ (x : X) in G \ G', ‖T_lin CP.Q σ₁ σ₂ f x‖ₑ ≤ ↑(C2_0_1 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
English: Let $CP$ be data of type $\mathrm{CP304}(q,q',F,f,\sigma_1,\sigma_2)$ and let $G$ be bounded and measurable. Then there exists a bounded measurable $G'\subseteq G$ with $2\mu(G')\le\mu(G)$ and $$\int_{G\setminus G'}\big\|T_{\mathrm{lin}}(Q_{CP},\sigma_1,\sigma_2)f(x)\big\|\,dx\le C_{2.0.1}(a,q)\,\mu(G)^{1/q'}\,\mu(F)^{1/q}.$$

### `P304.succ`
Lean: `[KernelProofData a K] [IsCancellative X (defaultτ a)] (P : P304 q q' F f σ₁ σ₂) : P304 q q' F f σ₁ σ₂`
English: Given data $P$ of type $\mathrm{P304}(q,q',F,f,\sigma_1,\sigma_2)$ (containing a set $G_n$), constructs the next data $P'$ of the same type, containing $G_{n+1}$.

### `enorm_carlesonOperatorIntegrand_le_T_S`
Lean: `[KernelProofData a K] (hR₁ : 0 < R₁) (hR₂ : R₁ < R₂) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) : ‖carlesonOperatorIntegrand K (Q x) R₁ R₂ f x‖ₑ ≤ ‖T_S Q (L302 a R₁) (U302 a R₂) f x‖ₑ + 4 * ↑(C2_1_3 a) * globalMaximalFunction volume 1 (F.indicator 1) x`
English: Let $0<R_1<R_2$, let $f$ be measurable with $|f|\le\mathbf 1_F$ pointwise. Then $$\big\|\mathrm{carlesonOperatorIntegrand}(K,Q(x),R_1,R_2,f)(x)\big\|\le\big\|T_S(Q,L_{302}(a,R_1),U_{302}(a,R_2))f(x)\big\|+4\,C_{2.1.3}(a)\,M(\mathbf 1_F)(x),$$ where $M$ is the global maximal function with exponent $1$.

### `linearized_truncation`
Lean: `[KernelProofData a K] [IsCancellative X (defaultτ a)] (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (bF : Bornology.IsBounded F) (bG : Bornology.IsBounded G) (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (mσ₁ : Measurable σ₁) (mσ₂ : Measurable σ₂) (rσ₁ : (Set.range σ₁).Finite) (rσ₂ : (Set.range σ₂).Finite) (lσ : σ₁ ≤ σ₂) (BST_T_Q : ∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, ‖T_lin Q σ₁ σ₂ f x‖ₑ ≤ ↑(C3_0_4 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
English: (Lemma 3.0.4) Let $q\in(1,2]$ and let $q'$ be its Hölder conjugate, let $F,G$ be bounded measurable sets, let $f$ be measurable with $|f|\le\mathbf 1_F$, let $\sigma_1,\sigma_2:X\to\mathbb Z$ be measurable with finite ranges and $\sigma_1\le\sigma_2$, and suppose that for every $\theta\in\Theta(X)$ the linearized nontangential operator associated with $Q$, $\theta$ and $K$ has bounded strong type $(2,2)$ with constant $C_{T_s}(a)$. Then $$\int_G\big\|T_{\mathrm{lin}}(Q,\sigma_1,\sigma_2)f(x)\big\|\,dx\le C_{3.0.4}(a,q)\,\mu(G)^{1/q'}\,\mu(F)^{1/q}.$$

### `volume_slice`
Lean: `[KernelProofData a K] [IsCancellative X (defaultτ a)] : 2 * volume (slice CP bG mG (n + 1)).G ≤ volume (slice CP bG mG n).G`
English: Let $CP$ be data of type $\mathrm{CP304}(q,q',F,f,\sigma_1,\sigma_2)$ and let $G$ be bounded and measurable, and write $G_n$ for the set $(\mathrm{slice}\,CP\,G\,n).G$ of the $n$-th slice. Then $2\mu(G_{n+1})\le\mu(G_n)$.

### `slice_G_subset`
Lean: `[KernelProofData a K] [IsCancellative X (defaultτ a)] : (slice CP bG mG (n + 1)).G ⊆ (slice CP bG mG n).G`
English: Let $CP$ be data of type $\mathrm{CP304}(q,q',F,f,\sigma_1,\sigma_2)$ and let $G$ be bounded and measurable, and write $G_n$ for the set $(\mathrm{slice}\,CP\,G\,n).G$ of the $n$-th slice. Then $G_{n+1}\subseteq G_n$.

### `slice_integral_bound`
Lean: `[KernelProofData a K] [IsCancellative X (defaultτ a)] : ∫⁻ (x : X) in (slice CP bG mG n).G \ (slice CP bG mG (n + 1)).G, ‖T_lin CP.Q σ₁ σ₂ f x‖ₑ ≤ ↑(C2_0_1 a q) * volume (slice CP bG mG n).G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
English: Let $CP$ be data of type $\mathrm{CP304}(q,q',F,f,\sigma_1,\sigma_2)$ and let $G$ be bounded and measurable, and write $G_n$ for the set $(\mathrm{slice}\,CP\,G\,n).G$ of the $n$-th slice. Then $$\int_{G_n\setminus G_{n+1}}\big\|T_{\mathrm{lin}}(Q_{CP},\sigma_1,\sigma_2)f(x)\big\|\,dx\le C_{2.0.1}(a,q)\,\mu(G_n)^{1/q'}\,\mu(F)^{1/q}.$$

### `slice_integral_bound_sum`
Lean: `[KernelProofData a K] [IsCancellative X (defaultτ a)] : ∫⁻ (x : X), (G \ (slice CP bG mG (n + 1)).G).indicator (fun x => ‖T_lin CP.Q σ₁ σ₂ f x‖ₑ) x ≤ (↑(C2_0_1 a q) * ∑ i ∈ Finset.range (n + 1), (2⁻¹ ^ i) ^ (↑q')⁻¹) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
English: Let $CP$ be data of type $\mathrm{CP304}(q,q',F,f,\sigma_1,\sigma_2)$ and let $G$ be bounded and measurable, and write $G_n$ for the set $(\mathrm{slice}\,CP\,G\,n).G$ of the $n$-th slice. Then $$\int_X\mathbf 1_{G\setminus G_{n+1}}(x)\,\big\|T_{\mathrm{lin}}(Q_{CP},\sigma_1,\sigma_2)f(x)\big\|\,dx\le\Big(C_{2.0.1}(a,q)\sum_{i=0}^{n}(2^{-i})^{1/q'}\Big)\,\mu(G)^{1/q'}\,\mu(F)^{1/q}.$$ (The integrand is written with an indicator to facilitate the monotone convergence theorem.)

### `S_truncation`
Lean: `[KernelProofData a K] [IsCancellative X (defaultτ a)] (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (bF : Bornology.IsBounded F) (bG : Bornology.IsBounded G) (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (BST_T_Q : ∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, ⨆ s₁ ∈ Finset.Icc (-↑B) ↑B, ⨆ s₂ ∈ Finset.Icc s₁ ↑B, ‖T_S Q s₁ s₂ f x‖ₑ ≤ ↑(C3_0_4 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
English: (Lemma 3.0.3) Let $q\in(1,2]$ and let $q'$ be its Hölder conjugate, let $F,G$ be bounded measurable sets, let $f$ be measurable with $|f|\le\mathbf 1_F$, and suppose that for every $\theta\in\Theta(X)$ the linearized nontangential operator associated with $Q$, $\theta$ and $K$ has bounded strong type $(2,2)$ with constant $C_{T_s}(a)$. Then, with $B$ the blueprint's $S$, $$\int_G\sup_{s_1\in[-B,B]}\ \sup_{s_2\in[s_1,B]}\big\|T_S(Q,s_1,s_2)f(x)\big\|\,dx\le C_{3.0.4}(a,q)\,\mu(G)^{1/q'}\,\mu(F)^{1/q},$$ where $s_1,s_2$ range over integers.
