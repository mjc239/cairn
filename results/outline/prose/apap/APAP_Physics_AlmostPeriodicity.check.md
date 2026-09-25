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

### `AlmostPeriodicity.LProp`
Lean (short): `[Fintype G] (k : ℕ) (m : ℕ) (ε : ℝ) (f : G → ℂ) (A : Finset G) (a : Fin k → G) : Prop`
Lean (full): `{G : Type u_1} → [Fintype G] → [DecidableEq G] → [AddCommGroup G] → [MeasurableSpace G] → (k : ℕ) → ℕ → ℝ → (G → ℂ) → Finset G → (Fin k → G) → Prop`
English: Let $G$ be a finite (additive commutative) group. For $k, m \in \mathbb{N}$, $\varepsilon \in \mathbb{R}$, $f : G \to \mathbb{C}$, a finite set $A \subseteq G$ and a $k$-tuple $a = (a_1,\dots,a_k) \in G^k$, $\mathrm{LProp}(k,m,\varepsilon,f,A,a)$ is a proposition (a predicate on $k$-tuples $a \in G^k$).

### `AlmostPeriodicity.l`
Lean (short): `[Fintype G] (k : ℕ) (m : ℕ) (ε : ℝ) (f : G → ℂ) (A : Finset G) : Finset (Fin k → G)`
Lean (full): `{G : Type u_1} → [Fintype G] → [DecidableEq G] → [AddCommGroup G] → [MeasurableSpace G] → (k : ℕ) → ℕ → ℝ → (G → ℂ) → Finset G → Finset (Fin k → G)`
English: Let $G$ be a finite (additive commutative) group. For $k, m \in \mathbb{N}$, $\varepsilon \in \mathbb{R}$, $f : G \to \mathbb{C}$ and a finite set $A \subseteq G$, $l(k,m,\varepsilon,f,A)$ is a finite set of $k$-tuples $a \in G^k$.

### `AlmostPeriodicity.just_the_triangle_inequality`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (ha : a ∈ l k m ε f A) (ha' : (a + fun x => t) ∈ l k m ε f A) (hk : 0 < k) (hm : 1 ≤ m) : ‖translate (-t) (mu A ∗ᵈ f) - mu A ∗ᵈ f‖_[2 * ↑m] ≤ 2 * ε * ‖f‖_[2 * ↑m]`
Lean (full): `∀ {G : Type u_1} [inst : Fintype G] {A : Finset G} {f : G → ℂ} {ε : ℝ} {k m : ℕ} [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G] {t : G} {a : Fin k → G}, a ∈ l k m ε f A → (a + fun x => t) ∈ l k m ε f A → (0 : ℕ) < k → (1 : ℕ) ≤ m → ‖translate (-t) (mu A ∗ᵈ f) - mu A ∗ᵈ f‖_[(2 : ENNReal) * ↑m] ≤ (2 : ℝ) * ε * ‖f‖_[(2 : ENNReal) * ↑m]`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. Suppose $a \in l(k,m,\varepsilon,f,A)$ and the shifted tuple $(a_1+t,\dots,a_k+t) \in l(k,m,\varepsilon,f,A)$, with $k > 0$ and $m \ge 1$. Then $\|\tau_{-t}(\mu_A \ast f) - \mu_A \ast f\|_{2m} \le 2\varepsilon \|f\|_{2m}$, where $\mu_A$ is the normalised indicator of $A$, $\ast$ is discrete convolution, $\tau_{-t}$ is translation by $-t$ and $\|\cdot\|_{2m}$ is the discrete $L^{2m}$ norm.

### `AlmostPeriodicity.lemma28`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hε : 0 < ε) (hm : 1 ≤ m) (hk : 64 * ↑m / ε ^ 2 ≤ ↑k) : ↑A.card ^ k / 2 ≤ ↑(l k m ε f A).card`
Lean (full): `∀ {G : Type u_1} [inst : Fintype G] {A : Finset G} {f : G → ℂ} {ε : ℝ} {k m : ℕ} [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G], (0 : ℝ) < ε → (1 : ℕ) ≤ m → (64 : ℝ) * ↑m / ε ^ (2 : ℕ) ≤ ↑k → ↑A.card ^ k / (2 : ℝ) ≤ ↑(l k m ε f A).card`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. If $\varepsilon > 0$, $m \ge 1$ and $64m/\varepsilon^2 \le k$, then $|A|^k/2 \le |l(k,m,\varepsilon,f,A)|$.

