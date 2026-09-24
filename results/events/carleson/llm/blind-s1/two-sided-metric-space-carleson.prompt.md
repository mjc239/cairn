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

- id `r233`: lemma; steps here: state and prove. For $F$ as defined in `r683`, we have \begin{equation} \mu(\{x\in X\setminus\Omega: F(x)>\alpha/8\}) \le \frac{2^{a^3+9a+4}}{\alpha} \int |f(y)|\,d\mu(y)\,. \end{equation}
- id `r108`: lemma; steps here: state and prove. Let $f:X\to\C$ be a bounded measurable function supported on a set of finite measure. Let $x\in X$ and $R>0$. Then, for all $\epsilon>0$, there exists some $\delta>0$ such that \begin{equation} \left| \int_{R<\rho(x,y)<R+\delta} K(x,y) f(y) \, d\mu(y) \right| \le \epsilon \end{equation} and \begin{equation} \left| \int_{R-\delta<\rho(x,y)<R} K(x,y) f(y) \, d\mu(y) \right| \le \epsilon \,. \end{equation}
- id `r674`: lemma; steps here: state and prove. Let $0<r\le R$ and $x\in X$. Let $g:X\to\C$ be a bounded measurable function supported on a set of finite measure. Then for all $x'\in X$ with $\rho(x,x')\le\frac {R}{4}$ we have \begin{equation} \left|T_R g(x) \right|\le |T_r(g-g\mathbf{1}_{B(x,\frac {R} 2)})(x')| + 2^{a^3 + 4a + 1} Mg(x)\, . \end{equation}
- id `r999`: lemma; steps here: state and prove. Let $f$ be a bounded, a.e. measurable function supported on a set of finite measure and let $\alpha>\frac{1}{\mu(X)}\int |f|\,d\mu$. Then there exists a bounded a.e. measurable function $g$ supported on a set of finite measure, a countable family of balls $B_{3,j}$ (where we allow $B_{3,1} = X$ in the special case that $\mu(X)<\infty$) such that each $x\in X$ is contained in at most $2^{6a}$ of the $B_{3,j}$, and a countable family of a.e. measurable functions $\{b_j\}_{j\in J}$ such that for all $x \in X$ \begin{equation} f(x)= g(x) + \sum_{j} b_j(x) \end{equation} and such that the following holds. For almost every $x\in X$, \begin{equation} |g(x)|\leq 2^{3a} \alpha\,. \end{equation} We have \begin{equation} \int |g(y)|\, d\mu(y)\leq \int |f(y)|\, d\mu(y). \end{equation} For every $j$ \begin{equation} \operatorname{supp} b_j \subset B_{3,j}\,. \end{equation} For every $j$ \begin{equation} \int_{B_{3,j}} b_j(x)\, d\mu(x)=0, \end{equation} and \begin{equation} \int_{B_{3,j}} |b_j(x)|\, d\mu(x) \leq 2^{2a+1} \alpha \mu(B_{3,j}). \end{equation} We have \begin{equation} \sum_j \mu(B_{3,j})\leq \frac{2^{4a}}{\alpha}\int |f(y)|\, d\mu(y) \end{equation} and \begin{equation} \sum_{j}\int_{B_{3,j}} |b_j(y)|\, d\mu(y)\leq 2 \int |f(y)|\, d\mu(y)\,. \end{equation}
- id `r970`: lemma; steps here: state and prove. Assume that `r571` holds. Let $0<r\le R$ and $x\in X$. Let $g:X\to\C$ be a bounded measurable function supported on a set of finite measure. Then \begin{equation} |T_Rg(x)| \le 2^{2}M(T_rg)(x)+ 2^{a^3+20a+3} Mg(x) \, . \end{equation}
- id `r138`: lemma; steps here: state and prove. Assume that `r571` holds. Let $0<r\le R$ and $x\in X$. Let $g:X\to\C$ be a bounded measurable function supported on a set of finite measure. Then the measure $|F_1|$ of the set $F_1$ of all $x'\in B(x,\frac {R} 4)$ such that \begin{equation} |T_rg(x')|> 4 M(T_rg)(x) \end{equation} is less than or equal to $\mu(B(x,\frac{R}{4}))/4$. Moreover, the measure $|F_2|$ of the set $F_2$ of all $x'\in B(x,\frac {R} 4)$ such that \begin{equation} |T_r(g\mathbf{1}_{B(x,\frac {R} 2)})(x')| > 2^{a^3 + 20a + 2} Mg(x) \end{equation} is less than or equal to $\mu(B(x,\frac{R}{4}))/4$.
- id `r704`: lemma; steps here: state and prove. We have \begin{equation*} \mu\left({\{x\in X: |T_r b(x)|>\alpha/2\}}\right) \le \frac{\frac{2^{5a}}{c} + 2^{a^3+9a+4}}{\alpha} \int |f(y)|\,d\mu(y) \,. \end{equation*}
- id `r939`: lemma; steps here: state and prove. Assume that `r571` holds. For every $r>0$ and every bounded measurable function $g$ supported on a set of finite measure the function $T_{*}^r g$ is lower-semicontinuous and we have \begin{equation} \|T_{*}^rg\|_2\le 2^{a^3+24a+6}\|g\|_2, \end{equation}
- id `r322`: lemma; steps here: state and prove. \begin{equation*} \mu\left(\{x\in X: |T_r g(x)|>{\alpha}/2\}\right) \le \frac{2^{2a^3+3a+2}c}{\alpha} \int |f(y)|\, d\mu(y). \end{equation*}
- id `r683`: lemma; steps here: state and prove. Let $x\in X\setminus\Omega$. Then \begin{equation*} |T_rb(x)| \le 3F(x)+\alpha/8, \end{equation*} where \begin{equation*} F(x) := 2^{a^3+2a+1} c\alpha \sum_{j\in J} \left(\frac{3r_j}{\rho(x,x_j)}\right)^{\frac{1}{a}}\frac{\mu(B_{3,j})}{V(x,x_j)}. \end{equation*}
- id `r571`: theorem; steps here: state and prove. For all integers $a \ge 4$ and real numbers $1<q\le 2$ the following holds. Let $(X,\rho,\mu,a)$ be a doubling metric measure space. Let $\Mf$ be a cancellative compatible collection of functions and let $K$ be a two-sided Calder\'on--Zygmund kernel on $(X,\rho,\mu,a)$. Assume that for every bounded measurable function $g$ on $X$ supported on a set of finite measure and all $r>0$ we have \begin{equation} \|T_r g\|_{2} \leq 2^{a^3} \|g\|_2\,. \end{equation} Then for all Borel sets $F$ and $G$ in $X$ and all Borel functions $f:X\to \C$ with $|f|\le \mathbf{1}_F$, we have, with $T$ defined in [another result], \begin{equation} \left|\int_{G} T f \, \mathrm{d}\mu\right| \leq \frac{2^{474a^3}}{(q-1)^6} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}}\, . \end{equation}
- id `r275`: lemma; steps here: state and prove. For all real numbers $x\ge 4$, \begin{equation*} \sum_{n=0}^\infty 2^{-\frac{n}{x}} \le 2^x. \end{equation*}
- id `r947`: lemma; steps here: state and prove. Let $f:X\to\C$ be a bounded measurable function supported on a set of finite measure and assume for some $r>0$ that for every bounded measurable function $g:X\to\C$ supported on a set of finite measure, \begin{equation} \|T_rg\|_{2}\le 2^{a^3} \|g\|_2. \end{equation} Then for all $\alpha>0$, we have \begin{equation} \mu\left(\{x\in X: |T_r f(x)|>\alpha\}\right)\le \frac{2^{a^3 + 19a}}{\alpha} \int |f(y)|\, d\mu(y). \end{equation}
- id `r988`: lemma; steps here: state and prove. Let $0<r$ and $x\in X$. Let $g:X\to\C$ be a bounded measurable function supported on a set of finite measure. Then for all $x'$ with $\rho(x,x')\le r$. \begin{equation*} \left| T_r g(x) - T_r g(x') \right| \le 2^{a^3 + 2a + 2} Mg(x)\, . \end{equation*}
- id `r990`: lemma; steps here: state and prove. Let $f: X \to \C$ be bounded, measurable, supported on a set of finite measure, and let $\alpha > 0$. Then \begin{equation} \mu(\{x\in X : Mf(x) > \alpha\}) \le \frac{2^{2a}}{\alpha} \int |f(y)|\, d\mu(y). \end{equation}
- id `r898`: lemma; steps here: state and prove. Assume `r571` holds. Then, for every bounded measurable function $g : X \to \C$ supported on a set of finite measure we have \begin{equation} \|T_*g\|_2\le 2^{3a^3}\|g\|_2. \end{equation}
- id `r820`: lemma; steps here: state and prove. Given an open set $O\ne X$, there exists a countable family of balls $B_j = B(x_j, r_j)$ such that \begin{equation} B_j \cap B_{j'} = \emptyset \quad \text{ for } j \ne j', \end{equation} and \begin{equation} \bigcup_j B_{3,j} = O, \end{equation} and \begin{equation} B_{7,j} \cap (X \setminus O) \ne \emptyset \quad \text{ for all } j \end{equation} and we have the bounded intersection property that each $x\in O$ is contained in at most $2^{6a}$ of the $B_{3,j}$.
- id `r737`: lemma; steps here: state and prove. Let $f:X\to\C$ be a bounded measurable function supported on a set of finite measure. For all $x\in X$, \begin{equation} T_*f(x) = \sup_{R_1 < R_2} \sup_{x'\in B(x,R_1)} \left|\int_{B(x',R_2)\setminus B(x',R_1)} K(x',y) f(y) \, \mathrm{d}\mu(y) \right| \end{equation}
- id `r621`: lemma; steps here: state and prove. Let $f$ be a bounded measurable function supported on a set of finite measure. Then for $\mu$ almost every $x$, we have $$\lim_{n\to \infty} \frac{1}{\mu(B_n)}\int_{B_n} f(y)\, dy= f(x),$$ where $\{B_n\}_{n\geq 1}$ is a sequence of balls with radii $r_n>0$ such that $x\in B_n$ for each $n\geq 1$ and \begin{equation*} \lim_{n\to \infty} r_n=0 \,. \end{equation*}

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:r108` before `P:r737`
- `S:r138` before `P:r970`
- `S:r233` before `P:r704`
- `S:r275` before `P:r233`
- `S:r275` before `P:r988`
- `S:r322` before `P:r947`
- `S:r621` before `P:r999`
- `S:r674` before `P:r970`
- `S:r683` before `P:r704`
- `S:r704` before `P:r947`
- `S:r737` before `P:r898`
- `S:r820` before `P:r233`
- `S:r820` before `P:r322`
- `S:r820` before `P:r683`
- `S:r820` before `P:r704`
- `S:r820` before `P:r947`
- `S:r820` before `P:r999`
- `S:r898` before `P:r571`
- `S:r939` before `P:r898`
- `S:r947` before `P:r138`
- `S:r970` before `P:r939`
- `S:r988` before `P:r674`
- `S:r988` before `P:r939`
- `S:r990` before `P:r322`
- `S:r990` before `P:r683`
- `S:r990` before `P:r947`
- `S:r990` before `P:r999`
- `S:r999` before `P:r233`
- `S:r999` before `P:r322`
- `S:r999` before `P:r683`
- `S:r999` before `P:r704`
- `S:r999` before `P:r947`
