# S-GOV-20260911-041 · ZCode宿主治理接入

## 任务与权限
用户2026-09-11原话见 `exchange/rounds/R041-ZCODE-GOVERNANCE/REQUEST.md`：完整读交接README后接手，做好项目内ZCode治理框架文档。授权范围=read、workspace内新增文件、经唯一引擎checkpoint、本地git commit（2026-09-10既有授权）；不push、不对外发送、不改模型。

## 读取版本
接手时HEAD 6581d1a2e75e9f931a77e7021c2197c7f4381de6（=tag handoff-r040，status干净，fsck无错）；verify_package PASS（5,729文件、324份原件748,544,776字节字节级重建、快照一致）；治理snapshot 446bf757…、revision 40、plan 488 documents。治理链全文读入：包外层README、workspace AGENTS、governance全部入口文件、两份原Skill与SKILL_ROLES、PROTOCOL、USER_REQUIREMENTS、LOAD_SET、MEMORY、FRONTIER、RESUME、HANDOFF_RESEARCH_STATUS、exchange/README、checkpoint模板、STATE结构与90条records状态分布。数学语料（第五闭包、三问、用户原话owner、主张矩阵、onboarding卷）本轮未全文加载——本轮为治理工程，如实记录于包外层RECEIVER_ACK，不声称完整认知验收。

## 实际行动
1. 移出误放包根的自引用ZIP（至包外/Volumes/D/）后verify_package通过；git四项检查通过。
2. 新增 `governance/ZCODE_INTEGRATION.md`（zcode-integration v1.0.0）：产品事实基线、加载映射、标准会话流程、RTK全文加载警告、Skills不注册策略与指针Skill规范、Hook/Project Memory/model-io边界、已验证与未验证清单。
3. 经官方 `govern.py install-entry --directory .zcode` 生成 `.zcode/HOTT_ENTRYPOINT.md`（ENTRY_WRITTEN_NOT_HOST_AUTODISCOVERY_VERIFIED）。
4. 建立并填实 `exchange/rounds/R041-ZCODE-GOVERNANCE/`（REQUEST/RESEARCH_DELTA/AUDIT_REQUEST/RUNS/ROUND）。
5. 本checkpoint（revision 40→41）经唯一原引擎dry-run后apply提交；随后本地git commit。

## 证据与失败
逐项argv/退出状态在RUNS.json。失败记录：首次verify_package因包根多余ZIP报Unexpected files，移出后通过（原因与处置已记录，非包损坏）。无数学证据变化。

## 范围与结论变化
mathematical_status UNCHANGED_FROM_R039；无数学结论、候选、证明状态变化。新增工程认识进LESSONS R041（RTK截断风险、单真值源在ZCode下天然保持、密封清单时效、.zcode不自动发现）。

## 受影响依赖
未修改AGENTS.md、PATHS.json、LOAD_SET.json、PROTOCOL、两份Skill与任何数学语料；无旧record依赖失效（无source_hashes变动）。S-GOV-20260911-037与S-RES-20260911-036锚定的AGENTS.md字节未动。

## 下一动作与未执行项
ZCode后续数学会话按ZCODE_INTEGRATION §4流程先完成全文加载（第五闭包起）再研究；race/timeout下降条件候选未执行。未执行：原生证明助手（NOT_RUN）、旧session脚本批量运行、raw model-io级行为注入复核、其他机器ZCode行为验证。
