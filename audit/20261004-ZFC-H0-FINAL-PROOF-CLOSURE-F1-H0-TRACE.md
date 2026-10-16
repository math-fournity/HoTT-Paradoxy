# ZFC-H0 总证明闭环：F1-A fixed H0 的有限观察 trace

> **身份：** `FORMALIZATION_PROGRESS_RECORD / M1_FRAGMENT / NOT_FULL_H0MAP / NOT_BARE_ZFC_CONCLUSION`。

## 1. 为什么这一步是总闭环的开始，而不是另一份 fixture

fixed `H0` 的结果不是一个没有行为内容的命题：`QuestioningDelay` 的输出是 `Delay ℕ`，其 `runFor` 指定有限 fuel 的观察。总 SOP 的 M1 要求我们最终获得从 exact H0 到一个明确语义 target 的逐字段 `H0Map`。全模型尚未构造之前，最小不换题的切片是先固定 H0 **实际输出层**的 map：

```text
Delay ℕ  ── trace(d,n) = runFor n d ──>  ℕ → Maybe ℕ
```

右侧是 h-set。它不是“ZFC 的集合模型”，但它把 exact H0 的每个有限观察投影到一个集合值对象，因此后续 CCHM/ZFC transport 必须至少保留这个接口。

## 2. 来源与理论变体

本包直接导入固定 Cubical Agda 2.8.0 + cubical 0.9 的：

- `PedometerSemantics.Delay`、`never` 与 `runFor`；
- `DelayMonad.runForNever`；
- `QuestioningDelay.universeQuestioningRunsNothing`。

Agda 的 coinductive record 文档说明这种对象允许无限深度、以 copattern 定义，并禁止 eta equality 以避免类型检查循环；Cubical Agda 论文也把 coinductive types、projection copatterns 与 path equality 的相互作用列为其特征。它们说明本切片的语法/计算语义身份，但不构成 CCHM/ZFC full model theorem。

## 3. C-365

`H0TraceObservation.agda` 机器证明：

1. `Trace = ℕ → Maybe ℕ` 是 h-set；
2. `trace never ≡ silentTrace`；
3. trace 保持 `Delay ℕ` 的 path equality；
4. 对任意 H0 Judge，`trace (question (Type ℓ-zero) judge) ≡ silentTrace`；
5. 因而任意有限 fuel 和任意候选 answer 都不能出现 `just answer`。

canonical 主运行 `20261004-MP-ZFC-H0-TRACE-001-05` 使用 pinned Agda/cubical assets、`--ignore-interfaces`，退出 `0`。canonical 负控制 `20261004-MP-ZFC-H0-TRACE-NEG-001-05` 把 fuel 0 的 exact universe trace 伪写为 `just 1`，在 `nothing != just 1` 处以退出 `42` 被拒。预索引 `-01`、schema-complete `-02`、registry-replay `-03` 和总SOP更新前 `-04` 运行保留于相邻目录；最终 recapture 原因见 `REVISIONS.md`。

## 4. 它没有支付什么

`C-365` 只支付 `M1-A / H0_OPERATIONAL_FRAGMENT_ONLY`。它尚未支付：

- CCHM 或 set-theoretic model 对 Cubical Agda 2.8.0 + cubical 0.9 的完整解释；
- `EM₁`、suspension、truncation、univalence、universe 和 h-level facts 的同一模型覆盖；
- trace target 到 bare ZFC object theory 的解释；
- `C_accept`、`AdequacyLift`、P、Q、SameFullQ 或最终 ZFC 归因。

下一 F1 动作必须是一个具体 target 的 full feature-coverage matrix；不能把 C-365 重命名为完整 H0Map。
