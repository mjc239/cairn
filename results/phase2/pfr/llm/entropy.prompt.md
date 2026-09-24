You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order.

## Results

- id `uniform-def`: definition (Uniform distribution). If $H$ is a subset of $S$, an $S$-random variable $X$ is said to be uniformly distributed on $H$ if $\bbP[X = s] = 1/|H|$ for $s \in X$ and $\bbP[X=s] = 0$ otherwise.
- id `alternative-mutual`: lemma (Alternative formulae for mutual information). With notation as above, we have $$ \bbI[X : Y] = \bbI[Y:X]$$ $$ \bbI[X : Y] = \bbH[X] - \bbH[X|Y]$$ $$ \bbI[X : Y] = \bbH[Y] - \bbH[Y|X]$$
- id `relabeled-entropy-cond`: lemma (Conditional entropy and relabeling). If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, and $Y = f(X,Z)$ almost surely for some map $f: S \times U \to T$ that is injective for each fixed $U$, then $\bbH[X|Z] = \bbH[Y|Z]$. Similarly, if $g: T \to U$ is injective, then $\bbH[X|g(Y)] = \bbH[X|Y]$.
- id `cond-reduce`: corollary (Conditioning reduces entropy). With notation as above, we have $\bbH[X|Y] \leq \bbH[X]$.
- id `uniform-entropy`: lemma (Entropy of uniform random variable). If $X$ is $S$-valued random variable, then $\bbH[X] = \log |S|$ if and only if $X$ is uniformly distributed on $S$.
- id `entropy-def`: definition (Entropy). If $X$ is an $S$-valued random variable, the entropy $\bbH[X]$ of $X$ is defined $$ \bbH[X] := \sum_{s \in S} \bbP[X=x] \log \frac{1}{\bbP[X=x]}$$ with the convention that $0 \log \frac{1}{0} = 0$.
- id `bound-conc`: lemma (Bounded entropy implies concentration). If $X$ is an $S$-valued random variable, then there exists $s \in S$ such that $\bbP[X=s] \geq \exp(-\bbH[X])$.
- id `add-entropy`: corollary (Additivity of entropy). If $X,Y$ are random variables, then $\bbH[X,Y] = \bbH[X] + \bbH[Y]$ if and only if $X,Y$ are independent.
- id `alt-submodularity`: corollary (Alternate form of submodularity). With three random variables $X,Y,Z$, one has $$ \bbH[X,Y,Z] + \bbH[Z] \leq \bbH[X,Z] + \bbH[Y,Z].$$
- id `submodularity`: corollary (Submodularity). With three random variables $X,Y,Z$, one has $\bbH[X|Y,Z] \leq \bbH[X|Z]$.
- id `conditional-mutual-alt`: lemma (Alternate formula for conditional mutual information). We have $$ \bbI[X:Y|Z] := \bbH[X|Z] + \bbH[Y|Z] - \bbH[X,Y|Z]$$ and $$ \bbI[X:Y|Z] := \bbH[X|Z] - \bbH[X|Y,Z].$$
- id `conditional-independent-def`: definition (Conditionally independent random variables). Two random variables $X: \Omega \to S$ and $Y: \Omega \to T$ are conditionally independent relative to another random variable $Z: \Omega \to U$ if $P[X = s \wedge Y = t| Z=u] = P[X=s|Z=u] P[Y=t|Z=u]$ for all $s \in S, t \in T, u \in U$. (We won't need conditional independence for more variables than this.)
- id `unif-exist`: lemma (Uniform distributions exist). Given a finite non-empty subset $H$ of a set $S$, there exists a random variable $X$ (on some probability space) that is uniformly distributed on $H$.
- id `jensen-bound`: lemma (Jensen bound). If $X$ is an $S$-valued random variable, then $\bbH[X] \leq \log |S|$.
- id `conditional-mutual-def`: definition (Conditional mutual information). If $X,Y,Z$ are random variables, with $Z$ $U$-valued, then $$ \bbI[X:Y|Z] := \sum_{z \in U} P[Z=z] \bbI[(X|Z=z): (Y|Z=z)].$$
- id `uniform-entropy-II`: lemma (Entropy of uniform random variable, II). If $X$ is uniformly distributed on $H$, then, then $\bbH[X] = \log |H|$.
- id `chain-rule`: lemma (Chain rule). If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, then $$ \bbH[X, Y] = \bbH[Y] + \bbH[X|Y].$$
- id `vanish-entropy`: lemma (Vanishing of mutual information). If $X,Y$ are random variables, then $\bbI[X:Y] = 0$ if and only if $X,Y$ are independent.
- id `conditional-entropy-def`: definition (Conditional entropy). If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, the conditional entropy $\bbH[X|Y]$ is defined as $$ \bbH[X|Y] := \sum_{y \in Y} \bbP[Y = y] \bbH[(X | Y=y)].$$
- id `conditional-vanish`: lemma (Vanishing conditional mutual information). If $X,Y,Z$ are random variables, then $\bbI[X:Y|Z] = 0$ iff $X,Y$ are conditionally independent over $Z$.
- id `mutual-nonneg`: lemma (Nonnegativity of mutual information). We have $\bbI[X:Y] \geq 0$.
- id `subadditive`: corollary (Subadditivity). With notation as above, we have $\bbH[X,Y] \leq \bbH[X] + \bbH[Y]$.
- id `entropy-comm`: lemma (Commutativity and associativity of joint entropy). If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, then $\bbH[X, Y] = \bbH[Y, X]$ and $\bbH[X, (Y,Z)] = \bbH[(X,Y), Z]$.
- id `relabeled-entropy`: lemma (Entropy and relabeling). \begin{itemize} \item[(i)] If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ for some injection $f: S \to T$, then $\bbH[X] = \bbH[Y]$. \item[(ii)] If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ and $X = g(Y)$ for some functions $f: S \to T$, $g: T \to S$, then $\bbH[X] = \bbH[Y]$. \end{itemize}
- id `information-def`: definition (Mutual information). If $X: \Omega \to S$, $Y: \Omega \to T$ are random variables, then $$\bbI[X : Y] := \bbH[X] + \bbH[Y] - \bbH[X,Y].$$
- id `conditional-nonneg`: lemma (Nonnegativity of conditional mutual information). If $X,Y,Z$ are random variables, then $\bbI[X:Y|Z] \ge 0$.
- id `conditional-chain-rule`: lemma (Conditional chain rule). If $X: \Omega \to S$, $Y: \Omega \to T$, $Z: \Omega \to U$ are random variables, then $$ \bbH[X, Y | Z] = \bbH[Y | Z] + \bbH[X|Y, Z].$$
- id `cond-trial-ent`: corollary (Entropy of conditionally independent variables). If $X, Y$ are conditionally independent over $Z$, then $$ \bbH[X,Y,Z] =\bbH[X,Z] + \bbH[Y,Z] - \bbH[Z].$$

## Constraints

- `chain-rule` before `alt-submodularity`
- `chain-rule` before `alternative-mutual`
- `chain-rule` before `cond-reduce`
- `chain-rule` before `cond-trial-ent`
- `chain-rule` before `relabeled-entropy-cond`
- `chain-rule` before `submodularity`
- `conditional-chain-rule` before `conditional-mutual-alt`
- `conditional-entropy-def` before `alt-submodularity`
- `conditional-entropy-def` before `alternative-mutual`
- `conditional-entropy-def` before `chain-rule`
- `conditional-entropy-def` before `cond-reduce`
- `conditional-entropy-def` before `cond-trial-ent`
- `conditional-entropy-def` before `conditional-chain-rule`
- `conditional-entropy-def` before `conditional-mutual-alt`
- `conditional-entropy-def` before `relabeled-entropy-cond`
- `conditional-entropy-def` before `submodularity`
- `conditional-independent-def` before `cond-trial-ent`
- `conditional-independent-def` before `conditional-vanish`
- `conditional-mutual-alt` before `cond-trial-ent`
- `conditional-mutual-def` before `cond-trial-ent`
- `conditional-mutual-def` before `conditional-mutual-alt`
- `conditional-mutual-def` before `conditional-nonneg`
- `conditional-mutual-def` before `conditional-vanish`
- `conditional-vanish` before `cond-trial-ent`
- `entropy-comm` before `alternative-mutual`
- `entropy-comm` before `chain-rule`
- `entropy-comm` before `cond-trial-ent`
- `entropy-def` before `add-entropy`
- `entropy-def` before `alt-submodularity`
- `entropy-def` before `alternative-mutual`
- `entropy-def` before `bound-conc`
- `entropy-def` before `chain-rule`
- `entropy-def` before `cond-reduce`
- `entropy-def` before `cond-trial-ent`
- `entropy-def` before `conditional-chain-rule`
- `entropy-def` before `conditional-entropy-def`
- `entropy-def` before `conditional-mutual-alt`
- `entropy-def` before `conditional-mutual-def`
- `entropy-def` before `conditional-nonneg`
- `entropy-def` before `conditional-vanish`
- `entropy-def` before `entropy-comm`
- `entropy-def` before `information-def`
- `entropy-def` before `jensen-bound`
- `entropy-def` before `mutual-nonneg`
- `entropy-def` before `relabeled-entropy`
- `entropy-def` before `relabeled-entropy-cond`
- `entropy-def` before `subadditive`
- `entropy-def` before `submodularity`
- `entropy-def` before `uniform-entropy`
- `entropy-def` before `uniform-entropy-II`
- `entropy-def` before `vanish-entropy`
- `information-def` before `add-entropy`
- `information-def` before `alternative-mutual`
- `information-def` before `cond-reduce`
- `information-def` before `conditional-vanish`
- `information-def` before `mutual-nonneg`
- `information-def` before `vanish-entropy`
- `mutual-nonneg` before `cond-reduce`
- `mutual-nonneg` before `conditional-nonneg`
- `mutual-nonneg` before `conditional-vanish`
- `mutual-nonneg` before `subadditive`
- `relabeled-entropy` before `entropy-comm`
- `relabeled-entropy` before `relabeled-entropy-cond`
- `relabeled-entropy` before `submodularity`
- `relabeled-entropy-cond` before `conditional-chain-rule`
- `submodularity` before `alt-submodularity`
- `uniform-def` before `unif-exist`
- `uniform-def` before `uniform-entropy`
- `uniform-def` before `uniform-entropy-II`
- `vanish-entropy` before `add-entropy`
- `vanish-entropy` before `conditional-vanish`
