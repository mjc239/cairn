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

- id `r417`: definition; steps here: state only (no proof needed). Let $m$ be a positive integer, and let $X_{[m]} = (X_i)_{1 \leq i \leq m}$ be an $m$-tuple of $G$-valued random variables $X_i$. Then we define \[ D[X_{[m]}] := \bbH[\sum_{i=1}^m \tilde X_i] - \frac{1}{m} \sum_{i=1}^m \bbH[\tilde X_i], \] where the $\tilde X_i$ are independent copies of the $X_i$.
- id `r405`: lemma; steps here: state and prove. Let $X,Y,Z$. For any functions $f, g$ on the ranges of $X, Y$ respectively, we have $\bbI[f(X) : g(Y )|Z] \leq \bbI[X :Y |Z]$.
- id `r861`: lemma; steps here: state and prove. If the $(X_i,Y_i)$ are independent, \begin{equation} D[ X_{[m]} | Y_{[m]}] := \bbH[\sum_{i=1}^m X_i \big| (Y_j)_{1 \leq j \leq m} ] - \frac{1}{m} \sum_{i=1}^m \bbH[ X_i | Y_i]. \end{equation}
- id `r262`: lemma; steps here: state and prove. Let $X,Y$ be random variables. For any functions $f, g$ on the ranges of $X, Y$ respectively, we have $\bbI[f(X) : g(Y )] \leq \bbI[X : Y]$.
- id `r526`: lemma; steps here: state and prove. Let $(X_i)_{1 \leq i \leq m}$ and $(Y_j)_{1 \leq j \leq l}$ be tuples of jointly independent random variables (so the $X$'s and $Y$'s are also independent of each other), and let $f: \{1,\dots,l\} \to \{1,\dots,m\}$ be a function, then $$ \bbH[\sum_{j=1}^l Y_j] \leq \bbH[ \sum_{i=1}^m X_i ] + \sum_{j=1}^l (\bbH[ Y_j - X_{f(j)}] - \bbH[X_{f(j)}]).$$
- id `r678`: lemma; steps here: state and prove. We have $\bbI[W : Z_2] \leq 2 (m-1) k$.
- id `r358`: lemma; steps here: state and prove. If $X_{[m]} = (X_i)_{1 \leq i \leq m}$ and $Y_{[m]} = (Y_i)_{1 \leq i \leq m}$ are tuples of random variables, then $D[ X_{[m]} | Y_{[m]} ] \geq 0$.
- id `r233`: lemma; steps here: state and prove. If $(X_i)_{1 \leq i \leq m}$ is a $\tau$-minimizer, and $k := D[(X_i)_{1 \leq i \leq m}]$, then for any other tuples $(X'_i)_{1 \leq i \leq m}$ and $(Y_i)_{1 \leq i \leq m}$ with the $X'_i$ $G$-valued, one has $$ k - D[(X'_i)_{1 \leq i \leq m} | (Y_i)_{1 \leq i \leq m}] \leq \eta \sum_{i=1}^m d[X_i; X'_i|Y_i].$$
- id `r108`: lemma; steps here: state and prove. If $\phi: \{1,\dots,m\} \to \{1,\dots,m\}$ is a bijection, then $D[X_{[m]}] = D[(X_{\phi(j)})_{1 \leq j \leq m}]$.
- id `r674`: lemma; steps here: state and prove. Let $m \ge 2$, and let $X_{[m]}$ be a tuple of $G$-valued random variables. If the $X_i$ all have the same distribution, then $D[X_{[m]}] \leq m d[X_i;X_i]$ for any $1 \leq i \leq m$.
- id `r999`: corollary; steps here: state and prove. With the notation of the previous lemma, we have \begin{equation} k - D[ X'_{[m]} | Y_{[m]} ] \leq \eta \sum_{i=1}^m d[X_{\sigma(i)};X'_i|Y_i] \end{equation} for any permutation $\sigma : \{1,\dots,m\} \rightarrow \{1,\dots,m\}$.
- id `r970`: corollary; steps here: state and prove. Let $G$ be an abelian group and let $m \geq 2$. Suppose that $X_{i,j}$, $1 \leq i, j \leq m$, are independent $G$-valued random variables. Then \begin{align*} &\bbI[ \bigl(\sum_{i=1}^m X_{i,j}\bigr)_{j =1}^{m} : \bigl(\sum_{j=1}^m X_{i,j}\bigr)_{i = 1}^m \; \big| \; \sum_{i=1}^m \sum_{j = 1}^m X_{i,j} ] \\ &\quad \leq \sum_{j=1}^{m-1} \Bigl(D[(X_{i, j})_{i = 1}^m] - D[ (X_{i, j})_{i = 1}^m \; \big| \; (X_{i,j} + \cdots + X_{i,m})_{i =1}^m ]\Bigr) \\ & \qquad\qquad\qquad\qquad + D[(X_{i,m})_{i=1}^m] - D[ \bigl(\sum_{j=1}^m X_{i,j}\bigr)_{i=1}^m ], \end{align*} where all the multidistances here involve the indexing set $\{1,\dots, m\}$.
- id `r138`: lemma; steps here: state and prove. Let $X,Y,X'$ be independent $G$-valued random variables, with $X'$ a copy of $X$, and let $a$ be an integer. Then $$\bbH[X-(a+1)Y] \leq \bbH[X-aY] + \bbH[X-Y-X'] - \bbH[X]$$ and $$\bbH[X-(a-1)Y] \leq \bbH[X-aY] + \bbH[X-Y-X'] - \bbH[X].$$
- id `r704`: lemma; steps here: state and prove. Let $X,Y$ be independent $G$-valued random variables, and let $a$ be an integer. Then $$\bbH[X-aY] - \bbH[X] \leq 4 |a| d[X;Y].$$
- id `r939`: lemma; steps here: state and prove. We have $\bbH[W] \leq (2m-1)k + \frac1m \sum_{i=1}^m \bbH[X_i]$.
- id `r322`: lemma; steps here: state and prove. Let $X$ be a random variable. Then for any function $f$ on the range of $X$, one has $\bbH[f(X)] \leq \bbH[X]$.
- id `r683`: theorem; steps here: state and prove. Suppose that $G$ is a finite abelian group of torsion $m$. Suppose that $X$ is a $G$-valued random variable. Then there exists a subgroup $H \leq G$ such that \[ d[X;U_H] \leq 64 m^3 d[X;X].\]
- id `r571`: proposition; steps here: state and prove. If $D[X_{[m]}]=0$, then for each $1 \leq i \leq m$ there is a finite subgroup $H_i \leq G$ such that $d[X_i; U_{H_i}] = 0$.
- id `r275`: lemma; steps here: state and prove. We have $\sum_{i=1}^m d[X_i;Z_2|W] \leq 4(m^3-m^2) k$.
- id `r947`: proposition; steps here: state and prove. We have $k = 0$.
- id `r988`: theorem; steps here: state and prove. Suppose that $G$ is a finite abelian group of torsion $m$. If $A \subset G$ is non-empty and $|A+A| \leq K|A|$, then $A$ can be covered by at most $mK^{256m^3+1}$ translates of a subspace $H$ of $G$ with $|H| \leq |A|$.
- id `r990`: lemma; steps here: state and prove. Let $m \ge 2$, and let $X_{[m]}$ be a tuple of $G$-valued random variables. Then $$\sum_{j=1}^m d[X_j;X_j] \leq 2 m D[X_{[m]}].$$
- id `r898`: proposition; steps here: state and prove. Suppose that $X_{i,j}$, $1 \leq i,j \leq m$, are jointly independent $G$-valued random variables, such that for each $j = 1,\dots,m$, the random variables $(X_{i,j})_{i = 1}^m$ coincide in distribution with some permutation of $X_{[m]}$. Write \[ {\mathcal I} := \bbI[ \bigl(\sum_{i=1}^m X_{i,j}\bigr)_{j =1}^{m} : \bigl(\sum_{j=1}^m X_{i,j}\bigr)_{i = 1}^m \; \big| \; \sum_{i=1}^m \sum_{j = 1}^m X_{i,j} ]. \] Then \begin{equation} {\mathcal I} \leq m(4m+1) \eta k. \end{equation}
- id `r820`: lemma; steps here: state and prove. Let $G$ be an abelian group, let $(T_1,T_2,T_3)$ be a $G^3$-valued random variable such that $T_1+T_2+T_3=0$ holds identically, and write \[ \delta := \bbI[T_1 : T_2] + \bbI[T_1 : T_3] + \bbI[T_2 : T_3]. \] Let $Y_1,\dots,Y_n$ be some further $G$-valued random variables and let $\alpha>0$ be a constant. Then there exists a random variable $U$ such that \begin{equation} d[U;U] + \alpha \sum_{i=1}^n d[Y_i;U] \leq \Bigl(2 + \frac{\alpha n}{2} \Bigr) \delta + \alpha \sum_{i=1}^n d[Y_i;T_2]. \end{equation}
- id `r737`: proposition; steps here: state and prove. We have \[ \bbI[Z_1 : Z_2\, |\, W],\ \bbI[Z_2 : Z_3\, |\, W],\ \bbI[Z_1 : Z_3\, |\, W] \leq t \] where \begin{equation} t := m(4m+1) \eta k. \end{equation}
- id `r621`: definition; steps here: state only (no proof needed). If $(X_i)_{1 \leq i \leq m}$ is a tuple, we define its $\tau$-functional $$ \tau[ (X_i)_{1 \leq i \leq m}] := D[(X_i)_{1 \leq i \leq m}] + \eta \sum_{i=1}^m d[X_i; X^0].$$
- id `r487`: lemma; steps here: state and prove. Let $\pi \colon G \to H$ be a homomorphism of abelian groups. Let $I$ be a finite index set and let $X_{[m]}$ be a tuple of $G$-valued random variables. Let $Y_{[m]}$ be another tuple of random variables (not necessarily $G$-valued). Suppose that the pairs $(X_i, Y_i)$ are jointly independent of one another (but $X_i$ need not be independent of $Y_i$). Then \begin{align}\nonumber D[ X_{[m]} | Y_{[m]} ] &= D[ X_{[m]} \,|\, \pi(X_{[m]}), Y_{[m]}] + D[ \pi(X_{[m]}) \,|\, Y_{[m]}] \\ &\quad\qquad + \bbI[ \sum_{i=1}^m X_i : \pi(X_{[m]}) \; \big| \; \pi\bigl(\sum_{i=1}^m X_i \bigr), Y_{[m]} ]. \end{align}
- id `r305`: lemma; steps here: state and prove. If $n \geq 0$ and $X, Y_1, \dots, Y_n$ are jointly independent $G$-valued random variables, then $$\bbH\left[X + \sum_{i=1}^n Y_i\right] - \bbH[X] \leq \sum_{i=1}^n \left(\bbH[X+Y_i] - \bbH[X]\right).$$
- id `r455`: definition; steps here: state only (no proof needed). A $\tau$-minimizer is a tuple $(X_i)_{1 \leq i \leq m}$ that minimizes the $\tau$-functional among all tuples of $G$-valued random variables.
- id `r201`: lemma; steps here: state and prove. We have \begin{equation} Z_1+Z_2+Z_3= 0 \end{equation}
- id `r310`: lemma; steps here: state and prove. If $X,Y$ are $G$-valued, then $$ d[X ; -Y] \leq 3 d[X;Y].$$
- id `r687`: proposition; steps here: state and prove. If $(X_i)_{1 \leq i \leq m}$ is a $\tau$-minimizer, then $\sum_{i=1}^m d[X_i; X^0] \leq \frac{2m}{\eta} d[X^0; X^0]$.
- id `r790`: lemma; steps here: state and prove. Let $m$ be a positive integer. Suppose one has a sequence \begin{equation} G_m \to G_{m-1} \to \dots \to G_1 \to G_0 = \{0\} \end{equation} of homomorphisms between abelian groups $G_0,\dots,G_m$, and for each $d=0,\dots,m$, let $\pi_d : G_m \to G_d$ be the homomorphism from $G_m$ to $G_d$ arising from this sequence by composition (so for instance $\pi_m$ is the identity homomorphism and $\pi_0$ is the zero homomorphism). Let $X_{[m]} = (X_i)_{1 \leq i \leq m}$ be a jointly independent tuple of $G_m$-valued random variables. Then \begin{equation} \begin{split} D[ X_{[m]} ] &= \sum_{d=1}^m D[ \pi_d(X_{[m]}) \,|\, \pi_{d-1}(X_{[m]})] \\ &\quad + \sum_{d=1}^{m-1} \bbI[ \sum_i X_i : \pi_d(X_{[m]}) \; \big| \; \pi_d\big(\sum_i X_i\big), \pi_{d-1}(X_{[m]}) ]. \end{split} \end{equation} In particular, by [another result], \begin{align}\nonumber D[ X_{[m]} ] \geq & \sum_{d=1}^m D[ \pi_d(X_{[m]})|\pi_{d-1}(X_{[m]}) ] \\ & + \bbI[ \sum_i X_i : \pi_1(X_{[m]}) \; \big| \; \pi_1\bigl(\sum_i X_i\bigr) ]. \end{align}
- id `r543`: lemma; steps here: state and prove. For any such tuple, we have $D[X_{[m]}] \geq 0$.
- id `r705`: lemma; steps here: state and prove. Suppose that $G$ is a finite abelian group of torsion $m$. If $A \subset G$ is non-empty and $|A+A| \leq K|A|$, then $A$ can be covered by at most $K ^ {128m^3+1}|A|^{1/2}/|H|^{1/2}$ translates of a subspace $H$ of $G$ with \begin{equation} |H|/|A| \in [K^{-256m^3}, K^{256m^3}]. \end{equation}
- id `r298`: definition; steps here: state only (no proof needed). If $X_{[m]} = (X_i)_{1 \leq i \leq m}$ and $Y_{[m]} = (Y_i)_{1 \leq i \leq m}$ are tuples of random variables, with the $X_i$ being $G$-valued (but the $Y_i$ need not be), then we define \begin{equation} D[ X_{[m]} | Y_{[m]} ] = \sum_{(y_i)_{1 \leq i \leq m}} \biggl(\prod_{1 \leq i \leq m} p_{Y_i}(y_i)\biggr) D[ (X_i \,|\, Y_i \mathop{=}y_i)_{1 \leq i \leq m}] \end{equation} where each $y_i$ ranges over the support of $p_{Y_i}$ for $1 \leq i \leq m$.
- id `r604`: lemma; steps here: state and prove. If $X_{[m]} = (X_i)_{1 \leq i \leq m}$ are jointly independent, then $D[X_{[m]}] = \bbH[\sum_{i=1}^m X_i] - \frac{1}{m} \sum_{i=1}^m \bbH[X_i]$.
- id `r206`: lemma; steps here: state and prove. Let $\pi \colon G \to H$ be a homomorphism of abelian groups and let $X_{[m]}$ be a tuple of jointly independent $G$-valued random variables. Then $D[X_{[m]}]$ is equal to \begin{equation} D[ X_{[m]} | \pi(X_{[m]}) ] +D[ \pi(X_{[m]}) ] + \bbI[ \sum_{i=1}^m X_i : \pi(X_{[m]}) \; \big| \; \pi\bigl(\sum_{i=1}^m X_i\bigr) ] \end{equation} where $\pi(X_{[m]}) := (\pi(X_i))_{1 \leq i \leq m}$.
- id `r781`: lemma; steps here: state and prove. We have $\bbH[Z_2] \leq (8m^2-16m+1) k + \frac{1}{m} \sum_{i=1}^m \bbH[X_i]$.
- id `r499`: lemma; steps here: state and prove. If $n \geq 1$ and $X, Y_1, \dots, Y_n$ are jointly independent $G$-valued random variables, then $$ d[X; \sum_{i=1}^n Y_i] \leq 2 \sum_{i=1}^n d[X; Y_i].$$
- id `r403`: lemma; steps here: state and prove. Let $m \ge 2$, and let $X_{[m]}$ be a tuple of $G$-valued random variables. Then $$\sum_{1 \leq j,k \leq m: j \neq k} d[X_j; -X_k] \leq m(m-1) D[X_{[m]}].$$
- id `r616`: lemma; steps here: state and prove. If $X_{[m]} = (X_i)_{1 \leq i \leq m}$ and $Y_{[m]} = (Y_i)_{1 \leq i \leq m}$ are such that $X_i$ and $Y_i$ have the same distribution for each $i$, then $D[X_{[m]}] = D[Y_{[m]}]$.
- id `r611`: lemma; steps here: state and prove. If $(X_i)_{1 \leq i \leq m}$ is a $\tau$-minimizer, and $k := D[(X_i)_{1 \leq i \leq m}]$, then for any other tuple $(X'_i)_{1 \leq i \leq m}$, one has $$ k - D[(X'_i)_{1 \leq i \leq m}] \leq \eta \sum_{i=1}^m d[X_i; X'_i].$$
- id `r117`: definition; steps here: state only (no proof needed). We set $\eta := \frac{1}{32m^3}$.
- id `r433`: proposition; steps here: state and prove. If $G$ is finite, then a $\tau$-minimizer exists.
- id `r726`: lemma; steps here: state and prove. Let $m \ge 2$, and let $X_{[m]}$ be a tuple of independent $G$-valued random variables. Let $W := \sum_{i=1}^m X_i$. Then $$ d[W;-W] \leq 2 D[X_i].$$
- id `r992`: lemma; steps here: state and prove. Let $X,Y$ be random variables. For any function $f, g$ on the range of $X$, we have $\bbI[f(X) : Y] \leq \bbI[X:Y]$.
- id `r511`: lemma; steps here: state and prove. If $n \geq 1$ and $X, Y_1, \dots, Y_n$ are jointly independent $G$-valued random variables, then $$d\left[X; \sum_{i=1}^n Y_i\right] \leq d\left[X; Y_1\right] + \frac{1}{2}\left(\bbH\left[ \sum_{i=1}^n Y_i\right] - \bbH[Y_1]\right).$$

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:r108` before `P:r898`
- `S:r108` before `P:r999`
- `S:r117` before `P:r683`
- `S:r117` before `S:r201`
- `S:r117` before `S:r233`
- `S:r117` before `S:r275`
- `S:r117` before `S:r433`
- `S:r117` before `S:r455`
- `S:r117` before `S:r611`
- `S:r117` before `S:r621`
- `S:r117` before `S:r678`
- `S:r117` before `S:r687`
- `S:r117` before `S:r737`
- `S:r117` before `S:r781`
- `S:r117` before `S:r898`
- `S:r117` before `S:r939`
- `S:r117` before `S:r947`
- `S:r117` before `S:r999`
- `S:r138` before `P:r704`
- `S:r201` before `P:r947`
- `S:r206` before `P:r487`
- `S:r233` before `P:r999`
- `S:r262` before `P:r405`
- `S:r275` before `P:r947`
- `S:r298` before `P:r898`
- `S:r298` before `S:r206`
- `S:r298` before `S:r233`
- `S:r298` before `S:r358`
- `S:r298` before `S:r487`
- `S:r298` before `S:r790`
- `S:r298` before `S:r861`
- `S:r298` before `S:r970`
- `S:r298` before `S:r999`
- `S:r305` before `P:r499`
- `S:r305` before `P:r526`
- `S:r305` before `P:r674`
- `S:r305` before `P:r781`
- `S:r305` before `P:r939`
- `S:r310` before `P:r704`
- `S:r322` before `P:r310`
- `S:r358` before `P:r790`
- `S:r403` before `P:r990`
- `S:r405` before `P:r737`
- `S:r417` before `P:r358`
- `S:r417` before `P:r433`
- `S:r417` before `P:r487`
- `S:r417` before `P:r683`
- `S:r417` before `P:r687`
- `S:r417` before `P:r861`
- `S:r417` before `S:r108`
- `S:r417` before `S:r206`
- `S:r417` before `S:r233`
- `S:r417` before `S:r275`
- `S:r417` before `S:r298`
- `S:r417` before `S:r403`
- `S:r417` before `S:r543`
- `S:r417` before `S:r571`
- `S:r417` before `S:r604`
- `S:r417` before `S:r611`
- `S:r417` before `S:r616`
- `S:r417` before `S:r621`
- `S:r417` before `S:r674`
- `S:r417` before `S:r678`
- `S:r417` before `S:r726`
- `S:r417` before `S:r737`
- `S:r417` before `S:r781`
- `S:r417` before `S:r790`
- `S:r417` before `S:r898`
- `S:r417` before `S:r939`
- `S:r417` before `S:r947`
- `S:r417` before `S:r970`
- `S:r417` before `S:r990`
- `S:r417` before `S:r999`
- `S:r433` before `P:r683`
- `S:r455` before `P:r683`
- `S:r455` before `S:r233`
- `S:r455` before `S:r433`
- `S:r455` before `S:r611`
- `S:r455` before `S:r687`
- `S:r455` before `S:r737`
- `S:r455` before `S:r898`
- `S:r455` before `S:r947`
- `S:r455` before `S:r999`
- `S:r487` before `P:r790`
- `S:r511` before `P:r275`
- `S:r526` before `P:r898`
- `S:r543` before `P:r275`
- `S:r543` before `P:r358`
- `S:r543` before `P:r687`
- `S:r543` before `P:r947`
- `S:r571` before `P:r683`
- `S:r604` before `P:r206`
- `S:r604` before `P:r403`
- `S:r604` before `P:r543`
- `S:r604` before `P:r674`
- `S:r604` before `P:r678`
- `S:r604` before `P:r726`
- `S:r604` before `P:r781`
- `S:r604` before `P:r861`
- `S:r604` before `P:r898`
- `S:r604` before `P:r939`
- `S:r604` before `P:r970`
- `S:r611` before `P:r233`
- `S:r611` before `P:r898`
- `S:r611` before `P:r947`
- `S:r616` before `P:r403`
- `S:r616` before `P:r433`
- `S:r616` before `P:r487`
- `S:r616` before `P:r543`
- `S:r616` before `P:r674`
- `S:r616` before `P:r678`
- `S:r616` before `P:r737`
- `S:r616` before `P:r781`
- `S:r616` before `P:r861`
- `S:r616` before `P:r898`
- `S:r616` before `P:r939`
- `S:r621` before `P:r611`
- `S:r621` before `P:r687`
- `S:r621` before `P:r737`
- `S:r621` before `P:r898`
- `S:r621` before `P:r999`
- `S:r621` before `S:r433`
- `S:r621` before `S:r455`
- `S:r674` before `P:r687`
- `S:r674` before `P:r947`
- `S:r678` before `P:r275`
- `S:r683` before `P:r705`
- `S:r687` before `P:r683`
- `S:r704` before `P:r781`
- `S:r705` before `P:r988`
- `S:r726` before `P:r781`
- `S:r726` before `P:r939`
- `S:r737` before `P:r947`
- `S:r781` before `P:r275`
- `S:r790` before `P:r970`
- `S:r820` before `P:r947`
- `S:r861` before `P:r206`
- `S:r861` before `P:r970`
- `S:r898` before `P:r737`
- `S:r939` before `P:r678`
- `S:r947` before `P:r683`
- `S:r970` before `P:r898`
- `S:r990` before `P:r275`
- `S:r990` before `P:r571`
- `S:r990` before `P:r898`
- `S:r992` before `P:r262`
- `S:r999` before `P:r898`
