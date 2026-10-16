from __future__ import annotations

import json
import os
import re
import shutil
import hashlib
import zipfile
from collections import defaultdict, deque
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

BASE = Path('/mnt/data')
DATE = '2026-08-31'
STAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
BACKUP = BASE / '_research_backup_20260831_before_hierarchical_wbs_v2'
BACKUP.mkdir(parents=True, exist_ok=True)

FILES_TO_BACKUP = [
    'AGENTS.md', 'CURRENT_RESEARCH_INDEX.md', 'RESEARCH_LOG.md',
    'HOTT_Z_SOURCE_REGISTRY.json',
    'HOTT_Z_后续工作总方案与工作包分解_v1.md',
    'HOTT_Z_后续工作总体方案与工作包分解_第四轮.md',
    'HOTT_Z_后续工作总方案与WBS_v1.md',
    'HOTT_Z_WORK_PACKAGE_REGISTER.json',
    'HOTT_Z_WORK_BREAKDOWN_STRUCTURE.json',
    'HOTT_Z_WBS_REGISTRY_v1.json',
    'HOTT_Z_执行看板.md',
    'HOTT_Z_阶段闸门与验收矩阵.md',
    'HOTT_Z_风险与红队登记表.md',
    'HOTT_Z_WORKPLAN_CANONICAL_POINTER.md',
    'HOTT_Z_工作包—来源—主张追踪矩阵_v1_1.md',
    'HOTT_Z_后续工作执行摘要_规范版.md',
]
for name in FILES_TO_BACKUP:
    src = BASE / name
    if src.exists():
        shutil.copy2(src, BACKUP / name)


def load_json_path(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding='utf-8'))

def load_json(name: str, fallback: str | None = None) -> dict[str, Any]:
    p = BASE / name
    if not p.exists() and fallback is not None:
        p = BASE / fallback
    return load_json_path(p)

wp_register = load_json(
    'HOTT_Z_WORK_PACKAGE_REGISTER.json',
    'archive/superseded_workplans_20260831/26_wp_plan_superseded/HOTT_Z_WORK_PACKAGE_REGISTER.json'
)
macro_register = load_json(
    'HOTT_Z_WORK_BREAKDOWN_STRUCTURE.json',
    'archive/superseded_workplans_20260831/14_wp_round4_plan_superseded/HOTT_Z_WORK_BREAKDOWN_STRUCTURE.json'
)
micro_register = load_json('HOTT_Z_WBS_REGISTRY_v1.json')
source_registry = load_json('HOTT_Z_SOURCE_REGISTRY.json')

# ---------------------------------------------------------------------------
# Canonical hierarchy
# ---------------------------------------------------------------------------
areas = [
    {'id': 'AREA-00', 'title': '治理、来源与单一事实源', 'objective': '固定源材料、活动台账、版本、编号和变更控制，使所有结论可追溯且不重复计证。'},
    {'id': 'AREA-01', 'title': '理论剖面与不完备性口径', 'objective': '逐定理固定 HoTT 变体、对象/元理论、宇宙、相等概念、目标语义与允许结论。'},
    {'id': 'AREA-02', 'title': 'Z 铁律数学核心', 'objective': '建立因子分解障碍、真值损失谱、表示精化和最小充分真值商。'},
    {'id': 'AREA-03', 'title': '单价时间定向与群胚方向障碍', 'objective': '证明裸单价对象和可逆 core 不能自然、免费、无损恢复一般时间方向。'},
    {'id': 'AREA-04', 'title': '时间轨道、极限与操作完成', 'objective': '区分固定点、轨道、极限、闭包、可达性、有限时间完成与 guarded 富化。'},
    {'id': 'AREA-05', 'title': '历史、语义角色与语境', 'objective': '研究 provenance、originality、intended role 与上下文规约在遗忘后的不可定义性。'},
    {'id': 'AREA-06', 'title': '资源制度与操作成本', 'objective': '以外延语义非因子化和 Cartesian–linear/quantitative 结构差异替代旧 transport 攻击。'},
    {'id': 'AREA-07', 'title': '断言、截断与具体见证', 'objective': '区分布尔标签、mere existence 与具体 path/equivalence witness，并研究无统一抽取。'},
    {'id': 'AREA-08', 'title': '有效求解与未来判定', 'objective': '在固定有效演算中研究稳定性、inhabitation、合成与 canonicalization 的不可总化边界。'},
    {'id': 'AREA-09', 'title': '反射、宇宙与对角化', 'objective': '在真实语法编码、评价与可证明性对象基础上独立研究 Lawvere/Gödel/宇宙开放性。'},
    {'id': 'AREA-10', 'title': '证明助理与可复现形式化', 'objective': '锁定工具链、完成核心定理机器检查、交叉验证和持续集成。'},
    {'id': 'AREA-11', 'title': '文献、原创性与红队', 'objective': '逐定理查清既有工作、最强反驳、变体边界和贡献等级。'},
    {'id': 'AREA-12', 'title': '论文组合与哲学分流', 'objective': '形成窄数学论文 A–D 与哲学伴随稿，防止支线污染主证明。'},
    {'id': 'AREA-13', 'title': '独立复核、复现与发布', 'objective': '完成独立核验、干净环境重建、清单、匿名包和公开包。'},
]

wp_area = {
    'WP-00': 'AREA-00', 'WP-02': 'AREA-00',
    'WP-01': 'AREA-01',
    'WP-10': 'AREA-02', 'WP-11': 'AREA-02',
    'WP-12': 'AREA-03', 'WP-13': 'AREA-03',
    'WP-14': 'AREA-04',
    'WP-15': 'AREA-05', 'WP-18': 'AREA-05',
    'WP-16': 'AREA-06',
    'WP-17': 'AREA-07',
    'WP-19': 'AREA-08',
    'WP-20': 'AREA-09',
    'WP-30': 'AREA-10', 'WP-31': 'AREA-10', 'WP-32': 'AREA-10', 'WP-33': 'AREA-10',
    'WP-03': 'AREA-11', 'WP-40': 'AREA-11',
    'WP-41': 'AREA-12', 'WP-42': 'AREA-12', 'WP-43': 'AREA-12', 'WP-44': 'AREA-12', 'WP-45': 'AREA-12',
    'WP-46': 'AREA-13',
}

# Map the 45 fine-grained legacy WPs to canonical work packages.
legacy_tm_parent = {
    'WP-000': 'WP-01', 'WP-010': 'WP-02', 'WP-020': 'WP-00', 'WP-030': 'WP-40',
    'WP-100': 'WP-01', 'WP-110': 'WP-10', 'WP-120': 'WP-11', 'WP-130': 'WP-11',
    'WP-140': 'WP-10', 'WP-150': 'WP-11',
    'WP-200': 'WP-12', 'WP-210': 'WP-12', 'WP-220': 'WP-12',
    'WP-230': 'WP-13', 'WP-240': 'WP-13', 'WP-250': 'WP-41',
    'WP-300': 'WP-15', 'WP-310': 'WP-15', 'WP-320': 'WP-18', 'WP-330': 'WP-17', 'WP-340': 'WP-15',
    'WP-400': 'WP-16', 'WP-410': 'WP-16', 'WP-420': 'WP-19', 'WP-430': 'WP-19',
    'WP-440': 'WP-14', 'WP-450': 'WP-14', 'WP-460': 'WP-14',
    'WP-500': 'WP-20', 'WP-510': 'WP-20',
    'WP-600': 'WP-30', 'WP-610': 'WP-31', 'WP-620': 'WP-31', 'WP-630': 'WP-32',
    'WP-640': 'WP-31', 'WP-650': 'WP-30',
    'WP-700': 'WP-03', 'WP-710': 'WP-03', 'WP-720': 'WP-40', 'WP-730': 'WP-46',
    'WP-800': 'WP-41', 'WP-810': 'WP-42', 'WP-820': 'WP-44', 'WP-830': 'WP-45', 'WP-840': 'WP-46',
}
legacy_tm_supports = {
    'WP-240': ['WP-14', 'WP-40'],
    'WP-250': ['WP-10', 'WP-12', 'WP-13', 'WP-15'],
    'WP-330': ['WP-32'],
    'WP-420': ['WP-43'],
    'WP-430': ['WP-43'],
    'WP-440': ['WP-32'],
    'WP-450': ['WP-45'],
    'WP-460': ['WP-43', 'WP-45'],
    'WP-630': ['WP-31', 'WP-33'],
    'WP-640': ['WP-40'],
    'WP-650': ['WP-46'],
    'WP-700': ['WP-41', 'WP-42', 'WP-43', 'WP-44'],
    'WP-710': ['WP-41', 'WP-42', 'WP-43', 'WP-44'],
    'WP-720': ['WP-41', 'WP-42', 'WP-43', 'WP-44'],
    'WP-730': ['WP-41'],
    'WP-840': ['WP-41'],
}

# Mechanisms used across the program.
mechanisms = [
    {'id': 'M1', 'name': '非因子化／不可定义', 'criterion': '同一抽象纤维中存在目标真值差异，故目标不能经遗忘映射下降。'},
    {'id': 'M2', 'name': '无截面／无自然选择', 'criterion': '自同构或 monodromy 对候选富化无固定点，故不存在自然全局选择。'},
    {'id': 'M3', 'name': '不可总判定／不可总合成', 'criterion': '假定总算法可归约出 halting、inhabitation 或程序语义等已知不可判定问题。'},
    {'id': 'M4', 'name': '反射与元理论开放性', 'criterion': '对象理论无法无条件内部化其全部真理、可证明性或一致性；必须明确语法和元理论。'},
    {'id': 'GOV', 'name': '治理与证据控制', 'criterion': '不产生数学定理，但保证来源、编号、版本、状态和证据等级可信。'},
    {'id': 'FORMAL', 'name': '机器化与复现', 'criterion': '把纸笔定理转成固定工具链上的可重复编译证据。'},
    {'id': 'PUB', 'name': '论文与发布', 'criterion': '将已过门结果组织为范围明确、可复核、可复现的稿件。'},
]

evidence_levels = [
    {'id': 'E0', 'name': '源材料直觉', 'definition': '来自对话、比喻、思想实验或待修复攻击；不能作定理证据。'},
    {'id': 'E1', 'name': '良构陈述', 'definition': '对象、量词、宇宙、相等和目标语义已明确，但证明未完成。'},
    {'id': 'E2', 'name': '纸笔证明', 'definition': '已有可审查证明或严格反例；尚无证明助理回执。'},
    {'id': 'E3', 'name': '有限程序核验', 'definition': '有限枚举、模型检查或索引检查通过；不得冒充无界证明。'},
    {'id': 'E4', 'name': '证明助理通过', 'definition': '固定版本工具链对核心源码 type-check/compile 成功，并保存回执。'},
    {'id': 'E5', 'name': '独立红队复核', 'definition': '独立证明、反例搜索或第二形式化栈复核通过。'},
    {'id': 'E6', 'name': '文献与原创性审计', 'definition': '逐定理完成 prior-art、归属、差异和不确定性审计。'},
    {'id': 'E7', 'name': '发布级复现', 'definition': '干净环境重建、论文/源码/日志/哈希一致并可公开复现。'},
]

