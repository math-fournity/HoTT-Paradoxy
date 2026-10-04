# Lean 政策核与 Cubical Agda HoTT 控制：跨 kernel 命题对应表

> **身份：** `EXTERNAL_FORMAL_RESULT_ASSUMED_WITH_RECEIPT / NOT_A_SINGLE_KERNEL_TRANSLATION`。

Lean 与 Cubical Agda 检查不同的形式系统。本表的作用是让跨系统使用可审计；它不把一个系统的 theorem 自动导入另一个系统。

## 1. 精确对应

| 层 | Lean `ActualQPolicy.lean` | Cubical Agda `HoTTCounterexample.agda` | 对应方向 | 当前状态 |
|---|---|---|---|---|
| 形式完成 | `task.formalDone state` | `runFor 0 (question TU judgeTU) ≡ just 1` | Agda witness 可作为未来 Lean B 实例的 `formalDone` 证据候选。 | `EXTERNAL_FORMAL_RESULT_WITH_RECEIPT` |
| 原过程完成 | `task.originDone state` | `Questioning.Halts (Type ℓ-zero) judgeU` | 两者都意在保留未粗化的完成条件。 | `INTERPRETIVE_MAPPING_NOT_YET_PROVED` |
| B 的形状 | `∃ state, formalDone state ∧ ¬ originDone state` | `¬ (coarseCompletion → originalHalting)`，且已有 `coarseCompletion`。 | 由 Agda 的 `coarseCompletion` 与 `originalCompletionFails` 可构成“某一固定粗状态完成而原状态不完成”的模式。 | `FORMAL_SHAPE_MATCHED_EXTERNALLY` |
| 强 P | `MathematicalIllusionP.promote` | `CompletionReflectsOriginalHalting` | 在这一个 HoTT control 中，P 的具体化为 completion-reflection 蕴含。 | `EXACT_WITHIN_FIXED_AGDA_TASK` |
| 同一实际 Q | `TaskEquiv` 保留 six fields | 无对应 Agda theorem | 不能因两个文件都含“completion”就填写。 | `NOT_ESTABLISHED` |
| ZFC-1 后果 | `zfc1_same_actual_Q_P_with_B_is_inconsistent` | 不含 ZFC 定义 | 若把 Agda B 作为 Lean 前提，必须显式标注外部 receipt。 | `CONDITIONAL_ONLY` |

## 2. 当前能安全使用的组合规则

```text
C-358（Cubical Agda）
  + 明示的跨 kernel 解释映射
  ⇒ 可作为 Lean B 前提的候选证据

Lean 的 ZFC-1 consequence
  + 实际 TaskEquiv + 来源归属的 P
  ⇒ 条件性 policy conflict
```

第二行的前两项目前没有由 kernel 或来源支付。因此当前正确状态是：**两个原生 proof assistant 各自完成了自己的局部数学命题；跨系统的实际 Q 仍是开放证明义务。**

## 3. 不能省略的两个反控制

1. **理论变体控制。** KLV 单纯集模型、HoTT Book 的基础性叙述、Cubical Agda、guarded Delay 和本项目 `QuestioningDelay` 并非同一演算。未给保过程翻译时，任何“ZFC 已经接受这个 HoTT Q”的说法均超出来源。
2. **任务控制。** 即使存在一个形式 completion 和一个未完成的原过程，也还要证明 Zeno／圆环和该 HoTT Q 的 `State/input/step/observe/formalDone/originDone` 全部对应；标签相同、O1–O5 的状态相同或比喻相似都不够。
