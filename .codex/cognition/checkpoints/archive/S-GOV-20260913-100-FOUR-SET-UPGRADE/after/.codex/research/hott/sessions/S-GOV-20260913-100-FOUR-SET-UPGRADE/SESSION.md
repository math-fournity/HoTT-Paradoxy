# S-GOV-20260913-100-FOUR-SET-UPGRADE

- 用户审阅长文后说“甚至我们要从三件套升级到四件套”，并在 A/B/C 中选择 **A**（授权见 `rulings.md` §19）。
- 第 1 步：长文加 `essay-role:v1` 角色声明（AI 阐释层）、原位修正“不改变加载配置”旧自述、分 5 片 + 首屏 banner。
- 第 2 步：加载链升四件套——runtime 3.6.0（`FULL_SET` 四元组 / schema v4 / `always_full_documents` / `document_order` / `essay_change`）、
  LOAD_SET 4.0.0（含 `full_set_roles`）、PROTOCOL v2.6、本地治理 Skill 3.6.0、根/`.codex` AGENTS、分片合同 §7、`feature-list` F-014。
- 校验器：`verify_fresh_three_way.py`（四件套身份/顺序/分片展开）、`verify_three_way_cognition.py`（四件套固定顺序 + 长文角色 marker）、
  `build_core_cognition_audit.py`（7 字段）同步；测试 fixture 与负向用例同步（runtime 38/38、三方 6/6）。
- 明确边界：长文是 AI 阐释层，不产出数学结论、不反向改写 core；每次启动必读体量 +约 75 KB。不 push。
