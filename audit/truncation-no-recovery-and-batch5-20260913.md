# N16：集合值截断不可恢复族（机器包）与第五批证据队列抽样（2026-09-13）

> Session：`S-RES-20260913-062-N16-TRUNC-NORECOVERY-AND-BATCH5`。本报告新增一个机器证明包（C-134–C-138），并完成第五批证据队列抽样（40 条）。结论限定在固定工具链与固定抽样规则内；判词阶梯仍为第二级 `REPRESENTATION_BOUNDARY`。

## 1. 本轮为什么选这条构造

N1/N5/N10/T4 的审计都把升级口收敛到 E6（真实自然使用链）。在等待 E6 的同时，用户最自然的悖论路线是“理论保留了存在、遗忘了身份”——即 ASK 的资格错位。C-67–C-70 已在 Bool 上机器化这一边界。本轮把它族群化：

**任意集合值读出**都受 squash 路径约束，从而“从 mere existence 逐点恢复原 witness”的合同不可满足。这条构造直接对应 KC-000010/000013 的“不可计算/不可停机”特征与 KC-000029 的“理论经济拿掉多余现实因素”。

## 2. 机器包 `MP-TRUNC-NORECOVERY-001`（C-134–C-138）

- 源码：[TruncationNoRecovery.agda](/Volumes/D/HoTT_AI_HANDOFF_20260911/HoTT/formal/truncation-no-recovery/TruncationNoRecovery.agda)；说明：[README.md](/Volumes/D/HoTT_AI_HANDOFF_20260911/HoTT/formal/truncation-no-recovery/README.md)
- 工具链：Agda 2.8.0-3d04bac + Cubical v0.9（tree `73ccfbaf…`），`--safe --cubical --guardedness`，`--ignore-interfaces`，exit 0，stderr 0 字节，零 warning。
- final run：[20260913-MP-TRUNC-NORECOVERY-001-01](/Volumes/D/HoTT_AI_HANDOFF_20260911/HoTT/verification/runs/20260913-MP-TRUNC-NORECOVERY-001-01/RUN.json)，`KERNEL_ACCEPTED_WITH_SCOPE`、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`、`EXACT_INDEX_SNAPSHOT_MATCH`。
- 索引：`HoTT/CLAIM_EVIDENCE_MATRIX.md` 新增 proof 行与 C-134–C-138 五行；`index-row-manifest.json` 冻结 6 行（1 proof + 5 claim）。

五条 claim 的判词：

| claim | 内容 | 判词 |
|---|---|---|
| C-134 | 集合值读出与实现一致 ⇒ 任意两点值相等（`pointConstructorsForceEquality`） | `MACHINE_PROVED_LOCAL_UNCOMMITTED` |
| C-135 | 加分离见证后，读出与一致性证明不可能共存（`noPointRecovery`） | 同上 |
| C-136 | Bool 实例：逐点保持的 `∥ Bool ∥₁ → Bool` 不存在（`boolRecoveryImpossible`） | 同上 |
| C-137 | ℕ 实例：分离对 0/1，障碍非二元目标假象（`ℕRecoveryImpossible`） | 同上 |
| C-138 | 正控制：mere proposition 目标下 `rec Pprop f` 可用（`propositionValuedTestExists`） | 同上 |

适用域围栏：C-134 的 motive 是路径类型，而“集合中路径类型是命题”由库定理 `isOfHLevelPath'` 提供；非集合（高阶）目标不外推。反向限定同 C-70：不声称所有 `∥ A ∥₁ → A` 不存在。

## 3. 第五批证据队列抽样（40 条）

固定规则（无结果依赖）：前 1–4 批抽样比升序（并列按路径）逐 owner 填充 40 条预算、每 owner 上限 5、owner 内等距且剔除前批。覆盖 `README`、`B2`、`全量精读工作方案`、`B4`、`A6`、`B1`、`B0`、`A11` 各 5 条；判词写入 [样本 JSON](/Volumes/D/HoTT_AI_HANDOFF_20260911/audit/understanding-claim-sample-batch5-20260912.json)。

| 批 | 条数 | SUPPORTED | SUPERSEDED | UNSUPPORTED | PENDING | E6 |
|---|---:|---:|---:|---:|---:|---|
| 1–4 累计 | 162 | 93 | 12 | 0 | 57 | 否 |
| **第 5 批** | **40** | **29** | **0** | **0** | **11** | **否** |
| **累计** | **202/2,396（8.4%）** | **122** | **12** | **0** | **68** | **五批一致未出现** |

本批 SUPPORTED 多为路由/覆盖元数据与可核计数（Gemini 24/17/17/2/21/36、网页 111 节、workspace R018/R019、1,928 组对照、G:ALL:8470721）；PENDING 全部是解释性综合、核证性范围断言、残句与覆盖性断言，符合前批“待裁决主体是表述类型”的结论。

本轮未触发 F-011 打包（无 E6），但按 F-011 为新数学 claim 完成了打包（见 §2）——两者是不同动作，不互相替代。

## 4. 边界

- 不证明 HoTT 内部矛盾；不证明现实/物理时间结论；不把 `DEFENSE_WORKS` 升级成 `NATURAL_USAGE_MISMATCH`。
- 冻结 2,396 分母不变；抽样判词只覆盖样本；`SUPPORTED` 只表示登记角色内可核。
- 未 commit/tag/push；全部证明仍为 `MACHINE_PROVED_LOCAL_UNCOMMITTED`。

## 5. 下一步

1. 证据队列第 6 批（下一档 owner：`A5`/`升级方案-v2`/`A10` 等，按同规则去重）。
2. E6 仍是唯一升格口；若出现即转 F-011 打包。
3. ERCF-3 T3（Gödel 句）保持 gated。
