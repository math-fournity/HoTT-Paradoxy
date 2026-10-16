# 粗完成观察不会恢复原 universe：Q 停止对照与无统一回填（C-357）

> **状态：** `KERNEL_ACCEPTED_WITH_SCOPE / EXACT_REPLAY_CONFIRMED / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。
>
> **理论变体：** Cubical Agda 2.8.0 + cubical 0.9，`--safe --cubical --guardedness`。

## 问题

固定 C-78 的 universe questioning process 与 C-83 的 set-truncation control。对原 universe `Type ℓ-zero`，逐层 h-level 追问永远不交出有限 `now k`；对其集合截断 `TU`，同一追问在第一步交出 `just 1`。本包把这两个完成结果和 C-83 的 `noDecoding` 合成同一个机器检查的命题。

## 精确命题

`coarseCompletionCreatesNoRestoration`（project claim `C-357`；早期 CG001 local capture 使用过临时身份 `CG001-C-84`，不作为 canonical claim ID）：

```agda
(question (Type ℓ-zero) judgeU ≡ never)
× (runFor 0 (question TU judgeTU) ≡ just 1)
× ¬ (Σ[ g ∈ (TU → Type ℓ-zero) ]
       ((A : Type ℓ-zero) → g ∣ A ∣₂ ≡ A))
```

它严格说的是：一个固定的粗化 `∣_∣₂` 让固定完成观察变成第一步停机，同时没有统一的 section 把每个被截断的原 universe 元素还回其自身。

## 证据与依赖

- C-78／`QuestioningDelay.agda`：原 universe 的询问为 `never`；
- C-83／`TruncationQuestioning.agda`：截断 universe 第一问停止，并有 `noDecoding`；
- 本包把这三个已存在的形式事实联结成一个可直接引用的 conjunction；它没有把它们改造成关于 ZFC 的命题。这样可以避免在 ZFC-HoTT 比较中把“截断后停止”误读成“原对象已恢复”。

## 负控制

`WrongObservationCompletionBridge.agda`以同层常值`Bool`当作统一decoder。它必须在类型检查时被拒，因为这不能证明对任意 `A` 有 `Bool ≡ A`。

## 当前运行状态

主运行 `20261003-CG001-ZFC-HOTT-OBSERVATION-BRIDGE-01` 已由 Cubical Agda 2.8.0 + cubical 0.9 接受，随后以同一精确命令、stdout 与 stderr 完成重放比对。负控制 `-NEG-01` 在预期的 `Bool != A` 处被内核拒绝。它们的完整范围仍以本页“禁止外推”为界。

## 禁止外推

- 不证明集合截断错误；
- 不裁定对截断发问与对原 universe 发问是否是研究发起人意义下的同一任务；
- 不形式化ZFC、Kapulkin–Lumsdaine模型或任何实际AcceptanceContract；
- 不证明ZFC时间观察力不完备、HoTT不一致或UR的现实判词。
