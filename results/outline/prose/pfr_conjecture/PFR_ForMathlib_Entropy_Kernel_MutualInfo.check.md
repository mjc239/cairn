You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.Kernel.mutualInfo`
Lean: `(κ : Kernel T (S × U)) (μ : Measure T) : ℝ`
English: For a kernel $\kappa$ from $T$ into a product space $S\times U$ and a measure $\mu$ on $T$, $I_k[\kappa,\mu]$ denotes the mutual information of the kernel $\kappa$ with respect to $\mu$.

### `ProbabilityTheory.Kernel.mutualInfo_nonneg`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass U] [MeasurableSingletonClass T] [Countable T] [IsFiniteMeasure μ] [FiniteSupport μ] (hκ : κ.AEFiniteKernelSupport μ) : 0 ≤ Ik[κ , μ]`
English: Let $\kappa$ be a kernel from $T$ into $S \times U$ that has almost everywhere finite kernel support with respect to the measure $\mu$. Then $0 \le I_k[\kappa,\mu]$.
