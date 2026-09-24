You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order.

## Results

- id `dist-sums`: lemma (Distance between sums). We have $$ d[X_1+\tilde X_1; X_2+\tilde X_2] \geq k - \frac{\eta}{2} ( d[X_1; X_1] + d[X_2;X_2] ).$$
- id `key-ident`: lemma (Key identity). We have $U+V+W=0$.
- id `tau-min-def`: definition ($\tau$-minimizer). A pair of $G$-valued random variables $X_1, X_2$ are said to be a $\tau$-minimizer if one has $$\tau[X_1;X_2] \leq \tau[X'_1;X'_2] $$ for all $G$-valued random variables $X'_1, X'_2$.
- id `total-dist`: lemma (Bound on distance increments). We have \begin{align*} \sum_{i=1}^2 \sum_{A\in\{U,V,W\}} \big(d[X^0_i;A|S] & - d[X^0_i;X_i]\big) \\ &\leq (6 - 3\eta) k + 3(2 \eta k - I_1). \end{align*}
- id `construct-good-prelim`: lemma (Constructing good variables, I). One has \begin{align*} k \leq \delta + \eta (& d[X^0_1;T_1]-d[X^0_1;X_1]) + \eta (d[X^0_2;T_2]-d[X^0_2;X_2]) \\ & + \tfrac12 \eta \bbI[T_1:T_3] + \tfrac12 \eta \bbI[T_2:T_3]. \end{align*}
- id `entropy-pfr`: theorem (Entropy version of PFR). Let $G = \F_2^n$, and suppose that $X^0_1, X^0_2$ are $G$-valued random variables. Then there is some subgroup $H \leq G$ such that \[ d[X^0_1;U_H] + d[X^0_2;U_H] \le 11 d[X^0_1;X^0_2], \] where $U_H$ is uniformly distributed on $H$. Furthermore, both $d[X^0_1;U_H]$ and $d[X^0_2;U_H]$ are at most $6 d[X^0_1;X^0_2]$.
- id `tau-copy`: lemma ($\tau$ depends only on distribution). If $X'_1, X'_2$ are copies of $X_1,X_2$, then $\tau[X'_1;X'_2] = \tau[X_1;X_2]$.
- id `foursum-bound`: lemma (Entropy bound on quadruple sum). With the same notation, we have \begin{equation} \bbH[X_1+X_2+\tilde X_1+\tilde X_2] \le \tfrac{1}{2} \bbH[X_1]+\tfrac{1}{2} \bbH[X_2] + (2 + \eta) k - I_1. \end{equation}
- id `tau-def`: definition ($\tau$ functional). If $X_1,X_2$ are two $G$-valued random variables, then $$ \tau[X_1; X_2] := d[X_1; X_2] + \eta d[X^0_1; X_1] + \eta d[X^0_2; X_2].$$
- id `symm-lemma`: lemma (Symmetry identity). We have $$ I(U:W | S) = I(V:W | S).$$
- id `first-cond`: lemma (Lower bound on conditional distances). We have \begin{align*} & d[X_1|X_1+\tilde X_2; X_2|X_2+\tilde X_1] \\ & \qquad\quad \geq k - \eta (d[X^0_1; X_1 | X_1 + \tilde X_2] - d[X^0_1; X_1]) \\ & \qquad\qquad\qquad\qquad - \eta(d[X^0_2; X_2 | X_2 + \tilde X_1] - d[X^0_2; X_2]). \end{align*}
- id `first-dist-sum`: lemma (Lower bound on distances). We have \begin{align*} d[X_1+\tilde X_2; X_2+\tilde X_1] \geq k &- \eta (d[X^0_1; X_1+\tilde X_2] - d[X^0_1; X_1]) \\& \qquad- \eta (d[X^0_2; X_2+\tilde X_1] - d[X^0_2; X_2]) \end{align*}
- id `de-prop`: theorem ($\tau$-decrement). Let $X_1, X_2$ be tau-minimizers. Then $d[X_1;X_2] = 0$.
- id `second-estimate`: lemma (Second estimate). We have $$ I_2 \leq 2 \eta k + \frac{2 \eta (2 \eta k - I_1)}{1 - \eta}.$$
- id `distance-lower`: lemma (Distance lower bound). For any $G$-valued random variables $X'_1,X'_2$, one has $$ d[X'_1;X'_2] \geq k - \eta (d[X^0_1;X'_1] - d[X^0_1;X_1] ) - \eta (d[X^0_2;X'_2] - d[X^0_2;X_2] ).$$
- id `first-fibre`: lemma (Fibring identity for first estimate). We have \begin{align*} & d[X_1+\tilde X_2;X_2+\tilde X_1] + d[X_1|X_1+\tilde X_2; X_2|X_2+\tilde X_1] \\ &\quad + \bbI[X_1+ X_2 : \tilde X_1 + X_2 \,|\, X_1 + X_2 + \tilde X_1 + \tilde X_2] = 2k. \end{align*}
- id `second-estimate-aux`: lemma. We have \[d[X_1;X_1] + d[X_2;X_2] \leq 2 k + \frac{2(2 \eta k - I_1)}{1-\eta}. \]
- id `uvw-s`: lemma (Bound on conditional mutual informations). We have $$ I(U : V \, | \, S) + I(V : W \, | \,S) + I(W : U \, | \, S) \leq 6 \eta k - \frac{1 - 5 \eta}{1-\eta} (2 \eta k - I_1). $$
- id `first-estimate`: lemma (First estimate). We have $I_1 \leq 2 \eta k$.
- id `tau-min`: proposition ($\tau$ has minimum). A pair $X_1, X_2$ of $\tau$-minimizers exist.
- id `first-upper`: lemma (Upper bound on distance differences). We have \begin{align*} d[X^0_1; X_1+\tilde X_2] - d[X^0_1; X_1] &\leq \tfrac{1}{2} k + \tfrac{1}{4} \bbH[X_2] - \tfrac{1}{4} \bbH[X_1]\\ d[X^0_2;X_2+\tilde X_1] - d[X^0_2; X_2] &\leq \tfrac{1}{2} k + \tfrac{1}{4} \bbH[X_1] - \tfrac{1}{4} \bbH[X_2], \\ d[X_1^0;X_1|X_1+\tilde X_2] - d[X_1^0;X_1] &\leq \tfrac{1}{2} k + \tfrac{1}{4} \bbH[X_1] - \tfrac{1}{4} \bbH[X_2] \\ d[X_2^0; X_2|X_2+\tilde X_1] - d[X_2^0; X_2] &\leq \tfrac{1}{2}k + \tfrac{1}{4} \bbH[X_2] - \tfrac{1}{4} \bbH[X_1]. \end{align*}
- id `construct-good`: lemma (Constructing good variables, II). One has \begin{align*} k & \leq \delta + \frac{\eta}{3} \biggl( \delta + \sum_{i=1}^2 \sum_{j = 1}^3 (d[X^0_i;T_j] - d[X^0_i; X_i]) \biggr). \end{align*}
- id `cond-distance-lower`: lemma (Conditional distance lower bound). For any $G$-valued random variables $X'_1,X'_2$ and random variables $Z,W$, one has $$ d[X'_1|Z;X'_2|W] \geq k - \eta (d[X^0_1;X'_1|Z] - d[X^0_1;X_1] ) - \eta (d[X^0_2;X'_2|W] - d[X^0_2;X_2] ).$$

