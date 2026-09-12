# 跨来源方向—成果逐项 reconciliation 报告

截至：`2026-09-12`；Schema：`cross-source-reconciliation/v1`。

> 本报告由机器登记器生成。它证明每个纳入范围的来源行都有稳定 locator、候选方向/成果链接和显式语义状态；它不把规则匹配、文件存在、历史 AI 自述或 ledger PASS 当作数学证明或模型理解证明。

## 1. 覆盖分母

| 来源 | 行数 | 处理方式 |
|---|---:|---|
| WebGPT STATE revision 41 | 91 | 全部 record 逐项登记；保留历史状态和 source path |
| AI response ledger（LocalGPT 305 + WebGPT 55 + Gemini 24） | 384 | 逐行 locator + 内容/owner 路由 |
| LocalGPT tool event | 3146 | 逐行 event locator；不把工具调用当结果 |
| work product | 16209 | 逐项 artifact/file/tree locator |
| understanding claim | 2396 | 逐句/逐行 claim locator；全部保留直接语义复核状态 |
| **合计** | **22226** | **无静默丢弃** |

## 2. 映射与语义边界

- `entries_with_direction=22226`；`entries_with_result=22226`；`unmapped_reason=0`。
- 方向 ID 越界：`0`；结果 ID 越界：`0`。
- `understanding_claim` 的 `2396` 行仍需直接句级语义裁决；这不是遗漏，而是显式未知。
- `EXPLICIT_OR_OWNER_ROUTE` 只表示 record ID、owner 路径或结果名称有直接路由依据；`PROVENANCE_FALLBACK` 只表示安全地归入历史/治理覆盖方向，不代表主题已经判断完成。

## 3. 当前来源边界

- LocalGPT live 工作树仍 dirty；register 不写入或清理 `/Volumes/D/ALL-Markdown`。
- WebGPT 使用顶层保存的 workspace snapshot 和其 revision 41 STATE；原 workspace 不被修改。
- 所有条目 `mathematical_certification=NOT_PERFORMED_BY_THIS_REGISTER`；已有 R039/R036 等结果的实际证据等级仍以 `全景视野.md` 与原 result owner 为准。
- 方向/结果链接是当前投影的交叉入口；详细 raw payload、tool result、artifact、Git diff 和句子必须沿 locator 回源。

## 4. 运行收据

- 生成器：`scripts/audit/build_cross_source_reconciliation.py`
- 验证器：`scripts/audit/verify_cross_source_reconciliation.py`
- 预期验证：所有输入文件 hash、WebGPT 91 条 record、四类 LocalGPT/理解账本行数、ID 域和无理由孤儿均通过。
