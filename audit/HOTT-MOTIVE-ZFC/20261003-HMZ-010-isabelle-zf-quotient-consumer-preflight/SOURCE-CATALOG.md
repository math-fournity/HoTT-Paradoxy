# HMZ-010：来源目录、版本与 locator

## 新归档原件

| 文件 | SHA-256 | 上游固定身份 | 访问与来源边界 |
|---|---|---|---|
| `originals/HMZ-S-027-Isabelle2021-1-RC5-EquivClass.thy` | `83016841fba6a0b469692ccc5a5b8d65e3953bee1ca6bb348eac9acd51619b76` | `isabelle-prover/mirror-isabelle` tag `Isabelle2021-1-RC5` = `6a65dad3761d436f234dbd752201fe70fffa0200`; raw URL `https://raw.githubusercontent.com/isabelle-prover/mirror-isabelle/6a65dad3761d436f234dbd752201fe70fffa0200/src/ZF/EquivClass.thy`. | 2026-10-03 public, no login. Git tag resolution was read by `git ls-remote`; file is a source snapshot, not a kernel execution receipt. |

## 关键源码 locator

| 行 | 来源事实 | 本预检的使用边界 |
|---:|---|---|
| 10–12 | `quotient` is defined as `A//r == {r``{x} . x ∈ A}` and labeled “set of equiv classes”. | 固定 formation interface；其 concrete constructor is `RepFun`, not a Power Set subset. |
| 14–30 | `congruent` / `congruent2` and `respects` / `respects2` are defined. | 接受 quotient operation 前的 well-definedness payment。 |
| 67–100 | source proves related elements yield equal equivalence classes, and conversely under explicit premises. | equality of classes is derived with `equiv(A,r)` and membership conditions. |
| 106–124 | `quotientI`, `quotientE`, `Union_quotient`, `quotient_disj`. | actual construction/consumption interface and quotient observations. |
| 126–159 | unary operation / conversion / type rules. | consumer only concludes after `equiv`, `respects`, member hypotheses and a target-type condition. |
| 162–231 | binary operation rules. | same explicit congruence and type conditions persist for a larger consumer. |

## 复用来源

| ID | Frozen identity | Relevant locator | Role and limit |
|---|---|---|---|
| `HMZ-S-011` | [HMZ-001 Isabelle2021-1 manual](../20261003-HMZ-001-primary-motives/originals/HMZ-S-011-Isabelle2021-Logics-ZF.pdf), SHA-256 `2b91b2f89480e8b14201dbc93382df366737d405dbd67c39de6970ecf14cd646`. | manual pp. 25–30 / derived lines 1322–1354, 1461–1469. | `RepFun` is functional replacement; source-level formation/payment explanation. Its version is recorded separately from `HMZ-S-027`. |
| `HMZ-S-026` | [HMZ-009 Book original](../20261003-HMZ-009-book-powerset-quotient-preflight/originals/HMZ-S-026-HoTT-Book-578b85cc-hits.tex), SHA-256 `d43dac381da7f978fb1d2ff6c2c2d3cca7f9b0dab90c96cd20815c13e7ab8454`; plus `setmath.tex`. | `hits.tex:1257–1297`; `setmath.tex:363–455,487–499`. | fixes the contrasting Power Set-subset route and its universe/Done controls. |

## 派生 locator material

| File | SHA-256 | Use |
|---|---|---|
| `derived/LOCATORS.md` | `28db39d13607fa7c867f2a60d16bd33cb621a0a53fb477c502f40b4da1f0058a` | compact I/O/Done and source-payment map; original source remains authoritative. |
