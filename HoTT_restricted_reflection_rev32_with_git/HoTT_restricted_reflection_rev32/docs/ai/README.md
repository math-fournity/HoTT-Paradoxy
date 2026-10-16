# AI

职责：模型、Prompt、Agent 角色、工具、上下文隔离、trajectory、截断、eval 和泄漏。

本项目包含大量 AI 对话、AI 生成证明、角色扮演审稿和 AI 交接包。它们可作为 provenance、候选
论证和行为轨迹，但以下信号均不能直接升级为数学证据：模型自称专家、多个 AI 同意、长思考文本、
`COMPLETE_INTERNAL`、模拟审稿接收或文件名含 `✅/Final`。数学主张须回到定型表达式、证明/反例、
机器检查或一手文献；外部专家门必须由独立人员/环境留下可识别收据。

当前不运行面向用户的 AI 软件组件；若以后引入模型执行、Prompt 或 agent pipeline，再建立版本、
权限、隔离和 eval 合同。

## HoTT 未来 Session 上下文合同

HoTT/Z/时间/抽象/悖论任务的未来 AI 必须按根AGENTS与 `.codex/cognition/LOAD_SET.json`，每次先全文加载第五闭包和已对齐三问，再完整读指定用户原文、Z owner、时间owner、主张矩阵及最新MEMORY/前沿/经验/接续，并全文展开当前候选和实际依赖。用户原文拥有意图和研究方法来源权威，AI 总结不能替代；
历史对话和交接包仍只作 trajectory/provenance。Fresh Session 是否真正恢复该工作意识由
`HoTT/verification/FRESH_SESSION_COGNITION_CHECK.md` 的理解性问题验证，关键词出现或文件存在
本身不算通过。

### 用户数学哲学优先、证据批判的双阶段协议

本项目研究前人尚未给出的元数学／数学哲学问题。LLM 的训练数据汇总的是既有认知，它既可能
提供重要数学工具，也可能在问题尚未被理解以前用主流答案将问题提前关闭。因此相关 AI 必须遵守：

```text
Stage A: WITHIN_USER_MATH_PHILOSOPHY
  读取原文 → 恢复用户术语／前提 → 内部重建程序与推演 → 得到条件裁决

Stage B: STANDARD/EXTERNAL_COMPARISON
  引入既有数学 → 精确比较前提／模型／反例／证据 → 得到外部裁决

Final:
  双重裁决并列；冲突可见；不得静默覆盖。
```

`USER_MATH_PHILOSOPHY_FIRST` 决定解释顺序和研究问题所有权；`EVIDENCE_CRITICAL` 决定任何数学／
物理结论仍须证明。禁止两个相反失败：

1. `CONSENSUS_FIRST_FAILURE`：把训练 prior／教科书结论当默认裁判，未重建用户问题就宣布已解决、
   不成立或只是误解；
2. `USER_ASSERTION_IS_PROOF_FAILURE`：把用户哲学的研究优先权误当成免证、不可反驳或物理事实。

Russell 是本协议的验收例：AI 必须先给出用户的 `rₙ₊₁=¬rₙ` 拿入／拿出、构造不落定、formation
promotion 和 validator rejection，再分列朴素集合论、现代集合论／类型论及标准 computability 的
比较。只回答“ZFC 用公理模式解决了 Russell”或只说“这是无固定点”都不算理解了用户问题。

当任务要求恢复“过去是否讨论过某个 HoTT 问题”或作出“旧资产中没有/已经全部覆盖”的负结论时，
未来 AI 必须先查询 `HoTT/sources/aistudio-discussions/CURRENT` 对应 manifest/INDEX，并按结果回到
原始源行区间；不能只看 16 份迁移全文、AI 摘要或 `# N. 问` 标题。该语料明确包含问答、章节式
长文和无标题正文，所有条目仍是 `UNREVIEWED_RAW_CAPTURE`，不能被升级为当前数学认知。

## 跨Session持久化

本轮引入文件式认知加载和受控checkpoint，不是额外AI组件。具体协议见 `.codex/cognition/PROTOCOL.md`。脚本只能检查文件版本/覆盖/引用及写回原子边界，不能认证模型理解、代替数学裁决或自行授予执行权限。依赖失效需传播待复核；用户不必重复安排研究路线。
