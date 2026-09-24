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

- id `r762`: lemma; steps here: state and prove. For all $J \in \mathcal{J}'$ and all bounded $g$ with bounded support $$ \sup_{B^\circ{}(J)} |T_{\mathfrak{T}(\mathfrak{u}_2)\setminus\mathfrak{S}}^* g| \le 2^{104a^3} \inf_J M_{\mathcal{B},1}|g| $$
- id `r408`: lemma; steps here: state and prove. If $\fp \in \fT(\fu_2) \setminus \mathfrak{S}$ and $J \in \mathcal{J'}$ with $B(\scI(\fp)) \cap B(J) \ne \emptyset$, then $$ \ps(\fp) \le s(J) + 2 - \frac{Zn}{202a^3}\,. $$
- id `r458`: lemma; steps here: state and prove. For each $\fp \in \fP$, we have $$ T_{\fp}^* g = \mathbf{1}_{B(\pc(\fp), 5D^{\ps(\fp)})} T_{\fp}^* \mathbf{1}_{\scI(\fp)} g\,. $$ For each $\fu \in \fU$ and each $\fp \in \fT(\fu)$, we have $$ T_{\fp}^* g = \mathbf{1}_{\scI(\fu)} T_{\fp}^* \mathbf{1}_{\scI(\fu)} g\,. $$
- id `r546`: lemma; steps here: state and prove. For any $\fu_1 \ne \fu_2 \in \fU$ and all bounded $g_1, g_2$ with bounded support, we have \begin{equation} \left| \int_X \sum_{\fp_1 \in \fT(\fu_1)} \sum_{\fp_2 \in \fT(\fu_2)} T^*_{\fp_1}g_1 \overline{T^*_{\fp_2}g_2 }\,\mathrm{d}\mu \right| \end{equation} \begin{equation} \le 2^{512a^3-4n} \prod_{j =1}^2 \| S_{2, \fu_j} g_j\|_{L^2(\scI(\fu_1) \cap \scI(\fu_2))}\,. \end{equation}
- id `r284`: lemma; steps here: state and prove. If $J, J' \in \mathcal{J'}$ with $$ B(J) \cap B(J') \ne \emptyset\,, $$ then $|s(J) - s(J')| \le 1$.
- id `r162`: lemma; steps here: state and prove. For each $J \in \mathcal{J}'$ and all $s$, we have $$ \frac{1}{\mu(J)} \int_J \Bigg(\sum_{\substack{I \in \mathcal{D}, s(I) = s(J) - s\\ I \cap \scI(\fu_1) = \emptyset\\ J \cap B(I) \ne \emptyset}} \mathbf{1}_{B(I)}\bigg)^2 \, \mathrm{d}\mu \le 2^{14a+1} (8 D^{-s})^\kappa\,. $$
- id `r615`: lemma; steps here: state and prove. We have $$ \scI(\fu_1) = \dot{\bigcup_{J \in \mathcal{J}'}} J\,. $$
- id `r578`: lemma; steps here: state and prove. We have for all $\fu_1 \ne \fu_2 \in \fU$ with $\scI(\fu_1) \subset \scI(\fu_2)$ and all bounded $g_1, g_2$ with bounded support \begin{equation} \left| \int_X \sum_{\fp_1 \in \fT(\fu_1)} \sum_{\fp_2 \in \fT(\fu_2) \cap \mathfrak{S}} T^*_{\fp_1}g_1 \overline{T^*_{\fp_2}g_2 }\,\mathrm{d}\mu \right| \end{equation} \begin{equation} \le 2^{511a^3} 2^{-Zn/(4a^2 + 2a^3)} \prod_{j =1}^2 \| S_{2, \fu_j} g_j\|_{L^2(\scI(\fu_1))}\,. \end{equation}
- id `r140`: lemma; steps here: state and prove. For all $\fu \in \fU$ and all bounded functions $f$ with bounded support \begin{equation} \|S_{1,\fu}f\|_2 \le 2^{12a} \|f\|_2\,. \end{equation}
- id `r710`: lemma; steps here: state and prove. We have for all $J \in \mathcal{J}'$ that \begin{equation} \|h_J\|_{C^{\tau}(B(c(J), 16D^{s(J)}))} \le 2^{485a^3} \prod_{j = 1,2} (\inf_{B(c(J), \frac{1}{8}D^{s(J)})} |T_{\fT(\fu_j)}^* g_j| + \inf_J M_{\mathcal{B}, 1} |g_j|)\,. \end{equation}
- id `r203`: proposition; steps here: prove only (it was stated in an earlier section). For any $n\ge 0$ and any $n$-forest $(\fU,\fT)$ we have for all $f,g: X \to \mathbb{C}$ with $|f| \le \mathbf{1}_F$ and $|g| \le \mathbf{1}_G$ $$ | \int \overline{g(x)} \sum_{\fu\in \fU} \sum_{\fp\in \fT(\fu)} T_{\fp} f(x) \, \mathrm{d}\mu(x)| $$ $$ \le 2^{440a^3}2^{-\frac{q-1}{q} n} \dens_2\left(\bigcup_{\fu\in \fU}\fT(\fu)\right)^{\frac{1}{q}-\frac{1}{2}} \|f\|_2 \|g\|_2 \,. $$
- id `r816`: lemma; steps here: state and prove. Let $\fp \in \fT(\fu_2) \setminus \mathfrak{S}$, $J \in \mathcal{J}'$ and suppose that $$ B(\scI(\fp)) \cap B^\circ(J) \ne \emptyset\,. $$ Then $$ s(J) \le \ps(\fp) \le s(J) +3\,. $$
- id `r500`: lemma; steps here: state and prove. The sets $E_j$, $1 \le j \le 2^n$ are pairwise disjoint.
- id `r304`: lemma; steps here: state and prove. We have for all $\fu \in \fU$ and all bounded $g$ supported on $G$ $$ \|S_{2, \fu} g\|_2 \le 2^{182a^3} \|g\|_2\,. $$
- id `r366`: lemma; steps here: state and prove. For all bounded $f$ with bounded support and all $\mfa \in \Mf$ $$ \|T_{\mathcal{N}}^{\mfa} f\|_2 \le 2^{102a^3} \|f\|_2\,. $$
- id `r467`: lemma; steps here: state and prove. Let $\fC_1 = \fT(\fu_1)$ and $\fC_2 = \fT(\fu_2) \cap \mathfrak{S}$. Then for $i = 1,2$ and each $J \in \mathcal{J}'$ and all bounded $g$ with bounded support, we have \begin{align} \sup_{B'(J)} |T_{\fC_i}^*g| \leq \inf_{B^\circ{}(J)} |T^*_{\fC_i} g| + 2^{128a^3+4a+3} \inf_{J} M_{\mathcal{B}, 1} |g| \end{align} and for all $y,y' \in B'(J)$ $$ |e(\fcc(\fu_i)(y)) T_{\fC_i}^* g(y) - e(\fcc(\fu_i)(y')) T_{\fC_i}^* g(y')| $$ \begin{equation} \le 2^{128a^3+4a+1} \left(\frac{\rho(y,y')}{D^{s(J)}}\right)^{1/a} \inf_J M_{\mathcal{B},1} |g|\,. \end{equation}
- id `r849`: lemma; steps here: state and prove. For all $\fu \in \fU$, all $L \in \mathcal{L}(\fT(\fu))$, all $x, x' \in L$ and all bounded $f$ with bounded support, we have \begin{equation*} \Bigg| \sum_{s \in \sigma(\fu, x)} \int K_s(x,y) (f(y) - P_{\mathcal{J}(\fT(\fu))} f(y)) \, \mathrm{d}\mu(y) \Bigg| \end{equation*} \begin{equation*} \le 2^{128a^3} S_{1,\fu} P_{\mathcal{J}(\fT(\fu))}|f|(x')\,. \end{equation*}
- id `r581`: lemma; steps here: state and prove. For all $1 \le j,j' \le 2^n$ with $j\ne j'$ and for all bounded $g_1, g_2$ supported on $G$, it holds that $$ \left| \int T_{\mathfrak{R}_j}^*g_1 \overline{T_{\mathfrak{R}_{j'}}^*g_2} \, \mathrm{d}\mu \right| \le 2^{876a^3-4n}\|g_1\|_2 \|g_2\|_2\,. $$
- id `r958`: lemma; steps here: state and prove. For all $J \in \mathcal{J}'$, we have that $$ d_{B(J)}(\fcc(\fu_1), \fcc(\fu_2)) \ge 2^{-201a^3} 2^{Zn/2}\,. $$
- id `r683`: lemma; steps here: state and prove. For each $\mathfrak{S} \subset \fP$, we have \begin{equation} \bigcup_{I \in \mathcal{D}} I = \dot{\bigcup_{J \in \mathcal{J}(\mathfrak{S})}} J \end{equation} and \begin{equation} \bigcup_{I \in \mathcal{D}} I = \dot{\bigcup_{L \in \mathcal{L}(\mathfrak{S})}} L\,. \end{equation}
- id `r273`: lemma; steps here: state and prove. Let $\fu \in \fU$ and $\fp \in \fT(\fu)$. Then for all $y, y' \in X$ and all bounded $g$ with bounded support, we have $$ |e(\fcc(\fu)(y)) T_{\fp}^* g(y) - e(\fcc(\fu)(y')) T_{\fp}^* g(y')| $$ \begin{equation} \le \frac{2^{128a^3}}{\mu(B(\pc(\fp), 4D^{\ps(\fp)}))} \left(\frac{\rho(y, y')}{D^{\ps(\fp)}}\right)^{1/a} \int_{E(\fp)} |g(x)| \, \mathrm{d}\mu(x)\,. \end{equation}
- id `r814`: lemma; steps here: state and prove. Let $\fu \in \fU$ and $L \in \mathcal{L}(\fT(\fu))$. Then \begin{equation} \mu(L \cap G \cap \bigcup_{\fp \in \fT(\fu)} E(\fp)) \le 2^{101a^3} \dens_1(\fT(\fu)) \mu(L)\,. \end{equation}
- id `r788`: lemma; steps here: state and prove. We have for all bounded $f$ with bounded support $$ \|P_{\mathcal{J}'}|T_{\fT(\fu_2) \setminus \mathfrak{S}}^* g_2|\|_2 \le 2^{102a^3+21a+5} 2^{-\frac{25}{101a}Zn\kappa} \|\mathbf{1}_{\scI(\fu_1)} M_{\mathcal{B},1} |g_2|\|_2 $$
- id `r308`: lemma; steps here: state and prove. Let $\fu \in \fU$ and $J \in \mathcal{J}(\fT(\fu))$. Then $$ \mu(F \cap J) \le 2^{201a^3} \dens_2(\fT(\fu)) \mu(J)\,. $$
- id `r885`: lemma; steps here: state and prove. We have for all $J \in \mathcal{J}'$ and all bounded $g$ with bounded support $$ \sup_{B'(J)} |T^*_{\fT(\fu_2) \cap \mathfrak{S}} g| \le \inf_{B^\circ{}(J)} |T^*_{\fT(\fu_2)} g| + 2^{129a^3} \inf_{J} M_{\mathcal{B},1}|g|\,. $$
- id `r159`: lemma; steps here: state and prove. We have for all $\fu_1 \ne \fu_2 \in \fU$ with $\scI(\fu_1) \subset \scI(\fu_2)$ and all bounded $g_1, g_2$ with bounded support \begin{equation} \left| \int_X \sum_{\fp_1 \in \fT(\fu_1)} \sum_{\fp_2 \in \fT(\fu_2) \setminus \mathfrak{S}} T^*_{\fp_1}g_1 \overline{T^*_{\fp_2}g_2 }\,\mathrm{d}\mu \right| \end{equation} \begin{equation} \le 2^{232a^3+21a+5} 2^{-\frac{25}{101a}Zn\kappa} \prod_{j=1}^2 \|S_{2, \fu_j} g_j\|_{L^2(\scI(\fu_1))}\,. \end{equation}
- id `r907`: lemma; steps here: state and prove. Let $\fu_1 \ne \fu_2 \in \fU$ with $\scI(\fu_1) \subset \scI(\fu_2)$. If $\fp \in \fT(\fu_1) \cup \fT(\fu_2)$ with $\scI(\fp) \cap \scI(\fu_1) \ne \emptyset$, then $\fp \in \mathfrak{S}$. In particular, we have $\fT(\fu_1) \subset \mathfrak{S}$.
- id `r792`: lemma; steps here: state and prove. Let $(\fU, \fT)$ be an $n$-forest. Then there exists a decomposition $$ \fU = \dot{\bigcup_{1 \le j \le 2^n}} \fU_j $$ such that for all $j = 1, \dotsc, 2^n$ the pair $(\fU_j, \fT|_{\fU_j})$ is an $n$-row.
- id `r262`: lemma; steps here: state and prove. We have that $$ \scI(\fu_1) = \dot{\bigcup_{J \in \mathcal{J}'}} J\,. $$
- id `r965`: lemma; steps here: state and prove. For each $1 \le j \le 2^n$ and each bounded $g$ supported on $G$ we have \begin{equation} \left\| T_{\mathfrak{R}_j}^*g \right\|_2 \le 2^{182a^3} 2^{-n/2} \|g\|_2 \end{equation} and \begin{equation} \left\| \mathbf{1}_F T_{\mathfrak{R}_j}^*g \right\|_2 \le 2^{283a^3} 2^{-n/2} \dens_2(\bigcup_{\fu\in \fU}\fT(\fu))^{1/2} \|g\|_2\,. \end{equation}
- id `r265`: lemma; steps here: state and prove. For each $\fu \in \fU$, we have $$ \sigma(\fu, x) = \mathbb{Z} \cap [\underline{\sigma} (\fu, x), \overline{\sigma} (\fu, x)]\,. $$
- id `r450`: lemma; steps here: state and prove. For all $\fu \in \fU$, all $L \in \mathcal{L}(\fT(\fu))$, all $x, x' \in L$ and all bounded $f$ with bounded support, we have $$ \Bigg| \sum_{s \in \sigma(\fu, x)} \int K_s(x,y) P_{\mathcal{J}(\fT(\fu))} f(y) \, \mathrm{d}\mu(y) \Bigg| \le T_{\mathcal{N}}^{\fcc(\fu)} P_{\mathcal{J}(\fT(\fu))} f(x')\,. $$
- id `r642`: lemma; steps here: state and prove. Let $\fu \in \fU$ and $L \in \mathcal{L}(\fT(\fu))$. Let $x, x' \in L$. Then for all bounded functions $f$ with bounded support $$ \left|\sum_{\fp \in \fT(\fu)} T_{\fp}[ e(-\fcc(\fu))f](x)\right| $$ \begin{equation} \leq 2^{129a^3}(M_{\mathcal{B},1}+S_{1,\fu})P_{\mathcal{J}(\fT(\fu))}|f|(x')+|T_{\mathcal{N}}^{\fcc(\fu)} P_{\mathcal{J}(\fT(\fu))}f(x')|, \end{equation}
- id `r356`: lemma; steps here: state and prove. For all bounded $g$ supported on $G$ we have that $$ \left\| \sum_{\fp \in \fT(\fu)} T_{\fp}^* g\right\|_2 \le 2^{181a^3} \dens_1(\fT(\fu))^{1/2} \|g\|_2\,, $$ $$ \left\| \mathbf{1}_F \sum_{\fp \in \fT(\fu)} T_{\fp}^* g\right\|_2 \le 2^{282a^3} \dens_1(\fT(\fu))^{1/2} \dens_2(\fT(\fu))^{1/2} \|g\|_2\,. $$
- id `r220`: lemma; steps here: state and prove. For every cube $I \in \mathcal{D}$, there exist at most $2^{9a}$ cubes $J \in \mathcal{D}$ with $s(J) = s(I)$ and $B(c(I), 16D^{s(I)}) \cap B(c(J), 16 D^{s(J)}) \ne \emptyset$.
- id `r711`: lemma; steps here: state and prove. Let $\fu \in \fU$. Then we have for all $f, g$ bounded with bounded support $$ \Bigg|\int_X \sum_{\fp \in \fT(\fu)} \bar g(y) T_{\fp}f(y) \, \mathrm{d}\mu(y) \Bigg| $$ \begin{equation} \le 2^{130a^3}\|P_{\mathcal{J}(\fT(\fu))}|f|\|_{2}\|P_{\mathcal{L}(\fT(\fu))}|g|\|_{2}. \end{equation}
- id `r552`: lemma; steps here: state and prove. For all $\fu \in \fU$, all $L \in \mathcal{L}(\fT(\fu))$, all $x, x' \in L$ and all bounded $f$ with bounded support, we have $$ [another result] \le 10 \cdot 2^{104a^3} M_{\mathcal{B}, 1}P_{\mathcal{J}(\fT(\fu))}|f|(x')\,. $$
- id `r781`: lemma; steps here: state and prove. Let $\fC = \fT(\fu_1)$ or $\fC = \fT(\fu_2) \cap \mathfrak{S}$. Then for each $J \in \mathcal{J}'$ and $\fp \in \fC$ with $B(\scI(\fp)) \cap B'(J) \neq \emptyset$, we have $\ps(\fp) \ge s(J)$.
- id `r279`: lemma; steps here: state and prove. There exists a family of functions $\chi_J$, $J \in \mathcal{J}'$ such that \begin{equation} \mathbf{1}_{\scI(\fu_1)} = \sum_{J \in \mathcal{J}'} \chi_J\,, \end{equation} and for all $J \in \mathcal{J}'$ and all $y,y' \in \scI(\fu_1)$ \begin{equation} 0 \leq \chi_J(y) \leq \mathbf{1}_{B(J)}(y)\,, \end{equation} \begin{equation} |\chi_J(y) - \chi_J(y')| \le 2^{227a^3} \frac{\rho(y,y')}{D^{s(J)}}\,. \end{equation}
- id `r113`: lemma; steps here: state and prove. Let $\fu \in \fU$. Then for all bounded $f$ with bounded support and bounded $g$ supported on $G$ we have \begin{equation} \left|\int_X \bar g \sum_{\fp \in \fT(\fu)} T_{\fp }f \, \mathrm{d}\mu \right| \le 2^{181a^3} \dens_1(\fT(\fu))^{1/2} \|f\|_2\|g\|_2\,. \end{equation} If additionally $\text{support}(f) \subseteq F$, then we have \begin{equation} \left| \int_X \bar g \sum_{\fp \in \fT(\fu)} T_{\fp }f\, \mathrm{d}\mu \right| \le 2^{282a^3} \dens_1(\fT(\fu))^{1/2} \dens_2(\fT(\fu))^{1/2} \|f\|_2\|g\|_2\,. \end{equation}

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:r113` before `P:r356`
- `S:r140` before `P:r711`
- `S:r159` before `P:r546`
- `S:r162` before `P:r788`
- `S:r220` before `P:r140`
- `S:r262` before `P:r279`
- `S:r262` before `P:r578`
- `S:r265` before `P:r450`
- `S:r273` before `P:r467`
- `S:r279` before `P:r578`
- `S:r279` before `P:r710`
- `S:r284` before `P:r279`
- `S:r304` before `P:r581`
- `S:r308` before `P:r113`
- `S:r356` before `P:r304`
- `S:r356` before `P:r965`
- `S:r366` before `P:r711`
- `S:r408` before `P:r788`
- `S:r450` before `P:r642`
- `S:r458` before `P:r159`
- `S:r458` before `P:r273`
- `S:r458` before `P:r467`
- `S:r458` before `P:r546`
- `S:r458` before `P:r578`
- `S:r458` before `P:r710`
- `S:r458` before `P:r762`
- `S:r458` before `P:r788`
- `S:r458` before `P:r965`
- `S:r467` before `P:r710`
- `S:r467` before `P:r885`
- `S:r500` before `P:r203`
- `S:r546` before `P:r581`
- `S:r552` before `P:r642`
- `S:r578` before `P:r546`
- `S:r581` before `P:r203`
- `S:r615` before `P:r159`
- `S:r615` before `P:r788`
- `S:r642` before `P:r711`
- `S:r683` before `P:r113`
- `S:r683` before `P:r140`
- `S:r683` before `P:r159`
- `S:r683` before `P:r262`
- `S:r683` before `P:r552`
- `S:r683` before `P:r615`
- `S:r683` before `P:r711`
- `S:r683` before `P:r849`
- `S:r710` before `P:r578`
- `S:r711` before `P:r113`
- `S:r711` before `P:r159`
- `S:r762` before `P:r885`
- `S:r781` before `P:r467`
- `S:r788` before `P:r159`
- `S:r792` before `P:r203`
- `S:r792` before `P:r581`
- `S:r792` before `P:r965`
- `S:r792` before `S:r500`
- `S:r814` before `P:r113`
- `S:r816` before `P:r762`
- `S:r849` before `P:r642`
- `S:r885` before `P:r710`
- `S:r907` before `P:r262`
- `S:r907` before `P:r781`
- `S:r907` before `P:r788`
- `S:r907` before `P:r816`
- `S:r907` before `P:r958`
- `S:r958` before `P:r578`
- `S:r965` before `P:r203`
