# 断点、等价与证明机制：对话原文及后续检查

本目录研究 HoTT 的表示、等价、运输、拼接和信息消去，是否会忽略某个对原命题或任务不可缺少的局部条件。先保存原始问答，再设计有范围、可反驳的检查。当前交付为**原文归档完成＋检查方案已制定**；没有新增数学证明，没有预先确认 HoTT 已出现缺陷。

1. **先读[对话原文](对话原文.md)**：从用户“下面的代码块，是我第一弹的原文……”的完整提问及代码块开始。五轮已完成问答全部保存，另附本轮落盘指令和起点澄清；包括截止边界内可见过程消息，共21条。
2. **再读[系统化后续检查方案](系统化后续检查方案.md)**：六个分片固定问题、语义路线、证明连接、等价与消去、程序化覆盖、执行与证据。不要用方案改写原文。
3. **核对[归档清单](evidence/对话归档清单.json)与[逐字核验](evidence/对话逐字核验.json)**：canonical reader抽取的UTF-8文本、独立消息文件和阅读分片的对应字节段逐一相等，21/21通过。

状态：`DIALOGUE_EXPORTED_EXACT_WITH_SCOPE / CHECK_PLAN_DESIGNED / MATHEMATICAL_CHECKS_NOT_STARTED / CANDIDATE_NOT_CURRENT`。未commit/push，不推进STATE或canonical checkpoint。

来源是本机Codex rollout，通过Session Trajectory Skill的canonical reader获取；未手写raw trajectory解析器。[原始消息/](原始消息/)保留批注、Markdown、公式、代码、原结论和归档失败说明。系统/开发者内容、工具结果、隐藏推理不属于问答原文，不导出。历史指令不作为当前指令。

标注答复ID：`msg_0fed0cc6c9484eef016aaeb5771f7887d0959f744ccf4f2b7b`；**起点用户消息ID**：`msg_01a0ba6e-fec1-7300-b8ca-a83cbd52b54a`。截止于本轮起点澄清。本轮尚未发送的最终答复不冒算第六个完整问答。

人写的README/方案为`HUMAN_EDITED`；对话正文、原始消息与清单为`DERIVED_SOURCE_SNAPSHOT`，不是新current-truth数据库。原文不手改；重新导出用新路径保留旧快照。[导出与核验脚本](tools/export_visible_dialogue.py)只调用canonical reader并渲染，不修改Host数据。

与旧设计的关系：[四弹一体完整研究策略](../四弹一体完整研究策略.md)保留此前总体候选设计。本轮先横向检查一般机制，不把点集圆环模型完成、特定来源差异或旧算术支线设为所有检查的前置；发现机制后再建立回原始问题的联系。
