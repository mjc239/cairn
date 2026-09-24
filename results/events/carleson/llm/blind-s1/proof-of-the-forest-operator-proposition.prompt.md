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

- id `r419`: lemma; steps here: state and prove. For all $J \in \mathcal{J}'$, we have that $$ d_{B(J)}(\fcc(\fu_1), \fcc(\fu_2)) \ge 2^{-201a^3} 2^{Zn/2}\,. $$
- id `r495`: lemma; steps here: state and prove. Let $\fu \in \fU$. Then we have for all $f, g$ bounded with bounded support $$ \Bigg|\int_X \sum_{\fp \in \fT(\fu)} \bar g(y) T_{\fp}f(y) \, \mathrm{d}\mu(y) \Bigg| $$ \begin{equation} \le 2^{130a^3}\|P_{\mathcal{J}(\fT(\fu))}|f|\|_{2}\|P_{\mathcal{L}(\fT(\fu))}|g|\|_{2}. \end{equation}
- id `r451`: lemma; steps here: state and prove. We have for all $J \in \mathcal{J}'$ that \begin{equation} \|h_J\|_{C^{\tau}(B(c(J), 16D^{s(J)}))} \le 2^{485a^3} \prod_{j = 1,2} (\inf_{B(c(J), \frac{1}{8}D^{s(J)})} |T_{\fT(\fu_j)}^* g_j| + \inf_J M_{\mathcal{B}, 1} |g_j|)\,. \end{equation}
- id `r531`: lemma; steps here: state and prove. We have for all $\fu_1 \ne \fu_2 \in \fU$ with $\scI(\fu_1) \subset \scI(\fu_2)$ and all bounded $g_1, g_2$ with bounded support \begin{equation} \left| \int_X \sum_{\fp_1 \in \fT(\fu_1)} \sum_{\fp_2 \in \fT(\fu_2) \cap \mathfrak{S}} T^*_{\fp_1}g_1 \overline{T^*_{\fp_2}g_2 }\,\mathrm{d}\mu \right| \end{equation} \begin{equation} \le 2^{511a^3} 2^{-Zn/(4a^2 + 2a^3)} \prod_{j =1}^2 \| S_{2, \fu_j} g_j\|_{L^2(\scI(\fu_1))}\,. \end{equation}
- id `r915`: lemma; steps here: state and prove. Let $\fu_1 \ne \fu_2 \in \fU$ with $\scI(\fu_1) \subset \scI(\fu_2)$. If $\fp \in \fT(\fu_1) \cup \fT(\fu_2)$ with $\scI(\fp) \cap \scI(\fu_1) \ne \emptyset$, then $\fp \in \mathfrak{S}$. In particular, we have $\fT(\fu_1) \subset \mathfrak{S}$.
- id `r292`: lemma; steps here: state and prove. Let $\fu \in \fU$. Then for all bounded $f$ with bounded support and bounded $g$ supported on $G$ we have \begin{equation} \left|\int_X \bar g \sum_{\fp \in \fT(\fu)} T_{\fp }f \, \mathrm{d}\mu \right| \le 2^{181a^3} \dens_1(\fT(\fu))^{1/2} \|f\|_2\|g\|_2\,. \end{equation} If additionally $\text{support}(f) \subseteq F$, then we have \begin{equation} \left| \int_X \bar g \sum_{\fp \in \fT(\fu)} T_{\fp }f\, \mathrm{d}\mu \right| \le 2^{282a^3} \dens_1(\fT(\fu))^{1/2} \dens_2(\fT(\fu))^{1/2} \|f\|_2\|g\|_2\,. \end{equation}
- id `r364`: lemma; steps here: state and prove. We have for all $\fu_1 \ne \fu_2 \in \fU$ with $\scI(\fu_1) \subset \scI(\fu_2)$ and all bounded $g_1, g_2$ with bounded support \begin{equation} \left| \int_X \sum_{\fp_1 \in \fT(\fu_1)} \sum_{\fp_2 \in \fT(\fu_2) \setminus \mathfrak{S}} T^*_{\fp_1}g_1 \overline{T^*_{\fp_2}g_2 }\,\mathrm{d}\mu \right| \end{equation} \begin{equation} \le 2^{232a^3+21a+5} 2^{-\frac{25}{101a}Zn\kappa} \prod_{j=1}^2 \|S_{2, \fu_j} g_j\|_{L^2(\scI(\fu_1))}\,. \end{equation}
- id `r211`: lemma; steps here: state and prove. Let $\fC_1 = \fT(\fu_1)$ and $\fC_2 = \fT(\fu_2) \cap \mathfrak{S}$. Then for $i = 1,2$ and each $J \in \mathcal{J}'$ and all bounded $g$ with bounded support, we have \begin{align} \sup_{B'(J)} |T_{\fC_i}^*g| \leq \inf_{B^\circ{}(J)} |T^*_{\fC_i} g| + 2^{128a^3+4a+3} \inf_{J} M_{\mathcal{B}, 1} |g| \end{align} and for all $y,y' \in B'(J)$ $$ |e(\fcc(\fu_i)(y)) T_{\fC_i}^* g(y) - e(\fcc(\fu_i)(y')) T_{\fC_i}^* g(y')| $$ \begin{equation} \le 2^{128a^3+4a+1} \left(\frac{\rho(y,y')}{D^{s(J)}}\right)^{1/a} \inf_J M_{\mathcal{B},1} |g|\,. \end{equation}
- id `r359`: lemma; steps here: state and prove. We have $$ \scI(\fu_1) = \dot{\bigcup_{J \in \mathcal{J}'}} J\,. $$
- id `r847`: lemma; steps here: state and prove. Let $\fu \in \fU$ and $J \in \mathcal{J}(\fT(\fu))$. Then $$ \mu(F \cap J) \le 2^{201a^3} \dens_2(\fT(\fu)) \mu(J)\,. $$
- id `r622`: lemma; steps here: state and prove. For each $\fp \in \fP$, we have $$ T_{\fp}^* g = \mathbf{1}_{B(\pc(\fp), 5D^{\ps(\fp)})} T_{\fp}^* \mathbf{1}_{\scI(\fp)} g\,. $$ For each $\fu \in \fU$ and each $\fp \in \fT(\fu)$, we have $$ T_{\fp}^* g = \mathbf{1}_{\scI(\fu)} T_{\fp}^* \mathbf{1}_{\scI(\fu)} g\,. $$
- id `r314`: lemma; steps here: state and prove. We have that $$ \scI(\fu_1) = \dot{\bigcup_{J \in \mathcal{J}'}} J\,. $$
- id `r720`: lemma; steps here: state and prove. For all $\fu \in \fU$, all $L \in \mathcal{L}(\fT(\fu))$, all $x, x' \in L$ and all bounded $f$ with bounded support, we have $$ \Bigg| \sum_{s \in \sigma(\fu, x)} \int K_s(x,y) P_{\mathcal{J}(\fT(\fu))} f(y) \, \mathrm{d}\mu(y) \Bigg| \le T_{\mathcal{N}}^{\fcc(\fu)} P_{\mathcal{J}(\fT(\fu))} f(x')\,. $$
- id `r542`: lemma; steps here: state and prove. Let $\fu \in \fU$ and $\fp \in \fT(\fu)$. Then for all $y, y' \in X$ and all bounded $g$ with bounded support, we have $$ |e(\fcc(\fu)(y)) T_{\fp}^* g(y) - e(\fcc(\fu)(y')) T_{\fp}^* g(y')| $$ \begin{equation} \le \frac{2^{128a^3}}{\mu(B(\pc(\fp), 4D^{\ps(\fp)}))} \left(\frac{\rho(y, y')}{D^{\ps(\fp)}}\right)^{1/a} \int_{E(\fp)} |g(x)| \, \mathrm{d}\mu(x)\,. \end{equation}
- id `r936`: lemma; steps here: state and prove. We have for all $\fu \in \fU$ and all bounded $g$ supported on $G$ $$ \|S_{2, \fu} g\|_2 \le 2^{182a^3} \|g\|_2\,. $$
- id `r121`: lemma; steps here: state and prove. For all $1 \le j,j' \le 2^n$ with $j\ne j'$ and for all bounded $g_1, g_2$ supported on $G$, it holds that $$ \left| \int T_{\mathfrak{R}_j}^*g_1 \overline{T_{\mathfrak{R}_{j'}}^*g_2} \, \mathrm{d}\mu \right| \le 2^{876a^3-4n}\|g_1\|_2 \|g_2\|_2\,. $$
- id `r330`: lemma; steps here: state and prove. For every cube $I \in \mathcal{D}$, there exist at most $2^{9a}$ cubes $J \in \mathcal{D}$ with $s(J) = s(I)$ and $B(c(I), 16D^{s(I)}) \cap B(c(J), 16 D^{s(J)}) \ne \emptyset$.
- id `r118`: lemma; steps here: state and prove. If $\fp \in \fT(\fu_2) \setminus \mathfrak{S}$ and $J \in \mathcal{J'}$ with $B(\scI(\fp)) \cap B(J) \ne \emptyset$, then $$ \ps(\fp) \le s(J) + 2 - \frac{Zn}{202a^3}\,. $$
- id `r506`: lemma; steps here: state and prove. We have for all bounded $f$ with bounded support $$ \|P_{\mathcal{J}'}|T_{\fT(\fu_2) \setminus \mathfrak{S}}^* g_2|\|_2 \le 2^{102a^3+21a+5} 2^{-\frac{25}{101a}Zn\kappa} \|\mathbf{1}_{\scI(\fu_1)} M_{\mathcal{B},1} |g_2|\|_2 $$
- id `r249`: lemma; steps here: state and prove. For all $\fu \in \fU$, all $L \in \mathcal{L}(\fT(\fu))$, all $x, x' \in L$ and all bounded $f$ with bounded support, we have $$ [another result] \le 10 \cdot 2^{104a^3} M_{\mathcal{B}, 1}P_{\mathcal{J}(\fT(\fu))}|f|(x')\,. $$
- id `r136`: lemma; steps here: state and prove. If $J, J' \in \mathcal{J'}$ with $$ B(J) \cap B(J') \ne \emptyset\,, $$ then $|s(J) - s(J')| \le 1$.
- id `r836`: lemma; steps here: state and prove. For all bounded $f$ with bounded support and all $\mfa \in \Mf$ $$ \|T_{\mathcal{N}}^{\mfa} f\|_2 \le 2^{102a^3} \|f\|_2\,. $$
- id `r264`: lemma; steps here: state and prove. For all $\fu \in \fU$ and all bounded functions $f$ with bounded support \begin{equation} \|S_{1,\fu}f\|_2 \le 2^{12a} \|f\|_2\,. \end{equation}
- id `r556`: lemma; steps here: state and prove. Let $\fp \in \fT(\fu_2) \setminus \mathfrak{S}$, $J \in \mathcal{J}'$ and suppose that $$ B(\scI(\fp)) \cap B^\circ(J) \ne \emptyset\,. $$ Then $$ s(J) \le \ps(\fp) \le s(J) +3\,. $$
- id `r821`: lemma; steps here: state and prove. Let $(\fU, \fT)$ be an $n$-forest. Then there exists a decomposition $$ \fU = \dot{\bigcup_{1 \le j \le 2^n}} \fU_j $$ such that for all $j = 1, \dotsc, 2^n$ the pair $(\fU_j, \fT|_{\fU_j})$ is an $n$-row.
- id `r618`: lemma; steps here: state and prove. For each $\fu \in \fU$, we have $$ \sigma(\fu, x) = \mathbb{Z} \cap [\underline{\sigma} (\fu, x), \overline{\sigma} (\fu, x)]\,. $$
- id `r794`: lemma; steps here: state and prove. Let $\fC = \fT(\fu_1)$ or $\fC = \fT(\fu_2) \cap \mathfrak{S}$. Then for each $J \in \mathcal{J}'$ and $\fp \in \fC$ with $B(\scI(\fp)) \cap B'(J) \neq \emptyset$, we have $\ps(\fp) \ge s(J)$.
- id `r536`: lemma; steps here: state and prove. Let $\fu \in \fU$ and $L \in \mathcal{L}(\fT(\fu))$. Let $x, x' \in L$. Then for all bounded functions $f$ with bounded support $$ \left|\sum_{\fp \in \fT(\fu)} T_{\fp}[ e(-\fcc(\fu))f](x)\right| $$ \begin{equation} \leq 2^{129a^3}(M_{\mathcal{B},1}+S_{1,\fu})P_{\mathcal{J}(\fT(\fu))}|f|(x')+|T_{\mathcal{N}}^{\fcc(\fu)} P_{\mathcal{J}(\fT(\fu))}f(x')|, \end{equation}
- id `r657`: lemma; steps here: state and prove. The sets $E_j$, $1 \le j \le 2^n$ are pairwise disjoint.
- id `r952`: lemma; steps here: state and prove. For all $J \in \mathcal{J}'$ and all bounded $g$ with bounded support $$ \sup_{B^\circ{}(J)} |T_{\mathfrak{T}(\mathfrak{u}_2)\setminus\mathfrak{S}}^* g| \le 2^{104a^3} \inf_J M_{\mathcal{B},1}|g| $$
- id `r325`: lemma; steps here: state and prove. For each $1 \le j \le 2^n$ and each bounded $g$ supported on $G$ we have \begin{equation} \left\| T_{\mathfrak{R}_j}^*g \right\|_2 \le 2^{182a^3} 2^{-n/2} \|g\|_2 \end{equation} and \begin{equation} \left\| \mathbf{1}_F T_{\mathfrak{R}_j}^*g \right\|_2 \le 2^{283a^3} 2^{-n/2} \dens_2(\bigcup_{\fu\in \fU}\fT(\fu))^{1/2} \|g\|_2\,. \end{equation}
- id `r745`: lemma; steps here: state and prove. For any $\fu_1 \ne \fu_2 \in \fU$ and all bounded $g_1, g_2$ with bounded support, we have \begin{equation} \left| \int_X \sum_{\fp_1 \in \fT(\fu_1)} \sum_{\fp_2 \in \fT(\fu_2)} T^*_{\fp_1}g_1 \overline{T^*_{\fp_2}g_2 }\,\mathrm{d}\mu \right| \end{equation} \begin{equation} \le 2^{512a^3-4n} \prod_{j =1}^2 \| S_{2, \fu_j} g_j\|_{L^2(\scI(\fu_1) \cap \scI(\fu_2))}\,. \end{equation}
- id `r916`: lemma; steps here: state and prove. For all $\fu \in \fU$, all $L \in \mathcal{L}(\fT(\fu))$, all $x, x' \in L$ and all bounded $f$ with bounded support, we have \begin{equation*} \Bigg| \sum_{s \in \sigma(\fu, x)} \int K_s(x,y) (f(y) - P_{\mathcal{J}(\fT(\fu))} f(y)) \, \mathrm{d}\mu(y) \Bigg| \end{equation*} \begin{equation*} \le 2^{128a^3} S_{1,\fu} P_{\mathcal{J}(\fT(\fu))}|f|(x')\,. \end{equation*}
- id `r811`: proposition; steps here: prove only (it was stated in an earlier section). For any $n\ge 0$ and any $n$-forest $(\fU,\fT)$ we have for all $f,g: X \to \mathbb{C}$ with $|f| \le \mathbf{1}_F$ and $|g| \le \mathbf{1}_G$ $$ | \int \overline{g(x)} \sum_{\fu\in \fU} \sum_{\fp\in \fT(\fu)} T_{\fp} f(x) \, \mathrm{d}\mu(x)| $$ $$ \le 2^{440a^3}2^{-\frac{q-1}{q} n} \dens_2\left(\bigcup_{\fu\in \fU}\fT(\fu)\right)^{\frac{1}{q}-\frac{1}{2}} \|f\|_2 \|g\|_2 \,. $$
- id `r628`: lemma; steps here: state and prove. Let $\fu \in \fU$ and $L \in \mathcal{L}(\fT(\fu))$. Then \begin{equation} \mu(L \cap G \cap \bigcup_{\fp \in \fT(\fu)} E(\fp)) \le 2^{101a^3} \dens_1(\fT(\fu)) \mu(L)\,. \end{equation}
- id `r561`: lemma; steps here: state and prove. For all bounded $g$ supported on $G$ we have that $$ \left\| \sum_{\fp \in \fT(\fu)} T_{\fp}^* g\right\|_2 \le 2^{181a^3} \dens_1(\fT(\fu))^{1/2} \|g\|_2\,, $$ $$ \left\| \mathbf{1}_F \sum_{\fp \in \fT(\fu)} T_{\fp}^* g\right\|_2 \le 2^{282a^3} \dens_1(\fT(\fu))^{1/2} \dens_2(\fT(\fu))^{1/2} \|g\|_2\,. $$
- id `r328`: lemma; steps here: state and prove. For each $\mathfrak{S} \subset \fP$, we have \begin{equation} \bigcup_{I \in \mathcal{D}} I = \dot{\bigcup_{J \in \mathcal{J}(\mathfrak{S})}} J \end{equation} and \begin{equation} \bigcup_{I \in \mathcal{D}} I = \dot{\bigcup_{L \in \mathcal{L}(\mathfrak{S})}} L\,. \end{equation}
- id `r636`: lemma; steps here: state and prove. We have for all $J \in \mathcal{J}'$ and all bounded $g$ with bounded support $$ \sup_{B'(J)} |T^*_{\fT(\fu_2) \cap \mathfrak{S}} g| \le \inf_{B^\circ{}(J)} |T^*_{\fT(\fu_2)} g| + 2^{129a^3} \inf_{J} M_{\mathcal{B},1}|g|\,. $$
- id `r764`: lemma; steps here: state and prove. There exists a family of functions $\chi_J$, $J \in \mathcal{J}'$ such that \begin{equation} \mathbf{1}_{\scI(\fu_1)} = \sum_{J \in \mathcal{J}'} \chi_J\,, \end{equation} and for all $J \in \mathcal{J}'$ and all $y,y' \in \scI(\fu_1)$ \begin{equation} 0 \leq \chi_J(y) \leq \mathbf{1}_{B(J)}(y)\,, \end{equation} \begin{equation} |\chi_J(y) - \chi_J(y')| \le 2^{227a^3} \frac{\rho(y,y')}{D^{s(J)}}\,. \end{equation}
- id `r131`: lemma; steps here: state and prove. For each $J \in \mathcal{J}'$ and all $s$, we have $$ \frac{1}{\mu(J)} \int_J \Bigg(\sum_{\substack{I \in \mathcal{D}, s(I) = s(J) - s\\ I \cap \scI(\fu_1) = \emptyset\\ J \cap B(I) \ne \emptyset}} \mathbf{1}_{B(I)}\bigg)^2 \, \mathrm{d}\mu \le 2^{14a+1} (8 D^{-s})^\kappa\,. $$

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:r118` before `P:r506`
- `S:r121` before `P:r811`
- `S:r131` before `P:r506`
- `S:r136` before `P:r764`
- `S:r211` before `P:r451`
- `S:r211` before `P:r636`
- `S:r249` before `P:r536`
- `S:r264` before `P:r495`
- `S:r292` before `P:r561`
- `S:r314` before `P:r531`
- `S:r314` before `P:r764`
- `S:r325` before `P:r811`
- `S:r328` before `P:r249`
- `S:r328` before `P:r264`
- `S:r328` before `P:r292`
- `S:r328` before `P:r314`
- `S:r328` before `P:r359`
- `S:r328` before `P:r364`
- `S:r328` before `P:r495`
- `S:r328` before `P:r916`
- `S:r330` before `P:r264`
- `S:r359` before `P:r364`
- `S:r359` before `P:r506`
- `S:r364` before `P:r745`
- `S:r419` before `P:r531`
- `S:r451` before `P:r531`
- `S:r495` before `P:r292`
- `S:r495` before `P:r364`
- `S:r506` before `P:r364`
- `S:r531` before `P:r745`
- `S:r536` before `P:r495`
- `S:r542` before `P:r211`
- `S:r556` before `P:r952`
- `S:r561` before `P:r325`
- `S:r561` before `P:r936`
- `S:r618` before `P:r720`
- `S:r622` before `P:r211`
- `S:r622` before `P:r325`
- `S:r622` before `P:r364`
- `S:r622` before `P:r451`
- `S:r622` before `P:r506`
- `S:r622` before `P:r531`
- `S:r622` before `P:r542`
- `S:r622` before `P:r745`
- `S:r622` before `P:r952`
- `S:r628` before `P:r292`
- `S:r636` before `P:r451`
- `S:r657` before `P:r811`
- `S:r720` before `P:r536`
- `S:r745` before `P:r121`
- `S:r764` before `P:r451`
- `S:r764` before `P:r531`
- `S:r794` before `P:r211`
- `S:r821` before `P:r121`
- `S:r821` before `P:r325`
- `S:r821` before `P:r811`
- `S:r821` before `S:r657`
- `S:r836` before `P:r495`
- `S:r847` before `P:r292`
- `S:r915` before `P:r314`
- `S:r915` before `P:r419`
- `S:r915` before `P:r506`
- `S:r915` before `P:r556`
- `S:r915` before `P:r794`
- `S:r916` before `P:r536`
- `S:r936` before `P:r121`
- `S:r952` before `P:r636`
