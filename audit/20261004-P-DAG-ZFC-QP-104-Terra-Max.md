# P-DAG H104：UOU《Real Analysis》中的实际 completion-promotion 来源核证

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / M6_ACTUAL_P_SOURCE_MAP / ACTUAL_P_CANDIDATE_SOURCE_MAPPED / Q_NARROW / NOT_A_ZFC_VERDICT`。

## 1. 来源与字节身份

本卡审的是 Uttarakhand Open University 的课程文本 *Real Analysis*，课程号
MT(N)-201，§5.1，PDF 物理第 75 页。它不是 ZFC 的公理文本，因而不能替代
bare ZFC 的来源证明；它是一个实际数学教育／实分析来源，足以检验“数学共同体如何
把极限结果交付为 Achilles 完成”的来源级候选。

| 项目 | 已固定的事实 |
|---|---|
| URL | `https://uou.ac.in/sites/default/files/slm/MT%28N%29-201.pdf` |
| 下载时间 | 2026-10-04 |
| HTTP 身份 | `Content-Length=13,810,753`、`ETag="67e292e7-d2bc41"`、`Last-Modified=2025-03-25T11:26:31Z`；`Range: bytes=0-0` 返回 `206` 与相符总长度。 |
| 保存位置 | `/Volumes/D/HoTT-ZFC-sources/20261004-UOU-Real-Analysis/MT-N-201-real-analysis.pdf` |
| PDF SHA-256 | `e8c3e3bb4867b3547f3174f5623d75ea401362ca6f338d195e3723874f4b833b` |
| 文字提取 SHA-256 | `550d0167073f1ee31168f7129fd2014c084256f281b0d6dd8849c2eee0e8975c` |

该段落把 Achilles/tortoise 叙述为无穷多个、各自耗有限时间的子赛程；它说级数的
有限和给出 Achilles 追上乌龟所需的时间，并把这称作悖论的解决。全文提取中的
`Achilles`/`Zeno` 搜索只命中这个段落；这能说明固定文本中没有第二个同名叙述，
不能证明整部教材或所有数学文献不存在某种 bridge。

## 2. 冻结 TaskCard 与直接来源映射

| 字段 | H104 冻结内容 | UOU §5.1 的支持范围 |
|---|---|---|
| `F` | 无穷项级数有有限和／极限 | 明说无穷项级数有有限和。 |
| `D` | Achilles 追上乌龟；悖论得到解决 | 明说有限和给出追上所需时间，并称为悖论的解决。 |
| `promotionClaim` | `F` 被当作 `D` 的充分理由 | 明说有限和给出所需时间，处在“resolution”的句法位置。 |
| `verifiedBridge` | 同一任务的 F→D 保真桥 | 冻结段落没有给出独立的过程保持定理、Done 区分或操作性对应。 |
| 更强 Done | final-action、SEP every-step、圆环复原、物理完成 | 段落没有定义或等同这些合同。 |

这就是 P 的目前可证伪、来源级形状：

```text
P_card(F,D) = finite-sum / limit F
              is stated as sufficient for source-level catch-up / resolution D
              while the frozen source card does not supply a verified
              task-preserving F -> D bridge.
```

`not supply` 是有关该冻结来源卡的描述；它不是“任何可能的桥都不存在”的结论。

## 3. Terra/Max source-match 与轨迹收据

| 字段 | 结果 |
|---|---|
| actor | `gpt-5.6-terra / max` |
| profile | `source-match`；只见 H104 的冻结来源卡 |
| run | `H104-UOU-REAL-ANALYSIS-ZENO-COMPLETION-PROMOTION-20261004` |
| thread / turn | `01a10595-d025-7a02-9503-edc8257f738a` / `01a10595-d0e1-7a01-8c5e-db7a3473ba4e` |
| prompt preflight | runner 的唯一 fenced payload 提取 PASS；3,117 characters；SHA-256 `b2cb429173738bd2a77d6d42fb2713ea1a2ac3d89882d0dc9028cd718108fc53` |
| terminal | completed，23.371 seconds，E0--E7 齐备，535 words，public final SHA-256 `211732988a2212710c9c194c7e8b937ea7b2016e379bcb47e094f03e0a9f87cf` |
| side effects | command/file-change/approval = `0 / 0 / 0` |

