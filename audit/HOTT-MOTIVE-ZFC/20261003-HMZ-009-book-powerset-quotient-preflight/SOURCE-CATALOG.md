# HMZ-009：来源目录、原件身份与 locator

## `HMZ-S-026` — HoTT Book 578b85cc 的三份原始源码

| 原件 | SHA-256 | 上游与本地 provenance | 本轮角色 |
|---|---|---|---|
| `originals/HMZ-S-026-HoTT-Book-578b85cc-logic.tex` | `76ac2e06ffa133ede0612584fef4b9c81d698d4e0b7a4ec683131448edfed2f2` | 上游 `https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/logic.tex`；从已追踪的 `sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc/logic.tex` 复制。 | Power Set 定义、propositional resizing 和 predicativity 限定。 |
| `originals/HMZ-S-026-HoTT-Book-578b85cc-hits.tex` | `d43dac381da7f978fb1d2ff6c2c2d3cca7f9b0dab90c96cd20815c13e7ab8454` | 上游同 commit 的 `hits.tex`；同上复制。 | “set theoretic approach”、等价类 predicate 和 quotient equivalence。 |
| `originals/HMZ-S-026-HoTT-Book-578b85cc-setmath.tex` | `c9684dffba31892b12839e60eac769706faa2301b7fba7b930f5acf4b097563e` | 上游同 commit 的 `setmath.tex`；同上复制。 | quotient 作为 Power Set 子集、universe cost、external/internal construction 与内部 \(V\) 的 ZFC control。 |

本项目的上游 snapshot 由 Git commit `cc30c530201a06dae6f0c2dc48f68a7289eed8ed` 导入；本轮只复制、哈希并读取，未改写来源。Book source 是技术／教材原典，不把这一段误称为某一位作者单独的历史动机陈述。

### 精确 locator

| 主题 | 原件 locator | 本项目解释范围 |
|---|---|---|
| resizing 是显式 axiom；Power Set \(\mathcal P A\) 可在 resizing 下定义为 \(A\to\Omega\) | `logic.tex:525–555` | 记录 HoTT-side universe/impredicativity payment；不是 bare ZFC 的 axiom proof。 |
| set-theoretic quotient 为 equivalence classes 的 Power Set 子集；定义 \(A\sslash R\) | `hits.tex:1257–1277` | 这是本预检的直接 construction bridge。 |
| \(A\sslash R\simeq A/R\)，且 `A//R` raises universe unless resizing | `hits.tex:1279–1297` | 显式 Done 比较和同 universe payment。 |
| 第二 quotient construction、coequalizer form、两种 quotient 等价 | `setmath.tex:363–455` | 补足同一 quotient-style output 的 source report。 |
| external setoids/exact completion 与 internal HIT constructions 的区分 | `setmath.tex:487–499` | 防止把两种交付接口混成“同一 Done 已无成本实现”。 |
| type theory + Choice + universe 的内部 \(V\) 模型 ZFC；Power Set 在该模型中是 function type | `setmath.tex:1755–1761` | 反类比控制：这是 HoTT 内模型，不是 bare ZFC Power Set consumer。 |

## 复用的 ZFC / ZF 形成来源

| ID | 已归档原件／哈希 | 本轮复用事实 | 限度 |
|---|---|---|---|
| `HMZ-S-007` | [HMZ-001 Metamath `ax-pow`](../20261003-HMZ-001-primary-motives/originals/metamath/ax-pow.html)，SHA-256 `1d418aea8c4b91a4b0dda2c59c075a3ccb2f5ed36df0200ff0a7eae53cb7d0c0`；`pwex`，SHA-256 `eb1b4c57776993385ff563f207ec5a0e3cb25a73fdd841c65428d9b0f2a852db`。 | `ax-pow` 把 Power Set 说明为包含给定 set 一切子集的 set 的存在；`pwex` 给出 class notation。 | `PROOF_FORMALIZATION`；没有本预检需要的 actual quotient consumer 或 Done。 |
| `HMZ-S-010` | [HMZ-001 Shulman PDF](../20261003-HMZ-001-primary-motives/originals/HMZ-S-010-Shulman-2008-Set-Theory-for-Category-Theory.pdf)，SHA-256 `3f1e2d9f9a7a026ab54cd982cfad8742c9c38e9696cb60b52e18dfaa90298012`。 | pp. 3–4（派生行 165–194）把 Separation 与 Power Set 列为 accepted ZFC axioms，并说明 definable subset formation。 | 该段支持 formation layer，不给本 preflight 的 \(A,R\) quotient consumer。 |

## 派生材料

| 文件 | SHA-256 | 生成／用途 |
|---|---|---|
| `derived/LOCATORS.md` | `50c8af5cbd40c67d35ea513874d8b5e0337e644cec5f009a4fe5b3e1a24b6ac9` | 对原件的 locator、source fact 与禁止外推摘要；不复制大段正文。 |
