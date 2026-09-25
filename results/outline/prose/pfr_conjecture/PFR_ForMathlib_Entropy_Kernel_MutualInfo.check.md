You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. A "Project
definitions" section first lists the project notions the statements refer to (statement, docstring, body,
fields). Compare the English with the full statement; anything the English attributes to the docstring must
actually be in it.

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
be supported by the docstring or the Lean. So is a formula or description of what a defined object is: a project
notion's description must agree with its entry under "Project definitions" (statement, docstring, definition body,
fields), and a library notion may only be given its standard mathematical meaning; otherwise flag it. Every variable
needs its type ("$f : G \to \mathbb{C}$", "$m$ a natural number"), every symbol must be introduced, by definition
or by name ("the Ruzsa distance $d[X;Y]$", "the maximal operator $M_{\mathcal B}$"), and no letter may mean two
things. When in doubt, flag it: a false alarm costs one repair, a missed error stays in the outline.
A definition whose body is shown must be described by what it defines (in words or a formula that agrees with the
body), not only by a paraphrase of its docstring. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `ProbabilityTheory.Kernel.entropy` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → ℝ`
Docstring: Entropy of a kernel with respect to a measure.
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) (μ : Measure T) => ∫ (x : T), (fun (y : T) => measureEntropy.{u_2} (S := S) (κ y)) x ∂μ`

#### `ProbabilityTheory.FiniteSupport` (structure or class)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) FiniteSupport._auto_1 → Prop`
Docstring: A measure has finite support if there exists a finite set whose complement has zero measure.
Constructor (every field with its type): `∀ {S : Type u_2} [inst : MeasurableSpace S] {μ : autoParam (Measure S) FiniteSupport._auto_1}, (∃ (A : Finset S), ∀ᵐ (x : S) ∂μ, x ∈ A) → FiniteSupport μ`

#### `ProbabilityTheory.Kernel.AEFiniteKernelSupport` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → Prop`
Docstring: A kernel `κ` has almost everywhere finite support wrt a measure `μ` if, for almost every point `t`, then `κ t` has finite support. Note that we don't require any uniformity wrt `t`.
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) (μ : Measure T) => ∀ᵐ (t : T) ∂μ, ∃ (A : Finset S), (κ t : Measure S) (↑A)ᶜ = (0 : ENNReal)`

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

## Translations

### `ProbabilityTheory.Kernel.mutualInfo`
Lean (short): `(κ : Kernel T (S × U)) (μ : Measure T) : ℝ`
Lean (full): `{S : Type u_2} → {T : Type u_3} → {U : Type u_4} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → [inst_2 : MeasurableSpace U] → Kernel T (S × U) → Measure T → ℝ`
Definition: `fun {S : Type u_2} {T : Type u_3} {U : Type u_4} [MeasurableSpace S] [MeasurableSpace T] [MeasurableSpace U] (κ : Kernel T (S × U)) (μ : Measure T) => Hk[κ.fst , μ] + Hk[κ.snd , μ] - Hk[κ , μ]`
Docstring: Mutual information of a kernel into a product space with respect to a measure.
English: Definition. Let $S$, $T$ and $U$ be measurable spaces. For a kernel $\kappa$ from $T$ to the product space $S\times U$ and a measure $\mu$ on $T$, $I_k[\kappa,\mu]\in\mathbb R$ is the mutual information of the kernel $\kappa$ with respect to $\mu$ (as its docstring describes it).

### `ProbabilityTheory.Kernel.mutualInfo_nonneg`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass U] [MeasurableSingletonClass T] [Countable T] [IsFiniteMeasure μ] [FiniteSupport μ] (hκ : κ.AEFiniteKernelSupport μ) : 0 ≤ Ik[κ , μ]`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [inst_2 : MeasurableSpace U] [MeasurableSingletonClass S] [MeasurableSingletonClass U] [MeasurableSingletonClass T] [Countable T] {κ : Kernel T (S × U)} {μ : Measure T} [IsFiniteMeasure μ] [FiniteSupport μ], κ.AEFiniteKernelSupport μ → (0 : ℝ) ≤ Ik[κ , μ]`
English: Let $S$, $T$, $U$ be measurable spaces in which every singleton is measurable, with $T$ countable. Let $\mu$ be a finite measure on $T$ which has finite support (there is a finite set whose complement has $\mu$-measure zero), and let $\kappa$ be a kernel from $T$ to $S \times U$ which has almost everywhere finite support with respect to $\mu$, i.e. for $\mu$-almost every $t \in T$ there is a finite set $A \subseteq S \times U$ with $\kappa(t)(A^c) = 0$. Let $I_k[\kappa,\mu]$ denote the mutual information of the kernel $\kappa$ with respect to $\mu$ (Lean `Kernel.mutualInfo`), defined as $H_k[\kappa_1,\mu] + H_k[\kappa_2,\mu] - H_k[\kappa,\mu]$, where $\kappa_1 : T \to S$ and $\kappa_2 : T \to U$ are the first and second marginal kernels of $\kappa$ and, for a kernel $\eta$ from $T$ to a measurable space, $H_k[\eta,\mu] = \int_T \operatorname{measureEntropy}(\eta(t))\, d\mu(t)$ is the entropy of $\eta$ with respect to $\mu$ (Lean `Kernel.entropy`). Then $0 \le I_k[\kappa,\mu]$.
