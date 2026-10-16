#!/usr/bin/env python3
"""Commit the scoped proof-version recovery and the next real consumer check."""
from pathlib import Path
import argparse, importlib.util, json, re, subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = 'S-RES-20260920-ASTRA-REMAINING-CLOSURE'
BASE = '.codex/research/hott/sessions/' + SID + '/'
REPORT = 'Astra继续尝试/断点与证明机制系统检查/第二十轮执行报告.md'
NEXT = 'BP-S1-CONSUMER-01：执行第二十轮003片冻结的SC-00至SC-05六成员。固定Cubical0.9的实际sucPathℤ/ua/Glue→helix/subst→decodeSquare/unglue/hcomp→decodeEncode/J→ΩS¹Isoℤ及winding-hom链；四个单因素消融、基线与独立位置合法恢复，完整保存源码diff、依赖、类型诊断与运行。接受变体先查冗余/换题，不预断缺陷。14旧断点包版本已闭合；全registry另有历史Coq命令/源码关系缺口，后续按实际依赖/整体交付核查。原广义圆环、弱Lift、截断/商实际使用、必要性/元层与整体交付继续OPEN。'
sp = importlib.util.spec_from_file_location('runtime', ROOT / '.codex/tools/cognition_runtime.py')
R = importlib.util.module_from_spec(sp)
sp.loader.exec_module(R)

