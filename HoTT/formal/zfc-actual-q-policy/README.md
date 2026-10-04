# ZFC 实际 Q：Q／P／A／B／ZFC-1 的可审计形式化包

本目录执行 [`ZFC-Q-ACTUAL-INSTANCE-FORMALIZATION-SOP`](../../../dev-docs/ZFC实际同Q实例化与机器证明SOP.md) 的 A6 机器化部分。它把研究发起人 2026-10-04 提出的链条

```text
Q 缺失 → 强 P 被接受 → Zeno 侧取得 A
同一实际 Q → P 运输到 HoTT → B 使其冲突
```

写成明确前提下的 Lean consequence，并用原生 Cubical Agda 固定 HoTT 侧的完成反射反例。

## 文件地图

| 文件 | 唯一职责 |
|---|---|
| [ActualQPolicy.lean](ActualQPolicy.lean) | 当前 Lean 4 core 逻辑核、受控 Zeno／endpoint 正反控制与无公理检查。 |
| [LEAN_TOOLCHAIN.json](LEAN_TOOLCHAIN.json) | 当前 Lean 4.34.1 二进制版本与 SHA-256 pin；只记录 Lean core 的可信运行边界。 |
| [ZFC1IllusionPolicy.lean](ZFC1IllusionPolicy.lean) | 保留的第一稿，已被拒绝；不可作任何 theorem 依据。 |
| [HoTTCounterexample.agda](HoTTCounterexample.agda) | 固定 Cubical Agda HoTT Q 对强 completion-reflection P 的原生反例。 |
| [WrongHoTTCounterexample.agda](WrongHoTTCounterexample.agda) | 必须在 `nothing != just 1` 处失败的 Agda 负控制。 |
| [ZenoLimitControl.lean](ZenoLimitControl.lean) | 固定几何数列的形式极限与严格有限阶段完成之间的 Mathlib 控制，以及闭连续时间 endpoint 正控制。 |
| [capture_zeno_limit_control.py](capture_zeno_limit_control.py) | 用 pin 的 Lean 4.34.0／Mathlib 环境捕获 C-361 的 source、环境和经典公理报告。 |
| [CLAIM.md](CLAIM.md) | 命题全文、人话、范围和禁止外推。 |
| [CROSS-KERNEL-MAPPING.md](CROSS-KERNEL-MAPPING.md) | Lean／Cubical Agda 命题对应与未支付转换。 |
| [SOURCE-BOUNDARY.md](SOURCE-BOUNDARY.md) | Standard Solution、ZFC 基础叙述和用户圆环任务之间的来源边界。 |
| [REVISIONS.md](REVISIONS.md) | 第一稿与初始 Agda 导入失配的可审计谱系。 |
| [CORE-INGESTION.md](CORE-INGESTION.md) | 用户原论述的 generation-14 core curation 输入、已验证的生成预演和 canonical integration 步骤。 |

## 当前可交付的层次

1. **逻辑核：** 若真实来源给出 `ZFCOneUse`、`PolicyScopeWitness` 和 B，则 Lean 内核已经证明结果为 `False`；严格 `SameActualQ` 是一条更强的充分控制。
2. **HoTT 控制：** 在固定 Cubical Agda `QuestioningDelay` 实例中，粗 completion 不反射为原 Q 的有限 completion。
3. **实分析控制：** 对 (1-2^{-n})，形式极限不推出有限自然数阶段 endpoint；闭连续时间端点仍可到达。
4. **来源边界：** 当前来源仍不足以把强 P、`A ↔ P`、可审的 `PolicyScopeWitness` 或严格 `SameActualQ` 填成实际事实；因此本包没有、也不应声称已经证明关于 bare ZFC 的矛盾。

当前交付运行为：

- [`MP-ZFC-ACTUAL-Q-POLICY-002` 的 Lean receipt](../../verification/runs/20261004-MP-ZFC-ACTUAL-Q-POLICY-002-06/RUN.json)：`KERNEL_ACCEPTED_WITH_SCOPE`，精确重放一致；
- [`MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001` 的 Cubical Agda receipt](../../verification/runs/20261004-MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001-01/RUN.json)：`KERNEL_ACCEPTED_WITH_SCOPE`，精确重放一致；
- [`MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001` 的 Lean/Mathlib receipt](../../verification/runs/20261004-MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001-04/RUN.json)：`KERNEL_ACCEPTED_WITH_SCOPE`，`LEAN_PATH` 已进入精确重放命令；
- [`C-360` 的 Agda 负控制](../../verification/runs/20261004-MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-NEG-001-01/RUN.json)：`KERNEL_REJECTED`，在预期的 `nothing != just 1` 处失败。

这些 selected run 已经在 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 与 `HoTT/verification/PROOF_VERSION_CLOSURE.json` 登记。运行前的草稿、失败 run 和外部文本都不能替代这一闭环。
