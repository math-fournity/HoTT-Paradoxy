# Session A 工作闭包：第三轮 HoTT 机器统观

> HUMAN_EDITED；可复用的任务闭包，不是原典摘要替代品。方法owner为[goal-5](../../goal-5.md)，事实快照及资格化证据见[整备验收](整备验收.md)。本文件不拥有项目current queue；新Session启动后回读STATE及所有决定性owner。

## 1. 本次接手应知道什么

用户需要AI以其元思考主动找出理论的经济/普适性取舍，并设计恰好使被改条件显形的过程。最近两项增量是：每条结论留痕并审计；统观必须覆盖不同尺度的局部与整体，不能受章节切分约束。A要产出第三轮实际研究，B另行审计。提示词短、完整SOP在goal-5，两份Session提示词分开。

此闭包的来源判断为 `COMPOSE_FROM_OWNERS`：复用核心原文、最高指示、旧覆盖与证明管线，补多尺度工作组织和独立交接。高代价误判包括把模型分支替换其声称回答的问题、把AI解释当用户原话、用局部无异常关闭整体、用源文件/表格/一次PASS宣布发现能力或全理论完备。

当前入口先按TASK_ROUTING读执行Skill和单体goal-6.md，再使用本工具闭包及goal-5.md领域SOP。最高指示第七稿§0B区分总目标、候选自身X_i与实际引用/承接的历史X_h；新候选无须历史祖先，历史保真只在实际引用或声称回答时触发，不强配圆环也不禁止相关题材。14题全部回答，历史子检查可按依据不适用；留出按当前机制缺口选择，不设固定题材配额。旧输入哈希变化按Goal6§8重读与复核，不改旧收据假称已消费。

当前整备读取的基线为main `a98926f65d5c804261c7143084dd49050aa45ef0`，STATE revision268、latest `S-RES-20260923-ASTRA-P47-SYNTHESIS`；这些仅是2026-09-23时点的历史定位。当前core与最高指示身份从实际文件/STATE/整备证据动态核，不将本段当永久活动队列。现场有大量dirty/untracked，不能全库add/commit或清理。

## 2. 阅读顺序和每份材料的用途

|顺序/触发|必须实际加载的入口|解决的认知问题|
|---|---|---|
|启动|根AGENTS；全局`repo-cognitive-closure`与相应workflow；README完整索引/入口片；MEMORY索引/当前队列片；Feature/rulings本题条款|根、权限、旧与新、当前写者、事实owner。|
|启动|`.codex/skills/hott-local-session-governance/SKILL.md`、`.codex/cognition/LOAD_SET.json`、`PROTOCOL.md`、`.codex/skills/SKILL_ROLES.json`、STATE|生命周期、分档、加载与checkpoint。|
|首次research|`核心认知.md`→`方向追踪.md`及全部分片→`全景视野.md`及全部分片→`扩展认知.md`及全部分片|用户原意、方向、成果、AI阐释四种身份；严格顺序和EOF。|
|每个新语义单元|`最高指示.md`全文；core KC-000047/048完整原文；当前源段|发现态优先、重新呈现、逐结论审计；原文不被熟悉代理替代。|
|启动research|`.codex/skills/hott-paradox-research/SKILL.md`、`hott-paradox-search-sop/SKILL.md`；research plan列出的三问、FRONTIER/LESSONS/RESUME|研究流程、反思、当前前沿和避免重复。|
|系统化研究启动|程序化完备性规划索引及全部001–006分片；本goal5全文|八轴、TC/OP、方法选择、未知入口、本轮完成范围。|
|W1|`HoTT/THEORY_SCHEMA.md`、`HoTT/theory-schema/SOURCES_AND_COVERAGE.md`及各C/D/S/E正文；总体方案006；理论检视001/009/010|实际理论分母、已有首轮覆盖/局限、待复用候选排序。|
|W1/W2|`dev-docs/第三轮机器统观多尺度覆盖改进工作方案-20260923.md`|五尺度、语义关系、结构驱动、方法控制的设计根据。|
|候选查重|`audit/机器统观目标与针对性策略审计-20260922.md`；PREMISE-001索引及命中分片；goal-3与旧路径树；对应proof/run|旧代理、密度解释、来源/复原合同偏移、真正未审的差分。|
|效果/原意审计|`audit/最高指示Astra质量复审-20260923.md`、`audit/最高指示结论审计与偏差复测-20260923.md`；原始用户sources|先前行为测试的范围，不能把有提示且顺序混杂测试当永久能力。|
|强数学结论前|`docs/quality/数学结论机器证明与证据留存规范.md`；精确source/run/index/registry|原生语义、实际检查、版本闭合与禁止外推。|

