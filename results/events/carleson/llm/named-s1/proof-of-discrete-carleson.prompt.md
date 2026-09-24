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

- id `C-convex`: lemma (C convex); steps here: state and prove. For each $k,n$, the collection $\fC(k,n)$ is convex.
- id `C6-forest`: lemma (C6 forest); steps here: state and prove. We have \begin{equation} \fC_6(k,n,j)=\bigcup_{\fu\in \fU_3(k,n,j)}\mathfrak{T}_2(\fu)\, . \end{equation}
- id `boundary-exception`: lemma (boundary exception); steps here: state and prove. Let $\mathcal{L}(\fu)$ be as defined in \eqref{eq-L-def}. We have for each $\fu\in \fU_1(k,n,l)$, \begin{equation} \mu(\bigcup_{I\in \mathcal{L}(\fu)} I) \le D^{1-\kappa Z(n+1)} \mu(\scI(\mathfrak{u})). \end{equation}
- id `discrete-Carleson`: proposition (discrete Carleson); steps here: prove only (it was stated in an earlier section). Let $(\mathcal{D}, c, s)$ be a grid structure and \begin{equation*} (\fP,\scI,\fc,\fcc,\pc,\ps) \end{equation*} a tile structure for this grid structure. Define for $\fp\in \fP$ \begin{equation} E(\fp)=\{x\in \scI(\fp): \tQ(x)\in \fc(\fp) , {\sigma_1}(x)\le \ps(\fp)\le {\sigma_2}(x)\} \end{equation} and \begin{equation} T_{\fp} f(x)= \mathbf{1}_{E(\fp)}(x) \int K_{\ps(\fp)}(x,y) f(y) e(\tQ(x)(y)-\tQ(x)(x))\, d\mu(y). \end{equation} Then there exists a Borel set $G'$ with $2\mu(G') \leq \mu(G)$ such that for all Borel functions $f:X\to \C$ with $|f|\le \mathbf{1}_F$ we have \begin{equation} \int_{G \setminus G'} \left| \sum_{\fp \in \fP} T_{\fp} f (x) \right| \, \mathrm{d}\mu(x) \le \frac{2^{442a^3}}{(q-1)^5} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}}\,. \end{equation}
- id `forest-convex`: lemma (forest convex); steps here: state and prove. For each $\fu\in \fU_3(k,n,j)$, the set $\mathfrak{T}_2(\fu)$ satisfies the convexity condition \eqref{forest2}.
- id `pairwise-disjoint`: lemma (pairwise disjoint); steps here: state and prove. If $\fp, \fp' \in {\mathfrak{M}}(k,n)$ and \begin{equation} {E_1}(\fp)\cap {E_1}(\fp')\neq \emptyset, \end{equation} then $\fp=\fp'$.
- id `C1-convex`: lemma (C1 convex); steps here: state and prove. For each $k,n,j$, the collection $\fC_1(k,n,j)$ is convex.
- id `dense-cover`: lemma (dense cover); steps here: state and prove. For each $k\ge 0$, the union of all dyadic cubes in $\mathcal{C}(G,k)$ has measure at most $2^{k+1} \mu(G)$ .
- id `C3-convex`: lemma (C3 convex); steps here: state and prove. For each $k,n,j$, the collection $\fC_3(k,n,j)$ is convex.
- id `first-exception`: lemma (first exception); steps here: state and prove. We have \begin{equation} \mu(G_1)\le 2^{-5}\mu(G)\, . \end{equation}
- id `forest-complement`: lemma (forest complement); steps here: state and prove. Let \begin{equation} \fP_2 =\fP\setminus \fP_1\,. \end{equation} For all $f:X\to \C$ with $|f|\le \mathbf{1}_F$ we have \begin{equation} \int_{G \setminus G'} \left|\sum_{\fp \in \fP_2} T_{\fp} f\right| \, \mathrm{d}\mu \le \frac{2^{120a^3}}{(q-1)^5} \mu(G)^{1 - \frac{1}{q}} \mu(F)^{\frac{1}{q}}\,. \end{equation}
- id `L2-antichain`: lemma (L2 antichain); steps here: state and prove. Each of the sets $\fL_2(k,n,j)$ is an antichain.
- id `top-tiles`: lemma (top tiles); steps here: state and prove. We have \begin{equation} \sum_{\mathfrak{m} \in \mathfrak{M}(k,n)} \mu(\scI(\mathfrak{m}))\le 2^{n+k+3}\mu(G). \end{equation}
- id `John-Nirenberg`: lemma (John Nirenberg); steps here: state and prove. For all integers $k,n,\lambda\ge 0$, we have \begin{equation} \mu(A(\lambda,k,n)) \le 2^{k+1-\lambda}\mu(G)\,. \end{equation}
- id `relation-geometry`: lemma (relation geometry); steps here: state and prove. If $\fu \sim \fu'$, then $\scI(u) = \scI(u')$ and \begin{equation*} B_{\fu}(\fcc(\fu), 100) \cap B_{\fu'}(\fcc(\fu'), 100) \neq \emptyset\ . \end{equation*}
- id `forest-inner`: lemma (forest inner); steps here: state and prove. For each $\fu\in \fU_3(k,n,j)$ and each $\fp \in \mathfrak{T}_2(\fu)$ we have \begin{equation} B(\pc(\fp), 8 D^{\ps(\fp)}) \subset \scI(\fu). \end{equation}
- id `forest-geometry`: lemma (forest geometry); steps here: state and prove. For each $\fu\in \fU_3(k,n,j)$, the set $\mathfrak{T}_2(\fu)$ satisfies \eqref{forest1}.
- id `second-exception`: lemma (second exception); steps here: state and prove. We have \begin{equation} \mu(G_2)\le 2^{-2} \mu(G)\, . \end{equation}
- id `C-dens1`: lemma (C dens1); steps here: state and prove. For each set $\mathfrak{A} \subset \mathfrak{C}(k,n)$, we have $$ \dens_1(\mathfrak{A}) \le 2^{4a}2^{-n+1}\,. $$
- id `C2-convex`: lemma (C2 convex); steps here: state and prove. For each $k,n,j$, the collection $\fC_2(k,n,j)$ is convex.
- id `C4-convex`: lemma (C4 convex); steps here: state and prove. For each $k,n,j$, the collection $\fC_4(k,n,j)$ is convex.
- id `tree-count`: lemma (tree count); steps here: state and prove. Let $k,n,j\ge 0$. We have for every $x\in X$ \begin{equation} \sum_{\fu\in \fU_1(k,n,j)} \mathbf{1}_{\scI(\fu)}(x) \le 2^{-j} 2^{9a} \sum_{\mathfrak{m}\in \mathfrak{M}(k,n)} \mathbf{1}_{\scI(\mathfrak{m})}(x) \end{equation}
- id `forest-separation`: lemma (forest separation); steps here: state and prove. For each $\fu,\fu'\in \fU_3(k,n,j)$ with $\fu\neq \fu'$ and each $\fp \in \fT_2(\fu)$ with $\scI(\fp)\subset \scI(\fu')$ we have \begin{equation} d_{\fp}(\fcc(\fp), \fcc(\fu')) > 2^{Z(n+1)}\,. \end{equation}
- id `P-convex`: lemma (P convex); steps here: state and prove. For each $k$, the collection $\fP(k)$ is convex.
- id `wiggle-order-2`: lemma (wiggle order 2); steps here: state and prove. Let $n, m \ge 1$ and $k > 0$. If $\fp, \fp' \in \fP$ with $\scI(\fp) \ne \scI(\fp')$ and \begin{equation} n \fp \lesssim k \fp' \end{equation} then \begin{equation} (n + 2^{-95 a} m) \fp \lesssim m\fp'\,. \end{equation}
- id `wiggle-order-1`: lemma (wiggle order 1); steps here: state and prove. If $n\fp \lesssim m\fp'$ and $n' \ge n$ and $m \ge m'$ then $n'\fp \lesssim m'\fp'$.
- id `forest-stacking`: lemma (forest stacking); steps here: state and prove. It holds for $k\le n$ that \begin{equation} \sum_{\fu \in \fU_3(k,n,j)} \mathbf{1}_{\scI(\fu)} \le (4n+12)2^{n}\,. \end{equation}
- id `dyadic-union`: lemma (dyadic union); steps here: state and prove. For each $x\in A(\lambda,k,n)$, there is a dyadic cube $I$ that contains $x$ and is a subset of $A(\lambda,k,n)$.
- id `wiggle-order-3`: lemma (wiggle order 3); steps here: state and prove. The following implications hold for all $\fq, \fq' \in \fP$: \begin{equation} \fq \le \fq' \ \text{and} \ \lambda \ge 1.1 \implies \lambda \fq \lesssim \lambda \fq'\,, \end{equation} \begin{equation} 10\fq \lesssim \fq' \ \text{and} \ \scI(\fq) \ne \scI(\fq') \implies 100 \fq \lesssim 100 \fq'\,, \end{equation} \begin{equation} 2\fq \lesssim \fq' \ \text{and} \ \scI(\fq) \ne \scI(\fq') \implies 4 \fq \lesssim 500 \fq'\,. \end{equation}
- id `L0-antichain`: lemma (L0 antichain); steps here: state and prove. We have that $$ \fL_0(k,n) = \dot{\bigcup_{0 \le l < n}} \fL_0(k,n,l)\,, $$ where each $\fL_0(k,n,l)$ is an antichain.
- id `C5-convex`: lemma (C5 convex); steps here: state and prove. For each $k,n,j$, the collection $\fC_5(k,n,j)$ is convex.
- id `equivalence-relation`: lemma (equivalence relation); steps here: state and prove. For each $k,n,j$, the relation $\sim$ on $\fU_2(k,n,j)$ is an equivalence relation.
- id `third-exception`: lemma (third exception); steps here: state and prove. We have \begin{equation} \mu(G_3)\le 2^{-4} \mu(G)\, . \end{equation}
- id `dens-compare`: lemma (dens compare); steps here: state and prove. We have for every $k\ge 0$ and $\fP'\subset \fP(k)$ \begin{equation} \dens_1(\fP')\le \dens_k'(\fP')\, . \end{equation}
- id `exceptional-set`: lemma (exceptional set); steps here: state and prove. We have \begin{equation} \mu(G')\le 2^{-1}\mu(G)\, . \end{equation}
- id `antichain-decomposition`: lemma (antichain decomposition); steps here: state and prove. We have that \begin{align} &\quad \fP_2 \cap \fP_{G \setminus G'}\\ &= \bigcup_{k \ge 0} \bigcup_{n \ge k} \fL_0(k,n) \cap \fP_{G \setminus G'} \\ &\quad\cup \bigcup_{k \ge 0} \bigcup_{n \ge k}\bigcup_{0 \le j \le 2n+3} \fL_2(k,n,j) \cap \fP_{G \setminus G'}\\ &\quad\cup \bigcup_{k \ge 0} \bigcup_{n \ge k}\bigcup_{0 \le j \le 2n+3} \bigcup_{0 \le l \le Z(n+1)} \fL_1(k,n,j,l) \cap \fP_{G \setminus G'}\\ &\quad\cup \bigcup_{k \ge 0} \bigcup_{n \ge k}\bigcup_{0 \le j \le 2n+3} \bigcup_{0 \le l \le Z(n+1)} \fL_3(k,n,j,l)\cap \fP_{G \setminus G'}\,. \end{align}
- id `L1-L3-antichain`: lemma (L1 L3 antichain); steps here: state and prove. Each of the sets $\fL_1(k,n,j,l)$ and $\fL_3(k,n,j,l)$ is an antichain.
- id `forest-union`: lemma (forest union); steps here: state and prove. Let \begin{equation} \fP_1 =\bigcup_{k\ge 0}\bigcup_{n\ge k} \bigcup_{0\le j\le 2n+3}\fC_5(k,n,j) \end{equation} For all $f:X\to \C$ with $|f|\le \mathbf{1}_F$ we have \begin{equation} \int_{G \setminus G'} \left|\sum_{\fp \in \fP_1} T_{\fp} f \right|\, \mathrm{d}\mu \le \frac{2^{441a^3}}{(q-1)^4} \mu(G)^{1 - \frac{1}{q}} \mu(F)^{\frac{1}{q}}\,. \end{equation}

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:C-convex` before `P:C1-convex`
- `S:C-dens1` before `P:forest-complement`
- `S:C-dens1` before `P:forest-union`
- `S:C1-convex` before `P:C2-convex`
- `S:C2-convex` before `P:C3-convex`
- `S:C3-convex` before `P:C4-convex`
- `S:C4-convex` before `P:C5-convex`
- `S:C5-convex` before `P:forest-convex`
- `S:C6-forest` before `P:forest-union`
- `S:John-Nirenberg` before `P:second-exception`
- `S:John-Nirenberg` before `P:top-tiles`
- `S:L0-antichain` before `P:forest-complement`
- `S:L1-L3-antichain` before `P:forest-complement`
- `S:L2-antichain` before `P:forest-complement`
- `S:P-convex` before `P:C-convex`
- `S:boundary-exception` before `P:third-exception`
- `S:dens-compare` before `P:C-dens1`
- `S:dense-cover` before `P:John-Nirenberg`
- `S:dyadic-union` before `P:John-Nirenberg`
- `S:equivalence-relation` before `P:C6-forest`
- `S:equivalence-relation` before `P:forest-geometry`
- `S:equivalence-relation` before `P:forest-inner`
- `S:equivalence-relation` before `P:forest-separation`
- `S:equivalence-relation` before `P:forest-stacking`
- `S:equivalence-relation` before `P:forest-union`
- `S:exceptional-set` before `P:discrete-Carleson`
- `S:first-exception` before `P:exceptional-set`
- `S:forest-complement` before `P:discrete-Carleson`
- `S:forest-convex` before `P:forest-union`
- `S:forest-geometry` before `P:forest-union`
- `S:forest-inner` before `P:forest-union`
- `S:forest-separation` before `P:forest-union`
- `S:forest-stacking` before `P:forest-union`
- `S:forest-union` before `P:discrete-Carleson`
- `S:pairwise-disjoint` before `P:John-Nirenberg`
- `S:relation-geometry` before `P:equivalence-relation`
- `S:relation-geometry` before `P:forest-geometry`
- `S:relation-geometry` before `P:forest-inner`
- `S:relation-geometry` before `P:forest-union`
- `S:second-exception` before `P:exceptional-set`
- `S:third-exception` before `P:exceptional-set`
- `S:top-tiles` before `P:third-exception`
- `S:tree-count` before `P:third-exception`
- `S:wiggle-order-1` before `P:forest-inner`
- `S:wiggle-order-1` before `P:forest-union`
- `S:wiggle-order-1` before `P:relation-geometry`
- `S:wiggle-order-2` before `P:L2-antichain`
- `S:wiggle-order-2` before `P:wiggle-order-3`
- `S:wiggle-order-3` before `P:C-convex`
- `S:wiggle-order-3` before `P:C1-convex`
- `S:wiggle-order-3` before `P:C3-convex`
- `S:wiggle-order-3` before `P:L2-antichain`
- `S:wiggle-order-3` before `P:equivalence-relation`
- `S:wiggle-order-3` before `P:forest-convex`
- `S:wiggle-order-3` before `P:forest-geometry`
- `S:wiggle-order-3` before `P:forest-inner`
- `S:wiggle-order-3` before `P:forest-separation`
- `S:wiggle-order-3` before `P:forest-stacking`
- `S:wiggle-order-3` before `P:relation-geometry`
