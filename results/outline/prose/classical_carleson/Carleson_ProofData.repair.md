You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): TileStructure, MeasureTheory, Antichain.

### `ProofData`
Lean (short): `(a : outParam ℕ) (q : outParam ℝ) (K : outParam (X → X → ℂ)) (σ₁ : outParam (X → ℤ)) (σ₂ : outParam (X → ℤ)) (F : outParam (Set X)) (G : outParam (Set X)) : Type (u_1 + 1)`
Lean (full): `{X : Type u_1} → outParam ℕ → outParam ℝ → outParam (X → X → ℂ) → outParam (X → ℤ) → outParam (X → ℤ) → outParam (Set X) → outParam (Set X) → [PseudoMetricSpace X] → Type (u_1 + 1)`
Docstring: Data common through most of chapters 2-7 (except 3).
Previous English: Defines the structure $\mathrm{ProofData}(a,q,K,\sigma_1,\sigma_2,F,G)$ on $X$, bundling the data (a natural number $a$, a real $q$, a kernel $K:X\times X\to\mathbb C$, functions $\sigma_1,\sigma_2:X\to\mathbb Z$ and sets $F,G\subseteq X$) and assumptions common to most of Chapters 2–7 (except Chapter 3).
Checker's issue: The definition omits that X is a pseudometric space, which the signature requires.

### `ProofData.toKernelProofData`
Lean (short): `KernelProofData a K`
Lean (full): `{X : Type u_1} → {a : outParam ℕ} → {q : outParam ℝ} → {K : outParam (X → X → ℂ)} → {σ₁ σ₂ : outParam (X → ℤ)} → {F G : outParam (Set X)} → {inst : PseudoMetricSpace X} → [self : ProofData a q K σ₁ σ₂ F G] → KernelProofData a K`
Previous English: The kernel data $\mathrm{KernelProofData}(a,K)$ underlying a $\mathrm{ProofData}$ structure.
Checker's issue: The definition omits that X is a pseudometric space, which the signature requires.

### `defaultS`
Lean (short): `(X : Type u_1) : ℕ`
Lean (full): `(X : Type u_1) → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [ProofData a q K σ₁ σ₂ F G] → ℕ`
Previous English: Defines the natural number $S=\mathrm{defaultS}(X)$ associated with the space $X$.
Checker's issue: The definition omits the setting: a pseudometric space X carrying the ProofData bundle.
