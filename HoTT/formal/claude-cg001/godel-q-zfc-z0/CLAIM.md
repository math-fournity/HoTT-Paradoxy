# CG001-C-103：Z0 的条件形式——𝗭𝗙𝗖 的算术影子与哥德尔第二不完备定理

> **证明包：** `MP-CG001-GODEL-Q-ZFC-Z0-001`（主包）；负控制 `MP-CG001-GODEL-Q-ZFC-Z0-NEG-ISIGMA1-001`。
>
> **目标包：** CG-006 的 S6（`.claude/goals/CG-006-zfc-complete-formalization/`），本机会话 d58e0c0d，Opus 5.5，2026-10-08。研究发起人 2026-10-07【原话】“你要综合所有之前的AI的所有工作，推进到完全的形式化和机器证明的完成。”
>
> **理论变体：** 同 `godel-q-zfc`：Lean 4.34.0 内核，Mathlib `5ed29652…`，FormalizedFormalLogic/Foundation `1fb01b72`；经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。
>
> **身份：** 条件定理。两条前提就是 S6 的卡点，本包**没有**证明它们。它是 Z0 的最小可续形式状态：把“还差什么”写成精确的 Lean 命题，并证明“差的就是这些”。

## 1. 记号

- `σᵗ := arithTrln.translate σ`：S3 的直接翻译（ℒₒᵣ 到 ℒₛₑₜ，把算术解释在 ω 上；`godel-q-zfc` 的 `GodelQ/ZFC/ArithInterp.lean`）。
- `Sh := {σ ∣ 𝗭𝗙𝗖 ⊢ σᵗ}`：𝗭𝗙𝗖 的算术影子。
- `Sh.RE`：Foundation 的 `Theory.RE`，即 `REPred (· ∈ Sh)`。
- `𝗜𝚺₁ ⪯ Sh`：Foundation 的 `WeakerThan`：𝗜𝚺₁ 证明的每个句子，`Sh` 都证明。
- `Sh.craig`：Craig 技巧给出的、与 `Sh` 等价的 Δ1 公理化；`Sh.craig.consistent`：它的标准一致性句（𝚷₁）。

## 2. 精确命题（类型逐字见 `GodelQ/ZFC/Z0Shadow.lean`）

| 编号 | 定理 | 内容 | 前提 |
|---|---|---|---|
| CG001-C-103 | `Sh_provable_iff`、`Sh_consistent`、`R0_le_Sh`、`zfc_z0_conditional`、`sh_z0_conditional` | `Sh ⊢ σ ↔ 𝗭𝗙𝗖 ⊢ σᵗ`；`Sh` 一致；`𝗥₀ ⪯ Sh`；若 `Sh.RE` 且 `𝗜𝚺₁ ⪯ Sh`，则 `𝗭𝗙𝗖 ⊬ (Sh.craig.consistent)ᵗ`，并且 `Sh ⊬ Sh.craig.consistent` | 前三条无前提（一致性经 Foundation 的 `zfc_consistent`，即 Lean 元层的 `Universe` 模型）；后两条以 `[Sh.RE] [𝗜𝚺₁ ⪯ Sh]` 为前提 |

证明路线：`zfc_z0_conditional` 由 Foundation 的 `craig_consistent_unprovable_of_RE`（对 r.e. 且扩张 𝗜𝚺₁ 的一致算术理论 T，`T ⊬ T.craig.consistent`）与 `Sh_provable_iff` 得到：若 𝗭𝗙𝗖 证明了那句一致性句的翻译，它就属于 `Sh`，于是 `Sh` 证明了自己的一致性句，与第二定理矛盾。

## 3. 两条前提就是卡点

