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

- id `r492`: lemma; steps here: state and prove. We have $$ I(U:W | S) = I(V:W | S).$$
- id `r902`: lemma; steps here: state and prove. We have $$ I_2 \leq 2 \eta k + \frac{2 \eta (2 \eta k - I_1)}{1 - \eta}.$$
- id `r977`: lemma; steps here: state and prove. If $X'_1, X'_2$ are copies of $X_1,X_2$, then $\tau[X'_1;X'_2] = \tau[X_1;X_2]$.
- id `r940`: lemma; steps here: state and prove. We have \begin{align*} d[X^0_1; X_1+\tilde X_2] - d[X^0_1; X_1] &\leq \tfrac{1}{2} k + \tfrac{1}{4} \bbH[X_2] - \tfrac{1}{4} \bbH[X_1]\\ d[X^0_2;X_2+\tilde X_1] - d[X^0_2; X_2] &\leq \tfrac{1}{2} k + \tfrac{1}{4} \bbH[X_1] - \tfrac{1}{4} \bbH[X_2], \\ d[X_1^0;X_1|X_1+\tilde X_2] - d[X_1^0;X_1] &\leq \tfrac{1}{2} k + \tfrac{1}{4} \bbH[X_1] - \tfrac{1}{4} \bbH[X_2] \\ d[X_2^0; X_2|X_2+\tilde X_1] - d[X_2^0; X_2] &\leq \tfrac{1}{2}k + \tfrac{1}{4} \bbH[X_2] - \tfrac{1}{4} \bbH[X_1]. \end{align*}
- id `r858`: definition; steps here: state only (no proof needed). A pair of $G$-valued random variables $X_1, X_2$ are said to be a $\tau$-minimizer if one has $$\tau[X_1;X_2] \leq \tau[X'_1;X'_2] $$ for all $G$-valued random variables $X'_1, X'_2$.
- id `r624`: lemma; steps here: state and prove. For any $G$-valued random variables $X'_1,X'_2$, one has $$ d[X'_1;X'_2] \geq k - \eta (d[X^0_1;X'_1] - d[X^0_1;X_1] ) - \eta (d[X^0_2;X'_2] - d[X^0_2;X_2] ).$$
- id `r928`: lemma; steps here: state and prove. We have $I_1 \leq 2 \eta k$.
- id `r232`: lemma; steps here: state and prove. We have \begin{align*} \sum_{i=1}^2 \sum_{A\in\{U,V,W\}} \big(d[X^0_i;A|S] & - d[X^0_i;X_i]\big) \\ &\leq (6 - 3\eta) k + 3(2 \eta k - I_1). \end{align*}
- id `r631`: lemma; steps here: state and prove. We have \begin{align*} & d[X_1+\tilde X_2;X_2+\tilde X_1] + d[X_1|X_1+\tilde X_2; X_2|X_2+\tilde X_1] \\ &\quad + \bbI[X_1+ X_2 : \tilde X_1 + X_2 \,|\, X_1 + X_2 + \tilde X_1 + \tilde X_2] = 2k. \end{align*}
- id `r896`: lemma; steps here: state and prove. We have \[d[X_1;X_1] + d[X_2;X_2] \leq 2 k + \frac{2(2 \eta k - I_1)}{1-\eta}. \]
- id `r674`: lemma; steps here: state and prove. With the same notation, we have \begin{equation} \bbH[X_1+X_2+\tilde X_1+\tilde X_2] \le \tfrac{1}{2} \bbH[X_1]+\tfrac{1}{2} \bbH[X_2] + (2 + \eta) k - I_1. \end{equation}
- id `r310`: lemma; steps here: state and prove. We have \begin{align*} & d[X_1|X_1+\tilde X_2; X_2|X_2+\tilde X_1] \\ & \qquad\quad \geq k - \eta (d[X^0_1; X_1 | X_1 + \tilde X_2] - d[X^0_1; X_1]) \\ & \qquad\qquad\qquad\qquad - \eta(d[X^0_2; X_2 | X_2 + \tilde X_1] - d[X^0_2; X_2]). \end{align*}
- id `r536`: proposition; steps here: state and prove. A pair $X_1, X_2$ of $\tau$-minimizers exist.
- id `r157`: theorem; steps here: state and prove. Let $G = \F_2^n$, and suppose that $X^0_1, X^0_2$ are $G$-valued random variables. Then there is some subgroup $H \leq G$ such that \[ d[X^0_1;U_H] + d[X^0_2;U_H] \le 11 d[X^0_1;X^0_2], \] where $U_H$ is uniformly distributed on $H$. Furthermore, both $d[X^0_1;U_H]$ and $d[X^0_2;U_H]$ are at most $6 d[X^0_1;X^0_2]$.
- id `r592`: definition; steps here: state only (no proof needed). If $X_1,X_2$ are two $G$-valued random variables, then $$ \tau[X_1; X_2] := d[X_1; X_2] + \eta d[X^0_1; X_1] + \eta d[X^0_2; X_2].$$
- id `r990`: lemma; steps here: state and prove. We have \begin{align*} d[X_1+\tilde X_2; X_2+\tilde X_1] \geq k &- \eta (d[X^0_1; X_1+\tilde X_2] - d[X^0_1; X_1]) \\& \qquad- \eta (d[X^0_2; X_2+\tilde X_1] - d[X^0_2; X_2]) \end{align*}
- id `r473`: lemma; steps here: state and prove. We have $$ I(U : V \, | \, S) + I(V : W \, | \,S) + I(W : U \, | \, S) \leq 6 \eta k - \frac{1 - 5 \eta}{1-\eta} (2 \eta k - I_1). $$
- id `r683`: lemma; steps here: state and prove. One has \begin{align*} k & \leq \delta + \frac{\eta}{3} \biggl( \delta + \sum_{i=1}^2 \sum_{j = 1}^3 (d[X^0_i;T_j] - d[X^0_i; X_i]) \biggr). \end{align*}
- id `r667`: lemma; steps here: state and prove. For any $G$-valued random variables $X'_1,X'_2$ and random variables $Z,W$, one has $$ d[X'_1|Z;X'_2|W] \geq k - \eta (d[X^0_1;X'_1|Z] - d[X^0_1;X_1] ) - \eta (d[X^0_2;X'_2|W] - d[X^0_2;X_2] ).$$
- id `r304`: lemma; steps here: state and prove. We have $$ d[X_1+\tilde X_1; X_2+\tilde X_2] \geq k - \frac{\eta}{2} ( d[X_1; X_1] + d[X_2;X_2] ).$$
- id `r616`: theorem; steps here: state and prove. Let $X_1, X_2$ be tau-minimizers. Then $d[X_1;X_2] = 0$.
- id `r523`: lemma; steps here: state and prove. We have $U+V+W=0$.
- id `r596`: lemma; steps here: state and prove. One has \begin{align*} k \leq \delta + \eta (& d[X^0_1;T_1]-d[X^0_1;X_1]) + \eta (d[X^0_2;T_2]-d[X^0_2;X_2]) \\ & + \tfrac12 \eta \bbI[T_1:T_3] + \tfrac12 \eta \bbI[T_2:T_3]. \end{align*}

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:r232` before `P:r616`
- `S:r304` before `P:r896`
- `S:r304` before `P:r902`
- `S:r310` before `P:r674`
- `S:r310` before `P:r928`
- `S:r473` before `P:r616`
- `S:r492` before `P:r473`
- `S:r523` before `P:r616`
- `S:r536` before `P:r157`
- `S:r592` before `P:r157`
- `S:r592` before `P:r536`
- `S:r592` before `P:r616`
- `S:r592` before `P:r624`
- `S:r592` before `S:r858`
- `S:r592` before `S:r977`
- `S:r596` before `P:r683`
- `S:r616` before `P:r157`
- `S:r624` before `P:r304`
- `S:r624` before `P:r596`
- `S:r624` before `P:r667`
- `S:r624` before `P:r990`
- `S:r631` before `P:r674`
- `S:r631` before `P:r928`
- `S:r667` before `P:r310`
- `S:r667` before `P:r902`
- `S:r674` before `P:r232`
- `S:r674` before `P:r896`
- `S:r683` before `P:r616`
- `S:r858` before `P:r157`
- `S:r858` before `S:r232`
- `S:r858` before `S:r304`
- `S:r858` before `S:r310`
- `S:r858` before `S:r473`
- `S:r858` before `S:r536`
- `S:r858` before `S:r596`
- `S:r858` before `S:r616`
- `S:r858` before `S:r624`
- `S:r858` before `S:r667`
- `S:r858` before `S:r674`
- `S:r858` before `S:r683`
- `S:r858` before `S:r896`
- `S:r858` before `S:r902`
- `S:r858` before `S:r928`
- `S:r858` before `S:r990`
- `S:r896` before `P:r902`
- `S:r902` before `P:r473`
- `S:r928` before `P:r616`
- `S:r940` before `P:r674`
- `S:r940` before `P:r928`
- `S:r977` before `P:r157`
- `S:r977` before `P:r536`
- `S:r977` before `P:r616`
- `S:r977` before `P:r624`
- `S:r990` before `P:r928`
