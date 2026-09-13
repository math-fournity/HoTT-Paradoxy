# project-local governance v3.4.1：索引读取 banner 加固证据

> 会话：`S-GOV-20260913-097-INDEX-READER-BANNER`（revision 97）
> 授权：用户回复“开始加固”，对应上一轮给出的可选加固方案
> 范围：8 个 canonical 索引全部加首屏可见 banner + 机械检查；不改任何 KC、数学判词、proof source/run/index
> 回滚边界：本地 annotated `governance-v3.4.0`（加固前的索引文本状态）

## 1. 加固内容

**banner（每行一处，位于 v2 marker 块之后、正文/表之前）：**

```text
> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 N 个分片；缺一片即未完成，按表顺序读取；300 行只是软目标，不是上限。
```

覆盖 8 个 canonical 索引：`README.md`(4)、`MEMORY.md`(3)、`理解章节/C1`(4)、`C2`(6)、`C3`(5)、`C4`(6)、
`方向追踪.md`(5)、`全景视野.md`(8)。`MEMORY.md`/`方向追踪.md`/`全景视野.md` 为 MUTABLE，经本 checkpoint 写入；
其余 5 个直接提交。

**为什么放在 marker 块之后**：v2 marker 仍在第 1 行（规范要求“索引顶部包含”），banner 紧随其后，
仍在 validator 的 20 行发现窗口内，不改变任何既有解析规则。

## 2. 机械强制（不是约定）

| 位置 | 机制 |
|---|---|
| `scripts/audit/logical_document.py` | 新增 `READER_BANNER_PREFIX`、`READER_BANNER_WINDOW=15`、`READER_BANNER_REQUIRED`、`canonical_indexes()`（排除 `.git`/`templates`/checkpoint 副本）、`banner_issues()` |
| `scripts/audit/verify_governance_shards.py` | 包装器在 validator 之外叠加 banner 策略：缺失 → `MISSING_READER_BANNER`、残缺 → `INCOMPLETE_READER_BANNER`，**状态置 FAIL 并退出 1**；receipt 记录 `canonical_indexes_checked` 与 `reader_banner_issues` |
| `scripts/audit/test_shard_index_banners.py` | 5/5：banner 存在通过、缺失告警、残缺告警、窗口外告警、checkpoint 副本排除 |
| `docs/quality/长治理文档分片与索引合同.md` §3 | banner 的契约化（前缀、窗口、必需子串、失败语义） |
| `AGENTS.md` / `.codex/AGENTS.md` / `LOAD_SET.json`(3.4.1) / 本地治理 Skill(3.4.1) | 路由与版本写回 |

## 3. 连带影响链（本轮真实的 pin 传播）

- `理解章节/C1`–`C4` 的索引文件被 `audit/understanding-chapter-merge-manifest.json` 逐文件 pin → 索引文本一改，
  manifest 必须重建：本轮重建后计数不变（35/24/15/9/11/0），随后 **14 条**引用该 manifest 的 record 重新签 hash。
- `理解章节/C3`、`C4` 本身还被 10 条 record 直接 hash 固定 → 连同 manifest 与 `AGENTS.md` 一起，共 **4 类路径**
  在本 checkpoint 内重签并写入 `revalidation`。
- 结果：`plan --profile research --task <S094/S095/S096/S097>` 全部正常，无新增 stale。

## 4. 验证（revision 97 实测）

| 检查 | 结果 |
|---|---|
| banner 策略 + 结构校验 | `PASS`；`canonical_indexes_checked=8`、`reader_banner_issues=[]`；validator 发现 indexes=19（8 canonical + 11 个 checkpoint before/after 副本，副本不计入 banner 检查） |
| banner 单测 | 5/5 |
| runtime 单测 / 三方单测 | 38/38 / 6/6 |
| 三方校验 | `PASS`（28 方向 / 89 结果 / revision 97） |
| fresh 冷启动 | `PASS_WITH_SCOPE`，revision 97 |
| projection freshness | `PASS_WITH_SCOPE`（`source_state_revision: 97` 在索引首屏） |
| math gate / core / merge / cross-source / history | 全部 `PASS`/`PASS_WITH_SCOPE` |
| canonical checkpoint | `.codex/cognition/checkpoints/S-GOV-20260913-097-INDEX-READER-BANNER/result.json` = `CHECKPOINT_COMMITTED` |

## 5. 残余风险

- banner 降低“只打开索引就以为读完全文”的概率，但**不能强制模型消费**：一个既不读 `AGENTS.md`、也不调用
  runtime/validator 的 AI 仍可忽略它。可机械保证的边界仍是：**任何一次正规工具调用都会报错**（`COVERAGE_INCOMPLETE`
  / `UNLISTED_SHARD` / `UNCOMMITTED_STATE` / `MISSING_READER_BANNER`），以及索引自身首屏声明身份。
- fresh model behavior 仍 `NOT_RUN`：本轮同样只证明结构与字节层行为。
