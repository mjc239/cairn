You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, propositions, theorems), in an arbitrary order, each with an id and its statement.

You decide the order of two kinds of step:
- `S:<id>` means *state* the result;
- `P:<id>` means *prove* it.
Each result says which of its steps belong to this chapter; include exactly those.

You may prove a result immediately after stating it, or state it early (for instance, announce the goal of
the chapter first) and prove it later, once the lemmas its proof needs have been developed. Whichever you
choose, respect every constraint below. A proof may use any result that has already been *stated*, even if
that result's own proof comes later.

Choose the order that makes the chapter clearest for a mathematician reading it for the first time.

Reply with only a JSON array containing every step exactly once, in your chosen order,
e.g. ["S:a", "S:b", "P:b", "P:a"].

## Results

- id `dist-sums`: lemma (Distance between sums); steps here: state and prove. We have $$ d[X_1+\tilde X_1; X_2+\tilde X_2] \geq k - \frac{\eta}{2} ( d[X_1; X_1] + d[X_2;X_2] ).$$
- id `key-ident`: lemma (Key identity); steps here: state and prove. We have $U+V+W=0$.
- id `tau-min-def`: definition ($\tau$-minimizer); steps here: state only (no proof needed). A pair of $G$-valued random variables $X_1, X_2$ are said to be a $\tau$-minimizer if one has $$\tau[X_1;X_2] \leq \tau[X'_1;X'_2] $$ for all $G$-valued random variables $X'_1, X'_2$.
- id `total-dist`: lemma (Bound on distance increments); steps here: state and prove. We have \begin{align*} \sum_{i=1}^2 \sum_{A\in\{U,V,W\}} \big(d[X^0_i;A|S] & - d[X^0_i;X_i]\big) \\ &\leq (6 - 3\eta) k + 3(2 \eta k - I_1). \end{align*}
- id `construct-good-prelim`: lemma (Constructing good variables, I); steps here: state and prove. One has \begin{align*} k \leq \delta + \eta (& d[X^0_1;T_1]-d[X^0_1;X_1]) + \eta (d[X^0_2;T_2]-d[X^0_2;X_2]) \\ & + \tfrac12 \eta \bbI[T_1:T_3] + \tfrac12 \eta \bbI[T_2:T_3]. \end{align*}
- id `entropy-pfr`: theorem (Entropy version of PFR); steps here: state and prove. Let $G = \F_2^n$, and suppose that $X^0_1, X^0_2$ are $G$-valued random variables. Then there is some subgroup $H \leq G$ such that \[ d[X^0_1;U_H] + d[X^0_2;U_H] \le 11 d[X^0_1;X^0_2], \] where $U_H$ is uniformly distributed on $H$. Furthermore, both $d[X^0_1;U_H]$ and $d[X^0_2;U_H]$ are at most $6 d[X^0_1;X^0_2]$.
- id `tau-copy`: lemma ($\tau$ depends only on distribution); steps here: state and prove. If $X'_1, X'_2$ are copies of $X_1,X_2$, then $\tau[X'_1;X'_2] = \tau[X_1;X_2]$.
- id `foursum-bound`: lemma (Entropy bound on quadruple sum); steps here: state and prove. With the same notation, we have \begin{equation} \bbH[X_1+X_2+\tilde X_1+\tilde X_2] \le \tfrac{1}{2} \bbH[X_1]+\tfrac{1}{2} \bbH[X_2] + (2 + \eta) k - I_1. \end{equation}
- id `tau-def`: definition ($\tau$ functional); steps here: state only (no proof needed). If $X_1,X_2$ are two $G$-valued random variables, then $$ \tau[X_1; X_2] := d[X_1; X_2] + \eta d[X^0_1; X_1] + \eta d[X^0_2; X_2].$$
- id `symm-lemma`: lemma (Symmetry identity); steps here: state and prove. We have $$ I(U:W | S) = I(V:W | S).$$
- id `first-cond`: lemma (Lower bound on conditional distances); steps here: state and prove. We have \begin{align*} & d[X_1|X_1+\tilde X_2; X_2|X_2+\tilde X_1] \\ & \qquad\quad \geq k - \eta (d[X^0_1; X_1 | X_1 + \tilde X_2] - d[X^0_1; X_1]) \\ & \qquad\qquad\qquad\qquad - \eta(d[X^0_2; X_2 | X_2 + \tilde X_1] - d[X^0_2; X_2]). \end{align*}
- id `first-dist-sum`: lemma (Lower bound on distances); steps here: state and prove. We have \begin{align*} d[X_1+\tilde X_2; X_2+\tilde X_1] \geq k &- \eta (d[X^0_1; X_1+\tilde X_2] - d[X^0_1; X_1]) \\& \qquad- \eta (d[X^0_2; X_2+\tilde X_1] - d[X^0_2; X_2]) \end{align*}
- id `de-prop`: theorem ($\tau$-decrement); steps here: state and prove. Let $X_1, X_2$ be tau-minimizers. Then $d[X_1;X_2] = 0$.
- id `second-estimate`: lemma (Second estimate); steps here: state and prove. We have $$ I_2 \leq 2 \eta k + \frac{2 \eta (2 \eta k - I_1)}{1 - \eta}.$$
- id `distance-lower`: lemma (Distance lower bound); steps here: state and prove. For any $G$-valued random variables $X'_1,X'_2$, one has $$ d[X'_1;X'_2] \geq k - \eta (d[X^0_1;X'_1] - d[X^0_1;X_1] ) - \eta (d[X^0_2;X'_2] - d[X^0_2;X_2] ).$$
- id `first-fibre`: lemma (Fibring identity for first estimate); steps here: state and prove. We have \begin{align*} & d[X_1+\tilde X_2;X_2+\tilde X_1] + d[X_1|X_1+\tilde X_2; X_2|X_2+\tilde X_1] \\ &\quad + \bbI[X_1+ X_2 : \tilde X_1 + X_2 \,|\, X_1 + X_2 + \tilde X_1 + \tilde X_2] = 2k. \end{align*}
- id `second-estimate-aux`: lemma; steps here: state and prove. We have \[d[X_1;X_1] + d[X_2;X_2] \leq 2 k + \frac{2(2 \eta k - I_1)}{1-\eta}. \]
- id `uvw-s`: lemma (Bound on conditional mutual informations); steps here: state and prove. We have $$ I(U : V \, | \, S) + I(V : W \, | \,S) + I(W : U \, | \, S) \leq 6 \eta k - \frac{1 - 5 \eta}{1-\eta} (2 \eta k - I_1). $$
- id `first-estimate`: lemma (First estimate); steps here: state and prove. We have $I_1 \leq 2 \eta k$.
- id `tau-min`: proposition ($\tau$ has minimum); steps here: state and prove. A pair $X_1, X_2$ of $\tau$-minimizers exist.
- id `first-upper`: lemma (Upper bound on distance differences); steps here: state and prove. We have \begin{align*} d[X^0_1; X_1+\tilde X_2] - d[X^0_1; X_1] &\leq \tfrac{1}{2} k + \tfrac{1}{4} \bbH[X_2] - \tfrac{1}{4} \bbH[X_1]\\ d[X^0_2;X_2+\tilde X_1] - d[X^0_2; X_2] &\leq \tfrac{1}{2} k + \tfrac{1}{4} \bbH[X_1] - \tfrac{1}{4} \bbH[X_2], \\ d[X_1^0;X_1|X_1+\tilde X_2] - d[X_1^0;X_1] &\leq \tfrac{1}{2} k + \tfrac{1}{4} \bbH[X_1] - \tfrac{1}{4} \bbH[X_2] \\ d[X_2^0; X_2|X_2+\tilde X_1] - d[X_2^0; X_2] &\leq \tfrac{1}{2}k + \tfrac{1}{4} \bbH[X_2] - \tfrac{1}{4} \bbH[X_1]. \end{align*}
- id `construct-good`: lemma (Constructing good variables, II); steps here: state and prove. One has \begin{align*} k & \leq \delta + \frac{\eta}{3} \biggl( \delta + \sum_{i=1}^2 \sum_{j = 1}^3 (d[X^0_i;T_j] - d[X^0_i; X_i]) \biggr). \end{align*}
- id `cond-distance-lower`: lemma (Conditional distance lower bound); steps here: state and prove. For any $G$-valued random variables $X'_1,X'_2$ and random variables $Z,W$, one has $$ d[X'_1|Z;X'_2|W] \geq k - \eta (d[X^0_1;X'_1|Z] - d[X^0_1;X_1] ) - \eta (d[X^0_2;X'_2|W] - d[X^0_2;X_2] ).$$

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:cond-distance-lower` before `P:first-cond`
- `S:cond-distance-lower` before `P:second-estimate`
- `S:construct-good` before `P:de-prop`
- `S:construct-good-prelim` before `P:construct-good`
- `S:de-prop` before `P:entropy-pfr`
- `S:dist-sums` before `P:second-estimate`
- `S:dist-sums` before `P:second-estimate-aux`
- `S:distance-lower` before `P:cond-distance-lower`
- `S:distance-lower` before `P:construct-good-prelim`
- `S:distance-lower` before `P:dist-sums`
- `S:distance-lower` before `P:first-dist-sum`
- `S:first-cond` before `P:first-estimate`
- `S:first-cond` before `P:foursum-bound`
- `S:first-dist-sum` before `P:first-estimate`
- `S:first-estimate` before `P:de-prop`
- `S:first-fibre` before `P:first-estimate`
- `S:first-fibre` before `P:foursum-bound`
- `S:first-upper` before `P:first-estimate`
- `S:first-upper` before `P:foursum-bound`
- `S:foursum-bound` before `P:second-estimate-aux`
- `S:foursum-bound` before `P:total-dist`
- `S:key-ident` before `P:de-prop`
- `S:second-estimate` before `P:uvw-s`
- `S:second-estimate-aux` before `P:second-estimate`
- `S:symm-lemma` before `P:uvw-s`
- `S:tau-copy` before `P:de-prop`
- `S:tau-copy` before `P:distance-lower`
- `S:tau-copy` before `P:entropy-pfr`
- `S:tau-copy` before `P:tau-min`
- `S:tau-def` before `P:de-prop`
- `S:tau-def` before `P:distance-lower`
- `S:tau-def` before `P:entropy-pfr`
- `S:tau-def` before `P:tau-min`
- `S:tau-def` before `S:tau-copy`
- `S:tau-def` before `S:tau-min-def`
- `S:tau-min` before `P:entropy-pfr`
- `S:tau-min-def` before `P:entropy-pfr`
- `S:tau-min-def` before `S:cond-distance-lower`
- `S:tau-min-def` before `S:construct-good`
- `S:tau-min-def` before `S:construct-good-prelim`
- `S:tau-min-def` before `S:de-prop`
- `S:tau-min-def` before `S:dist-sums`
- `S:tau-min-def` before `S:distance-lower`
- `S:tau-min-def` before `S:first-cond`
- `S:tau-min-def` before `S:first-dist-sum`
- `S:tau-min-def` before `S:first-estimate`
- `S:tau-min-def` before `S:foursum-bound`
- `S:tau-min-def` before `S:second-estimate`
- `S:tau-min-def` before `S:second-estimate-aux`
- `S:tau-min-def` before `S:tau-min`
- `S:tau-min-def` before `S:total-dist`
- `S:tau-min-def` before `S:uvw-s`
- `S:total-dist` before `P:de-prop`
- `S:uvw-s` before `P:de-prop`
