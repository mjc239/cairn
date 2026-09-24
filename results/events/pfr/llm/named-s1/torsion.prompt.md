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

- id `data-process-unc-one`: lemma (One-sided unconditional data processing inequality); steps here: state and prove. Let $X,Y$ be random variables. For any function $f, g$ on the range of $X$, we have $\bbI[f(X) : Y] \leq \bbI[X:Y]$.
- id `multidist-ruzsa-IV`: lemma (Multidistance and Ruzsa distance, IV); steps here: state and prove. Let $m \ge 2$, and let $X_{[m]}$ be a tuple of independent $G$-valued random variables. Let $W := \sum_{i=1}^m X_i$. Then $$ d[W;-W] \leq 2 D[X_i].$$
- id `klm-1`: lemma (Kaimonovich--Vershik--Madiman inequality); steps here: state and prove. If $n \geq 0$ and $X, Y_1, \dots, Y_n$ are jointly independent $G$-valued random variables, then $$\bbH\left[X + \sum_{i=1}^n Y_i\right] - \bbH[X] \leq \sum_{i=1}^n \left(\bbH[X+Y_i] - \bbH[X]\right).$$
- id `klm-3`: lemma (Kaimonovich--Vershik--Madiman inequality, III); steps here: state and prove. If $n \geq 1$ and $X, Y_1, \dots, Y_n$ are jointly independent $G$-valued random variables, then $$d\left[X; \sum_{i=1}^n Y_i\right] \leq d\left[X; Y_1\right] + \frac{1}{2}\left(\bbH\left[ \sum_{i=1}^n Y_i\right] - \bbH[Y_1]\right).$$
- id `sign-flip`: lemma (Flipping a sign); steps here: state and prove. If $X,Y$ are $G$-valued, then $$ d[X ; -Y] \leq 3 d[X;Y].$$
- id `multi-zero`: proposition (Vanishing); steps here: state and prove. If $D[X_{[m]}]=0$, then for each $1 \leq i \leq m$ there is a finite subgroup $H_i \leq G$ such that $d[X_i; U_{H_i}] = 0$.
- id `pfr-torsion`: theorem (PFR); steps here: state and prove. Suppose that $G$ is a finite abelian group of torsion $m$. If $A \subset G$ is non-empty and $|A+A| \leq K|A|$, then $A$ can be covered by at most $mK^{256m^3+1}$ translates of a subspace $H$ of $G$ with $|H| \leq |A|$.
- id `lem:get-better`: lemma (Application of BSG); steps here: state and prove. Let $G$ be an abelian group, let $(T_1,T_2,T_3)$ be a $G^3$-valued random variable such that $T_1+T_2+T_3=0$ holds identically, and write \[ \delta := \bbI[T_1 : T_2] + \bbI[T_1 : T_3] + \bbI[T_2 : T_3]. \] Let $Y_1,\dots,Y_n$ be some further $G$-valued random variables and let $\alpha>0$ be a constant. Then there exists a random variable $U$ such that \begin{equation} d[U;U] + \alpha \sum_{i=1}^n d[Y_i;U] \leq \Bigl(2 + \frac{\alpha n}{2} \Bigr) \delta + \alpha \sum_{i=1}^n d[Y_i;T_2]. \end{equation}
- id `ent-z2`: lemma (Entropy of $Z_2$); steps here: state and prove. We have $\bbH[Z_2] \leq (8m^2-16m+1) k + \frac{1}{m} \sum_{i=1}^m \bbH[X_i]$.
- id `data-process-unc`: lemma (Unconditional data processing inequality); steps here: state and prove. Let $X,Y$ be random variables. For any functions $f, g$ on the ranges of $X, Y$ respectively, we have $\bbI[f(X) : g(Y )] \leq \bbI[X : Y]$.
- id `Zero-sum`: lemma (Zero-sum); steps here: state and prove. We have \begin{equation} Z_1+Z_2+Z_3= 0 \end{equation}
- id `cond-multidist-lower-II`: corollary (Lower bound on conditional multidistance, II); steps here: state and prove. With the notation of the previous lemma, we have \begin{equation} k - D[ X'_{[m]} | Y_{[m]} ] \leq \eta \sum_{i=1}^m d[X_{\sigma(i)};X'_i|Y_i] \end{equation} for any permutation $\sigma : \{1,\dots,m\} \rightarrow \{1,\dots,m\}$.
- id `multidist-copy`: lemma (Multidistance of copy); steps here: state and prove. If $X_{[m]} = (X_i)_{1 \leq i \leq m}$ and $Y_{[m]} = (Y_i)_{1 \leq i \leq m}$ are such that $X_i$ and $Y_i$ have the same distribution for each $i$, then $D[X_{[m]}] = D[Y_{[m]}]$.
- id `xi-z2-w-dist`: lemma (Distance bound); steps here: state and prove. We have $\sum_{i=1}^m d[X_i;Z_2|W] \leq 4(m^3-m^2) k$.
- id `sum-dilate-I`: lemma (Sums of dilates I); steps here: state and prove. Let $X,Y,X'$ be independent $G$-valued random variables, with $X'$ a copy of $X$, and let $a$ be an integer. Then $$\bbH[X-(a+1)Y] \leq \bbH[X-aY] + \bbH[X-Y-X'] - \bbH[X]$$ and $$\bbH[X-(a-1)Y] \leq \bbH[X-aY] + \bbH[X-Y-X'] - \bbH[X].$$
- id `multidist-nonneg`: lemma (Nonnegativity); steps here: state and prove. For any such tuple, we have $D[X_{[m]}] \geq 0$.
- id `sum-dilate-II`: lemma (Sums of dilates II); steps here: state and prove. Let $X,Y$ be independent $G$-valued random variables, and let $a$ be an integer. Then $$\bbH[X-aY] - \bbH[X] \leq 4 |a| d[X;Y].$$
- id `multidist-lower`: lemma (Lower bound on multidistance); steps here: state and prove. If $(X_i)_{1 \leq i \leq m}$ is a $\tau$-minimizer, and $k := D[(X_i)_{1 \leq i \leq m}]$, then for any other tuple $(X'_i)_{1 \leq i \leq m}$, one has $$ k - D[(X'_i)_{1 \leq i \leq m}] \leq \eta \sum_{i=1}^m d[X_i; X'_i].$$
- id `ent-w`: lemma (Entropy of $W$); steps here: state and prove. We have $\bbH[W] \leq (2m-1)k + \frac1m \sum_{i=1}^m \bbH[X_i]$.
- id `eta-def-multi`: definition ($\eta$); steps here: state only (no proof needed). We set $\eta := \frac{1}{32m^3}$.
- id `tau-min-multi`: definition ($\tau$-minimizer); steps here: state only (no proof needed). A $\tau$-minimizer is a tuple $(X_i)_{1 \leq i \leq m}$ that minimizes the $\tau$-functional among all tuples of $G$-valued random variables.
- id `cond-multidist-alt`: lemma (Alternate form of conditional multidistance); steps here: state and prove. If the $(X_i,Y_i)$ are independent, \begin{equation} D[ X_{[m]} | Y_{[m]}] := \bbH[\sum_{i=1}^m X_i \big| (Y_j)_{1 \leq j \leq m} ] - \frac{1}{m} \sum_{i=1}^m \bbH[ X_i | Y_i]. \end{equation}
- id `cond-multidist-lower`: lemma (Lower bound on conditional multidistance); steps here: state and prove. If $(X_i)_{1 \leq i \leq m}$ is a $\tau$-minimizer, and $k := D[(X_i)_{1 \leq i \leq m}]$, then for any other tuples $(X'_i)_{1 \leq i \leq m}$ and $(Y_i)_{1 \leq i \leq m}$ with the $X'_i$ $G$-valued, one has $$ k - D[(X'_i)_{1 \leq i \leq m} | (Y_i)_{1 \leq i \leq m}] \leq \eta \sum_{i=1}^m d[X_i; X'_i|Y_i].$$
- id `multidist-chain-rule-iter`: lemma; steps here: state and prove. Let $m$ be a positive integer. Suppose one has a sequence \begin{equation} G_m \to G_{m-1} \to \dots \to G_1 \to G_0 = \{0\} \end{equation} of homomorphisms between abelian groups $G_0,\dots,G_m$, and for each $d=0,\dots,m$, let $\pi_d : G_m \to G_d$ be the homomorphism from $G_m$ to $G_d$ arising from this sequence by composition (so for instance $\pi_m$ is the identity homomorphism and $\pi_0$ is the zero homomorphism). Let $X_{[m]} = (X_i)_{1 \leq i \leq m}$ be a jointly independent tuple of $G_m$-valued random variables. Then \begin{equation} \begin{split} D[ X_{[m]} ] &= \sum_{d=1}^m D[ \pi_d(X_{[m]}) \,|\, \pi_{d-1}(X_{[m]})] \\ &\quad + \sum_{d=1}^{m-1} \bbI[ \sum_i X_i : \pi_d(X_{[m]}) \; \big| \; \pi_d\big(\sum_i X_i\big), \pi_{d-1}(X_{[m]}) ]. \end{split} \end{equation} In particular, by \Cref{conditional-nonneg}, \begin{align}\nonumber D[ X_{[m]} ] \geq & \sum_{d=1}^m D[ \pi_d(X_{[m]})|\pi_{d-1}(X_{[m]}) ] \\ & + \bbI[ \sum_i X_i : \pi_1(X_{[m]}) \; \big| \; \pi_1\bigl(\sum_i X_i\bigr) ]. \end{align}
- id `multidist-ruzsa-I`: lemma (Multidistance and Ruzsa distance, I); steps here: state and prove. Let $m \ge 2$, and let $X_{[m]}$ be a tuple of $G$-valued random variables. Then $$\sum_{1 \leq j,k \leq m: j \neq k} d[X_j; -X_k] \leq m(m-1) D[X_{[m]}].$$
- id `klm-2`: lemma (Kaimonovich--Vershik--Madiman inequality, II); steps here: state and prove. If $n \geq 1$ and $X, Y_1, \dots, Y_n$ are jointly independent $G$-valued random variables, then $$ d[X; \sum_{i=1}^n Y_i] \leq 2 \sum_{i=1}^n d[X; Y_i].$$
- id `mutual-w-z2`: lemma (Mutual information bound); steps here: state and prove. We have $\bbI[W : Z_2] \leq 2 (m-1) k$.
- id `multidist-ruzsa-III`: lemma (Multidistance and Ruzsa distance, III); steps here: state and prove. Let $m \ge 2$, and let $X_{[m]}$ be a tuple of $G$-valued random variables. If the $X_i$ all have the same distribution, then $D[X_{[m]}] \leq m d[X_i;X_i]$ for any $1 \leq i \leq m$.
- id `multidist-def`: definition (Multidistance); steps here: state only (no proof needed). Let $m$ be a positive integer, and let $X_{[m]} = (X_i)_{1 \leq i \leq m}$ be an $m$-tuple of $G$-valued random variables $X_i$. Then we define \[ D[X_{[m]}] := \bbH[\sum_{i=1}^m \tilde X_i] - \frac{1}{m} \sum_{i=1}^m \bbH[\tilde X_i], \] where the $\tilde X_i$ are independent copies of the $X_i$.
- id `k-vanish`: proposition (Vanishing entropy); steps here: state and prove. We have $k = 0$.
- id `multidist-perm`: lemma (Relabeling); steps here: state and prove. If $\phi: \{1,\dots,m\} \to \{1,\dots,m\}$ is a bijection, then $D[X_{[m]}] = D[(X_{\phi(j)})_{1 \leq j \leq m}]$.
- id `data-process`: lemma (Data processing inequality); steps here: state and prove. Let $X,Y,Z$. For any functions $f, g$ on the ranges of $X, Y$ respectively, we have $\bbI[f(X) : g(Y )|Z] \leq \bbI[X :Y |Z]$.
- id `cond-multidist-def`: definition (Conditional multidistance); steps here: state only (no proof needed). If $X_{[m]} = (X_i)_{1 \leq i \leq m}$ and $Y_{[m]} = (Y_i)_{1 \leq i \leq m}$ are tuples of random variables, with the $X_i$ being $G$-valued (but the $Y_i$ need not be), then we define \begin{equation} D[ X_{[m]} | Y_{[m]} ] = \sum_{(y_i)_{1 \leq i \leq m}} \biggl(\prod_{1 \leq i \leq m} p_{Y_i}(y_i)\biggr) D[ (X_i \,|\, Y_i \mathop{=}y_i)_{1 \leq i \leq m}] \end{equation} where each $y_i$ ranges over the support of $p_{Y_i}$ for $1 \leq i \leq m$.
- id `multidist-indep`: lemma (Multidistance of independent variables); steps here: state and prove. If $X_{[m]} = (X_i)_{1 \leq i \leq m}$ are jointly independent, then $D[X_{[m]}] = \bbH[\sum_{i=1}^m X_i] - \frac{1}{m} \sum_{i=1}^m \bbH[X_i]$.
- id `multidist-chain-rule-cond`: lemma (Conditional multidistance chain rule); steps here: state and prove. Let $\pi \colon G \to H$ be a homomorphism of abelian groups. Let $I$ be a finite index set and let $X_{[m]}$ be a tuple of $G$-valued random variables. Let $Y_{[m]}$ be another tuple of random variables (not necessarily $G$-valued). Suppose that the pairs $(X_i, Y_i)$ are jointly independent of one another (but $X_i$ need not be independent of $Y_i$). Then \begin{align}\nonumber D[ X_{[m]} | Y_{[m]} ] &= D[ X_{[m]} \,|\, \pi(X_{[m]}), Y_{[m]}] + D[ \pi(X_{[m]}) \,|\, Y_{[m]}] \\ &\quad\qquad + \bbI[ \sum_{i=1}^m X_i : \pi(X_{[m]}) \; \big| \; \pi\bigl(\sum_{i=1}^m X_i \bigr), Y_{[m]} ]. \end{align}
- id `compare-sums`: lemma (Comparing sums); steps here: state and prove. Let $(X_i)_{1 \leq i \leq m}$ and $(Y_j)_{1 \leq j \leq l}$ be tuples of jointly independent random variables (so the $X$'s and $Y$'s are also independent of each other), and let $f: \{1,\dots,l\} \to \{1,\dots,m\}$ be a function, then $$ \bbH[\sum_{j=1}^l Y_j] \leq \bbH[ \sum_{i=1}^m X_i ] + \sum_{j=1}^l (\bbH[ Y_j - X_{f(j)}] - \bbH[X_{f(j)}]).$$
- id `pfr_aux_torsion`: lemma; steps here: state and prove. Suppose that $G$ is a finite abelian group of torsion $m$. If $A \subset G$ is non-empty and $|A+A| \leq K|A|$, then $A$ can be covered by at most $K ^ {128m^3+1}|A|^{1/2}/|H|^{1/2}$ translates of a subspace $H$ of $G$ with \begin{equation} |H|/|A| \in [K^{-256m^3}, K^{256m^3}]. \end{equation}
- id `tau-min-exist-multi`: proposition (Existence of $\tau$-minimizer); steps here: state and prove. If $G$ is finite, then a $\tau$-minimizer exists.
- id `data-process-single`: lemma (Data processing for a single variable); steps here: state and prove. Let $X$ be a random variable. Then for any function $f$ on the range of $X$, one has $\bbH[f(X)] \leq \bbH[X]$.
- id `prop:52`: proposition (Mutual information bound); steps here: state and prove. We have \[ \bbI[Z_1 : Z_2\, |\, W],\ \bbI[Z_2 : Z_3\, |\, W],\ \bbI[Z_1 : Z_3\, |\, W] \leq t \] where \begin{equation} t := m(4m+1) \eta k. \end{equation}
- id `cor-multid`: corollary; steps here: state and prove. Let $G$ be an abelian group and let $m \geq 2$. Suppose that $X_{i,j}$, $1 \leq i, j \leq m$, are independent $G$-valued random variables. Then \begin{align*} &\bbI[ \bigl(\sum_{i=1}^m X_{i,j}\bigr)_{j =1}^{m} : \bigl(\sum_{j=1}^m X_{i,j}\bigr)_{i = 1}^m \; \big| \; \sum_{i=1}^m \sum_{j = 1}^m X_{i,j} ] \\ &\quad \leq \sum_{j=1}^{m-1} \Bigl(D[(X_{i, j})_{i = 1}^m] - D[ (X_{i, j})_{i = 1}^m \; \big| \; (X_{i,j} + \cdots + X_{i,m})_{i =1}^m ]\Bigr) \\ & \qquad\qquad\qquad\qquad + D[(X_{i,m})_{i=1}^m] - D[ \bigl(\sum_{j=1}^m X_{i,j}\bigr)_{i=1}^m ], \end{align*} where all the multidistances here involve the indexing set $\{1,\dots, m\}$.
- id `multidist-ruzsa-II`: lemma (Multidistance and Ruzsa distance, II); steps here: state and prove. Let $m \ge 2$, and let $X_{[m]}$ be a tuple of $G$-valued random variables. Then $$\sum_{j=1}^m d[X_j;X_j] \leq 2 m D[X_{[m]}].$$
- id `cond-multidist-nonneg`: lemma (Conditional multidistance nonnegative); steps here: state and prove. If $X_{[m]} = (X_i)_{1 \leq i \leq m}$ and $Y_{[m]} = (Y_i)_{1 \leq i \leq m}$ are tuples of random variables, then $D[ X_{[m]} | Y_{[m]} ] \geq 0$.
- id `main-entropy`: theorem (Entropy form of PFR); steps here: state and prove. Suppose that $G$ is a finite abelian group of torsion $m$. Suppose that $X$ is a $G$-valued random variable. Then there exists a subgroup $H \leq G$ such that \[ d[X;U_H] \leq 64 m^3 d[X;X].\]
- id `key`: proposition (Bounding mutual information); steps here: state and prove. Suppose that $X_{i,j}$, $1 \leq i,j \leq m$, are jointly independent $G$-valued random variables, such that for each $j = 1,\dots,m$, the random variables $(X_{i,j})_{i = 1}^m$ coincide in distribution with some permutation of $X_{[m]}$. Write \[ {\mathcal I} := \bbI[ \bigl(\sum_{i=1}^m X_{i,j}\bigr)_{j =1}^{m} : \bigl(\sum_{j=1}^m X_{i,j}\bigr)_{i = 1}^m \; \big| \; \sum_{i=1}^m \sum_{j = 1}^m X_{i,j} ]. \] Then \begin{equation} {\mathcal I} \leq m(4m+1) \eta k. \end{equation}
- id `tau-def-multi`: definition ($\tau$-functional); steps here: state only (no proof needed). If $(X_i)_{1 \leq i \leq m}$ is a tuple, we define its $\tau$-functional $$ \tau[ (X_i)_{1 \leq i \leq m}] := D[(X_i)_{1 \leq i \leq m}] + \eta \sum_{i=1}^m d[X_i; X^0].$$
- id `multidist-chain-rule`: lemma (Multidistance chain rule); steps here: state and prove. Let $\pi \colon G \to H$ be a homomorphism of abelian groups and let $X_{[m]}$ be a tuple of jointly independent $G$-valued random variables. Then $D[X_{[m]}]$ is equal to \begin{equation} D[ X_{[m]} | \pi(X_{[m]}) ] +D[ \pi(X_{[m]}) ] + \bbI[ \sum_{i=1}^m X_i : \pi(X_{[m]}) \; \big| \; \pi\bigl(\sum_{i=1}^m X_i\bigr) ] \end{equation} where $\pi(X_{[m]}) := (\pi(X_i))_{1 \leq i \leq m}$.
- id `tau-ref`: proposition (Minimizer close to reference variables); steps here: state and prove. If $(X_i)_{1 \leq i \leq m}$ is a $\tau$-minimizer, then $\sum_{i=1}^m d[X_i; X^0] \leq \frac{2m}{\eta} d[X^0; X^0]$.

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:Zero-sum` before `P:k-vanish`
- `S:compare-sums` before `P:key`
- `S:cond-multidist-alt` before `P:cor-multid`
- `S:cond-multidist-alt` before `P:multidist-chain-rule`
- `S:cond-multidist-def` before `P:key`
- `S:cond-multidist-def` before `S:cond-multidist-alt`
- `S:cond-multidist-def` before `S:cond-multidist-lower`
- `S:cond-multidist-def` before `S:cond-multidist-lower-II`
- `S:cond-multidist-def` before `S:cond-multidist-nonneg`
- `S:cond-multidist-def` before `S:cor-multid`
- `S:cond-multidist-def` before `S:multidist-chain-rule`
- `S:cond-multidist-def` before `S:multidist-chain-rule-cond`
- `S:cond-multidist-def` before `S:multidist-chain-rule-iter`
- `S:cond-multidist-lower` before `P:cond-multidist-lower-II`
- `S:cond-multidist-lower-II` before `P:key`
- `S:cond-multidist-nonneg` before `P:multidist-chain-rule-iter`
- `S:cor-multid` before `P:key`
- `S:data-process` before `P:prop:52`
- `S:data-process-single` before `P:sign-flip`
- `S:data-process-unc` before `P:data-process`
- `S:data-process-unc-one` before `P:data-process-unc`
- `S:ent-w` before `P:mutual-w-z2`
- `S:ent-z2` before `P:xi-z2-w-dist`
- `S:eta-def-multi` before `P:main-entropy`
- `S:eta-def-multi` before `S:Zero-sum`
- `S:eta-def-multi` before `S:cond-multidist-lower`
- `S:eta-def-multi` before `S:cond-multidist-lower-II`
- `S:eta-def-multi` before `S:ent-w`
- `S:eta-def-multi` before `S:ent-z2`
- `S:eta-def-multi` before `S:k-vanish`
- `S:eta-def-multi` before `S:key`
- `S:eta-def-multi` before `S:multidist-lower`
- `S:eta-def-multi` before `S:mutual-w-z2`
- `S:eta-def-multi` before `S:prop:52`
- `S:eta-def-multi` before `S:tau-def-multi`
- `S:eta-def-multi` before `S:tau-min-exist-multi`
- `S:eta-def-multi` before `S:tau-min-multi`
- `S:eta-def-multi` before `S:tau-ref`
- `S:eta-def-multi` before `S:xi-z2-w-dist`
- `S:k-vanish` before `P:main-entropy`
- `S:key` before `P:prop:52`
- `S:klm-1` before `P:compare-sums`
- `S:klm-1` before `P:ent-w`
- `S:klm-1` before `P:ent-z2`
- `S:klm-1` before `P:klm-2`
- `S:klm-1` before `P:multidist-ruzsa-III`
- `S:klm-3` before `P:xi-z2-w-dist`
- `S:lem:get-better` before `P:k-vanish`
- `S:main-entropy` before `P:pfr_aux_torsion`
- `S:multi-zero` before `P:main-entropy`
- `S:multidist-chain-rule` before `P:multidist-chain-rule-cond`
- `S:multidist-chain-rule-cond` before `P:multidist-chain-rule-iter`
- `S:multidist-chain-rule-iter` before `P:cor-multid`
- `S:multidist-copy` before `P:cond-multidist-alt`
- `S:multidist-copy` before `P:ent-w`
- `S:multidist-copy` before `P:ent-z2`
- `S:multidist-copy` before `P:key`
- `S:multidist-copy` before `P:multidist-chain-rule-cond`
- `S:multidist-copy` before `P:multidist-nonneg`
- `S:multidist-copy` before `P:multidist-ruzsa-I`
- `S:multidist-copy` before `P:multidist-ruzsa-III`
- `S:multidist-copy` before `P:mutual-w-z2`
- `S:multidist-copy` before `P:prop:52`
- `S:multidist-copy` before `P:tau-min-exist-multi`
- `S:multidist-def` before `P:cond-multidist-alt`
- `S:multidist-def` before `P:cond-multidist-nonneg`
- `S:multidist-def` before `P:main-entropy`
- `S:multidist-def` before `P:multidist-chain-rule-cond`
- `S:multidist-def` before `P:tau-min-exist-multi`
- `S:multidist-def` before `P:tau-ref`
- `S:multidist-def` before `S:cond-multidist-def`
- `S:multidist-def` before `S:cond-multidist-lower`
- `S:multidist-def` before `S:cond-multidist-lower-II`
- `S:multidist-def` before `S:cor-multid`
- `S:multidist-def` before `S:ent-w`
- `S:multidist-def` before `S:ent-z2`
- `S:multidist-def` before `S:k-vanish`
- `S:multidist-def` before `S:key`
- `S:multidist-def` before `S:multi-zero`
- `S:multidist-def` before `S:multidist-chain-rule`
- `S:multidist-def` before `S:multidist-chain-rule-iter`
- `S:multidist-def` before `S:multidist-copy`
- `S:multidist-def` before `S:multidist-indep`
- `S:multidist-def` before `S:multidist-lower`
- `S:multidist-def` before `S:multidist-nonneg`
- `S:multidist-def` before `S:multidist-perm`
- `S:multidist-def` before `S:multidist-ruzsa-I`
- `S:multidist-def` before `S:multidist-ruzsa-II`
- `S:multidist-def` before `S:multidist-ruzsa-III`
- `S:multidist-def` before `S:multidist-ruzsa-IV`
- `S:multidist-def` before `S:mutual-w-z2`
- `S:multidist-def` before `S:prop:52`
- `S:multidist-def` before `S:tau-def-multi`
- `S:multidist-def` before `S:xi-z2-w-dist`
- `S:multidist-indep` before `P:cond-multidist-alt`
- `S:multidist-indep` before `P:cor-multid`
- `S:multidist-indep` before `P:ent-w`
- `S:multidist-indep` before `P:ent-z2`
- `S:multidist-indep` before `P:key`
- `S:multidist-indep` before `P:multidist-chain-rule`
- `S:multidist-indep` before `P:multidist-nonneg`
- `S:multidist-indep` before `P:multidist-ruzsa-I`
- `S:multidist-indep` before `P:multidist-ruzsa-III`
- `S:multidist-indep` before `P:multidist-ruzsa-IV`
- `S:multidist-indep` before `P:mutual-w-z2`
- `S:multidist-lower` before `P:cond-multidist-lower`
- `S:multidist-lower` before `P:k-vanish`
- `S:multidist-lower` before `P:key`
- `S:multidist-nonneg` before `P:cond-multidist-nonneg`
- `S:multidist-nonneg` before `P:k-vanish`
- `S:multidist-nonneg` before `P:tau-ref`
- `S:multidist-nonneg` before `P:xi-z2-w-dist`
- `S:multidist-perm` before `P:cond-multidist-lower-II`
- `S:multidist-perm` before `P:key`
- `S:multidist-ruzsa-I` before `P:multidist-ruzsa-II`
- `S:multidist-ruzsa-II` before `P:key`
- `S:multidist-ruzsa-II` before `P:multi-zero`
- `S:multidist-ruzsa-II` before `P:xi-z2-w-dist`
- `S:multidist-ruzsa-III` before `P:k-vanish`
- `S:multidist-ruzsa-III` before `P:tau-ref`
- `S:multidist-ruzsa-IV` before `P:ent-w`
- `S:multidist-ruzsa-IV` before `P:ent-z2`
- `S:mutual-w-z2` before `P:xi-z2-w-dist`
- `S:pfr_aux_torsion` before `P:pfr-torsion`
- `S:prop:52` before `P:k-vanish`
- `S:sign-flip` before `P:sum-dilate-II`
- `S:sum-dilate-I` before `P:sum-dilate-II`
- `S:sum-dilate-II` before `P:ent-z2`
- `S:tau-def-multi` before `P:cond-multidist-lower-II`
- `S:tau-def-multi` before `P:key`
- `S:tau-def-multi` before `P:multidist-lower`
- `S:tau-def-multi` before `P:prop:52`
- `S:tau-def-multi` before `P:tau-ref`
- `S:tau-def-multi` before `S:tau-min-exist-multi`
- `S:tau-def-multi` before `S:tau-min-multi`
- `S:tau-min-exist-multi` before `P:main-entropy`
- `S:tau-min-multi` before `P:main-entropy`
- `S:tau-min-multi` before `S:cond-multidist-lower`
- `S:tau-min-multi` before `S:cond-multidist-lower-II`
- `S:tau-min-multi` before `S:k-vanish`
- `S:tau-min-multi` before `S:key`
- `S:tau-min-multi` before `S:multidist-lower`
- `S:tau-min-multi` before `S:prop:52`
- `S:tau-min-multi` before `S:tau-min-exist-multi`
- `S:tau-min-multi` before `S:tau-ref`
- `S:tau-ref` before `P:main-entropy`
- `S:xi-z2-w-dist` before `P:k-vanish`