status_vocabulary = [
    {'id': 'COMPLETE', 'meaning': '本工作包当前版本的验收条件已满足；后续变更需重新开门。'},
    {'id': 'ACTIVE', 'meaning': '正在执行且依赖已满足。'},
    {'id': 'READY', 'meaning': '定义和纸笔基础充分，可以开始。'},
    {'id': 'PAPER_PROVED_FORMALIZATION_BLOCKED', 'meaning': '纸笔证明存在，但机器化受工具链或依赖阻塞。'},
    {'id': 'BLOCKED_TOOLCHAIN_ABSENT', 'meaning': '当前环境缺少必要证明助理或库。'},
    {'id': 'BLOCKED_DEPENDENCY', 'meaning': '依赖工作包尚未通过。'},
    {'id': 'DEFERRED', 'meaning': '主动延后，防止分散主线。'},
    {'id': 'PARKED', 'meaning': '保留材料但不进入活动证明链。'},
]

# Convert fine-grained work packages to task modules.
def tm_id(old_id: str) -> str:
    assert old_id.startswith('WP-')
    return 'TM-' + old_id[3:]

modules: list[dict[str, Any]] = []
for old in micro_register['work_packages']:
    oid = old['id']
    if oid not in legacy_tm_parent:
        raise KeyError(f'Missing TM parent mapping for {oid}')
    m = deepcopy(old)
    m['id'] = tm_id(oid)
    m['legacy_id'] = oid
    m['parent_wp'] = legacy_tm_parent[oid]
    m['supports_wps'] = legacy_tm_supports.get(oid, [])
    m['dependencies'] = [tm_id(x) for x in old.get('dependencies', [])]
    m['legacy_stream'] = m.pop('stream', None)
    m['level'] = 'task_module'
    modules.append(m)

# Add a dedicated formalization module for canonical WP-33, which the old fine-grained plan only covered indirectly.
modules.append({
    'id': 'TM-635',
    'legacy_id': None,
    'parent_wp': 'WP-33',
    'supports_wps': ['WP-13', 'WP-16', 'WP-19'],
    'title': '形式化批次 C：范畴、资源与可计算性集成',
    'legacy_stream': 'S6 形式化验证',
    'mechanism': 'FORMAL/M1/M3',
    'priority': 'P2',
    'status': 'BLOCKED',
    'objective': '把 walking-arrow/core、cartesian–linear 结构障碍与固定演算归约组织为独立重型机器化批次。',
    'current_basis': '纸笔证明与最小有限模型存在；尚缺合适的范畴/可计算性形式化栈。',
    'source_refs': ['SRC-NARR-001', 'SRC-HEEL-001', 'SRC-SELF-001'],
    'claim_refs': ['Z-33', 'Z-34', 'Z-39', 'Z-136', 'Z-137', 'Z-138'],
    'proof_refs': ['PA-09', 'PA-11', 'PA-33', 'PA-63', 'PA-64', 'PA-72', 'PA-73'],
    'result_refs': ['R-08', 'R-10', 'R-30', 'R-59', 'R-60', 'R-70', 'R-71'],
    'dependencies': ['TM-230', 'TM-400', 'TM-410', 'TM-420', 'TM-430', 'TM-600'],
    'tasks': ['选择 Rzk/Agda Categories/Lean 等适配栈', '机器化 walking arrow 与 core', '机器化 strong monoidal comonoid transfer 或最小替代', '机器化至少一条 halting/inhabitation reduction', '保存失败最小复现'],
    'deliverables': ['formal/batch_c/', 'verification/batch_c_build.log', 'formal/batch_c/ASSUMPTIONS.md'],
    'acceptance_criteria': ['工具选择有书面理由', '至少一条核心对象/归约达到 E4', '不把有限搜索冒充无界证明', '失败依赖和 postulates 完整公开'],
    'failure_or_split_conditions': ['若单一工具栈无法覆盖三类结果，则拆分为 category/resource 与 computability 两个批次；不得因工具不匹配改变数学结论。'],
    'target_outputs': ['Paper A/B/C formal appendices'],
    'level': 'task_module',
})

# Add the publication module missing from the 45-package detailed plan.
modules.append({
    'id': 'TM-815',
    'legacy_id': None,
    'parent_wp': 'WP-43',
    'supports_wps': ['WP-19', 'WP-33', 'WP-40'],
    'title': '论文 C：有效求解与未来判定边界组装',
    'legacy_stream': 'S8 写作发布',
    'mechanism': 'PUB/M3',
    'priority': 'P2',
    'status': 'READY',
    'objective': '把 future stabilization、inhabitation synthesis 与 semantic canonicalization 的条件性不可计算结果组织为独立论文，避免绑架 Paper A。',
    'current_basis': 'WP-19 已有纸笔归约框架；尚缺固定演算、机器化和逐定理文献审计。',
    'source_refs': ['SRC-HEEL-001', 'SRC-SELF-001', 'SRC-Z-001'],
    'claim_refs': ['Z-46', 'Z-59', 'Z-137', 'Z-156'],
    'proof_refs': ['PA-15', 'PA-64', 'PA-65', 'PA-72'],
    'result_refs': ['R-14', 'R-25', 'R-31', 'R-32', 'R-70'],
    'dependencies': ['TM-420', 'TM-430', 'TM-700', 'TM-720'],
    'tasks': ['锁定统一计算模型与编码', '统一三类归约的假设模板', '写 positive escape routes：partial/interactive/heuristic solver', '完成论文范围、limitations 和复现附录'],
    'deliverables': ['paper_C/main.md或.tex', 'paper_C/reductions/', 'paper_C/assumption_matrix.json'],
    'acceptance_criteria': ['所有不可判定性结论给出明确归约', '至少一条归约达到 E4 或 E5', '标题不暗示 HoTT 独有', '不从自然语言模糊直接跳到 halting'],
    'failure_or_split_conditions': ['若固定 HoTT 演算的 inhabitation 元理论不足，则降为一般依赖类型论/证明合成论文；若三个归约缺乏共同结构，则拆为短文。'],
    'target_outputs': ['Paper C'],
    'level': 'task_module',
})

# Status overrides grounded in current environment/tool facts.
status_override = {
    'WP-30': ('BLOCKED_TOOLCHAIN_ABSENT', 'E1'),
    'WP-31': ('BLOCKED_TOOLCHAIN_ABSENT', 'E1'),
    'WP-32': ('BLOCKED_DEPENDENCY', 'E1'),
    'WP-33': ('BLOCKED_DEPENDENCY', 'E1'),
    'WP-12': ('PAPER_PROVED_FORMALIZATION_BLOCKED', 'E2'),
    'WP-17': ('PAPER_PROVED_FORMALIZATION_BLOCKED', 'E2'),
    'WP-46': ('BLOCKED_DEPENDENCY', 'E0'),
}

# Additional source basis when not captured by the detailed modules.
wp_source_extra: dict[str, list[str]] = {
    'WP-00': ['SRC-META-001'],
    'WP-01': ['SRC-Z-001', 'SRC-FINAL-001', 'SRC-NARR-001'],
    'WP-02': ['SRC-META-001'],
    'WP-03': [],
    'WP-10': ['SRC-Z-001', 'SRC-FINAL-001'],
    'WP-11': ['SRC-Z-001', 'SRC-LAST-001'],
    'WP-12': ['SRC-Z-001', 'SRC-ID-001'],
    'WP-13': ['SRC-NARR-001', 'SRC-Z-001'],
    'WP-14': ['SRC-Z-001', 'SRC-FINAL-EX-001', 'SRC-SELF-001'],
    'WP-15': ['SRC-SEM-001', 'SRC-ID-001'],
    'WP-16': ['SRC-HEEL-001', 'SRC-NARR-001'],
    'WP-17': ['SRC-PROB-001', 'SRC-PROB-EX-001'],
    'WP-18': ['SRC-HEEL-001', 'SRC-Z-001'],
    'WP-19': ['SRC-HEEL-001', 'SRC-SELF-001'],
    'WP-20': ['SRC-GODEL-001', 'SRC-CANTOR-001', 'SRC-MIRROR-001', 'SRC-MIRROR-EX-001', 'SRC-UNIV-001'],
    'WP-30': [], 'WP-31': [], 'WP-32': [], 'WP-33': [],
    'WP-40': ['SRC-EXP-001', 'SRC-OBSERVER-001', 'SRC-QUANTUM-001', 'SRC-HOMID-001', 'SRC-CANTOR-001', 'SRC-GODEL-001'],
    'WP-41': ['SRC-Z-001', 'SRC-ID-001', 'SRC-SEM-001'],
    'WP-42': ['SRC-SEM-001', 'SRC-HEEL-001', 'SRC-PROB-EX-001', 'SRC-ID-001'],
    'WP-43': ['SRC-HEEL-001', 'SRC-SELF-001', 'SRC-Z-001'],
    'WP-44': ['SRC-GODEL-001', 'SRC-CANTOR-001', 'SRC-MIRROR-001'],
    'WP-45': ['SRC-FINAL-001', 'SRC-NARR-001', 'SRC-FINAL-EX-001', 'SRC-Z-001'],
    'WP-46': ['SRC-META-001'],
}

modules_by_parent: dict[str, list[dict[str, Any]]] = defaultdict(list)
for m in modules:
    modules_by_parent[m['parent_wp']].append(m)

# Parse linked research IDs from the 26-WP plan and union with detailed modules.
def classify_ref(x: str) -> tuple[str, str] | None:
    x = x.strip()
    # ranges are retained as linked_research_ids but not used for existence checking.
    if re.fullmatch(r'Z-\d+', x): return ('claim', x)
    if re.fullmatch(r'PA-\d+', x): return ('proof', x)
    if re.fullmatch(r'R-\d+', x): return ('result', x)
    if re.fullmatch(r'LIT-\d+', x): return ('literature', x)
    return None

canonical_wps: list[dict[str, Any]] = []
for old in wp_register['work_packages']:
    w = deepcopy(old)
    wid = w['id']
    w['level'] = 'work_package'
    w['area_id'] = wp_area[wid]
    if wid in status_override:
        w['status'], w['current_evidence'] = status_override[wid]
    tms = sorted(modules_by_parent.get(wid, []), key=lambda x: x['id'])
    w['task_modules'] = [m['id'] for m in tms]
    source_refs = set(wp_source_extra.get(wid, []))
    claims, proofs, results, lits = set(), set(), set(), set()
    for m in tms:
        source_refs.update(m.get('source_refs', []))
        claims.update(m.get('claim_refs', []))
        proofs.update(m.get('proof_refs', []))
        results.update(m.get('result_refs', []))
    for ref in w.get('linked_research_ids', []):
        c = classify_ref(ref)
        if c:
            kind, val = c
            {'claim': claims, 'proof': proofs, 'result': results, 'literature': lits}[kind].add(val)
    w['source_refs'] = sorted(source_refs)
    w['claim_refs'] = sorted(claims, key=lambda s: int(s.split('-')[1]))
    w['proof_refs'] = sorted(proofs, key=lambda s: int(s.split('-')[1]))
    w['result_refs'] = sorted(results, key=lambda s: int(s.split('-')[1]))
    w['literature_refs'] = sorted(lits)
    w['failure_or_split_conditions'] = []
    for m in tms:
        for item in m.get('failure_or_split_conditions', []):
            if item not in w['failure_or_split_conditions']:
                w['failure_or_split_conditions'].append(item)
    if not w['failure_or_split_conditions']:
        w['failure_or_split_conditions'] = ['若验收条件无法满足，则收缩量词、分离 HoTT 特定与一般部分，或降级为限制/反例/哲学动机；不得以修辞替代证明。']
    canonical_wps.append(w)