### `AlmostPeriodicity.almost_periodicity`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (ε : ℝ) (hε : 0 < ε) (hε' : ε ≤ 1) (m : ℕ) (f : G → ℂ) (hK₂ : 2 ≤ K) (hK : ↑(A.addConst S) ≤ K) : ∃ T, K ^ (-512 * ↑m / ε ^ 2) * ↑S.card ≤ ↑T.card ∧ ∀ t ∈ T, ‖translate t (mu A ∗ᵈ f) - mu A ∗ᵈ f‖_[2 * ↑m] ≤ ε * ‖f‖_[2 * ↑m]`
Lean (full): `∀ {G : Type u_1} [inst : Fintype G] {A S : Finset G} {K : ℝ} [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G] (ε : ℝ), (0 : ℝ) < ε → ε ≤ (1 : ℝ) → ∀ (m : ℕ) (f : G → ℂ), (2 : ℝ) ≤ K → ↑(A.addConst S) ≤ K → ∃ T, K ^ ((-512 : ℝ) * ↑m / ε ^ (2 : ℕ)) * ↑S.card ≤ ↑T.card ∧ ∀ t ∈ T, ‖translate t (mu A ∗ᵈ f) - mu A ∗ᵈ f‖_[(2 : ENNReal) * ↑m] ≤ ε * ‖f‖_[(2 : ENNReal) * ↑m]`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. Let $0 < \varepsilon \le 1$, $m \in \mathbb{N}$, $f : G \to \mathbb{C}$, and let $K \ge 2$ with $\sigma[A,S] \le K$, where $\sigma[A,S]$ is the additive constant `A.addConst S` of the finite sets $A, S \subseteq G$. Then there is a finite set $T \subseteq G$ with $K^{-512m/\varepsilon^2}|S| \le |T|$ such that for every $t \in T$, $\|\tau_t(\mu_A \ast f) - \mu_A \ast f\|_{2m} \le \varepsilon \|f\|_{2m}$ (with $\mu_A$ the normalised indicator of $A$, $\ast$ discrete convolution, $\tau_t$ translation by $t$, and $\|\cdot\|_{2m}$ the discrete $L^{2m}$ norm).

### `AlmostPeriodicity.linfty_almost_periodicity`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (ε : ℝ) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (hK₂ : 2 ≤ K) (hK : ↑(A.addConst S) ≤ K) (B : Finset G) (C : Finset G) (hB : B.Nonempty) (hC : C.Nonempty) : ∃ T, K ^ (-4096 * ↑⌈1 + Real.log (min 1 (↑C.card / ↑B.card))⁻¹⌉ / ε ^ 2) * ↑S.card ≤ ↑T.card ∧ ∀ t ∈ T, ‖translate t ((mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C) - (mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C‖_[⊤] ≤ ε`
Lean (full): `∀ {G : Type u_1} [inst : Fintype G] {A S : Finset G} {K : ℝ} [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G] (ε : ℝ), (0 : ℝ) < ε → ε ≤ (1 : ℝ) → (2 : ℝ) ≤ K → ↑(A.addConst S) ≤ K → ∀ (B C : Finset G), B.Nonempty → C.Nonempty → ∃ T, K ^ ((-4096 : ℝ) * ↑⌈(1 : ℝ) + Real.log (min (1 : ℝ) (↑C.card / ↑B.card))⁻¹⌉ / ε ^ (2 : ℕ)) * ↑S.card ≤ ↑T.card ∧ ∀ t ∈ T, ‖translate t ((mu A ∗ᵈ (↑B).indicator fun x => (1 : ℂ)) ∗ᵈ mu C) - (mu A ∗ᵈ (↑B).indicator fun x => (1 : ℂ)) ∗ᵈ mu C‖_[⊤] ≤ ε`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. Let $0 < \varepsilon \le 1$, $K \ge 2$ with $\sigma[A,S] \le K$, and let $B, C$ be nonempty finite subsets of $G$. Then there is a finite set $T \subseteq G$ with $K^{-4096\lceil 1 + \log(\min(1, |C|/|B|)^{-1})\rceil/\varepsilon^2}|S| \le |T|$ such that for all $t \in T$, $\|\tau_t F - F\|_\infty \le \varepsilon$, where $F = (\mu_A \ast 1_B) \ast \mu_C$. Here $\mu_X$ is the normalised indicator of $X$, $1_B$ is the indicator of $B$, $\ast$ is discrete convolution, $\tau_t$ is translation by $t$, $\|\cdot\|_{\infty}$ is the discrete $L^\infty$ norm, and $\sigma[A,S]$ denotes Lean's `A.addConst S` (the additive doubling constant of $A$ and $S$).

