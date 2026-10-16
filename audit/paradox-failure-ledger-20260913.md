# 悖论失败台账：S031–S070 的候选及其机器判定（2026-09-13）

> Session：`S-RES-20260913-071-N25-FAILURE-LEDGER`。本文件把本工作线迄今**尝试过的全部悖论候选**逐项登记，给出它们被什么机器结果处置、当前判词与复活条件。它不新增 claim，只把已有证据整理成一张可以直接回答"悖论找到了吗"的台账。

## 1. 判词阶梯（沿用 C3/C5）

`DEFENSE_WORKS` → `REPRESENTATION_BOUNDARY` → `NATURAL_USAGE_MISMATCH` → `INTERNAL_INCONSISTENCY`。当前整体停在第二级；升级唯一口是 E6（真实、固定版本、可回查的自然使用链）。八批抽样（322/2,396）与五层审计塔均未发现 E6。

## 2. 候选台账（按方向分组）

### A 方向：现实可完成而理论中完成困难

| 候选 | 机器结果 | 判词 | 复活/继续条件 |
|---|---|---|---|
| 截断偷换（mere existence→原 witness） | `MP-ERCF-TRUNC-001`（C-67–C-70）：命题 recursor 可用、二重截断压平、Bool 输出恒定、逐点恢复不可能 | `DEFENSE_WORKS` | 出现真实消费者承诺恢复 witness（E6） |
| 截断不可恢复族群化（任意集合值读出） | `MP-TRUNC-NORECOVERY-001`（C-134–C-141，含 Bool/ℕ 实例、命题值正控制、`isFinSet` 形状） | `DEFENSE_WORKS`（族群） | 同上 |
| 完成候选类型为空（理论内部否定形式） | 同包（C-139/C-140，run `-02`） | `DEFENSE_WORKS`（内部否定形式） | 同上 |
| 部分性商 × race/timeout | `MP-RACE-TIMEOUT-001`（C-71–C-76）：bind 下降、race/deadline 不可下降 | `REPRESENTATION_BOUNDARY` | 出现把结果商用于 race 的自然接口 |
| 上下文等价与时序 | `MP-CONTEXTUAL-EQUIV-001`/`MP-CONTEXT-CHARACTERIZATION-001`（C-77–C-91）：`≡c` 严格细于 `≈`；Bool 片段 `≡c` = 代表相等 | `REPRESENTATION_BOUNDARY` / 完整刻画 | 更宽上下文语言 |
| 商值 continuation | `MP-QUOTIENT-MONAD-001`（C-84–C-88）：商可分裂、单子成立 | `MONAD_STRUCTURE_CONSTRUCTED` | 无 section 的一般商 |
| 阶段/guard 擦除 | `MP-GUARD-ERASURE-001`（C-92–C-95）：保律擦除 ⇔ 不动点存在 | `GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE` | guarded/clocked 完整翻译 |
| 同函数异时（成本） | `MP-COST-FACTORIZATION-001`（C-96–C-99）：裸函数不可区分、细化可恢复 | `NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL` | 真实编译器/资源语义 |
| 路径证书（R034） | `MP-PATH-CERTIFICATE-001`（C-100–C-105）：MereMove 非栖居 + 路径正例 | `MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS` | R032 证书语法回放 |
| 在线因果 | `MP-ONLINE-CAUSALITY-001`（C-106–C-109）：时刻 0 无前视、完整知识 ≠ 在线资格 | `ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS` | 物理时间/guarded 完整翻译 |
| 过渡抽象/极限 | `MP-TRANSITION-LIFT-001`（C-110–C-117） | `TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS` | 新机制或新接口 |
| partial/total 判定 | `MP-PARTIAL-DECISION-001`（C-118–C-123） | `PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL` | 完整 partiality monad |
| SIP/表示 | `MP-SIP-REPRESENTATION-001`（C-124–C-128） | `SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL` | 真实库误用 |
| Cauchy modulus | `MP-CAUCHY-MODULUS-001`（C-129–C-133） | `CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS` | 完整 Real 库/十进制展开 |

### B 方向：现实不可完成而理论假装完成

| 候选 | 机器结果 | 判词 | 复活/继续条件 |
|---|---|---|---|
| LEM 分类 → 有效实现（W51×RP-B01） | N2 提取接口审计：MAlonzo `error "postulate evaluated"`、Lean 拒 `Prop→Bool` 大消去与非计算消费者 | scoped `DEFENSE_WORKS`；`B01-TARGET` 仍 OPEN | B01-TARGET 的其它接口或真实消费者出现 |
| 自证/已验证交付声明 | T4 五源审计：全部自带三层限定（禁用特性/传输不计算/信任基/相对规范/QIIT 元语言） | `BOUNDED_DEFENSE_WITH_TRUST_BASE` | 出现不带限定的自证消费者 |
| 编译后端交付 | N10：`--cubical` 全拒、`--erased-cubical` 仅擦除、普通模块导入 `InfectiveImport`；Lean 双层分离 | scoped `DEFENSE_WORKS` | 其它后端/版本 |
| ERCF-3（反射与哥德尔内部化） | C8 前置评估 + T1 对角核 + T2 语法 + S067–S070 四个 T3 脉冲（编码、替换、表示骨架、反射具名化） | `ERCF3_GATED`（脉冲为证据，非 claim） | P8 natural consumer；或完成码级算术恒等式与不动点构造后重评 |

### 元层候选

| 候选 | 处理 | 判词 |
|---|---|---|
| A 方向候选生成（13 条） | N11 归约为表示/资格边界、通用边界、元层/工具链观察三类 | `A_DIRECTION_BOUNDED_NEGATIVE` |
| 库接口形状（`isFinOrd`/`isFinSet`、`isFinSet` 统一枚举读出） | C-141 机器化边界；库自身保持资格分离 | `LIBRARY_DESIGN_EVIDENCE` |
| 总性测试消费者 | S066 库扫描：无 `terminating/halts` 型消费者 | 有界负结论 |
| 历史 claim 抑制 | 八批抽样 322/2,396：`UNSUPPORTED=0`、E6 未出现 | `BOUNDED_SAMPLE`（继续） |

## 3. 结论（当前证据基础）

1. **没有找到满足完整升格链的 HoTT 悖论**：既有候选在固定工具链上全部以防御或表示边界收口，判词阶梯停在第二级。
2. **所有"困难"都落在接口相对的位置**：换一个携带更多数据的接口（细化表示、显式参数、伴随选择数据），同样的失败就消失。因此目前的负结论是**接口相对**的，而不是"HoTT 不可能"的。
3. **唯一能改变上述结论的动作是 E6**：一条真实、固定版本、可回查、把弱资格当强资格使用的消费链。八批抽样与五层审计均未发现它。
4. 用户命题中"现实相对非现实性"的形式（理论中不可完成而现实中完成）在本工作线里对应的是**资格割**而非矛盾；要把它推成悖论，必须出现 E6，或出现"任何细化都无法弥合"的实例（目前也没有）。

## 4. 下一步（按期望收益排序）

1. 继续寻找 E6（每个新候选接口先问：谁在真实系统里消费它、消费时是否隐藏了资格假设）。
2. 完成 T3 的两条子义务（码级算术恒等式、对象层不动点），把 ERCF-3 从"gated"推到"可重评"。
3. 证据队列第 10 批及其后（低优先级，主要功能是防止历史主张漏检）。