# Areas get their work packages and intended outputs.
area_output_map = {
    'AREA-00': ['单一事实源', '来源与编号治理'],
    'AREA-01': ['TheoryProfile', 'Claim Scope Matrix'],
    'AREA-02': ['Z core', 'Loss spectrum', 'Minimal sufficient quotient'],
    'AREA-03': ['Paper A core theorems', 'orientation/core formalization'],
    'AREA-04': ['Paper A appendix', 'Paper III / philosophy companion'],
    'AREA-05': ['Paper B'],
    'AREA-06': ['Paper B'],
    'AREA-07': ['Paper B'],
    'AREA-08': ['Paper C'],
    'AREA-09': ['Paper D'],
    'AREA-10': ['formal/ source and receipts'],
    'AREA-11': ['originality matrix', 'red-team reports'],
    'AREA-12': ['Papers A–D', 'philosophy companion'],
    'AREA-13': ['reproducibility bundle'],
}
for a in areas:
    a['work_packages'] = [w['id'] for w in canonical_wps if w['area_id'] == a['id']]
    a['target_outputs'] = area_output_map[a['id']]

# Unified gates.
gates = [
    {
        'id': 'G-00', 'title': '单一事实源与治理基线',
        'requires': ['WP-00', 'WP-02'],
        'criteria': ['活动 Source/Claim/Proof/Result/Literature/WP/TM ID 唯一', '规范/候选/历史计划状态无冲突', '源文件重复与派生关系已登记'],
        'unlocks': ['WP-01', 'WP-03', 'WP-10', 'WP-30']
    },
    {
        'id': 'G-01', 'title': '理论剖面与数学核心冻结',
        'requires': ['WP-01', 'WP-10', 'WP-11'],
        'criteria': ['每个定理指定 HoTT 变体、对象/元理论、宇宙与相等概念', 'Z 因子化必要方向纸笔证明完整', '充分性仅在 image/quotient/满射等明确条件下陈述'],
        'unlocks': ['WP-12', 'WP-13', 'WP-14', 'WP-15', 'WP-16', 'WP-18', 'WP-19']
    },
    {
        'id': 'G-02', 'title': '可复现证明助理工具链',
        'requires': ['WP-30'],
        'criteria': ['固定编译器与库 commit', 'smoke test 退出码 0', '命令、stdout/stderr、源码哈希和环境锁文件齐全'],
        'unlocks': ['WP-31', 'WP-32', 'WP-33']
    },
    {
        'id': 'G-03', 'title': '首个 HoTT 特定机器定理',
        'requires': ['WP-12', 'WP-31'],
        'criteria': ['no-canonical-earlier-event 或同等核心定理达到 E4', '无等价于结论的新增 postulate', '纸笔定理、源码与主稿逐项对应'],
        'unlocks': ['WP-17', 'WP-41']
    },
    {
        'id': 'G-04', 'title': '核心定理套件与变体红队',
        'requires': ['WP-13', 'WP-17', 'WP-40'],
        'criteria': ['ordinary non-invertible functions 等最强反驳已处理', '裸层、富化层与具体遗忘映射严格区分', '至少一个 core/time-reversal 或 witness 定理达到 E4/E5'],
        'unlocks': ['WP-41', 'WP-42']
    },
    {
        'id': 'G-05', 'title': '文献、归属与原创性清算',
        'requires': ['WP-03', 'WP-40'],
        'criteria': ['逐定理 prior-art matrix 完成', '创建者/拥趸主张仅使用一手可核对材料', '无无证“首次/推翻/学界未发现”措辞'],
        'unlocks': ['WP-41', 'WP-42', 'WP-43', 'WP-44']
    },
    {
        'id': 'G-06', 'title': 'Paper A 投稿就绪',
        'requires': ['WP-41'],
        'criteria': ['中心定理至少一项 E4', '关键定理均有 E2、E5、E6', '摘要明确相对不完备而非 HoTT⊢⊥', '形式化附录和 claim crosswalk 完整'],
        'unlocks': ['WP-46']
    },
    {
        'id': 'G-07', 'title': '独立复现与项目发布',
        'requires': ['WP-46'],
        'criteria': ['从干净环境重建成功', '论文/源码/日志/清单哈希一致', '未解决异议与失败路线公开', '发布物明确区分主论文与支线'],
        'unlocks': ['公开发布', '后续论文 B/C/D 正式启动']
    },
]

critical_path = ['WP-00', 'WP-02', 'WP-01', 'WP-10', 'WP-30', 'WP-12', 'WP-31', 'WP-03', 'WP-13', 'WP-14', 'WP-40', 'WP-41', 'WP-46']

parallel_lanes = [
    {'id': 'LANE-A', 'name': 'Paper A 主线', 'sequence': ['WP-01', 'WP-10', 'WP-30', 'WP-12', 'WP-31', 'WP-13', 'WP-14', 'WP-40', 'WP-41', 'WP-46']},
    {'id': 'LANE-B', 'name': '签名/语义/资源', 'sequence': ['WP-10', 'WP-15', 'WP-16', 'WP-17', 'WP-18', 'WP-32', 'WP-42']},
    {'id': 'LANE-C', 'name': '有效求解', 'sequence': ['WP-01', 'WP-10', 'WP-19', 'WP-33', 'WP-43']},
    {'id': 'LANE-D', 'name': '反射与宇宙（隔离）', 'sequence': ['WP-01', 'WP-03', 'WP-20', 'WP-44']},
    {'id': 'LANE-PH', 'name': '哲学伴随', 'sequence': ['WP-10', 'WP-14', 'WP-40', 'WP-45']},
]

publication_portfolio = [
    {
        'id': 'PAPER-A',
        'working_title': 'No-Free Temporal and Historical Enrichment in Univalent Foundations',
        'scope': ['Z factorization', 'no canonical temporal orientation', 'groupoid core/time reversal', 'minimal historical enrichment', 'selected limit/operational corollary'],
        'must_exclude': ['HoTT⊢⊥', 'all HoTT arrows are reversible', 'HoTT cannot encode time', 'old transport paradox', 'Gödel-space shortcut'],
        'work_packages': ['WP-10', 'WP-12', 'WP-13', 'WP-14', 'WP-31', 'WP-40', 'WP-41', 'WP-46'],
    },
    {
        'id': 'PAPER-B',
        'working_title': 'Signature-Relative Incompleteness: Context, Intent, Evidence, and Resource Regimes in Univalent Foundations',
        'scope': ['provenance', 'intended role', 'contextual formalization', 'cost/resource regimes', 'truncation/witness'],
        'must_exclude': ['meaning is intrinsically non-mathematical', 'Nat≃Nat′ implies judgmental interchangeability', 'old once-only transport'],
        'work_packages': ['WP-15', 'WP-16', 'WP-17', 'WP-18', 'WP-32', 'WP-42'],
    },
    {
        'id': 'PAPER-C',
        'working_title': 'Effective Boundaries of Formalization, Proof Synthesis, and Future Stabilization',
        'scope': ['future stabilization', 'inhabitation synthesis', 'semantic canonicalization', 'partial/interactive positive results'],
        'must_exclude': ['halting claim without a reduction', 'natural-language ambiguity directly implies undecidability', 'HoTT-specific attribution without proof'],
        'work_packages': ['WP-19', 'WP-33', 'WP-43'],
    },
    {
        'id': 'PAPER-D',
        'working_title': 'Reflection and Diagonalization in Univalent Type-Theoretic Foundations',
        'scope': ['syntax coding', 'provability/evaluation', 'Lawvere fixed point', 'universe/resizing/predicativity'],
        'must_exclude': ['Map(1,G)=ΩG', 'a universe of all types at the same level', 'observer-dimension analogy as proof'],
        'work_packages': ['WP-20', 'WP-44'],
    },
    {
        'id': 'PAPER-PH',
        'working_title': 'Z Law, Zeno, Being and Becoming: The Ontological Limits of Formal Abstraction',
        'scope': ['original philosophical insight', 'photograph/film/projector', 'extensional vs operational completion', 'model/reality boundary'],
        'must_exclude': ['philosophical premise presented as formal theorem', 'limit theory is mathematically inconsistent'],
        'work_packages': ['WP-14', 'WP-45'],
    },
]

immediate_queue = [
    {'id': 'AQ-01', 'priority': 'P0', 'work_package': 'WP-00', 'action': '完成分层 WBS v2 合并、废止竞争计划、更新单一事实源。', 'output': '本方案、机器注册表、交叉索引和完整性回执。', 'status': 'COMPLETE'},
    {'id': 'AQ-02', 'priority': 'P0', 'work_package': 'WP-01', 'action': '建立 HOTT_Z_THEORY_PROFILE.md：逐定理固定 axiomatic/cubical/directed/guarded/linear profile。', 'output': 'TheoryProfile 与 Claim Scope Matrix。', 'status': 'NEXT'},
    {'id': 'AQ-03', 'priority': 'P0', 'work_package': 'WP-10', 'action': '冻结 Z factorization 的集合、hProp、image/quotient 三版陈述。', 'output': 'Z_FACTORISATION_CORE.md 与 formal lemma spec。', 'status': 'NEXT'},
    {'id': 'AQ-04', 'priority': 'P0', 'work_package': 'WP-30', 'action': '安装并锁定 Agda-unimath 主栈；若当前环境不可安装，生成可复现容器/脚本和明确阻塞回执。', 'output': 'toolchain.lock、smoke test、完整日志。', 'status': 'BLOCKED_TOOLCHAIN_ABSENT'},
    {'id': 'AQ-05', 'priority': 'P0', 'work_package': 'WP-31', 'action': '机器化 fixed-point-free monodromy 与 no-canonical-earlier-event。', 'output': '首个 E4 HoTT 特定定理。', 'status': 'BLOCKED_BY_AQ-04'},
    {'id': 'AQ-06', 'priority': 'P0', 'work_package': 'WP-03', 'action': '建立 Paper A 逐定理 prior-art matrix，重点检索 univalence/no-section/global choice/directed type theory。', 'output': 'HOTT_Z_ORIGINALITY_MATRIX.md。', 'status': 'PARALLEL_READY'},
    {'id': 'AQ-07', 'priority': 'P0', 'work_package': 'WP-13', 'action': '完成 walking-arrow/core/time-reversal 最小形式模型，并选择 Rzk/Agda Categories/Lean 路线。', 'output': '方向障碍定理稿与机器化设计。', 'status': 'READY'},
    {'id': 'AQ-08', 'priority': 'P1', 'work_package': 'WP-17', 'action': '复用 no-section/global-choice 结果建立 no-uniform-witness-extractor。', 'output': '证据截断定理和形式化文件。', 'status': 'DEPENDENT_ON_AQ-05'},
    {'id': 'AQ-09', 'priority': 'P0', 'work_package': 'WP-40', 'action': '对 Paper A 运行最强红队：ordinary functions、Step relations、directed/cubical/guarded enrichments。', 'output': '反驳矩阵与定理收缩记录。', 'status': 'ACTIVE'},
    {'id': 'AQ-10', 'priority': 'P0', 'work_package': 'WP-41', 'action': '只在 G-03/G-05 通过后冻结 Paper A 定理集并压缩 v4 候选。', 'output': '窄 Paper A 匿名稿。', 'status': 'BLOCKED_BY_GATES'},
]

