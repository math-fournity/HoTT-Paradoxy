# HoTT-Paradoxy: Non-reality paradoxes in homotopy type theory — conclusions and evidence

[中文](README-ZH.md) · [Русский](README-RU.md) · [Deutsch](README-DE.md) · [Français](README-FR.md) · **English**

**Abstract.** For economy and generality, homotopy type theory (HoTT) turns "being the same" from a fact that a single check settles into a structure that can be questioned level by level ("in which ways are these the same?"): isomorphic things are identical (univalence), and shapes of every dimension are available in the universe at once (higher inductive types). We write "deciding whether two things are the same" as a program that asks level by level: the k-th question asks whether this sameness has settled at level k (that is, whether the type has h-level k+1); a judge answers each question with a proof of "yes" or of "no"; on "yes" the program stops and reports the level. We prove in Cubical Agda that, for every judge, this program equals the non-terminating program `never` on the universe (with higher inductive types) and on the product ∏ₙ K(ℤ,n+1); when the height of the members is capped, it stops exactly at the question that the cap determines; transcribed by the same equations to Lean 4, where sameness is a mere fact, it stops at the first question; asked about the set truncation, it also stops at the first question, but truncation merges the several ways of being the same into one and cannot be decoded back into the universe. The researcher who initiated the project defines a non-reality paradox as "something that should be very simple, yet cannot be done even in theory X" (UR), reads this result as a paradox of the same shape as Zeno's, and judges it very likely to be the one this project set out to find. The mathematics is mostly not new: the product is Example 8.8.6 of the HoTT Book; for the universe, the Book (2013) said the result was expected to be provable but had not yet been done, and this repository gives a machine-checked proof. What is new is mainly the reading and the premise it points to, univalence first. A second line: a uniform definition of semi-simplicial types in book HoTT is still unknown, a well-known open problem; the researcher judged that this line "revived the ghost of Zeno's paradox". All positive claims are kernel-checked (Cubical Agda 2.8.0 with cubical 0.9; Lean 4.34.0), with negative controls and 107 replayable run receipts. We do not claim that HoTT is inconsistent; "very likely found" is the researcher's judgment, not a theorem.

**Keywords.** homotopy type theory; univalence; higher inductive types; truncation levels; delay monad; infinite coherence; Zeno's paradox; non-reality paradox

