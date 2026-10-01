# HoTT-Paradoxy: Non-reality paradoxes in homotopy type theory — conclusions and evidence

[中文](README-ZH.md) · **English** · [Français](README-FR.md) · [Deutsch](README-DE.md)

**Abstract.** For economy and generality, homotopy type theory (HoTT) turns "being the same" from a fact that a single check settles into a structure that can be questioned level by level ("in which ways are these the same?"): isomorphic things are identical (univalence), and shapes of every dimension are available in the universe at once (higher inductive types). We write "deciding whether two things are the same" as a program that asks level by level: the k-th question asks whether this sameness has settled at level k (that is, whether the type has h-level k+1); a judge answers each question with a proof of "yes" or of "no"; on "yes" the program stops and reports the level. We prove in Cubical Agda that, for every judge, this program equals the non-terminating program `never` on the universe (with higher inductive types) and on the product ∏ₙ K(ℤ,n+1); when the height of the members is capped, it stops exactly at the question that the cap determines; transcribed by the same equations to Lean 4, where sameness is a mere fact, it stops at the first question; asked about the set truncation, it also stops at the first question, but truncation merges the several ways of being the same into one and cannot be decoded back into the universe. The researcher who initiated the project defines a non-reality paradox as "something that should be very simple, yet cannot be done even in theory X" (UR), reads this result as a paradox of the same shape as Zeno's, and judges it very likely to be the one this project set out to find. The mathematics is mostly not new: the product is Example 8.8.6 of the HoTT Book; for the universe, the Book (2013) said the result was expected to be provable but had not yet been done, and this repository gives a machine-checked proof. What is new is mainly the reading and the premise it points to, univalence first. A second line: a uniform definition of semi-simplicial types in book HoTT is still unknown, a well-known open problem; the researcher judged that this line "revived the ghost of Zeno's paradox". All positive claims are kernel-checked (Cubical Agda 2.8.0 with cubical 0.9; Lean 4.34.0), with negative controls and {{RUN_TOTAL}} replayable run receipts. We do not claim that HoTT is inconsistent; "very likely found" is the researcher's judgment, not a theorem.

**Keywords.** homotopy type theory; univalence; higher inductive types; truncation levels; delay monad; infinite coherence; Zeno's paradox; non-reality paradox

> **About this branch.** `main` holds only the content that supports the conclusions: the conclusion documents, precise claims, proof sources, run receipts and a way to replay them. The whole research process is on the [`dev` branch]({{REPO}}/tree/dev): the ledger of the researcher's original statements, the direction and outcome projections, the AI workspaces, audits and exchanges, governance and state. This branch is generated from commit [`{{SOURCE_SHORT}}`]({{REPO}}/commit/{{SOURCE_COMMIT}}) of `dev` according to a manifest ([`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json)) and is not edited directly. This README also exists in Chinese, French and German with the same content. The conclusion papers, the phase-close report and `CLAIMS.md` are written in Chinese; papers 01 and 02 open with an English summary.

## 1. The researcher's definition and verdicts

The researcher's operational definition of a "non-reality paradox" (2026-09-30, original words):

> `UR`=`本来应该很简单的事情，甚至在X理论中，都做不到`，我想这就是一种类似芝诺悖论的`不合理`。

Translation: "`UR` = `something that should be very simple, yet cannot be done even in theory X`; I think this is an unreasonableness of the kind found in Zeno's paradox."

"Reality" refers to the first half of UR ("something that should be very simple"), "paradox" to the whole of UR; whoever judges the "unreasonableness" is a person taking one look. That judgment belongs to the researcher; it is not a mathematical theorem. The researcher's two verdicts (original words, each followed by a translation):

> 本repo复活了芝诺悖论的幽灵和罗素悖论的幽灵，并且找到的HoTT理论的问题。

Translation (2026-09-27): "This repo has revived the ghost of Zeno's paradox and the ghost of Russell's paradox, and has found the problem of the HoTT theory."

