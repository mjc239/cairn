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
be supported by the docstring or the Lean. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProofData`
Lean (short): `(a : outParam ℕ) (q : outParam ℝ) (K : outParam (X → X → ℂ)) (σ₁ : outParam (X → ℤ)) (σ₂ : outParam (X → ℤ)) (F : outParam (Set X)) (G : outParam (Set X)) : Type (u_1 + 1)`
Lean (full): `{X : Type u_1} → outParam ℕ → outParam ℝ → outParam (X → X → ℂ) → outParam (X → ℤ) → outParam (X → ℤ) → outParam (Set X) → outParam (Set X) → [PseudoMetricSpace X] → Type (u_1 + 1)`
Docstring: Data common through most of chapters 2-7 (except 3).
English: Let $X$ be a pseudometric space. Definition: given a natural number $a$, a real number $q$, a kernel $K : X \times X \to \mathbb{C}$, functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$, the type of structures $\mathrm{ProofData}(a, q, K, \sigma_1, \sigma_2, F, G)$ on $X$; according to the docstring, it bundles the data common throughout most of Chapters 2–7 (except Chapter 3).

### `ProofData.toKernelProofData`
Lean (short): `KernelProofData a K`
Lean (full): `{X : Type u_1} → {a : outParam ℕ} → {q : outParam ℝ} → {K : outParam (X → X → ℂ)} → {σ₁ σ₂ : outParam (X → ℤ)} → {F G : outParam (Set X)} → {inst : PseudoMetricSpace X} → [self : ProofData a q K σ₁ σ₂ F G] → KernelProofData a K`
English: Let $X$ be a pseudometric space, $a$ a natural number, $q$ a real number, $K : X \times X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$. Definition: the kernel data $\mathrm{KernelProofData}(a, K)$ underlying a structure $\mathrm{ProofData}(a, q, K, \sigma_1, \sigma_2, F, G)$.

### `defaultS`
Lean (short): `(X : Type u_1) : ℕ`
Lean (full): `(X : Type u_1) → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [ProofData a q K σ₁ σ₂ F G] → ℕ`
English: Let $X$ be a pseudometric space equipped with $\mathrm{ProofData}(a, q, K, \sigma_1, \sigma_2, F, G)$ (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \times X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$, $F, G \subseteq X$). Definition: the natural number $S = \mathrm{defaultS}(X)$ associated with this data.
