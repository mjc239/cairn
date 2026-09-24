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

- id `Lebesgue-differentiation`: lemma (Lebesgue differentiation); steps here: state and prove. Let $f$ be a bounded measurable function supported on a set of finite measure. Then for $\mu$ almost every $x$, we have $$\lim_{n\to \infty} \frac{1}{\mu(B_n)}\int_{B_n} f(y)\, dy= f(x),$$ where $\{B_n\}_{n\geq 1}$ is a sequence of balls with radii $r_n>0$ such that $x\in B_n$ for each $n\geq 1$ and \begin{equation*} \lim_{n\to \infty} r_n=0 \,. \end{equation*}
- id `estimate-bad-partial`: lemma (Estimate bad partial); steps here: state and prove. Let $x\in X\setminus\Omega$. Then \begin{equation*} |T_rb(x)| \le 3F(x)+\alpha/8, \end{equation*} where \begin{equation*} F(x) := 2^{a^3+2a+1} c\alpha \sum_{j\in J} \left(\frac{3r_j}{\rho(x,x_j)}\right)^{\frac{1}{a}}\frac{\mu(B_{3,j})}{V(x,x_j)}. \end{equation*}
- id `estimate-x-shift`: lemma (estimate x shift); steps here: state and prove. Let $0<r$ and $x\in X$. Let $g:X\to\C$ be a bounded measurable function supported on a set of finite measure. Then for all $x'$ with $\rho(x,x')\le r$. \begin{equation*} \left| T_r g(x) - T_r g(x') \right| \le 2^{a^3 + 2a + 2} Mg(x)\, . \end{equation*}
- id `Cotlar-sets`: lemma (Cotlar sets); steps here: state and prove. Assume that \eqref{two-sided-Hr-bound-assumption} holds. Let $0<r\le R$ and $x\in X$. Let $g:X\to\C$ be a bounded measurable function supported on a set of finite measure. Then the measure $|F_1|$ of the set $F_1$ of all $x'\in B(x,\frac {R} 4)$ such that \begin{equation} |T_rg(x')|> 4 M(T_rg)(x) \end{equation} is less than or equal to $\mu(B(x,\frac{R}{4}))/4$. Moreover, the measure $|F_2|$ of the set $F_2$ of all $x'\in B(x,\frac {R} 4)$ such that \begin{equation} |T_r(g\mathbf{1}_{B(x,\frac {R} 2)})(x')| > 2^{a^3 + 20a + 2} Mg(x) \end{equation} is less than or equal to $\mu(B(x,\frac{R}{4}))/4$.
- id `estimate-F-set`: lemma (Estimate F set); steps here: state and prove. For $F$ as defined in \Cref{estimate-bad-partial}, we have \begin{equation} \mu(\{x\in X\setminus\Omega: F(x)>\alpha/8\}) \le \frac{2^{a^3+9a+4}}{\alpha} \int |f(y)|\,d\mu(y)\,. \end{equation}
- id `nontangential-operator-boundary`: lemma (nontangential operator boundary); steps here: state and prove. Let $f:X\to\C$ be a bounded measurable function supported on a set of finite measure. For all $x\in X$, \begin{equation} T_*f(x) = \sup_{R_1 < R_2} \sup_{x'\in B(x,R_1)} \left|\int_{B(x',R_2)\setminus B(x',R_1)} K(x',y) f(y) \, \mathrm{d}\mu(y) \right| \end{equation}
- id `two-sided-metric-space-Carleson`: theorem (two-sided metric space Carleson); steps here: state and prove. For all integers $a \ge 4$ and real numbers $1<q\le 2$ the following holds. Let $(X,\rho,\mu,a)$ be a doubling metric measure space. Let $\Mf$ be a cancellative compatible collection of functions and let $K$ be a two-sided Calder\'on--Zygmund kernel on $(X,\rho,\mu,a)$. Assume that for every bounded measurable function $g$ on $X$ supported on a set of finite measure and all $r>0$ we have \begin{equation} \|T_r g\|_{2} \leq 2^{a^3} \|g\|_2\,. \end{equation} Then for all Borel sets $F$ and $G$ in $X$ and all Borel functions $f:X\to \C$ with $|f|\le \mathbf{1}_F$, we have, with $T$ defined in \eqref{def-main-op}, \begin{equation} \left|\int_{G} T f \, \mathrm{d}\mu\right| \leq \frac{2^{474a^3}}{(q-1)^6} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}}\, . \end{equation}
- id `simple-nontangential-operator`: lemma (simple nontangential operator); steps here: state and prove. Assume that \eqref{two-sided-Hr-bound-assumption} holds. For every $r>0$ and every bounded measurable function $g$ supported on a set of finite measure the function $T_{*}^r g$ is lower-semicontinuous and we have \begin{equation} \|T_{*}^rg\|_2\le 2^{a^3+24a+6}\|g\|_2, \end{equation}
- id `geometric-series-estimate`: lemma (geometric series estimate); steps here: state and prove. For all real numbers $x\ge 4$, \begin{equation*} \sum_{n=0}^\infty 2^{-\frac{n}{x}} \le 2^x. \end{equation*}
- id `estimate-bad`: lemma (Estimate bad); steps here: state and prove. We have \begin{equation*} \mu\left({\{x\in X: |T_r b(x)|>\alpha/2\}}\right) \le \frac{\frac{2^{5a}}{c} + 2^{a^3+9a+4}}{\alpha} \int |f(y)|\,d\mu(y) \,. \end{equation*}
- id `ball-covering`: lemma (Ball covering); steps here: state and prove. Given an open set $O\ne X$, there exists a countable family of balls $B_j = B(x_j, r_j)$ such that \begin{equation} B_j \cap B_{j'} = \emptyset \quad \text{ for } j \ne j', \end{equation} and \begin{equation} \bigcup_j B_{3,j} = O, \end{equation} and \begin{equation} B_{7,j} \cap (X \setminus O) \ne \emptyset \quad \text{ for all } j \end{equation} and we have the bounded intersection property that each $x\in O$ is contained in at most $2^{6a}$ of the $B_{3,j}$.
- id `Cotlar-estimate`: lemma (Cotlar estimate); steps here: state and prove. Assume that \eqref{two-sided-Hr-bound-assumption} holds. Let $0<r\le R$ and $x\in X$. Let $g:X\to\C$ be a bounded measurable function supported on a set of finite measure. Then \begin{equation} |T_Rg(x)| \le 2^{2}M(T_rg)(x)+ 2^{a^3+20a+3} Mg(x) \, . \end{equation}
- id `nontangential-from-simple`: lemma (nontangential-from-simple); steps here: state and prove. Assume \eqref{two-sided-Hr-bound-assumption} holds. Then, for every bounded measurable function $g : X \to \C$ supported on a set of finite measure we have \begin{equation} \|T_*g\|_2\le 2^{3a^3}\|g\|_2. \end{equation}
- id `small-annulus`: lemma (small annulus); steps here: state and prove. Let $f:X\to\C$ be a bounded measurable function supported on a set of finite measure. Let $x\in X$ and $R>0$. Then, for all $\epsilon>0$, there exists some $\delta>0$ such that \begin{equation} \left| \int_{R<\rho(x,y)<R+\delta} K(x,y) f(y) \, d\mu(y) \right| \le \epsilon \end{equation} and \begin{equation} \left| \int_{R-\delta<\rho(x,y)<R} K(x,y) f(y) \, d\mu(y) \right| \le \epsilon \,. \end{equation}
- id `Cotlar-control`: lemma (Cotlar control); steps here: state and prove. Let $0<r\le R$ and $x\in X$. Let $g:X\to\C$ be a bounded measurable function supported on a set of finite measure. Then for all $x'\in X$ with $\rho(x,x')\le\frac {R}{4}$ we have \begin{equation} \left|T_R g(x) \right|\le |T_r(g-g\mathbf{1}_{B(x,\frac {R} 2)})(x')| + 2^{a^3 + 4a + 1} Mg(x)\, . \end{equation}
- id `calderon-zygmund-weak-1-1`: lemma (Calderon-Zygmund Weak (1, 1)); steps here: state and prove. Let $f:X\to\C$ be a bounded measurable function supported on a set of finite measure and assume for some $r>0$ that for every bounded measurable function $g:X\to\C$ supported on a set of finite measure, \begin{equation} \|T_rg\|_{2}\le 2^{a^3} \|g\|_2. \end{equation} Then for all $\alpha>0$, we have \begin{equation} \mu\left(\{x\in X: |T_r f(x)|>\alpha\}\right)\le \frac{2^{a^3 + 19a}}{\alpha} \int |f(y)|\, d\mu(y). \end{equation}
- id `maximal-theorem`: lemma (Maximal theorem); steps here: state and prove. Let $f: X \to \C$ be bounded, measurable, supported on a set of finite measure, and let $\alpha > 0$. Then \begin{equation} \mu(\{x\in X : Mf(x) > \alpha\}) \le \frac{2^{2a}}{\alpha} \int |f(y)|\, d\mu(y). \end{equation}
- id `estimate-good`: lemma (Estimate good); steps here: state and prove. \begin{equation*} \mu\left(\{x\in X: |T_r g(x)|>{\alpha}/2\}\right) \le \frac{2^{2a^3+3a+2}c}{\alpha} \int |f(y)|\, d\mu(y). \end{equation*}
- id `Calderon-Zygmund-decomposition`: lemma (Calderon Zygmund decomposition); steps here: state and prove. Let $f$ be a bounded, a.e. measurable function supported on a set of finite measure and let $\alpha>\frac{1}{\mu(X)}\int |f|\,d\mu$. Then there exists a bounded a.e. measurable function $g$ supported on a set of finite measure, a countable family of balls $B_{3,j}$ (where we allow $B_{3,1} = X$ in the special case that $\mu(X)<\infty$) such that each $x\in X$ is contained in at most $2^{6a}$ of the $B_{3,j}$, and a countable family of a.e. measurable functions $\{b_j\}_{j\in J}$ such that for all $x \in X$ \begin{equation} f(x)= g(x) + \sum_{j} b_j(x) \end{equation} and such that the following holds. For almost every $x\in X$, \begin{equation} |g(x)|\leq 2^{3a} \alpha\,. \end{equation} We have \begin{equation} \int |g(y)|\, d\mu(y)\leq \int |f(y)|\, d\mu(y). \end{equation} For every $j$ \begin{equation} \operatorname{supp} b_j \subset B_{3,j}\,. \end{equation} For every $j$ \begin{equation} \int_{B_{3,j}} b_j(x)\, d\mu(x)=0, \end{equation} and \begin{equation} \int_{B_{3,j}} |b_j(x)|\, d\mu(x) \leq 2^{2a+1} \alpha \mu(B_{3,j}). \end{equation} We have \begin{equation} \sum_j \mu(B_{3,j})\leq \frac{2^{4a}}{\alpha}\int |f(y)|\, d\mu(y) \end{equation} and \begin{equation} \sum_{j}\int_{B_{3,j}} |b_j(y)|\, d\mu(y)\leq 2 \int |f(y)|\, d\mu(y)\,. \end{equation}

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:Calderon-Zygmund-decomposition` before `P:calderon-zygmund-weak-1-1`
- `S:Calderon-Zygmund-decomposition` before `P:estimate-F-set`
- `S:Calderon-Zygmund-decomposition` before `P:estimate-bad`
- `S:Calderon-Zygmund-decomposition` before `P:estimate-bad-partial`
- `S:Calderon-Zygmund-decomposition` before `P:estimate-good`
- `S:Cotlar-control` before `P:Cotlar-estimate`
- `S:Cotlar-estimate` before `P:simple-nontangential-operator`
- `S:Cotlar-sets` before `P:Cotlar-estimate`
- `S:Lebesgue-differentiation` before `P:Calderon-Zygmund-decomposition`
- `S:ball-covering` before `P:Calderon-Zygmund-decomposition`
- `S:ball-covering` before `P:calderon-zygmund-weak-1-1`
- `S:ball-covering` before `P:estimate-F-set`
- `S:ball-covering` before `P:estimate-bad`
- `S:ball-covering` before `P:estimate-bad-partial`
- `S:ball-covering` before `P:estimate-good`
- `S:calderon-zygmund-weak-1-1` before `P:Cotlar-sets`
- `S:estimate-F-set` before `P:estimate-bad`
- `S:estimate-bad` before `P:calderon-zygmund-weak-1-1`
- `S:estimate-bad-partial` before `P:estimate-bad`
- `S:estimate-good` before `P:calderon-zygmund-weak-1-1`
- `S:estimate-x-shift` before `P:Cotlar-control`
- `S:estimate-x-shift` before `P:simple-nontangential-operator`
- `S:geometric-series-estimate` before `P:estimate-F-set`
- `S:geometric-series-estimate` before `P:estimate-x-shift`
- `S:maximal-theorem` before `P:Calderon-Zygmund-decomposition`
- `S:maximal-theorem` before `P:calderon-zygmund-weak-1-1`
- `S:maximal-theorem` before `P:estimate-bad-partial`
- `S:maximal-theorem` before `P:estimate-good`
- `S:nontangential-from-simple` before `P:two-sided-metric-space-Carleson`
- `S:nontangential-operator-boundary` before `P:nontangential-from-simple`
- `S:simple-nontangential-operator` before `P:nontangential-from-simple`
- `S:small-annulus` before `P:nontangential-operator-boundary`
