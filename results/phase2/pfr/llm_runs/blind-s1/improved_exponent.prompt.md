You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order.

## Results

- id `r923`: lemma. Let $X_1, X_2, X_3, X_4$ be independent $G$-valued random variables, and let $Y$ be another $G$-valued random variable. Set $S := X_1+X_2+X_3+X_4$. Then \begin{align*} & d[Y; X_1+X_2|X_1 + X_3, S] - d[Y; X_1] \\ &\quad \leq \tfrac{1}{4} (d[X_1;X_2] + 2d[X_1;X_3] + d[X_2;X_4])\\ &\qquad \qquad + \tfrac{1}{4} (d[X_1|X_1+X_3;X_2|X_2+X_4] - d[X_3|X_3+X_4; X_1|X_1+X_2])\\ &\qquad \qquad + \tfrac{1}{8} (\bbH[X_1+X_2] - \bbH[X_3+X_4] + \bbH[X_2] - \bbH[X_3]\\ &\qquad \qquad \qquad + \bbH[X_2|X_2+X_4] - \bbH[X_1|X_1+X_3]). \end{align*}
- id `r335`: lemma. If $A \subset {\bf F}_2^n$ is non-empty and $|A+A| \leq K|A|$, then $A$ can be covered by at most $K^6 |A|^{1/2}/|H|^{1/2}$ translates of a subspace $H$ of ${\bf F}_2^n$ with $$ |H|/|A| \in [K^{-10}, K^{10}]. $$
- id `r750`: lemma. One has \begin{align*} k & \leq \delta + \frac{\eta}{6} \sum_{i=1}^2 \sum_{1 \leq j,l \leq 3; j \neq l} (d[X^0_i;T_j|T_l] - d[X^0_i; X_i]) \end{align*}
- id `r281`: lemma. One has \begin{align*} k & \leq I(U : V \, | \, S) + I(V : W \, | \,S) + I(W : U \, | \, S) + \frac{\eta}{6} \sum_{i=1}^2 \sum_{A,B \in \{U,V,W\}: A \neq B} (d[X^0_i;A|B,S] - d[X^0_i; X_i]). \end{align*}
- id `r663`: theorem. Let $G = \F_2^n$, and suppose that $X^0_1, X^0_2$ are $G$-valued random variables. Then there is some subgroup $H \leq G$ such that \[ d[X^0_1;U_H] + d[X^0_2;U_H] \le 10 d[X^0_1;X^0_2], \] where $U_H$ is uniformly distributed on $H$. Furthermore, both $d[X^0_1;U_H]$ and $d[X^0_2;U_H]$ are at most $\tfrac{11}{2} d[X^0_1;X^0_2]$.
- id `r698`: lemma. We have \begin{align*} &\sum_{i=1}^2 \sum_{A,B \in \{U,V,W\}: A \neq B} d[X_i^0;A|B, S] - d[X_i^0;X_i]\\ &\qquad \leq 12 k + \frac{4(2 \eta k - I_1)}{1-\eta}. \end{align*}
- id `r285`: lemma. One has \begin{align*} k \leq \delta + \eta (& d[X^0_1;T_1|T_3]-d[X^0_1;X_1]) + \eta (d[X^0_2;T_2|T_3]-d[X^0_2;X_2]). \end{align*}
- id `r981`: theorem. If $A \subset {\bf F}_2^n$ is non-empty and $|A+A| \leq K|A|$, then $A$ can be covered by most $2K^{11}$ translates of a subspace $H$ of ${\bf F}_2^n$ with $|H| \leq |A|$.
- id `r193`: theorem. For $\eta = 1/8$, there exist tau-minimizers $X_1, X_2$ satisfying $d[X_1;X_2] = 0$.
- id `r917`: theorem. Suppose $0 < \eta < 1/8$. Let $X_1, X_2$ be tau-minimizers. Then $d[X_1;X_2] = 0$.

## Constraints

- `r193` before `r663`
- `r281` before `r917`
- `r285` before `r750`
- `r335` before `r981`
- `r663` before `r335`
- `r698` before `r917`
- `r750` before `r281`
- `r917` before `r193`
- `r923` before `r698`
