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

- id `averaged-construct-good`: lemma (Constructing good variables, III'); steps here: state and prove. One has \begin{align*} k & \leq I(U : V \, | \, S) + I(V : W \, | \,S) + I(W : U \, | \, S) + \frac{\eta}{6} \sum_{i=1}^2 \sum_{A,B \in \{U,V,W\}: A \neq B} (d[X^0_i;A|B,S] - d[X^0_i; X_i]). \end{align*}
- id `de-prop-improv`: theorem (Improved $\tau$-decrement); steps here: state and prove. Suppose $0 < \eta < 1/8$. Let $X_1, X_2$ be tau-minimizers. Then $d[X_1;X_2] = 0$.
- id `construct-good-improv`: lemma (Constructing good variables, II'); steps here: state and prove. One has \begin{align*} k & \leq \delta + \frac{\eta}{6} \sum_{i=1}^2 \sum_{1 \leq j,l \leq 3; j \neq l} (d[X^0_i;T_j|T_l] - d[X^0_i; X_i]) \end{align*}
- id `de-prop-lim-improv`: theorem (Limiting improved $\tau$-decrement); steps here: state and prove. For $\eta = 1/8$, there exist tau-minimizers $X_1, X_2$ satisfying $d[X_1;X_2] = 0$.
- id `entropy-pfr-improv`: theorem (Improved entropy version of PFR); steps here: state and prove. Let $G = \F_2^n$, and suppose that $X^0_1, X^0_2$ are $G$-valued random variables. Then there is some subgroup $H \leq G$ such that \[ d[X^0_1;U_H] + d[X^0_2;U_H] \le 10 d[X^0_1;X^0_2], \] where $U_H$ is uniformly distributed on $H$. Furthermore, both $d[X^0_1;U_H]$ and $d[X^0_2;U_H]$ are at most $\tfrac{11}{2} d[X^0_1;X^0_2]$.
- id `construct-good-prelim-improv`: lemma (Constructing good variables, I'); steps here: state and prove. One has \begin{align*} k \leq \delta + \eta (& d[X^0_1;T_1|T_3]-d[X^0_1;X_1]) + \eta (d[X^0_2;T_2|T_3]-d[X^0_2;X_2]). \end{align*}
- id `gen-ineq`: lemma (General inequality); steps here: state and prove. Let $X_1, X_2, X_3, X_4$ be independent $G$-valued random variables, and let $Y$ be another $G$-valued random variable. Set $S := X_1+X_2+X_3+X_4$. Then \begin{align*} & d[Y; X_1+X_2|X_1 + X_3, S] - d[Y; X_1] \\ &\quad \leq \tfrac{1}{4} (d[X_1;X_2] + 2d[X_1;X_3] + d[X_2;X_4])\\ &\qquad \qquad + \tfrac{1}{4} (d[X_1|X_1+X_3;X_2|X_2+X_4] - d[X_3|X_3+X_4; X_1|X_1+X_2])\\ &\qquad \qquad + \tfrac{1}{8} (\bbH[X_1+X_2] - \bbH[X_3+X_4] + \bbH[X_2] - \bbH[X_3]\\ &\qquad \qquad \qquad + \bbH[X_2|X_2+X_4] - \bbH[X_1|X_1+X_3]). \end{align*}
- id `dist-diff-bound`: lemma (Bound on distance differences); steps here: state and prove. We have \begin{align*} &\sum_{i=1}^2 \sum_{A,B \in \{U,V,W\}: A \neq B} d[X_i^0;A|B, S] - d[X_i^0;X_i]\\ &\qquad \leq 12 k + \frac{4(2 \eta k - I_1)}{1-\eta}. \end{align*}
- id `pfr_aux-improv`: lemma; steps here: state and prove. If $A \subset {\bf F}_2^n$ is non-empty and $|A+A| \leq K|A|$, then $A$ can be covered by at most $K^6 |A|^{1/2}/|H|^{1/2}$ translates of a subspace $H$ of ${\bf F}_2^n$ with $$ |H|/|A| \in [K^{-10}, K^{10}]. $$
- id `pfr-improv`: theorem (Improved PFR); steps here: state and prove. If $A \subset {\bf F}_2^n$ is non-empty and $|A+A| \leq K|A|$, then $A$ can be covered by most $2K^{11}$ translates of a subspace $H$ of ${\bf F}_2^n$ with $|H| \leq |A|$.

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:averaged-construct-good` before `P:de-prop-improv`
- `S:construct-good-improv` before `P:averaged-construct-good`
- `S:construct-good-prelim-improv` before `P:construct-good-improv`
- `S:de-prop-improv` before `P:de-prop-lim-improv`
- `S:de-prop-lim-improv` before `P:entropy-pfr-improv`
- `S:dist-diff-bound` before `P:de-prop-improv`
- `S:entropy-pfr-improv` before `P:pfr_aux-improv`
- `S:gen-ineq` before `P:dist-diff-bound`
- `S:pfr_aux-improv` before `P:pfr-improv`
