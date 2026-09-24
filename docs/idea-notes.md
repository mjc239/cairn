# Cairn — turning verified AI proofs into readable ones

*Idea notes from a conversation with Claude, 23 Sep 2026. Status: idea / pre-prototype.*

**Name:** Cairn — the stone stacks that mark a trail. Backronym: *Clarifying Arguments by Identifying Relevant Nodes*. (Alternatives considered: Throughline, Keystone, Breadcrumbs, Hourglass, Lemming.)

## Starting point

Prompted by Grant Sanderson's guest post on Tao's blog, "If math is more than proof, we need to better celebrate the rest of it" (18 Sep 2026): https://terrytao.wordpress.com/2026/09/18/if-math-is-more-than-proof-we-need-to-better-celebrate-the-rest-of-it/

Sanderson's argument: proofs were always a proxy for human understanding; now that AI can produce proofs without understanding, the community should define and give credit to **motivated explanations**. His criteria:
- Definitions sit in the middle — a construction only enters once the problem it solves is clear.
- It's fine (even desirable) to start with not-quite-right ideas and correct them ("discovery fiction", Michael Nielsen).
- Scope includes *why* the theorem is the right one to pose and how it's used in context.
- Test: "could you have discovered it yourself?"
- He notes that every AI-generated proof starts life as an unsolved exposition problem, and that there will never be a Lean for motivated explanations.
- Key example: Erdős Problem 1196 — AI (GPT-5.4 Pro via Liam Price) found the proof; Sothanaphan & Lichtman made it human-readable; the follow-up paper (Alexeev, …, Tao; arXiv 2605.00301) extracted the key idea and got a cleaner proof of the Erdős Primitive Set Conjecture too.

## My idea

The essay assumes humans do the translating. A separate model could take verified proofs (Lean or AI output) and convert them into clear, well-reasoned ones — trained with RL/RLHF where feedback rewards clarity rather than just correctness.

## Challenges identified

- **Reward signal.** Proof-search RL works because Lean is a cheap, binary reward. Clarity has no equivalent; expert raters for frontier proofs are scarce and expensive.
- **Reward hacking.** Optimising "feels clear" risks fluent explanations that skate over the hard step. Mitigations: anchor every informal claim to the formal proof; use a behavioural proxy — can a reader (human or weaker model) reconstruct the proof or solve a neighbouring problem afterwards?
- **Clarification is often new maths.** The best clean versions come from new definitions/framings (cf. Erdős 1196), so a "translator" is really a research model with a different objective (conceptual compression).
- **Bottleneck moves.** Perfect AI exposition makes human uptake the scarce resource; it also weakens Sanderson's proposal to credit exposition, since that becomes automatable too.

## Training data from existing expositions

Natural aligned pairs (terse ↔ clear, same result):
- Original paper vs later survey/textbook treatment
- Mathlib proofs vs the informal arguments they formalise
- arXiv v1 → v2 revisions; papers rewritten as book chapters
- Preference pairs for a clarity reward model

Limits: imitation learns the *style* of clarity more easily than faithfulness; **distribution shift** — human expositions recover a motivation that existed; AI proofs may have none, so it must be invented. Textbook versions often came after conceptual advances, so the pairs partly teach new maths rather than rewriting.

## Core formulation: ordering the Lean dependency DAG

- Lean gives a DAG of lemmas; any topological sort is a valid proof → choose the most readable one. Correctness for free, well-posed search.
- **Hand-crafted baseline:** minimise the number of "open" results the reader holds at each point ≈ **cutwidth** of the linear arrangement (related to pebbling / register allocation). NP-hard exactly; good heuristics exist.
- **Learned score:** likelihood of the ordering under a model trained on human mathematical writing.
- Ordering alone isn't enough. Full action space: **order + cluster + name + elide + augment**:
  - Granularity: collapse many tiny lemmas, name concepts, elide routine steps.
  - Narrative vs logical order: top-down with forward references; "no node before the goal it serves".
  - The irreducible node: a strange auxiliary construction needs added nodes (failed attempts, special cases, heuristics) — editing the graph, not just sorting it.

## Identifying key nodes (graph importance)

- **Dominators** (dominator tree): nodes every assumptions→theorem path passes through — a candidate proof skeleton.
- **Bottlenecks / min vertex cuts** (Menger): the "waist" of hourglass-shaped proofs.
- **Betweenness centrality** as a softer version.
- **Trap:** structural ≠ conceptual importance. Raw in-degree/PageRank ranks `mul_comm`-style utilities top → use IDF-style weighting against Mathlib-wide usage. The clever step may be a low-centrality node used once.
- Non-structural signals:
  - **Hardness:** can automation (`simp`, `omega`, `aesop`, small-budget LLM prover) prove it from its immediate deps? If not, thinking happened there.
  - **Novelty:** new to the project vs already in the library.
  - **Proof size** relative to statement size (compression points).
- Candidate score: dominance/bottleneck × hardness × novelty = unavoidable, non-trivial, new.

## Relation to Sanderson's "motivated explanation"

Only partial. The pipeline produces a **readable proof**, a necessary first stage.
- ✅ Definitions-in-the-middle ≈ "no node before the goal it serves".
- ⚠️ Discovery fiction's wrong turns conflict with Lean anchoring (every step true).
- ❌ Why-this-theorem / context: the DAG only looks downward, not outward.
- ⚠️ Low cognitive load makes a proof easier to *follow*, not necessarily *discoverable*.
- The **augment** step is where it becomes a motivated explanation.
- **Idea:** certify wrong turns too — formalise the counterexample showing the naive approach fails, or that the tempting stronger lemma is false. True steps certified by the proof, false steps certified as false. Guards against quietly-wrong "motivated" stories.

## Prior work

- **Ganesalingam & Gowers**, "A Fully Automatic Theorem Prover with Human-Style Output" (J. Autom. Reason. 2016; arXiv 1309.4501) — elementary metric space problems, near-indistinguishable from human write-ups, but had to restrict proof methods. Readability built into search, not post-hoc translation.
- **LLM informalization of Mathlib:** Herald (ICLR 2025; informalizes in dependency order); "Natural Language Translation of Formal Proofs through Informalization of Proof Steps and Recursive Summarization along Proof Structure" (2025); MerLean autoinformalization (arXiv 2602.16554). Mostly line-by-line translation for autoformalization data — not search over presentation.
- **Lean blueprints** (Massot's leanblueprint, from 2020 Sphere Eversion; used by Liquid Tensor, PFR, PNT, FLT): human LaTeX expositions with lemmas linked to Lean declarations + dependency graph → essentially labelled data for human chunking and ordering. https://github.com/PatrickMassot/leanblueprint
- Didn't find anyone explicitly optimising ordering/chunking or key-node identification.

## Prototype plan

1. **Extract graphs.** Clone blueprint projects (start with PFR). Parse `\uses{}` / `\lean{}` for the human graph + order; write a Lean metaprogram collecting used constants per declaration for the fine-grained formal graph.
2. **Tasks.** Given the formal graph: (a) recover blueprint clustering (which Lean decls were grouped into one lemma); (b) recover blueprint ordering; (c) recover which decls were promoted to named lemmas (key-node scoring, precision/recall).
3. **Baselines.** Random topological sort; cutwidth heuristic (networkx); LLM-chosen order; dominator/centrality/hardness scores. Metrics: Kendall tau, cluster agreement, P/R on promoted set.
4. **Only then learn.** If heuristics already match, that's a finding (human order ≈ working-memory load). Otherwise the residual is what a learned model must capture.

Caveat: only a few dozen serious blueprints → evaluation set more than training set. Result might interest Massot / Tao.
