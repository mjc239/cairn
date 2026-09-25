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

### `ProofData`
Lean (short): `(a : outParam ℕ) (q : outParam ℝ) (K : outParam (X → X → ℂ)) (σ₁ : outParam (X → ℤ)) (σ₂ : outParam (X → ℤ)) (F : outParam (Set X)) (G : outParam (Set X)) : Type (u_1 + 1)`
Lean (full): `{X : Type u_1} → outParam ℕ → outParam ℝ → outParam (X → X → ℂ) → outParam (X → ℤ) → outParam (X → ℤ) → outParam (Set X) → outParam (Set X) → [PseudoMetricSpace X] → Type (u_1 + 1)`
English: Defines the structure $\mathrm{ProofData}(a,q,K,\sigma_1,\sigma_2,F,G)$ on $X$, bundling the data (a natural number $a$, a real $q$, a kernel $K:X\times X\to\mathbb C$, functions $\sigma_1,\sigma_2:X\to\mathbb Z$ and sets $F,G\subseteq X$) and assumptions common to most of Chapters 2–7 (except Chapter 3).

### `ProofData.toKernelProofData`
Lean (short): `KernelProofData a K`
Lean (full): `{X : Type u_1} → {a : outParam ℕ} → {q : outParam ℝ} → {K : outParam (X → X → ℂ)} → {σ₁ σ₂ : outParam (X → ℤ)} → {F G : outParam (Set X)} → {inst : PseudoMetricSpace X} → [self : ProofData a q K σ₁ σ₂ F G] → KernelProofData a K`
English: The kernel data $\mathrm{KernelProofData}(a,K)$ underlying a $\mathrm{ProofData}$ structure.

### `defaultS`
Lean (short): `(X : Type u_1) : ℕ`
Lean (full): `(X : Type u_1) → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [ProofData a q K σ₁ σ₂ F G] → ℕ`
English: Defines the natural number $S=\mathrm{defaultS}(X)$ associated with the space $X$.
