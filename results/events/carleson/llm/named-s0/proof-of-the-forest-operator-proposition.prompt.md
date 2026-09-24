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

- id `convex-scales`: lemma (convex scales); steps here: state and prove. For each $\fu \in \fU$, we have $$ \sigma(\fu, x) = \mathbb{Z} \cap [\underline{\sigma} (\fu, x), \overline{\sigma} (\fu, x)]\,. $$
- id `scales-impacting-interval`: lemma (scales impacting interval); steps here: state and prove. Let $\fC = \fT(\fu_1)$ or $\fC = \fT(\fu_2) \cap \mathfrak{S}$. Then for each $J \in \mathcal{J}'$ and $\fp \in \fC$ with $B(\scI(\fp)) \cap B'(J) \neq \emptyset$, we have $\ps(\fp) \ge s(J)$.
- id `Holder-correlation-tree`: lemma (Holder correlation tree); steps here: state and prove. We have for all $J \in \mathcal{J}'$ that \begin{equation} \|h_J\|_{C^{\tau}(B(c(J), 16D^{s(J)}))} \le 2^{485a^3} \prod_{j = 1,2} (\inf_{B(c(J), \frac{1}{8}D^{s(J)})} |T_{\fT(\fu_j)}^* g_j| + \inf_J M_{\mathcal{B}, 1} |g_j|)\,. \end{equation}
- id `nontangential-operator-bound`: lemma (nontangential operator bound); steps here: state and prove. For all bounded $f$ with bounded support and all $\mfa \in \Mf$ $$ \|T_{\mathcal{N}}^{\mfa} f\|_2 \le 2^{102a^3} \|f\|_2\,. $$
- id `lower-oscillation-bound`: lemma (lower oscillation bound); steps here: state and prove. For all $J \in \mathcal{J}'$, we have that $$ d_{B(J)}(\fcc(\fu_1), \fcc(\fu_2)) \ge 2^{-201a^3} 2^{Zn/2}\,. $$
- id `correlation-separated-trees`: lemma (correlation separated trees); steps here: state and prove. For any $\fu_1 \ne \fu_2 \in \fU$ and all bounded $g_1, g_2$ with bounded support, we have \begin{equation} \left| \int_X \sum_{\fp_1 \in \fT(\fu_1)} \sum_{\fp_2 \in \fT(\fu_2)} T^*_{\fp_1}g_1 \overline{T^*_{\fp_2}g_2 }\,\mathrm{d}\mu \right| \end{equation} \begin{equation} \le 2^{512a^3-4n} \prod_{j =1}^2 \| S_{2, \fu_j} g_j\|_{L^2(\scI(\fu_1) \cap \scI(\fu_2))}\,. \end{equation}
- id `adjoint-tile-support`: lemma (adjoint tile support); steps here: state and prove. For each $\fp \in \fP$, we have $$ T_{\fp}^* g = \mathbf{1}_{B(\pc(\fp), 5D^{\ps(\fp)})} T_{\fp}^* \mathbf{1}_{\scI(\fp)} g\,. $$ For each $\fu \in \fU$ and each $\fp \in \fT(\fu)$, we have $$ T_{\fp}^* g = \mathbf{1}_{\scI(\fu)} T_{\fp}^* \mathbf{1}_{\scI(\fu)} g\,. $$
- id `first-tree-pointwise`: lemma (first tree pointwise); steps here: state and prove. For all $\fu \in \fU$, all $L \in \mathcal{L}(\fT(\fu))$, all $x, x' \in L$ and all bounded $f$ with bounded support, we have $$ \eqref{eq-term-A} \le 10 \cdot 2^{104a^3} M_{\mathcal{B}, 1}P_{\mathcal{J}(\fT(\fu))}|f|(x')\,. $$
- id `correlation-distant-tree-parts`: lemma (correlation distant tree parts); steps here: state and prove. We have for all $\fu_1 \ne \fu_2 \in \fU$ with $\scI(\fu_1) \subset \scI(\fu_2)$ and all bounded $g_1, g_2$ with bounded support \begin{equation} \left| \int_X \sum_{\fp_1 \in \fT(\fu_1)} \sum_{\fp_2 \in \fT(\fu_2) \cap \mathfrak{S}} T^*_{\fp_1}g_1 \overline{T^*_{\fp_2}g_2 }\,\mathrm{d}\mu \right| \end{equation} \begin{equation} \le 2^{511a^3} 2^{-Zn/(4a^2 + 2a^3)} \prod_{j =1}^2 \| S_{2, \fu_j} g_j\|_{L^2(\scI(\fu_1))}\,. \end{equation}
- id `local-dens2-tree-bound`: lemma (local dens2 tree bound); steps here: state and prove. Let $\fu \in \fU$ and $J \in \mathcal{J}(\fT(\fu))$. Then $$ \mu(F \cap J) \le 2^{201a^3} \dens_2(\fT(\fu)) \mu(J)\,. $$
- id `forest-operator`: proposition (forest operator); steps here: prove only (it was stated in an earlier section). For any $n\ge 0$ and any $n$-forest $(\fU,\fT)$ we have for all $f,g: X \to \mathbb{C}$ with $|f| \le \mathbf{1}_F$ and $|g| \le \mathbf{1}_G$ $$ | \int \overline{g(x)} \sum_{\fu\in \fU} \sum_{\fp\in \fT(\fu)} T_{\fp} f(x) \, \mathrm{d}\mu(x)| $$ $$ \le 2^{440a^3}2^{-\frac{q-1}{q} n} \dens_2\left(\bigcup_{\fu\in \fU}\fT(\fu)\right)^{\frac{1}{q}-\frac{1}{2}} \|f\|_2 \|g\|_2 \,. $$
- id `densities-tree-bound`: lemma (densities tree bound); steps here: state and prove. Let $\fu \in \fU$. Then for all bounded $f$ with bounded support and bounded $g$ supported on $G$ we have \begin{equation} \left|\int_X \bar g \sum_{\fp \in \fT(\fu)} T_{\fp }f \, \mathrm{d}\mu \right| \le 2^{181a^3} \dens_1(\fT(\fu))^{1/2} \|f\|_2\|g\|_2\,. \end{equation} If additionally $\text{support}(f) \subseteq F$, then we have \begin{equation} \left| \int_X \bar g \sum_{\fp \in \fT(\fu)} T_{\fp }f\, \mathrm{d}\mu \right| \le 2^{282a^3} \dens_1(\fT(\fu))^{1/2} \dens_2(\fT(\fu))^{1/2} \|f\|_2\|g\|_2\,. \end{equation}
- id `moderate-scale-change`: lemma (moderate scale change); steps here: state and prove. If $J, J' \in \mathcal{J'}$ with $$ B(J) \cap B(J') \ne \emptyset\,, $$ then $|s(J) - s(J')| \le 1$.
- id `local-dens1-tree-bound`: lemma (local dens1 tree bound); steps here: state and prove. Let $\fu \in \fU$ and $L \in \mathcal{L}(\fT(\fu))$. Then \begin{equation} \mu(L \cap G \cap \bigcup_{\fp \in \fT(\fu)} E(\fp)) \le 2^{101a^3} \dens_1(\fT(\fu)) \mu(L)\,. \end{equation}
- id `adjoint-tree-estimate`: lemma (adjoint tree estimate); steps here: state and prove. For all bounded $g$ supported on $G$ we have that $$ \left\| \sum_{\fp \in \fT(\fu)} T_{\fp}^* g\right\|_2 \le 2^{181a^3} \dens_1(\fT(\fu))^{1/2} \|g\|_2\,, $$ $$ \left\| \mathbf{1}_F \sum_{\fp \in \fT(\fu)} T_{\fp}^* g\right\|_2 \le 2^{282a^3} \dens_1(\fT(\fu))^{1/2} \dens_2(\fT(\fu))^{1/2} \|g\|_2\,. $$
- id `thin-scale-impact`: lemma (thin scale impact); steps here: state and prove. If $\fp \in \fT(\fu_2) \setminus \mathfrak{S}$ and $J \in \mathcal{J'}$ with $B(\scI(\fp)) \cap B(J) \ne \emptyset$, then $$ \ps(\fp) \le s(J) + 2 - \frac{Zn}{202a^3}\,. $$
- id `limited-scale-impact`: lemma (limited scale impact); steps here: state and prove. Let $\fp \in \fT(\fu_2) \setminus \mathfrak{S}$, $J \in \mathcal{J}'$ and suppose that $$ B(\scI(\fp)) \cap B^\circ(J) \ne \emptyset\,. $$ Then $$ s(J) \le \ps(\fp) \le s(J) +3\,. $$
- id `row-bound`: lemma (row bound); steps here: state and prove. For each $1 \le j \le 2^n$ and each bounded $g$ supported on $G$ we have \begin{equation} \left\| T_{\mathfrak{R}_j}^*g \right\|_2 \le 2^{182a^3} 2^{-n/2} \|g\|_2 \end{equation} and \begin{equation} \left\| \mathbf{1}_F T_{\mathfrak{R}_j}^*g \right\|_2 \le 2^{283a^3} 2^{-n/2} \dens_2(\bigcup_{\fu\in \fU}\fT(\fu))^{1/2} \|g\|_2\,. \end{equation}
- id `second-tree-pointwise`: lemma (second tree pointwise); steps here: state and prove. For all $\fu \in \fU$, all $L \in \mathcal{L}(\fT(\fu))$, all $x, x' \in L$ and all bounded $f$ with bounded support, we have $$ \Bigg| \sum_{s \in \sigma(\fu, x)} \int K_s(x,y) P_{\mathcal{J}(\fT(\fu))} f(y) \, \mathrm{d}\mu(y) \Bigg| \le T_{\mathcal{N}}^{\fcc(\fu)} P_{\mathcal{J}(\fT(\fu))} f(x')\,. $$
- id `bound-for-tree-projection`: lemma (bound for tree projection); steps here: state and prove. We have for all bounded $f$ with bounded support $$ \|P_{\mathcal{J}'}|T_{\fT(\fu_2) \setminus \mathfrak{S}}^* g_2|\|_2 \le 2^{102a^3+21a+5} 2^{-\frac{25}{101a}Zn\kappa} \|\mathbf{1}_{\scI(\fu_1)} M_{\mathcal{B},1} |g_2|\|_2 $$
- id `pointwise-tree-estimate`: lemma (pointwise tree estimate); steps here: state and prove. Let $\fu \in \fU$ and $L \in \mathcal{L}(\fT(\fu))$. Let $x, x' \in L$. Then for all bounded functions $f$ with bounded support $$ \left|\sum_{\fp \in \fT(\fu)} T_{\fp}[ e(-\fcc(\fu))f](x)\right| $$ \begin{equation} \leq 2^{129a^3}(M_{\mathcal{B},1}+S_{1,\fu})P_{\mathcal{J}(\fT(\fu))}|f|(x')+|T_{\mathcal{N}}^{\fcc(\fu)} P_{\mathcal{J}(\fT(\fu))}f(x')|, \end{equation}
- id `dyadic-partition-2`: lemma (dyadic partition 2); steps here: state and prove. We have $$ \scI(\fu_1) = \dot{\bigcup_{J \in \mathcal{J}'}} J\,. $$
- id `boundary-operator-bound`: lemma (boundary operator bound); steps here: state and prove. For all $\fu \in \fU$ and all bounded functions $f$ with bounded support \begin{equation} \|S_{1,\fu}f\|_2 \le 2^{12a} \|f\|_2\,. \end{equation}
- id `Lipschitz-partition-unity`: lemma (Lipschitz partition unity); steps here: state and prove. There exists a family of functions $\chi_J$, $J \in \mathcal{J}'$ such that \begin{equation} \mathbf{1}_{\scI(\fu_1)} = \sum_{J \in \mathcal{J}'} \chi_J\,, \end{equation} and for all $J \in \mathcal{J}'$ and all $y,y' \in \scI(\fu_1)$ \begin{equation} 0 \leq \chi_J(y) \leq \mathbf{1}_{B(J)}(y)\,, \end{equation} \begin{equation} |\chi_J(y) - \chi_J(y')| \le 2^{227a^3} \frac{\rho(y,y')}{D^{s(J)}}\,. \end{equation}
- id `overlap-implies-distance`: lemma (overlap implies distance); steps here: state and prove. Let $\fu_1 \ne \fu_2 \in \fU$ with $\scI(\fu_1) \subset \scI(\fu_2)$. If $\fp \in \fT(\fu_1) \cup \fT(\fu_2)$ with $\scI(\fp) \cap \scI(\fu_1) \ne \emptyset$, then $\fp \in \mathfrak{S}$. In particular, we have $\fT(\fu_1) \subset \mathfrak{S}$.
- id `dyadic-partitions`: lemma (dyadic partitions); steps here: state and prove. For each $\mathfrak{S} \subset \fP$, we have \begin{equation} \bigcup_{I \in \mathcal{D}} I = \dot{\bigcup_{J \in \mathcal{J}(\mathfrak{S})}} J \end{equation} and \begin{equation} \bigcup_{I \in \mathcal{D}} I = \dot{\bigcup_{L \in \mathcal{L}(\mathfrak{S})}} L\,. \end{equation}
- id `global-tree-control-2`: lemma (global tree control 2); steps here: state and prove. We have for all $J \in \mathcal{J}'$ and all bounded $g$ with bounded support $$ \sup_{B'(J)} |T^*_{\fT(\fu_2) \cap \mathfrak{S}} g| \le \inf_{B^\circ{}(J)} |T^*_{\fT(\fu_2)} g| + 2^{129a^3} \inf_{J} M_{\mathcal{B},1}|g|\,. $$
- id `local-tree-control`: lemma (local tree control); steps here: state and prove. For all $J \in \mathcal{J}'$ and all bounded $g$ with bounded support $$ \sup_{B^\circ{}(J)} |T_{\mathfrak{T}(\mathfrak{u}_2)\setminus\mathfrak{S}}^* g| \le 2^{104a^3} \inf_J M_{\mathcal{B},1}|g| $$
- id `tree-projection-estimate`: lemma (tree projection estimate); steps here: state and prove. Let $\fu \in \fU$. Then we have for all $f, g$ bounded with bounded support $$ \Bigg|\int_X \sum_{\fp \in \fT(\fu)} \bar g(y) T_{\fp}f(y) \, \mathrm{d}\mu(y) \Bigg| $$ \begin{equation} \le 2^{130a^3}\|P_{\mathcal{J}(\fT(\fu))}|f|\|_{2}\|P_{\mathcal{L}(\fT(\fu))}|g|\|_{2}. \end{equation}
- id `square-function-count`: lemma (square function count); steps here: state and prove. For each $J \in \mathcal{J}'$ and all $s$, we have $$ \frac{1}{\mu(J)} \int_J \Bigg(\sum_{\substack{I \in \mathcal{D}, s(I) = s(J) - s\\ I \cap \scI(\fu_1) = \emptyset\\ J \cap B(I) \ne \emptyset}} \mathbf{1}_{B(I)}\bigg)^2 \, \mathrm{d}\mu \le 2^{14a+1} (8 D^{-s})^\kappa\,. $$
- id `boundary-overlap`: lemma (boundary overlap); steps here: state and prove. For every cube $I \in \mathcal{D}$, there exist at most $2^{9a}$ cubes $J \in \mathcal{D}$ with $s(J) = s(I)$ and $B(c(I), 16D^{s(I)}) \cap B(c(J), 16 D^{s(J)}) \ne \emptyset$.
- id `adjoint-tree-control`: lemma (adjoint tree control); steps here: state and prove. We have for all $\fu \in \fU$ and all bounded $g$ supported on $G$ $$ \|S_{2, \fu} g\|_2 \le 2^{182a^3} \|g\|_2\,. $$
- id `dyadic-partition-1`: lemma (dyadic partition 1); steps here: state and prove. We have that $$ \scI(\fu_1) = \dot{\bigcup_{J \in \mathcal{J}'}} J\,. $$
- id `Holder-correlation-tile`: lemma (Holder correlation tile); steps here: state and prove. Let $\fu \in \fU$ and $\fp \in \fT(\fu)$. Then for all $y, y' \in X$ and all bounded $g$ with bounded support, we have $$ |e(\fcc(\fu)(y)) T_{\fp}^* g(y) - e(\fcc(\fu)(y')) T_{\fp}^* g(y')| $$ \begin{equation} \le \frac{2^{128a^3}}{\mu(B(\pc(\fp), 4D^{\ps(\fp)}))} \left(\frac{\rho(y, y')}{D^{\ps(\fp)}}\right)^{1/a} \int_{E(\fp)} |g(x)| \, \mathrm{d}\mu(x)\,. \end{equation}
- id `third-tree-pointwise`: lemma (third tree pointwise); steps here: state and prove. For all $\fu \in \fU$, all $L \in \mathcal{L}(\fT(\fu))$, all $x, x' \in L$ and all bounded $f$ with bounded support, we have \begin{equation*} \Bigg| \sum_{s \in \sigma(\fu, x)} \int K_s(x,y) (f(y) - P_{\mathcal{J}(\fT(\fu))} f(y)) \, \mathrm{d}\mu(y) \Bigg| \end{equation*} \begin{equation*} \le 2^{128a^3} S_{1,\fu} P_{\mathcal{J}(\fT(\fu))}|f|(x')\,. \end{equation*}
- id `global-tree-control-1`: lemma (global tree control 1); steps here: state and prove. Let $\fC_1 = \fT(\fu_1)$ and $\fC_2 = \fT(\fu_2) \cap \mathfrak{S}$. Then for $i = 1,2$ and each $J \in \mathcal{J}'$ and all bounded $g$ with bounded support, we have \begin{align} \sup_{B'(J)} |T_{\fC_i}^*g| \leq \inf_{B^\circ{}(J)} |T^*_{\fC_i} g| + 2^{128a^3+4a+3} \inf_{J} M_{\mathcal{B}, 1} |g| \end{align} and for all $y,y' \in B'(J)$ $$ |e(\fcc(\fu_i)(y)) T_{\fC_i}^* g(y) - e(\fcc(\fu_i)(y')) T_{\fC_i}^* g(y')| $$ \begin{equation} \le 2^{128a^3+4a+1} \left(\frac{\rho(y,y')}{D^{s(J)}}\right)^{1/a} \inf_J M_{\mathcal{B},1} |g|\,. \end{equation}
- id `correlation-near-tree-parts`: lemma (correlation near tree parts); steps here: state and prove. We have for all $\fu_1 \ne \fu_2 \in \fU$ with $\scI(\fu_1) \subset \scI(\fu_2)$ and all bounded $g_1, g_2$ with bounded support \begin{equation} \left| \int_X \sum_{\fp_1 \in \fT(\fu_1)} \sum_{\fp_2 \in \fT(\fu_2) \setminus \mathfrak{S}} T^*_{\fp_1}g_1 \overline{T^*_{\fp_2}g_2 }\,\mathrm{d}\mu \right| \end{equation} \begin{equation} \le 2^{232a^3+21a+5} 2^{-\frac{25}{101a}Zn\kappa} \prod_{j=1}^2 \|S_{2, \fu_j} g_j\|_{L^2(\scI(\fu_1))}\,. \end{equation}
- id `row-correlation`: lemma (row correlation); steps here: state and prove. For all $1 \le j,j' \le 2^n$ with $j\ne j'$ and for all bounded $g_1, g_2$ supported on $G$, it holds that $$ \left| \int T_{\mathfrak{R}_j}^*g_1 \overline{T_{\mathfrak{R}_{j'}}^*g_2} \, \mathrm{d}\mu \right| \le 2^{876a^3-4n}\|g_1\|_2 \|g_2\|_2\,. $$
- id `forest-row-decomposition`: lemma (forest row decomposition); steps here: state and prove. Let $(\fU, \fT)$ be an $n$-forest. Then there exists a decomposition $$ \fU = \dot{\bigcup_{1 \le j \le 2^n}} \fU_j $$ such that for all $j = 1, \dotsc, 2^n$ the pair $(\fU_j, \fT|_{\fU_j})$ is an $n$-row.
- id `disjoint-row-support`: lemma (disjoint row support); steps here: state and prove. The sets $E_j$, $1 \le j \le 2^n$ are pairwise disjoint.

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:Holder-correlation-tile` before `P:global-tree-control-1`
- `S:Holder-correlation-tree` before `P:correlation-distant-tree-parts`
- `S:Lipschitz-partition-unity` before `P:Holder-correlation-tree`
- `S:Lipschitz-partition-unity` before `P:correlation-distant-tree-parts`
- `S:adjoint-tile-support` before `P:Holder-correlation-tile`
- `S:adjoint-tile-support` before `P:Holder-correlation-tree`
- `S:adjoint-tile-support` before `P:bound-for-tree-projection`
- `S:adjoint-tile-support` before `P:correlation-distant-tree-parts`
- `S:adjoint-tile-support` before `P:correlation-near-tree-parts`
- `S:adjoint-tile-support` before `P:correlation-separated-trees`
- `S:adjoint-tile-support` before `P:global-tree-control-1`
- `S:adjoint-tile-support` before `P:local-tree-control`
- `S:adjoint-tile-support` before `P:row-bound`
- `S:adjoint-tree-control` before `P:row-correlation`
- `S:adjoint-tree-estimate` before `P:adjoint-tree-control`
- `S:adjoint-tree-estimate` before `P:row-bound`
- `S:bound-for-tree-projection` before `P:correlation-near-tree-parts`
- `S:boundary-operator-bound` before `P:tree-projection-estimate`
- `S:boundary-overlap` before `P:boundary-operator-bound`
- `S:convex-scales` before `P:second-tree-pointwise`
- `S:correlation-distant-tree-parts` before `P:correlation-separated-trees`
- `S:correlation-near-tree-parts` before `P:correlation-separated-trees`
- `S:correlation-separated-trees` before `P:row-correlation`
- `S:densities-tree-bound` before `P:adjoint-tree-estimate`
- `S:disjoint-row-support` before `P:forest-operator`
- `S:dyadic-partition-1` before `P:Lipschitz-partition-unity`
- `S:dyadic-partition-1` before `P:correlation-distant-tree-parts`
- `S:dyadic-partition-2` before `P:bound-for-tree-projection`
- `S:dyadic-partition-2` before `P:correlation-near-tree-parts`
- `S:dyadic-partitions` before `P:boundary-operator-bound`
- `S:dyadic-partitions` before `P:correlation-near-tree-parts`
- `S:dyadic-partitions` before `P:densities-tree-bound`
- `S:dyadic-partitions` before `P:dyadic-partition-1`
- `S:dyadic-partitions` before `P:dyadic-partition-2`
- `S:dyadic-partitions` before `P:first-tree-pointwise`
- `S:dyadic-partitions` before `P:third-tree-pointwise`
- `S:dyadic-partitions` before `P:tree-projection-estimate`
- `S:first-tree-pointwise` before `P:pointwise-tree-estimate`
- `S:forest-row-decomposition` before `P:forest-operator`
- `S:forest-row-decomposition` before `P:row-bound`
- `S:forest-row-decomposition` before `P:row-correlation`
- `S:forest-row-decomposition` before `S:disjoint-row-support`
- `S:global-tree-control-1` before `P:Holder-correlation-tree`
- `S:global-tree-control-1` before `P:global-tree-control-2`
- `S:global-tree-control-2` before `P:Holder-correlation-tree`
- `S:limited-scale-impact` before `P:local-tree-control`
- `S:local-dens1-tree-bound` before `P:densities-tree-bound`
- `S:local-dens2-tree-bound` before `P:densities-tree-bound`
- `S:local-tree-control` before `P:global-tree-control-2`
- `S:lower-oscillation-bound` before `P:correlation-distant-tree-parts`
- `S:moderate-scale-change` before `P:Lipschitz-partition-unity`
- `S:nontangential-operator-bound` before `P:tree-projection-estimate`
- `S:overlap-implies-distance` before `P:bound-for-tree-projection`
- `S:overlap-implies-distance` before `P:dyadic-partition-1`
- `S:overlap-implies-distance` before `P:limited-scale-impact`
- `S:overlap-implies-distance` before `P:lower-oscillation-bound`
- `S:overlap-implies-distance` before `P:scales-impacting-interval`
- `S:pointwise-tree-estimate` before `P:tree-projection-estimate`
- `S:row-bound` before `P:forest-operator`
- `S:row-correlation` before `P:forest-operator`
- `S:scales-impacting-interval` before `P:global-tree-control-1`
- `S:second-tree-pointwise` before `P:pointwise-tree-estimate`
- `S:square-function-count` before `P:bound-for-tree-projection`
- `S:thin-scale-impact` before `P:bound-for-tree-projection`
- `S:third-tree-pointwise` before `P:pointwise-tree-estimate`
- `S:tree-projection-estimate` before `P:correlation-near-tree-parts`
- `S:tree-projection-estimate` before `P:densities-tree-bound`
