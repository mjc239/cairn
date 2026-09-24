You are writing the text of a mathematical outline generated from a verified Lean formalisation.
Below are the results of one chapter, in the order the outline presents them. For each you get its Lean name, its
statement in Lean (only explicit hypotheses are shown; implicit and type-class assumptions are omitted), its
docstring if there is one, and, for theorems, the named results its proof uses (with their statements) and the
helper lemmas folded into the proof.

Write:
1. `title`: a short chapter title (at most 8 words), as a mathematician would name this material.
2. For every result, `statement`: the statement in clear mathematical English, using LaTeX between $...$ for
   formulas. Be faithful: keep every hypothesis and the exact conclusion; do not add, drop, strengthen or weaken
   anything. If some notation's meaning is unclear, keep the notation rather than guessing. For a definition, say
   what is being defined.
3. For every theorem, `sketch`: one or two sentences on how the proof goes, based only on the listed results it
   uses and their statements. Do not invent steps; if the structure is not clear, just say which results it
   combines.

Reply with only a JSON object:
{"title": "...", "results": {"<lean name>": {"statement": "...", "sketch": "..."}}}
(omit "sketch" for definitions). Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

## Chapter (Lean module `PFR.TauFunctional`)

### `refPackage` (definition)
Lean: `(Ω₀₁ : Type u_1) (Ω₀₂ : Type u_2) (G : Type uG) : Type (max (max uG u_1) u_2)`
Docstring: A structure that packages all the fixed information in the main argument. In this way, when defining the τ functional, we will only only need to refer to the package once in the notation instead of stating the reference spaces, the reference measures and the reference random variables. The η parameter has now been incorporated into the package, in preparation for being able to manipulate the pack…

### `refPackage.X₀₁` (definition)
Lean: `(self : refPackage Ω₀₁ Ω₀₂ G) (_ : Ω₀₁) : G`
Docstring: The first variable in a package.

### `refPackage.X₀₂` (definition)
Lean: `(self : refPackage Ω₀₁ Ω₀₂ G) (_ : Ω₀₂) : G`
Docstring: The second variable in a package.

### `refPackage.η` (definition)
Lean: `(self : refPackage Ω₀₁ Ω₀₂ G) : ℝ`
Docstring: The constant that parameterizes how good the package is. The argument only works for small enough `η`, typically `≤ 1/9` or `< 1/8`.

### `tau` (definition)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω₁ → G) (X₂ : Ω₂ → G) (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) : ℝ`
Docstring: If $X_1,X_2$ are two $G$-valued random variables, then $$ \tau[X_1; X_2] := d[X_1; X_2] + \eta d[X^0_1; X_1] + \eta d[X^0_2; X_2].$$ Here, $X^0_1$ and $X^0_2$ are two random variables fixed once and for all in most of the argument. To lighten notation, We package `X^0_1` and `X^0_2` in a single object named `p`. We denote it as `τ[X₁ ; μ₁ # X₂ ; μ₂ | p]` where `p` is a fixed package containing th…

### `TauMinimizes` (definition)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) : Prop`
Docstring: Property recording the fact that two random variables minimize the tau functional. Expressed in terms of measures on the group to avoid quantifying over all spaces, but this implies comparison with any pair of random variables, see Lemma `is_tau_min`.

