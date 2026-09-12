# 本次顶层综合 repo 的治理维护 Gate 影响记录

> 日期：2026-09-12
>
> 适用范围：`/Volumes/D/HoTT_AI_HANDOFF_20260911` 新建顶层业务/研究 repo。
>
> 共享治理主库 `/Users/aurolafly/codex`、Codex host runtime、OpenCode 主库和外部服务均为本次只读参考，不在本轮写入。

## C01–C10 固定影响组

| 组 | 本次裁定 | 影响说明 |
|---|---|---|
| C01 | `UPDATE` | 用户明确新增顶层综合 repo、核心认知原文整合、每次全文加载和结束逐 ID 评估要求；本轮继续明确三件套、跨双 GPT 方向/成果投影和 core 更新归属，已写入本 repo 的 `rulings.md`、`feature-list.md` 和方案/审计 owner。 |
| C02 | `UPDATE` | 新 repo 需要单一当前工作根、三 AI 来源岛、理解章节解释层、核心认知 owner 和 evidence ledger 职责；共享 system/detailed design 不变。 |
| C03 | `UPDATE` | 在新 repo 建项目级 `.codex` governance/business Skill 和 local protocol；本轮将三件套全文加载、投影依赖边界和交叉审视接入本地 Skill；不改共享 canonical workflow。 |
| C04 | `UPDATE` | 新建并更新顶层 `AGENTS.md`、`.codex/AGENTS.md` 和确定性三件套启动路由；全局 AGENTS 不变。 |
| C05 | `UPDATE` | 新建 root README/docs/MEMORY/Feature/rulings、LOAD_SET、source manifest 和 cross-session 路由；本轮新增 `方向追踪.md`、`全景视野.md`、比较审计和唯一职责入口。 |
| C06 | `UPDATE` | 新建 core extraction、source/hash/locator、逐 ID audit、stale/missing/truncation/recovery 验证；本轮新增三件套顺序/孤儿链接正负测试；fresh Session 理解验收在后续单独执行。 |
| C07 | `NO_CHANGE` | 不改 `~/.codex` 配置、Rules、Hooks、Plugins、凭据或 host 权限；本 repo 内的 `.codex` 文件不改变 host runtime 本身。 |
| C08 | `NO_CHANGE` | 不改 OpenCode、BrowserOS、Devin、ZCode 等产品专属主库或 host adapter。 |
| C09 | `UPDATE` | 顶层新 Git 历史、精确提交、版本/回滚和 clean-clone 收据属于本 repo；本轮治理 checkpoint 已由 STATE revision 4→9 逐次封存，后续需精确 commit；不打共享 `governance-v*` tag，不 push。 |
| C10 | `UPDATE` | 保存 LocalGPT/WebGPT/Gemini/理解章节的历史身份、removed `aistudio-docs` 边界、dirty/untracked provenance、旧版本冲突和残余未知；本轮额外保留 projection 容量修复和孤儿引用失败证据。 |

影响组 remainder：`0`。

## 证据边界

- 本记录证明本轮项目级治理影响已经分类，不证明新 Skill 已被宿主自动发现或模型已理解。
- `aistudio-docs` 已由用户移走，旧依赖它的 validator 失败将保留为 `BLOCKED_SOURCE_REMOVED`，不能被新 core validator 覆盖。
- 新 repo 的 current state 只有在相应快照、代码、测试、运行和 Git 证据完成后才提高状态。
