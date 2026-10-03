# H060：派生刀具来源门审查的输入合同失败

> **身份：** `INPUT_CONTRACT_FAILURE / NO_AGENT_OUTPUT / RUNNER_OR_EVIDENCE_FAILURE / NOT_A_MODEL_OR_THEORY_VERDICT`。

## 冻结材料

- H060 NodeCard 与 prompt 已在本分支提交 `e15364a95d7cbea63396fcd2889262e96f9343aa`；
- prompt SHA-256：`47a4a9bc4b9ca38f7188e0557e74f951f949321f95a280a783bae855435e903d`；
- runner：`scripts/pattern_p_appserver_blind_discovery.py`，固定运行器版本为 H060 NodeCard 所列 `a39e9afa`；
- 启动 profile：`source-match`。

## 可观察终态

运行器在任何 App Server thread/start 或模型采样之前退出，stderr 为：

```text
--prompt-file does not contain the frozen source-match profile
```

直接代码证据是 `scripts/pattern_p_appserver_blind_discovery.py:388--392`：`source-match`
同时要求精确文本 `You are a P-VALIDATION source mapper.` 和 `BEGIN FROZEN SOURCE CARD`。
H060 有前者而缺后者。

因此本节点的唯一合法状态是：

```text
INPUT_CONTRACT_FAILURE / NO_AGENT_OUTPUT
model / theory / Tool-Birth verdict: NONE
private wire / tool calls / file changes / approvals: NOT CREATED
```

## 纠正边界

H061 重新冻结同一审查问题与同一 sealed evidence，只增加 `BEGIN FROZEN SOURCE CARD`
和对应的结束边界。它不改写 H060，不增加来源，不改变模型、effort、权限、私有根的项目外
要求或预期结论。这个最小修正将检验的是 contract-source-gate 问题，而不是运行器拒绝行为。
