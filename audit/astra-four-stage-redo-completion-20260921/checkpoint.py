#!/usr/bin/env python3
"""Close only the scoped original-four-stage redo; do not start phase two."""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = 'S-COM-20260921-ASTRA-FOUR-STAGE-REDO-COMPLETE'
BASE = '.codex/research/hott/sessions/' + SID + '/'
REPORT = 'Astra继续尝试/断点与证明机制系统检查/第三十五轮执行报告.md'
DELIVERY = 'audit/astra-assumption-integration-20260921/DELIVERY.json'
GOAL = 'goal.md'
PLAN_COMMIT = '8b625564ba32ebd8d514166ed5712b915b21abd0'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(body, old, new):
    result, count = re.subn(re.escape(old), new, body, count=1)
    assert count == 1, old
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('runtime', ROOT / '.codex/tools/cognition_runtime.py')
    runtime = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(runtime)

    assert (ROOT / 'goal.md').read_text().splitlines()[0] == '# 四弹一体原方案 redo Goal'
    assert subprocess_output(['git', 'rev-parse', 'HEAD']) == PLAN_COMMIT
    state = json.loads((ROOT / runtime.STATE).read_text())
    assert state['revision'] == 209
    head = json.loads((ROOT / runtime.HEAD).read_text())
    assert all(sha(ROOT / path) == value for path, value in head['tracked'].items())

    plan = runtime.plan(ROOT, profile='research', task_ids=['R-ASTRA-ASSUMPTION-INTEGRATION-20260921'])
    assert not plan['review_required']
    assert not plan['hydration_diagnostics']['query_first_promoted']
    (OUT / 'CHECKPOINT-PLAN.json').write_bytes(runtime.dump(plan))

    prior_latest = state['latest_session']
    state['revision'] = 210
    state['latest_session'] = SID
    retain_active = {'I-DIRECTION-PORTFOLIO-20260912', 'I-OUTCOME-PANORAMA-20260912'}
    state['active'] = [item for item in state['active'] if item in retain_active]
    retired = [
        'A-ASTRA-CONTINUING-GOAL-20260919',
        'A-HOTT-MACHINE-OVERVIEW-GOAL-002',
        'A-R4-HOTT-NAT-EFFECTIVITY-001',
        'A-PREMISE-001',
    ]
    for record_id in retired:
        record = state['records'][record_id]
        record['lifecycle_status'] = 'SUPERSEDED'
        record['evidence_status'] = 'PARKED_PENDING_EXPLICIT_PHASE2_TRIGGER'
        record['status'] = 'parked_by_four_stage_redo_goal'
        record['resolution'] = {
            'evidence': [GOAL, REPORT, DELIVERY],
            'reason': 'The user replaced the current goal with a two-phase redo. These remain historical or phase-two candidates and cannot auto-start.',
        }

    result = state['records']['R-ASTRA-ASSUMPTION-INTEGRATION-20260921']
    result['evidence_status'] = 'PHASE_1_REDO_COMPLETED_WITH_SCOPE / SOURCE_CONTRACT_AUDITED_NOT_COQ_REPLAY'
    result['status'] = 'original_four_stage_redo_completed_with_scope_target_not_established'
    result['scope'] = (
        'The six original user statements/five historical plans, C321–324, geometry/arithmetic controls, '
        'nine qualified proof packages and fixed primary locator source were reconciled. The original whole '
        'four-stage defeat target is not established: the same-task bridge and unconditional actual theoretical '
        'commitment are absent in the inspected scope. Exact local results remain. This is not a global HoTT '
        'safety theorem, Coq replay, physical realization result, or phase-two candidate proof.'
    )
    result['related_records'] = list(dict.fromkeys(result['related_records'] + [SID]))

    state['records'][SID] = {
        'kind': 'session',
        'path': BASE + 'SESSION.md',
        'lifecycle_status': 'HISTORICAL',
        'evidence_status': 'PHASE_1_COMPLETION_AUDIT_WITH_SCOPE',
        'status': 'complete_with_scope',
        'depends_on': [],
        'related_records': ['R-ASTRA-ASSUMPTION-INTEGRATION-20260921', prior_latest],
        'full_sources': [BASE + name for name in ('SESSION.md', 'RUNS.json', 'CORE_COGNITION_AUDIT.md')],
    }
    state['execution_control'].update(
        status='FOUR_STAGE_REDO_PHASE_1_COMPLETE_WITH_SCOPE',
        last_checkpoint_session=SID,
        checkpoint_result='.codex/cognition/checkpoints/' + SID + '/result.json',
        next_minimal_verification=(
            'NONE_BY_DEFAULT. Start phase two only if a new explicit user instruction or a documented '\
            '判词改变凭据 identifies a concrete same-task commitment, counterexample, source/run invalidation, '\
            'or unmet fixed six-obligation question.'
        ),
        current_phase='PHASE_1_COMPLETE',
        second_phase_status='NOT_OPENED',
        phase_1_result_record='R-ASTRA-ASSUMPTION-INTEGRATION-20260921',
    )

    session = f'''# {SID}

- host: Codex desktop local
- model: GPT-5-based Codex；不认证服务端路由
- tier: T3 completion-state mutation
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: 四弹一体原方案 redo 的第一阶段
- plan_commit: {PLAN_COMMIT}
- status: PHASE_1_COMPLETE_WITH_SCOPE / SECOND_PHASE_NOT_OPENED

本单元不新增数学命题、证明源码、内核运行或外部来源。它执行用户 2026-09-21 的两阶段 goal：原四弹 redo 可以以范围判词完成，新候选研究必须另立且先满足判词改变凭据。第三十五轮报告逐项覆盖过程、对象与兑现、识别、元层、层间桥、理论承诺、保任务恢复与证据范围；结论是原整体击落论证未建立，局部原生结果保留。九包十八资格收据、14 固定 Coq 源字节/声明定位、revision209 收据和交付核验均仍可定位。本轮不因旧资格脚本的非幂等输出目录保护而删除或重跑未变输入。

旧机器统观/PREMISE/R4 活动记录改为 SECOND_PHASE 候选，不再位于 active 队列；它们不是被数学反驳或删除。根 goal、goal-1、rulings 与四弹策略已先在 {PLAN_COMMIT} 记录。feature-list.md 有另一写者的未提交改动，本单元不覆盖它。无 Sub Agent、push、tag、公开或外部消息。

本检查点只同步 current state：goal 完成资格、投影/MEMORY/FRONTIER/RESUME、46 KC 回评及唯一 canonical receipt。工具不认证模型理解或数学真理。
'''

    core = state['current_core']
    headings = re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$', (ROOT / '核心认知.md').read_text(), re.M)
    assert len(headings) == core['kc_count'] == 46
    audit = f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: FOUR_STAGE_REDO_PHASE_1_COMPLETE_WITH_SCOPE
