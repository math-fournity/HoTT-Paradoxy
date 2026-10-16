# 收官补强两件执行记录（ReboundDisarm + NecessityLEM + A1/A4 处置）（2026-09-19）

## 用户指令（逐字）

> 开始，全部做了

## 执行结果

1. **① ReboundDisarm.agda 一次过核**（--safe 零公理）：`ideal-point-is-explicit = base`
   （理想点=显式构造子）、`endpoint-identification-is-a-path = loop`（端点同一化=
   路径构造子）、`hit-computation-witness : intLoop (pos 0) ≡ refl`（经 HIT 的闭
   计算取得典范形——canonicity 不被 HIT 收费）。收据
   `20260919-MP-DEDEKIND-OMEGA-REBOUND-DISARM-01`：`PASS_WITH_SCOPE` +
   `EXACT_INDEX_SNAPSHOT_MATCH` + `--rerun` 逐位一致。
2. **② MissileFourNecessityLEM.agda 过核**（四轮迭代修三处：⊎-elim→elim 名、
   isoToEquiv 在 Isomorphism、¬p 直接应用于 lift x）：`hProp≃Bool`（LEM 逐点
   决策组装，coherence 由 isProp 吸收，hProp 内相等=ΣPathP(ua, toPathP·isPropIsProp)）
   → `SingleOmega-from-LEM`（Ω:=Lift Bool）→ **`LEM→Necessity : LEMProp ℓ →
   Necessity ℓ`——前提 ℝLayerAt 未被使用**。收据
   `20260919-MP-DEDEKIND-OMEGA-NECESSITY-LEM-01`：同上全绿。
   **数学内容：必要性问题的全部内容被机器化定位到构造性片段**（LEM 下后件
   无条件成立；Book 取法 3「LEM ⇒ Ω≡Bool」原文首次收据化）。
3. **A4 处置（文献扫描）**：检索确认 Huber 的 canonicity 证明（与 Sattler，
   gluing 模型路线）为论文级，**无可直接重放的现成机械化件**（cubical Agda
   本身是 CCHM 的实现，但其 canonicity 元定理未被单独机械化入库）。维持
   `SOURCE_REPORTED_NOT_REPLAYED`，重放=论文级原创形式化工程（登记不启动）。
4. **A1 处置（方向分析登记）**：`PropResizing→SingleOmega`——pointwise 反射
   无法直接组装小 Ω（hProp ℓ 是 set 非 prop，PropResizing 只反射 prop，集合的
   整体小型化不在其力量内）；`SingleOmega→PropResizing`——hProp ℓ 只覆盖 ℓ 层
   prop，而 PropResizing ℓ 的靶是 Type (ℓ-suc ℓ) 层 prop（如 Ω 自身），
   方向不匹配。两方向均无快定理，**维持开放**（B1b′ 相关，NecessityLEM 的存在
   使该问题在经典侧已无内容，纯构造性问题）。

## 提交链

`08cb865`（两模块+双收据+矩阵节）→ `a2b86d8`（index closure ×2）→ 本 dev-note。

## AI 最终回复（摘要）

见对外终报。

#### turn 产出（元信息，非回复正文）

本文件（dev-notes/0049）。
