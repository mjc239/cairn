You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order.

## Results

- id `r462`: definition. If $H$ is a subset of $S$, an $S$-random variable $X$ is said to be uniformly distributed on $H$ if $\bbP[X = s] = 1/|H|$ for $s \in X$ and $\bbP[X=s] = 0$ otherwise.
- id `r544`: lemma. With notation as above, we have $$ \bbI[X : Y] = \bbI[Y:X]$$ $$ \bbI[X : Y] = \bbH[X] - \bbH[X|Y]$$ $$ \bbI[X : Y] = \bbH[Y] - \bbH[Y|X]$$
- id `r423`: lemma. If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, and $Y = f(X,Z)$ almost surely for some map $f: S \times U \to T$ that is injective for each fixed $U$, then $\bbH[X|Z] = \bbH[Y|Z]$. Similarly, if $g: T \to U$ is injective, then $\bbH[X|g(Y)] = \bbH[X|Y]$.
- id `r725`: corollary. With notation as above, we have $\bbH[X|Y] \leq \bbH[X]$.
- id `r755`: lemma. If $X$ is $S$-valued random variable, then $\bbH[X] = \log |S|$ if and only if $X$ is uniformly distributed on $S$.
- id `r309`: definition. If $X$ is an $S$-valued random variable, the entropy $\bbH[X]$ of $X$ is defined $$ \bbH[X] := \sum_{s \in S} \bbP[X=x] \log \frac{1}{\bbP[X=x]}$$ with the convention that $0 \log \frac{1}{0} = 0$.
- id `r665`: lemma. If $X$ is an $S$-valued random variable, then there exists $s \in S$ such that $\bbP[X=s] \geq \exp(-\bbH[X])$.
- id `r588`: corollary. If $X,Y$ are random variables, then $\bbH[X,Y] = \bbH[X] + \bbH[Y]$ if and only if $X,Y$ are independent.
- id `r553`: corollary. With three random variables $X,Y,Z$, one has $$ \bbH[X,Y,Z] + \bbH[Z] \leq \bbH[X,Z] + \bbH[Y,Z].$$
- id `r986`: corollary. With three random variables $X,Y,Z$, one has $\bbH[X|Y,Z] \leq \bbH[X|Z]$.
- id `r633`: lemma. We have $$ \bbI[X:Y|Z] := \bbH[X|Z] + \bbH[Y|Z] - \bbH[X,Y|Z]$$ and $$ \bbI[X:Y|Z] := \bbH[X|Z] - \bbH[X|Y,Z].$$
- id `r366`: definition. Two random variables $X: \Omega \to S$ and $Y: \Omega \to T$ are conditionally independent relative to another random variable $Z: \Omega \to U$ if $P[X = s \wedge Y = t| Z=u] = P[X=s|Z=u] P[Y=t|Z=u]$ for all $s \in S, t \in T, u \in U$. (We won't need conditional independence for more variables than this.)
- id `r163`: lemma. Given a finite non-empty subset $H$ of a set $S$, there exists a random variable $X$ (on some probability space) that is uniformly distributed on $H$.
- id `r924`: lemma. If $X$ is an $S$-valued random variable, then $\bbH[X] \leq \log |S|$.
- id `r661`: definition. If $X,Y,Z$ are random variables, with $Z$ $U$-valued, then $$ \bbI[X:Y|Z] := \sum_{z \in U} P[Z=z] \bbI[(X|Z=z): (Y|Z=z)].$$
- id `r114`: lemma. If $X$ is uniformly distributed on $H$, then, then $\bbH[X] = \log |H|$.
- id `r195`: lemma. If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, then $$ \bbH[X, Y] = \bbH[Y] + \bbH[X|Y].$$
- id `r836`: lemma. If $X,Y$ are random variables, then $\bbI[X:Y] = 0$ if and only if $X,Y$ are independent.
- id `r960`: definition. If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, the conditional entropy $\bbH[X|Y]$ is defined as $$ \bbH[X|Y] := \sum_{y \in Y} \bbP[Y = y] \bbH[(X | Y=y)].$$
- id `r508`: lemma. If $X,Y,Z$ are random variables, then $\bbI[X:Y|Z] = 0$ iff $X,Y$ are conditionally independent over $Z$.
- id `r827`: lemma. We have $\bbI[X:Y] \geq 0$.
- id `r944`: corollary. With notation as above, we have $\bbH[X,Y] \leq \bbH[X] + \bbH[Y]$.
- id `r903`: lemma. If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, then $\bbH[X, Y] = \bbH[Y, X]$ and $\bbH[X, (Y,Z)] = \bbH[(X,Y), Z]$.
- id `r784`: lemma. \begin{itemize} \item[(i)] If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ for some injection $f: S \to T$, then $\bbH[X] = \bbH[Y]$. \item[(ii)] If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ and $X = g(Y)$ for some functions $f: S \to T$, $g: T \to S$, then $\bbH[X] = \bbH[Y]$. \end{itemize}
- id `r740`: definition. If $X: \Omega \to S$, $Y: \Omega \to T$ are random variables, then $$\bbI[X : Y] := \bbH[X] + \bbH[Y] - \bbH[X,Y].$$
- id `r101`: lemma. If $X,Y,Z$ are random variables, then $\bbI[X:Y|Z] \ge 0$.
- id `r726`: lemma. If $X: \Omega \to S$, $Y: \Omega \to T$, $Z: \Omega \to U$ are random variables, then $$ \bbH[X, Y | Z] = \bbH[Y | Z] + \bbH[X|Y, Z].$$
- id `r605`: corollary. If $X, Y$ are conditionally independent over $Z$, then $$ \bbH[X,Y,Z] =\bbH[X,Z] + \bbH[Y,Z] - \bbH[Z].$$

## Constraints

- `r195` before `r423`
- `r195` before `r544`
- `r195` before `r553`
- `r195` before `r605`
- `r195` before `r725`
- `r195` before `r986`
- `r309` before `r101`
- `r309` before `r114`
- `r309` before `r195`
- `r309` before `r423`
- `r309` before `r508`
- `r309` before `r544`
- `r309` before `r553`
- `r309` before `r588`
- `r309` before `r605`
- `r309` before `r633`
- `r309` before `r661`
- `r309` before `r665`
- `r309` before `r725`
- `r309` before `r726`
- `r309` before `r740`
- `r309` before `r755`
- `r309` before `r784`
- `r309` before `r827`
- `r309` before `r836`
- `r309` before `r903`
- `r309` before `r924`
- `r309` before `r944`
- `r309` before `r960`
- `r309` before `r986`
- `r366` before `r508`
- `r366` before `r605`
- `r423` before `r726`
- `r462` before `r114`
- `r462` before `r163`
- `r462` before `r755`
- `r508` before `r605`
- `r633` before `r605`
- `r661` before `r101`
- `r661` before `r508`
- `r661` before `r605`
- `r661` before `r633`
- `r726` before `r633`
- `r740` before `r508`
- `r740` before `r544`
- `r740` before `r588`
- `r740` before `r725`
- `r740` before `r827`
- `r740` before `r836`
- `r784` before `r423`
- `r784` before `r903`
- `r784` before `r986`
- `r827` before `r101`
- `r827` before `r508`
- `r827` before `r725`
- `r827` before `r944`
- `r836` before `r508`
- `r836` before `r588`
- `r903` before `r195`
- `r903` before `r544`
- `r903` before `r605`
- `r960` before `r195`
- `r960` before `r423`
- `r960` before `r544`
- `r960` before `r553`
- `r960` before `r605`
- `r960` before `r633`
- `r960` before `r725`
- `r960` before `r726`
- `r960` before `r986`
- `r986` before `r553`
