# ZFC-1 与实际 Q 的第一轮机器化：精确命题与边界

> **身份：** `CURRENT_PROJECT_FORMAL_PACKAGE / FORMAL_POLICY_CONSEQUENCE_AND_NATIVE_HOTT_CONTROL / NOT_A_FORMALIZATION_OF_BARE_ZFC`。

## `MP-ZFC-ACTUAL-Q-POLICY-001` / C-359

[ZFC1IllusionPolicy.lean](ZFC1IllusionPolicy.lean) 以 Lean 4 core 形式化用户的抽象论证结构。

### 对象

- `QFingerprint` 记录 O1–O5、是否需要 bridge、是否支付 bridge、是否保留原任务的**来源证据状态**，而不是把“没有看到证据”写成 `false`。
- `QObservesPromotionFailure` 把本轮所说的观察 Q 精确化为：一个被 P 允许的 site 同时有 `formalDone` 与 `¬ originDone`。`QMissing` 是对这个观察失败的否定。它是对用户所说“Q 缺失”的形式代理，不是 bare ZFC 的已证属性。
- `MathematicalIllusionP` 是一个完成提升政策：在它适用的 Q shape 内，将 `formalDone` 升格为 `originDone`。
- `ZFCOneUse` 是 `ZFC-1 = ZFC + P` 的使用模型：它包含被接受的 base、一个明确的 `qMissing` 前提、P，以及“该 gap 使 Zeno-side P 被接受”的显式 field。它不是 ZFC 的对象语言语法或一致性模型。
- `A` 是 Zeno-side formal completion；`B` 是 HoTT-side `formalDone ∧ ¬ originDone`。

### 机器命题

1. `zfc_plus_A_iff_zfc_plus_P`：仅在另有 `A ↔ P` 时，`ZFC + A` 与 `ZFC + P` 才逻辑等价。
2. `q_gap_does_not_logically_force_P`：Q gap 单独不能推出 P；“缺 Q 允许 P”必须作为受来源审计的政策前提。
3. `zfc1_promotes_A`：在 `ZFCOneUse` 中，A 被 P 升格为 Zeno-side `originDone`。
4. `same_Q_transports_P_to_HoTT`：只有明确的完整 profile 等式才能把 Zeno-side P 许可运输到 HoTT-side。
5. `same_Q_P_with_B_exposes_promotion_failure`：若运输成立且 B 给出 HoTT-side `formalDone ∧ ¬ originDone`，B 就是 Q 应当观察到的 P 反例。
6. `zfc1_q_missing_with_same_Q_P_and_B_is_inconsistent`：上述 B 直接反驳 use-model 所记录的 `QMissing`。
7. `zfc1_same_Q_P_with_B_is_inconsistent`：同一组前提也经 P 的 `promote` 字段导出 `False`。
8. `revised_is_not_original`、`unobserved_is_not_refuted` 和 `different_Q_blocks_unlicensed_transfer` 是范围控制。

`WrongQGapForcesP.lean` 是负控制：它试图从任意 `qGap : Prop` 直接给出任意 `P : Prop`，应被 Lean 在 `gap : qGap` 不能作为 `P` 的证明处拒绝。

### 禁止外推

这些定理不证明：

- bare ZFC 不一致，或 `ZFC ⊢ False`；
- 数学共同体、IEP 或任何来源实际采用了 `ZFCOneUse`；
- Zeno 与 HoTT 已经拥有相同完整 Q；
- A 与 P 已由真实来源证明等价；
- B 已由 Lean 表示为条件前提；固定 HoTT Q 对具体 P 的原生反例证书由 C-360 在 Cubical Agda 中另行给出，二者之间的跨证明器对应仍是明确记录的桥接义务。

## `MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001` / C-360

[HoTTCounterexample.agda](HoTTCounterexample.agda) 在原生 Cubical Agda 中复用 C-358 的固定 HoTT Q，给出 B 的准确形式控制：

```text
coarseCompletion : truncated Q stops at stage one
originalCompletionFails : original universe Q has no finite halt witness
¬ MathematicalIllusionP
```

这里的 `MathematicalIllusionP` 精确等同于

```text
(stage-one completion of the truncated Q)
  → (finite halt of the original universe Q).
```

它不判断截断问题和原问题是不是同一个用户任务；它只机器证明上述提升蕴含在固定 Cubical Agda Q 上不成立。

## `MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001` / C-361

[ZenoLimitControl.lean](ZenoLimitControl.lean) 在固定几何部分和

\[
s_n = 1 - 2^{-n}
\]

上机器证明：

```text
FormalA                         = Tendsto s_n (𝓝 1)
StrictSequentialDone            = ∃ n, s_n = 1
¬ (FormalA → StrictSequentialDone)
```

因此它反驳一个**刻意严格的 P control**：“有极限结果就意味着某个有限自然数阶段已经到达终点”。它同时证明闭实数时间区间有真实终点参数并可到达 1，防止把该控制错读成“连续运动没有端点”。

该包不把 `StrictSequentialDone` 归给 IEP 或数学共同体；Standard Solution 是否采用它、修改它，还是给出另一种原任务桥，仍是来源卡问题。

## 证据层次

| 层次 | 当前证据 |
|---|---|
| Lean policy consequence | 新鲜 Lean core kernel run；无 import、无公理、无 `sorry`。 |
| HoTT B control | 新鲜 Cubical Agda native kernel run；复用 C-358 的完整固定依赖，负控制应在 `nothing != just 1` 处拒绝。 |
| 实际 Zeno／来源／ZFC policy | 未完成；按 `ZFC-Q-ACTUAL-INSTANCE-FORMALIZATION-SOP` A1–A5 继续。 |
| 跨证明器桥 | 只有外部 formal-result receipt 对应，尚不是单一 kernel theorem。 |

运行与 source-manifest 的首次失败、修复和 primary-run 选择见 [REVISIONS.md](REVISIONS.md)。