- panorama_change: ORIGINAL_TARGET_NOT_ESTABLISHED_WITH_PRESERVED_LOCAL_RESULTS
- essay_change: NO
- update_decision: 原四弹 redo 已形成可交付范围判词；第二阶段未开启
- cross_conflicts: 旧 machine-overview current goal 与新两阶段 goal 已在 goal.md/STATE 原位收敛；feature-list.md 有外部 dirty 改动未覆盖
- unresolved: 新的同任务实际承诺、反例机制、证据失效或用户明确第二阶段指令才可重开

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
'''
    directly = {1, 3, 5, 10, 12, 14, 15, 19, 21, 22, 31, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46}
    for number, (kc, title) in enumerate(headings, 1):
        if number in directly:
            relation = 'DEEPENED' if number not in {3, 15, 19, 38, 43} else 'CORRECTED'
            reason = '第三十五轮与当前完成审计将该问题接回同任务、承诺和范围判词；不以局部结果替代整体结论。'
            evidence = '第三十五轮报告、INPUT/AUDIT/DELIVERY 收据与 goal.md；仅新同任务承诺、反例或证据失效可重开。'
        else:
            relation = 'NOT_TOUCHED'
            reason = '本阶段不扩展到该独立历史候选；新 goal 禁止以开放问题自动续作。'
            evidence = 'goal.md 第二阶段重开条件；用户明确开启或合格判词改变凭据前保持停止。'
        audit += f'| `{kc}` | {title} | {relation} | {reason} | {evidence} |\n'
    audit += '''
