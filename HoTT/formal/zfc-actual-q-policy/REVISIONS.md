# ZFC 实际 Q 第一轮形式化：运行与修订谱系

## 2026-10-04：Agda 主包的首次捕获缺少 `⊥` 导入

`20261004-MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001-01` 使用
`HoTTCounterexample.agda` 时，在 `hottCounterexampleExpanded` 的结果类型处报
`NotInScope ⊥`。这是新适配器漏导入 `Cubical.Data.Empty`，尚未检查 C-360 的目标命题；该 run 保留为
`KERNEL_REJECTED / SOURCE_IMPORT_FAILURE`，不作为负控制或数学反例。

修复只加入：

```agda
open import Cubical.Data.Empty using (⊥)
```

`...-02` 随后以相同主命题通过。`...-03` 再加入编译 stdout 实际读取的
`ProductQuestioning.agda` 到 source manifest。`...-04`与`...-05`保留逐步扩展的依赖证据；后续 closure verifier 从实际 Agda stdout 发现还必须固定`DelayMonad.agda`，因此`...-06`在当前 claim、README、用户 primary、8个实际本地模块与相同外部库闭包下重放通过，现为 C-360 的 primary run。

## 2026-10-04：C-361 capture wrapper 的 receipt 字段修复

`20261004-MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001-01/02` 成功执行了 Lean，
但首次 wrapper 把 `source-manifest.json` 写入错误的 receipt key，并用绝对 source path，不能通过 project
proof-index verifier。修复 wrapper 后的 `...-03` 使用 `source_manifest` 标准字段与相对 source argument。`...-04`至`...-06`
保留后续 receipt 的逐步修订；`...-07`把保存的 `LEAN_PATH` 写入可重放的`command_argv`，并在当前 claim、README、用户 primary 和脚本快照下通过，现为 C-361 的 primary run。旧 run 保留，不覆盖。

## 2026-10-04：C-359 的 Q 观察代理与负控制修复

`ZFC1IllusionPolicy.lean` 将原先只作来源标签的 `qMissing` 收紧为
`QMissing = ¬ QObservesPromotionFailure`：一旦某个 site 同时具有 P 的适用性、`formalDone` 与
`¬ originDone`，它就是 Q 应观察到的 promotion failure。新增定理分别证明：在 actual same-Q 的条件下，HoTT-side B
构成这一观察；并因此反驳 `ZFCOneUse` 所记录的 `QMissing`。这仍是条件性 use-model consequence，不是 bare ZFC 的定理。

`...POLICY-NEG-03`原本在 Lean 的 import 位置规则处停止，因而没有到达拟定的 `qGap → P` 类型边界；它保留为
`KERNEL_REJECTED / NEGATIVE_CONTROL_SETUP_FAILURE`。负控制改为最小、无导入的命题后，`...POLICY-NEG-04`在
`gap : qGap`不能作为任意`P`的证明处正确被拒，成为 C-359 的 canonical negative control。`...POLICY-001-04`
则是增补 Q 观察代理后的初始 replay。`...POLICY-001-06`新增 pinned Lean core toolchain 和可验证的二进制散列，现为 C-359 的 primary run；它修复的是证据闭包，不改变 Lean 命题。