STANCES = {
    1: ('ALIGNED', '原目标仍是同任务的理论/现实判断；版本检查不替代数学。'),
    2: ('DEEPENED', '下个实际类型族、依赖motive、面条件与消费者已经定位。'),
    3: ('ALIGNED', '没有把多项通过相加为矛盾；算术结果保持原范围。'),
    5: ('ALIGNED', '先固定真实消费者再作归因，不预设消融一定被拒或理论一定有错。'),
    7: ('ALIGNED', '100文件对照和14包检查由实物决定，不以AI自述作证。'),
    10: ('ALIGNED', '现实相对目标保持；下一HIT链只对应模型内绕行信息。'),
    11: ('ALIGNED', '路径参数和checker耗时没有被当作现实过程时间。'),
    12: ('DEEPENED', '下一具体检验局部数据是否为下游类型资格实际所需。'),
    13: ('DEEPENED', '资格变化与换题有单因素diff和恢复，不能把编译诊断当普遍非法。'),
    14: ('ALIGNED', '原交付越级问题仍开放；版本可取不等于取得原现实能力。'),
    15: ('TENSION', '当前版本修复无新理论失配，原强式判断仍须相称证据。'),
    17: ('ALIGNED', '固定上游源码接受实物审查；社区身份不是正确性替代。'),
    19: ('ALIGNED', '没有把非零间隔推广为全部过程无法完成。'),
    21: ('DEEPENED', '97资产进入main，旧源/run与快照完全相同；14包关系和选项复核。'),
    22: ('ALIGNED', '双向目标保持，不用版本工程或正常拒绝冒充完成。'),
    31: ('DEEPENED', '下一使用实际helix/decode/J，不重复无实例接口或布尔标签。'),
    34: ('ALIGNED', '六成员只给固定变体范围；不外推全理论决定性或不可完成性。'),
    35: ('ALIGNED', '广义用户来源/操作语境未被该HIT模型自动覆盖。'),
    37: ('ALIGNED', '真实点集圆/区间证据保留，HIT圆不替换几何删点。'),
    38: ('DEEPENED', '从实际基础库证明链查兼容数据，而非把拒签名称当缺陷。'),
    39: ('DEEPENED', '核对基础构造到实际consumer的资格传递，有具体源码范围。'),
    40: ('ALIGNED', '来源知识被作为待检对象，下一非盲测不冒充独立审稿。'),
    41: ('ALIGNED', '小包版本完成与总目标/同行交付分别验收。'),
    42: ('ALIGNED', '合法恢复和反解释可否定当前候选，不以投入保护假说。'),
    43: ('CORRECTED', '解决反复版本欠账后回真实HIT内部链，停止同形小控制累积。'),
    44: ('ALIGNED', '模型内绕行任务是明确解释，不能自证全部现实保真。'),
    45: ('DEEPENED', '具体检查哪项局部结构被后续消去/运输需要，避免空泛讨论。'),
    46: ('ALIGNED', '已把理解动作落实到源代码与受控合同，下一需实际执行。'),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()
    state = json.loads((ROOT / R.STATE).read_text())
    assert state['revision'] == 193
    head = json.loads((ROOT / '.codex/cognition/HEAD.json').read_text())
    assert all(R.sha((ROOT / p).read_bytes()) == h for p, h in head['tracked'].items())
    evidence = json.loads((OUT / 'RECONCILIATION.json').read_text())
    assert len(evidence['selected']) == 14 and all(f['same_as_snapshot'] for f in evidence['files'])
    selected = json.loads((OUT / 'selected-version.stdout.json').read_text())
    assert selected['status'] == 'SELECTED_PACKAGES_VERSION_CLOSED'
    plan_commit = (OUT / 'PLAN-COMMIT.txt').read_text().strip()
    prior = json.loads((ROOT / 'audit/astra-task-comparison-20260920/RESUME.json').read_text())
    assert R.sha((ROOT / '核心认知.md').read_bytes()) == prior['core_sha256']
    docs = [{'path': d['path'], 'prior_sha256': d['sha256'],
             'sha256': R.sha((ROOT / d['path']).read_bytes())} for d in prior['documents']]
    (OUT / 'RESUME.json').write_bytes(R.dump({
        'policy': 'Same-T3 PROTOCOL v3 receipt reattestation; not new full emission',
        'revision': 193, 'core_sha256': prior['core_sha256'], 'core_unchanged': True,
        'documents': docs, 'known_changes': 'Own checkpoint193; current32 hashes verified',
        'kc_stance_revisited': 'All46 current IDs revisited; source samples KC10–14 and44–46 retained',
        'model_understanding': 'NOT_CERTIFIED_BY_TOOL', 'objective': '完成四弹一体的redo',
        'app_goal_status_observed': 'active'}))
    plan = R.plan(ROOT, profile='research', task_ids=['R-ASTRA-TASK-COMPARISON-20260920'])
    assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted']
    (OUT / 'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
    old = state['latest_session']
    state['revision'] = 194
    state['latest_session'] = SID
    state['records'][SID] = {
        'kind': 'session', 'path': BASE + 'SESSION.md', 'lifecycle_status': 'HISTORICAL',
        'evidence_status': 'FOURTEEN_BREAKPOINT_PACKAGES_VERSION_CLOSED',
        'status': 'complete_with_scope', 'depends_on': [],
        'related_records': [old, 'A-ASTRA-CONTINUING-GOAL-20260919'],
        'full_sources': [BASE + x for x in ['SESSION.md', 'RUNS.json', 'CORE_COGNITION_AUDIT.md']]}
    state['records']['R-ASTRA-REMAINING-CLOSURE-20260920'] = {
        'kind': 'result', 'path': REPORT, 'lifecycle_status': 'CURRENT',
        'evidence_status': 'SCOPED_VERSION_CLOSED / SUCCESSOR_FROZEN_NOT_RUN',
        'status': 'fourteen_old_packages_integrated_parent_open', 'depends_on': [],
        'related_records': [SID, 'R-ASTRA-TASK-COMPARISON-20260920'],
        'full_sources': [REPORT, 'audit/astra-remaining-20260920/RECONCILIATION.json',
                         'audit/astra-remaining-20260920/SOURCE-INPUTS.json'],
        'scope': '14 existing packages C250–264, 100 exact snapshot files, 97 assets integrated into main. No mathematical source or original run changed; no new theorem. S1 real consumer six-member successor frozen, not executed. Global Coq command/source relationship remains unresolved.',
        'source_hashes': {r['path']: r['sha256'] for r in evidence['files']
                          if r['path'].endswith(('.agda', 'TOOLCHAIN.json'))}}
    state['execution_control'].update(
        status='ACTIVE_GOAL_BREAKPOINT_VERSIONS_CLOSED_S1_CONSUMER_NEXT',
        last_checkpoint_session=SID,
        checkpoint_result='.codex/cognition/checkpoints/' + SID + '/result.json',
        next_minimal_verification=NEXT)
    session = f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 canonical mutation / scoped evidence audit
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-remaining-20260920/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；C302/C303、revision193与12654ad实际完成
- status: BREAKPOINT_VERSIONS_RECOVERED / PARENT_OPEN

14包对应C250–264，100文件与d059恢复快照完全相同；97缺失资产在f8e0fc81aef8a89c0ccf3dae1cf95db17c0c5cee进入main。14次formal收据/选项检查、关系与提交后版本检查通过；未重跑内核、未新增数学claim、未改原run。全registry后续失败为历史Coq命令/源码关系，不伪修旧收据。

按14模板与U00–09核实范围，冻结实际圆HIT整数覆盖的ua/Glue、局部decode和依赖J消费链，SC00–05尚未运行。四原件/范围在SOURCE-INPUTS。策略v1.22由{plan_commit}保存；当前下一动作：{NEXT}

PROTOCOL§5允许的46KC legacy原子bundle沿用，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001不隐去；报告四分片。T01–05父需求未变，T06–10后继合同与来源，T11–17已有证明资格及恢复性，T18–21无部署，T22–24历史/main边界与当前范围，T25无AI合同变更，T26精确本地提交。共享C01–C09 NO_CHANGE，C10项目证据更新。无Sub Agent、push/tag/发布。

element_usage：closure/收据复认、research范围分层、SOP真实后继、verification14包、Git精确恢复、canonical事务、dev-notes。无新通用框架。
'''
    audit = f'''# {SID} 核心认知回评

core-cognition-generation-7；46条。

- core_change: NO
- direction_change: S1_CONSUMER_CHAIN_NEXT
- panorama_change: ADD_SCOPED_VERSION_RECOVERY
- essay_change: NO
- update_decision: 旧14包版本缺口已修，回实际自然消费者
- cross_conflicts: 版本通过不是数学新证明；原理论成功目标仍须同任务证据
- unresolved: 全registry Coq关系、原广义圆环/弱Lift、其它消费者、元层/整体

| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一选择与反证条件 |
|---|---|---|---|---|
'''
    headings = re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$', (ROOT / '核心认知.md').read_text(), re.M)
    assert len(headings) == 46
    for n, (kc, title) in enumerate(headings, 1):
        relation, reason = STANCES.get(n, ('NOT_TOUCHED', '该具名时间/自指/反射问题未推进，不从版本修复宣称闭合。'))
        boundary = ('第二十轮001–004及原源/run；后继SC00–05。若源/run不一致、当前状态被旧快照覆盖、候选换题或没有实际消费者则撤回；真正同任务失配可重评。'
                    if n in STANCES else '第二十轮002未触达；该具名机制实际成为当前依赖或新原文要求时重开。')
        audit += f'| `{kc}` | {title} | {relation} | {reason} | {boundary} |\n'
    audit += '''
## 扩展认知逐片复认

001问题/简化：版本修复不等于理论结果；002前提/时间：HIT参数不作物理运行；003圆环/ASK：实际局部资格与后续响应分层；004HoTT/自反：不自动启动无依赖Gödel问题；005表达/原文：原广义操作保留，不把HIT删点当点集删除；006知识谱：实际上游作为被检证据；007助力/阻力：97资产确切修复后离开反复准备；008现实骨架：模型内绕行恢复有明示解释，未自证物理对应。

## 已走过的路

原PointRestoration阻塞已按100文件实证消除，14包版本通过，原历史真值未回滚；全registry其它问题保留。旧正常拒签没有由Git变成理论缺陷。

## 即将作出的选择与完备性

SC00–05选择的是实际整数覆盖中非平凡类型族/Glue/依赖J链；旧holdout仅看winding输出。先基线再单因素，再独立恢复，所有意外保留。未选更多Bool改名或无依赖元层，未把全部库审计许诺为此六项完成。14模板/U00–09双分类与八轴、遗漏、停止见报告002/003。父Goal仍OPEN。
'''
    runs = {'schema_version': 'hott-session-runs/v1', 'session_id': SID,
            'primary_runs': [p['run'] for p in evidence['selected']], 'new_math_claims': [],
            'validation': 'audit/astra-remaining-20260920/RECONCILIATION.json',
            'extra_kernel_rerun': False, 'successor': 'FROZEN_NOT_RUN', 'parent_objective': 'OPEN'}
    for rec, kind in [('I-DIRECTION-PORTFOLIO-20260912', 'direction'), ('I-OUTCOME-PANORAMA-20260912', 'outcome')]:
        state['records'][rec]['projection_generation'] = '20260920-' + kind + '-194'
    targets = list(R.MUTABLE) + list(R.mutable_shard_paths(ROOT))
    baseline = subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh', *targets], cwd=ROOT, capture_output=True, check=True)
    (OUT / 'current-owner-baseline.txt').write_bytes(baseline.stdout)
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = R.dump(state).decode() if rel == R.STATE else raw.decode()
        if rel in (R.DIRECTION, R.PANORAMA):
            body, n = re.subn(r'(?m)^source_state_revision: 193$', 'source_state_revision: 194', body)
            assert n == 1
            kind = 'direction' if rel == R.DIRECTION else 'outcome'
            body, n = re.subn(r'(?m)^projection_generation: .+$', 'projection_generation: 20260920-' + kind + '-194', body)
            assert n == 1
        if rel == 'MEMORY/001 - 当前执行队列.md':
            start = body.index('用户当前App Goal')
            end = body.index('\n\n', start)
            body = body[:start] + '用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。C250–264的14旧断点包经100文件快照核对，97资产精确集成main，14包版本检查通过；原PointRestoration缺口已修。无新数学claim或额外核重放。全registry另有历史Coq命令/源码关系缺口；不改旧收据。按14模板/U00–09核剩余后，策略v1.22由' + plan_commit + '保存。下一动作' + NEXT + ' 入口：`' + REPORT + '`。' + body[end:]
        if rel == '方向追踪/002 - 治理与用户方向.md':
            lines = body.splitlines()
            for i, line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):
                    lines[i] = line.replace('ARITHMETIC_REQUESTS_CHECKED_REMAINING_CLOSURE_NEXT', 'BREAKPOINT_VERSIONS_CLOSED_S1_CONSUMER_NEXT').replace('`OUT-ASTRA-TASK-COMPARISON-19` |', '`OUT-ASTRA-TASK-COMPARISON-19`、`OUT-ASTRA-REMAINING-CLOSURE-20` |').replace('九族算术合同已核；下一剩余覆盖/相关版本，再实际库消费者；原广义范围开放', '14旧包版本已修；下一实际S1依赖消费链六成员；原广义及其它机制开放')
            body = '\n'.join(lines) + '\n'
        if rel == '全景视野/003 - 当前机器证明包与原生重放.md':
            body = body.rstrip() + '\n| `OUT-ASTRA-REMAINING-CLOSURE-20` | 14旧断点包版本恢复与剩余范围核对 | `DIR-U-ASTRA-BREAKPOINT` | 100文件同快照、97资产main集成、选项/关系/版本检查 | `SCOPED_VERSION_CLOSED / SUCCESSOR_NOT_RUN` | C250–264原字节及历史run保持；下一S1实际六成员已冻结 | 全registry Coq关系、其它机制/原广义任务/整体 | `' + REPORT + '`；`audit/astra-remaining-20260920/RECONCILIATION.json` |\n'
        files.append({'path': rel, 'expected_sha256': R.sha(raw), 'text': body})
    for name, body in [('SESSION.md', session), ('RUNS.json', R.dump(runs).decode()), ('CORE_COGNITION_AUDIT.md', audit)]:
        files.append({'path': BASE + name, 'expected_sha256': None, 'text': body})
    payload = {'schema_version': 'cognition-checkpoint/v1', 'session_id': SID,
               'load_profile': 'research', 'task_ids': ['R-ASTRA-TASK-COMPARISON-20260920'],
               'authorization': '用户持续Goal及既有T3集成授权；已修当前链版本，保持父范围并转真实源消费者。',
               'files': files}
    (OUT / 'checkpoint-payload.json').write_bytes(R.dump(payload))
    result = R.checkpoint(ROOT, plan['snapshot'], payload, apply=args.apply)
    (OUT / ('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result))
    print(json.dumps({k: v for k, v in result.items() if k != 'paths'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