## 扩展认知逐片复认

001–008：本单元承认理论/现实对齐仍是研究方向，但不把启发式当作原四弹已证结论；现实同一性、ASK、来源和完成均在本报告中以同任务/承诺义务审查。没有新候选，避免把“超越 AI”的目标变为同形工作积累。

## 停止裁决

已改变的判词：原四弹 redo 已完成为 `ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED`，而不是继续开放的执行队列。未产生新的合格判词改变凭据。故保存状态并停止第一阶段；第二阶段未开启。
'''
    runs = {
        'schema_version': 'hott-session-runs/v1',
        'session_id': SID,
        'primary_runs': [],
        'new_math_claims': [],
        'new_kernel_replay': False,
        'existing_evidence': [DELIVERY, 'audit/astra-assumption-integration-20260921/INPUT-VERIFICATION.json'],
        'scope': 'Completion-state audit only; no mathematical re-execution.',
    }

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode()
        if rel == runtime.STATE:
            body = runtime.dump(state).decode()
        elif rel == runtime.DIRECTION:
            body = replace_once(body, 'source_state_revision: 209', 'source_state_revision: 210')
            body = replace_once(body, 'projection_generation: 20260921-direction-209', 'projection_generation: 20260921-direction-210')
            body = replace_once(body, 'semantic_status: INTERVAL_I_SEPARATION_FORMS_FAMILY_AND_COFIBRATION_BOOL_OBSERVER_UNWRITABLE', 'semantic_status: FOUR_STAGE_REDO_PHASE_1_COMPLETE_WITH_SCOPE')
        elif rel == runtime.PANORAMA:
            body = replace_once(body, 'source_state_revision: 209', 'source_state_revision: 210')
            body = replace_once(body, 'projection_generation: 20260921-outcome-209', 'projection_generation: 20260921-outcome-210')
            body = replace_once(body, 'semantic_status: INTERVAL_I_SEPARATION_FORMS_FAMILY_AND_COFIBRATION_BOOL_OBSERVER_UNWRITABLE', 'semantic_status: FOUR_STAGE_REDO_PHASE_1_COMPLETE_WITH_SCOPE')
        elif rel == '方向追踪/002 - 治理与用户方向.md':
            lines = body.splitlines()
            for i, line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):
                    lines[i] = '| `DIR-U-ASTRA-BREAKPOINT` | 原四弹 redo：范围判词与局部结果保全 | 用户两阶段 goal；`goal.md` | `CLOSED_WITH_SCOPE / PHASE_1_REDO_COMPLETE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `OUT-ASTRA-ASSUMPTION-INTEGRATION-35`及C250–324 | 原整体击落论证未建立；第二阶段未开启 | `goal.md`；第三十五轮报告；revision210 completion receipt |'
            body = '\n'.join(lines) + '\n'
        elif rel == '全景视野/003 - 当前机器证明包与原生重放.md':
            lines = body.splitlines()
            for i, line in enumerate(lines):
                if line.startswith('| `OUT-ASTRA-ASSUMPTION-INTEGRATION-35` |'):
                    lines[i] = '| `OUT-ASTRA-ASSUMPTION-INTEGRATION-35` | 原四弹 redo 的范围判词 | `DIR-U-ASTRA-BREAKPOINT` | 六原文/五方案、C250–324、9包18资格、14固定Coq源 | `PHASE_1_REDO_COMPLETED_WITH_SCOPE / ORIGINAL_TARGET_NOT_ESTABLISHED` | 原四层、层桥、承诺、恢复与证据范围完成对账；精确局部结果保留 | 不证明全HoTT无问题、物理实现、Coq全库有效或已击落；第二阶段未开启 | `goal.md`；第三十五轮报告；completion receipt |'
            body = '\n'.join(lines) + '\n'
        elif rel == 'MEMORY/001 - 当前执行队列.md':
            start = body.index('用户当前App Goal原文为')
            end = body.index('\n\n', start)
            replacement = '用户当前 `/goal` 是两阶段的四弹一体 redo。第一阶段已经完成：第三十五轮逐层对账、九包十八资格项、固定 Coq 源码合同和 revision209 收据支持范围判词 `ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED / ASSUMPTIONS_AND_TASKS_RECONCILED_WITH_SCOPE`。原整体击落结论未建立，精确局部证明保留。第二阶段未开启；旧机器统观、PREMISE-001、R4、一般反向、独立性、更多消费者与新版包不再自动排队。只在用户明确开启或新事实满足 `goal.md` 的判词改变凭据时重开。当前 checkpoint revision210 将该完成状态写入 STATE；feature-list.md 有另一写者的 dirty 修改，本单元未覆盖。入口：`goal.md`、`Astra继续尝试/断点与证明机制系统检查/第三十五轮执行报告.md`。'
            body = body[:start] + replacement + body[end:]
        elif rel == runtime.PREFIX + 'FRONTIER.md':
            body = '''# HoTT 研究前沿（hot 指针）

