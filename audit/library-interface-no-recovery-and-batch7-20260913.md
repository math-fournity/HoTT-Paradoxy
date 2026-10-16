# N18：库接口形状的不可恢复实例（C-141）与第七批抽样（2026-09-13）

> Session：`S-RES-20260913-064-N18-LIBRARY-INTERFACE-AND-BATCH7`。本轮把截断不可恢复族落到**固定库的真实接口形状**上（C-141），并完成第七批证据队列抽样（40 条）。

## 1. 新 claim：`isFinSet` 形状的接口边界（C-141）

Cubical v0.9 的接口形状（`Cubical/Data/FinSet/Base.agda`，tree `73ccfbaf…`）：

```text
isFinSet A = Σ[ n ∈ ℕ ] ∥ A ≃ Fin n ∥₁
```

枚举组件是**命题**（`isPropIsFinSet` 在库中给出），因此不同枚举在类型层被识别。C-141（`isFinSetLikeNoUniformEnumeration`）证明：对任意集合 `E`、分离对与逐点保持的 `pick : ∥ E ∥₁ → E`，都导出 `⊥`；即**不存在从该接口形状统一读出具体枚举的函数**。这正是 C-139 的一般形状在真实库接口上的实例，也是"理论经济保留存在、遗忘是哪一个"在有限集接口上的最小机器化。

运行：`HoTT/verification/runs/20260913-MP-TRUNC-NORECOVERY-001-03/`（Agda 2.8.0 + Cubical v0.9、exit 0、stderr 0 字节、零 warning、`EXACT_INDEX_SNAPSHOT_MATCH`、独立重放 exact match）；matrix 覆盖 C-134–C-141，冻结 9 行 manifest。

**为什么不是 E6**：C-141 说的是"这个接口形状不允许统一读出"。要成为 E6，还需要找到**真实、固定版本、可回查的消费者**把该接口的弱资格当作强资格使用（例如承诺返回具体枚举而未携带表示数据）。本轮的扫描在固定库内未发现这种消费者（库自身在该接口上保持资格分离）；因此判词仍是 `DEFENSE_WORKS` 家族，E6 保持 OPEN。

## 2. 第七批证据队列抽样（40 条）

固定规则（同第 3–6 批）：按前 1–6 批抽样比升序、每 owner≤5、owner 内等距、与前批去重。覆盖 `B3`、`A3`、`A9`、`A0`、`B1`、`A2`、`B2`、`A8` 各 5 条。逐条判词见 [样本 JSON](/Volumes/D/HoTT_AI_HANDOFF_20260911/audit/understanding-claim-sample-batch7-20260912.json)。

| 批 | 条数 | SUPPORTED | SUPERSEDED | UNSUPPORTED | PENDING |
|---|---:|---:|---:|---:|---:|
| 1–6 累计 | 242 | 149 | 12 | 0 | 81 |
| **第 7 批** | **40** | **27** | **0** | **0** | **13** |
| **累计** | **282/2,396（11.8%）** | **176** | **12** | **0** | **94** |

E6 七批一致未出现。PENDING 仍集中在解释性综合、残句、计划条目与需逐件回源的细节。

## 3. 边界

- 不证明 HoTT 内部矛盾；C-141 是接口形状边界，不是"某库误用"的实例。
- 冻结 2,396 分母不变；未 commit/tag/push；证明仍为 `MACHINE_PROVED_LOCAL_UNCOMMITTED`。

## 4. 下一步

1. 证据队列第 8 批（下一档 owner：B5、A7、A1 等）。
2. E6 仍是唯一升格口；出现即转 F-011。
3. ERCF-3 T3 保持 gated。
