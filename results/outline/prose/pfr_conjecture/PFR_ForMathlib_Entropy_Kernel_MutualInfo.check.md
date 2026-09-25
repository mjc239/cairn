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

### `ProbabilityTheory.Kernel.mutualInfo`
Lean (short): `(κ : Kernel T (S × U)) (μ : Measure T) : ℝ`
Lean (full): `{S : Type u_2} → {T : Type u_3} → {U : Type u_4} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → [inst_2 : MeasurableSpace U] → Kernel T (S × U) → Measure T → ℝ`
English: For a kernel $\kappa$ from $T$ into a product space $S\times U$ and a measure $\mu$ on $T$, $I_k[\kappa,\mu]$ denotes the mutual information of the kernel $\kappa$ with respect to $\mu$.

### `ProbabilityTheory.Kernel.mutualInfo_nonneg`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass U] [MeasurableSingletonClass T] [Countable T] [IsFiniteMeasure μ] [FiniteSupport μ] (hκ : κ.AEFiniteKernelSupport μ) : 0 ≤ Ik[κ , μ]`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [inst_2 : MeasurableSpace U] [MeasurableSingletonClass S] [MeasurableSingletonClass U] [MeasurableSingletonClass T] [Countable T] {κ : Kernel T (S × U)} {μ : Measure T} [IsFiniteMeasure μ] [FiniteSupport μ], κ.AEFiniteKernelSupport μ → (0 : ℝ) ≤ Ik[κ , μ]`
English: Let $S$, $U$, $T$ have measurable singletons, with $T$ countable. Let $\mu$ be a finite measure on $T$ with finite support, and let $\kappa$ be a kernel from $T$ into $S \times U$ that has almost everywhere finite kernel support with respect to $\mu$. Then $0 \le I_k[\kappa,\mu]$.
