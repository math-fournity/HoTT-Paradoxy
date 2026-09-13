# N19：库内"数据 vs 存在"接口对照与第八批抽样（2026-09-13）

> Session：`S-RES-20260913-065-N19-INTERFACE-DATA-CUT-AND-BATCH8`。本轮完成第八批证据队列抽样（40 条），并记录固定库内一处直接的"数据 vs 存在"接口对照证据。

## 1. 库内对照（无新数学 claim；固定库读取）

Cubical v0.9 在同一主题上并置两个接口（`Cubical/Data/FinSet/Base.agda`，树 `73ccfbaf…`）：

```text
isFinOrd A = Σ[ n ∈ ℕ ] A ≃ Fin n      -- 携带具体枚举（数据）
isFinSet A = Σ[ n ∈ ℕ ] ∥ A ≃ Fin n ∥₁ -- 只保留存在（命题）
```

且库中给出 `isFinOrd→isFinSet`（数据到存在的单向映射）与 `isPropIsFinSet`（存在侧是命题）。这正是用户命题"理论经济保留存在、遗忘是哪一个"在**真实库设计选择**中的直接体现：需要枚举时用 `isFinOrd`，只需有限性时用 `isFinSet`；从 `isFinSet` 不可能恢复 `isFinOrd` 的枚举（C-141 已机器化该边界）。库自身保持资格分离，未发现把 `isFinSet` 当 `isFinOrd` 使用的消费者——E6 保持 OPEN。

本条为库读取证据，不新增 claim（不与 C-141 重复计分）。

## 2. 第八批证据队列抽样（40 条）

固定规则（同第 3–7 批）：按前 1–7 批抽样比升序、每 owner≤5、owner 内等距、与前批去重。覆盖 `B3`、`读遍账本`、`B1`、`全量精读工作方案`、`B5`、`A1`、`A8`、`C0` 各 5 条。逐条判词见 [样本 JSON](/Volumes/D/HoTT_AI_HANDOFF_20260911/audit/understanding-claim-sample-batch8-20260912.json)。

| 批 | 条数 | SUPPORTED | SUPERSEDED | UNSUPPORTED | PENDING |
|---|---:|---:|---:|---:|---:|
| 1–7 累计 | 282 | 176 | 12 | 0 | 94 |
| **第 8 批** | **40** | **24** | **0** | **0** | **16** |
| **累计** | **322/2,396（13.4%）** | **200** | **12** | **0** | **110** |

本批可回源事实核验：`test_r036` 28/28、`186+34=220`、三个 git 仓库 commit 数、`.codex/research/hott/` 290 文件、`dotc` 计数 1928/1888/40/241、网页 55 节。另有两条口径差被显式记录：`16,151 vs 16,209`（work products 快照 vs ledger-summary）与 `40 vs 41`（A8 个位数条目）；均按"待复核口径差"处理，未按支持或否证计。E6 八批一致未出现。

## 3. 边界

- 不证明 HoTT 内部矛盾；不新增数学 claim；未 commit/tag/push。
- 冻结 2,396 分母不变；抽样判词只覆盖样本。

## 4. 下一步

1. 证据队列第 9 批（剩余低覆盖 owner 与口径差复核）。
2. E6 仍是唯一升格口；出现即转 F-011。
3. ERCF-3 T3 保持 gated。
