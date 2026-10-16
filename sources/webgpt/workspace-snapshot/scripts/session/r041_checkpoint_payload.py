#!/usr/bin/env python3
"""R041 ZCode governance integration: build the checkpoint payload for the single original engine.

Read-only against current state; writes only scripts/session/r041_checkpoint_payload.json.
Run: python3 -B scripts/session/r041_checkpoint_payload.py
"""
from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[2]
SID = 'S-GOV-20260911-041-ZCODE-INTEGRATION'
SESSION_REL = '.codex/research/hott/sessions/' + SID + '/SESSION.md'
MUTABLE = [
    'MEMORY.md',
    '.codex/research/hott/FRONTIER.md',
    '.codex/research/hott/LESSONS.md',
    '.codex/research/hott/RESUME.md',
    '.codex/research/hott/STATE.json',
]
PINNED_SOURCES = [
    'governance/ZCODE_INTEGRATION.md',
    '.zcode/HOTT_ENTRYPOINT.md',
    'exchange/rounds/R041-ZCODE-GOVERNANCE/REQUEST.md',
    'exchange/rounds/R041-ZCODE-GOVERNANCE/RESEARCH_DELTA.md',
    'exchange/rounds/R041-ZCODE-GOVERNANCE/AUDIT_REQUEST.md',
    'exchange/rounds/R041-ZCODE-GOVERNANCE/ROUND.json',
    'exchange/outbox/zcode-takeover-plan.json',
    'scripts/session/r041_checkpoint_payload.py',
]
READ_ONLY_SOURCES = [
    'exchange/rounds/R041-ZCODE-GOVERNANCE/RUNS.json',
]


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(rel):
    return sha_bytes((ROOT / rel).read_bytes())


def dump(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2) + '\n'


MEMORY_TEXT = """# MEMORY · revision41 · ZCode接手与治理接入

状态 ACTIVE。R041由ZCode Desktop 3.8.1（build 3.8.1.5310）接手：用户2026-09-11指令为完整读交接README后接手，并做好项目内ZCode治理框架文档。交接验收实际执行：verify_package PASS（5729文件哈希、324份原件748,544,776字节可重建）、git HEAD=tag handoff-r040=6581d1a2、status干净、fsck无错。最后实际数学仍R039。

## R041实际新增
- `governance/ZCODE_INTEGRATION.md`（zcode-integration v1.0.0）：ZCode产品事实基线（两级AGENTS组合、Skill 1024/100KB限制、项目Hook忽略、Project Memory不可审计、无CLI/ACP、model-io轨迹）、加载映射、标准会话流程、RTK输出过滤警告（全文加载必须`rtk proxy`或内置Read）、Skills默认不注册与指针Skill规范、隐私边界。
- `.zcode/HOTT_ENTRYPOINT.md`：经官方`govern.py install-entry --directory .zcode`生成的转接指针；ZCode不自动发现项目内.zcode。
- 包外层`onboarding/RECEIVER_ACK.md`：真实接手记录（治理链全文读入；数学语料未全文加载，不声称完整认知验收）。
- `exchange/rounds/R041-ZCODE-GOVERNANCE/`：REQUEST/RESEARCH_DELTA/AUDIT_REQUEST/RUNS/ROUND齐备。
- 本checkpoint revision41经唯一原引擎提交；随后本地git commit；未push、未外发。

## 共同认识和成果不变
HoTT的已有能力、共享计算界限与具体理论化新增失真分开；双向现实相对目标、ASK与Z原话、正反例和独立思考保留。原records逐值保留。R039回源仍为SILENT-STEPS-001/PROOF_NOTE.md；R038迁移Acc、R036抽象假路径、R033—34路径作用、R029—32反射、RP-B01和R026均沿旧链保留。

## 检查边界
ZCode本机产品事实经/Users/aurolafly/zcode权威库复核（2026-08-25核查、本轮复核）；未做raw model-io级注入复核。原生证明助手未运行，历史NOT_RUN不升级。密封包清单只对接收时点负责：接收方开工后顶层verify_package报Unexpected files是预期行为，此后完整性以git差异对handoff-r040与exchange协议为准。

## 后续
ZCode数学会话先按govern.py plan全文加载（RTK警告见ZCODE_INTEGRATION §4.3），完成RECEIVER_ACK级真实读入后再研究。下一未执行候选仍为：保结果确定性部分性等价上顺序bind与race/timeout的下降条件。不重复R039自环枚举，不等Gemini，不凭历史权限push/发信/改模型。
"""

FRONTIER_TEXT = """# FRONTIER · revision41 · 数学前沿仍R039；R041为ZCode治理接入

当前`P-SILENT-STEPS-039`：完成R038约定的silent-step检查。精确结果：发散不敏感弱互模拟保本例may、不保must；有限跳过与无限单边余归纳不同，后者Bad甚至非传递；正确Delay关系有终止/结果保护。

该族停止追加同类图穷举。下一有判别力的候选：确定性部分结果等价与race/timeout操作的组合，核真实操作类型及quotient respect，不把共用"等价"名称当成同一合同。RP-B01原生对应和R026规约/环境有效范围仍开放，不因工具缺失清空。没有发给其他AI的依赖任务。

R041由ZCode Desktop接手，只做宿主治理接入（governance/ZCODE_INTEGRATION.md与.zcode指针），下一数学动作未执行。接手按governance/ENTRYPOINT.md、外层README和当前全文计划恢复；增量交流按exchange/。
"""

