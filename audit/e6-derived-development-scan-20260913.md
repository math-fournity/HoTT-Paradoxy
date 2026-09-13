# N37：E6 定向搜索（派生开发/应用层）（2026-09-13）

> Session：`S-RES-20260913-083-N37-E6-DERIVED-SCAN`。按 N36 的结论把 E6 搜索面扩展到**派生开发**：扫描本 repo 中全部 211 个 `.agda` 文件里、位于固定库之外的消费者。

## 1. 扫描范围与发现

- 本仓库（排除 `private-audit/`）共 **211** 个 `.agda` 文件；其中绝大多数是本 repo 自己的机器包（`HoTT/formal/*`）。
- 发现一个**此前未审计**的派生开发：`HoTT/formal/agda-unimath/hott-z/NoCanonicalPoint.agda`（用户侧 Z-串联工作）。它导入 agda-unimath 的 `univalent-combinatorics.2-element-types`，并：
  - 直接引用库定理 `no-section-type-2-Element-Type`，给出 `no-canonical-point : ¬ ((X : 2-Element-Type l) → type-2-Element-Type X)`；
  - 进一步包装为 `PointedOrientation`（只含一个被选中的端点），并证明 `no-canonical-pointed-orientation`；注释明确声明："它刻意不叫 temporal order：没有 irreflexivity/transitivity/totality 公理；任何时间读法都需要单独的桥。"

## 2. 这说明了什么（以及不是什么）

- **是**：真实库（agda-unimath）中存在**自然的不存在性定理**（unlabeled 2-element type 没有统一选点），且派生开发**正确地**使用它——没有把"没有统一选点"改写成"存在一个统一选点"，也没有把 `PointedOrientation` 冒充成时间序。这再次显示资格分离在真实开发里被**执行**，而不是被绕过。
- **不是 E6**：E6 的定义要求"把弱资格当强资格使用"的真实消费者。此文件恰好相反：它把"不存在统一选点"作为定理使用，并把额外读法（时间序）显式标记为需要单独桥接。因此它属于**负向证据**（与 N1/N2/N5/N10/T4/E6-scan 同向）。
- **状态限定**：本 repo 只保存了该派生文件，**不含 agda-unimath 库本体**，因此本轮**没有**重跑该文件的 kernel 检查；`no-section-type-2-Element-Type` 的存在性按库来源身份登记为 `SOURCE_REPORTED_NOT_REPLAYED`，不得当成当前 AI 的机器结果。

## 3. 结论

在"派生开发/应用层"这一搜索面上，本轮找到一个真实的库级不存在性定理被正确使用的实例；未找到 E6（弱资格→强资格的自然消费链）。E6 仍 OPEN；判词阶梯仍是第二级 `REPRESENTATION_BOUNDARY`。

## 4. 下一步

1. 若要继续这一搜索面：取得固定版本的 agda-unimath 检出并重跑 `NoCanonicalPoint.agda`，把它从 `SOURCE_REPORTED_NOT_REPLAYED` 提升为可复跑证据。
2. T3 共享判定联合递归（ERCF-3 的收口路径）。
3. 证据队列第 11 批。
