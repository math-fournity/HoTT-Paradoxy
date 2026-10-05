# `MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001`：精确主张与禁止外推

## C-375：保留 graph domain 的时间 primitive 消去控制

```lean
theorem graph_only_determines_endpoint (endpoint : Time) :
    Determines graphOnly (fun trace => EndpointAvailable trace endpoint)
```

### 形式假设

对每个 `GraphTrace`：

```lean
domain_is_time : ∀ t, (∃ x, graph t x) ↔ time t
```

### 严格结论

存在一个 decoder，只看 `graphOnly trace`，即可在每个固定 endpoint 给出
`trace.time endpoint`。该 decoder 是 graph domain。

### 禁止外推

- 不证明 ZFC 的一个对象语言定理、模型存在性、一致性或不一致性；
- 不重放 Sant'Anna--Bueno 的 Padoa proof 或 MSS axioms；
- 不证明实际连续运动、physical endpoint arrival 或 OriginDone；
- 不证明所有 ZFC 表达都保留每一种时间过程观察；
- 不证明 bare ZFC 已经承担 `Q_norm`、bridge 或 application adequacy 责任。

## C-376：function-only projection 的 endpoint 非决定性反控制

```lean
theorem function_only_does_not_determine_endpoint :
    ¬ Determines functionOnly (fun candidate => EndpointAllowed candidate 1)
```

### 形式 witness

```text
shortCandidate.time = {0}
longCandidate.time  = {0,1}
functionOnly shortCandidate = functionOnly longCandidate = sharedFunction
1 ∉ shortCandidate.time
1 ∈ longCandidate.time
```

### 严格结论

任何只由 `FunctionView` 决定 endpoint membership 的假定 decoder 都会在这对
候选上给出矛盾。因此，若一个表示**真的省去了 designated time carrier**，则在本
最小模型里无法统一恢复该 endpoint observation。

### 禁止外推

- 不证明实际 `N`、N-MSS 或任何 domainless-function theory 接受这两个精确实例；
- 不证明 N-MSS 的物理解释有错误，或 time 在物理上不存在；
- 不把这个有限 witness 推广为所有 temporal observation 或所有 physical tasks；
- 不构成 ZFC、HoTT 或数学共同体的矛盾；
- 不把 endpoint membership 偷换为用户的全部 `OriginDone`。

## 来源身份

本包的来源动机和范围来自：

1. Sant'Anna--Bueno, *Sets and Functions in Theoretical Physics* (2014),
   snapshot `sources/external/zfc-meta-subtheory-c0r8-santanna-bueno-2014-20261005/`；
2. `audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R8-SANTANNA-BUENO-ZFC-TIME-ELIMINATION-CANDIDATE.md`。

来源事实由原件页面读取、source card 和本 README 记录；Lean 只证明明确给出的
representation-level consequence。
