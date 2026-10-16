from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import zipfile
from collections import Counter, defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/mnt/data')
ARCHIVE_ROOT = ROOT / 'archive' / 'superseded_workplans_20260831'
ARCHIVE_ROOT.mkdir(parents=True, exist_ok=True)

DATE = '2026-08-31'
REVISION = '1.1'


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def copy_preserve(src: Path, dst_dir: Path) -> None:
    if not src.exists():
        return
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / src.name
    if dst.exists():
        return
    if src.is_dir():
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)


def move_preserve(src: Path, dst_dir: Path) -> None:
    if not src.exists():
        return
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / src.name
    if dst.exists():
        if dst.is_dir():
            shutil.rmtree(dst)
        else:
            dst.unlink()
    shutil.move(str(src), str(dst))


# ---------------------------------------------------------------------------
# 1. Archive all noncanonical or superseded plans before mutation.
# ---------------------------------------------------------------------------
archive_45_v10 = ARCHIVE_ROOT / '45_wp_v1_0_pre_reconcile'
for rel in [
    'HOTT_Z_后续工作总方案与WBS_v1.md',
    'HOTT_Z_WBS_REGISTRY_v1.json',
    'HOTT_Z_WBS_DEPENDENCY_GRAPH_v1.mmd',
    'HOTT_Z_下一执行批次_P0P1.md',
    'HOTT_Z_WORKPLAN_V1_MANIFEST.sha256',
    'HOTT_Z_workplan_WBS_v1_20260831.zip',
    'verification/wbs_v1_integrity_check.txt',
    '_build_hott_z_workplan.py',
]:
    copy_preserve(ROOT / rel, archive_45_v10)

archive_26 = ARCHIVE_ROOT / '26_wp_plan_superseded'
for rel in [
    'HOTT_Z_后续工作总方案与工作包分解_v1.md',
    'HOTT_Z_WORK_PACKAGE_REGISTER.json',
    'HOTT_Z_WORK_PROGRAM_20260831',
    'HOTT_Z_WORK_PROGRAM_MANIFEST.sha256',
    'HOTT_Z_WORK_PROGRAM_ROOT.sha256',
    'HOTT_Z_work_program_20260831.zip',
    'verification/HOTT_Z_WBS_FINAL_VERIFICATION.json',
    'verification/HOTT_Z_WBS_FINAL_VERIFICATION.txt',
    'verification/wbs_plan_integrity.json',
]:
    move_preserve(ROOT / rel, archive_26)
# Board/gate/risk at root belonged to the 26-WP plan. Preserve copies, then overwrite.
for rel in ['HOTT_Z_执行看板.md', 'HOTT_Z_阶段闸门与验收矩阵.md', 'HOTT_Z_风险与红队登记表.md']:
    copy_preserve(ROOT / rel, archive_26)

archive_14 = ARCHIVE_ROOT / '14_wp_round4_plan_superseded'
for rel in [
    'HOTT_Z_后续工作总体方案与工作包分解_第四轮.md',
    'HOTT_Z_WORK_BREAKDOWN_STRUCTURE.json',
    'HOTT_Z_下一执行队列_第四轮.md',
    'hott_z_round4_workplan',
]:
    move_preserve(ROOT / rel, archive_14)

readme = ARCHIVE_ROOT / 'README.md'
readme.write_text(
    '''# Superseded HOTT–Z work plans\n\n'''
    '''This directory preserves earlier work-plan drafts for auditability. They are **not active execution baselines**.\n\n'''
    '''- `45_wp_v1_0_pre_reconcile/`: the first 45-package plan; superseded because it contained a dependency cycle (`WP-240 ↔ WP-440`) and a non-topological displayed critical path.\n'''
    '''- `26_wp_plan_superseded/`: an earlier 26-package program plan.\n'''
    '''- `14_wp_round4_plan_superseded/`: a later alternative 14-package draft that conflicted with the 45-package numbering.\n\n'''
    '''The sole active plan is declared in `/mnt/data/HOTT_Z_WORKPLAN_CANONICAL_POINTER.md`.\n''',
    encoding='utf-8',
)

# ---------------------------------------------------------------------------
# 2. Load and repair the 45-WP registry.
# ---------------------------------------------------------------------------
reg_path = ROOT / 'HOTT_Z_WBS_REGISTRY_v1.json'
if not reg_path.exists():
    archived = archive_45_v10 / reg_path.name
    if not archived.exists():
        raise FileNotFoundError('Cannot locate the 45-WP registry')
    shutil.copy2(archived, reg_path)
registry = json.loads(reg_path.read_text(encoding='utf-8'))
wp_map = {w['id']: w for w in registry['work_packages']}

# Dependency-cycle repair and publication dependency normalization.
wp_map['WP-440']['dependencies'] = ['WP-110', 'WP-700']
wp_map['WP-250']['dependencies'] = ['WP-110', 'WP-140', 'WP-210', 'WP-610', 'WP-230', 'WP-300', 'WP-700']
wp_map['WP-710']['dependencies'] = ['WP-700', 'WP-250']
wp_map['WP-730']['dependencies'] = ['WP-610', 'WP-700', 'WP-720', 'WP-800']
wp_map['WP-840']['dependencies'] = ['WP-020', 'WP-650', 'WP-800', 'WP-730']