## Constraints

- `cond-distance-lower` before `first-cond`
- `cond-distance-lower` before `second-estimate`
- `construct-good` before `de-prop`
- `construct-good-prelim` before `construct-good`
- `de-prop` before `entropy-pfr`
- `dist-sums` before `second-estimate`
- `dist-sums` before `second-estimate-aux`
- `distance-lower` before `cond-distance-lower`
- `distance-lower` before `construct-good-prelim`
- `distance-lower` before `dist-sums`
- `distance-lower` before `first-dist-sum`
- `first-cond` before `first-estimate`
- `first-cond` before `foursum-bound`
- `first-dist-sum` before `first-estimate`
- `first-estimate` before `de-prop`
- `first-fibre` before `first-estimate`
- `first-fibre` before `foursum-bound`
- `first-upper` before `first-estimate`
- `first-upper` before `foursum-bound`
- `foursum-bound` before `second-estimate-aux`
- `foursum-bound` before `total-dist`
- `key-ident` before `de-prop`
- `second-estimate` before `uvw-s`
- `second-estimate-aux` before `second-estimate`
- `symm-lemma` before `uvw-s`
- `tau-copy` before `de-prop`
- `tau-copy` before `distance-lower`
- `tau-copy` before `entropy-pfr`
- `tau-copy` before `tau-min`
- `tau-def` before `de-prop`
- `tau-def` before `distance-lower`
- `tau-def` before `entropy-pfr`
- `tau-def` before `tau-copy`
- `tau-def` before `tau-min`
- `tau-def` before `tau-min-def`
- `tau-min` before `entropy-pfr`
- `tau-min-def` before `cond-distance-lower`
- `tau-min-def` before `construct-good`
- `tau-min-def` before `construct-good-prelim`
- `tau-min-def` before `de-prop`
- `tau-min-def` before `dist-sums`
- `tau-min-def` before `distance-lower`
- `tau-min-def` before `entropy-pfr`
- `tau-min-def` before `first-cond`
- `tau-min-def` before `first-dist-sum`
- `tau-min-def` before `first-estimate`
- `tau-min-def` before `foursum-bound`
- `tau-min-def` before `second-estimate`
- `tau-min-def` before `second-estimate-aux`
- `tau-min-def` before `tau-min`
- `tau-min-def` before `total-dist`
- `tau-min-def` before `uvw-s`
- `total-dist` before `de-prop`
- `uvw-s` before `de-prop`
