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

- id `antichain-tile-count`: lemma (antichain tile count); steps here: state and prove. Set $p:=4a^4$. For every $\mfa\in\Mf$ and every antichain $\mathfrak{A}$ we have \begin{equation} \Big\|\sum_{\fp\in\mathfrak{A}}(1+d_{\fp}(\fcc(\fp), \mfa))^{-1/(2a^2+a^3)}\mathbf{1}_{E(\fp)}\mathbf{1}_G\Big\|_{p} \end{equation} \begin{equation} \le 2^{5a}\dens_1(\mathfrak{A})^{\frac 1p}\mu\left(\cup_{\fp\in\mathfrak{A}}I_{\fp}\right)^{\frac 1p}\, . \end{equation}
- id `tile-reach`: lemma (tile reach); steps here: state and prove. Let $\mfa\in \Mf$ and $N\ge0$ be an integer. Let $\fp, \fp'\in \fP$ with \begin{equation} d_{\fp}(\fcc(\fp), \mfa))\le 2^N\, \end{equation} \begin{equation} d_{\fp'}(\fcc(\fp'), \mfa))\le 2^N\, . \end{equation} Assume $\scI(\fp)\subset \scI(\fp')$ and $\ps(\fp)<\ps(\fp')$. Then \begin{equation}2^{N+2}\fp\lesssim 2^{N+2} \fp'\, . \end{equation}
- id `dens2-antichain`: lemma (dens2 antichain); steps here: state and prove. We have that \begin{equation} \left|\int \overline{g(x)} \sum_{\fp \in \mathfrak{A}} T_{\fp} f(x)\, d\mu(x)\right|\le 2^{103a^3}({q}-1)^{-1} \dens_2(\mathfrak{A})^{\frac 1{\tilde{q}}-\frac 12} \|f\|_2\|g\|_2\, . \end{equation}
- id `local-antichain-density`: lemma (local antichain density); steps here: state and prove. Let $\mfa\in\Mf$ and {$N$} be an integer. Let $\fp_{\mfa}$ be a tile with $\mfa\in B_{\fp_{\mfa}}(\fcc(\fp_{\mfa}), 2^{N+1})$. Then we have \begin{equation} \sum_{\fp\in\mathfrak{A}_{\mfa,N}: \ps(\fp_{\mfa})<\ps(\fp)}\mu(E(\fp)\cap G \cap \scI(\fp_{\mfa})) \le \mu (E_2(2^{N+3},\fp_{\mfa})) \, . \end{equation}
- id `stack-density`: lemma (stack density); steps here: state and prove. Let $\mfa \in \Mf$, $N\ge 0$ and $L\in \mathcal{D}$. Then \begin{equation} \sum_{\fp\in\mathfrak{A}_{\mfa,N}:\scI(\fp)=L}\mu(E(\fp)\cap G)\le 2^{a(N+5)}\dens_1(\mathfrak{A})\mu(L)\, . \end{equation}
- id `maximal-bound-antichain`: lemma (maximal bound antichain); steps here: state and prove. Let $x\in X$. Then \begin{equation} | \sum_{\fp \in \mathfrak{A}}T_{\fp} f(x)|\le 2^{102 a^3} M_{\mathcal{B}} f (x) \, . \end{equation}
- id `dens1-antichain`: lemma (dens1 antichain); steps here: state and prove. Set $p:=4a^4$. We have \begin{equation} \left|\int \overline{g(x)} \sum_{\fp \in \mathfrak{A}} T_{\fp} f(x)\, d\mu(x)\right|\le 2^{117a^3}\dens_1(\mathfrak{A})^{\frac 1{2p}} \|f\|_2\|g\|_2\,. \end{equation}
- id `tile-disjointness`: lemma (tile disjointness); steps here: state and prove. Let $\fp,\fp'\in \mathfrak{A}$. If there exists an $x\in X$ with $x\in E(\fp)\cap E(\fp')$, then $\fp= \fp'$.
- id `antichain-operator`: proposition (antichain operator); steps here: prove only (it was stated in an earlier section). For any antichain $\mathfrak{A} $ and for all $f:X\to \C$ with $|f|\le \mathbf{1}_F$ and all $g:X\to\C$ with $|g| \le \mathbf{1}_G$ \begin{equation} |\int \overline{g(x)} \sum_{\fp \in \mathfrak{A}} T_{\fp} f(x)\, d\mu(x)| \end{equation} \begin{equation} \le \frac{2^{117a^3}}{q-1} \dens_1(\mathfrak{A})^{\frac {q-1}{8a^4}}\dens_2(\mathfrak{A})^{\frac 1{q}-\frac 12} \|f\|_2 \|g\|_2\, . \end{equation}
- id `tile-range-support`: lemma (tile range support); steps here: state and prove. For each $\fp\in \fP$, and each $y\in X$, we have that \begin{equation} T_{\fp}^* g(y)\neq 0 \end{equation} implies \begin{equation} y\in B(\pc(\fp),5D^{\ps(\fp)})\, . \end{equation}
- id `correlation-kernel-bound`: lemma (correlation kernel bound); steps here: state and prove. Let $-S\le s_1\le s_2\le S$ and let $x_1,x_2\in X$. Define \begin{equation} \varphi(y) := \overline{K_{s_1}(x_1, y)} K_{s_2}(x_2, y) \, . \end{equation} If $\varphi(y)\neq 0$, then \begin{equation} y\in B(x_1, D^{s_1})\, . \end{equation} Moreover, we have with $\tau = 1/a$ \begin{equation} \|\varphi\|_{C^\tau(B(x_1, 2 D^{s_1}))}\le \frac{2^{231 a^3}}{\mu(B(x_1, D^{s_1}))\mu(B(x_2, D^{s_2}))} \, . \end{equation}
- id `tile-uncertainty`: lemma; steps here: state and prove. Let $\fp_1, \fp_2\in \fP$ with $B(\pc(\fp_1),5D^{\ps(\fp_1)}) \cap B(\pc(\fp_2),5D^{\ps(\fp_2)}) \ne \emptyset$ and $\ps({\fp_1})\leq \ps({\fp_2})$. For each $x_1\in E(\fp_1)$ and $x_2\in E(\fp_2)$ we have \begin{equation} 1+d_{\fp_1}(\fcc(\fp_1), \fcc(\fp_2))\le 2^{8a}(1 + d_{B(x_1, D^{\ps(\fp_1)})}(\tQ(x_1),\tQ(x_2)))\, . \end{equation}
- id `global-antichain-density`: lemma (global antichain density); steps here: state and prove. Let $\mfa\in Q(X)$ and let $N\ge 0$ be an integer. Then we have \begin{equation} \sum_{\fp\in\mathfrak{A}_{\mfa,N}}\mu(E(\fp)\cap G) \le 2^{101a^3+Na}\dens_1(\mathfrak{A})\mu\left(\cup_{\fp\in\mathfrak{A}}I_{\fp}\right)\, . \end{equation}
- id `tile-correlation`: lemma (tile correlation); steps here: state and prove. Let $\fp, \fp'\in \fP$ with $\ps({\fp'})\leq \ps({\fp})$. Then \begin{equation} \left|\int T^*_{\fp'}g\overline{T^*_{\fp}g}\right| \end{equation} \begin{equation} \le 2^{232a^3}\frac{(1+d_{\fp'}(\fcc(\fp'), \fcc(\fp))^{-1/(2a^2+a^3)}}{\mu(\scI(\fp))}\int_{E(\fp')}|g|\int_{E(\fp)}|g|\,. \end{equation} Moreover, the term \eqref{eq-basic-TT*-est} vanishes unless \begin{equation} \scI(\fp') \subset B(\pc(\fp), 14D^{\ps(\fp)})\, . \end{equation}

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:antichain-tile-count` before `P:dens1-antichain`
- `S:correlation-kernel-bound` before `P:tile-correlation`
- `S:dens1-antichain` before `P:antichain-operator`
- `S:dens2-antichain` before `P:antichain-operator`
- `S:global-antichain-density` before `P:antichain-tile-count`
- `S:local-antichain-density` before `P:global-antichain-density`
- `S:maximal-bound-antichain` before `P:dens2-antichain`
- `S:stack-density` before `P:global-antichain-density`
- `S:tile-correlation` before `P:dens1-antichain`
- `S:tile-disjointness` before `P:antichain-tile-count`
- `S:tile-disjointness` before `P:dens1-antichain`
- `S:tile-disjointness` before `P:local-antichain-density`
- `S:tile-disjointness` before `P:maximal-bound-antichain`
- `S:tile-range-support` before `P:tile-correlation`
- `S:tile-reach` before `P:global-antichain-density`
- `S:tile-reach` before `P:local-antichain-density`
- `S:tile-uncertainty` before `P:tile-correlation`
