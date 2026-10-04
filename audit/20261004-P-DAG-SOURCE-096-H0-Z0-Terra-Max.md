# H096：H0→Z0 的理论变体与基础验收来源映射

> **身份：** SOURCE_MATCH_RUNTIME_EVIDENCE / HZ0_0_1 / SOURCE_SPLIT_NO_COMMON_CONTRACT。
>
> **NodeCard：** H096 H0→Z0 理论变体与基础验收。

## 1. 节点问题

H096 不问“ZFC 有什么问题”，而问一份冻结来源包是否已经有同一个合同，同时给出：

    exact H0 theory variant
    H0Map
    actual acceptance consumer
    Done_meta
    adequacy lift
    Q observation

若其中任何项只来自另一份来源，结论必须保持 source split。

## 2. 运行收据

| 字段 | 结果 |
|---|---|
| actor | gpt-5.6-terra / max |
| profile | source-match，唯一模型输入为冻结来源卡和 TaskCard |
| thread / turn | 01a106cb-237e-7010-a189-bec1e1939132 / 01a106cb-2450-7b80-85aa-f4d0ad1c662f |
| prompt gate | PASS |
| exact start | model、effort、cwd、approval policy、permission profile 均通过 |
| side effects | command=0、file_change=0、approval_request=0 |
| terminal | 正常 completed，96.65 seconds，E0-E7 齐全，753 words，hash c8c8ed9b55df02c0fd2fd50a79d353cfc22fd14e5c9eec038e5ca7564c411c8b |

私有 wire、认证和 prompt input 留在项目外实验根。trajectory reader 记录 1303 events、零 tools/results；direct wire 不含完整 isolated AGENTS 正文，L1 仍是 NOT_FULLY_CERTIFIED。这个限制不被终态质量掩盖。

## 3. MatchTrace 的裁决

| 来源 | worker 分类 | Master 裁决 |
|---|---|---|
| KLV | 相对一致性来源，但 exact Cubical Agda/H0 identity 与 H0Map 缺失。 | VARIANT_GAP / MODEL_DONE_ONLY。 |
| CCHM | cubical semantics、univalence 和部分 HIT；无 exact QuestioningDelay map 或 ZFC acceptance claim。 | PARTIAL_VARIANT_CONTROL。 |
| Cubical Agda | 最接近 H0 的实现／计算家族；无 set-theoretic model/adequacy consumer。 | IMPLEMENTATION_CONTROL_ONLY。 |
| HoTT Book | foundation framing；无 H0Map、Done_meta 或 completion bridge。 | ADEQUACY_SOURCE_CANDIDATE_ONLY。 |

公开终态给出的边界 verdict 是：

    SOURCE_SPLIT_NO_COMMON_CONTRACT

这意味着当前冻结来源还没有一个足以将 H0 交给 ZFC-side foundation acceptance 审查的共同对象。它不意味着 ZFC 已被证明看不见 H0，也不意味着 main H0 与 ZFC 无关。

## 4. 下一来源动作

H096 之后发现的 MPIM 2024 talk 提出一个新的、尚待主来源核验的 H0Map 候选：它称 Cubical Agda proofs 可经 cubical-set model 转为 set-theory proofs。H097 必须追溯该 model 的一手技术来源并逐项检查：

1. exact Cubical Agda variation 与版本；
2. fixed H0 的 universe、Delay、HIT 和 h-level dependencies；
3. proof translation 是否足以构成 H0Map；
4. acceptance consumer 是否仅是 proof translation，还是含 foundation adequacy lift；
5. H0 的 never / finite halt observation 是否被保留、排除或未给出。

在这些字段冻结前，H096 不产生 ZFC Q，也不重新调用 C-359。
