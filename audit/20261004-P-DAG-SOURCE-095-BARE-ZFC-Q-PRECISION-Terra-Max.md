# H095：bare ZFC Q 理论精度的冻结来源映射

> **身份：** SOURCE_MATCH_RUNTIME_EVIDENCE / P0_P1_P3_CLASSIFICATION / NOT_A_BARE_ZFC_THEOREM。
>
> **NodeCard：** [P-DAG-SOURCE-095](20261004-P-DAG-SOURCE-095-BARE-ZFC-Q-PRECISION-NODECARD.md)。
>
> **公开输入：** [frozen payload](20261004-P-DAG-SOURCE-095-BARE-ZFC-Q-PRECISION-PROMPT.md)。

## 1. 节点目标

本节点只问一件事：SEP 的 ZFC 语言／表示事实、IEP 的 ZFC-supported Standard Solution claim，以及 Norton 的 completion revision，究竟冻结了 bare ZFC 本身的 Q interface，还是只冻结了一个 application-level completion policy。

模型没有网络、文件、Git、工具或项目 history。它不能创造新的 ZFC 解释，也不能访问已有的 P-DAG 结论。

## 2. 可复核的运行收据

| 字段 | 值 |
|---|---|
| actor | gpt-5.6-terra / max |
| runner | scripts/pattern_p_appserver_blind_discovery.py --profile source-match |
| health canary | H095-HEALTH-001 PASS；exact marker、0 tools、0 file changes、0 approvals |
| source run | H095-SOURCE-001 PASS |
| App Server thread / turn | 01a10685-c464-7592-afe9-83ecb807b30a / 01a10685-c51b-7173-ace0-3b0ec7c460e6 |
| source input gate | PASS；frozen card/profile present，project root、old project answers、P-DAG skill identifier absent |
| exact launch echo | model, effort, cwd, approval policy and permission profile all verified |
| behavior | command=0、file_change=0、approval_request=0、自然 completed |
| elapsed | 289.14 seconds；60-second observation cadence；没有自动 wall-clock interrupt |
| terminal | E0–E7 全部存在；776 words；hash d0665ad1486dcb5c8a9c6a387207f7c4b214eab1dba8196233cdbc3adea9743d |

私有 experiment root 在业务项目外；wire、认证、prompt input 与 liveness 为 0700/0600 私有实物。此公开文件只保留非敏感的身份、结果 hash、访问限制与结论范围。

## 3. 公开 MatchTrace 的实质内容

worker 按 E0–E7 形成如下可复核映射：

| 项 | worker 的公开判词 | Master 对冻结来源的复核 |
|---|---|---|
| E1/P0 | S1 给 bare ZFC 的 syntax／representation，未给 semantic completion predicate、OriginDone 或 Bridge。 | 与 SEP 的 language 与 foundation 段一致。 |
| E2/E4 | 应选 application interface 为 resolution locus；rich process interface 是 bridge 责任的边界；不选 bare syntax 作为 bridge obligation locus。 | 与 IEP 的 foundation-to-resolution claim 和 Norton 的 contract distinction 一致。 |
| E5/P1 | IEP 给出粗 application C/I/O/Done，C 只能是 application source owner。 | 接受；不改称 bare-ZFC consumer。 |
| E5/P3 | Norton 显式改写 completion；无 FormalDone -> OriginDone payment。 | 接受；与 C-362 的来源分类控制一致。 |
| E6 | 若来源真的给出受域限定的 paid bridge，rich interface 的欠缺会消失。 | 正确反事实。 |
| E7 | P0_LANGUAGE_FIXED + P1_APPLICATION_CONTRACT_FIXED + P3_EXPLICIT_TASK_SWITCH + SOURCE_APPLICATION_OWNER_ONLY + SOURCE_INTERFACE_UNDERDETERMINED。 | 接受为本来源分母的 scoped verdict。 |

该节点既不以“ZFC 无时间 primitive”推出不可编码性，也不以“source 没写 bridge”推出 bare ZFC 不一致。

## 4. TrajectoryReceipt

canonical session_trajectory.py 对私有 direct App Server wire 做了：

    catalog -> tree -> scan -> search -> coverage

| 层 | 可观察结论 |
|---|---|
| L1 context injection | NOT_FULLY_CERTIFIED：wire 有 user payload，但 raw wire 中没有完整 isolated AGENTS 正文。 |
| L2 selected read | NOT_OBSERVED_EXPECTED：worker contract 禁止工具，0 tools／0 reads。 |
| L3 recall | NOT_TESTED。 |
| L4 cognition | MASTER_REVIEWED_WITH_SCOPE：只审公开 E0–E7 与冻结来源，不从 reasoning summaries推断隐藏过程。 |
| L5 behavior | NODE_ACCEPTED_WITH_SCOPE：exact model/effort/start fields、source preflight、normal terminal 和零副作用通过；不等于其来源解释已被机器证明。 |

原始 reader 输出的 1302 events 与 private source locator 保留在 experiment root，不在 Git 中复制。任何将来要依赖 H095 做更多决定的工作，必须重新读取 frozen NodeCard、payload、public terminal 与相应一手 source；本报告本身不能替代它们。

## 5. QConvergenceLink 与后续动作

    Target-Q       = F-049 bare ZFC theoretical-precision hypothesis
    Candidate-Q    = a bare-ZFC-facing completion-observation interface
    Control-Q      = encodability / paid bridge / rich interface / explicit task switch
    effect         = Q_NARROW
    before/after   = source interface not frozen
                    -> bare semantic interface underdetermined,
                       application contract frozen
    Q-4/ZFC_Q_LOCATED = not reached

H095 允许后续执行 C-364 的 application-interface-relative Lean control。它明确禁止将该 control 写成 bare ZFC 的语义 interface proof。若将来存在实际 source owner 把 bare-ZFC formal acceptance 自身提升为原过程完成，才是新的 P3 ingress。