### `distance_ge_of_min` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (h : TauMinimizes p X₁ X₂) (h1 : Measurable X₁') (h2 : Measurable X₂') : d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁'] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂'] - d[p.X₀₂ # X₂]) ≤ d[X₁' # X₂']`
Docstring: Let `X₁` and `X₂` be tau-minimizers associated to `p`, with $d[X_1,X_2]=k$, then $$ d[X'_1;X'_2] \geq k - \eta (d[X^0_1;X'_1] - d[X^0_1;X_1] ) - \eta (d[X^0_2;X'_2] - d[X^0_2;X_2] )$$ for any $G$-valued random variables $X'_1,X'_2$.
Proof uses:
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `tau`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω₁ → G) (X₂ : Ω₂ → G) (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) : ℝ`
Helper lemmas folded into the proof: `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr_right`, `ProbabilityTheory.IdentDistrib.tau_eq`, `ProbabilityTheory.identDistrib_id_left`, `ProbabilityTheory.identDistrib_id_right`, `is_tau_min`, `refPackage.hmeas1`

### `condRuzsaDistance_ge_of_min` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) (h : TauMinimizes p X₁ X₂) (h1 : Measurable X₁') (h2 : Measurable X₂') (Z : Ω'₁ → S) (W : Ω'₂ → T) (hZ : Measurable Z) (hW : Measurable W) : d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁' | Z] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂' | W] - d[p.X₀₂ # X₂]) ≤ d[X₁' | Z # X₂' | W]`
Docstring: For any $G$-valued random variables $X'_1,X'_2$ and random variables $Z,W$, one can lower bound $d[X'_1|Z;X'_2|W]$ by $$k - \eta (d[X^0_1;X'_1|Z] - d[X^0_1;X_1] ) - \eta (d[X^0_2;X'_2|W] - d[X^0_2;X_2] ).$$
Proof uses:
- `FiniteRange`: `(X : Ω → G) : Prop`
- `FiniteRange.fintype`: `(X : Ω → G) : Fintype ↑(Set.range X)`
- `FiniteRange.toFinset`: `(X : Ω → G) : Finset G`
- `condRuzsaDist'_eq_sum`: `(hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (μ' : Measure Ω') : d[X ; μ # Y | W ; μ'] = ∑ w ∈ FiniteRange.toFinset W, μ'.real (W ⁻¹' {w}) * d[X; μ # Y; μ'[|W ⁻¹' {w}]]`
- `condRuzsaDist_eq_sum`: `(hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (μ' : Measure Ω') : d[X | Z ; μ # Y | W ; μ'] = ∑ z ∈ FiniteRange.toFinset Z, ∑ w ∈ FiniteRange.toFinse…`
- `distance_ge_of_min`: `(p : refPackage Ω₀₁ Ω₀₂ G) (h : TauMinimizes p X₁ X₂) (h1 : Measurable X₁') (h2 : Measurable X₂') : d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁'] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂'] - d[p.X₀₂ # X₂]) ≤ d[X₁…`
Helper lemmas folded into the proof: `FiniteRange.full`, `FiniteRange.mem_iff`, `FiniteRange.range`, `FiniteRange.real_full`, `ProbabilityTheory.cond_isProbabilityMeasure_of_real`, `distance_ge_of_min'`, `instFiniteRangeOfFinite`

### `tau_minimizer_exists` (theorem)
Lean: `(p : refPackage Ω₀₁ Ω₀₂ G) : ∃ Ω x X₁ X₂, Measurable X₁ ∧ Measurable X₂ ∧ IsProbabilityMeasure volume ∧ TauMinimizes p X₁ X₂`
Docstring: A pair of random variables minimizing $τ$ exists.
Proof uses:
- `ProbabilityTheory.entropy`: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
- `ProbabilityTheory.measureEntropy`: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
- `continuous_rdist_restrict_probabilityMeasure`: `Continuous fun μ => d[id; ↑μ.1 # id; ↑μ.2]`
- `rdist`: `(X : Ω → G) (Y : Ω' → G) (μ : autoParam (Measure Ω) rdist._auto_1) (μ' : autoParam (Measure Ω') rdist._auto_3) : ℝ`
- `refPackage.X₀₁`: `(self : refPackage Ω₀₁ Ω₀₂ G) (_ : Ω₀₁) : G`
- `refPackage.X₀₂`: `(self : refPackage Ω₀₁ Ω₀₂ G) (_ : Ω₀₂) : G`
- `refPackage.η`: `(self : refPackage Ω₀₁ Ω₀₂ G) : ℝ`
- `tau`: `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω₁ → G) (X₂ : Ω₂ → G) (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) : ℝ`
Helper lemmas folded into the proof: `ProbabilityTheory.IdentDistrib.entropy_congr`, `ProbabilityTheory.IdentDistrib.fst_id`, `ProbabilityTheory.IdentDistrib.rdist_congr`, `ProbabilityTheory.IdentDistrib.rdist_congr_right`, `ProbabilityTheory.IdentDistrib.snd_id`, `ProbabilityTheory.IdentDistrib.tau_eq`, `ProbabilityTheory.identDistrib_id_left`, `ProbabilityTheory.identDistrib_id_right`
