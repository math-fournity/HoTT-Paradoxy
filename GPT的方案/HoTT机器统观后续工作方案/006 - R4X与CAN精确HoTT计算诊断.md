<!-- governance-shard:v2
logical_id: GPT-HOTT-MACHINE-OVERVIEW-PLAN
shard_id: 006
index: ../HoTT机器统观后续工作方案.md
-->

# R4X与CAN精确HoTT计算诊断

## 1. R4X 与 current TaskSpec

current `R4-HOTT-NAT-EFFECTIVITY-001` 已冻结、实现未开始。它列 cubicaltt/redtt/cooltt/cctt，并承认 holes、undefined、metavariables 和 unchecked recursion 需要受限 accepted corpus。

本方案保留 current TaskSpec 的全部资格化职责，改变目标选择与解释顺序。正式采纳前先完成 FR source identity。

## 2. 十个资格化门

第八轮修正后的完整集合是：

| Gate | 义务 |
|---|---|
| `Q-SOURCE` | URL、commit、date、license、tree hash |
| `Q-BUILD` | 固定工具链 build 与 smoke tests |
| `Q-RAW-SYNTAX` | term/type/context/rule AST 的 source anchors |
| `Q-NAT` | Nat formation/introduction/elimination/computation |
| `Q-PATH` | Path/identity、composition/transport、universe/univalence/HIT 层级 |
| `Q-CONVERSION` | checker 入口、conversion、错误与终止依据 |
| `Q-INCOMPLETE-INPUT` | holes/undefined/unsolved metavariables 的域外规则 |
| `Q-RECURSION` | general recursion、mutual/corecursion 与 termination/guardedness |
| `Q-DETERMINISM` | 同一正反 corpus 双遍结果与 hash |
| `Q-CORRESPONDENCE` | implementation AST/acceptance 与声明 calculus 的保真边界 |

任何一门 PASS 不自动替代其它门。尤其 `Q-BUILD` 不证明 calculus fidelity，`Q-RAW-SYNTAX` 不证明 checker acceptance。

## 3. target 选择顺序

1. 已发表 formal calculus、内部语法或机器化元理论；
2. 社区实现作为 parse/conversion/evaluation/differential target；
3. 自建 closed-input profile 只定义受限 accepted corpus；
4. 只有经证明 translation/embedding/sufficiency/correspondence，才把实现结论提升到演算结论。

不因 feature 多、build 快或源码新自动胜出。

## 4. arithmetic-only 消融先行

先问：保留有效语法、Nat、proof relation 与算术解释，删除 Path/univalence/HIT 后，一般不完备机制是否仍成立？

若保持：

```text
GENERIC_GODEL_BOUNDARY_WITH_HOTT_INSTANCE
/ HOTT_ESSENTIALITY_NOT_ESTABLISHED
```

按用户“程序问题被 HoTT 继承”的框架交付，但不完成根 Goal，不构造第三套同型 Gödel 编码。

若消融改变 proof relation、表示性、固定点或有效性，才形成 `HOTT_ESSENTIAL_R4_CANDIDATE_WITH_EXACT_OPEN_OBLIGATIONS` 并深化。

## 5. R4 义务阶梯

1. exact syntax/context/substitution；
2. Nat 与算术表达；
3. identity/Path/universe/conversion；
4. closed proof acceptance 与 proof-code enumerability；
5. arithmetic interpretation／Robinson-Q strength；
6. strong separation／representability；
7. substitution、s-m-n 或相称自应用；
8. fixed point／diagonal sentence；
9. independent sentence 与前提；
10. Path/univalence/HIT 消融和 inner/outer 边界。

每级使用 `PRESENT / ABSENT_BY_DEFINITION / OPEN / BLOCKED_BY_PRESERVATION / REFUTED`。前级未闭合时，后级不由文件存在提升。

## 6. ERCF-3 进入条件

C-157–C-187 只关闭编码／解码／替换／引用的自足部分。ERCF-3 本体仅在 exact target 提供以下条件时重开：

- 对象语言编码和表示关系；
- 可枚举 proof relation；
- inner/outer theory；
- source-grounded self-validation consumer。

proof checking、proof search、theoremhood、global soundness、consistency 和 self-guarantee 必须分层。手写递归或 timeout 不是 Gödel 实例。

## 7. R4X 终局

```text
GENERIC_GODEL_BOUNDARY_WITH_HOTT_INSTANCE
HOTT_ESSENTIAL_R4_CANDIDATE_WITH_EXACT_OPEN_OBLIGATIONS
R4_TARGET_CORRESPONDENCE_INADEQUATE
```

build success 不是第四种完成出口。

## 8. CAN-001 的两个问题

1. 相关性：opaque constant 恰为 univalence，现象与 axiomatic HoTT 相关；
2. 特有性：stuck 是否来自 univalence laws，或任意 opaque indexed equality schema。

原 `transport (λ _ → Bool)` 常值 family 已被撤回。新规格至少从 `X ↦ X` 开始，并固定 calculus、universe、equality、K/UIP、reducer 和 canonicity 命题。

## 9. 五组对照

| 对照 | 目的 |
|---|---|
| 纯 MLTT | constructor/canonicity 基线 |
| 单一 opaque equality constant | 孤立不透明性 |
| equivalence 同型索引 generic opaque schema | 索引宽度/FAMILY_SPREAD |
| axiomatic univalence | ua 命题与判断计算边界 |
| Cubical univalence | 计算规则正控制 |

## 10. 观察层分开

```text
syntactic stuck set
judgmental equivalence class
propositional behavior
canonicity theorem
library consumer closure
compiler/backend support
```

一次 reducer 观察只支持该项和环境，不证明一般 normalization 失败。propositional computation 能完成数学任务时必须作为正控制。

## 11. CAN 提升与停止

只有 axiomatic univalence 相对 generic indexed schema 仍有由 univalence law 解释的差异，且 source-grounded consumer 要求对应 judgmental computation，才进入现实相对候选。

否则：

```text
GENERIC_OPAQUE_AXIOM_COMPUTATION_BOUNDARY
UNIVALENCE_RELATED_CANONICITY_BOUNDARY
IMPLEMENTATION_OR_BACKEND_OBSERVATION
```

