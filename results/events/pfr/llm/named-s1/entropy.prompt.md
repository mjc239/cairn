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

- id `conditional-mutual-alt`: lemma (Alternate formula for conditional mutual information); steps here: state and prove. We have $$ \bbI[X:Y|Z] := \bbH[X|Z] + \bbH[Y|Z] - \bbH[X,Y|Z]$$ and $$ \bbI[X:Y|Z] := \bbH[X|Z] - \bbH[X|Y,Z].$$
- id `conditional-vanish`: lemma (Vanishing conditional mutual information); steps here: state and prove. If $X,Y,Z$ are random variables, then $\bbI[X:Y|Z] = 0$ iff $X,Y$ are conditionally independent over $Z$.
- id `chain-rule`: lemma (Chain rule); steps here: state and prove. If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, then $$ \bbH[X, Y] = \bbH[Y] + \bbH[X|Y].$$
- id `relabeled-entropy-cond`: lemma (Conditional entropy and relabeling); steps here: state and prove. If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, and $Y = f(X,Z)$ almost surely for some map $f: S \times U \to T$ that is injective for each fixed $U$, then $\bbH[X|Z] = \bbH[Y|Z]$. Similarly, if $g: T \to U$ is injective, then $\bbH[X|g(Y)] = \bbH[X|Y]$.
- id `conditional-mutual-def`: definition (Conditional mutual information); steps here: state only (no proof needed). If $X,Y,Z$ are random variables, with $Z$ $U$-valued, then $$ \bbI[X:Y|Z] := \sum_{z \in U} P[Z=z] \bbI[(X|Z=z): (Y|Z=z)].$$
- id `relabeled-entropy`: lemma (Entropy and relabeling); steps here: state and prove. \begin{itemize} \item[(i)] If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ for some injection $f: S \to T$, then $\bbH[X] = \bbH[Y]$. \item[(ii)] If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ and $X = g(Y)$ for some functions $f: S \to T$, $g: T \to S$, then $\bbH[X] = \bbH[Y]$. \end{itemize}
- id `uniform-entropy`: lemma (Entropy of uniform random variable); steps here: state and prove. If $X$ is $S$-valued random variable, then $\bbH[X] = \log |S|$ if and only if $X$ is uniformly distributed on $S$.
- id `cond-trial-ent`: corollary (Entropy of conditionally independent variables); steps here: state and prove. If $X, Y$ are conditionally independent over $Z$, then $$ \bbH[X,Y,Z] =\bbH[X,Z] + \bbH[Y,Z] - \bbH[Z].$$
- id `alt-submodularity`: corollary (Alternate form of submodularity); steps here: state and prove. With three random variables $X,Y,Z$, one has $$ \bbH[X,Y,Z] + \bbH[Z] \leq \bbH[X,Z] + \bbH[Y,Z].$$
- id `information-def`: definition (Mutual information); steps here: state only (no proof needed). If $X: \Omega \to S$, $Y: \Omega \to T$ are random variables, then $$\bbI[X : Y] := \bbH[X] + \bbH[Y] - \bbH[X,Y].$$
- id `conditional-entropy-def`: definition (Conditional entropy); steps here: state only (no proof needed). If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, the conditional entropy $\bbH[X|Y]$ is defined as $$ \bbH[X|Y] := \sum_{y \in Y} \bbP[Y = y] \bbH[(X | Y=y)].$$
- id `cond-reduce`: corollary (Conditioning reduces entropy); steps here: state and prove. With notation as above, we have $\bbH[X|Y] \leq \bbH[X]$.
- id `subadditive`: corollary (Subadditivity); steps here: state and prove. With notation as above, we have $\bbH[X,Y] \leq \bbH[X] + \bbH[Y]$.
- id `entropy-def`: definition (Entropy); steps here: state only (no proof needed). If $X$ is an $S$-valued random variable, the entropy $\bbH[X]$ of $X$ is defined $$ \bbH[X] := \sum_{s \in S} \bbP[X=x] \log \frac{1}{\bbP[X=x]}$$ with the convention that $0 \log \frac{1}{0} = 0$.
- id `bound-conc`: lemma (Bounded entropy implies concentration); steps here: state and prove. If $X$ is an $S$-valued random variable, then there exists $s \in S$ such that $\bbP[X=s] \geq \exp(-\bbH[X])$.
- id `add-entropy`: corollary (Additivity of entropy); steps here: state and prove. If $X,Y$ are random variables, then $\bbH[X,Y] = \bbH[X] + \bbH[Y]$ if and only if $X,Y$ are independent.
- id `uniform-entropy-II`: lemma (Entropy of uniform random variable, II); steps here: state and prove. If $X$ is uniformly distributed on $H$, then, then $\bbH[X] = \log |H|$.
- id `conditional-chain-rule`: lemma (Conditional chain rule); steps here: state and prove. If $X: \Omega \to S$, $Y: \Omega \to T$, $Z: \Omega \to U$ are random variables, then $$ \bbH[X, Y | Z] = \bbH[Y | Z] + \bbH[X|Y, Z].$$
- id `vanish-entropy`: lemma (Vanishing of mutual information); steps here: state and prove. If $X,Y$ are random variables, then $\bbI[X:Y] = 0$ if and only if $X,Y$ are independent.
- id `alternative-mutual`: lemma (Alternative formulae for mutual information); steps here: state and prove. With notation as above, we have $$ \bbI[X : Y] = \bbI[Y:X]$$ $$ \bbI[X : Y] = \bbH[X] - \bbH[X|Y]$$ $$ \bbI[X : Y] = \bbH[Y] - \bbH[Y|X]$$
- id `mutual-nonneg`: lemma (Nonnegativity of mutual information); steps here: state and prove. We have $\bbI[X:Y] \geq 0$.
- id `uniform-def`: definition (Uniform distribution); steps here: state only (no proof needed). If $H$ is a subset of $S$, an $S$-random variable $X$ is said to be uniformly distributed on $H$ if $\bbP[X = s] = 1/|H|$ for $s \in X$ and $\bbP[X=s] = 0$ otherwise.
- id `entropy-comm`: lemma (Commutativity and associativity of joint entropy); steps here: state and prove. If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, then $\bbH[X, Y] = \bbH[Y, X]$ and $\bbH[X, (Y,Z)] = \bbH[(X,Y), Z]$.
- id `jensen-bound`: lemma (Jensen bound); steps here: state and prove. If $X$ is an $S$-valued random variable, then $\bbH[X] \leq \log |S|$.
- id `conditional-nonneg`: lemma (Nonnegativity of conditional mutual information); steps here: state and prove. If $X,Y,Z$ are random variables, then $\bbI[X:Y|Z] \ge 0$.
- id `conditional-independent-def`: definition (Conditionally independent random variables); steps here: state only (no proof needed). Two random variables $X: \Omega \to S$ and $Y: \Omega \to T$ are conditionally independent relative to another random variable $Z: \Omega \to U$ if $P[X = s \wedge Y = t| Z=u] = P[X=s|Z=u] P[Y=t|Z=u]$ for all $s \in S, t \in T, u \in U$. (We won't need conditional independence for more variables than this.)
- id `submodularity`: corollary (Submodularity); steps here: state and prove. With three random variables $X,Y,Z$, one has $\bbH[X|Y,Z] \leq \bbH[X|Z]$.
- id `unif-exist`: lemma (Uniform distributions exist); steps here: state and prove. Given a finite non-empty subset $H$ of a set $S$, there exists a random variable $X$ (on some probability space) that is uniformly distributed on $H$.

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:chain-rule` before `P:alt-submodularity`
- `S:chain-rule` before `P:alternative-mutual`
- `S:chain-rule` before `P:cond-reduce`
- `S:chain-rule` before `P:cond-trial-ent`
- `S:chain-rule` before `P:relabeled-entropy-cond`
- `S:chain-rule` before `P:submodularity`
- `S:conditional-chain-rule` before `P:conditional-mutual-alt`
- `S:conditional-entropy-def` before `P:alt-submodularity`
- `S:conditional-entropy-def` before `P:cond-trial-ent`
- `S:conditional-entropy-def` before `S:alternative-mutual`
- `S:conditional-entropy-def` before `S:chain-rule`
- `S:conditional-entropy-def` before `S:cond-reduce`
- `S:conditional-entropy-def` before `S:conditional-chain-rule`
- `S:conditional-entropy-def` before `S:conditional-mutual-alt`
- `S:conditional-entropy-def` before `S:relabeled-entropy-cond`
- `S:conditional-entropy-def` before `S:submodularity`
- `S:conditional-independent-def` before `S:cond-trial-ent`
- `S:conditional-independent-def` before `S:conditional-vanish`
- `S:conditional-mutual-alt` before `P:cond-trial-ent`
- `S:conditional-mutual-def` before `P:cond-trial-ent`
- `S:conditional-mutual-def` before `S:conditional-mutual-alt`
- `S:conditional-mutual-def` before `S:conditional-nonneg`
- `S:conditional-mutual-def` before `S:conditional-vanish`
- `S:conditional-vanish` before `P:cond-trial-ent`
- `S:entropy-comm` before `P:alternative-mutual`
- `S:entropy-comm` before `P:chain-rule`
- `S:entropy-comm` before `P:cond-trial-ent`
- `S:entropy-def` before `P:conditional-chain-rule`
- `S:entropy-def` before `P:conditional-mutual-alt`
- `S:entropy-def` before `P:conditional-nonneg`
- `S:entropy-def` before `P:conditional-vanish`
- `S:entropy-def` before `P:mutual-nonneg`
- `S:entropy-def` before `P:relabeled-entropy-cond`
- `S:entropy-def` before `P:submodularity`
- `S:entropy-def` before `P:vanish-entropy`
- `S:entropy-def` before `S:add-entropy`
- `S:entropy-def` before `S:alt-submodularity`
- `S:entropy-def` before `S:alternative-mutual`
- `S:entropy-def` before `S:bound-conc`
- `S:entropy-def` before `S:chain-rule`
- `S:entropy-def` before `S:cond-reduce`
- `S:entropy-def` before `S:cond-trial-ent`
- `S:entropy-def` before `S:conditional-entropy-def`
- `S:entropy-def` before `S:conditional-mutual-def`
- `S:entropy-def` before `S:entropy-comm`
- `S:entropy-def` before `S:information-def`
- `S:entropy-def` before `S:jensen-bound`
- `S:entropy-def` before `S:relabeled-entropy`
- `S:entropy-def` before `S:subadditive`
- `S:entropy-def` before `S:uniform-entropy`
- `S:entropy-def` before `S:uniform-entropy-II`
- `S:information-def` before `P:add-entropy`
- `S:information-def` before `P:cond-reduce`
- `S:information-def` before `P:conditional-vanish`
- `S:information-def` before `S:alternative-mutual`
- `S:information-def` before `S:mutual-nonneg`
- `S:information-def` before `S:vanish-entropy`
- `S:mutual-nonneg` before `P:cond-reduce`
- `S:mutual-nonneg` before `P:conditional-nonneg`
- `S:mutual-nonneg` before `P:conditional-vanish`
- `S:mutual-nonneg` before `P:subadditive`
- `S:relabeled-entropy` before `P:entropy-comm`
- `S:relabeled-entropy` before `P:relabeled-entropy-cond`
- `S:relabeled-entropy` before `P:submodularity`
- `S:relabeled-entropy-cond` before `P:conditional-chain-rule`
- `S:submodularity` before `P:alt-submodularity`
- `S:uniform-def` before `S:unif-exist`
- `S:uniform-def` before `S:uniform-entropy`
- `S:uniform-def` before `S:uniform-entropy-II`
- `S:vanish-entropy` before `P:add-entropy`
- `S:vanish-entropy` before `P:conditional-vanish`
