# `zfcTr-D3-plan.md` 独立评审（第五份，Codex 接手后，2026-10-11）

> **性质**：对 `外部资料/zfcTr-D3-plan.md` 的独立评审与修订建议，附在旁边，不修改原计划文件。
> 本评审在 Codex 接管 Claude 的 CG-007 工作、并实测了本机 Lean 4.34.0 / Foundation `1fb01b72`
> 构建环境之后写成。凡未实测的均标【未实测】。

## 0. 直接回答：这个计划对吗？

**方向对，但"缺口形状"已被后续三段工作（Claude 的 W8、第三位 AI 的 `ShCraigElim` 系列、
本文作者实测）进一步收窄，且原计划 §5 的"经翻译的 Σ1 完全性移植"路线已被证明不必做。**

| 项 | 原计划说法 | 本评审结论 | 依据 |
|---|---|---|---|
| §3 的 Bridge′ 弱化（`V ⊧ σ` 输入） | 正确且关键 | **正确** | C-128（`Z0Bridge.lean`）已据此证成条件归约；本文作者未重测，采信既有收据 |
| §4 `of_provability` 语义性、搬不进 𝗜𝚺₁ | 正确 | **正确** | `LK/Interpretation.lean:443` 经完备性定理，无内化版本（全量 grep 确认，见 review-4） |
| §5 移植 ~1080 行 Σ1 完全性（L1–L5） | 主攻路线 | **不必做** | 缺口已被收成更窄的 `ShCraigElim`；Foundation 对 `Sh.craig` 直接 `inferInstance` 给出 D3 |
| §8 验收标准 | 正确，可采用 | **正确** | F-011 五件事与现有收据工具一致 |

## 1. 计划与现状的关键偏差（请接手者注意）

原计划把缺口写成"重做经翻译的 Σ1 完全性"（§5，L1–L5）。但后续工作把它收得更小、更具体：

- C-390（`Z0UniBridge.lean`）把 Z0 完整形式归约到 `ShCraigElim`：
  `∀ σ, Provable Sh.craig ⌜σ⌝ → Provable 𝗭𝗙𝗖 ⌜translate σ⌝`。
- `ShCraigElim` 经 `bwd_of_shcraig_elim`（`keyE` 的 `bwd` 方向）归约到原 `zfcTr_D3_internalize`。
- 已证零件：C-391 `iVE` 计算规则与 `isSemiformula_iT`、C-392 归纳不变量 Σ1 谓词、
  C-390 宇宙多态桥、本文作者实测确认 `iT_neg`（`ShCraigElimNegLaw.lean`，9 支全填无 sorry）
  证好——这意味着原计划 §4 担心的"`neg` 相容律缺失"**已不是障碍**。

**结论**：原计划的"§5 移植 Σ1 完全性"是过头的路线；真正剩下的是 `ShCraigElim` 归纳的
8 个 `sorry` 支（其中 `hAnd`/`hOr`/`hAxL`/`hCut` 本文作者已实测类型可填，`hAll`/`hExs`/
`hShift` 需 `iT_setShift`/`iT_substs1` 这两个照 `iT_neg` 写的相容律，`axm` 需读
`CraigTrick.lean`）。详见同目录 `Z0-D3-攻关包-给外部AI/` 的 `00-缺口精确定位.md` 与
`03-九支归纳任务拆解.md`。

## 2. 对 §4"为什么现有工具填不上"的修正

原计划 §4 列了三条，其中第 3 条"`sigma_one_complete` 给错理论的编码"——现在看，
这正是"为什么不能直接套、必须走 `ShCraigElim`"的原因，本评审**同意**。但第 1 条
（`of_provability` 语义性）的真正后果不是"需要重做 Σ1 完全性"，而是"需要对 `Sh.craig`
的推导编码做结构归纳消去"——即 `ShCraigElim`。所以这个计划**整体可读**，只是它推荐的
主攻路线（§5）比实际需要的更重；接手者应走 `ShCraigElim` 归纳，而不是 §5 的 L1–L5。

## 3. 第三位 AI 反馈的纠正

第三位 AI 在沙箱里既无 Lean/Mathlib/Foundation、zip 又只含 4 个模块，因此断言"缺
`D3.lean`/`CraigTrick.lean`/`Proof/Typed.lean` 等 20 个模块、交不出编译骨架"。**这一判断
在本机不成立**：Foundation 全量 308 个 `.lean`（commit `1fb01b72`）就在
`/Volumes/D/HoTT-toolchain-cache/foundation-src/`，且已构建；GitHub 上每个模块都有
`raw.githubusercontent.com/.../1fb01b72.../<路径>` 地址（本评审实测 `D3.lean` 返回 200/8708B）。
本项目实际依赖的 Foundation 闭包是 **167 个模块**（见 `Z0-D3-攻关包-给外部AI/Foundation_fetch_list.txt`，
已由 import 传递闭包算出，非手数）。第三位 AI 说的"两个独立 AI 在同一处卡住"**不能成立**，
因为它根本没编译过、对着看不见的 API 写结论。

## 4. 给执行 AI 的建议（修订后的最小路线）

1. 先填 `hAnd`/`hOr`（用 `iT_and`/`iT_or` + `Derivable.and_m`/`or_m`，本文作者已实测类型对得上）。
2. 填 `hAxL`/`hCut`（用已证的 `iT_neg` 把 `iT (neg p)` 化成 `neg (iT p)`）。
3. 照 `iT_neg` 的模板写 `iT_setShift`/`iT_substs1`，填 `hAll`/`hExs`/`hShift`。
4. 读 `CraigTrick.lean` 填 `axm`（唯一用到 `𝗭𝗙𝗖` 公理的支）。
5. 把 8 支接进 `ShCraigElimSetup.induction_setup`，得到无 sorry 的 `ShCraigElim`；
   `Z0Blocked.lean` 的 `sorry` 改为引用它。

**不要**走原计划 §5 的 ~1080 行 Σ1 完全性移植（已由 `ShCraigElim` 取代）。

## 5. 环境（本机已实测可用）

- Lean 4.34.0 @ `/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0`
- Foundation 源 `1fb01b72`：`/Volumes/D/HoTT-toolchain-cache/foundation-src`（308 个 .lean）
- Foundation olean 构建：`/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean`
- Mathlib `5ed29652`：`/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/`
- 增量编译：`/tmp/d3build/devbuild.py`（开发期；收据用 `capture_run.py`）
- GitHub：`https://github.com/FormalizedFormalLogic/Foundation` @ `1fb01b72de546e1b50821fd05b1314a8d958583f`
