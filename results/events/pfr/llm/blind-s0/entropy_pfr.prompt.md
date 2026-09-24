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

- id `r598`: lemma; steps here: state and prove. We have \begin{align*} d[X_1+\tilde X_2; X_2+\tilde X_1] \geq k &- \eta (d[X^0_1; X_1+\tilde X_2] - d[X^0_1; X_1]) \\& \qquad- \eta (d[X^0_2; X_2+\tilde X_1] - d[X^0_2; X_2]) \end{align*}
- id `r701`: lemma; steps here: state and prove. For any $G$-valued random variables $X'_1,X'_2$ and random variables $Z,W$, one has $$ d[X'_1|Z;X'_2|W] \geq k - \eta (d[X^0_1;X'_1|Z] - d[X^0_1;X_1] ) - \eta (d[X^0_2;X'_2|W] - d[X^0_2;X_2] ).$$
- id `r745`: lemma; steps here: state and prove. One has \begin{align*} k & \leq \delta + \frac{\eta}{3} \biggl( \delta + \sum_{i=1}^2 \sum_{j = 1}^3 (d[X^0_i;T_j] - d[X^0_i; X_i]) \biggr). \end{align*}
- id `r443`: definition; steps here: state only (no proof needed). If $X_1,X_2$ are two $G$-valued random variables, then $$ \tau[X_1; X_2] := d[X_1; X_2] + \eta d[X^0_1; X_1] + \eta d[X^0_2; X_2].$$
- id `r965`: lemma; steps here: state and prove. One has \begin{align*} k \leq \delta + \eta (& d[X^0_1;T_1]-d[X^0_1;X_1]) + \eta (d[X^0_2;T_2]-d[X^0_2;X_2]) \\ & + \tfrac12 \eta \bbI[T_1:T_3] + \tfrac12 \eta \bbI[T_2:T_3]. \end{align*}
- id `r294`: lemma; steps here: state and prove. We have $$ I_2 \leq 2 \eta k + \frac{2 \eta (2 \eta k - I_1)}{1 - \eta}.$$
- id `r348`: lemma; steps here: state and prove. With the same notation, we have \begin{equation} \bbH[X_1+X_2+\tilde X_1+\tilde X_2] \le \tfrac{1}{2} \bbH[X_1]+\tfrac{1}{2} \bbH[X_2] + (2 + \eta) k - I_1. \end{equation}
- id `r116`: theorem; steps here: state and prove. Let $X_1, X_2$ be tau-minimizers. Then $d[X_1;X_2] = 0$.
- id `r849`: lemma; steps here: state and prove. We have \begin{align*} & d[X_1+\tilde X_2;X_2+\tilde X_1] + d[X_1|X_1+\tilde X_2; X_2|X_2+\tilde X_1] \\ &\quad + \bbI[X_1+ X_2 : \tilde X_1 + X_2 \,|\, X_1 + X_2 + \tilde X_1 + \tilde X_2] = 2k. \end{align*}
- id `r377`: lemma; steps here: state and prove. We have \begin{align*} d[X^0_1; X_1+\tilde X_2] - d[X^0_1; X_1] &\leq \tfrac{1}{2} k + \tfrac{1}{4} \bbH[X_2] - \tfrac{1}{4} \bbH[X_1]\\ d[X^0_2;X_2+\tilde X_1] - d[X^0_2; X_2] &\leq \tfrac{1}{2} k + \tfrac{1}{4} \bbH[X_1] - \tfrac{1}{4} \bbH[X_2], \\ d[X_1^0;X_1|X_1+\tilde X_2] - d[X_1^0;X_1] &\leq \tfrac{1}{2} k + \tfrac{1}{4} \bbH[X_1] - \tfrac{1}{4} \bbH[X_2] \\ d[X_2^0; X_2|X_2+\tilde X_1] - d[X_2^0; X_2] &\leq \tfrac{1}{2}k + \tfrac{1}{4} \bbH[X_2] - \tfrac{1}{4} \bbH[X_1]. \end{align*}
- id `r219`: lemma; steps here: state and prove. We have $I_1 \leq 2 \eta k$.
- id `r822`: lemma; steps here: state and prove. We have \[d[X_1;X_1] + d[X_2;X_2] \leq 2 k + \frac{2(2 \eta k - I_1)}{1-\eta}. \]
- id `r325`: proposition; steps here: state and prove. A pair $X_1, X_2$ of $\tau$-minimizers exist.
- id `r480`: lemma; steps here: state and prove. We have $U+V+W=0$.
- id `r913`: lemma; steps here: state and prove. We have $$ I(U:W | S) = I(V:W | S).$$
- id `r274`: lemma; steps here: state and prove. We have \begin{align*} & d[X_1|X_1+\tilde X_2; X_2|X_2+\tilde X_1] \\ & \qquad\quad \geq k - \eta (d[X^0_1; X_1 | X_1 + \tilde X_2] - d[X^0_1; X_1]) \\ & \qquad\qquad\qquad\qquad - \eta(d[X^0_2; X_2 | X_2 + \tilde X_1] - d[X^0_2; X_2]). \end{align*}
- id `r440`: lemma; steps here: state and prove. We have $$ I(U : V \, | \, S) + I(V : W \, | \,S) + I(W : U \, | \, S) \leq 6 \eta k - \frac{1 - 5 \eta}{1-\eta} (2 \eta k - I_1). $$
- id `r536`: lemma; steps here: state and prove. We have $$ d[X_1+\tilde X_1; X_2+\tilde X_2] \geq k - \frac{\eta}{2} ( d[X_1; X_1] + d[X_2;X_2] ).$$
- id `r935`: lemma; steps here: state and prove. We have \begin{align*} \sum_{i=1}^2 \sum_{A\in\{U,V,W\}} \big(d[X^0_i;A|S] & - d[X^0_i;X_i]\big) \\ &\leq (6 - 3\eta) k + 3(2 \eta k - I_1). \end{align*}
- id `r163`: definition; steps here: state only (no proof needed). A pair of $G$-valued random variables $X_1, X_2$ are said to be a $\tau$-minimizer if one has $$\tau[X_1;X_2] \leq \tau[X'_1;X'_2] $$ for all $G$-valued random variables $X'_1, X'_2$.
- id `r203`: lemma; steps here: state and prove. If $X'_1, X'_2$ are copies of $X_1,X_2$, then $\tau[X'_1;X'_2] = \tau[X_1;X_2]$.
- id `r901`: theorem; steps here: state and prove. Let $G = \F_2^n$, and suppose that $X^0_1, X^0_2$ are $G$-valued random variables. Then there is some subgroup $H \leq G$ such that \[ d[X^0_1;U_H] + d[X^0_2;U_H] \le 11 d[X^0_1;X^0_2], \] where $U_H$ is uniformly distributed on $H$. Furthermore, both $d[X^0_1;U_H]$ and $d[X^0_2;U_H]$ are at most $6 d[X^0_1;X^0_2]$.
- id `r249`: lemma; steps here: state and prove. For any $G$-valued random variables $X'_1,X'_2$, one has $$ d[X'_1;X'_2] \geq k - \eta (d[X^0_1;X'_1] - d[X^0_1;X_1] ) - \eta (d[X^0_2;X'_2] - d[X^0_2;X_2] ).$$

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:r116` before `P:r901`
- `S:r163` before `P:r901`
- `S:r163` before `S:r116`
- `S:r163` before `S:r219`
- `S:r163` before `S:r249`
- `S:r163` before `S:r274`
- `S:r163` before `S:r294`
- `S:r163` before `S:r325`
- `S:r163` before `S:r348`
- `S:r163` before `S:r440`
- `S:r163` before `S:r536`
- `S:r163` before `S:r598`
- `S:r163` before `S:r701`
- `S:r163` before `S:r745`
- `S:r163` before `S:r822`
- `S:r163` before `S:r935`
- `S:r163` before `S:r965`
- `S:r203` before `P:r116`
- `S:r203` before `P:r249`
- `S:r203` before `P:r325`
- `S:r203` before `P:r901`
- `S:r219` before `P:r116`
- `S:r249` before `P:r536`
- `S:r249` before `P:r598`
- `S:r249` before `P:r701`
- `S:r249` before `P:r965`
- `S:r274` before `P:r219`
- `S:r274` before `P:r348`
- `S:r294` before `P:r440`
- `S:r325` before `P:r901`
- `S:r348` before `P:r822`
- `S:r348` before `P:r935`
- `S:r377` before `P:r219`
- `S:r377` before `P:r348`
- `S:r440` before `P:r116`
- `S:r443` before `P:r116`
- `S:r443` before `P:r249`
- `S:r443` before `P:r325`
- `S:r443` before `P:r901`
- `S:r443` before `S:r163`
- `S:r443` before `S:r203`
- `S:r480` before `P:r116`
- `S:r536` before `P:r294`
- `S:r536` before `P:r822`
- `S:r598` before `P:r219`
- `S:r701` before `P:r274`
- `S:r701` before `P:r294`
- `S:r745` before `P:r116`
- `S:r822` before `P:r294`
- `S:r849` before `P:r219`
- `S:r849` before `P:r348`
- `S:r913` before `P:r440`
- `S:r935` before `P:r116`
- `S:r965` before `P:r745`
