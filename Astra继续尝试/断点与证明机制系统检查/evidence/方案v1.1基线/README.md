# 断点、等价与证明机制：对话原文及后续检查

本目录研究 HoTT 的表示、等价、运输、拼接和信息消去，是否会忽略某个对原命题或任务不可缺少的局部条件。先保存原始问答，再设计有范围、可反驳的检查。当前交付为**原文归档完成＋检查方案已制定**；没有新增数学证明，没有预先确认 HoTT 已出现缺陷。

1. **先读[对话原文](对话原文.md)**：从第一弹完整提问及代码块开始。初始21条原样保留；[增量002](evidence/对话归档增量-002.json)补入前轮其余过程消息/最终交付及最新“指定缺口与特殊构造方法”的完整提问，总计27条，六轮完整问答及当前提问。
2. **再读[系统化后续检查方案v1.1](系统化后续检查方案.md)**：七片、14检查模板。[第007片](<系统化后续检查方案/007 - 指定缺口、构造来源与相对变形.md>)完整讨论最新想法，新增结构保真与构造可达性检查。原六机制横向主线保留。
3. **核对[初始清单](evidence/对话归档清单.json)、[增量清单](evidence/对话归档增量-002.json)与[27条逐字核验](evidence/对话逐字核验-002.json)**：每条UTF-8原文、独立txt、阅读分片对应字节、canonical inspect一致。

状态：`DIALOGUE_EXPORTED_EXACT_WITH_SCOPE / CHECK_PLAN_DESIGNED / MATHEMATICAL_CHECKS_NOT_STARTED / CANDIDATE_NOT_CURRENT`。未commit/push，不推进STATE或canonical checkpoint。

来源是本机Codex rollout，通过Session Trajectory Skill的canonical reader获取；未手写raw trajectory解析器。[原始消息/](原始消息/)保留批注、Markdown、公式、代码、原结论和归档失败说明。系统/开发者内容、工具结果、隐藏推理不属于问答原文，不导出。历史指令不作为当前指令。

标注答复ID：`msg_0fed0cc6c9484eef016aaeb5771f7887d0959f744ccf4f2b7b`；**起点用户消息ID**：`msg_01a0ba6e-fec1-7300-b8ca-a83cbd52b54a`。当前截止新提问`msg_01a0babe-5430-78d3-a0e1-c92cd26fe814`；尚未发送的当前final不冒充历史答复。

人写的README/方案为`HUMAN_EDITED`；原文与清单为`DERIVED_SOURCE_SNAPSHOT`。原文不手改；[初始导出器](tools/export_visible_dialogue.py)与[增量导出器](tools/append_marked_puncture.py)只调用canonical reader并渲染，保留旧原文/清单，不改Host数据。v1.0候选设计已另存[修订前基线](evidence/方案修订前基线.json)，不是不可恢复覆盖。

与旧设计的关系：[四弹一体完整研究策略](../四弹一体完整研究策略.md)保留此前总体候选设计。本轮先横向检查一般机制，不把点集圆环模型完成、特定来源差异或旧算术支线设为所有检查的前置；发现机制后再建立回原始问题的联系。
