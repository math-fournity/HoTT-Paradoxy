# M1-A：fixed H0 的集合值有限观察 trace

> **身份：** `FORMAL_CLAIM_SPECIFICATION / ZFC-H0-FINAL-PROOF-CLOSURE-SOP / M1_FRAGMENT`。
>
> **状态：** `KERNEL_ACCEPTED_WITH_SCOPE / H0_OPERATIONAL_FRAGMENT_TRACE_MACHINE_PROVED`。

## Claim

在固定 Cubical Agda 2.8.0 + cubical 0.9 的 H0 依赖中，定义：

```text
Trace       = ℕ → Maybe ℕ
trace(d,n)  = runFor n d
silentTrace = λ n → nothing
```

待机器检查的命题为：

1. `Trace` 是一个 h-set；
2. `trace never = silentTrace`；
3. trace 保持 `Delay ℕ` 的 path equality；
4. 对每一个 `Judge (Type ℓ-zero)`，
   `trace (question (Type ℓ-zero) judge) = silentTrace`；
5. 因而任意有限 fuel 与任意 answer 都不能让这个 trace 返回 `just answer`；
6. 负控制中，`fuel = 0` 时的 `just 1` 主张必须被 Cubical Agda 拒绝。

## 严格范围

这是 exact `Delay ℕ`／`runFor` observation 的原生 Cubical Agda 结果。它把 H0 的过程输出投影到一个集合层 trace，但**不**构造完整 CCHM cubical-set model，不解释 EM1、suspension、truncation、univalence 或整个 Cubical Agda 2.8.0 + cubical 0.9 library，也不证明 bare ZFC 的 `C_accept`、`AdequacyLift`、`SameFullQ` 或 Q 缺失。

它的成功状态只能写为：

```text
H0_OPERATIONAL_FRAGMENT_TRACE_MACHINE_PROVED
```

它不是 `H0MAP_MACHINE_PROVED`。

## 运行与负控制

- 主运行：`HoTT/verification/runs/20261004-MP-ZFC-H0-TRACE-001-05/`，Agda 2.8.0-3d04bac + cubical v0.9，`--safe --cubical --guardedness` 源码、`--ignore-interfaces` 全量重检，退出码 `0`，stderr 为空。
- 负控制：`HoTT/verification/runs/20261004-MP-ZFC-H0-TRACE-NEG-001-05/`，退出码 `42`；伪造 `trace (question Type judgeU) 0 ≡ just 1` 时，内核在 `nothing != just 1` 拒绝。
- 证据范围：主运行实际检查 `H0TraceObservation.agda`、`PedometerSemantics.agda`、`DelayMonad.agda`、`QuestioningDelay.agda` 和 pin 的 cubical v0.9 tree。它只认证该 trace 的原生计算/路径命题。