## 当前状态（2026-09-21）

- 四弹一体原方案 redo 第一阶段已完成：`ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED / ASSUMPTIONS_AND_TASKS_RECONCILED_WITH_SCOPE`；精确局部结果、原始运行、固定源码和边界保留。
- 第二阶段未开启。旧机器统观、PREMISE-001、R4、文献和其它候选只作历史/潜在研究材料；不得因仍开放自动恢复。
- 唯一重开条件：用户明确开启，或一个已记录的判词改变凭据给出具体同任务承诺、反例、证据失效或未回答的固定六义务。
'''
        elif rel == runtime.PREFIX + 'RESUME.md':
            body = body.replace('## 当前停止点', '## 当前阶段（2026-09-21）\n\n四弹一体原方案 redo 已以第三十五轮范围判词完成第一阶段。`goal.md` 是唯一 current owner；第二阶段未开启。新工作必须先满足判词改变凭据，旧机器统观/PREMISE/R4 不再自动接续。\n\n## 历史停止点', 1)
        files.append({'path': rel, 'expected_sha256': runtime.sha(raw), 'text': body})

    for name, body in (
        ('SESSION.md', session),
        ('RUNS.json', runtime.dump(runs).decode()),
        ('CORE_COGNITION_AUDIT.md', audit),
    ):
        files.append({'path': BASE + name, 'expected_sha256': None, 'text': body})
    payload = {
        'schema_version': 'cognition-checkpoint/v1',
        'session_id': SID,
        'load_profile': 'research',
        'task_ids': ['R-ASTRA-ASSUMPTION-INTEGRATION-20260921'],
        'authorization': '用户当前两阶段 /goal：保存第一阶段范围判词并停止默认扩张；不启动第二阶段。',
        'files': files,
    }
    (OUT / 'checkpoint-payload.json').write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan['snapshot'], payload, apply=args.apply)
    (OUT / ('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != 'paths'}, ensure_ascii=False))


def subprocess_output(argv):
    import subprocess
    return subprocess.check_output(argv, cwd=ROOT, text=True).strip()


if __name__ == '__main__':
    main()
