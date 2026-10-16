# 粗完成不能反射原 Q 的有限完成（C-358）

> **状态：** `KERNEL_ACCEPTED_WITH_SCOPE / PENDING_CANONICAL_INDEX`。
>
> **理论变体：** Cubical Agda 2.8.0 + cubical 0.9，`--safe --cubical --guardedness`。

## 精确命题

固定原 universe 问题 `question (Type ℓ-zero) judgeU` 与集合截断问题
`question TU judgeTU`。定义：

```agda
CompletionReflectsOriginalHalting : Type
CompletionReflectsOriginalHalting =
  runFor 0 (question TU judgeTU) ≡ just 1
  → Questioning.Halts (Type ℓ-zero) judgeU
```

主命题 `coarseCompletionDoesNotReflectOriginalHalting`（claim `C-358`）是：

```agda
¬ CompletionReflectsOriginalHalting
```

也就是说，固定截断版 Q 在第一步给出完成，不能推出原 universe Q 有任何有限的 halting witness。

## 依赖与负控制

- 原 universe 不会给出有限 halt：`universeQuestioningNeverAnswers judgeU`；
- 截断版在第一步给出 `just 1`：`truncUniverseStopsAtOne judgeTU`；
- 负控制硬把原 Q 的 fuel-0 结果写成 `just 1`，应被拒绝，因为原运行的结果是 `nothing`。

## 当前运行状态

主源码已由 Cubical Agda 2.8.0 + cubical 0.9 接受。负控制的第一运行仅因漏导入 `just` 在 scope checking 处被拒，不能作为反控制；最小修复后的新运行必须在原 Q 的 `nothing != just 1` 处拒绝。完整失败谱系见 `REVISIONS.md`。

## 禁止外推

- 不证明集合截断错误；
- 不决定截断问题与原问题是否是研究发起人意义下的同一任务；
- 不形式化 ZFC、KLV 模型或任何实际基础验收器；
- 不证明 ZFC 时间观察力不完备、HoTT 不一致或 UR 的现实判词。