> 把所有该做的，全部做完，我认为我们要阶段性地收尾HoTT悖论查找工作了，因为我们很可能已经找到了。

Translation (2026-09-30): "Do everything that should be done. I think we should bring the search for HoTT paradoxes to a close for this phase, because we have very likely found it."

## 2. HoTT's Zeno: "being the same" never settles

**The thing that should be simple:** deciding whether two things are the same.

**The process aimed at it:** a program Q that asks level by level. It asks "has the sameness in this catalogue settled at level k?" (technically: is it a type of h-level k+1?); a judge answers each question with a proof of "yes" or of "no"; on "yes" the program stops and reports the level. Q stops if and only if the sameness settles at some finite level (CG001-C-77).

**Results** (machine-checked):

| Case | Outcome of the same program | Claim |
|---|---|---|
| Sameness is a fact (the same equations transcribed to Lean 4) | the universe stops at question 1 | CG001-C-80 |
| HoTT, the catalogue of types of h-level 1+n | stops exactly at question 1+n | CG001-C-79 |
| HoTT, the same product with the height of the members capped at b | stops exactly at question 2+b | CG001-C-82 |
| HoTT, the product ∏ₙ K(ℤ,n+1) (HoTT Book, Example 8.8.6) | equals the non-terminating `never` for every judge | CG001-C-81 |
| HoTT (with higher inductive types), the universe | equals `never` for every judge | CG001-C-75, CG001-C-78 |
| HoTT, the set truncation | stops at question 1; but truncation merges the ways of being the same into one, and it cannot be decoded back into the universe | CG001-C-83 |

**Correspondence with Zeno** (a pattern match, not a mathematical isomorphism):

| | Zeno | HoTT |
|---|---|---|
| The thing that should be simple | getting from here to there | deciding whether two things are the same |
| The condition the theory changed to be convenient | position can be divided without end | sameness can be divided without end |
| What each step shows | half the way remains; certainly not there yet | this level has not settled; a definite "no" |
| Outcome | the walk never ends | the program equals `never` |
| Textbook resolution | limits | truncation |

**The strongest objection:** "Asked about the set truncation, the program stops at question 1, so the question was simply posed the wrong way." Reply: truncation answers "how many branches are there"; it merges the ways of being the same into one and cannot return to the universe, so the object being asked about has changed. This is like answering Zeno with limits: a definition declares that one has arrived, while the condition that was changed is not restored. This reply is an interpretation and is submitted for audit.

**What it is not:**

- It is not an internal contradiction of HoTT.
- The mathematics is mostly not new: that such products have no finite level is Example 8.8.6 of the HoTT Book; for the universe itself, the Book (2013) said it was expected to be provable but had not yet been done; Kraus and Sattler (2015) proved that the n-th universe of a univalent hierarchy is not an n-type; for a single universe with higher inductive types, this repository has a machine-checked proof (CG001-C-75). What is new is mainly the reading and the premise it points to, univalence first.
- "Never stops" is a theorem inside the theory. Reading it as "running the program in reality never yields an answer" further requires the consistency of the theory and, for an arbitrary judge, canonicity.
- "Very likely found" is the researcher's judgment, not a theorem.

Further reading (in Chinese): [community audit paper 03, "HoTT's Zeno"](docs/社区审计提交/03-HoTT的芝诺.md) (the shortest, ending with five audit questions); [02, "The ghost of Russell's paradox"](docs/社区审计提交/02-罗素悖论的幽灵.md); [the phase-close report](docs/HoTT悖论查找阶段收尾报告-20260930.md).

## 3. The ghost of Zeno's paradox: infinite coherence

