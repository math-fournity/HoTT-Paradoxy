# P-DAG-ZFC-SOURCE-023：relative-powerset source-match 的预启动失败

> **身份：** `PRE_AUTH_PROMPT_PROFILE_FAILURE / NO_AGENT_OUTPUT / NOT_A_THEORY_RESULT`。

H023 的 NodeCard 和 source excerpt 已冻结，但 runner 在读取 prompt 后、认证借用和 App Server 启动前退出：

```text
--prompt-file does not contain the frozen source-match profile
```

原因是 source-match profile要求 literal marker `BEGIN FROZEN SOURCE CARD`，而 H023 prompt 写成了`BEGIN FROZEN PRIMARY SOURCE CARD`。`read_frozen_turn`可以抽出文本，但 profile gate正确拒绝了不符合合同的输入。没有 model sampling、thread、turn、wire、认证借用、tool、file change或理论输出。

处置：H023保持原字节作为失败收据；H024使用唯一的 marker 修复后重新冻结。这个事件属于`RUNNER_OR_EVIDENCE_FAILURE`，不评价 relative-powerset source，也不产生 P1/P2/P3 verdict。