### `AlmostPeriodicity.linfty_almost_periodicity_boosted`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (ε : ℝ) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (k : ℕ) (hk : k ≠ 0) (hK₂ : 2 ≤ K) (hK : ↑(A.addConst S) ≤ K) (hS : S.Nonempty) (B : Finset G) (C : Finset G) (hB : B.Nonempty) (hC : C.Nonempty) : ∃ T, K ^ (-4096 * ↑⌈1 + Real.log (min 1 (↑C.card / ↑B.card))⁻¹⌉ * ↑k ^ 2 / ε ^ 2) * ↑S.card ≤ ↑T.card ∧ ‖mu T ∗ᵈ^ k ∗ᵈ ((mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C) - (mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C‖_[⊤] ≤ ε`
Lean (full): `∀ {G : Type u_1} [inst : Fintype G] {A S : Finset G} {K : ℝ} [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G] (ε : ℝ), (0 : ℝ) < ε → ε ≤ (1 : ℝ) → ∀ (k : ℕ), k ≠ (0 : ℕ) → (2 : ℝ) ≤ K → ↑(A.addConst S) ≤ K → S.Nonempty → ∀ (B C : Finset G), B.Nonempty → C.Nonempty → ∃ T, K ^ ((-4096 : ℝ) * ↑⌈(1 : ℝ) + Real.log (min (1 : ℝ) (↑C.card / ↑B.card))⁻¹⌉ * ↑k ^ (2 : ℕ) / ε ^ (2 : ℕ)) * ↑S.card ≤ ↑T.card ∧ ‖mu T ∗ᵈ^ k ∗ᵈ ((mu A ∗ᵈ (↑B).indicator fun x => (1 : ℂ)) ∗ᵈ mu C) - (mu A ∗ᵈ (↑B).indicator fun x => (1 : ℂ)) ∗ᵈ mu C‖_[⊤] ≤ ε`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. Let $0 < \varepsilon \le 1$, $k \in \mathbb{N}$ with $k \ne 0$, $K \ge 2$ with $\sigma[A,S] \le K$, $S$ nonempty, and $B, C$ nonempty finite subsets of $G$. Then there is a finite set $T \subseteq G$ with $K^{-4096\lceil 1 + \log(\min(1, |C|/|B|)^{-1})\rceil k^2/\varepsilon^2}|S| \le |T|$ and $\|\mu_T^{\ast k} \ast F - F\|_\infty \le \varepsilon$, where $F = (\mu_A \ast 1_B) \ast \mu_C$ and $\mu_T^{\ast k}$ is the $k$-fold convolution power of $\mu_T$. Here $\mu_X$ is the normalised indicator of $X$, $1_B$ is the indicator of $B$, $\ast$ is discrete convolution, $\|\cdot\|_{\infty}$ is the discrete $L^\infty$ norm, and $\sigma[A,S]$ denotes Lean's `A.addConst S` (the additive doubling constant of $A$ and $S$).