相对路径均以repo根解释（表中Skill短名相对于`.codex/skills/`）。上述owner若是逻辑索引，按任务触发读相应完整分片；四件套和完备性规划首次必须全读。索引、manifest、旧总结、hash都不能替代决定性正文。关于核心原意的跨主题纠偏，再按根AGENTS完整重读核心与扩展。

## 3. 必须持续保留的四项语义对齐

1. **用户主张**：理论为经济和普适性作非现实抽象，悖论的构造应专门触及这些条件；本轮先把这作为生成视角实际使用。
2. **不得收窄**：不把所有案子变成信息丢失、类型拒绝、耗时或一般不可判定；不把多尺度只做成更多pairwise或更深目录。
3. **怎样改变行动**：先问理论取舍并生成过程；无低层异常也做高层检查；精化后保留原问余项；每个公开结论可回源可撤回。
4. **仍开放的义务**：理论实际规则、候选成立性、现实桥、原生证明、范围外未知。研究姿态一致不等于这些义务自动成立。

## 4. 可直接调用的加载工具

在repo根执行，完整输出可保存本轮独占目录再逐块实际读取：

```bash
python3 -B .codex/tools/cognition_runtime.py plan --profile research
python3 -B .codex/tools/cognition_runtime.py query --record RECORD_ID
python3 -B .codex/tools/cognition_runtime.py plan --profile research --task RECORD_ID
python3 -B .codex/tools/cognition_runtime.py read --snapshot SNAPSHOT --path RELATIVE_PATH --start-line 1 --max-bytes 8000 --profile research
python3 -B .codex/tools/cognition_runtime.py check --snapshot SNAPSHOT --profile research
```

大写项是本次plan/query真实返回值，不能原样执行。task plan与read/check必须使用一致task参数。read返回下一行/EOF，接着读取；单次工具输出截断不能算完成。plan输出的query_first_promoted应为空；否则查真实依赖边，不把巨大历史账本当正文。整备时research plan可以生成，但这不证明新Session已读或理解。

研究起步T2；注册/更新STATE或交付数学结论前T3，按根协议补全对应义务。模型上下文容量以实际host为准，不依赖文档中的旧容量估计；分块读取和压缩恢复不会免除用户规定的完整输入。

## 5. 原生工具链与证据命令

本机可用的原生检查器不是PATH上的`agda`，而是`/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/agda`。固定工具链例见`HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`与`AGDA_LIBRARIES`，包含Agda2.8.0、Cubical0.9的binary/archive/tree身份。每次环境变化重核，不按名称相信版本。其他演算先资格化，不能为方便偷换语义。

新proof用原生源码与对应toolchain/库登记，实际capture入口：

```bash
python3 scripts/audit/capture_agda_proof_run.py --help
python3 scripts/audit/verify_formal_proof_run.py --help
python3 scripts/audit/verify_proof_version_closure.py --help
```

capture必填run-id/proof-id/claim-id/source/toolchain/scope/non-goal；传递本地import通过重复`--manifest-file`纳入。以当前唯一matrix分配新C-ID，MP-ID与run用MO3前缀防撞。捕获完成后按现有proof规范登记精确matrix/registry关系，使用`mark_proof_run_indexed.py --run-dir ...`、`freeze_proof_index_rows.py --run-dir ...`和验证器。registry新增package沿当前规范与canonical writer（若字段已经有manager则必须用它），不得改旧package或把replay冒作新定理。