RESUME_TEXT = """# RESUME · revision41

先读完整包外层README、项目AGENTS与governance/ENTRYPOINT.md；ZCode宿主再读governance/ZCODE_INTEGRATION.md（含RTK全文加载警告与Skills/Pointer/Hook边界）。通过scripts/handoff/govern.py生成当前全文计划，先第五闭包再三问并读所有实际依赖；必要时一次载入onboarding核心全文卷并核快照。不要把旧报告中的根路径当当前根。R041真实接手记录在包外层onboarding/RECEIVER_ACK.md。

原最后研究R039；新AI如需继续，从原STATE/FRONTIER列出的Delay结果等价与race/timeout选有判别力的动作。原records未删。R040交接、R041 ZCode治理接入均无新数学。

默认exchange/rounds/<id>独立存用户请求、实际增量、审计问题和运行账本；用户要求时commit后导出，仅传共同基线后的变更。首次共同基线tag为handoff-r040，实际HEAD见外层manifest。导出不自动认可，接收不自动合并。

已知旧治理测试3处陈旧断言失败见VERSION_NOTES；不要复制为新错误或伪称历史全部通过。R001原源缺口和原生工具未运行状态继续保留。
"""

LESSONS_ADDITION = """
## R041 · ZCode宿主接入

- 宿主输出压缩Hook（本机RTK）会静默截断`govern.py read`的全文输出，使"全文已进入上下文"失真；全文认知加载必须`rtk proxy`绕过或用不经Hook的内置Read工具，压缩输出不能当认知收据。
- ZCode只自动组合全局与workspace根两级AGENTS；governance/、.codex/对其无特殊身份。单真值源因此天然保持——不为宿主便利复制Skill正文或可变状态；如需slash入口只建指针Skill。
- 密封包清单只对接收时点负责；接收方开工后verify_package报Unexpected files是预期，完整性改由git基线与exchange协议承担，不是包损坏。
- 项目内.zcode/目录不被ZCode自动发现；install-entry生成的指针只服务按惯例查找的人/AI，不构成自动加载声明。
"""

SESSION_TEXT = """# S-GOV-20260911-041 · ZCode宿主治理接入

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
"""


def main():
    state = json.loads((ROOT / '.codex/research/hott/STATE.json').read_text())
    assert state['revision'] == 40 and state['latest_session'] == 'S-HANDOFF-20260911-040-CHECKPOINT'
    new_state = json.loads(json.dumps(state))
    new_state['revision'] = 41
    new_state['latest_session'] = SID
    if SID in state['records']:
        raise SystemExit('record already exists')
    new_state['review_due'] = sorted(set(state['review_due']) | {SID})
    new_state['records'][SID] = {
        'cognition_status': 'BOUNDED_GOVERNANCE_ENGINEERING_NOT_FULL_RESEARCH_COGNITION',
        'depends_on': ['S-HANDOFF-20260911-040-CHECKPOINT'],
        'full_sources': PINNED_SOURCES + READ_ONLY_SOURCES,
        'kind': 'session',
        'mathematical_status': 'UNCHANGED_FROM_R039',
        'path': SESSION_REL,
        'scope': 'ZCode host governance integration docs and entry pointer; no new mathematics',
        'source_hashes': {p: sha_file(p) for p in PINNED_SOURCES},
        'status': 'review_required',
    }
    ec = dict(new_state['execution_control'])
    ec.update({
        'status': 'ZCODE_HOST_INTEGRATED',
        'reason': 'User directed ZCode takeover plus in-project ZCode governance framework documentation; governance engineering only.',
        'request_path': 'exchange/rounds/R041-ZCODE-GOVERNANCE/REQUEST.md',
    })
    new_state['execution_control'] = ec
    lg = dict(new_state['local_git'])
    lg['pre_checkpoint_head'] = '6581d1a2e75e9f931a77e7021c2197c7f4381de6'
    new_state['local_git'] = lg

    lessons_old = (ROOT / '.codex/research/hott/LESSONS.md').read_text()
    if not lessons_old.endswith('\n'):
        lessons_old += '\n'
    new_texts = {
        'MEMORY.md': MEMORY_TEXT,
        '.codex/research/hott/FRONTIER.md': FRONTIER_TEXT,
        '.codex/research/hott/LESSONS.md': lessons_old + LESSONS_ADDITION.lstrip('\n'),
        '.codex/research/hott/RESUME.md': RESUME_TEXT,
        '.codex/research/hott/STATE.json': dump(new_state),
    }
    files = []
    for rel in MUTABLE:
        files.append({'path': rel, 'expected_sha256': sha_file(rel), 'text': new_texts[rel]})
    files.append({'path': SESSION_REL, 'expected_sha256': None, 'text': SESSION_TEXT})
    payload = {
        'schema_version': 'cognition-checkpoint/v1',
        'session_id': SID,
        'authorization': 'User 2026-09-11: 完整加载交接README并按其指示接手，做好项目内的ZCode治理框架文档；沿用2026-09-10本地Git与checkpoint授权；不授权push/外发/模型切换。',
        'files': files,
    }
    out = ROOT / 'scripts/session/r041_checkpoint_payload.json'
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'PAYLOAD_BUILT', 'path': str(out), 'session_id': SID,
                      'state_revision': 41, 'pinned_sources': len(PINNED_SOURCES),
                      'read_only_sources': len(READ_ONLY_SOURCES)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
