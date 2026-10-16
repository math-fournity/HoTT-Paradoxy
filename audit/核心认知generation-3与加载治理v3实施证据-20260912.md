# 核心认知 generation-3 与加载治理 v3 实施证据

版本：`HOTT-LOCAL-GOVERNANCE-3.0.0-IMPLEMENTATION-EVIDENCE`

日期：2026-09-12

状态：`IMPLEMENTED_AND_CHECKPOINTED_REVISION_18 / MECHANICAL_FULL_SUITE_PASS / FRESH_MODEL_BEHAVIOR_NOT_RUN / GIT_VERSION_CLOSED`

## 1. 本轮接受的纠偏

用户明确指出：

> 注意，你完全可以重建我当初定义的 核心认知.md 文档，而不是从一个巨大无比的怪物文档中找东西。

该纠偏与此前已经写入 `rulings.md` 的原始定义共同决定本次实现：`核心认知.md` 是用户为元数学创新设计的反训练先验上下文工程，但“必须全文加载”不等于“必须继承旧生成器误纳的全部内容”。当前 core 应从三份用户指定 primary 原件重新构造，只保留用户本人关于悖论、HoTT 悖论挖掘、元数学和直接研究方法的精确原文语义单元。

用户随后明确授权“可以 rename 历史文件，直接放入归档目录中”。两份已经失去 current-truth 资格的 generation-2 报告因此通过 Git rename 进入 `history/governance-v2.1.0/`，并由 S016 迁移 README、方向投影和当前 STATE consumer。顶层 `archive/` 已有原 handoff pack/object store 的专门职责，所以叙事性治理历史使用 `history/`；当前 generation-3 `核心认知.md` 不是历史文件，保持原位和固定全文输入身份。

## 2. 旧版本可恢复基线

| 项 | 基线 |
|---|---|
| Git commit | `7e9b9ee709423234c76a69be2da91da3cb1a7554` |
| annotated tag | `governance-v2.1.0` |
| old core | `core-cognition-generation-2`；913 KC；SHA-256 `7986ed26eab032ae2b79e02a5d64addf1f70b1f3e46bcb35d49b1e839d2ea16d` |
| old manifest | SHA-256 `bf40d8bdeb97022a4191aab99bfc9bdf3563b8f008a82881c7f1c0df54f21e2f` |
| old governance load plan | 105 documents；9,424,036 bytes；110,356 lines |
| old tests | core PASS；three-way PASS；runtime 56/56 PASS；single-core reader 17/17 PASS |

旧 tag 是 rollback authority。没有删除旧 core、旧 manifest、旧 Session、旧逐-KC表、supplemental 或任何原始提取文件。

## 3. generation-3 的语义和数据合同

### 3.1 单一职责

| 资产 | 类别 | 唯一职责 |
|---|---|---|
| `scripts/audit/core-cognition-curation-v3.json` | `HUMAN_EDITED_CURATION_AUTHORITY` | 对三份 primary 的 88 条消息逐条给出纳入/排除理由，并指定精确源行/子串组成语义单元 |
| `scripts/audit/build_core_cognition.py` | canonical manager | 默认只读 check；`--write` 时锁定、原子生成 core/manifest/transition；不做语义裁决 |
| `核心认知.md` | `MACHINE_MANAGED_CANONICAL` 的人类/模型全文输入 | 只展示 27 个按 UTC 排序的直接用户原文语义单元和紧凑来源锚点 |
| `核心认知.manifest.json` | `MACHINE_MANAGED_CANONICAL` 查询/验证层 | 完整 source hash、message disposition、selector、unit hash、主题与关系；不替代 core 正文 |
| `audit/core-cognition-generation-3-transition-20260912.json` | machine-generated history receipt | 对旧 913 KC 逐一给出保留、合并、收窄或退出当前 core 的理由和目标 ID |

### 3.2 当前实际结果

```text
primary files       = 3
messages parsed     = 88
messages included   = 23
messages excluded   = 65
current KC units    = 27
units by platform   = LocalGPT 6 / WebGPT 8 / Gemini 13
core bytes / lines  = 26,870 / 265
core SHA-256        = 8aa005505c68d20eb11c48b946fa61e68b03013d56926ca2b9c928d06c5a7dfb
old KC mappings     = 913 / 913
mapping remainder  = 0
```

65 条排除消息仍全部进入 manifest disposition。主要类型是：附件/可见性、继续指令、一般治理、研究管理、无新增认识的重复、以及 user role 中转发或作者身份不可判定的 AI/复合文本。`GEMINI-M-012` 的长篇自包含征询材料没有被强认定为用户原创；其直接用户认识已由更早可确定原文覆盖，完整文本仍保留在 primary source。

旧 KC 映射当前实际分类：