# Risks unified from prior plans plus reconciliation risk.
risks = [
    {'id': 'RK-01', 'severity': 'CRITICAL', 'risk': '把相对表示不完备误写成 HoTT 内部不一致。', 'mitigation': 'WP-01 scope matrix；摘要和每条定理强制写目标语义、遗忘映射和富化政策。'},
    {'id': 'RK-02', 'severity': 'CRITICAL', 'risk': '把 ordinary function/Step 可表示非可逆过程这一反例忽略。', 'mitigation': 'WP-40 永久回归测试；结论限定 identity/core 或指定遗忘表示。'},
    {'id': 'RK-03', 'severity': 'CRITICAL', 'risk': 'no-section 机制和因子分解定理属于既有一般数学，原创性被否定。', 'mitigation': 'WP-03 逐定理 prior-art；贡献改为 HoTT 特定专门化、统一框架或新应用。'},
    {'id': 'RK-04', 'severity': 'HIGH', 'risk': '当前证明助理工具链不存在，形式化长期阻塞。', 'mitigation': 'WP-30 先建立容器/锁文件；允许换第二工具栈但必须保留可复现回执。'},
    {'id': 'RK-05', 'severity': 'HIGH', 'risk': '单价“无方向”定理只是任意对称对象无自然选择的改名。', 'mitigation': '明确一般引理与 HoTT/time 专门化的贡献层级；增加 strict order、core 和 enrichment 下界。'},
    {'id': 'RK-06', 'severity': 'HIGH', 'risk': '从数学极限越界到物理超任务或连续统本体结论。', 'mitigation': 'WP-14 每个物理结论附加模型公理；数学结论只谈 reachability/closure/factorization。'},
    {'id': 'RK-07', 'severity': 'HIGH', 'risk': '形式化翻译的不确定性被无归约地升级为停机不可判定。', 'mitigation': 'WP-18 先证明语境欠定；WP-19 只有固定编码后做 reduction。'},
    {'id': 'RK-08', 'severity': 'HIGH', 'risk': '旧 transport、Gödel space、universe equivalence、observer dimension 或 quantum successor 重新进入主证明。', 'mitigation': 'WP-40 负控制套件和隔离表；CI 检查禁用措辞/引用。'},
    {'id': 'RK-09', 'severity': 'MEDIUM', 'risk': '论文 A 范围过宽，被哲学、资源和反射支线淹没。', 'mitigation': 'Paper A 只保留 Z core、orientation、core/time-reversal 和必要历史富化。'},
    {'id': 'RK-10', 'severity': 'MEDIUM', 'risk': '源材料多为 AI 对话与派生摘录，被误作独立学术证据。', 'mitigation': 'WP-02 来源谱系；对话只作思想来源，数学证据来自证明/形式化/一手文献。'},
    {'id': 'RK-11', 'severity': 'MEDIUM', 'risk': '无截面证明隐藏选择、公理或 universe/truncation 问题。', 'mitigation': 'WP-10/WP-12 明确 constructive assumptions；源码审查 postulates。'},
    {'id': 'RK-12', 'severity': 'MEDIUM', 'risk': '不同 HoTT/cubical/directed/linear 变体被混称为同一理论。', 'mitigation': 'WP-01 TheoryProfile；每条定理附 profile card。'},
    {'id': 'RK-13', 'severity': 'MEDIUM', 'risk': '并行写入再次产生多个规范计划或重复编号。', 'mitigation': '本 v2 为唯一规范；旧计划标记 SUPERSEDED；AGENTS 和 JSON 固定变更流程。'},
    {'id': 'RK-14', 'severity': 'MEDIUM', 'risk': '有限 Python 枚举被误写为无界形式证明。', 'mitigation': 'E3/E4 分级；所有日志注明证据等级。'},
    {'id': 'RK-15', 'severity': 'LOW', 'risk': '哲学稿的强修辞被误引入数学摘要。', 'mitigation': 'Paper-PH 与 Paper A 分仓；claim lint 检查“粉碎/幻觉/非法”等词。'},
]

superseded_plans = [
    {'file': 'HOTT_Z_后续工作总方案与工作包分解_v1.md', 'role': '26-WP execution plan; canonical WP IDs retained in v2', 'status': 'SUPERSEDED_NONCANONICAL'},
    {'file': 'HOTT_Z_WORK_PACKAGE_REGISTER.json', 'role': 'legacy 26-WP registry; absorbed verbatim/normalized into v2', 'status': 'SUPERSEDED_NONCANONICAL'},
    {'file': 'HOTT_Z_后续工作总体方案与工作包分解_第四轮.md', 'role': '14-macro-area plan; concepts retained as AREA level', 'status': 'SUPERSEDED_NONCANONICAL'},
    {'file': 'HOTT_Z_WORK_BREAKDOWN_STRUCTURE.json', 'role': 'legacy 14-WP macro registry; absorbed as program areas and gates', 'status': 'SUPERSEDED_NONCANONICAL'},
    {'file': 'HOTT_Z_后续工作总方案与WBS_v1.md', 'role': '45-package fine-grained plan; IDs converted to TM task modules', 'status': 'SUPERSEDED_NONCANONICAL'},
    {'file': 'HOTT_Z_WBS_REGISTRY_v1.json', 'role': 'legacy 45-package registry; converted to TM modules, plus TM-635 and TM-815 added', 'status': 'SUPERSEDED_NONCANONICAL'},
    {'file': 'HOTT_Z_工作包—来源—主张追踪矩阵_v1_1.md', 'role': 'v1.1 trace matrix; replaced by v2 registry and crosswalk', 'status': 'SUPERSEDED_NONCANONICAL'},
]

program = {
    'schema_version': 'hott_z_hierarchical_wbs.v2',
    'canonical': True,
    'program_id': 'HOTT-Z-RP-20260831',
    'version': '2.0',
    'date': DATE,
    'generated_at_utc': STAMP,
    'title': 'HoTT–Z 相对不完备性研究：后续工作总体方案与分层 WBS',
    'mission': '把 Z 铁律的哲学洞察重构为可证明、可形式化、可红队、可检索和可复现的 HoTT 相对不完备性结果。',
    'central_thesis': '当指定 HoTT/单价表示遗忘了目标相关的时间、历史、语境、资源或见证差异时，这些真值不能在无新增信息条件下由裸表示免费、自然、无损恢复。',
    'non_goals': [
        '不以当前项目证明 HoTT⊢⊥。',
        '不主张 HoTT 完全不能编码时间、非可逆函数、状态转移或资源结构。',
        '不把一般 Gödel/halting/no-choice 限制冒充 HoTT 独有漏洞。',
        '不把 AI 对话中的赞同、沉默或专家角色当作数学证据。',
        '不把有限枚举和索引脚本冒充证明助理验证。',
    ],
    'source_basis_note': '源材料提供问题发现、Being/Becoming、照片/电影/放映机、三大阿喀琉斯之踵和语义角色等思想；旧证明中的逻辑、类型和归约错误已转入红队负控制。',
    'hierarchy': {'areas': 14, 'work_packages': len(canonical_wps), 'task_modules': len(modules), 'gates': len(gates)},
    'mechanisms': mechanisms,
    'evidence_levels': evidence_levels,
    'status_vocabulary': status_vocabulary,
    'areas': areas,
    'work_packages': canonical_wps,
    'task_modules': sorted(modules, key=lambda x: x['id']),
    'gates': gates,
    'critical_path': critical_path,
    'parallel_lanes': parallel_lanes,
    'publication_portfolio': publication_portfolio,
    'immediate_queue': immediate_queue,
    'risks': risks,
    'current_toolchain_facts': {
        'checked_on': DATE,
        'executables': {'agda': False, 'lean': False, 'lake': False, 'coqc': False, 'rocq': False, 'rzk': False},
        'consequence': 'WP-30/WP-31 remain blocked until a reproducible stack is installed or supplied.'
    },
    'superseded_plans': superseded_plans,
    'canonical_pointer': {
        'file': 'HOTT_Z_WORKPLAN_CANONICAL_POINTER.md',
        'status': 'ACTIVE_CANONICAL',
        'note': 'The earlier v1.1 pointer content was replaced in place; this path now points exclusively to hierarchical WBS v2 and is not a superseded artifact.',
    },
}

# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------
def unique_ids(items: Iterable[dict[str, Any]], key: str = 'id') -> tuple[bool, list[str]]:
    seen, dup = set(), []
    for x in items:
        val = x[key]
        if val in seen: dup.append(val)
        seen.add(val)
    return (not dup, dup)


def cycle_check(nodes: list[str], deps: dict[str, list[str]]) -> tuple[bool, list[str]]:
    indeg = {n: 0 for n in nodes}
    out = {n: [] for n in nodes}
    for n in nodes:
        for d in deps.get(n, []):
            if d in indeg:
                indeg[n] += 1
                out[d].append(n)
    q = deque([n for n, i in indeg.items() if i == 0])
    order = []
    while q:
        n = q.popleft(); order.append(n)
        for y in out[n]:
            indeg[y] -= 1
            if indeg[y] == 0: q.append(y)
    return len(order) == len(nodes), order


def extract_ids(path: Path, pattern: str) -> set[str]:
    if not path.exists(): return set()
    return set(re.findall(pattern, path.read_text(encoding='utf-8', errors='replace')))

area_ids = {a['id'] for a in areas}
wp_ids = {w['id'] for w in canonical_wps}
tm_ids = {m['id'] for m in modules}
source_ids = {s['id'] for s in source_registry['sources']}
claim_ids = extract_ids(BASE/'CLAIM_LEDGER.md', r'(?<![A-Za-z0-9])Z-\d+(?![A-Za-z0-9])')
proof_ids = extract_ids(BASE/'PROOF_ATTEMPTS.md', r'(?<![A-Za-z0-9])PA-\d+(?![A-Za-z0-9])')
result_ids = extract_ids(BASE/'RESULTS.md', r'(?<![A-Za-z0-9])R-\d+(?![A-Za-z0-9])')
lit_ids = extract_ids(BASE/'LITERATURE_MAP.md', r'(?<![A-Za-z0-9])LIT-\d+(?![A-Za-z0-9])')

