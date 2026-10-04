# ZFC 实际 Q：第一轮政策形式化包

本目录实现 `ZFC-Q-ACTUAL-INSTANCE-FORMALIZATION-SOP` 的第一项可检查产物：把研究发起人提出的 `Q` 缺失、数学幻觉 `P`、Zeno-side A、HoTT-side B 和 `ZFC-1 = ZFC + P` 的**逻辑结构**写成两个原生 proof assistant 中可检查的命题。

- `ZFC1IllusionPolicy.lean`：Lean core 中的政策 consequence；它把 Q 表示为对 `formalDone ∧ ¬ originDone` 的可观察反例，并要求所有历史／来源事实作为明确前提。
- `HoTTCounterexample.agda`：Cubical Agda 中固定 HoTT Q 对具体 P 的反例；它复用 C-358 而不把其偷换成 ZFC 模型事实。
- `ZenoLimitControl.lean`：固定几何部分和中，形式极限不能推出有限阶段终点的严格 P 反控制；另给闭连续时间端点正控制。
- `ZenoSourceCompletionContract.lean`：固定 Norton/IEP 来源卡的严格／缩减完成合同的 Lean core 后果；不把来源分类本身伪称内核定理。
- `HoTTCompletionContract.agda`：将固定 Cubical Agda B 封装为通用 completion-gap schema；共同形状不等于同一完整 Q。
- `CROSS-KERNEL-COMPLETION-CONTRACT.md`：两条 kernel 的 schema 对应和禁止跨越。
- `WrongQGapForcesP.lean`：负控制，缺失 Q 不能仅凭逻辑自动推出 P。
- `REVISIONS.md`：C-360/C-361 首次捕获失败及 manifest/receipt 修复的不可覆盖谱系。
- `WrongHoTTCounterexample.agda`：负控制，伪造 P 必须被原 Q 的 `nothing != just 1` 拒绝。
- `CLAIM.md`：每个命题、桥与禁止外推。

这不是 actual Q instance 的完成，也不是 bare ZFC 的形式化。它的完成形态是：来源能够认证实际 Zeno／圆环 Done、实际 acceptance policy、实际 same-Q 对应和桥接 payment；若其中任一项失败，结果应停在有界的来源缺口或任务替换判词。