1. **`Sh.RE`**：要证 `σ ↦ 𝗭𝗙𝗖 ⊢ σᵗ` 可枚举。𝗭𝗙𝗖 的可证性已经是 Σ1（经 `𝗭𝗙𝗖.Δ₁`，CG001-C-95、C-97）；缺的是翻译 `arithTrln.translate` 的可计算性，或它在 𝗜𝚺₁ 内部的 Σ1 定义（与 `numCode` 同类的内部递归，但沿公式结构走）。
2. **`𝗜𝚺₁ ⪯ Sh`**：要证 𝗭𝗙𝗖 解释 𝗜𝚺₁。按 `arithInterp : 𝗭𝗙𝗖 ⊳ 𝗥₀` 的路线，需要在每个 𝗭𝗙𝗖 模型的 ω 上验证 𝗣𝗔⁻ 的公理与 Σ1 归纳：归纳实例由分离公理在模型中取子集，再用“ω 是最小归纳集”（`IsInductive.ω_subset`）给出。

已经证明的 `𝗥₀ ⪯ Sh` 不能代替第 2 条：负控制在缺少 `𝗜𝚺₁ ⪯ Sh` 实例处被拒（§5）。

## 4. 与 Z0 原意的距离

- **第三步没有做**：`Sh.craig.consistent` 说的是“𝗭𝗙𝗖 的算术影子（经 Craig 公理化）不矛盾”。在 Lean 元层，`Sh` 矛盾当且仅当 𝗭𝗙𝗖 矛盾（由 `Sh_provable_iff` 与翻译保持 `⊥`）。把这一等价搬进 𝗜𝚺₁ 内部，才能把结论读成“𝗭𝗙𝗖 证明不了 Con(𝗭𝗙𝗖)”，即研究发起人所问 Z0 的完整形式（CG-005 综合报告 §3）。
- 本包把 Z0 化成了两条精确的引理（另加第三步的内部化），没有越过它们。

## 5. 负控制

| proof id | 文件 | 去掉的前提 | 预期 |
|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-Z0-NEG-ISIGMA1-001` | `GodelQ/Negative/WrongZ0WithoutISigma1.lean` | `𝗜𝚺₁ ⪯ Sh`（保留 `Sh.RE`） | 拒绝：细化阶段找不到实例 `𝗜𝚺₁ ⪯ Sh` |

## 6. 依赖与运行

- 依赖模块 15 个，与 `godel-q-zfc` 的同名文件逐字节相同（`ProcessObservation`、`EffectiveTheory`、`GodelZenoRunner`、`FoundationArith`，以及 `ZFC/` 下的 `SetLanguage`、`SchemaDelta1`、`ReplacementDelta1`、`ZFCDelta1`、`NumeralCode`、`NeverRE`、`OmegaArith`、`NumeralSemantics`、`ArithInterp`、`R0Model`、`Effective`）。新文件只有 `GodelQ/ZFC/Z0Shadow.lean` 与负控制。
- 驱动：`.claude/goals/CG-006-zfc-complete-formalization/tools/zfc_lean_check.py`（原样复用，包路径是参数）；固定记录：`tools/make_z0_pins.py`（导入闭包 1,893 个模块）；捕获：`tools/capture_z0_run.py`。后两件是 `godel-q-zfc` 冻结工具的副本，只改了包路径与说明。运行表见 `README.md`。

## 7. 禁止外推

1. 不推出 Z0 对 𝗭𝗙𝗖 成立，也不推出“𝗭𝗙𝗖 证明不了 Con(𝗭𝗙𝗖)”的任何 𝗭𝗙𝗖 内部形式。
2. 两条前提是数理逻辑的标准结果（ZFC 的定理集可枚举且翻译可计算；ZFC 解释 PA），但本包没有证明它们；`zfc_z0_conditional` 的价值在于把卡点写成精确的 Lean 命题，而不是宣称已经越过卡点。
3. `Sh` 的一致性来自 Lean 元层的 `Universe` 模型，不是 𝗭𝗙𝗖 内部可证。
4. 不推出 `ZFC ⊢ ⊥`。
