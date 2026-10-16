# `zfcTr-D3-plan.md` 独立修订说明（Codex 接手复核，2026-10-11）

> 性质：对 `外部资料/zfcTr-D3-plan.md` 的独立评审与修订建议，附在旁边，不修改原计划文件。
> 本说明在完整读取 `dev` 工作树实物（非仅摘要）后写成。凡未本机实测的均标【未实测】。

## 0. 直接回答：这个计划对吗？

**方向对，目标命题精确，但"缺口形状"已被后续多段工作进一步收窄，且原计划 §5 主推的
"经翻译的 Σ1 完全性移植（L1–L5，约 1080 行）"已被证明不必做。** 真正剩下的数学工作，
是 `ShCraigElim` 归纳的 10 个规则支（其中 2 支已填骨架、8 支待填）。

| 项 | 原计划说法 | 本复核结论 | 依据（本机实物） |
|---|---|---|---|
|--- `§1` 目标命题 `zfcTr_D3_internalize` | 精确 | **精确且仍是唯一阻塞** | `HoTT/.../GodelQ/ZFC/Z0Blocked.lean:35` 的 `sorry` 仍在 |
|--- `§3` Bridge′ 弱化（`V ⊧ σ` 输入）| 正确且关键 | **正确** | 归约链 `Z0UniBridge`/`Z0Full` 已据其证成（前序收据） |
|--- `§4` `of_provability` 语义性、搬不进 𝗜𝚺₁ | 正确 | **正确** | `Foundation/.../LK/Interpretation.lean:443` 经完备性定理，无内化版本（已读源码确认） |
|--- `§5` 移植 ~1080 行 Σ1 完全性 | 主攻路线 | **不必做** | 缺口已收成更窄的 `ShCraigElim`；Foundation 对 `Sh.craig` 直接 `inferInstance` 给 D3 |
|--- `§8` 验收标准（F-011） | 正确 | **正确，应采用** | 与现有 `capture_run.py`/`verify_cg001_run.py` 一致 |

## 1. 与现状的关键偏差（接手者必读）

原计划把缺口写成"重做经翻译的 Σ1 完全性"。后续工作把它收得更小、更具体，且**前一个 Codex
交接摘要对进度作了乐观化描述，须校正**：

- `ShCraigElimNegLaw.lean`（`iT` 与 `neg` 的一般相容律，9 个构造子支）**确已 0-sorry 编译通过**；
  但 `ShCraigElimBranches.lean` 的文档仍写"一般 `neg` 相容律尚不存在"——**文档陈旧，未回改**。
- `ShCraigElimSetup.induction_setup` 的 10 个规则支**全部仍是 `sorry` 骨架**，尚未有任何一支被填。
  即"已证 9 支"不成立；真实是 neg 律证了但**没接进归纳**，归纳 10 支一个都没填。
- 所以接手第一件事是：把 `iT_neg`（已证）接进 `axL`/`cutRule`，并照其模板写 `iT_setShift`/
  `iT_substs1` 以填 `shiftRule`/`allIntro`/`exsIntro`，再读 `CraigTrick.lean` 填 `axm`。

## 2. 对 §4"为什么现有工具填不上"的修正

§4 三条里，第 1 条（`of_provability` 语义性）的真正后果不是"需要重做 Σ1 完全性"，而是"需要对
`Sh.craig` 的推导编码做结构归纳消去"——即 `ShCraigElim`。第 3 条（`sigma_one_complete` 给错理论编码）
正是"为何不能直接套、必须走 `ShCraigElim`"的原因，本复核同意。故原计划**整体可读**，但 §5 的
L1–L5 路线比实际需要的更重；接手者应走 `ShCraigElim` 归纳，而非 §5 的 Σ1 完全性移植。

## 3. 第三位 AI 反馈的纠正

第三位 AI 在沙箱里既无 Lean/Mathlib/Foundation、zip 又只含 4 个模块，因而断言"缺 `D3.lean`/
`CraigTrick.lean`/`Proof/Typed.lean`/`R0/Basic.lean` 等 20 个模块、交不出编译骨架"。**该判断在本机
不成立**：Foundation 全量 308 个 `.lean`（commit `1fb01b72`）就在 `/Volumes/D/HoTT-toolchain-cache/
foundation-src/`，且已构建；每个模块都有 `raw.githubusercontent.com/.../1fb01b72.../<路径>` 地址
（实测 `D3.lean` 返回 200/8708B）。项目实际依赖闭包是 **167 个模块**（已由 import 传递闭包算出，
见 `外部资料/Z0-D3-攻关包-给外部AI/Foundation_modules_urls.txt`）。故"两个独立 AI 在同一处卡住"
不能成立——第三位 AI 根本没编译过、对着看不见的 API 写结论。

> 但第三位 AI 的一点诉求合理：**若外部 AI 运行环境有网络但无本地 Foundation 缓存**，则应直接给
> 出每个模块的精确 GitHub raw URL 让其 `curl`，而不必打包 308 个文件。本复核据此新建
> `外部资料/Z0-D3-攻关包-网络完备版/`，含 167 个依赖模块的逐行 URL 与 `fetch_foundation.sh`。

## 4. 修订后的最小路线（给执行 / 外部 AI）

1. 填 `andIntro`/`orIntro`（`iT_and`/`iT_or` + `Derivable.and_m`/`or_m`；类型链路已实测对得上）。
2. 填 `axL`/`cutRule`（用已证 `iT_neg` 把 `iT (neg p)` 化成 `neg (iT p)`）。
3. 照 `iT_neg` 模板写 `iT_setShift`/`iT_substs1`，填 `shiftRule`/`allIntro`/`exsIntro`（核心难点）。
4. 读 `CraigTrick.lean` 填 `axm`（唯一用到 `𝗭𝗙𝗖` 公理的支）。
5. 把 8 支接进 `induction_setup`，新增无 `sorry` 的 `ShCraigElim`；`Z0Blocked.lean` 的 `sorry` 改为引用它。

**不要**走原计划 §5 的 ~1080 行 Σ1 完全性移植（已由 `ShCraigElim` 取代）。

## 5. 环境（本机已实测可用）

- Lean 4.34.0 @ `/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0`
- Foundation 源 `1fb01b72`：`/Volumes/D/HoTT-toolchain-cache/foundation-src`（308 个 .lean）
- Foundation olean 构建：`/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean`
- Mathlib `5ed29652`：`/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/`
- 增量编译：`/tmp/d3build/devbuild.py`（开发期；收据用 `capture_run.py`）
- GitHub：`https://github.com/FormalizedFormalLogic/Foundation` @ `1fb01b72de546e1b50821fd05b1314a8d958583f`
  单文件模板：`https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de546e1b50821fd05b1314a8d958583f/<相对路径>`

## 6. 八方向覆盖

形式化追踪 `05-分支上的形式包/` 记载：八个 worktree 方向的覆盖已于 2026-10-10 闭合
（CG001-C-123..C-127、CG001-C-387，均在本机 Foundation/Mathlib 构建树上重放）。本说明不重做该覆盖；
主线"形式化与机器证明"的剩余工作**只**是 Z0 完整形式的 D3（`ShCraigElim`）。
