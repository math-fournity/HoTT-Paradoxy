# Astra 审计结论回源说明

本目录支撑《Astra对击落HoTT工作的第一次审计》各片的原文/源码索引。目的：另一位 AI 不需要相信 Astra 的总结，即可从结论 ID 回到作者原话、具体类型、证明体、命令和原始输出。

## 读取顺序

1. 从报告正文标题后的 `audit-cites` 字段，或每片末尾“逐项来源索引”，找到 `C001-01` 一类稳定结论 ID。
2. 打开该行提供的直接来源。源码链接指向实际起始行，标签写出完整检查范围或符号；JSON 行提供 field/label，按该字段定位，不把整个 JSON 文件名当充分证据。
3. 用 [SOURCE-LOCATORS.md](SOURCE-LOCATORS.md) / [SOURCE-SNAPSHOT.json](SOURCE-SNAPSHOT.json) 核对路径、实际 SHA-256、字节、行数和 Git blob。`LOCAL_DERIVED_OR_UNTRACKED` 不冒充已版本化。
4. 对运行事实，继续打开 [RUN-LOCATORS.md](RUN-LOCATORS.md) 中的 source、历史 RUN、独立 replay receipt、stdout/stderr；对话按 [VISIBLE-MESSAGE-LOCATORS.json](VISIBLE-MESSAGE-LOCATORS.json) 的 raw locator 和可读提取版行号核对。
5. 区分该行的事实、来源转述、审计推断和建议，再自行检查推理是否成立。

## 证据身份

| 身份 | 读者应怎样使用 |
|---|---|
| FACT / RUN_OBSERVED | 可以按文件、命令、类型、退出状态直接复核；仍只覆盖该输入与环境 |
| SOURCE_REPORTED | 原典或原 AI 确实这样表述；不表示该陈述已被本次核证明 |
| USER_INTERPRETATION | Astra 对用户原意的理解；原文定位已给，允许用户修正 |
| INFERENCE | Astra 根据所列来源作出的审计推断；链接并不替它证明正确，需检查连接步骤 |
| SCOPED_NEGATIVE / OPEN | 只在声明的语料与已读范围内未找到所需连接；不推断全域不存在或不可形式化 |
| PROPOSAL | 根据定位缺口提出的工作/交付建议，非已采纳需求或已经完成的结果 |
| SELF_REPORTED | 本审计对自身读取/操作范围的说明；哈希、文件数和脚本不能认证模型理解或全部隐藏行为 |

## 版本和隐私

原证明审计基线为 `8a334e0636620209953a26aba354ffb38bbf7bbf`；Terra 对照及本次索引核对基线为 `19d45ce503fdacb2b6dc6d87f01bf794298b66c6`。输入是否真的相同以本次 SHA/Git blob 对账为准，不以日期或文件名相似为准。

原始 ZCode JSONL 和 canonical inspect 选段是私有现场来源，不复制 system prompt、reasoning 或整份轨迹到报告。本报告给出的可读行号指向用户已提供的“用户与AI完整对话”提取版；16 条决定性消息与 canonical 的可见正文逐项对账。缺少私有现场时仍可读该提取版，但不得声称自己已经复核 raw source。

## 机械检查

`verify_source_index.py` 是本目录唯一派生收据生成器。`--freeze` 从人工编辑的报告生成来源快照、扫描记录与当前检查收据；默认运行只核对已冻结来源和声明的索引。它不修改报告、证明、历史 run、registry 或项目 STATE。

```sh
python3 audit/astra-hott-first-20260919/citation-index-20260919/verify_source_index.py
```

`CITATION-CHECK.json` 的 PASS 只证明所声明索引的 ID、路径、行号、hash 和可见正文对应通过。它不证明每个推断正确，不证明数学真理、不认证整个学界覆盖，也不能代替另一位 AI 的独立阅读。负结论另看 `SCOPED-SEARCHES.json` 的命令、文件分母和原始 stdout/stderr。

资产类别：本 README、EXTERNAL-SOURCES 和报告证据表为 HUMAN_EDITED；其余 JSON、SOURCE/CLAIM/RUN-LOCATORS 与扫描输出是 MACHINE_MANAGED_DERIVED 审计实物，不是另一套 canonical 主张矩阵或 current-state 数据库。
