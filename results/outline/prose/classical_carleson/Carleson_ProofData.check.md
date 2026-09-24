You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProofData`
Lean: `(a : outParam ℕ) (q : outParam ℝ) (K : outParam (X → X → ℂ)) (σ₁ : outParam (X → ℤ)) (σ₂ : outParam (X → ℤ)) (F : outParam (Set X)) (G : outParam (Set X)) : Type (u_1 + 1)`
English: Defines the structure $\mathrm{ProofData}(a,q,K,\sigma_1,\sigma_2,F,G)$ on $X$, bundling the data (a natural number $a$, a real $q$, a kernel $K:X\times X\to\mathbb C$, functions $\sigma_1,\sigma_2:X\to\mathbb Z$ and sets $F,G\subseteq X$) and assumptions common to most of Chapters 2–7 (except Chapter 3).

### `ProofData.toKernelProofData`
Lean: `KernelProofData a K`
English: The kernel data $\mathrm{KernelProofData}(a,K)$ underlying a $\mathrm{ProofData}$ structure.

### `defaultS`
Lean: `(X : Type u_1) : ℕ`
English: Defines the natural number $S=\mathrm{defaultS}(X)$ associated with the space $X$.
