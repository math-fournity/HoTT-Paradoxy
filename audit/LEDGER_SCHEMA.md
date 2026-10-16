# 历史账本字段与证据等级

账本使用 JSONL，一行一个稳定对象；生成器负责机械序列化，语义裁决不由脚本自动完成。

| 文件 | 一行粒度 | 关键身份字段 | 主要证据 |
|---|---|---|---|
| `user-message-disposition.jsonl` | 一个提取用户消息 | `source_message_id` | 三份 primary 提取 + Codex supplemental |
| `ai-response-ledger.jsonl` | 一个可见 AI response | `response_id` | LocalGPT canonical inspect、WebGPT export、Gemini JSON |
| `tool-event-ledger.jsonl` | 一个 canonical tool call/result | `tool_event_id`、`call_id` | canonical reader locator；公共行对结果做 bounded head |
| `webgpt-section-ledger.jsonl` | 一个 Prompt/Response UI section | `section_id` | WebGPT 原始 Markdown section 行号 |
| `gemini-thought-ledger.jsonl` | 一个导出 thought record | `thought_id` | Gemini raw chunk locator；不是公开回答/证明 |
| `gemini-execution-ledger.jsonl` | 一个 code/result/inlineFile chunk | `execution_id` | Gemini raw JSON；inlineFile 先 base64→UTF-8 |
| `work-product-ledger.jsonl` | 一个快照树/文件/当前生成文件 | `artifact_id` | file SHA/tree SHA、repo/head、状态 |
| `claim-evidence-ledger.jsonl` | 理解章节中的一条非标题句/行 | `claim_id` | 文档 path+line；直接来源语义映射待人工审计 |

## 状态语义

`DOCUMENTED` 只表示文件/文字存在；`HISTORICAL_ONLY` 表示来源快照；`IMPLEMENTED` 表示代码/文档已写；`EXECUTED` 表示有运行收据；`VERIFIED_WITH_SCOPE` 表示验证器在明确范围通过；`RUNTIME_OBSERVED` 表示当前运行现场观察；`UNVERIFIED`、`MISSING`、`DIRTY_NOT_VERSION_CLOSED` 必须保留，不得被“已落盘”覆盖。

AI 自述是 `AI_VISIBLE_UNVERIFIED`，除非具体文件、Git、运行结果或 canonical event 另有支持。历史账本的结构验证 PASS 不等于历史数学主张 PASS；所有 ledger 的当前分母和失败项见 `ledger-summary.json` 与 `verification-report.json`。
