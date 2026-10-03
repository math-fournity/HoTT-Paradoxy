# 项目任务与上下文角色路由

> HUMAN_EDITED；唯一任务入口映射；2026-09-24。它不保存研究进度、不自动启动Goal。当前事实仍从用户/实际Goal/STATE及成果owner恢复。Goal7续做包已准备，C/D尚未由本准备工作启动。

先执行全局repo-cognitive-closure，再消费本项目root AGENTS、共同治理Skill及本页。任何项目Session均全文加载`最高指示.md`并按其§0A确定上下文角色；本页、metadata或hash不能替代正文。读取后先完成理解复核，再开始依赖它的行动。

|当前任务/明确身份|最高指示角色|必读项目Skill|单体开工闭包|领域细则|启用边界|
|---|---|---|---|---|---|
|用户新开第三轮续做C，或注入Goal7执行词|RESEARCH_GENERATION|`.codex/skills/hott-machine-overview-execution/SKILL.md`的Goal7分支|`goal-7.md`|Goal7拥有父范围/SOP/完成门；Goal5只复用不冲突纪律|注册MO3-COVERAGE-C须在实际启动后；旧A closed不是父目标完成。|
|用户新开续做成果审计D，或注入Goal7审计词|INDEPENDENT_AUDIT|`.codex/skills/hott-machine-overview-audit/SKILL.md`的Goal7分支|`goal-7-audit.md`及Goal7|先父范围充分性，再研究与证据|审C的新固定交付，不能以A final-002代替；不写研究状态。|
|第三轮机器统观的执行者A，或用户注入Goal6执行词|RESEARCH_GENERATION|`.codex/skills/hott-machine-overview-execution/SKILL.md`|`goal-6.md`|`goal-5.md`|只有用户启动/继续本研究后执行；文件存在不激活。|
|独立审计第三轮最终成果的B，或用户注入Goal6审计词|INDEPENDENT_AUDIT|`.codex/skills/hott-machine-overview-audit/SKILL.md`|`goal-6-audit.md`|`goal-5-audit.md`|先有唯一有效A封存输入；只写自己的审计证据。|
|用户要求模式 P 的 P1/P2/P3 动态 DAG、来源节点或 Battle；或要求 Master 按节点决定盲态、项目分支与网络访问；或在 `/goal` 中引用 `P-FORGE-SOP` 要求持续锻造、新刀、全历史自审或 Power Set 防御审查|GOVERNANCE_ALIGNMENT（Master）；实际理论节点按其自身证据任务使用 RESEARCH_GENERATION|`.codex/skills/hott-pattern-p-dynamic-dag-orchestration/SKILL.md`|`dev-docs/模式P刀具持续锻造SOP.md` + `dev-docs/模式P动态DAG调度.md` + 当轮 TaskCard|用户当前 P-DAG scope、P-FORGE-SOP与三把刀/共同锻造合同|只在根 AGENTS 的 2026-10-02 scoped authorization 下启动 Terra/Max read-only nodes；P-FORGE-SOP 不自行授权worker、网络、数学STATE写入或理论结论。|
|其它HoTT理论研究|RESEARCH_GENERATION，审计时INDEPENDENT_AUDIT|`hott-paradox-research`；实际执行有界步骤时再加载`hott-paradox-search-sop`|当前用户/Goal/STATE对应owner，不自动选6|该任务真实spec|不因本页列了第三轮就切到第三轮。|
|纯解释、原意澄清或项目答疑|SOURCE_EXPLANATION|共同治理及实际匹配的资料读取；core语义按source-first|当前问答所需owner即可|原文及来源身份|直接回答本题，不强制新候选/14题，不自动开始研究；真实研究另切角色。|
|治理/整备/提示词或Skills维护|GOVERNANCE_ALIGNMENT|`hott-local-session-governance`及相关全局治理Skills|本任务方案/owner；第三轮治理见`dev-docs/Goal任务项目治理化与全局复用方案-20260923.md`|当前治理合同|不生成数学结论，不擅自写数学current队列。|
|纯机械文件/工具维护|MECHANICAL_CONTEXT|共同治理的角色/来源边界；仅实际匹配的其它Skill|当次任务即可，不强建Goal|具体操作合同|不额外创建研究或审计任务。|

所有项目Skill路径均以repo根解释，短名对应`.codex/skills/<name>/SKILL.md`。Skill没有显示在host菜单时仍按路径读取，不能报告“没有该工作法”或另写同名副本。实际缺文件则停止依赖链，报告缺件；不凭训练记忆补齐。

Goal6/5保留原A/B阶段及固定旧交付的身份。用户要求继续完成父范围时，当前接续方案为新C/D与Goal7，入口见[接续方案](../../第三轮机器统观/续做整备/接续方案.md)。若用户明确指定原A/B任务，则按其精确范围读取旧合同，不擅自改host objective；未明确启动时只准备。编号最大或旧提示词存在不能自动恢复研究；其它goal/1/3同样不复活。

恢复顺序：确认用户/实际Goal与角色→root/common协议→本页→对应完整Skill/单体闭包→最高指示及该角色必读原文/当前证据→公开恢复说明与下一动作。四件套在其适用档位仍按核心→方向→全景→扩展顺序全文，通用收据豁免不能豁免最高指示的专门重读要求。

角色/目标不明或A/B权限冲突时暂停有副作用的分支，仍可完成共同只读闭包；只在确需用户选择时询问。不能用最高编号、最新文件、旧摘要或某个Skill的说明来确定当前任务。

跨Session/压缩/角色/Goal变更以及Skill/最高指示/闭包/关键来源版本改变，使对应任务输入失效。重新完整读取必读入口、核权威与未证项；完成说明至少含当前role/goal、实际读到的版本与EOF、原意/验收一句复述、上次状态/未完成项及本次动作。它是公开研究说明，不索取隐藏推理。

当前最高指示仍为第七稿；执行/审计Skill1.3.0同时保原任务分支与Goal7分支，common4.3.0选择角色。递归多尺度和X_i/X_h分离继续保留；Goal7新增PARENT_SCOPE_SUFFICIENCY_V1，先父范围到研究集的充分性，再研究结案。来源变更触发实际消费，不由维护者假写研究收据。旧[方法自审](../../audit/第三轮机器统观多尺度覆盖再次自审-20260923.md)保存原字节边界，其完成标准缺口见[专项复核](../../audit/第三轮机器统观全面覆盖与完成资格专项复核-20260924.md)。

原A/B仍可由Goal6六项追溯；C/D使用Goal7的范围充分性及研究完成双重验收。进度只由实际研究/审计实物证明，准备者不代填完成；新旧角色的写路径不得交叉。
