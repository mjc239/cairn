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

- id `rhoplus-def`: definition (Rho plus); steps here: state only (no proof needed). For any $G$-valued random variable $X$, we define $\rho^+(X) := \rho^-(X) + \bbH(X) - \bbH(U_A)$.
- id `rho-sums-sym`: lemma (Rho and sums, symmetrized); steps here: state and prove. If $X,Y$ are independent, then $$ \rho(X+Y) \leq \frac{1}{2}(\rho(X)+\rho(Y) + d[X;Y]).$$
- id `kl-div-convex`: lemma (Convexity of Kullback--Leibler); steps here: state and prove. If $S$ is a finite set, $\sum_{s \in S} w_s = 1$ for some non-negative $w_s$, and ${\bf P}(X=x) = \sum_{s\in S} w_s {\bf P}(X_s=x)$, ${\bf P}(Y=x) = \sum_{s\in S} w_s {\bf P}(Y_s=x)$ for all $x$, then $$D_{KL}(X\Vert Y) \le \sum_{s\in S} w_s D_{KL}(X_s\Vert Y_s).$$
- id `phi-minimizer-zero-distance`: proposition; steps here: state and prove. If $X_1,X_2$ is a $\phi$-minimizer, then $d[X_1;X_2] = 0$.
- id `rho-BSG-triplet-symmetrized`: lemma; steps here: state and prove. If $G$-valued random variables $T_1,T_2,T_3$ satisfy $T_1+T_2+T_3=0$, then $$d[X_1;X_2] \leq \sum_{1 \leq i<j \leq 3} \bbI[T_i:T_j] + \frac{\eta}{3} \sum_{1 \leq i<j \leq 3} (\rho(T_i|T_j) + \rho(T_j|T_i) -\rho(X_1)-\rho(X_2))$$
- id `rho-cond-relabeled`: lemma (Conditional rho and relabeling); steps here: state and prove. If $f$ is injective, then $\rho(X|f(Y))=\rho(X|Y)$.
- id `rho-subgroup`: lemma (Rho of subgroup); steps here: state and prove. If $H$ is a finite subgroup of $G$, and $\rho(U_H) \leq r$, then there exists $t$ such that $|A \cap (H+t)| \geq e^{-r} \sqrt{|A||H|}$, and $|H|/|A|\in[e^{-2r},e^{2r}]$.
- id `phi-first-estimate`: lemma; steps here: state and prove. $I_1\le 2\eta d[X_1;X_2]$
- id `rho-increase-symmetrized`: lemma; steps here: state and prove. For independent random variables $Y_1,Y_2,Y_3,Y_4$ over $G$, define $T_1:=Y_1+Y_2,T_2:=Y_1+Y_3,T_3:=Y_2+Y_3$ and $S:=Y_1+Y_2+Y_3+Y_4$. Then $$\sum_{1 \leq i<j \leq 3} (\rho(T_i|T_j,S) + \rho(T_j|T_i,S) - \frac{1}{2}\sum_{i} \rho(Y_i))\le \sum_{1\leq i < j \leq 4}d[Y_i;Y_j]$$
- id `phi-second-estimate`: lemma; steps here: state and prove. $I_2\le 2\eta d[X_1;X_2] + \frac{\eta}{1-\eta}(2\eta d[X_1;X_2]-I_1)$.
- id `I1-I2-diff`: lemma; steps here: state and prove. $d[X_1;X_1]+d[X_2;X_2]= 2d[X_1;X_2]+(I_2-I_1)$.
- id `phi-min-def`: definition; steps here: state only (no proof needed). Given $G$-valued random variables $X,Y$, define $$ \phi[X;Y] := d[X;Y] + \eta(\rho(X) + \rho(Y))$$ and define a \emph{$\phi$-minimizer} to be a pair of random variables $X,Y$ which minimizes $\phi[X;Y]$.
- id `rho-cts`: lemma (Rho continuous); steps here: state and prove. $\rho(X)$ depends continuously on the distribution of $X$.
- id `rho-BSG-triplet`: lemma; steps here: state and prove. If $G$-valued random variables $T_1,T_2,T_3$ satisfy $T_1+T_2+T_3=0$, then $$d[X_1;X_2]\le 3\bbI[T_1:T_2] + (2\bbH[T_3]-\bbH[T_1]-\bbH[T_2])+ \eta(\rho(T_1|T_3)+\rho(T_2|T_3)-\rho(X_1)-\rho(X_2)).$$
- id `kl-div-inj`: lemma (Kullback--Leibler and injections); steps here: state and prove. If $f:G \to H$ is an injection, then $D_{KL}(f(X)\Vert f(Y)) = D_{KL}(X\Vert Y)$.
- id `rhominus-def`: definition (Rho minus); steps here: state only (no proof needed). For any $G$-valued random variable $X$, we define $\rho^-(X)$ to be the infimum of $D_{KL}(X \Vert U_A + T)$, where $U_A$ is uniform on $A$ and $T$ ranges over $G$-valued random variables independent of $U_A$.
- id `rho-cond-def`: definition (Conditional Rho functional); steps here: state only (no proof needed). We define $\rho(X|Y) := \sum_y {\bf P}(Y=y) \rho(X|Y=y)$.
- id `rho-increase`: lemma; steps here: state and prove. For independent random variables $Y_1,Y_2,Y_3,Y_4$ over $G$, define $S:=Y_1+Y_2+Y_3+Y_4$, $T_1:=Y_1+Y_2$, $T_2:=Y_1+Y_3$. Then $$\rho(T_1|T_2,S)+\rho(T_2|T_1,S) - \frac{1}{2}\sum_{i} \rho(Y_i)\le \frac{1}{2}(d[Y_1;Y_2]+d[Y_3;Y_4]+d[Y_1;Y_3]+d[Y_2;Y_4]).$$
- id `pfr-9-aux`: corollary; steps here: state and prove. If $|A+A| \leq K|A|$, then there exists a subgroup $H$ and $t\in G$ such that $|A \cap (H+t)| \geq K^{-4} \sqrt{|A||H|}$, and $|H|/|A|\in[K^{-8},K^8]$.
- id `Conditional-Gibbs`: lemma (Conditional Gibbs inequality); steps here: state and prove. $D_{KL}((X|W)\Vert Y) \geq 0$.
- id `Gibbs-converse`: lemma (Converse Gibbs inequality); steps here: state and prove. If $D_{KL}(X\Vert Y) = 0$, then $Y$ is a copy of $X$.
- id `rho-cond-invariant`: lemma (Conditional rho and translation); steps here: state and prove. For any $s\in G$, $\rho(X+s|Y)=\rho(X|Y)$.
- id `rho-def`: definition (Rho functional); steps here: state only (no proof needed). We define $\rho(X) := (\rho^+(X) + \rho^-(X))/2$.
- id `rho-sums`: lemma (Rho and sums); steps here: state and prove. If $X,Y$ are independent, one has $$ \rho^-(X+Y) \leq \rho^-(X)$$ $$ \rho^+(X+Y) \leq \rho^+(X) + \bbH[X+Y] - \bbH[X]$$ and $$ \rho(X+Y) \leq \rho(X) + \frac{1}{2}( \bbH[X+Y] - \bbH[X] ).$$
- id `kl-div`: definition (Kullback--Leibler divergence); steps here: state only (no proof needed). If $X,Y$ are two $G$-valued random variables, the Kullback--Leibler divergence is defined as $$ D_{KL}(X\Vert Y) := \sum_x \mathbf{P}(X=x) \log \frac{\mathbf{P}(X=x)}{\mathbf{P}(Y=x)}.$$
- id `rho-cond`: lemma (Rho and conditioning); steps here: state and prove. If $X,Z$ are defined on the same space, one has $$ \rho^-(X|Z) \leq \rho^-(X) + \bbH[X] - \bbH[X|Z]$$ $$ \rho^+(X|Z) \leq \rho^+(X)$$ and $$ \rho(X|Z) \leq \rho(X) + \frac{1}{2}( \bbH[X] - \bbH[X|Z] ).$$
- id `pfr-rho`: proposition; steps here: state and prove. For any random variables $Y_1,Y_2$, there exist a subgroup $H$ such that $$ 2\rho(U_H) \leq \rho(Y_1) + \rho(Y_2) + 8 d[Y_1;Y_2].$$
- id `phi-min-exist`: lemma ($\phi$-minimizers exist); steps here: state and prove. There exists a $\phi$-minimizer.
- id `pfr-9`: theorem (PFR with \texorpdfstring{$C=9$}{C=9}); steps here: state and prove. If $A \subset {\bf F}_2^n$ is finite non-empty with $|A+A| \leq K|A|$, then there exists a subgroup $H$ of ${\bf F}_2^n$ with $|H| \leq |A|$ such that $A$ can be covered by at most $2K^9$ translates of $H$.
- id `kl-sums`: lemma (Kullback--Leibler and sums); steps here: state and prove. If $X, Y, Z$ are independent $G$-valued random variables, then $$D_{KL}(X+Z\Vert Y+Z) \leq D_{KL}(X\Vert Y).$$
- id `rho-invariant`: lemma (Rho invariant); steps here: state and prove. For any $s \in G$, $\rho(X+s) = \rho(X)$.
- id `pfr-9-aux'`: corollary; steps here: state and prove. If $|A+A| \leq K|A|$, then there exist a subgroup $H$ and a subset $c$ of $G$ with $A \subseteq c + H$, such that $|c| \leq K^{5} |A|^{1/2}/|H|^{1/2}$ and $|H|/|A|\in[K^{-8},K^8]$.
- id `rhominus-subgroup`: lemma (Rho minus of subgroup); steps here: state and prove. If $H$ is a finite subgroup of $G$, then $\rho^-(U_H) = \log |A| - \log \max_t |A \cap (H+t)|$.
- id `rhoplus-subgroup`: corollary (Rho plus of subgroup); steps here: state and prove. If $H$ is a finite subgroup of $G$, then $\rho^+(U_H) = \log |H| - \log \max_t |A \cap (H+t)|$.
- id `kl-div-copy`: lemma (Kullback--Leibler divergence of copy); steps here: state and prove. If $X'$ is a copy of $X$, and $Y'$ is a copy of $Y$, then $D_{KL}(X'\Vert Y') = D_{KL}(X\Vert Y)$.
- id `Gibbs`: lemma (Gibbs inequality); steps here: state and prove. $D_{KL}(X\Vert Y) \geq 0$.
- id `kl-cond`: lemma (Kullback--Leibler and conditioning); steps here: state and prove. If $X, Y$ are independent $G$-valued random variables, and $Z$ is another random variable defined on the same sample space as $X$, then $$D_{KL}((X|Z)\Vert Y) = D_{KL}(X\Vert Y) + \bbH[X] - \bbH[X|Z].$$
- id `rho-cond-sym`: lemma (Rho and conditioning, symmetrized); steps here: state and prove. If $X,Y$ are independent, then $$ \rho(X | X+Y) \leq \frac{1}{2}(\rho(X)+\rho(Y) + d[X;Y]).$$

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:Gibbs` before `P:Conditional-Gibbs`
- `S:Gibbs` before `P:pfr-9-aux`
- `S:Gibbs` before `P:rho-cond`
- `S:Gibbs` before `P:rho-cts`
- `S:Gibbs` before `P:rho-subgroup`
- `S:Gibbs` before `P:rho-sums`
- `S:Gibbs` before `P:rhominus-subgroup`
- `S:I1-I2-diff` before `P:phi-minimizer-zero-distance`
- `S:I1-I2-diff` before `P:phi-second-estimate`
- `S:kl-cond` before `P:rho-cond`
- `S:kl-div` before `P:pfr-9-aux`
- `S:kl-div` before `P:pfr-rho`
- `S:kl-div` before `P:phi-first-estimate`
- `S:kl-div` before `P:phi-min-exist`
- `S:kl-div` before `P:phi-minimizer-zero-distance`
- `S:kl-div` before `P:phi-second-estimate`
- `S:kl-div` before `P:rho-BSG-triplet`
- `S:kl-div` before `P:rho-cond`
- `S:kl-div` before `P:rho-cond-sym`
- `S:kl-div` before `P:rho-cts`
- `S:kl-div` before `P:rho-increase`
- `S:kl-div` before `P:rho-subgroup`
- `S:kl-div` before `P:rho-sums`
- `S:kl-div` before `P:rhominus-subgroup`
- `S:kl-div` before `S:Conditional-Gibbs`
- `S:kl-div` before `S:Gibbs`
- `S:kl-div` before `S:Gibbs-converse`
- `S:kl-div` before `S:kl-cond`
- `S:kl-div` before `S:kl-div-convex`
- `S:kl-div` before `S:kl-div-copy`
- `S:kl-div` before `S:kl-div-inj`
- `S:kl-div` before `S:kl-sums`
- `S:kl-div` before `S:rhominus-def`
- `S:kl-div-convex` before `P:kl-sums`
- `S:kl-div-copy` before `P:pfr-rho`
- `S:kl-div-copy` before `P:phi-first-estimate`
- `S:kl-div-copy` before `P:phi-min-exist`
- `S:kl-div-copy` before `P:phi-minimizer-zero-distance`
- `S:kl-div-copy` before `P:phi-second-estimate`
- `S:kl-div-copy` before `P:rho-BSG-triplet`
- `S:kl-div-copy` before `P:rho-cond-sym`
- `S:kl-div-copy` before `P:rho-increase`
- `S:kl-div-copy` before `P:rho-sums`
- `S:kl-div-inj` before `P:kl-sums`
- `S:kl-sums` before `P:rho-sums`
- `S:pfr-9-aux` before `P:pfr-9-aux'`
- `S:pfr-9-aux'` before `P:pfr-9`
- `S:pfr-rho` before `P:pfr-9-aux`
- `S:phi-first-estimate` before `P:phi-minimizer-zero-distance`
- `S:phi-min-def` before `P:pfr-rho`
- `S:phi-min-def` before `S:phi-first-estimate`
- `S:phi-min-def` before `S:phi-min-exist`
- `S:phi-min-def` before `S:phi-minimizer-zero-distance`
- `S:phi-min-def` before `S:phi-second-estimate`
- `S:phi-min-def` before `S:rho-BSG-triplet`
- `S:phi-min-def` before `S:rho-BSG-triplet-symmetrized`
- `S:phi-min-exist` before `P:pfr-rho`
- `S:phi-minimizer-zero-distance` before `P:pfr-rho`
- `S:phi-second-estimate` before `P:phi-minimizer-zero-distance`
- `S:rho-BSG-triplet` before `P:phi-minimizer-zero-distance`
- `S:rho-BSG-triplet` before `P:rho-BSG-triplet-symmetrized`
- `S:rho-cond` before `P:rho-cond-sym`
- `S:rho-cond` before `P:rho-increase`
- `S:rho-cond-def` before `P:phi-first-estimate`
- `S:rho-cond-def` before `P:phi-minimizer-zero-distance`
- `S:rho-cond-def` before `P:phi-second-estimate`
- `S:rho-cond-def` before `S:rho-BSG-triplet`
- `S:rho-cond-def` before `S:rho-BSG-triplet-symmetrized`
- `S:rho-cond-def` before `S:rho-cond`
- `S:rho-cond-def` before `S:rho-cond-invariant`
- `S:rho-cond-def` before `S:rho-cond-relabeled`
- `S:rho-cond-def` before `S:rho-cond-sym`
- `S:rho-cond-def` before `S:rho-increase`
- `S:rho-cond-def` before `S:rho-increase-symmetrized`
- `S:rho-cond-relabeled` before `P:rho-increase`
- `S:rho-cond-sym` before `P:phi-first-estimate`
- `S:rho-cond-sym` before `P:phi-second-estimate`
- `S:rho-cond-sym` before `P:rho-increase`
- `S:rho-cts` before `P:pfr-rho`
- `S:rho-cts` before `P:phi-min-exist`
- `S:rho-def` before `P:pfr-9-aux`
- `S:rho-def` before `P:phi-first-estimate`
- `S:rho-def` before `P:phi-min-exist`
- `S:rho-def` before `P:phi-minimizer-zero-distance`
- `S:rho-def` before `P:phi-second-estimate`
- `S:rho-def` before `P:rho-cond-invariant`
- `S:rho-def` before `P:rho-cond-relabeled`
- `S:rho-def` before `S:pfr-rho`
- `S:rho-def` before `S:phi-min-def`
- `S:rho-def` before `S:rho-BSG-triplet`
- `S:rho-def` before `S:rho-BSG-triplet-symmetrized`
- `S:rho-def` before `S:rho-cond`
- `S:rho-def` before `S:rho-cond-def`
- `S:rho-def` before `S:rho-cond-sym`
- `S:rho-def` before `S:rho-cts`
- `S:rho-def` before `S:rho-increase`
- `S:rho-def` before `S:rho-increase-symmetrized`
- `S:rho-def` before `S:rho-invariant`
- `S:rho-def` before `S:rho-subgroup`
- `S:rho-def` before `S:rho-sums`
- `S:rho-def` before `S:rho-sums-sym`
- `S:rho-increase` before `P:rho-increase-symmetrized`
- `S:rho-increase-symmetrized` before `P:phi-minimizer-zero-distance`
- `S:rho-invariant` before `P:pfr-rho`
- `S:rho-invariant` before `P:rho-cond-invariant`
- `S:rho-invariant` before `P:rho-cond-sym`
- `S:rho-subgroup` before `P:pfr-9-aux`
- `S:rho-sums` before `P:rho-invariant`
- `S:rho-sums` before `P:rho-sums-sym`
- `S:rho-sums-sym` before `P:phi-first-estimate`
- `S:rho-sums-sym` before `P:phi-second-estimate`
- `S:rho-sums-sym` before `P:rho-increase`
- `S:rhominus-def` before `P:pfr-9-aux`
- `S:rhominus-def` before `P:pfr-rho`
- `S:rhominus-def` before `P:phi-first-estimate`
- `S:rhominus-def` before `P:phi-min-exist`
- `S:rhominus-def` before `P:phi-minimizer-zero-distance`
- `S:rhominus-def` before `P:phi-second-estimate`
- `S:rhominus-def` before `P:rho-BSG-triplet`
- `S:rhominus-def` before `P:rho-cond-sym`
- `S:rhominus-def` before `P:rho-cts`
- `S:rhominus-def` before `P:rho-increase`
- `S:rhominus-def` before `P:rhoplus-subgroup`
- `S:rhominus-def` before `S:rho-cond`
- `S:rhominus-def` before `S:rho-def`
- `S:rhominus-def` before `S:rho-subgroup`
- `S:rhominus-def` before `S:rho-sums`
- `S:rhominus-def` before `S:rhominus-subgroup`
- `S:rhominus-def` before `S:rhoplus-def`
- `S:rhominus-subgroup` before `P:rho-subgroup`
- `S:rhominus-subgroup` before `P:rhoplus-subgroup`
- `S:rhoplus-def` before `P:pfr-9-aux`
- `S:rhoplus-def` before `P:pfr-rho`
- `S:rhoplus-def` before `P:phi-first-estimate`
- `S:rhoplus-def` before `P:phi-min-exist`
- `S:rhoplus-def` before `P:phi-minimizer-zero-distance`
- `S:rhoplus-def` before `P:phi-second-estimate`
- `S:rhoplus-def` before `P:rho-BSG-triplet`
- `S:rhoplus-def` before `P:rho-cond-sym`
- `S:rhoplus-def` before `P:rho-cts`
- `S:rhoplus-def` before `P:rho-increase`
- `S:rhoplus-def` before `P:rho-subgroup`
- `S:rhoplus-def` before `S:rho-cond`
- `S:rhoplus-def` before `S:rho-def`
- `S:rhoplus-def` before `S:rho-sums`
- `S:rhoplus-def` before `S:rhoplus-subgroup`
- `S:rhoplus-subgroup` before `P:rho-subgroup`