> **About this branch.** `main` holds only the content that supports the conclusions: the conclusion documents, precise claims, proof sources, run receipts and a way to replay them. The whole research process is on the [`dev` branch](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev): the ledger of the researcher's original statements, the direction and outcome projections, the AI workspaces, audits and exchanges, governance and state. This branch is generated from commit [`24950d5d`](https://github.com/math-fournity/HoTT-Paradoxy/commit/24950d5d19ee6d0e7edc6c2d6ff93f1c18a2c2e1) of `dev` according to a manifest ([`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json)) and is not edited directly. This README also exists in Chinese, Russian, German and French with the same content. The conclusion papers, the phase-close report and `CLAIMS.md` are written in Chinese; papers 01 and 02 open with an English summary.

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
- Run receipts: `HoTT/verification/runs/`, 107 in all: 49 accepted by the kernel and 58 negative controls rejected as expected (they test precise boundaries; they are not a history of failures). Some claims have runs on both macOS and Linux.
- [`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json): the SHA-256 and role of each of the 699 files on this branch, and the `dev` commit they come from.

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

| Path | On `dev` |
|---|---|
| `.claude/goals/CG-001-targeted-overview` | [open](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/goals/CG-001-targeted-overview) |
| `.claude/goals/CG-001-targeted-overview/证据索引.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/.claude/goals/CG-001-targeted-overview/%E8%AF%81%E6%8D%AE%E7%B4%A2%E5%BC%95.md) |
| `.claude/goals/CG-002-a7-infinite-coherence` | [open](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/goals/CG-002-a7-infinite-coherence) |
| `.claude/goals/CG-003-a7-self-audit` | [open](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/goals/CG-003-a7-self-audit) |
| `.claude/思考与发现` | [open](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/%E6%80%9D%E8%80%83%E4%B8%8E%E5%8F%91%E7%8E%B0) |
| `.claude/总索引.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/.claude/%E6%80%BB%E7%B4%A2%E5%BC%95.md) |
| `.claude/调研请求/20260930-相同永远了结不了-社区先例调研请求.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/.claude/%E8%B0%83%E7%A0%94%E8%AF%B7%E6%B1%82/20260930-%E7%9B%B8%E5%90%8C%E6%B0%B8%E8%BF%9C%E4%BA%86%E7%BB%93%E4%B8%8D%E4%BA%86-%E7%A4%BE%E5%8C%BA%E5%85%88%E4%BE%8B%E8%B0%83%E7%A0%94%E8%AF%B7%E6%B1%82.md) |
| `Cloud-Opus审计并补完GLM` | [open](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM) |
| `Cloud-Opus审计并补完GLM/01-工具链与复现.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/01-%E5%B7%A5%E5%85%B7%E9%93%BE%E4%B8%8E%E5%A4%8D%E7%8E%B0.md) |
| `Cloud-Opus审计并补完GLM/02-断裂审计-逐命题（D1）.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/02-%E6%96%AD%E8%A3%82%E5%AE%A1%E8%AE%A1-%E9%80%90%E5%91%BD%E9%A2%98%EF%BC%88D1%EF%BC%89.md) |
| `Cloud-Opus审计并补完GLM/11-收据核验结果.json` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/11-%E6%94%B6%E6%8D%AE%E6%A0%B8%E9%AA%8C%E7%BB%93%E6%9E%9C.json) |
| `Cloud-Opus审计并补完GLM/13-外部复核请求.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/13-%E5%A4%96%E9%83%A8%E5%A4%8D%E6%A0%B8%E8%AF%B7%E6%B1%82.md) |
| `Cloud-Opus审计并补完GLM/14-罗素面终局判词.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/14-%E7%BD%97%E7%B4%A0%E9%9D%A2%E7%BB%88%E5%B1%80%E5%88%A4%E8%AF%8D.md) |
| `Cloud-Opus审计并补完GLM/README.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/README.md) |
| `Cloud-Opus审计并补完GLM/tools` | [open](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/tools) |
| `Cloud-Opus审计并补完GLM/tools/capture_zeno_line_replays.sh` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/tools/capture_zeno_line_replays.sh) |
| `Cloud-Opus审计并补完GLM/附件/20260926-Session问答原文存档（用户上传，GLM-Auditor会话）.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/%E9%99%84%E4%BB%B6/20260926-Session%E9%97%AE%E7%AD%94%E5%8E%9F%E6%96%87%E5%AD%98%E6%A1%A3%EF%BC%88%E7%94%A8%E6%88%B7%E4%B8%8A%E4%BC%A0%EF%BC%8CGLM-Auditor%E4%BC%9A%E8%AF%9D%EF%BC%89.md) |
| `Cloud-Opus审计并补完GLM/附件/工作过程文件/自查轮/verify-all-rerun-46个运行.json` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/%E9%99%84%E4%BB%B6/%E5%B7%A5%E4%BD%9C%E8%BF%87%E7%A8%8B%E6%96%87%E4%BB%B6/%E8%87%AA%E6%9F%A5%E8%BD%AE/verify-all-rerun-46%E4%B8%AA%E8%BF%90%E8%A1%8C.json) |
| `GLM-5.3-Flash/README.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/GLM-5.3-Flash/README.md) |
| `GLM-5.3-Flash/审计请求` | [open](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/GLM-5.3-Flash/%E5%AE%A1%E8%AE%A1%E8%AF%B7%E6%B1%82) |
| `GLM-5.3-Flash/思考与发现` | [open](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/GLM-5.3-Flash/%E6%80%9D%E8%80%83%E4%B8%8E%E5%8F%91%E7%8E%B0) |
| `GLM-5.3-Flash/策略快照/20260926-D2后罗素线策略-大白话快照.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/GLM-5.3-Flash/%E7%AD%96%E7%95%A5%E5%BF%AB%E7%85%A7/20260926-D2%E5%90%8E%E7%BD%97%E7%B4%A0%E7%BA%BF%E7%AD%96%E7%95%A5-%E5%A4%A7%E7%99%BD%E8%AF%9D%E5%BF%AB%E7%85%A7.md) |
| `GLM-5.3-Flash/裁定问题/20260926-M2-形成规则是回答还是回避-两面陈词.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/GLM-5.3-Flash/%E8%A3%81%E5%AE%9A%E9%97%AE%E9%A2%98/20260926-M2-%E5%BD%A2%E6%88%90%E8%A7%84%E5%88%99%E6%98%AF%E5%9B%9E%E7%AD%94%E8%BF%98%E6%98%AF%E5%9B%9E%E9%81%BF-%E4%B8%A4%E9%9D%A2%E9%99%88%E8%AF%8D.md) |
| `HoTT/CLAIM_EVIDENCE_MATRIX.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/HoTT/CLAIM_EVIDENCE_MATRIX.md) |
| `HoTT/verification/PROOF_VERSION_CLOSURE.json` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/HoTT/verification/PROOF_VERSION_CLOSURE.json) |
| `README.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/README.md) |
| `Terra对Opus的审计` | [open](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Terra%E5%AF%B9Opus%E7%9A%84%E5%AE%A1%E8%AE%A1) |
| `Terra对Opus的审计/Opus给GPT的回应` | [open](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Terra%E5%AF%B9Opus%E7%9A%84%E5%AE%A1%E8%AE%A1/Opus%E7%BB%99GPT%E7%9A%84%E5%9B%9E%E5%BA%94) |
| `rulings.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/rulings.md) |
| `scripts/audit/verify_math_proof_delivery_governance.py` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/scripts/audit/verify_math_proof_delivery_governance.py) |
| `scripts/audit/verify_proof_version_closure.py` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/scripts/audit/verify_proof_version_closure.py) |
| `sources/prompts/Claude-UR与芝诺的模式匹配-用户原文-20260930.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Claude-UR%E4%B8%8E%E8%8A%9D%E8%AF%BA%E7%9A%84%E6%A8%A1%E5%BC%8F%E5%8C%B9%E9%85%8D-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260930.md) |
| `sources/prompts/Claude-归因是正题-用户原文-20260924.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Claude-%E5%BD%92%E5%9B%A0%E6%98%AF%E6%AD%A3%E9%A2%98-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260924.md) |
| `sources/prompts/Claude-罗素原则P1至P3-用户原文-20260926.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Claude-%E7%BD%97%E7%B4%A0%E5%8E%9F%E5%88%99P1%E8%87%B3P3-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260926.md) |
| `sources/prompts/Codex-非现实性悖论的目标与A向读法-用户原文-20260930.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Codex-%E9%9D%9E%E7%8E%B0%E5%AE%9E%E6%80%A7%E6%82%96%E8%AE%BA%E7%9A%84%E7%9B%AE%E6%A0%87%E4%B8%8EA%E5%90%91%E8%AF%BB%E6%B3%95-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260930.md) |
| `sources/prompts/GLM-算符先行于存在性落定-用户原文-20260926.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/GLM-%E7%AE%97%E7%AC%A6%E5%85%88%E8%A1%8C%E4%BA%8E%E5%AD%98%E5%9C%A8%E6%80%A7%E8%90%BD%E5%AE%9A-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260926.md) |
| `全景视野.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E5%85%A8%E6%99%AF%E8%A7%86%E9%87%8E.md) |
| `扩展认知.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%89%A9%E5%B1%95%E8%AE%A4%E7%9F%A5.md) |
| `扩展认知/011 - 本来应该很简单的事：UR 与芝诺的模式匹配.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%89%A9%E5%B1%95%E8%AE%A4%E7%9F%A5/011%20-%20%E6%9C%AC%E6%9D%A5%E5%BA%94%E8%AF%A5%E5%BE%88%E7%AE%80%E5%8D%95%E7%9A%84%E4%BA%8B%EF%BC%9AUR%20%E4%B8%8E%E8%8A%9D%E8%AF%BA%E7%9A%84%E6%A8%A1%E5%BC%8F%E5%8C%B9%E9%85%8D.md) |
| `方向追踪.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%96%B9%E5%90%91%E8%BF%BD%E8%B8%AA.md) |
| `核心认知.md` | [open](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%A0%B8%E5%BF%83%E8%AE%A4%E7%9F%A5.md) |

## 7. Branches

- `main` (this branch): conclusions and evidence. It is generated by `scripts/release/build_main_release.py` on `dev` according to `scripts/release/main-release-spec.json`. To update it, change the manifest or the conclusion documents on `dev` and generate it again; nothing is committed directly to this branch.
- `dev`: the whole research process; all work happens there.
