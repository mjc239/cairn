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

- id `r462`: definition; steps here: state only (no proof needed). If $H$ is a subset of $S$, an $S$-random variable $X$ is said to be uniformly distributed on $H$ if $\bbP[X = s] = 1/|H|$ for $s \in X$ and $\bbP[X=s] = 0$ otherwise.
- id `r544`: lemma; steps here: state and prove. With notation as above, we have $$ \bbI[X : Y] = \bbI[Y:X]$$ $$ \bbI[X : Y] = \bbH[X] - \bbH[X|Y]$$ $$ \bbI[X : Y] = \bbH[Y] - \bbH[Y|X]$$
- id `r423`: lemma; steps here: state and prove. If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, and $Y = f(X,Z)$ almost surely for some map $f: S \times U \to T$ that is injective for each fixed $U$, then $\bbH[X|Z] = \bbH[Y|Z]$. Similarly, if $g: T \to U$ is injective, then $\bbH[X|g(Y)] = \bbH[X|Y]$.
- id `r725`: corollary; steps here: state and prove. With notation as above, we have $\bbH[X|Y] \leq \bbH[X]$.
- id `r755`: lemma; steps here: state and prove. If $X$ is $S$-valued random variable, then $\bbH[X] = \log |S|$ if and only if $X$ is uniformly distributed on $S$.
- id `r309`: definition; steps here: state only (no proof needed). If $X$ is an $S$-valued random variable, the entropy $\bbH[X]$ of $X$ is defined $$ \bbH[X] := \sum_{s \in S} \bbP[X=x] \log \frac{1}{\bbP[X=x]}$$ with the convention that $0 \log \frac{1}{0} = 0$.
- id `r665`: lemma; steps here: state and prove. If $X$ is an $S$-valued random variable, then there exists $s \in S$ such that $\bbP[X=s] \geq \exp(-\bbH[X])$.
- id `r588`: corollary; steps here: state and prove. If $X,Y$ are random variables, then $\bbH[X,Y] = \bbH[X] + \bbH[Y]$ if and only if $X,Y$ are independent.
- id `r553`: corollary; steps here: state and prove. With three random variables $X,Y,Z$, one has $$ \bbH[X,Y,Z] + \bbH[Z] \leq \bbH[X,Z] + \bbH[Y,Z].$$
- id `r986`: corollary; steps here: state and prove. With three random variables $X,Y,Z$, one has $\bbH[X|Y,Z] \leq \bbH[X|Z]$.
- id `r633`: lemma; steps here: state and prove. We have $$ \bbI[X:Y|Z] := \bbH[X|Z] + \bbH[Y|Z] - \bbH[X,Y|Z]$$ and $$ \bbI[X:Y|Z] := \bbH[X|Z] - \bbH[X|Y,Z].$$
- id `r366`: definition; steps here: state only (no proof needed). Two random variables $X: \Omega \to S$ and $Y: \Omega \to T$ are conditionally independent relative to another random variable $Z: \Omega \to U$ if $P[X = s \wedge Y = t| Z=u] = P[X=s|Z=u] P[Y=t|Z=u]$ for all $s \in S, t \in T, u \in U$. (We won't need conditional independence for more variables than this.)
- id `r163`: lemma; steps here: state and prove. Given a finite non-empty subset $H$ of a set $S$, there exists a random variable $X$ (on some probability space) that is uniformly distributed on $H$.
- id `r924`: lemma; steps here: state and prove. If $X$ is an $S$-valued random variable, then $\bbH[X] \leq \log |S|$.
- id `r661`: definition; steps here: state only (no proof needed). If $X,Y,Z$ are random variables, with $Z$ $U$-valued, then $$ \bbI[X:Y|Z] := \sum_{z \in U} P[Z=z] \bbI[(X|Z=z): (Y|Z=z)].$$
- id `r114`: lemma; steps here: state and prove. If $X$ is uniformly distributed on $H$, then, then $\bbH[X] = \log |H|$.
- id `r195`: lemma; steps here: state and prove. If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, then $$ \bbH[X, Y] = \bbH[Y] + \bbH[X|Y].$$
- id `r836`: lemma; steps here: state and prove. If $X,Y$ are random variables, then $\bbI[X:Y] = 0$ if and only if $X,Y$ are independent.
- id `r960`: definition; steps here: state only (no proof needed). If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, the conditional entropy $\bbH[X|Y]$ is defined as $$ \bbH[X|Y] := \sum_{y \in Y} \bbP[Y = y] \bbH[(X | Y=y)].$$
- id `r508`: lemma; steps here: state and prove. If $X,Y,Z$ are random variables, then $\bbI[X:Y|Z] = 0$ iff $X,Y$ are conditionally independent over $Z$.
- id `r827`: lemma; steps here: state and prove. We have $\bbI[X:Y] \geq 0$.
- id `r944`: corollary; steps here: state and prove. With notation as above, we have $\bbH[X,Y] \leq \bbH[X] + \bbH[Y]$.
- id `r903`: lemma; steps here: state and prove. If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, then $\bbH[X, Y] = \bbH[Y, X]$ and $\bbH[X, (Y,Z)] = \bbH[(X,Y), Z]$.
- id `r784`: lemma; steps here: state and prove. \begin{itemize} \item[(i)] If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ for some injection $f: S \to T$, then $\bbH[X] = \bbH[Y]$. \item[(ii)] If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ and $X = g(Y)$ for some functions $f: S \to T$, $g: T \to S$, then $\bbH[X] = \bbH[Y]$. \end{itemize}
- id `r740`: definition; steps here: state only (no proof needed). If $X: \Omega \to S$, $Y: \Omega \to T$ are random variables, then $$\bbI[X : Y] := \bbH[X] + \bbH[Y] - \bbH[X,Y].$$
- id `r101`: lemma; steps here: state and prove. If $X,Y,Z$ are random variables, then $\bbI[X:Y|Z] \ge 0$.
- id `r726`: lemma; steps here: state and prove. If $X: \Omega \to S$, $Y: \Omega \to T$, $Z: \Omega \to U$ are random variables, then $$ \bbH[X, Y | Z] = \bbH[Y | Z] + \bbH[X|Y, Z].$$
- id `r605`: corollary; steps here: state and prove. If $X, Y$ are conditionally independent over $Z$, then $$ \bbH[X,Y,Z] =\bbH[X,Z] + \bbH[Y,Z] - \bbH[Z].$$

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:r195` before `P:r423`
- `S:r195` before `P:r544`
- `S:r195` before `P:r553`
- `S:r195` before `P:r605`
- `S:r195` before `P:r725`
- `S:r195` before `P:r986`
- `S:r309` before `P:r101`
- `S:r309` before `P:r423`
- `S:r309` before `P:r508`
- `S:r309` before `P:r633`
- `S:r309` before `P:r726`
- `S:r309` before `P:r827`
- `S:r309` before `P:r836`
- `S:r309` before `P:r986`
- `S:r309` before `S:r114`
- `S:r309` before `S:r195`
- `S:r309` before `S:r544`
- `S:r309` before `S:r553`
- `S:r309` before `S:r588`
- `S:r309` before `S:r605`
- `S:r309` before `S:r661`
- `S:r309` before `S:r665`
- `S:r309` before `S:r725`
- `S:r309` before `S:r740`
- `S:r309` before `S:r755`
- `S:r309` before `S:r784`
- `S:r309` before `S:r903`
- `S:r309` before `S:r924`
- `S:r309` before `S:r944`
- `S:r309` before `S:r960`
- `S:r366` before `S:r508`
- `S:r366` before `S:r605`
- `S:r423` before `P:r726`
- `S:r462` before `S:r114`
- `S:r462` before `S:r163`
- `S:r462` before `S:r755`
- `S:r508` before `P:r605`
- `S:r633` before `P:r605`
- `S:r661` before `P:r605`
- `S:r661` before `S:r101`
- `S:r661` before `S:r508`
- `S:r661` before `S:r633`
- `S:r726` before `P:r633`
- `S:r740` before `P:r508`
- `S:r740` before `P:r588`
- `S:r740` before `P:r725`
- `S:r740` before `S:r544`
- `S:r740` before `S:r827`
- `S:r740` before `S:r836`
- `S:r784` before `P:r423`
- `S:r784` before `P:r903`
- `S:r784` before `P:r986`
- `S:r827` before `P:r101`
- `S:r827` before `P:r508`
- `S:r827` before `P:r725`
- `S:r827` before `P:r944`
- `S:r836` before `P:r508`
- `S:r836` before `P:r588`
- `S:r903` before `P:r195`
- `S:r903` before `P:r544`
- `S:r903` before `P:r605`
- `S:r960` before `P:r553`
- `S:r960` before `P:r605`
- `S:r960` before `S:r195`
- `S:r960` before `S:r423`
- `S:r960` before `S:r544`
- `S:r960` before `S:r633`
- `S:r960` before `S:r725`
- `S:r960` before `S:r726`
- `S:r960` before `S:r986`
- `S:r986` before `P:r553`
