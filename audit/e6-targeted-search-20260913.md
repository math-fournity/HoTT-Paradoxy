# N36：E6 定向搜索（固定库扫描）（2026-09-13）

> Session：`S-RES-20260913-082-N36-E6-TARGETED-SEARCH`。按失败台账的最高期望收益项执行：在固定工具链（Cubical v0.9 全库，tree `73ccfbaf…`）内**定向**搜索 E6 的三种具体形态。无新数学 claim。

## 搜索的形态（按失败台账 §4.1 的提问方式）

| # | 形态 | 查询 | 结果 |
|---|---|---|---|
| 1 | 命题截断→数据 | `∥_∥₁ → (Bool｜ℕ｜ℤ｜List)` | **无匹配**（截断只出现在命题值消费者位置） |
| 2 | `isFinSet`→具体数据 | `isFinSet … → (Bool｜ℕ｜List)` | **无匹配**（枚举数据只经 `isFinOrd` 流通） |
| 3 | postulate 参与计算 | 全库 `postulate` 出现 | **仅 3 处，全部是注释**：`Experiments/HoTT-UF.agda`（说明"若有 funExt 公设"）、`Papers/Pi4S3-JournalVersion.agda` 与 `Papers/FunctorialQcQsSchemes.agda`（均声明 `--safe` 保证无公设/无未完成目标） |

## 结论（限定范围）

- 在固定 Cubical v0.9 全库内，**没有发现**把弱资格（mere existence / 命题截断 / 有限性命题）当强资格（具体数据）消费的自然使用链；库的 `--safe` 纪律与接口设计（`isFinOrd` vs `isFinSet` 并置）都在执行资格分离。
- 这是**有界负结论**：它覆盖该库该版本，不证明全局不存在 E6；其它库/派生开发/应用层仍需按同一提问方式逐个检查（N1/N2/N5/N10/T4 已覆盖五层，本项补上"固定库内定向形态扫描"）。
- 由此，判词阶梯继续停在第二级 `REPRESENTATION_BOUNDARY`；E6 仍 OPEN，仍是唯一升格口。

## 下一步

1. E6 的剩余搜索面：其它固定库（如 agda-unimath 的派生开发，已有部分接口审计）、以及**应用层**把理论结果当交付承诺的代码。
2. T3 共享判定联合递归（ERCF-3 的收口路径）。
3. 证据队列第 11 批。