validation: dict[str, Any] = {'schema_version': 'hott_z_hierarchical_wbs_validation.v2', 'checked_at_utc': STAMP}
validation['unique_area_ids'] = {'ok': unique_ids(areas)[0], 'duplicates': unique_ids(areas)[1]}
validation['unique_wp_ids'] = {'ok': unique_ids(canonical_wps)[0], 'duplicates': unique_ids(canonical_wps)[1]}
validation['unique_tm_ids'] = {'ok': unique_ids(modules)[0], 'duplicates': unique_ids(modules)[1]}
validation['wp_area_refs'] = {'ok': all(w['area_id'] in area_ids for w in canonical_wps), 'missing': sorted({w['area_id'] for w in canonical_wps if w['area_id'] not in area_ids})}
validation['wp_dependency_refs'] = {'ok': all(d in wp_ids for w in canonical_wps for d in w['dependencies']), 'missing': sorted({d for w in canonical_wps for d in w['dependencies'] if d not in wp_ids})}
validation['tm_parent_refs'] = {'ok': all(m['parent_wp'] in wp_ids for m in modules), 'missing': sorted({m['parent_wp'] for m in modules if m['parent_wp'] not in wp_ids})}
validation['tm_dependency_refs'] = {'ok': all(d in tm_ids for m in modules for d in m.get('dependencies', [])), 'missing': sorted({d for m in modules for d in m.get('dependencies', []) if d not in tm_ids})}
wp_acyclic, wp_topo = cycle_check(sorted(wp_ids), {w['id']: w['dependencies'] for w in canonical_wps})
tm_acyclic, tm_topo = cycle_check(sorted(tm_ids), {m['id']: m.get('dependencies', []) for m in modules})
validation['wp_acyclic'] = {'ok': wp_acyclic, 'topological_order': wp_topo}
validation['tm_acyclic'] = {'ok': tm_acyclic, 'topological_order': tm_topo}
validation['every_wp_has_module'] = {'ok': all(w['task_modules'] for w in canonical_wps), 'missing': [w['id'] for w in canonical_wps if not w['task_modules']]}
validation['source_refs'] = {
    'ok': all(s in source_ids for m in modules for s in m.get('source_refs', [])) and all(s in source_ids for w in canonical_wps for s in w.get('source_refs', [])),
    'missing': sorted(({s for m in modules for s in m.get('source_refs', [])} | {s for w in canonical_wps for s in w.get('source_refs', [])}) - source_ids),
}
validation['claim_refs'] = {'ok': all(x in claim_ids for m in modules for x in m.get('claim_refs', [])), 'missing': sorted({x for m in modules for x in m.get('claim_refs', []) if x not in claim_ids})}
validation['proof_refs'] = {'ok': all(x in proof_ids for m in modules for x in m.get('proof_refs', [])), 'missing': sorted({x for m in modules for x in m.get('proof_refs', []) if x not in proof_ids})}
validation['result_refs'] = {'ok': all(x in result_ids for m in modules for x in m.get('result_refs', [])), 'missing': sorted({x for m in modules for x in m.get('result_refs', []) if x not in result_ids})}
validation['critical_path_refs'] = {'ok': all(x in wp_ids for x in critical_path), 'missing': [x for x in critical_path if x not in wp_ids]}
validation['gate_refs'] = {'ok': all(x in wp_ids for g in gates for x in g['requires']), 'missing': sorted({x for g in gates for x in g['requires'] if x not in wp_ids})}
validation['counts'] = {'areas': len(areas), 'work_packages': len(canonical_wps), 'task_modules': len(modules), 'gates': len(gates), 'risks': len(risks), 'papers': len(publication_portfolio)}
validation['overall_ok'] = all(v.get('ok', True) for k, v in validation.items() if isinstance(v, dict) and 'ok' in v)
program['validation_summary'] = {'overall_ok': validation['overall_ok'], 'validation_file': 'verification/hierarchical_wbs_v2_integrity.json'}

# ---------------------------------------------------------------------------
# Update source registry with reverse links.
# ---------------------------------------------------------------------------
source_to_wps: dict[str, set[str]] = defaultdict(set)
source_to_tms: dict[str, set[str]] = defaultdict(set)
for w in canonical_wps:
    for s in w.get('source_refs', []): source_to_wps[s].add(w['id'])
for m in modules:
    for s in m.get('source_refs', []): source_to_tms[s].add(m['id'])
source_registry['workplan'] = {
    'canonical_plan': 'HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md',
    'canonical_registry': 'HOTT_Z_HIERARCHICAL_WBS_v2.json',
    'version': '2.0',
    'updated_at_utc': STAMP,
}
for s in source_registry['sources']:
    s['linked_work_packages'] = sorted(source_to_wps.get(s['id'], set()))
    s['linked_task_modules'] = sorted(source_to_tms.get(s['id'], set()))

# ---------------------------------------------------------------------------
# Markdown helpers
# ---------------------------------------------------------------------------
def md_list(items: list[str], indent: str = '') -> str:
    if not items: return indent + '- 无。'
    return '\n'.join(f'{indent}- {x}' for x in items)


def ref_list(items: list[str]) -> str:
    return '、'.join(items) if items else '—'

area_by_id = {a['id']: a for a in areas}
wp_by_id = {w['id']: w for w in canonical_wps}
tm_by_id = {m['id']: m for m in modules}

# Main plan markdown.
md: list[str] = []
md.append('# HoTT–Z 相对不完备性研究：后续工作总体方案与分层 WBS v2（规范版）')
md.append('')
md.append(f'**日期**：{DATE}  ')
md.append('**项目编号**：`HOTT-Z-RP-20260831`  ')
md.append('**状态**：`CANONICAL`  ')
md.append('**单一机器事实源**：`HOTT_Z_HIERARCHICAL_WBS_v2.json`')
md.append('')
md.append('> 本文件吸收并取代此前并行产生的 26-WP、14-WP 和 45-WP 三套计划。规范层级固定为：14 个 `AREA` → 26 个 `WP` → 47 个 `TM`。旧计划仅保留作历史记录，不再分配新状态或编号。')
md.append('')
md.append('## 1. 项目使命与严格边界')
md.append('')
md.append('### 1.1 项目使命')
md.append('')
md.append(program['mission'])
md.append('')
md.append('### 1.2 规范中心命题')
md.append('')
md.append('设现实/历史域为 `W`，数学表示域为 `M`，抽象或遗忘映射为 `α : W → M`，目标事实或完整命题—判定谱为 `J`。若同一 `α`-纤维内存在目标真值差异，则不存在只依赖 `M` 的恢复器在全部目标实例上无损恢复 `J`。')
md.append('')
md.append('应用于 HoTT/单价基础时，研究对象不是“不加限定的 HoTT”，而是指定的裸类型—identity/groupoid 表示、指定的遗忘函子或指定的等价自然性要求。')
md.append('')
md.append('### 1.3 明确不做的结论')
md.append('')
md.append(md_list(program['non_goals']))
md.append('')
md.append('## 2. 来源材料如何进入研究')
md.append('')
md.append('源材料承担四种角色：问题发现、思想谱系、反例启发和红队负控制。它们不因篇幅、重复次数或 AI 角色扮演中的“承认”而自动成为数学证据。')
md.append('')
md.append('- `SRC-Z-001` 与 `SRC-FINAL-001`：Z 铁律、Being/Becoming、照片/电影/放映机和极限类比的思想来源。')
md.append('- `SRC-HEEL-001`：资源、未知、表达三条旧攻击；其旧证明被废弃，分别重构为成本非因子化、无通用合成器和语境欠定。')
md.append('- `SRC-SEM-001` 与 `SRC-ID-001`：Nat/Nat′、provenance、角色和历史性；用于签名相对不完备与无免费富化。')
md.append('- `SRC-PROB-*`：断言、相似、mere existence 与具体 witness 的层级区分。')
md.append('- `SRC-SELF-001`：从静态循环转向 guarded/time-delayed dynamics。')
md.append('- `SRC-GODEL/CANTOR/UNIV/MIRROR-*`：只进入独立反射支线或负控制，不进入时间主证明。')
md.append('')
md.append('## 3. 研究架构')
md.append('')
md.append('### 3.1 三层 WBS')
md.append('')
md.append('| 层级 | 数量 | 作用 | 规范编号 |')
md.append('|---|---:|---|---|')
md.append(f'| Program Area | {len(areas)} | 学术领域和资源分流 | `AREA-00`–`AREA-13` |')
md.append(f'| Work Package | {len(canonical_wps)} | 可验收、可阻塞、可交付的主要工作 | `WP-00` 等 26 个稳定 ID |')
md.append(f'| Task Module | {len(modules)} | 定理、形式化、检索或写作的细粒度执行单元 | `TM-000` 等 47 个 ID |')
md.append('')
md.append('### 3.2 四种主要证明机制')
md.append('')
md.append('| ID | 名称 | 准入问题 |')
md.append('|---|---|---|')
for m in mechanisms[:4]:
    md.append(f"| {m['id']} | {m['name']} | {m['criterion']} |")
md.append('')
md.append('### 3.3 证据等级')
md.append('')
md.append('| 等级 | 名称 | 含义 |')
md.append('|---|---|---|')
for e in evidence_levels:
    md.append(f"| {e['id']} | {e['name']} | {e['definition']} |")
md.append('')
md.append('### 3.4 Program Areas')
md.append('')
md.append('| Area | 目标 | Work Packages | 主要产物 |')
md.append('|---|---|---|---|')
for a in areas:
    md.append(f"| {a['id']} {a['title']} | {a['objective']} | {ref_list(a['work_packages'])} | {ref_list(a['target_outputs'])} |")
md.append('')
md.append('## 4. 关键路径、并行轨道与当前阻塞')
md.append('')
md.append('### 4.1 唯一关键路径')
md.append('')
md.append('```text')
md.append(' → '.join(critical_path))
md.append('```')
md.append('')
md.append('此路径的中心不是扩写宏大判决，而是：先冻结理论口径与 Z 核心，再建立可复现工具链，获得 `no-canonical-earlier-event` 的真实机器回执，完成文献和红队审计，最后形成窄 Paper A。')
md.append('')
md.append('### 4.2 并行轨道')
md.append('')
for lane in parallel_lanes:
    md.append(f"- **{lane['id']} {lane['name']}**：`" + ' → '.join(lane['sequence']) + '`.')
md.append('')
md.append('### 4.3 当前工具链事实')
md.append('')
md.append('当前运行环境未发现 `agda`、`lean`、`lake`、`coqc`、`rocq` 或 `rzk`。因此 WP-30 与 WP-31 为真实阻塞状态；任何核心定理在获得编译回执前最多为 E2/E3。')
md.append('')
md.append('## 5. 工作包总览')
md.append('')
md.append('| WP | Area | 优先级 | 状态 | 当前证据 | 依赖 | 论文去向 |')
md.append('|---|---|---|---|---|---|---|')
for w in canonical_wps:
    md.append(f"| {w['id']} {w['title']} | {w['area_id']} | {w['priority']} | {w['status']} | {w['current_evidence']} | {ref_list(w['dependencies'])} | {w.get('paper_target') or '—'} |")