```text
CURATED_EXACT_SUBRANGE                       24
EXCLUDED_BY_CURRENT_SCOPE                  812
EXCLUDED_NON_CORE_WITHIN_INCLUDED_MESSAGE   10
EXCLUDED_NON_PRIMARY_INPUT                   65
EXCLUDED_RELAYED_AI_CONTEXT                   2
```

旧生成器常把消息尾部 `---` 一并装入单元，所以 24 项是“新 payload 为旧 payload 的精确子范围”，不能伪写成 byte-identical preserve。

## 4. 分层加载架构

`LOAD_SET v3` 的层次为：

1. `always_full_three_way`：core → direction → panorama；任何 profile/task 都不能删减或重排；
2. `always_full_boot`：根治理入口、README/MEMORY/Feature/rulings、本地治理 Skill/协议/STATE；
3. `research_full`：业务 Skill、三问、FRONTIER、LESSONS、RESUME；
4. `query_first`：manifest、source manifest、cross-source register 等机器索引；
5. `task_expand`：理解章节、HoTT owner 和 claim matrix 等按任务证据；
6. `archive_verify_only`：旧 transition、validator 源码、runtime 源码和历史收据。

revision 18 的 final fresh receipt 得到：

| Profile | documents | bytes | lines | 历史 Session 自动加载 | 冷资产自动加载 |
|---|---:|---:|---:|---:|---:|
| governance | 15 | 176,961 | 1,979 | 0 | 0 |
| research | 20 | 247,892 | 2,843 | 0 | 0 |

相对旧 9,424,036-byte 治理计划，governance 默认字节减少 98.12%，research 默认字节减少 97.37%；这不是以 byte 下降证明治理成功，而是证明被移除的是 manifest/历史收据/旧 Session 等非三件套载荷，三件套本身保持完整。

runtime 新增：

```text
plan --profile governance|research [--task ID]
query --record ID
read/check 绑定同一 profile/task snapshot
```

旧 Skill 路径下的 runtime 已改为 canonical `.codex/tools/cognition_runtime.py` 的 compatibility entrypoint，消除两份实现独立漂移。

## 5. STATE v2 迁移合同

目标 schema `hott-working-state/v2` 将两个维度分离：

- `lifecycle_status`：`ACTIVE_WORK | CURRENT | OPEN_ISSUE | CLOSED | HISTORICAL | SUPERSEDED`，决定任务资格；
- `evidence_status`：例如 `REVIEW_REQUIRED | VERIFIED_WITH_SCOPE | NOT_RUN | UNKNOWN`，只描述证据质量。

005–012 等治理 Session 已成为 `HISTORICAL/VERIFIED_WITH_SCOPE`；它们的旧 `status=review_required` 只作 legacy 字段，不再产生自动加载资格。五个真正开放的 `A-*` record 保持 `OPEN_ISSUE/REVIEW_REQUIRED`，没有通过批量关闭缩短计划。S013 原子完成 v1→v2 和 revision 13；manifest-aware validator 随后发现一个旧 core theme，S014 以 revision 14 原位修正；S015 revision 15 对齐 receipt/current owners；S016 revision 16 迁移两份 generation-2 历史报告及 4 个 current consumer；S017 revision 17 将 MEMORY 的旧 three-way 3/3 叙述与实际 4/4 验证对齐；S018 revision 18 把 merge receipt 的同名差异对与单侧独有项分开计数。六次 Session 均为 historical，默认加载仍为 0。v1→v2 缺 rollback ref/receipt 的负向测试会拒绝。

## 6. C01–C10 实施影响闭包

| ID | 结论 | 实际处置 |
|---|---|---|
| C01 | `UPDATE` | `rulings.md` 记录 core 重建纠偏及历史文件 rename 授权；F-003/F-005/F-008/F-010 原位更新要求/交付/验收 |
| C02 | `UPDATE_PROJECT_ONLY` | 本文件与项目协议拥有 generation-3、六层载荷、lifecycle/evidence、兼容/rollback；共享系统设计不变 |
| C03 | `UPDATE_PROJECT_ONLY` | 本地 governance/business Skill、PROTOCOL、runtime wrapper 更新；共享 canonical workflow 不变 |
| C04 | `UPDATE_PROJECT_ONLY` | 根与 `.codex` AGENTS 的启动/压缩路由更新；全局 AGENTS/runtime 不变 |
| C05 | `UPDATE_PROJECT_ONLY` | README/MEMORY/理解章节 current boundary/审计索引更新；两份 generation-2 报告进入 `history/governance-v2.1.0/` 并保留 current replacement |
| C06 | `UPDATE` | 新 core 7 tests、layered runtime 27 tests、reader 17 tests、three-way 4 tests（含 obsolete theme 负向）、fresh byte/profile/task/4-negative receipt、S005/S007 历史 task 对新归档路径的水合、S017 current narrative 修正，以及 merge-count 正/负向验证；fresh model behavior 仍 NOT_RUN |
| C07 | `NO_CHANGE` | 不新增 Hook/Plugin/Rule/config/权限或 secret 接触；当前 host context 只读发现为 1,000,000/900,000 tokens，不写 config |
| C08 | `NO_CHANGE` | WebGPT 快照、OpenCode、`/Volumes/D/ALL-Markdown` 及其 dirty 状态不改；本次是项目专属实现 |
| C09 | `UPDATE_PROJECT_ONLY` | 旧 tag `governance-v2.1.0` 保留；实现提交为 `e18c0a1ae5298006351760be55bcd7e087f8780d`；本文件的最终状态提交由 annotated tag `governance-v3.0.0` 指向，不 push |
| C10 | `UPDATE` | 913/913 transition、旧 Session 冷存、两份历史报告的 Git rename/replacement、未认证模型行为/数学状态和共享主库 dirty 边界全部保留 |