critical_path = [
    'WP-000', 'WP-100', 'WP-110', 'WP-200', 'WP-210', 'WP-610',
    'WP-250', 'WP-710', 'WP-800', 'WP-730', 'WP-840'
]
registry['schema_version'] = 'hott_z_wbs.v1.1'
registry['revision'] = REVISION
registry['generated_at'] = DATE
registry['reconciled_at'] = datetime.now(timezone.utc).isoformat()
registry['canonical_plan'] = 'HOTT_Z_后续工作总方案与WBS_v1.md'
registry['critical_path'] = critical_path
registry['dependency_semantics'] = (
    'Dependencies are closure prerequisites for declaring a work package complete. '
    'Exploratory subtasks may begin earlier, but no package may pass its milestone while prerequisites remain open.'
)
registry['supersedes'] = [
    '45-WP WBS v1.0 (dependency cycle repaired)',
    '26-WP HOTT-Z-RP-20260831 plan',
    '14-WP HOTT-Z-R4 alternative plan',
]
registry['validation_warnings'] = []
reg_path.write_text(json.dumps(registry, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# ---------------------------------------------------------------------------
# 3. Repair the human-readable master plan in place and mark revision 1.1.
# ---------------------------------------------------------------------------
master_path = ROOT / 'HOTT_Z_后续工作总方案与WBS_v1.md'
if not master_path.exists():
    shutil.copy2(archive_45_v10 / master_path.name, master_path)
master = master_path.read_text(encoding='utf-8')
master = master.replace('（WBS v1.0）', '（WBS v1.1）', 1)
master = master.replace('**状态**：CANONICAL PROGRAM PLAN  ',
                        '**状态**：CANONICAL PROGRAM PLAN  \n**修订**：v1.1；修复依赖环、关键路径和多计划入口冲突。  ', 1)
old_path = (
    'WP-000 → WP-100 → WP-110 → WP-200 → WP-210 → WP-600 → WP-610\n'
    '       → WP-250 → WP-700 → WP-710 → WP-720 → WP-800 → WP-730 → WP-840'
)
new_path = (
    'WP-000 → WP-100 → WP-110 → WP-200 → WP-210 → WP-610\n'
    '       → WP-250 → WP-710 → WP-800 → WP-730 → WP-840'
)
master = master.replace(old_path, new_path)
replacements = {
    '- **依赖**：WP-110, WP-140, WP-210, WP-230, WP-300, WP-700':
        '- **依赖**：WP-110, WP-140, WP-210, WP-610, WP-230, WP-300, WP-700',
    '- **依赖**：WP-110, WP-240':
        '- **依赖**：WP-110, WP-700',
    '- **依赖**：WP-700, WP-250, WP-340':
        '- **依赖**：WP-700, WP-250',
    '- **依赖**：WP-610, WP-700, WP-720':
        '- **依赖**：WP-610, WP-700, WP-720, WP-800',
    '- **依赖**：WP-020, WP-650, WP-800':
        '- **依赖**：WP-020, WP-650, WP-800, WP-730',
}
for old, new in replacements.items():
    master = master.replace(old, new)
# Idempotence normalization for repeated executions.
master = re.sub(r'(?:\*\*修订\*\*：v1\.1；修复依赖环、关键路径和多计划入口冲突。  \n)+',
                '**修订**：v1.1；修复依赖环、关键路径和多计划入口冲突。  \n', master)
master = master.replace('WP-610, WP-700, WP-720, WP-800, WP-800', 'WP-610, WP-700, WP-720, WP-800')
master = master.replace('WP-020, WP-650, WP-800, WP-730, WP-730', 'WP-020, WP-650, WP-800, WP-730')
# Make every dependency line authoritative from the repaired registry.
for _wid, _wp in wp_map.items():
    _deps_text = ', '.join(_wp['dependencies']) if _wp['dependencies'] else '无'
    _pat = re.compile(rf'(^### {re.escape(_wid)}\s+—.*?^- \*\*依赖\*\*：)[^\n]+', re.M | re.S)
    master, _count = _pat.subn(lambda _m, _d=_deps_text: _m.group(1) + _d, master, count=1)
    if _count != 1:
        raise RuntimeError(f'Could not normalize dependency line for {_wid}')
# Insert reconciliation note before the first main section.
needle = '---\n\n## 0. 执行摘要'
recon_note = '''---\n\n## 版本治理说明\n\n- 本文件为唯一活动工作计划，工作包编号为 `WP-000`–`WP-840`，共 45 个。\n- 先前 26 包和 14 包方案，以及有依赖环的 45 包 v1.0，均已移入 `archive/superseded_workplans_20260831/`。\n- 依赖关系用于工作包完成闭包；允许提前探索，但不得在前置包未闭合时通过里程碑。\n- 规范指针见 `HOTT_Z_WORKPLAN_CANONICAL_POINTER.md`。\n\n---\n\n## 0. 执行摘要'''
if '## 版本治理说明' not in master:
    master = master.replace(needle, recon_note, 1)
master_path.write_text(master, encoding='utf-8')

# ---------------------------------------------------------------------------
# 4. Generate canonical graph, execution summary, board, gates, risks, crosswalk.
# ---------------------------------------------------------------------------

def node_name(wp_id: str) -> str:
    return wp_id.replace('-', '_')

mmd = ['flowchart TD']
for w in registry['work_packages']:
    label = f"{w['id']}\\n{w['title']}"
    mmd.append(f'  {node_name(w["id"])}["{label.replace(chr(34), chr(92)+chr(34))}"]')
for w in registry['work_packages']:
    for dep in w['dependencies']:
        mmd.append(f'  {node_name(dep)} --> {node_name(w["id"])}')
for ms in registry['milestones']:
    mn = node_name(ms['id'])
    mmd.append(f'  {mn}{{"{ms["id"]}\\n{ms["title"]}"}}')
    for dep in ms['dependencies']:
        mmd.append(f'  {node_name(dep)} -.-> {mn}')
status_class = {
    'ACTIVE': 'active', 'READY': 'ready', 'PAPER_PROVED': 'proved',
    'PAPER_PROVED_CONDITIONAL': 'proved', 'BASELINED': 'base',
    'BLOCKED': 'blocked', 'BACKGROUND': 'background', 'EXTERNAL_GATE': 'external',
    'PARKED': 'parked',
}
for w in registry['work_packages']:
    mmd.append(f'  class {node_name(w["id"])} {status_class.get(w["status"], "ready")}')
mmd.extend([
    '  classDef active stroke-width:3px;',
    '  classDef ready stroke-dasharray: 5 5;',
    '  classDef proved stroke-width:2px;',
    '  classDef base stroke-width:2px;',
    '  classDef blocked stroke-dasharray: 2 2;',
    '  classDef background stroke-dasharray: 8 4;',
    '  classDef external stroke-width:3px,stroke-dasharray: 4 3;',
    '  classDef parked stroke-dasharray: 1 4;',
])
graph_path = ROOT / 'HOTT_Z_WBS_DEPENDENCY_GRAPH_v1.mmd'
graph_path.write_text('\n'.join(mmd) + '\n', encoding='utf-8')

# Toolchain status is a current factual blocker.
tool_names = ['agda', 'lean', 'lake', 'coqc', 'rocq', 'rzk']
tool_status = {name: shutil.which(name) for name in tool_names}
installed = {k: v for k, v in tool_status.items() if v}

next_path = ROOT / 'HOTT_Z_下一执行批次_P0P1.md'
next_path.write_text(
    f'''# HOTT–Z 下一执行批次：P0/P1（WBS v{REVISION}）\n\n'''
    '''**依据**：`HOTT_Z_后续工作总方案与WBS_v1.md`  \n'''
    '''**原则**：在中央 proof-assistant 定理完成前，不扩写新的宏大判决。\n\n'''
    '''## A. P0 不可分散链\n\n'''
    '''1. **WP-000/WP-020**：关闭单一事实源与编号治理；运行规范计划完整性检查。\n'''
    '''2. **WP-600**：锁定 Agda-unimath；若不可用，则建立 Cubical Agda 自足后备。\n'''
    '''3. **WP-200**：把 `noSectionFromFixedPointFreeMonodromy` 对接实际库接口。\n'''
    '''4. **WP-210/WP-610**：实现并编译 `no-canonical-earlier-event`。\n'''
    '''5. **WP-650**：保存版本、commit、命令、stdout/stderr、退出码和依赖哈希。\n'''
    '''6. **WP-230/WP-300/WP-630**：至少完成一个与二事件无方向独立的 V4 实例。\n'''
    '''7. **WP-250**：在 V4 证书到达后冻结论文 I 的中央定理链。\n'''
    '''8. **WP-700/WP-710/WP-720**：完成最近工作矩阵、主张校准和两轮红队。\n'''
    '''9. **WP-800/WP-730/WP-840**：形成窄稿、外部复核与可复现发布包。\n\n'''
    '''## B. P1 独立证据\n\n'''
    '''- WP-220/WP-620：从“较早事件”推出严格时间序的无自然选择版本。\n'''
    '''- WP-230/WP-630：walking-arrow/core 的时间反演盲性。\n'''
    '''- WP-300/WP-630：`Snapshot := Unit`、`Provenance := Fin 2` 的最小历史反例。\n'''
    '''- WP-330/WP-630：从命题截断到具体 witness 的无全局恢复专门化。\n'''
    '''- WP-240：建立 directed/clocked/guarded 富化充分性矩阵。\n\n'''
    '''## C. 当前工具事实\n\n'''
    + (f"已发现工具：{installed}\n\n" if installed else
       '当前运行环境未发现 `agda`、`lean`、`lake`、`coqc`、`rocq` 或 `rzk` 可执行文件；WP-600 仍是机器化入口。\n\n')
    + '''## D. 退出条件\n\n'''
    '''- `no-canonical-earlier-event` 达到 V4；\n'''
    '''- 至少一个独立实例达到 V4；\n'''
    '''- 中央定理的 nearest-prior-art 矩阵完成；\n'''
    '''- G1–G7 可逐项回答；\n'''
    '''- 论文 I 明确不声称 `HoTT ⊢ ⊥`，也不声称 HoTT 完全不能编码时间。\n''',
    encoding='utf-8',
)

status_counts = Counter(w['status'] for w in registry['work_packages'])
stream_counts = Counter(w['stream'] for w in registry['work_packages'])
active_p0 = [w for w in registry['work_packages'] if w['priority'] == 'P0']
board_lines = [
    f'# HOTT–Z 执行看板（WBS v{REVISION}）', '',
    f'**基线日期**：{DATE}  ',
    f'**活动工作包**：{len(registry["work_packages"])}  ',
    f'**工作流**：{len(registry["streams"])}  ',
    f'**规范计划**：`{registry["canonical_plan"]}`  ',
    '', '## 1. 当前关键依赖脊柱', '', '```text',
    'WP-000 → WP-100 → WP-110 → WP-200 → WP-210 → WP-610',
    '       → WP-250 → WP-710 → WP-800 → WP-730 → WP-840',
    '```', '',
    '并行强制前置：`WP-600` 汇入 `WP-210/WP-610`；`WP-140/WP-230/WP-300/WP-700` 汇入 `WP-250`；`WP-630/WP-720` 汇入 `WP-800`；`WP-650` 汇入 `WP-840`。',
    '', '## 2. 状态分布', '', '| 状态 | 数量 |', '|---|---:|',
]
for st in registry['status_vocabulary']:
    board_lines.append(f'| {st} | {status_counts.get(st, 0)} |')
board_lines.extend(['', '## 3. P0 工作包', '', '| WP | 状态 | 标题 | 当前完成信号 |', '|---|---|---|---|'])
for w in active_p0:
    signal = '; '.join(w['acceptance_criteria'][:2])
    board_lines.append(f'| {w["id"]} | {w["status"]} | {w["title"]} | {signal} |')
board_lines.extend(['', '## 4. 工作流规模', '', '| 工作流 | WP 数 |', '|---|---:|'])
for stream in [s['name'] for s in registry['streams']]:
    board_lines.append(f'| {stream} | {stream_counts.get(stream, 0)} |')
board_lines.extend([
    '', '## 5. 当前唯一硬阻塞', '',
    '- 中央 HoTT 定理尚无真实 V4 编译证书；当前环境未发现主流证明助理可执行文件。',
    '- 论文 I 在 `WP-610`、`WP-630`、`WP-710`、`WP-720` 关闭前保持 `BLOCKED`。',
    '- 外部复核 `WP-730` 是发布前的独立闸门，不能由内部 AI 自审替代。',
    '', '## 6. 状态更新协议', '',
    '每次实质推进同时更新 `HOTT_Z_WBS_REGISTRY_v1.json`、`RESEARCH_LOG.md` 和相应 Claim/Proof/Result/Literature 台账；机器结果进入 `verification/`。',
])
(ROOT / 'HOTT_Z_执行看板.md').write_text('\n'.join(board_lines) + '\n', encoding='utf-8')

# Gate and milestone matrix.
gate_lines = [
    f'# HOTT–Z 阶段闸门与验收矩阵（WBS v{REVISION}）', '',
    '任何工作包不得仅凭篇幅、修辞强度、有限枚举或 AI 自审标记完成。', '',
    '## 1. 验证等级', '', '| 等级 | 名称 | 定义 |', '|---|---|---|',
]
for v in registry['verification_levels']:
    gate_lines.append(f'| {v["id"]} | {v["name"]} | {v["definition"]} |')
gate_lines.extend(['', '## 2. 决策门', '', '| Gate | 名称 | 核心问题 | 失败动作 |', '|---|---|---|---|'])
for g in registry['gates']:
    gate_lines.append(f'| {g["id"]} | {g["name"]} | {g["question"]} | {g["failure_action"]} |')
gate_lines.extend(['', '## 3. 里程碑', '', '| 里程碑 | 依赖 WP | 退出标准 | 解锁 |', '|---|---|---|---|'])
for ms in registry['milestones']:
    gate_lines.append(f'| {ms["id"]} {ms["title"]} | {", ".join(ms["dependencies"])} | {"；".join(ms["exit_criteria"])} | {"；".join(ms["unlocks"])} |')
gate_lines.extend([
    '', '## 4. 中央定理验收卡', '', '```yaml',
    'theorem_id:', 'work_package:', 'theory_profile:', 'object_theory:', 'metatheory:',
    'universe_assumptions:', 'source_domain_W:', 'representation_M:', 'forgetful_map_alpha:',
    'target_observable_or_proposition:', 'equality_or_equivalence_notions:', 'allowed_enrichment:',
    'claim_of_incompleteness:', 'proof_mechanism: M1|M2|M3|M4', 'paper_proof:',
    'formal_proof:', 'finite_checks:', 'prior_art:', 'strongest_counterargument:',
    'limitations:', 'status: V0|V1|V2|V3|V4|V5|V6', '```', '',
    '## 5. 论文 I 发布条件', '',
    '必须同时通过 G1–G7。至少一个 HoTT 特定中央定理达到 V4；至少一个独立实例达到 V4 或 V5；最近工作与所有重大异议均有可核对处置。',
])
(ROOT / 'HOTT_Z_阶段闸门与验收矩阵.md').write_text('\n'.join(gate_lines) + '\n', encoding='utf-8')

owners = {
    'RK-01': 'WP-700/WP-710', 'RK-02': 'WP-700/WP-720', 'RK-03': 'WP-210/WP-610',
    'RK-04': 'WP-100/WP-250', 'RK-05': 'WP-140/WP-240', 'RK-06': 'WP-600/WP-610',
    'RK-07': 'WP-650', 'RK-08': 'WP-510', 'RK-09': 'WP-320/WP-420',
    'RK-10': 'WP-450/WP-830', 'RK-11': 'WP-010', 'RK-12': 'WP-250/WP-800',
    'RK-13': 'WP-020', 'RK-14': 'WP-730/WP-840',
}
triggers = {
    'RK-01': '最近工作已有同等 no-section/因子化定理',
    'RK-02': '正文把强本体论解释归于创建者但无一手引文',
    'RK-03': '结果可在普通集合/群作用中一行证明且无 HoTT 专门化',
    'RK-04': '同一篇中混用方向、时长、时钟、稳定性等不同“时间”',
    'RK-05': '把可编码写成可由裸层内生恢复',
    'RK-06': '库 API、依赖版本或工具安装无法复现',
    'RK-07': 'Python 有限检查被标为形式证明',
    'RK-08': '从某一 HoTT 变体结论泛化到全部变体',
    'RK-09': '无输入编码和归约即援引停机问题',
    'RK-10': '从极限数学直接断言物理连续统错误',
    'RK-11': '多个 AI 摘录被当作独立事实证据',
    'RK-12': '主稿再次同时吸收时间、资源、LLM、Gödel 与 Zeno',
    'RK-13': '出现第二套活动 WP/Claim 编号或规范入口',
    'RK-14': '他人无法从空环境重建或复现',
}
risk_lines = [f'# HOTT–Z 风险与红队登记表（WBS v{REVISION}）', '', '| ID | 风险 | 严重度 | 触发信号 | 缓解措施 | Owner |', '|---|---|---|---|---|---|']
for r in registry['risks']:
    risk_lines.append(f'| {r["id"]} | {r["risk"]} | {r["severity"]} | {triggers.get(r["id"], "—")} | {r["mitigation"]} | {owners.get(r["id"], "—")} |')
risk_lines.extend(['', '任何高严重度风险触发后，相关论文工作包自动回退为 `BLOCKED`，直到在 `RESEARCH_LOG.md` 中记录处置。'])
(ROOT / 'HOTT_Z_风险与红队登记表.md').write_text('\n'.join(risk_lines) + '\n', encoding='utf-8')

# Human-readable traceability matrix.
trace_lines = [
    f'# HOTT–Z 工作包—来源—主张追踪矩阵（WBS v{REVISION}）', '',
    '本表由机器注册表生成。空引用表示治理、写作或外部审查工作包，不表示无依赖。', '',
    '| WP | 流 | 机制 | 状态 | 来源 | Claims | Proofs | Results | 依赖 | 目标产物 |',
    '|---|---|---|---|---|---|---|---|---|---|',
]
for w in registry['work_packages']:
    fmt = lambda xs: ', '.join(xs) if xs else '—'
    trace_lines.append(
        f'| {w["id"]} {w["title"]} | {w["stream"]} | {w["mechanism"]} | {w["status"]} | '
        f'{fmt(w["source_refs"])} | {fmt(w["claim_refs"])} | {fmt(w["proof_refs"])} | '
        f'{fmt(w["result_refs"])} | {fmt(w["dependencies"])} | {fmt(w["target_outputs"])} |'
    )
trace_path = ROOT / 'HOTT_Z_工作包—来源—主张追踪矩阵_v1_1.md'
trace_path.write_text('\n'.join(trace_lines) + '\n', encoding='utf-8')

summary_path = ROOT / 'HOTT_Z_后续工作执行摘要_规范版.md'
summary_path.write_text(
    f'''# HOTT–Z 后续工作执行摘要（WBS v{REVISION}）\n\n'''
    '''## 1. 研究任务\n\n'''
    '''建立 HoTT/单价基础相对于时间、历史、语境、资源、见证和有效求解目标的**目标相对不完备性理论**。研究对象不是 HoTT 的内部爆炸，而是：给定明确遗忘映射、目标真值域和自然性/有效性要求，哪些信息不能从裸表示免费恢复。\n\n'''
    '''## 2. 四类证明机制\n\n'''
    '''- M1：非因子化/不可定义；\n- M2：无截面/无自然选择；\n- M3：不可总判定/不可总合成；\n- M4：反射/元理论开放性。\n\n'''
    '''## 3. 九条工作流\n\n'''
    '''S0 治理；S1 Z 核心；S2 HoTT 时间；S3 历史语义；S4 操作有效性；S5 反射宇宙；S6 形式化；S7 文献红队；S8 写作发布。\n\n'''
    '''## 4. 当前关键路径\n\n'''
    '''```text\nWP-000 → WP-100 → WP-110 → WP-200 → WP-210 → WP-610\n       → WP-250 → WP-710 → WP-800 → WP-730 → WP-840\n```\n\n'''
    '''并行前置包括工具链 `WP-600`、群胚 core `WP-230`、历史反例 `WP-300`、机器实例 `WP-630`、文献检索 `WP-700`、内部红队 `WP-720` 和发布 CI `WP-650`。\n\n'''
    '''## 5. 论文组合\n\n'''
    '''1. **论文 I**：No-Free Temporal and Historical Enrichment in Univalent Foundations。\n'''
    '''2. **论文 II**：Signature-Relative Incompleteness: Context, Intent, Evidence, and Resource Regimes。\n'''
    '''3. **论文 III**：Reflection and Diagonalization in Univalent Type-Theoretic Foundations，仅在反射准入门通过后启动。\n'''
    '''4. **哲学稿**：Z 铁律、Being/Becoming、Zeno 与外延—操作完成。\n\n'''
    '''## 6. 当前 P0\n\n'''
    '''唯一不可分散目标是获得 `no-canonical-earlier-event` 的真实证明助理编译证书，并完成最近工作与红队审查。没有 V4 之前，论文 I 只能是纸笔技术报告。\n\n'''
    '''## 7. 非目标\n\n'''
    '''不宣称 `HoTT ⊢ ⊥`；不宣称 HoTT 完全不能编码时间；不把所有悖论归因于时间缺失；不把有限枚举冒充无界形式化；不把 AI 对话赞同当作数学证据。\n''',
    encoding='utf-8',
)

pointer_path = ROOT / 'HOTT_Z_WORKPLAN_CANONICAL_POINTER.md'
pointer_path.write_text(
    f'''# HOTT–Z 规范工作计划指针\n\n'''
    f'''**当前唯一活动版本**：WBS v{REVISION}（45 个工作包）  \n'''
    f'''**生效日期**：{DATE}  \n\n'''
    '''## 规范入口\n\n'''
    '''1. `HOTT_Z_后续工作总方案与WBS_v1.md` — 完整人类可读计划；\n'''
    '''2. `HOTT_Z_WBS_REGISTRY_v1.json` — 唯一机器注册表；\n'''
    '''3. `HOTT_Z_WBS_DEPENDENCY_GRAPH_v1.mmd` — 依赖图；\n'''
    '''4. `HOTT_Z_工作包—来源—主张追踪矩阵_v1_1.md` — 双向追踪；\n'''
    '''5. `HOTT_Z_执行看板.md` — 当前状态；\n'''
    '''6. `HOTT_Z_阶段闸门与验收矩阵.md` — 完成与发布条件；\n'''
    '''7. `HOTT_Z_风险与红队登记表.md` — 风险控制；\n'''
    '''8. `HOTT_Z_下一执行批次_P0P1.md` — 当前执行队列。\n\n'''
    '''## 已废弃计划\n\n'''
    '''26-WP、14-WP 和 45-WP v1.0 草案均位于 `archive/superseded_workplans_20260831/`，只供审计，不得作为活动编号或执行依据。\n''',
    encoding='utf-8',
)

# ---------------------------------------------------------------------------
# 5. Normalize AGENTS and CURRENT_RESEARCH_INDEX to one active plan.
# ---------------------------------------------------------------------------
agents_path = ROOT / 'AGENTS.md'
agents = agents_path.read_text(encoding='utf-8')
first_26 = re.search(r'\n## 26\.', agents)
if first_26:
    agents = agents[:first_26.start()].rstrip()
canonical_agents = f'''\n\n## 26. HOTT–Z 后续工作总方案与工作包治理（WBS v{REVISION}）\n\n### 26.1 唯一规范入口\n\n- `HOTT_Z_WORKPLAN_CANONICAL_POINTER.md`；\n- `HOTT_Z_后续工作总方案与WBS_v1.md`；\n- `HOTT_Z_WBS_REGISTRY_v1.json`；\n- `HOTT_Z_WBS_DEPENDENCY_GRAPH_v1.mmd`；\n- `HOTT_Z_工作包—来源—主张追踪矩阵_v1_1.md`；\n- `HOTT_Z_下一执行批次_P0P1.md`。\n\n26-WP、14-WP 与有依赖环的 45-WP v1.0 均已归档。任何冲突时，以规范指针和机器注册表为准。\n\n### 26.2 工作包纪律\n\n每项新任务必须归属唯一 `WP-xxx`，并在状态变化时同步更新机器注册表、研究日志和相关 Claim/Proof/Result/Literature 台账。不得创建第二套活动 WP 编号。\n\n### 26.3 关键依赖脊柱\n\n```text\nWP-000 → WP-100 → WP-110 → WP-200 → WP-210 → WP-610\n       → WP-250 → WP-710 → WP-800 → WP-730 → WP-840\n```\n\n并行前置：WP-600、WP-140、WP-230、WP-300、WP-630、WP-700、WP-720、WP-650。\n\n### 26.4 P0 与投稿纪律\n\n在 `no-canonical-earlier-event` 未达到 V4、最近工作矩阵和内部红队未完成前，不得把论文 I 标记为投稿就绪。论文 I 必须通过 G1–G7。\n\n### 26.5 分稿纪律\n\n- 论文 I：时间、历史、方向、单价无自然选择；\n- 论文 II：签名、语境、意图、证据、成本、资源和求解；\n- 论文 III：反射、Lawvere/Gödel、宇宙，独立且延后；\n- 哲学稿：Being/Becoming、Zeno、外延完成与操作完成。\n\n任何支线不得把另一支线尚未完成的命题当作已证前提。\n'''
agents_path.write_text(agents + canonical_agents, encoding='utf-8')

index_path = ROOT / 'CURRENT_RESEARCH_INDEX.md'
idx = index_path.read_text(encoding='utf-8')
idx = re.sub(
    r'\*\*当前阶段\*\*：.*',
    f'**当前阶段**：WBS v{REVISION} 已完成统一：45 个工作包、9 条工作流、8 个里程碑、7 个决策门；进入 WP-600/WP-610 的中央机器化路径。',
    idx,
    count=1,
)
# Rewrite the primary entry block.
start = idx.find('### 首要入口')
end = idx.find('### 源材料与机器索引')
if start != -1 and end != -1 and start < end:
    primary = '''### 首要入口\n\n1. `HOTT_Z_WORKPLAN_CANONICAL_POINTER.md`：唯一活动计划指针。\n2. `HOTT_Z_后续工作总方案与WBS_v1.md`：45 个工作包的完整方案。\n3. `HOTT_Z_WBS_REGISTRY_v1.json`：依赖、状态、验收、来源和主张映射的单一机器事实源。\n4. `HOTT_Z_工作包—来源—主张追踪矩阵_v1_1.md`：人类可读追踪矩阵。\n5. `HOTT_Z_执行看板.md`、`HOTT_Z_阶段闸门与验收矩阵.md`、`HOTT_Z_风险与红队登记表.md`：执行控制面。\n6. `HOTT_Z_下一执行批次_P0P1.md`：当前唯一任务队列。\n7. `HOTT_Z_后续研究可用性总索引_第三轮.md`：逐来源和逐问题研究索引。\n8. `HOTT_Z_内生时间不完备性_论文草案_v3.md`：当前规范数学主稿；v4 仍为候选。\n\n'''
    idx = idx[:start] + primary + idx[end:]
# Remove all old project-level sections and append one canonical section.
idx = re.sub(r'\n## 11\..*\Z', '', idx, flags=re.S).rstrip()
idx += f'''\n\n## 11. 项目级执行基线（WBS v{REVISION}）\n\n- 活动计划：45 个工作包，编号 `WP-000`–`WP-840`；\n- 工作流：S0–S8；\n- 里程碑：MS-0–MS-7；\n- 决策门：G1–G7；\n- 关键依赖脊柱：`WP-000 → WP-100 → WP-110 → WP-200 → WP-210 → WP-610 → WP-250 → WP-710 → WP-800 → WP-730 → WP-840`；\n- 当前唯一 P0：锁定证明助理环境并编译 `no-canonical-earlier-event`；\n- 当前规范主稿：`HOTT_Z_内生时间不完备性_论文草案_v3.md`；\n- 26-WP、14-WP 与 45-WP v1.0 方案均已归档，不再分配活动编号。\n\n## 12. 完整方案产物\n\n- 总方案：`HOTT_Z_后续工作总方案与WBS_v1.md`；\n- 执行摘要：`HOTT_Z_后续工作执行摘要_规范版.md`；\n- 机器注册表：`HOTT_Z_WBS_REGISTRY_v1.json`；\n- 依赖图：`HOTT_Z_WBS_DEPENDENCY_GRAPH_v1.mmd`；\n- 追踪矩阵：`HOTT_Z_工作包—来源—主张追踪矩阵_v1_1.md`；\n- 验证结果：`verification/wbs_v1_1_integrity_check.json`；\n- 完整包：`HOTT_Z_workplan_WBS_v1_1_20260831.zip`。\n'''
index_path.write_text(idx, encoding='utf-8')

log_path = ROOT / 'RESEARCH_LOG.md'
log = log_path.read_text(encoding='utf-8').rstrip()
entry_marker = '统一工作计划 v1.1：消除多计划冲突与依赖环'
if entry_marker not in log:
    log += f'''\n\n## {DATE} — {entry_marker}\n\n### 发现\n\n工作区同时存在 26-WP、14-WP 和 45-WP 三套活动入口。首版 45-WP 注册表还包含 `WP-240 ↔ WP-440` 的依赖环，且展示的“关键路径”不是依赖拓扑链。若不处理，后续状态、编号和验收将出现多重真相。\n\n### 处置\n\n1. 将 26-WP、14-WP 与 45-WP v1.0 原件移入 `archive/superseded_workplans_20260831/`；\n2. 保留 45 个工作包的细粒度结构，发布修订版 WBS v1.1；\n3. 打破 `WP-240/WP-440` 循环：WP-440 改依赖 WP-110/WP-700，WP-240 在此基础上综合富化边界；\n4. 令 WP-250 显式依赖 V4 核心 WP-610；令 WP-730 在论文 I 草稿 WP-800 后执行；令 WP-840 依赖外部复核 WP-730；\n5. 将关键依赖脊柱修正为真实的直接依赖链；\n6. 重写 AGENTS、CURRENT_RESEARCH_INDEX、执行看板、闸门和风险表，使其只指向一套规范计划；\n7. 新增工作包—来源—主张追踪矩阵和机器完整性验证。\n\n### 当前唯一 P0\n\nWP-600/WP-610：锁定工具链并取得 `no-canonical-earlier-event` 的真实 V4 编译证书。\n'''
log_path.write_text(log + '\n', encoding='utf-8')

# ---------------------------------------------------------------------------
# 6. Validate registry, links, ledgers, graph and canonical pointers.
# ---------------------------------------------------------------------------
registry = json.loads(reg_path.read_text(encoding='utf-8'))
wps = registry['work_packages']
ids = [w['id'] for w in wps]
id_set = set(ids)
issues: list[str] = []
if len(ids) != 45:
    issues.append(f'expected 45 work packages, found {len(ids)}')
if len(id_set) != len(ids):
    issues.append('duplicate WP IDs')
for w in wps:
    for dep in w['dependencies']:
        if dep not in id_set:
            issues.append(f'{w["id"]}: missing dependency {dep}')
    if w['status'] not in registry['status_vocabulary']:
        issues.append(f'{w["id"]}: invalid status {w["status"]}')

# Kahn DAG check and topological order.
indeg = {i: 0 for i in ids}
succ: dict[str, list[str]] = defaultdict(list)
for w in wps:
    for dep in w['dependencies']:
        indeg[w['id']] += 1
        succ[dep].append(w['id'])
q = deque(sorted(i for i, d in indeg.items() if d == 0))
topo: list[str] = []
while q:
    n = q.popleft()
    topo.append(n)
    for s in sorted(succ[n]):
        indeg[s] -= 1
        if indeg[s] == 0:
            q.append(s)
acyclic = len(topo) == len(ids)
if not acyclic:
    issues.append('dependency graph contains a cycle')

cp = registry['critical_path']
cp_direct = True
for a, b in zip(cp, cp[1:]):
    if a not in wp_map[b]['dependencies']:
        cp_direct = False
        issues.append(f'critical path edge {a} -> {b} is not a direct dependency')

# Parse active ledger IDs.
def parse_ids(path: Path, prefix: str) -> set[str]:
    text = path.read_text(encoding='utf-8')
    if prefix == 'Z':
        # CLAIM_LEDGER is a Markdown table; the active ID is its first column.
        return set(re.findall(r'(?m)^\|\s*(Z-\d+)\s*\|', text))
    return set(re.findall(rf'(?m)^##+\s+({re.escape(prefix)}-\d+)\b', text))
claim_ids = parse_ids(ROOT / 'CLAIM_LEDGER.md', 'Z')
proof_ids = parse_ids(ROOT / 'PROOF_ATTEMPTS.md', 'PA')
result_ids = parse_ids(ROOT / 'RESULTS.md', 'R')
for w in wps:
    for ref in w.get('claim_refs', []):
        if ref not in claim_ids:
            issues.append(f'{w["id"]}: missing claim ref {ref}')
    for ref in w.get('proof_refs', []):
        if ref not in proof_ids:
            issues.append(f'{w["id"]}: missing proof ref {ref}')
    for ref in w.get('result_refs', []):
        if ref not in result_ids:
            issues.append(f'{w["id"]}: missing result ref {ref}')

# Check that human-readable dependency lines agree with the registry.
master_text_for_validation = master_path.read_text(encoding='utf-8')
for w in wps:
    pat = re.compile(rf'^### {re.escape(w["id"])}\s+—.*?^- \*\*依赖\*\*：([^\n]+)', re.M | re.S)
    match = pat.search(master_text_for_validation)
    if not match:
        issues.append(f'{w["id"]}: dependency line missing from master plan')
        continue
    raw = match.group(1).strip()
    md_deps = [] if raw == '无' else [x.strip() for x in raw.split(',') if x.strip()]
    if md_deps != w['dependencies']:
        issues.append(f'{w["id"]}: master dependencies {md_deps} != registry {w["dependencies"]}')

source_registry = json.loads((ROOT / 'HOTT_Z_SOURCE_REGISTRY.json').read_text(encoding='utf-8'))
source_ids = {s['id'] for s in source_registry['sources']}
for w in wps:
    for ref in w.get('source_refs', []):
        if ref not in source_ids:
            issues.append(f'{w["id"]}: missing source ref {ref}')

required_files = [
    master_path, reg_path, graph_path, next_path,
    ROOT / 'HOTT_Z_执行看板.md', ROOT / 'HOTT_Z_阶段闸门与验收矩阵.md',
    ROOT / 'HOTT_Z_风险与红队登记表.md', trace_path, summary_path, pointer_path,
    agents_path, index_path, log_path,
]
for p in required_files:
    if not p.exists():
        issues.append(f'missing required file {p.name}')

# Ensure the active files do not contain control characters from accidental escape processing.
for p in [master_path, agents_path, index_path, next_path, summary_path]:
    text = p.read_text(encoding='utf-8')
    bad = [ord(ch) for ch in text if ord(ch) < 9 or 13 < ord(ch) < 32]
    if bad:
        issues.append(f'{p.name}: contains control characters {sorted(set(bad))}')

agents_text = agents_path.read_text(encoding='utf-8')
index_text = index_path.read_text(encoding='utf-8')
if len(re.findall(r'(?m)^## 26\.', agents_text)) != 1:
    issues.append('AGENTS.md does not contain exactly one active section 26')
if len(re.findall(r'(?m)^## 11\.', index_text)) != 1:
    issues.append('CURRENT_RESEARCH_INDEX.md does not contain exactly one section 11')
if 'HOTT_Z_WORKPLAN_CANONICAL_POINTER.md' not in agents_text or 'HOTT_Z_WORKPLAN_CANONICAL_POINTER.md' not in index_text:
    issues.append('canonical pointer missing from AGENTS or current index')

superseded_roots = [
    ROOT / 'HOTT_Z_后续工作总方案与工作包分解_v1.md',
    ROOT / 'HOTT_Z_WORK_PACKAGE_REGISTER.json',
    ROOT / 'HOTT_Z_后续工作总体方案与工作包分解_第四轮.md',
    ROOT / 'HOTT_Z_WORK_BREAKDOWN_STRUCTURE.json',
    ROOT / 'hott_z_round4_workplan',
]
for p in superseded_roots:
    if p.exists():
        issues.append(f'superseded plan remains active at root: {p.name}')

validation = {
    'schema_version': 'hott_z_wbs_validation.v1.1',
    'date': DATE,
    'overall_ok': not issues,
    'issues': issues,
    'work_package_count': len(ids),
    'unique_work_package_ids': len(id_set),
    'dependency_graph_acyclic': acyclic,
    'topological_order_count': len(topo),
    'critical_path': cp,
    'critical_path_direct_dependency_chain': cp_direct,
    'source_reference_count': sum(len(w.get('source_refs', [])) for w in wps),
    'claim_reference_count': sum(len(w.get('claim_refs', [])) for w in wps),
    'proof_reference_count': sum(len(w.get('proof_refs', [])) for w in wps),
    'result_reference_count': sum(len(w.get('result_refs', [])) for w in wps),
    'milestone_count': len(registry['milestones']),
    'gate_count': len(registry['gates']),
    'risk_count': len(registry['risks']),
    'toolchain_detection': tool_status,
    'archive_root': str(ARCHIVE_ROOT.relative_to(ROOT)),
}
verification_dir = ROOT / 'verification'
verification_dir.mkdir(exist_ok=True)
validation_json = verification_dir / 'wbs_v1_1_integrity_check.json'
validation_txt = verification_dir / 'wbs_v1_1_integrity_check.txt'
validation_json.write_text(json.dumps(validation, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
validation_txt.write_text(
    '\n'.join([
        'HOTT-Z WBS v1.1 integrity check',
        f'date={DATE}',
        f'overall_ok={str(not issues).lower()}',
        f'work_packages={len(ids)} unique={len(id_set)}',
        f'dependency_graph_acyclic={str(acyclic).lower()}',
        f'critical_path_direct_dependency_chain={str(cp_direct).lower()}',
        f'milestones={len(registry["milestones"])} gates={len(registry["gates"])} risks={len(registry["risks"])}',
        f'issues={len(issues)}',
        *[f'ISSUE {x}' for x in issues],
    ]) + '\n',
    encoding='utf-8',
)
# Stable alias for callers expecting the old report filename.
(ROOT / 'verification' / 'wbs_v1_integrity_check.txt').write_text(validation_txt.read_text(encoding='utf-8'), encoding='utf-8')

# ---------------------------------------------------------------------------
# 7. Manifest and reproducible work-plan bundle.
# ---------------------------------------------------------------------------
package_files = [
    pointer_path, summary_path, master_path, reg_path, graph_path, trace_path,
    next_path, ROOT / 'HOTT_Z_执行看板.md', ROOT / 'HOTT_Z_阶段闸门与验收矩阵.md',
    ROOT / 'HOTT_Z_风险与红队登记表.md', agents_path, index_path, log_path,
    ROOT / 'HOTT_Z_SOURCE_REGISTRY.json', ROOT / 'HOTT_Z_后续研究可用性总索引_第三轮.md',
    validation_json, validation_txt, readme,
    ROOT / 'CLAIM_LEDGER.md', ROOT / 'PROOF_ATTEMPTS.md', ROOT / 'RESULTS.md', ROOT / 'LITERATURE_MAP.md',
    ROOT / 'tools' / 'reconcile_hott_z_workplan_v1_1.py',
]
manifest_path = ROOT / 'HOTT_Z_WORKPLAN_V1_1_MANIFEST.sha256'
manifest_lines = [f'{sha256(p)}  {p.relative_to(ROOT)}' for p in package_files]
manifest_path.write_text('\n'.join(manifest_lines) + '\n', encoding='utf-8')
# Stable alias now points to current canonical content.
(ROOT / 'HOTT_Z_WORKPLAN_V1_MANIFEST.sha256').write_text(manifest_path.read_text(encoding='utf-8'), encoding='utf-8')
package_files.append(manifest_path)

zip_path = ROOT / 'HOTT_Z_workplan_WBS_v1_1_20260831.zip'
with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
    for p in package_files:
        zf.write(p, arcname=str(p.relative_to(ROOT)))
# Stable alias for old outward-facing name.
stable_zip = ROOT / 'HOTT_Z_workplan_WBS_v1_20260831.zip'
shutil.copy2(zip_path, stable_zip)
zip_hash_path = ROOT / 'HOTT_Z_workplan_WBS_v1_1_20260831.zip.sha256'
zip_hash_path.write_text(f'{sha256(zip_path)}  {zip_path.name}\n', encoding='utf-8')

if issues:
    print(json.dumps(validation, ensure_ascii=False, indent=2))
    raise SystemExit(1)

print('canonical_revision', REVISION)
print('work_packages', len(ids))
print('dependency_graph_acyclic', acyclic)
print('critical_path_direct', cp_direct)
print('archive', ARCHIVE_ROOT)
print('zip', zip_path, sha256(zip_path))
print('validation', validation_json)