md.append('')
md.append('## 6. 工作包详细分解')
md.append('')
for w in canonical_wps:
    md.append(f"### {w['id']} — {w['title']}")
    md.append('')
    md.append(f"- **Program Area**：{w['area_id']} {area_by_id[w['area_id']]['title']}")
    md.append(f"- **优先级 / 状态 / 证据**：`{w['priority']}` / `{w['status']}` / `{w['current_evidence']}`")
    md.append(f"- **依赖**：{ref_list(w['dependencies'])}")
    md.append(f"- **论文去向**：{w.get('paper_target') or '无直接论文去向'}")
    md.append(f"- **源材料**：{ref_list(w.get('source_refs', []))}")
    md.append(f"- **研究索引**：Claims {ref_list(w.get('claim_refs', []))}；Proofs {ref_list(w.get('proof_refs', []))}；Results {ref_list(w.get('result_refs', []))}")
    md.append('')
    md.append('**目标**')
    md.append('')
    md.append(w['objective'])
    md.append('')
    md.append('**主要任务**')
    md.append('')
    md.append(md_list(w.get('tasks', [])))
    md.append('')
    md.append('**细粒度 Task Modules**')
    md.append('')
    for tid in w['task_modules']:
        t = tm_by_id[tid]
        md.append(f"- `{tid}` — {t['title']}（机制 `{t.get('mechanism','—')}`；状态 `{t.get('status','—')}`）")
    md.append('')
    md.append('**交付物**')
    md.append('')
    md.append(md_list(w.get('deliverables', [])))
    md.append('')
    md.append('**验收标准**')
    md.append('')
    md.append(md_list(w.get('acceptance_criteria', [])))
    md.append('')
    md.append('**失败、降级或拆分条件**')
    md.append('')
    md.append(md_list(w.get('failure_or_split_conditions', [])))
    if w.get('key_risks'):
        md.append('')
        md.append('**关键风险**')
        md.append('')
        md.append(md_list(w['key_risks']))
    md.append('')

md.append('## 7. Task Module 索引')
md.append('')
md.append('| TM | Parent WP | 旧 ID | 机制 | 优先级 | 状态 | 依赖 | 标题 |')
md.append('|---|---|---|---|---|---|---|---|')
for t in sorted(modules, key=lambda x: x['id']):
    md.append(f"| {t['id']} | {t['parent_wp']} | {t.get('legacy_id') or '新增'} | {t.get('mechanism','—')} | {t.get('priority','—')} | {t.get('status','—')} | {ref_list(t.get('dependencies', []))} | {t['title']} |")
md.append('')
md.append('## 8. 阶段门')
md.append('')
for g in gates:
    md.append(f"### {g['id']} — {g['title']}")
    md.append('')
    md.append(f"- **依赖工作包**：{ref_list(g['requires'])}")
    md.append('- **通过标准**：')
    md.append(md_list(g['criteria'], indent='  '))
    md.append(f"- **解锁**：{ref_list(g['unlocks'])}")
    md.append('')
md.append('## 9. 论文组合')
md.append('')
for p in publication_portfolio:
    md.append(f"### {p['id']} — {p['working_title']}")
    md.append('')
    md.append(f"- **工作包**：{ref_list(p['work_packages'])}")
    md.append(f"- **范围**：{ref_list(p['scope'])}")
    md.append(f"- **必须排除**：{ref_list(p['must_exclude'])}")
    md.append('')
md.append('## 10. 当前执行队列')
md.append('')
md.append('| Queue | WP | 优先级 | 状态 | 动作 | 验收产物 |')
md.append('|---|---|---|---|---|---|')
for q in immediate_queue:
    md.append(f"| {q['id']} | {q['work_package']} | {q['priority']} | {q['status']} | {q['action']} | {q['output']} |")
md.append('')
md.append('## 11. 风险登记')
md.append('')
md.append('| Risk | 严重度 | 风险 | 缓解措施 |')
md.append('|---|---|---|---|')
for r in risks:
    md.append(f"| {r['id']} | {r['severity']} | {r['risk']} | {r['mitigation']} |")
md.append('')
md.append('## 12. 变更控制与证据升级纪律')
md.append('')
md.append('1. 任何研究动作必须归属一个 `TM`，并通过其 parent `WP` 汇总。')
md.append('2. 数学真理状态变化必须同步更新 `CLAIM_LEDGER.md`、`PROOF_ATTEMPTS.md`、`RESULTS.md`。')
md.append('3. 文献或归属状态变化必须更新 `LITERATURE_MAP.md` 和 originality matrix。')
md.append('4. WP/TM 状态变化必须更新机器注册表、执行看板和 `RESEARCH_LOG.md`。')
md.append('5. E3 不能替代 E4；第二模型或有限枚举只能作错误探测。')
md.append('6. directed/guarded/linear/cost-aware 富化是合法逃逸路线；它们必须被记录为新增结构，不得被说成裸层免费恢复。')
md.append('7. 任何发现核心定理已知或错误的结果都属于成功的研究产出：定理必须降级、收缩或重新定位，不得隐藏。')
md.append('')
md.append('## 13. 废止与交叉索引')
md.append('')
md.append('以下计划已经被本 v2 吸收，不再是规范事实源：')
md.append('')
for s in superseded_plans:
    md.append(f"- `{s['file']}` — `{s['status']}`；{s['role']}。")
md.append('')
md.append('完整旧 ID → AREA/WP/TM 对照见 `HOTT_Z_WBS_CROSSWALK_v2.md`。')
md.append('')
md.append('## 14. 项目完成定义')
md.append('')
md.append('项目不能以“写完一篇宏大文本”为完成。至少满足：')
md.append('')
md.append('- Paper A 有清晰且窄的中心定理；至少一个 HoTT 特定核心达到 E4，全部关键结论达到 E5/E6。')
md.append('- 公开稿明确不证明 `HoTT ⊢ ⊥`，也不否认合法的时间/方向富化。')
md.append('- 源材料、数学证明、机器源码、一手文献和哲学解释分层可追溯。')
md.append('- 干净环境可复现，所有文件有哈希，所有未解决异议公开。')
md.append('- Paper B/C/D 只有在各自工作包通过后推进，不能反向拖累 Paper A。')
md.append('')

main_plan_path = BASE / 'HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md'
main_plan_path.write_text('\n'.join(md) + '\n', encoding='utf-8')