只复跑旧claim时使用已有replay注册路径，不覆盖primary。先验证本轮proof的`--evidence-only --proof-id ...`范围，再分别报告Git闭合；全局旧缺口不能伪称已修，也不能取代本轮真正依赖缺口的处理。官方proof运行至少保存RUN/stdout/stderr/environment/source-manifest五件套及精确索引关系。整备的正负工具测试只资格化运行方法，不注册新数学成果。

## 6. 原子状态写回接口

`cognition_runtime.py checkpoint --snapshot HASH --payload PATH`默认dry-run，确认后加`--apply`。payload的已存在schema为：

```json
{
  "schema_version": "cognition-checkpoint/v1",
  "session_id": "本次全新S-ID",
  "load_profile": "research",
  "task_ids": [],
  "authorization": "引用用户本次启动提示词的实际授权",
  "files": [{"path": "repo相对路径", "expected_sha256": "当前hash或新文件null", "text": "完整文件正文"}]
}
```

这是结构示意，不能直接当有效payload。须包括runtime的全部MUTABLE及其全部逻辑分片（未改也保留原字节）、新SESSION/RUNS/当前generation完整CORE_COGNITION_AUDIT；STATE revision只推进一次，latest/新record/path/kind/真实依赖一致。动态读取runtime和HEAD tracked，拒绝硬编码revision或套旧payload。

可复用`projection_edit.py`的load/replace_in_index/replace_in_shard/append_to_shard/payload_rows；`audit/p47-theory-synthesis-20260923/checkpoint_p47.py`仅为调用范例，**不得执行**，其中sid/revision/语义属于旧任务。A应为本轮实际内容生成payload，不临时开发第二个状态writer。

当前writer允许session第一层文件，却未完整支持事务中的嵌套audit shards。先回读PROTOCOL兼容规定：事务内完整审计满足现行checker，额外分片审计在独占证据路径保留并标原子边界。不能把新审计略掉，也不能声称未支持的原子性已实现。lock/stale冲突先重新plan，不抢锁、不绕过writer。以canonical result.json判定成功。

## 7. 交给 B 的接口

A的最终报告、覆盖/关系、过程结果、结论账本、方法控制和执行证据均按goal5§12纳入seal。`handoff_snapshot.py`只有seal/verify两项职责，不做数学裁决，不管current state，不自动收集整个repo。清单一行一个相对常规文件，注释以#开始，不接受目录/通配符/路径穿越/符号链接；A须明确列依赖文件。

B收到manifest身份后独立审同一字节；A新版本另封新目录。若外部库/工具消失，B有明确版本和来源可以诊断，不能用邻近版本默默替代。B不需要A的隐藏思维或全盘环境变量；证据以公开论证、源文、工具输入输出和源码为准。

## 8. 失效、未知与交接完成

本闭包在user目标/权限、最高指示/core、schema/source版本、工具链、checkpoint合同、当前写者、封存接口变化时失效对应slice。重新回源并更新本轮工作集；不能把2026-09-23整备PASS当未来现场PASS。

已知未知：尚无第三轮发现、A真实执行、B审计、未来模型持续遵守的证据；整备没有改变这些事实。本轮当前整备只保证文件/接口/已测范围；由A启动时资格化新现场。A完成需满足goal5全项，不能以本闭包加载完成代替研究完成。

## 递归多尺度的当前消费边界

当前方法依据[多尺度改进工作方案](../../dev-docs/第三轮机器统观多尺度覆盖改进工作方案-20260923.md)，完整操作合同在Goal5§5/7/13及Goal5-audit§4。五种方式不是固定深度，允许嵌套、重叠、多父与横向重组；关系保留联合条件、顺序、共享背景和理论配置。上下往返及无信号结构驱动须有实际记录；各已接受中高层问题独立对账，不能继承叶子PASS。核同源重排/删中层等粒度负例与真实HoTT重组，区分预给合成控制与自主发现。旧格化设计保留历史理由，不再作为当前选题模板；恢复按第七稿重新消费，旧收据不改。

恢复入口还必须完整消费[Goal6 §0](../../goal-6.md)的MO3-MS-01至MO3-MS-06及所链接方案/自审；在已有执行记录登记各项复用依据、待办和下一动作，按对应波次交付，未闭合不标完成。
