# Session checkpoint输入格式

这是模板，不是已执行研究。`checkpoint`默认dry-run，显式apply才写。当前权限不够时不要运行。

```json
{
  "schema_version": "cognition-checkpoint/v1",
  "session_id": "S-EXAMPLE-001",
  "authorization": "当前用户准许保存本轮记录的原话/范围",
  "files": [
    {"path": "MEMORY.md", "expected_sha256": "当前文件sha256", "text": "完整新正文"},
    {"path": ".codex/research/hott/FRONTIER.md", "expected_sha256": "当前文件sha256", "text": "完整新正文"},
    {"path": ".codex/research/hott/LESSONS.md", "expected_sha256": "当前文件sha256", "text": "完整新正文"},
    {"path": ".codex/research/hott/RESUME.md", "expected_sha256": "当前文件sha256", "text": "完整新正文"},
    {"path": ".codex/research/hott/STATE.json", "expected_sha256": "当前文件sha256", "text": "完整新STATE JSON字符串"},
    {"path": ".codex/research/hott/sessions/S-EXAMPLE-001/SESSION.md", "expected_sha256": null, "text": "本轮实际公开记录"}
  ]
}
```

STATE revision必须递增1，latest_session必须指向本轮不可覆盖的SESSION。新的活动记录和依赖必须存在于项目或本次写集合，不能只写标题。改变依赖后先标review_required，或者给出真正revalidation说明与更新的source_hashes。工具不认证语义。

Session正文含：任务/权限、读取版本、实际行动/构造、证据和失败、范围、结论变化、受影响依赖、下一动作与未执行项；不保存隐藏思维链。