canonical `session_trajectory.py` 对 private bidirectional App Server wire 依次完成
`catalog → tree → search → inspect → context → coverage`：一条 session、一条 turn、871
个事件；无 tool call/result。冻结 payload 的私有 context 抽取与
`read_frozen_turn` 的输入逐字匹配（3,117 chars、一个精确匹配）。

| 层 | 判词 | 范围 |
|---|---|---|
| L1 | `FROZEN_TURN_PAYLOAD_EXACT_MATCH` | 证明 sent user payload 与固定 payload 同字节；隔离 AGENTS 正文的完整注入仍未由 wire 认证。 |
| L2 | `NOT_OBSERVED_EXPECTED` | source-match 禁止工具；wire 和 runner 都是零 tools。 |
| L3 | `NOT_TESTED` | 本节点不是独立 recall 实验。 |
| L4 | `MASTER_REVIEWED_WITH_SCOPE` | 公开输出保持 TaskCard、没有伪造 P2 reentry，也没有越级到 ZFC。 |
| L5 | `NODE_ACCEPTED_WITH_SCOPE` | exact model/effort、permission、prompt input、terminal、schema 和零副作用均有收据。 |

worker 的 E6 为 `ACTUAL_P_CANDIDATE_SOURCE_MAPPED`。这个 verdict 与 Master 的原文复核一致，
但只接受到上面 `P_card(F,D)` 的边界。

## 4. P1/P2/P3-C 与 H083 反控制

| 刀 | H104 的结论 |
|---|---|
| P1 | 实际来源提供 `C/I/O/Done`，并把 F 提升到 source-level D；这是现有 M6 中第一张未见 Done 区分／bridge payment 的来源候选卡。 |
| P2 | `NOT_APPLICABLE`。无限项、极限或完成用语都不提供同一对象的 `Bind → Form → Bridge → Reenter`。 |
| P3-C | Representation=级数；Operation=用有限和解释总时间；Observation=以有限和判断追上时间；Done=追上／解决；LiftClaim=有限和给出所需时间；Payment=冻结卡未给 task-preserving bridge。 |

H083 的 SEP 卡是必须同时保留的相邻控制：SEP 明示区分 `every-step` 和
`final-action`，因此 H104 不能被夸大为“所有数学来源都忽略 Done”。相反，这两个
来源共同把 M6 的问题缩得更精确：**哪些实际来源把 F 交付为 D，而没有把它们之间的
任务保持关系写出来；哪些来源又显式地改写或限定 D？**

## 5. Master 判词、QConvergenceLink 与停止边界

```text
ACTUAL_P_CANDIDATE_SOURCE_MAPPED
scope = UOU §5.1 frozen source card only
Q effect = Q_NARROW
Q state = Q_OBSERVATION_GAP_NOT_SOURCE_MAPPED (unchanged)
ZFC_Q_LOCATED / bare-ZFC adoption / P-to-HoTT-B / object-level contradiction
             = no / no / no / no
```

本节点让“数学幻觉 P”第一次拥有一条不是 AI 归纳、不是 SEP 已付款控制、而是实际
实分析教材中的来源级候选。它仍不是终局：只有把该来源的 `D` 同用户任务/圆环或
HoTT B 建立同一任务 bridge，才可以推进 Q 或 ZFC 的判词。

**可推翻条件：** 若 UOU 的同一来源范围给出明确 Done 区分、任务保持 bridge，或将
catch-up 明确修订为弱 Done，则此卡改记 `BRIDGE_PAID_CONTROL` 或
`TASK_REVISED_CONTROL`。若一个来源把 UOU D 与用户的强 Done 明确等同并给出 bridge，
则才可进入 M3/M5 的下一条闭合链。

## 6. Delta SelfAuditCard

```text
original requirement  = 让锻刀与定位 ZFC Q 同一收敛过程，不把极限公式或 H0 类比直接当结论。
actual action         = 先发现并修正 H103 对 SEP 全卡的假阳性；再下载、核字节、抽取并冻结一份
                        不含相同 payment 的实分析教材来源；按 source-match 和 trajectory 合同运行 H104。
alignment             = ALIGNED.
H103 deviation        = SOURCE_CARD_COMPLETENESS_FAILURE; repair documented, not hidden.
H104 Q link           = Q_NARROW: 实际 P-card 出现，Q 本体尚未来源化。
tool-only-drift       = no: H104 改变了 M6 的可检验来源分母与下一 bridge 义务。
next trigger          = 同源 bridge/Done 审读，或一个能把 UOU D 与 HoTT/圆环任务连接的来源。
```