# Machine-readable registry.
registry_path = BASE / 'HOTT_Z_HIERARCHICAL_WBS_v2.json'
registry_path.write_text(json.dumps(program, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Crosswalk markdown.
cross: list[str] = []
cross.append('# HOTT–Z WBS v2 旧计划—规范层级对照表')
cross.append('')
cross.append(f'**日期**：{DATE}  ')
cross.append('**规范计划**：`HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md`')
cross.append('')
cross.append('## 1. 合并规则')
cross.append('')
cross.append('- 26-WP 计划的工作包 ID 被保留为规范 `WP`。')
cross.append('- 第四轮 14-WP 宏观计划被提升为 14 个 `AREA`，不再占用 `WP` 命名空间。')
cross.append('- 45-WP 细粒度计划全部重命名为 `TM`；另补 `TM-635` 与 `TM-815`，使 Paper C 具备明确写作模块。')
cross.append('')
cross.append('## 2. 26-WP 计划')
cross.append('')
cross.append('| 旧 ID | v2 ID | Area | 状态 |')
cross.append('|---|---|---|---|')
for w in canonical_wps:
    cross.append(f"| {w['id']} | {w['id']} | {w['area_id']} | 保留为规范 WP |")
cross.append('')
cross.append('## 3. 45-WP 细粒度计划')
cross.append('')
cross.append('| 旧 ID | v2 TM | Parent WP | Supporting WPs | 标题 |')
cross.append('|---|---|---|---|---|')
for t in sorted(modules, key=lambda x: x['id']):
    cross.append(f"| {t.get('legacy_id') or '新增'} | {t['id']} | {t['parent_wp']} | {ref_list(t.get('supports_wps', []))} | {t['title']} |")
cross.append('')
cross.append('## 4. 第四轮 14-WP 宏观计划')
cross.append('')
macro_to_area = {
    'WP-00': ['AREA-00'], 'WP-01': ['AREA-10'], 'WP-02': ['AREA-02'], 'WP-03': ['AREA-01', 'AREA-11'],
    'WP-04': ['AREA-03'], 'WP-05': ['AREA-03'], 'WP-06': ['AREA-05'], 'WP-07': ['AREA-06'],
    'WP-08': ['AREA-08'], 'WP-09': ['AREA-04'], 'WP-10': ['AREA-07'], 'WP-11': ['AREA-09'],
    'WP-12': ['AREA-11'], 'WP-13': ['AREA-12', 'AREA-13'],
}
cross.append('| 旧宏观 ID | v2 Program Area | 说明 |')
cross.append('|---|---|---|')
for old in macro_register['work_packages']:
    cross.append(f"| {old['id']} {old['title']} | {ref_list(macro_to_area[old['id']])} | 宏观内容被吸收，旧 ID 不再活动 |")
cross.append('')
cross.append('## 5. 不可再用的旧入口')
cross.append('')
for s in superseded_plans:
    cross.append(f"- `{s['file']}`：{s['role']}；仅作历史版本。")
(BASE / 'HOTT_Z_WBS_CROSSWALK_v2.md').write_text('\n'.join(cross) + '\n', encoding='utf-8')

# Mermaid graph.
graph: list[str] = ['flowchart LR']
for a in areas:
    graph.append(f"  subgraph {a['id'].replace('-','_')}[\"{a['id']} {a['title']}\"]")
    for wid in a['work_packages']:
        label = wp_by_id[wid]['title'].replace('"', "'")
        graph.append(f"    {wid.replace('-','_')}[\"{wid} {label}\"]")
    graph.append('  end')
for w in canonical_wps:
    for d in w['dependencies']:
        graph.append(f"  {d.replace('-','_')} --> {w['id'].replace('-','_')}")
for a, b in zip(critical_path, critical_path[1:]):
    graph.append(f"  {a.replace('-','_')} ==>|critical| {b.replace('-','_')}")
(BASE / 'HOTT_Z_HIERARCHICAL_WBS_v2.mmd').write_text('\n'.join(graph) + '\n', encoding='utf-8')

# Immediate queue file.
queue_md = ['# HOTT–Z 下一执行队列 v2', '', f'**日期**：{DATE}', '', '> 当前唯一不可分散 P0：建立工具链并使 `no-canonical-earlier-event` 获得真实 E4 回执。', '']
for q in immediate_queue:
    queue_md.append(f"## {q['id']} — {q['work_package']} — {q['status']}")
    queue_md.append('')
    queue_md.append(q['action'])
    queue_md.append('')
    queue_md.append(f"**产物**：{q['output']}")
    queue_md.append('')
queue_md.append('## 执行顺序')
queue_md.append('')
queue_md.append('```text')
queue_md.append('AQ-02 → AQ-03 → AQ-04 → AQ-05 → AQ-07 → AQ-09 → AQ-10')
queue_md.append('          ↘ AQ-06（并行文献）   ↘ AQ-08（首个无截面形式化后）')
queue_md.append('```')
queue_md.append('')
(BASE / 'HOTT_Z_下一执行队列_v2.md').write_text('\n'.join(queue_md), encoding='utf-8')

# Updated dashboard.
dash = ['# HOTT–Z 执行看板 v2', '', f'**更新时间**：{DATE}', '', '| WP | 标题 | 状态 | 证据 | 下一动作 |', '|---|---|---|---|---|']
next_action = {q['work_package']: q['action'] for q in immediate_queue}
for w in canonical_wps:
    dash.append(f"| {w['id']} | {w['title']} | {w['status']} | {w['current_evidence']} | {next_action.get(w['id'], '按依赖与验收标准推进')} |")
dash.append('')
dash.append('## 当前瓶颈')
dash.append('')
dash.append('`WP-30`：当前环境没有 Agda/Lean/Rocq/Rzk；因此 `WP-31` 尚不能达到 E4。')
dash.append('')
dash.append('## 当前唯一关键路径')
dash.append('')
dash.append('`' + ' → '.join(critical_path) + '`')
dash.append('')
(BASE / 'HOTT_Z_执行看板.md').write_text('\n'.join(dash), encoding='utf-8')

# Updated gates matrix.
gate_md = ['# HOTT–Z 阶段闸门与验收矩阵 v2', '', f'**日期**：{DATE}', '', '| Gate | 名称 | Requires | 核心验收 | Unlocks |', '|---|---|---|---|---|']
for g in gates:
    gate_md.append(f"| {g['id']} | {g['title']} | {ref_list(g['requires'])} | {'；'.join(g['criteria'])} | {ref_list(g['unlocks'])} |")
gate_md.append('')
gate_md.append('## 不可跨越规则')
gate_md.append('')
gate_md.append('- 未过 G-02，不得使用 `MACHINE_CHECKED`。')
gate_md.append('- 未过 G-03，不得把 Paper A 标成投稿就绪。')
gate_md.append('- 未过 G-05，不得使用“首次”“创建者认为”“学界未发现”等强归属。')
gate_md.append('- 未过 G-07，只能发布研究工作区快照，不能发布“最终证明包”。')
(BASE / 'HOTT_Z_阶段闸门与验收矩阵.md').write_text('\n'.join(gate_md) + '\n', encoding='utf-8')

# Updated risk table.
risk_md = ['# HOTT–Z 风险与红队登记表 v2', '', f'**日期**：{DATE}', '', '| ID | 严重度 | 风险 | 缓解措施 |', '|---|---|---|---|']
for r in risks:
    risk_md.append(f"| {r['id']} | {r['severity']} | {r['risk']} | {r['mitigation']} |")
risk_md.append('')
risk_md.append('## 永久负控制')
risk_md.append('')
risk_md.extend([
    '- ordinary `A→B` 可以非可逆；不得说 HoTT 所有箭头可逆。',
    '- 时间、方向、资源和成本可以通过显式结构富化；问题是是否可从裸层免费恢复。',
    '- `Map(1,G)` 不是环空间；环空间是带基点的自同一类型。',
    '- 宇宙“角色相似”不推出 universe equivalence。',
    '- 量子 successor、观察者维度和旧一次性 transport 不进入活动证明链。',
])
(BASE / 'HOTT_Z_风险与红队登记表.md').write_text('\n'.join(risk_md) + '\n', encoding='utf-8')

# Validation outputs.
verify_dir = BASE / 'verification'
verify_dir.mkdir(exist_ok=True)
(verify_dir / 'hierarchical_wbs_v2_integrity.json').write_text(json.dumps(validation, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
val_lines = [
    'HOTT-Z hierarchical WBS v2 integrity check',
    f'checked_at_utc: {STAMP}',
    f'overall_ok: {str(validation["overall_ok"]).lower()}',
    f'areas: {len(areas)}',
    f'work_packages: {len(canonical_wps)}',
    f'task_modules: {len(modules)}',
    f'gates: {len(gates)}',
    f'risks: {len(risks)}',
    f'papers: {len(publication_portfolio)}',
    f'wp_acyclic: {str(wp_acyclic).lower()}',
    f'tm_acyclic: {str(tm_acyclic).lower()}',
]
for key in ['unique_area_ids','unique_wp_ids','unique_tm_ids','wp_area_refs','wp_dependency_refs','tm_parent_refs','tm_dependency_refs','every_wp_has_module','source_refs','claim_refs','proof_refs','result_refs','critical_path_refs','gate_refs']:
    val_lines.append(f'{key}: {str(validation[key]["ok"]).lower()}')
    if validation[key].get('missing'): val_lines.append(f'  missing: {validation[key]["missing"]}')
    if validation[key].get('duplicates'): val_lines.append(f'  duplicates: {validation[key]["duplicates"]}')
(verify_dir / 'hierarchical_wbs_v2_integrity.txt').write_text('\n'.join(val_lines) + '\n', encoding='utf-8')

# Source registry update after validation.
(BASE / 'HOTT_Z_SOURCE_REGISTRY.json').write_text(json.dumps(source_registry, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Baseline lock with input/output hashes.
def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

baseline_inputs = [
    'archive/superseded_workplans_20260831/26_wp_plan_superseded/HOTT_Z_WORK_PACKAGE_REGISTER.json',
    'archive/superseded_workplans_20260831/14_wp_round4_plan_superseded/HOTT_Z_WORK_BREAKDOWN_STRUCTURE.json',
    'HOTT_Z_WBS_REGISTRY_v1.json',
    'HOTT_Z_SOURCE_REGISTRY.json', 'CLAIM_LEDGER.md', 'PROOF_ATTEMPTS.md', 'RESULTS.md', 'LITERATURE_MAP.md',
    'HOTT_Z_后续研究可用性总索引_第三轮.md', 'HOTT_Z_内生时间不完备性_论文草案_v3.md',
    'HOTT_Z_内生时间不完备性_论文草案_v4_候选.md',
]
lock = {
    'schema_version': 'hott_z_program_baseline.v2', 'date': DATE, 'generated_at_utc': STAMP,
    'canonical_plan': main_plan_path.name, 'canonical_registry': registry_path.name,
    'input_files': [], 'toolchain_check': program['current_toolchain_facts'],
}
for name in baseline_inputs:
    p = BASE / name
    if p.exists():
        lock['input_files'].append({'file': name, 'bytes': p.stat().st_size, 'sha256': sha256(p)})
(BASE / 'HOTT_Z_PROGRAM_BASELINE_v2.json').write_text(json.dumps(lock, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Mark old markdown plans as superseded without deleting historical content.
supersede_note = (
    '> **SUPERSEDED_NONCANONICAL — 2026-08-31**  \n'
    '> 本文件已被 `HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md` 吸收。'
    '保留作历史版本；不得再作为活动编号、状态或执行顺序的事实源。\n\n'
)
for name in ['HOTT_Z_后续工作总方案与工作包分解_v1.md', 'HOTT_Z_后续工作总体方案与工作包分解_第四轮.md', 'HOTT_Z_后续工作总方案与WBS_v1.md', 'HOTT_Z_下一执行批次_P0P1.md', 'HOTT_Z_下一执行队列_第四轮.md', 'HOTT_Z_工作包—来源—主张追踪矩阵_v1_1.md', 'HOTT_Z_后续工作执行摘要_规范版.md']:
    p = BASE / name
    if p.exists():
        text = p.read_text(encoding='utf-8')
        if not text.startswith('> **SUPERSEDED_NONCANONICAL'):
            p.write_text(supersede_note + text, encoding='utf-8')

# Mark old JSON registries as noncanonical, preserving their data.
for name in ['HOTT_Z_WORK_PACKAGE_REGISTER.json', 'HOTT_Z_WORK_BREAKDOWN_STRUCTURE.json', 'HOTT_Z_WBS_REGISTRY_v1.json']:
    p = BASE / name
    if p.exists():
        d = json.loads(p.read_text(encoding='utf-8'))
        d['canonical'] = False
        d['status'] = 'SUPERSEDED_NONCANONICAL'
        d['superseded_by'] = 'HOTT_Z_HIERARCHICAL_WBS_v2.json'
        d['superseded_at'] = DATE
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Replace AGENTS plan section from first section 26 onward with one canonical section.
agents_path = BASE / 'AGENTS.md'
agents = agents_path.read_text(encoding='utf-8')
pos = agents.find('\n## 26.')
if pos == -1:
    pos = len(agents)
canonical_agents_section = f'''\n\n## 26. HOTT–Z 分层 WBS v2：唯一后续工作治理基线（{DATE}）\n\n### 26.1 唯一规范入口\n\n- 人类可读总方案：`HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md`；\n- 机器事实源：`HOTT_Z_HIERARCHICAL_WBS_v2.json`；\n- 旧计划对照：`HOTT_Z_WBS_CROSSWALK_v2.md`；\n- 依赖图：`HOTT_Z_HIERARCHICAL_WBS_v2.mmd`；\n- 当前执行队列：`HOTT_Z_下一执行队列_v2.md`；\n- 阶段门：`HOTT_Z_阶段闸门与验收矩阵.md`；\n- 风险与红队：`HOTT_Z_风险与红队登记表.md`；\n- 完整性回执：`verification/hierarchical_wbs_v2_integrity.*`。\n\n任何旧 26-WP、14-WP 或 45-WP 计划均为 `SUPERSEDED_NONCANONICAL`。发生冲突时，只能以本节和 v2 机器注册表为准。\n\n### 26.2 三层编号制度\n\n- `AREA-00`–`AREA-13`：14 个 Program Areas，只用于学术分流；\n- 26 个稳定 `WP`：可验收、可阻塞、可交付的工作包；\n- 46 个 `TM`：细粒度任务模块。旧 45-WP 细计划全部转换为 `TM`，另补 `TM-635` 与 `TM-815` 作为 Paper C 组装模块。\n\n新工作不得创造第四套 WP 编号。任何行动先进入一个 TM，再汇总到其 parent WP。\n\n### 26.3 唯一关键路径\n\n```text\n{' → '.join(critical_path)}\n```\n\n中央 P0 是：锁定理论口径与 Z 核心，建立可复现证明助理环境，使 `no-canonical-earlier-event` 获得真实 E4 回执，再完成文献、红队和 Paper A。\n\n### 26.4 证据等级与阶段门\n\n证据等级固定为 E0–E7。E3 有限程序核验不得替代 E4 证明助理通过。阶段门固定为 G-00–G-07；未过 G-03 不得把 Paper A 标记为投稿就绪，未过 G-05 不得宣称“首次”“推翻”或归属于 HoTT 创建者。\n\n### 26.5 当前工具链事实\n\n当前环境未发现 `agda`、`lean`、`lake`、`coqc`、`rocq` 或 `rzk`。因此 WP-30 与 WP-31 是真实阻塞；在安装、版本锁定和 smoke test 前不得声称机器化。\n\n### 26.6 论文分流\n\n- Paper A：Z 因子化、单价无规范时间定向、群胚 core/时间反演和必要历史富化；\n- Paper B：provenance、intended role、语境、资源、成本和 witness；\n- Paper C：future stabilization、inhabitation synthesis 和 canonicalization；\n- Paper D：Lawvere/Gödel、反射、宇宙、resizing/predicativity，保持隔离；\n- 哲学伴随稿：Being/Becoming、Zeno、照片/电影/放映机，不承担形式证明。\n\n### 26.7 状态更新纪律\n\n1. WP/TM 状态变化必须更新 `HOTT_Z_HIERARCHICAL_WBS_v2.json`、`HOTT_Z_执行看板.md` 和 `RESEARCH_LOG.md`。\n2. 数学真理变化同步更新 Claim/Proof/Result 台账；文献变化同步更新 `LITERATURE_MAP.md`。\n3. 旧失败攻击只作负控制，不得重新进入主证明。\n4. 任何定理若被发现已知、错误或依赖更强假设，必须立即降级、收缩或拆分；不得隐藏。\n'''
agents_path.write_text(agents[:pos].rstrip() + canonical_agents_section, encoding='utf-8')

# Rewrite current index as a clean single-source index.
idx: list[str] = []
idx.append('# HOTT–Z 当前研究总索引')
idx.append('')
idx.append(f'**更新时间**：{DATE}  ')
idx.append('**当前阶段**：分层 WBS v2 已建立；进入理论剖面、Z core、工具链和首个机器定理的关键路径。  ')
idx.append('**规范边界**：研究目标是相对于时间、历史、语境、资源、见证和有效求解的表示/自然性/判定不完备；当前没有证明 `HoTT ⊢ ⊥`，也没有证明 HoTT 完全不能编码动态结构。')
idx.append('')
idx.append('## 1. 唯一项目入口')
idx.append('')
idx.append('1. `HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md` — 完整项目章程和 WBS。')
idx.append('2. `HOTT_Z_HIERARCHICAL_WBS_v2.json` — AREA/WP/TM、依赖、状态、闸门、风险和论文的机器事实源。')
idx.append('3. `HOTT_Z_下一执行队列_v2.md` — 当前 P0/P1 执行队列。')
idx.append('4. `HOTT_Z_WBS_CROSSWALK_v2.md` — 三套旧计划到 v2 的对照。')
idx.append('5. `HOTT_Z_HIERARCHICAL_WBS_v2.mmd` — 依赖图。')
idx.append('6. `HOTT_Z_阶段闸门与验收矩阵.md`、`HOTT_Z_风险与红队登记表.md`、`HOTT_Z_执行看板.md`。')
idx.append('')
idx.append('## 2. 数学与来源入口')
idx.append('')
idx.append('- `HOTT_Z_后续研究可用性总索引_第三轮.md`：逐来源可用内核、失败路线和 M1–M4 分类。')
idx.append('- `HOTT_Z_SOURCE_REGISTRY.json`：来源谱系、哈希、重复关系和反向 WP/TM 链接。')
idx.append('- `HOTT_Z_内生时间不完备性_论文草案_v3.md`：当前规范数学主稿。')
idx.append('- `HOTT_Z_内生时间不完备性_论文草案_v4_候选.md`：候选整合稿，尚未替代 v3。')
idx.append('- `Z_LAW_CANONICAL_FORM.md`、`HOTT_Z_无免费富化与历史约化定理.md`、`HOTT_Z_结构同一原则下的语义角色与操作不完备性定理.md`。')
idx.append('- `CLAIM_LEDGER.md`、`PROOF_ATTEMPTS.md`、`RESULTS.md`、`LITERATURE_MAP.md`、`RESEARCH_LOG.md`。')
idx.append('')
idx.append('## 3. 当前最稳固结论')
idx.append('')
idx.extend([
    '1. 抽象纤维内若目标真值变化，目标事实不能经该抽象无损因子化。',
    '2. 裸二事件类型在等价自然性下不存在免费规范的“较早事件”选择。',
    '3. 时间反演的过程可具有相同可逆 core，却在方向命题上真值相反。',
    '4. provenance、originality、intended role、context 和 operation cost 若被遗忘，就不能仅由裸结构恢复。',
    '5. 布尔断言、命题截断存在与具体 witness 是不同证据层；统一抽取需要额外选择结构。',
    '6. 某些时间轨道压成单一静态值并保持更新律时必须产生固定点；无固定点过程不能如此无损静态化。',
    '7. 在固定有效演算和明确归约下，未来稳定性、inhabitation synthesis 与 canonicalization 可出现不可总判定边界。',
])
idx.append('')
idx.append('## 4. 四种证明机制')
idx.append('')
for m in mechanisms[:4]: idx.append(f"- **{m['id']} {m['name']}**：{m['criterion']}")
idx.append('')
idx.append('## 5. 当前工作结构')
idx.append('')
idx.append(f'- 14 个 Program Areas；26 个规范 Work Packages；47 个 Task Modules；8 个阶段门；15 项活动风险。')
idx.append('- 关键路径：`' + ' → '.join(critical_path) + '`。')
idx.append('- 当前工具链不存在，WP-30/WP-31 阻塞；Paper A 不得提前升级。')
idx.append('')
idx.append('## 6. 下一执行批次')
idx.append('')
for q in immediate_queue[1:]: idx.append(f"- `{q['id']}` / `{q['work_package']}` / `{q['status']}`：{q['action']}")
idx.append('')
idx.append('## 7. 永久红队边界')
idx.append('')
idx.extend([
    '- ordinary `A→B` 可非可逆；主定理必须限定 identity/core 或明确遗忘映射。',
    '- directed、guarded、linear、clocked、cost-aware 富化是合法方案；它们说明新增结构承担区分工作。',
    '- axiomatic HoTT 与 cubical/computational variants 必须区分。',
    '- 一次性 transport、`Map(1,G)=ΩG`、同层全包 universe、宇宙角色相似、观察者维度、量子 successor 永久隔离。',
    '- AI 对话是思想谱系，不是数学或历史归属证据。',
])
idx.append('')
idx.append('## 8. 历史计划状态')
idx.append('')
for s in superseded_plans: idx.append(f"- `{s['file']}`：`SUPERSEDED_NONCANONICAL`；{s['role']}。")
idx.append('')
idx.append('## 9. 完整性状态')
idx.append('')
idx.append(f"- 分层 WBS 校验：`overall_ok = {str(validation['overall_ok']).lower()}`。")
idx.append('- 回执：`verification/hierarchical_wbs_v2_integrity.json` 与 `.txt`。')
idx.append('- 旧计划内容未删除，已备份并保留交叉索引；活动事实源只有 v2。')
(BASE / 'CURRENT_RESEARCH_INDEX.md').write_text('\n'.join(idx) + '\n', encoding='utf-8')

# Append research log.
log_path = BASE / 'RESEARCH_LOG.md'
log = log_path.read_text(encoding='utf-8')
entry = f'''\n\n## {DATE} — 三套竞争工作计划合并为分层 WBS v2\n\n### 发现的问题\n\n工作区同时存在 26-WP、14-WP 和 45-WP 三套自称规范的计划，且 `AGENTS.md` 与 `CURRENT_RESEARCH_INDEX.md` 同时指向不同入口。若继续执行，会造成 WP 编号碰撞、状态漂移和两个“单一事实源”。\n\n### 合并决策\n\n1. 14-WP 宏观计划转换为 `AREA-00`–`AREA-13`；\n2. 26-WP 计划保留为稳定 `WP`；\n3. 45-WP 细计划全部转换为 `TM`，并新增 `TM-815` 补齐 Paper C；\n4. 建立 8 个统一阶段门、15 项风险和唯一关键路径；\n5. 旧计划均标记 `SUPERSEDED_NONCANONICAL`，不删除历史内容；\n6. `AGENTS.md` 第 26 节和 `CURRENT_RESEARCH_INDEX.md` 重写为单一入口。\n\n### 当前事实\n\n- 14 Areas / 26 WPs / 46 TMs；\n- WP/TM 依赖图均无环；\n- Source/Claim/Proof/Result 引用完整；\n- 当前环境未发现 Agda、Lean、Rocq/Coq 或 Rzk，WP-30/WP-31 仍受工具链阻塞；\n- 完整性检查：`overall_ok = {str(validation['overall_ok']).lower()}`。\n\n### 新建/更新\n\n- `HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md`；\n- `HOTT_Z_HIERARCHICAL_WBS_v2.json`；\n- `HOTT_Z_WBS_CROSSWALK_v2.md`；\n- `HOTT_Z_HIERARCHICAL_WBS_v2.mmd`；\n- `HOTT_Z_下一执行队列_v2.md`；\n- `HOTT_Z_PROGRAM_BASELINE_v2.json`；\n- `verification/hierarchical_wbs_v2_integrity.*`；\n- `AGENTS.md`、`CURRENT_RESEARCH_INDEX.md`、`HOTT_Z_SOURCE_REGISTRY.json`、执行看板、阶段门和风险表。\n'''
log_path.write_text(log.rstrip() + entry + '\n', encoding='utf-8')

# Rewrite the canonical pointer to v2.
pointer = [
    '# HOTT–Z 规范工作计划指针', '',
    '**当前唯一活动版本**：分层 WBS v2  ',
    f'**生效日期**：{DATE}  ', '',
    '## 规范入口', '',
    '1. `HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md`；',
    '2. `HOTT_Z_HIERARCHICAL_WBS_v2.json`；',
    '3. `HOTT_Z_WBS_CROSSWALK_v2.md`；',
    '4. `HOTT_Z_HIERARCHICAL_WBS_v2.mmd`；',
    '5. `HOTT_Z_下一执行队列_v2.md`；',
    '6. `HOTT_Z_执行看板.md`、`HOTT_Z_阶段闸门与验收矩阵.md`、`HOTT_Z_风险与红队登记表.md`。', '',
    '## 层级', '',
    '- 14 个 `AREA`；',
    '- 26 个规范 `WP`；',
    '- 47 个 `TM`。', '',
    '旧 26-WP、14-WP 与 45-WP/v1.1 计划均为历史版本，不得再作为活动状态或编号事实源。',
]
(BASE / 'HOTT_Z_WORKPLAN_CANONICAL_POINTER.md').write_text('\n'.join(pointer) + '\n', encoding='utf-8')

# Final manifest and zip.
artifact_names = [
    'HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md',
    'HOTT_Z_HIERARCHICAL_WBS_v2.json',
    'HOTT_Z_WBS_CROSSWALK_v2.md',
    'HOTT_Z_HIERARCHICAL_WBS_v2.mmd',
    'HOTT_Z_下一执行队列_v2.md',
    'HOTT_Z_PROGRAM_BASELINE_v2.json',
    'HOTT_Z_执行看板.md',
    'HOTT_Z_阶段闸门与验收矩阵.md',
    'HOTT_Z_风险与红队登记表.md',
    'CURRENT_RESEARCH_INDEX.md',
    'AGENTS.md',
    'RESEARCH_LOG.md',
    'HOTT_Z_SOURCE_REGISTRY.json',
    'HOTT_Z_WORKPLAN_CANONICAL_POINTER.md',
    'verification/hierarchical_wbs_v2_integrity.json',
    'verification/hierarchical_wbs_v2_integrity.txt',
    '_build_hierarchical_wbs_v2.py',
]
manifest_lines = []
for name in artifact_names:
    p = BASE / name
    manifest_lines.append(f'{sha256(p)}  {name}')
manifest_path = BASE / 'HOTT_Z_WORKPLAN_V2_MANIFEST.sha256'
manifest_path.write_text('\n'.join(manifest_lines) + '\n', encoding='utf-8')
artifact_names.append(manifest_path.name)

zip_path = BASE / 'HOTT_Z_workplan_hierarchical_v2_20260831.zip'
with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
    for name in artifact_names:
        zf.write(BASE / name, arcname=name)

summary = {
    'overall_ok': validation['overall_ok'],
    'areas': len(areas), 'work_packages': len(canonical_wps), 'task_modules': len(modules),
    'gates': len(gates), 'risks': len(risks), 'papers': len(publication_portfolio),
    'zip': zip_path.name, 'zip_bytes': zip_path.stat().st_size, 'zip_sha256': sha256(zip_path),
    'main_plan_lines': len(main_plan_path.read_text(encoding='utf-8').splitlines()),
    'main_plan_bytes': main_plan_path.stat().st_size,
    'registry_bytes': registry_path.stat().st_size,
    'backup_dir': str(BACKUP),
}
print(json.dumps(summary, ensure_ascii=False, indent=2))
if not validation['overall_ok']:
    raise SystemExit(2)
