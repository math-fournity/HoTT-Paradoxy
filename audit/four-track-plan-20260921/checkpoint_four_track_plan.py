#!/usr/bin/env python3
"""Checkpoint the user-directed four-track HoTT research plan."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = 'S-PLAN-20260921-ASTRA-FOUR-TRACK'
BASE = '.codex/research/hott/sessions/' + SID + '/'
ABX_ID = 'R-ABX-ACTION-20260921'
PLAN_ID = 'R-HOTT-FOUR-TRACK-PLAN-20260921'
DIALOGUE = 'audit/four-track-plan-20260921/build_four_track_dialogue.py'
VERIFY = 'audit/four-track-plan-20260921/verify_four_track_plan.py'
RECEIPT = 'audit/four-track-plan-20260921/FOUR-TRACK-PLAN-VERIFICATION.json'
PLAN_INDEX = 'HoTT后续研究总体方案.md'
PLAN_SHARDS = tuple(
    'HoTT后续研究总体方案/' + name
    for name in (
        '001 - 上一轮问答与四分支校正.md',
        '002 - 共同任务、术语与优先级原则.md',
        '003 - 分支顺序、准入与停止条件.md',
        '004 - 令牌经济、反漂移与每单元复核.md',
        '005 - 当前第一步与交接.md',
    )
)
PLAN_SOURCES = (
    PLAN_INDEX, *PLAN_SHARDS, DIALOGUE, VERIFY, RECEIPT,
    'goal.md', 'feature-list.md', 'rulings.md',
    'ABX行动.md',
    'ABX行动/005 - 状态、停止条件与未来交接.md',
    'audit/abx-action-20260921/H-R-K查找思路整备/005 - 未覆盖义务、禁止重复与重新出发条件.md',
)
ABX_REFRESH = (
    'goal.md', 'feature-list.md',
    'ABX行动.md',
    'ABX行动/005 - 状态、停止条件与未来交接.md',
    'audit/abx-action-20260921/H-R-K查找思路整备/005 - 未覆盖义务、禁止重复与重新出发条件.md',
    PLAN_INDEX, RECEIPT,
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(body: str, old: str, new: str) -> str:
    result, count = re.subn(re.escape(old), new, body, count=1)
    assert count == 1, old
    return result


def replace_line(body: str, prefix: str, replacement: str) -> str:
    lines = body.splitlines()
    hits = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    lines[hits[0]] = replacement
    return '\n'.join(lines) + '\n'


def core_audit(core: dict) -> str:
    headings = re.findall(r'^### (KC-\d+) · .*? · (.+)$', (ROOT / '核心认知.md').read_text(), re.M)
    assert len(headings) == core['kc_count'] == 46
    touched = {1, 2, 3, 5, 10, 14, 15, 19, 21, 22, 31, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46}
    corrected = {15, 38, 39, 40}
    body = f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: FOUR_TRACK_PORTFOLIO_AND_BRANCH_ORDER_REGISTERED
- panorama_change: FOUR_TRACK_PLAN_AND_P1_NEXT_REGISTERED
- essay_change: NO
- update_decision: 当前第二阶段不再把 ABX 当作全部未来工作；先做 P1-RMIN-SPEC-001，P2/P3/P4 按已固定依赖和触发推进
- cross_conflicts: 结构理论、规则级桥、实际消费者和实现忠实性是四种不同问题；不能以任一分支的无命中、控制或拒绝替代另一分支的结论
- unresolved: R_min 是否可由独立任务理由固定、K_theory 是否存在、外部 K_app 是否存在、以及是否出现 K_engine 的真实触发

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
'''
    for number, (kc, title) in enumerate(headings, 1):
        if number in corrected:
            relation = 'CORRECTED'
            judgement = '将后续研究从单一 ABX 或引擎扫描的误读校正为四个相互约束的分支，不将任一局部结果升级为 HoTT 缺陷。'
            evidence = f'{PLAN_INDEX}；{RECEIPT}；新理论桥、实际消费者或实现差异才改变该范围。'
        elif number in touched:
            relation = 'DEEPENED'
            judgement = '四分支计划以现实同任务、理论归因、机器证据和防漂移为共同条件；P1 先固定规格，后续分支不得越级。'
            evidence = f'{PLAN_INDEX}；{RECEIPT}；P1 的三种明确结束决定后续。'
        else:
            relation = 'NOT_TOUCHED'
            judgement = '本单元只规划 HoTT 后续研究的分支和证据顺序，不重新裁决该条独立用户原文。'
            evidence = 'goal.md §1；无新数学主张。'
        body += f'| `{kc}` | {title} | {relation} | {judgement} | {evidence} |\n'
    body += '''
## 扩展认知逐片复认

001–008：本计划把现实对齐从单一熟悉通道中解开：先定义最小可检验的结构，再分别问理论规则、实际使用和实现是否出现强任务桥。计划本身不证明某条桥存在。

## 停止裁决

P0 已完成。下一次只有 `P1-RMIN-SPEC-001` 有资格启动；它结束后按 P1 判词选择 P2 或停止。不得把四条支线并行扩张成无边界工作。
'''
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    subprocess.check_call([sys.executable, '-B', DIALOGUE, '--check'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', VERIFY, '--write'], cwd=ROOT)
    for rel in PLAN_SOURCES:
        assert (ROOT / rel).is_file(), rel

    spec = importlib.util.spec_from_file_location('runtime', ROOT / '.codex/tools/cognition_runtime.py')
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text())
    assert state['revision'] == 218
    assert state['latest_session'] == 'S-ABX-20260921-ASTRA-HRK-READINESS'
    head = json.loads((ROOT / runtime.HEAD).read_text())
    assert all(sha(ROOT / rel) == digest for rel, digest in head['tracked'].items())
    plan = runtime.plan(ROOT, profile='research', task_ids=[ABX_ID])
    assert set(plan['review_required']) <= {ABX_ID}
    assert not plan['hydration_diagnostics']['query_first_promoted']
    (OUT / 'FOUR-TRACK-CHECKPOINT-PLAN.json').write_bytes(runtime.dump(plan))
    receipt = json.loads((ROOT / RECEIPT).read_text())
    assert receipt['status'] == 'PASS_WITH_SCOPE'

    prior_latest = state['latest_session']
    state['revision'] = 219
    state['latest_session'] = SID
    abx = state['records'][ABX_ID]
    abx['full_sources'] = list(dict.fromkeys(abx['full_sources'] + [PLAN_INDEX, RECEIPT]))
    abx['related_records'] = list(dict.fromkeys(abx['related_records'] + [PLAN_ID, SID]))
    abx['source_hashes'].update({rel: sha(ROOT / rel) for rel in ABX_REFRESH})
    abx['revalidation'] = (
        'Revision219 records the user-directed four-track portfolio. ABX is P3, after P1 R_min qualification and '
        'one new P2 theory denominator; its existing bounded no-hit evidence remains valid and is not reinterpreted as a defect verdict.'
    )
    abx['scope'] = (
        'ABX remains the actual-consumer branch: it may receive a new K_app denominator only after the common R_min '
        'contract and one P2 K_theory denominator are closed. Existing D1/D2/D3 remain no-repeat controls.'
    )
    state['records'][PLAN_ID] = {
        'kind': 'research_plan', 'path': PLAN_INDEX, 'lifecycle_status': 'ACTIVE_WORK',
        'evidence_status': 'USER_DIRECTED_PORTFOLIO_PLAN / P0_COMPLETE / NO_NEW_MATHEMATICAL_CLAIM',
        'status': 'p0_complete_p1_rmin_spec_next', 'depends_on': [],
        'related_records': [ABX_ID, prior_latest], 'full_sources': list(PLAN_SOURCES),
        'source_hashes': {rel: sha(ROOT / rel) for rel in PLAN_SOURCES},
        'scope': ('Four-track phase-two plan: P1 R_min qualification, P2 K_theory, P3 K_app/ABX, and triggered P4 '
                  'K_engine. This plan fixes order and stopping conditions; it asserts no mathematical result.'),
    }
    state['records'][SID] = {
        'kind': 'session', 'path': BASE + 'SESSION.md', 'lifecycle_status': 'HISTORICAL',
        'evidence_status': 'FOUR_TRACK_PLAN_CHECKPOINTED_WITH_SCOPE', 'status': 'complete_with_scope',
        'depends_on': [], 'related_records': [PLAN_ID, ABX_ID, prior_latest],
        'full_sources': [BASE + name for name in ('SESSION.md', 'RUNS.json', 'CORE_COGNITION_AUDIT.md')],
    }
    state['execution_control'].update(
        portfolio_record=PLAN_ID,
        status='FOUR_TRACK_PLAN_ADOPTED_NEXT_P1_RMIN_SPEC',
        current_phase='PHASE_2_FOUR_TRACK_P1_READY',
        second_phase_status='P0_COMPLETE_P1_RMIN_SPEC_NEXT',
        last_checkpoint_session=SID,
        checkpoint_result='.codex/cognition/checkpoints/' + SID + '/result.json',
        next_minimal_verification=(
            'P1-RMIN-SPEC-001 only: qualify whether RichCurve already supplies the independently justified minimal '
            'R_min contract. Do not rerun C250-C324/Flash/D1-D3/Book or scan an external K before its outcome.'
        ),
    )
    state['projection']['status'] = 'FOUR_TRACK_PLAN_ADOPTED_P1_RMIN_NEXT / ABX_IS_P3 / NO_NEW_HOTT_DEFECT_CLAIM'

    session = f'''# {SID}

- host: Codex desktop local
- model: GPT-5-based Codex；不认证服务端路由
- tier: T3 plan/state mutation for the user-directed four-track portfolio
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: preserve the prior four-branch explanation and set a single ordered, evidence-bounded future plan
- status: COMPLETED_WITH_SCOPE / P1_RMIN_SPEC_NEXT

This session changes planning and routing only. It places R_min qualification before rule-level K_theory, actual-consumer ABX/K_app, and triggered engine fidelity K_engine. It preserves the completed four-stage redo and all existing ABX bounded-negative results. No mathematical theorem, external scan, kernel replay, engine finding, or HoTT defect claim occurred.
'''
    runs = {
        'schema_version': 'hott-session-runs/v1', 'session_id': SID,
        'primary_runs': [{
            'kind': 'four-track-plan-projection-and-routing-verification',
            'command': f'python3 -B {DIALOGUE} --check && python3 -B {VERIFY} --write',
            'result': 'PASS_WITH_SCOPE; verbatim previous answer, plan structure and routing anchors match',
            'mathematics': 'NOT_A_KERNEL_RUN',
        }],
        'new_math_claims': [], 'new_kernel_replay': False,
        'scope': 'Planning/routing only; no mathematical or HoTT-defect theorem.',
    }

    new_direction = (
        '| `DIR-U-HOTT-FOUR-TRACK` | 第二阶段四分支：R_min、K_theory、K_app、K_engine | 用户 2026-09-21要求整体规划、令牌经济与防漂移 | `USER_DIRECTED_PLAN / P0_COMPLETE / P1_NEXT` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-HOTT-FOUR-TRACK-PLAN-20260921`；H/R/K整备与goal | 单一活动分支；P1先行，P2/P3/P4按准入 | `HoTT后续研究总体方案.md`；revision219 receipt |\n'
        '| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P3 实际消费者 `K_app` 分支 | 原圆环 A/B/X H/R/K 整备 | `P3_PENDING_P1_AND_P2 / NO_DEFECT_VERDICT` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；C250–324、D1/D2/D3 | P1/P2前不扩展K扫描；既有no-hit不重做 | `ABX行动.md`；总体方案；revision219 receipt |'
    )
    new_panorama = (
        '| `OUT-HOTT-FOUR-TRACK-PLAN` | 第二阶段四分支总体计划及令牌经济约束 | `DIR-U-HOTT-FOUR-TRACK` | 上一轮完整问答、H/R/K整备、goal、ABX | `PLAN_ADOPTED_P1_RMIN_NEXT` | 先共用规格，后理论桥、实际消费者、触发式引擎审计 | 不证明R_min、K或HoTT缺陷；不启动四支并行 | `HoTT后续研究总体方案.md`；revision219 receipt |\n'
        '| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环实际消费者分支 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C250–324、68份run、Flash、D1/D2/D3、Book/社区来源 | `P3_PENDING_P1_P2 / NO_ACTUAL_K` | H/R/U与操作合同已有控制；有界K分母无命中 | 不证明新拓扑、外部全库无K或HoTT缺陷 | `ABX行动.md`；总体方案；revision219 receipt |'
    )
    new_memory = (
        '第二阶段已采用四分支总体计划：P1 `R_min` 最小规格资格化先行；P2 检查规则/定理级 `K_theory`；'
        'P3 由 ABX 检查版本固定的实际 `K_app`；P4 仅有实现差异触发。ABX不再是全部未来工作。当前下一单元仅为 '
        '`P1-RMIN-SPEC-001`：检查既有 RichCurve 是否已足够，不重做C250–324、Flash、D1/D2/D3或Book。'
        '入口：`HoTT后续研究总体方案.md`；revision219 checkpoint。'
    )
    new_frontier = '- 第二阶段四分支计划已采用：P1 R_min 规格资格化是唯一下一单元；P2理论桥、P3 ABX消费者和P4引擎审计均须满足各自准入，入口：`HoTT后续研究总体方案.md`。'
    new_resume = '第二阶段不再仅是ABX：总体计划固定 P1 R_min → P2 K_theory → P3 ABX/K_app，P4 K_engine 只由实际差异触发。当前只做P1规格资格化，禁止重跑已有H/R/K控制或先扫外部消费者。入口：`HoTT后续研究总体方案.md`；revision219 checkpoint。'
    memory_log = '\nS-PLAN-20260921-ASTRA-FOUR-TRACK：用户要求将上一轮四分支回答完整落盘并以令牌经济、防漂移和单一活动分支重规划第二阶段。P0完成；当前唯一下一单元=P1-RMIN-SPEC-001。P2=K_theory，P3=ABX/K_app，P4=触发式K_engine；均未启动数学研究。验证器PASS_WITH_SCOPE；revision219 checkpoint。\n'

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode()
        if rel == runtime.STATE:
            body = runtime.dump(state).decode()
        elif rel == runtime.DIRECTION:
            body = replace_once(body, 'source_state_revision: 218', 'source_state_revision: 219')
            body = replace_once(body, 'projection_generation: 20260921-direction-218', 'projection_generation: 20260921-direction-219')
            body = replace_once(body, 'semantic_status: ABX_HRK_READINESS_REGISTERED_WITH_SCOPE', 'semantic_status: FOUR_TRACK_PLAN_ADOPTED_P1_RMIN_NEXT')
        elif rel == runtime.PANORAMA:
            body = replace_once(body, 'source_state_revision: 218', 'source_state_revision: 219')
            body = replace_once(body, 'projection_generation: 20260921-outcome-218', 'projection_generation: 20260921-outcome-219')
            body = replace_once(body, 'semantic_status: ABX_HRK_READINESS_REGISTERED_WITH_SCOPE', 'semantic_status: FOUR_TRACK_PLAN_ADOPTED_P1_RMIN_NEXT')
        elif rel == '方向追踪/002 - 治理与用户方向.md':
            body = replace_line(body, '| `DIR-U-ABX-ORIGINAL-CIRCLE` |', new_direction)
        elif rel == '全景视野/003 - 当前机器证明包与原生重放.md':
            body = replace_line(body, '| `OUT-ABX-ACTION-INTAKE` |', new_panorama)
        elif rel == 'MEMORY/001 - 当前执行队列.md':
            body = replace_line(body, 'ABX 的 H/R/K 历史整备完成：', new_memory)
        elif rel == 'MEMORY/003 - 当前验证状态与顺序日志.md':
            body += memory_log
        elif rel == runtime.PREFIX + 'FRONTIER.md':
            body = replace_once(body, '- ABX H/R/K 历史整备已完成：前四轴已有有界控制和禁止重复清单，但没有实际 K；下一步只能基于新版本固定消费者、更强 R/operation-spec、独立对象理论目标或直接证据失效。入口：`audit/abx-action-20260921/H-R-K查找思路整备.md`。', new_frontier)
        elif rel == runtime.PREFIX + 'RESUME.md':
            body = replace_once(body, 'ABX H/R/K 历史整备已完成：完整本轮问答、308 个断点专题追踪文件、C250–324 的 68 份关联 run、Flash、Lean/原生 Agda控制、第一阶段 redo 和 D1/D2/D3 均已建立索引。H 是裸空间关系；R 仍只是受限来源—操作—复原代理；U 是忘却；现有 SourceContract/TaskIntegration 显式保住字段和操作差异。未找到实际版本固定 K 将 H/U 升格为同一 Done_strong 任务。默认停止：未来先读 `audit/abx-action-20260921/H-R-K查找思路整备.md`；仅外部K、更强R/操作合同、独立对象理论目标或直接证据失效可重开。', new_resume)
        files.append({'path': rel, 'expected_sha256': runtime.sha(raw), 'text': body})

    for name, body in (
        ('SESSION.md', session),
        ('RUNS.json', runtime.dump(runs).decode()),
        ('CORE_COGNITION_AUDIT.md', core_audit(state['current_core'])),
    ):
        files.append({'path': BASE + name, 'expected_sha256': None, 'text': body})

    payload = {
        'schema_version': 'cognition-checkpoint/v1', 'session_id': SID,
        'load_profile': 'research', 'task_ids': [ABX_ID],
        'authorization': '用户2026-09-21要求把四分支回答完整落盘、把ABX降为其中一支，并以令牌经济和防漂移原则制定整体后续行动方案；当前唯一工作AI获授权更新goal、Feature、rulings、ABX路由、状态投影、STATE和canonical checkpoint。',
        'files': files,
    }
    (OUT / 'FOUR-TRACK-checkpoint-payload.json').write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan['snapshot'], payload, apply=args.apply)
    suffix = 'FOUR-TRACK-checkpoint-apply.json' if args.apply else 'FOUR-TRACK-checkpoint-dry-run.json'
    (OUT / suffix).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != 'paths'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
