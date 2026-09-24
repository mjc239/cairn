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

- id `r710`: lemma; steps here: state and prove. We have for every $k\ge 0$ and $\fP'\subset \fP(k)$ \begin{equation} \dens_1(\fP')\le \dens_k'(\fP')\, . \end{equation}
- id `r917`: lemma; steps here: state and prove. We have that $$ \fL_0(k,n) = \dot{\bigcup_{0 \le l < n}} \fL_0(k,n,l)\,, $$ where each $\fL_0(k,n,l)$ is an antichain.
- id `r494`: lemma; steps here: state and prove. If $\fu \sim \fu'$, then $\scI(u) = \scI(u')$ and \begin{equation*} B_{\fu}(\fcc(\fu), 100) \cap B_{\fu'}(\fcc(\fu'), 100) \neq \emptyset\ . \end{equation*}
- id `r424`: lemma; steps here: state and prove. For each $k,n,j$, the collection $\fC_1(k,n,j)$ is convex.
- id `r689`: lemma; steps here: state and prove. We have \begin{equation} \mu(G_2)\le 2^{-2} \mu(G)\, . \end{equation}
- id `r347`: lemma; steps here: state and prove. Let $\mathcal{L}(\fu)$ be as defined in [another result]. We have for each $\fu\in \fU_1(k,n,l)$, \begin{equation} \mu(\bigcup_{I\in \mathcal{L}(\fu)} I) \le D^{1-\kappa Z(n+1)} \mu(\scI(\mathfrak{u})). \end{equation}
- id `r397`: lemma; steps here: state and prove. For each $\fu\in \fU_3(k,n,j)$, the set $\mathfrak{T}_2(\fu)$ satisfies [another result].
- id `r288`: lemma; steps here: state and prove. For each $\fu\in \fU_3(k,n,j)$, the set $\mathfrak{T}_2(\fu)$ satisfies the convexity condition [another result].
- id `r293`: lemma; steps here: state and prove. Each of the sets $\fL_1(k,n,j,l)$ and $\fL_3(k,n,j,l)$ is an antichain.
- id `r941`: lemma; steps here: state and prove. We have \begin{equation} \mu(G_3)\le 2^{-4} \mu(G)\, . \end{equation}
- id `r291`: lemma; steps here: state and prove. Let \begin{equation} \fP_1 =\bigcup_{k\ge 0}\bigcup_{n\ge k} \bigcup_{0\le j\le 2n+3}\fC_5(k,n,j) \end{equation} For all $f:X\to \C$ with $|f|\le \mathbf{1}_F$ we have \begin{equation} \int_{G \setminus G'} \left|\sum_{\fp \in \fP_1} T_{\fp} f \right|\, \mathrm{d}\mu \le \frac{2^{441a^3}}{(q-1)^4} \mu(G)^{1 - \frac{1}{q}} \mu(F)^{\frac{1}{q}}\,. \end{equation}
- id `r133`: lemma; steps here: state and prove. Let $k,n,j\ge 0$. We have for every $x\in X$ \begin{equation} \sum_{\fu\in \fU_1(k,n,j)} \mathbf{1}_{\scI(\fu)}(x) \le 2^{-j} 2^{9a} \sum_{\mathfrak{m}\in \mathfrak{M}(k,n)} \mathbf{1}_{\scI(\mathfrak{m})}(x) \end{equation}
- id `r727`: lemma; steps here: state and prove. It holds for $k\le n$ that \begin{equation} \sum_{\fu \in \fU_3(k,n,j)} \mathbf{1}_{\scI(\fu)} \le (4n+12)2^{n}\,. \end{equation}
- id `r772`: lemma; steps here: state and prove. For all integers $k,n,\lambda\ge 0$, we have \begin{equation} \mu(A(\lambda,k,n)) \le 2^{k+1-\lambda}\mu(G)\,. \end{equation}
- id `r366`: lemma; steps here: state and prove. For each $k,n,j$, the collection $\fC_5(k,n,j)$ is convex.
- id `r587`: proposition; steps here: prove only (it was stated in an earlier section). Let $(\mathcal{D}, c, s)$ be a grid structure and \begin{equation*} (\fP,\scI,\fc,\fcc,\pc,\ps) \end{equation*} a tile structure for this grid structure. Define for $\fp\in \fP$ \begin{equation} E(\fp)=\{x\in \scI(\fp): \tQ(x)\in \fc(\fp) , {\sigma_1}(x)\le \ps(\fp)\le {\sigma_2}(x)\} \end{equation} and \begin{equation} T_{\fp} f(x)= \mathbf{1}_{E(\fp)}(x) \int K_{\ps(\fp)}(x,y) f(y) e(\tQ(x)(y)-\tQ(x)(x))\, d\mu(y). \end{equation} Then there exists a Borel set $G'$ with $2\mu(G') \leq \mu(G)$ such that for all Borel functions $f:X\to \C$ with $|f|\le \mathbf{1}_F$ we have \begin{equation} \int_{G \setminus G'} \left| \sum_{\fp \in \fP} T_{\fp} f (x) \right| \, \mathrm{d}\mu(x) \le \frac{2^{442a^3}}{(q-1)^5} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}}\,. \end{equation}
- id `r170`: lemma; steps here: state and prove. For each $\fu\in \fU_3(k,n,j)$ and each $\fp \in \mathfrak{T}_2(\fu)$ we have \begin{equation} B(\pc(\fp), 8 D^{\ps(\fp)}) \subset \scI(\fu). \end{equation}
- id `r191`: lemma; steps here: state and prove. The following implications hold for all $\fq, \fq' \in \fP$: \begin{equation} \fq \le \fq' \ \text{and} \ \lambda \ge 1.1 \implies \lambda \fq \lesssim \lambda \fq'\,, \end{equation} \begin{equation} 10\fq \lesssim \fq' \ \text{and} \ \scI(\fq) \ne \scI(\fq') \implies 100 \fq \lesssim 100 \fq'\,, \end{equation} \begin{equation} 2\fq \lesssim \fq' \ \text{and} \ \scI(\fq) \ne \scI(\fq') \implies 4 \fq \lesssim 500 \fq'\,. \end{equation}
- id `r795`: lemma; steps here: state and prove. We have \begin{equation} \sum_{\mathfrak{m} \in \mathfrak{M}(k,n)} \mu(\scI(\mathfrak{m}))\le 2^{n+k+3}\mu(G). \end{equation}
- id `r875`: lemma; steps here: state and prove. We have that \begin{align} &\quad \fP_2 \cap \fP_{G \setminus G'}\\ &= \bigcup_{k \ge 0} \bigcup_{n \ge k} \fL_0(k,n) \cap \fP_{G \setminus G'} \\ &\quad\cup \bigcup_{k \ge 0} \bigcup_{n \ge k}\bigcup_{0 \le j \le 2n+3} \fL_2(k,n,j) \cap \fP_{G \setminus G'}\\ &\quad\cup \bigcup_{k \ge 0} \bigcup_{n \ge k}\bigcup_{0 \le j \le 2n+3} \bigcup_{0 \le l \le Z(n+1)} \fL_1(k,n,j,l) \cap \fP_{G \setminus G'}\\ &\quad\cup \bigcup_{k \ge 0} \bigcup_{n \ge k}\bigcup_{0 \le j \le 2n+3} \bigcup_{0 \le l \le Z(n+1)} \fL_3(k,n,j,l)\cap \fP_{G \setminus G'}\,. \end{align}
- id `r233`: lemma; steps here: state and prove. We have \begin{equation} \fC_6(k,n,j)=\bigcup_{\fu\in \fU_3(k,n,j)}\mathfrak{T}_2(\fu)\, . \end{equation}
- id `r997`: lemma; steps here: state and prove. If $n\fp \lesssim m\fp'$ and $n' \ge n$ and $m \ge m'$ then $n'\fp \lesssim m'\fp'$.
- id `r253`: lemma; steps here: state and prove. For each $k$, the collection $\fP(k)$ is convex.
- id `r139`: lemma; steps here: state and prove. We have \begin{equation} \mu(G_1)\le 2^{-5}\mu(G)\, . \end{equation}
- id `r962`: lemma; steps here: state and prove. Each of the sets $\fL_2(k,n,j)$ is an antichain.
- id `r182`: lemma; steps here: state and prove. For each $x\in A(\lambda,k,n)$, there is a dyadic cube $I$ that contains $x$ and is a subset of $A(\lambda,k,n)$.
- id `r816`: lemma; steps here: state and prove. For each $k,n$, the collection $\fC(k,n)$ is convex.
- id `r949`: lemma; steps here: state and prove. If $\fp, \fp' \in {\mathfrak{M}}(k,n)$ and \begin{equation} {E_1}(\fp)\cap {E_1}(\fp')\neq \emptyset, \end{equation} then $\fp=\fp'$.
- id `r653`: lemma; steps here: state and prove. Let \begin{equation} \fP_2 =\fP\setminus \fP_1\,. \end{equation} For all $f:X\to \C$ with $|f|\le \mathbf{1}_F$ we have \begin{equation} \int_{G \setminus G'} \left|\sum_{\fp \in \fP_2} T_{\fp} f\right| \, \mathrm{d}\mu \le \frac{2^{120a^3}}{(q-1)^5} \mu(G)^{1 - \frac{1}{q}} \mu(F)^{\frac{1}{q}}\,. \end{equation}
- id `r799`: lemma; steps here: state and prove. For each $k,n,j$, the relation $\sim$ on $\fU_2(k,n,j)$ is an equivalence relation.
- id `r500`: lemma; steps here: state and prove. For each $k,n,j$, the collection $\fC_4(k,n,j)$ is convex.
- id `r957`: lemma; steps here: state and prove. For each $k,n,j$, the collection $\fC_2(k,n,j)$ is convex.
- id `r822`: lemma; steps here: state and prove. Let $n, m \ge 1$ and $k > 0$. If $\fp, \fp' \in \fP$ with $\scI(\fp) \ne \scI(\fp')$ and \begin{equation} n \fp \lesssim k \fp' \end{equation} then \begin{equation} (n + 2^{-95 a} m) \fp \lesssim m\fp'\,. \end{equation}
- id `r637`: lemma; steps here: state and prove. For each $k,n,j$, the collection $\fC_3(k,n,j)$ is convex.
- id `r382`: lemma; steps here: state and prove. For each $\fu,\fu'\in \fU_3(k,n,j)$ with $\fu\neq \fu'$ and each $\fp \in \fT_2(\fu)$ with $\scI(\fp)\subset \scI(\fu')$ we have \begin{equation} d_{\fp}(\fcc(\fp), \fcc(\fu')) > 2^{Z(n+1)}\,. \end{equation}
- id `r634`: lemma; steps here: state and prove. We have \begin{equation} \mu(G')\le 2^{-1}\mu(G)\, . \end{equation}
- id `r931`: lemma; steps here: state and prove. For each set $\mathfrak{A} \subset \mathfrak{C}(k,n)$, we have $$ \dens_1(\mathfrak{A}) \le 2^{4a}2^{-n+1}\,. $$
- id `r341`: lemma; steps here: state and prove. For each $k\ge 0$, the union of all dyadic cubes in $\mathcal{C}(G,k)$ has measure at most $2^{k+1} \mu(G)$ .

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:r133` before `P:r941`
- `S:r139` before `P:r634`
- `S:r170` before `P:r291`
- `S:r182` before `P:r772`
- `S:r191` before `P:r170`
- `S:r191` before `P:r288`
- `S:r191` before `P:r382`
- `S:r191` before `P:r397`
- `S:r191` before `P:r424`
- `S:r191` before `P:r494`
- `S:r191` before `P:r637`
- `S:r191` before `P:r727`
- `S:r191` before `P:r799`
- `S:r191` before `P:r816`
- `S:r191` before `P:r962`
- `S:r233` before `P:r291`
- `S:r253` before `P:r816`
- `S:r288` before `P:r291`
- `S:r291` before `P:r587`
- `S:r293` before `P:r653`
- `S:r341` before `P:r772`
- `S:r347` before `P:r941`
- `S:r366` before `P:r288`
- `S:r382` before `P:r291`
- `S:r397` before `P:r291`
- `S:r424` before `P:r957`
- `S:r494` before `P:r170`
- `S:r494` before `P:r291`
- `S:r494` before `P:r397`
- `S:r494` before `P:r799`
- `S:r500` before `P:r366`
- `S:r634` before `P:r587`
- `S:r637` before `P:r500`
- `S:r653` before `P:r587`
- `S:r689` before `P:r634`
- `S:r710` before `P:r931`
- `S:r727` before `P:r291`
- `S:r772` before `P:r689`
- `S:r772` before `P:r795`
- `S:r795` before `P:r941`
- `S:r799` before `P:r170`
- `S:r799` before `P:r233`
- `S:r799` before `P:r291`
- `S:r799` before `P:r382`
- `S:r799` before `P:r397`
- `S:r799` before `P:r727`
- `S:r816` before `P:r424`
- `S:r822` before `P:r191`
- `S:r822` before `P:r962`
- `S:r917` before `P:r653`
- `S:r931` before `P:r291`
- `S:r931` before `P:r653`
- `S:r941` before `P:r634`
- `S:r949` before `P:r772`
- `S:r957` before `P:r637`
- `S:r962` before `P:r653`
- `S:r997` before `P:r170`
- `S:r997` before `P:r291`
- `S:r997` before `P:r494`
