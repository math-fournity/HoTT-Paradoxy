# P23-INDEPENDENT-INGRESS-DISCOVERY-001：选择 ERCF-3 proof-predicate representability 门槛

**状态：** `SUCCESSOR_SELECTED / ERCF3_PROOF_PREDICATE_REPRESENTABILITY_AND_NATURAL_CONSUMER_CANDIDATE / P24_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM`

## 判词改变凭据

P21 已把 P3 同类消费者、P1 最小接口和 guarded→bare 桥分别停放。一个独立 ingress 必须改变理论构造与完成义务，而不是再查同类库。ERCF-3 的当前缺口满足此条件：对象语法、编码、替换、可解码性和局部 proof predicate interface 已有机器化资产，但对象层 representability、反射/对角不动点及实际 natural consumer 门仍未建立。

## 本地资产侦察

- `ObjectSyntax.agda` 已定义 `Prov : Fml → Set` 和局部 derivability interface；
- `ProvRepresentability.agda`、`DiagonalCore.agda`、`RepairedSyntax.agda` 等脉冲资产明确将完整 representability 保留在 door B；
- 当前程序化完整性规划把 full HoTT calculus、representability 与 natural consumer 标为未闭合，不把一般 Gödel/编码成果误报为 HoTT 自反真理验证问题已完成。

这些资产已是本地版本固定的、直接相关的独立工作面；本 P23 不重跑它们，也不把历史成功 modules 重新包装为新定理。

## 学术来源决定

P23 的工作是对当前本地 exact proof-predicate 门槛做 source/consumer qualification，不依赖新论文的名称或版本变化。公开检索在此前机器统观中已经覆盖 groupoid syntax、Coq undecidability、2LTT、internal universes 与 reflection literature；本步不新增外部理论比较，因此记录 `NOT_RERUN_WITH_REASON`。P24 若锁定一个特定外部 calculus/consumer，必须重新做一手来源核验。

## P24 候选卡

| 字段 | 冻结内容 |
|---|---|
| Candidate | `P24-ERCF3-PROOF-PREDICATE-REPRESENTABILITY-AND-CONSUMER-001` |
| Exact source | `HoTT/formal/ercf3-t3/ObjectSyntax.agda`、`ProvRepresentability.agda`、`DiagonalCore.agda`、`RepairedSyntax.agda` 与 C8/C4 current synthesis |
| Input | 对象语言 Fml、Prov interface、可解码编码、替换和明确 source calculus |
| Operation | representability/quotation/diagonal/reflection 的对象层构造；不是元语言直接调用 |
| Observation/Done | 当前 theory 内的 proof predicate、反射或真理验证消费者是否把对象层编码当成全局自身真理验证 |
| 正控制 | 局部 syntax/encoding/prov interface 可表达；必须承认已完成前置而非声称全部失败 |
| 负控制 | 缺对象层 representability 或实际 consumer 时，不能由一般对角引理推出 HoTT 自我验证循环 |
| 停止 | P24 先作依赖、对象层/元层与 natural-consumer qualification；若门 B 仍无具体 target，则保持 `GATED`，不继续脉冲式重写编码 |

## 波次定位

P23 选择的是用户核心的自反真理验证方向，而不是新一轮消费者关键词扫描。它的价值是把“HoTT 会不会在验证自身真理时循环”落实到可检查的 representability/consumer 门；它不预设最终答案为肯定或否定。