remainder：`0`。

共享治理主库 `/Users/aurolafly/codex` 与 Codex runtime `/Users/aurolafly/.codex` 在本轮检查时均有其它工作造成的 dirty 变化。本轮不修改、不 stage、不 commit 它们，也不把项目 v3 宣称为共享治理 release。

## 7. 已执行验证与证据上限

当前已通过：

- `scripts/audit/test_core_cognition.py`：7/7；
- `scripts/audit/verify_core_cognition.py`：88 messages、27 KC、913/913 transition PASS；
- `scripts/audit/test_three_way_cognition.py`：4/4；
- `scripts/audit/verify_three_way_cognition.py`：27 KC、24 directions、22 outcomes PASS；
- layered runtime tests：27/27；
- core compatibility reader：17/17 PASS；
- STATE v2 checkpoint：S013 revision 13 PASS；projection theme alignment：S014 revision 14 PASS；owner alignment：S015 revision 15 PASS；historical-document archive routing：S016 revision 16 PASS；verification alignment：S017 revision 17 PASS；merge count semantics：S018 revision 18 PASS；S016–S018 各 27/27 KC `NOT_TOUCHED`；
- manifest-aware three-way：4/4 tests，修复前 actual FAIL、修复后 PASS；
- final fresh receipt v2：revision 18、15/20 documents、完整三件套、task hydration、4 negative PASS；S005/S007 显式历史 task 均能解析两份新 history 路径；
- history ledger、understanding merge、cross-source reconciliation、projection freshness 均 PASS。history verifier 首次仍从 current core manifest 检查 Gemini Drive attachment，因 core 正确换代而失败；改为检查历史 `user-message-disposition.jsonl` owner 后 125/384/3,146/111/21/17+17+2/16,209/2,396 分母 PASS。
- understanding merge 的 `different_pairs` 已从“所有非 identical union 项”收窄为真正的同名差异对：24 个同名对=15 identical+9 different；另有 1 top-level unique，因此新增 `nonidentical_union_entries=10`。伪造 `different_pairs=10` 的 fixture 被稳定拒绝。
- `核心认知.md` 的 Gemini primary 原文有一处源末尾空格；`/.gitattributes` 仅对该 canonical 原文关闭 `trailing-space` 报警，使 `git diff --check` 仍可检查其他路径，同时避免违反 exact-source 合同。该例外不改变 payload 或扩大到其他文件。

Git 版本闭合分两步：`e18c0a1ae5298006351760be55bcd7e087f8780d` 保存全部实现、迁移、测试与 checkpoint；随后只更新交付状态和最终 fresh receipt，并以 annotated `governance-v3.0.0` 标记该状态提交。状态提交无法在自身正文中自指其完整 OID，实际身份必须以 `git rev-parse governance-v3.0.0^{commit}` 查询。

证据上限：

```text
CORE_SOURCE_FIDELITY        = VERIFIED_WITH_SCOPE
LOAD_ARCHITECTURE           = IMPLEMENTED_AND_UNIT_TESTED
STATE_V2                    = CHECKPOINTED_REVISION_18
FRESH_PYTHON_RUNTIME        = PASS_WITH_SCOPE_REVISION_18
FRESH_MODEL_BEHAVIOR        = NOT_RUN
MODEL_CONTEXT_UNDERSTANDING = NOT_CERTIFIED_BY_TOOL
MATHEMATICS                 = UNCHANGED / NOT_CERTIFIED_BY_THIS_SESSION
```

## 8. 回滚与残余风险

- core/schema/runtime/STATE 任一最终验证失败：停止发布，不删除现场；以 `governance-v2.1.0` 和 checkpoint before copies 回滚；
- source hash/curation selector 漂移：builder/validator fail closed，不自动重新选句；
- fresh model behavior 未运行：只能声称机械实现，不能声称所有未来模型实际理解/使用三件套；
- 27 个语义单元是本轮人工裁定，可由用户或未来直接证据提出修订；修订必须新 generation，而不是静默覆盖历史；
- 物理时空离散、Z 铁律全称性和 HoTT 自指怀疑仍是用户研究立场/开放问题，不因 core 重建获得数学或物理认证。