- **Trade-off:** univalence makes isomorphic things identical, so sameness becomes data. For example, Bool is "the same" as itself in two genuinely different ways, and transporting `true` along the second gives `false` (CG001-C-63).
- **Process:** write down a semi-simplicial structure, gluing a shape from points, segments, triangles and tetrahedra level by level and requiring that "faces of faces" agree. In classical mathematics this is a one-line definition.
- **Observations:** where sameness is a fact (Lean 4), that line is the whole definition, and the hexagon coherence holds by `rfl` (CG001-C-65); in HoTT, the same line accepts data that do not fit together, two simplification routes winding once and twice around the circle (CG001-C-64); once the hexagon is added, it can be filled in more than one way, and the next level (P₄) fails for one of the fillings (CG001-C-66, CG001-C-68); how many levels must be added depends on how many levels sameness has (CG001-C-70); each fixed level can be written down (machine-checked up to level 5, CG001-C-62).
- **Boundary:** an internal definition uniform in the number of levels n is a well-known open problem, and its impossibility has not been proved. If a uniform definition of semi-simplicial types appears in book HoTT, the strong form of this line is withdrawn.

Further reading (in Chinese, opening with an English summary): [community audit paper 01, "The ghost of Zeno's paradox"](docs/社区审计提交/01-芝诺悖论的幽灵.md).

## 4. Claims and evidence

- [`CLAIMS.md`](CLAIMS.md) (in Chinese): the precise statement, evidence and forbidden extrapolations of each claim; for each proof package, the main runs, negative controls and cross-platform replays.
- Proof sources: `HoTT/formal/`. Each package's `CLAIM.md` gives the full statements and their scope.
- Run receipts: `HoTT/verification/runs/`, {{RUN_TOTAL}} in all: {{RUN_ACCEPTED}} accepted by the kernel and {{RUN_REJECTED}} negative controls rejected as expected (they test precise boundaries; they are not a history of failures). Some claims have runs on both macOS and Linux.
- [`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json): the SHA-256 and role of each of the {{FILE_TOTAL}} files on this branch, and the `dev` commit they come from.

Toolchain: Cubical Agda 2.8.0 with the cubical library v0.9 (the options `--safe --cubical --guardedness` are set in each source file); Lean 4.34.0, core library only (no Mathlib), for the controls in which sameness is a fact. The toolchain records cited by the receipts are in `HoTT/formal/dedekind-omega-missile/` (Agda on macOS), `HoTT/formal/claude-cg001/pedometer-ablation-lean/` (Lean on macOS) and `HoTT/formal/cloud-opus-glm-audit/` (Linux); the first two directories keep their location on `dev` and hold only these records on this branch.

## 5. How to replay

With Agda 2.8.0, cubical v0.9 and Lean 4.34.0 installed, run from the repository root:

```sh
python3 tools/replay.py --agda /path/to/agda --cubical-lib /path/to/cubical/cubical.agda-lib --lean-sysroot /path/to/lean-4.34.0 --jobs 4
```

It rebuilds the command of each receipt with relative paths, runs it, and compares the result with the receipt: the outcome (accepted or rejected) must agree, and the output is compared line by line after the repository root and the library paths are replaced by placeholders. A negative control passes only if it is rejected again; if its output also agrees, it was rejected for the recorded reason. To replay a single receipt: `--only <run id>`; to list them all: `--list`. Replaying everything one after another takes about an hour and a half.

The commands in the receipts record absolute paths of the machine that captured them. The original byte-for-byte replay tools are on the `dev` branch (`.claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py`, `Cloud-Opus审计并补完GLM/tools/verify_copus_run.py`).

## 6. Paths mentioned in the documents but not on this branch

The conclusion documents also mention files from the research process: the ledger of the researcher's original statements `核心认知.md`, the direction and outcome projections, the AI workspaces, audits and exchanges, the goal-local indexes and so on. All of them are on the `dev` branch:

{{DEV_PATHS_TABLE}}

## 7. Branches

- `main` (this branch): conclusions and evidence. It is generated by `scripts/release/build_main_release.py` on `dev` according to `scripts/release/main-release-spec.json`. To update it, change the manifest or the conclusion documents on `dev` and generate it again; nothing is committed directly to this branch.
- `dev`: the whole research process; all work happens there.
