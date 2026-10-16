#!/usr/bin/env python3
"""Prepare the C0R9--C0R11 source-screen checkpoint without a core verdict."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".codex" / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import cognition_runtime as R
import projection_edit

SESSION_ID = "S-RES-20261005-ZFC-META-SUBTHEORY-C0R9-R11-SOURCE-SCREENS-001"
PREVIOUS = "S-GOV-20261005-ZFC-META-SUBTHEORY-C0R8-FINAL-RECEIPT-REBIND-001"

def sha(data: bytes) -> str: return hashlib.sha256(data).hexdigest()
def read(root: Path, rel: str) -> str: return (root / rel).read_text(encoding="utf-8")

def mutable(root: Path) -> list[str]:
    out=[]
    for rel in R.MUTABLE:
        if rel not in out: out.append(rel)
        index=R.parse_shard_index((root/rel).read_bytes(),rel)
        if index:
            for row in index['shards']:
                if row['path'] not in out: out.append(row['path'])
    return out

def prepend(text: str, marker: str, body: str) -> str:
    if marker in text: return text
    i=text.find('\n'); return text[:i+1]+body+text[i+1:]

def replace_row(text: str, ident: str, row: str) -> str:
    prefix=f"| `{ident}` |"; lines=text.splitlines(); hits=[i for i,x in enumerate(lines) if x.startswith(prefix)]
    if len(hits)!=1: raise SystemExit(f"ROW_COUNT:{ident}:{len(hits)}")
    lines[hits[0]]=row
    return '\n'.join(lines)+'\n'

def audit(root: Path) -> str:
    prior=read(root,f".codex/research/hott/sessions/{PREVIOUS}/CORE_COGNITION_AUDIT.md")
    prior=prior.replace(f"# CORE COGNITION AUDIT — {PREVIOUS}",f"# CORE COGNITION AUDIT — {SESSION_ID}",1)
    old="> **scope:** C0R8 final receipt rebinding. The proof inputs were byte-recaptured after documentation whitespace cleanup; this changes evidence locators/hashes only, not any source, theorem, or core verdict."
    new="> **scope:** C0R9--C0R11 source screens: ZFC-extension operational time, ZFC non-standard representability, and a shared bouncing-ball simulation-task candidate. No C1--C6 core contract or theorem is claimed."
    if old not in prior: raise SystemExit('AUDIT_SCOPE')
    prior=prior.replace(old,new,1)
    changes={
      "- direction_change: NO — C0R9 remains the current successor; this unit rebinds final proof receipts only。":"- direction_change: YES — C0R9/C0R10 provide comparative controls and C0R11 becomes the shared-consumer screen; no core verdict is released。",
      "- panorama_change: NO — C-375–C-378 and their source-to-spec classifications are unchanged。":"- panorama_change: YES — added source-level hybrid Zeno/operational and ZFC non-standard representability results; no new machine claim IDs。",
      "- update_decision: 将C0R8 record从pre-cleanup runs重绑到final `…-04` / `…-002` primary receipts，并保存新的registry/matrix/index hashes。":"- update_decision: write C0R9/C0R10/C0R11 source snapshots/cards, C0 manifest/successor, current projections and a new session record。",
      "- cross_conflicts: receipt rebinding occurs because exact source manifests are byte-sensitive; it is evidence hygiene, not an additional theoretical or philosophical argument。":"- cross_conflicts: a ZFC extension can supply an operational-time interface while ZFC itself can construct non-standard extension structures; neither fact alone assigns a bare-ZFC application duty. The Bliudze–Furic task is language semantics, not automatically the user's physical OriginDone。",
      "- unresolved: ZFC-specific M、fixed operational/process Q、actual P、FormalDone→OriginDone bridge、foundation adequacy role、SameQ_H0和C6仍未支付；receipt rebinding does not alter any of them。":"- unresolved: ZFC-specific M, shared standard/operational task bridge, actual P, FormalDone→OriginDone bridge, foundation adequacy role, SameQ_H0 and C6 remain unpaid。",
    }
    for a,b in changes.items():
        if a not in prior: raise SystemExit('AUDIT_LINE')
        prior=prior.replace(a,b,1)
    marker='## 本单元 source-first 对照'
    note="""## 本单元 source-first 对照

- Benveniste et al. 2012: ZFC extension + non-standard time supplies hybrid operational semantics;
- Kanovei--Lyubetskii 2007: ZFC can define an appropriate non-standard extension/BST structure;
- Bliudze--Furic 2014: standard-real-time bouncing-ball simulation reaches a source-defined Zeno semantic boundary; a non-standard operational repair provides a local continuation.

"""
    prior=prior.replace(marker,note,1)
    rows={
      'KC-000003': '| `KC-000003` | 连续分割/稠密时间的前提被放在真实hybrid Zeno source中审读；本轮保留它为模型假设，不宣称物理裁决。 | `DEEPENED` | Bliudze--Furic C0R11 card。 | source task仍非用户OriginDone。 |',
      'KC-000006': '| `KC-000006` | 时间问题分为密度、离散next、参数顺序、执行语义和physical bridge，不收窄为单一连续性口号。 | `DEEPENED` | C0R9--C0R11 cards。 | each layer needs separate payment。 |',
      'KC-000011': '| `KC-000011` | 程序的顺序/分支/循环视角在hybrid operational semantics获得真实消费者，而非仅作比喻。 | `DEEPENED` | Bliudze--Furic 2014。 | not bare-ZFC duty yet。 |',
      'KC-000012': '| `KC-000012` | ASK now has source-level analogue: whether a simulator remains within its alleged semantics past a Zeno point. | `DEEPENED` | C0R11 field card。 | user Q equivalence remains unpaid。 |',
      'KC-000013': '| `KC-000013` | theoretical utility/abstraction is source-visible: operational repair introduces explicit time structure; neither source makes a general ZFC conclusion. | `DEEPENED` | C0R9/C0R11. | no broad P conclusion。 |',
      'KC-000018': '| `KC-000018` | Time denial is not attributed to ZFC; the relevant question becomes who supplies/uses an operational time interface. | `CORRECTED` | C0R10 representability control。 | adequacy duty unpaid。 |',
      'KC-000044': '| `KC-000044` | Reality alignment is sharpened to source-defined model semantics; the source itself distinguishes idealised behavior from physical high fidelity. | `DEEPENED` | Bliudze--Furic controls。 | model task ≠ physical reality automatically。 |',
      'KC-000045': '| `KC-000045` | Theory economy is tested against explicit operational consequences rather than assumed from vocabulary. | `DEEPENED` | C0R9--C0R11. | shared foundation contract still absent。 |',
      'KC-000048': '| `KC-000048` | Targeted strategy now freezes common input/model/observation/Done before comparing standard and operational time semantics. | `DEEPENED` | C0 successor 011。 | no same task by label alone。 |',
      'KC-000054': '| `KC-000054` | A source-visible UR-like task exists inside the bouncing-ball language semantics; it is not yet the user’s full UR/Q. | `ALIGNED` | C0R11 card。 | same-Q bridge needed。 |',
      'KC-000059': '| `KC-000059` | P now has a real control case: standard-time Zeno execution vs an operational-time repair; ZFC-specific attribution remains blocked by C0R10. | `DEEPENED` | C0R9--C0R11. | do not transfer to bare ZFC。 |',
      'KC-000060': '| `KC-000060` | The obvious core location is a source-defined time model/semantic execution interface, not a diffuse search across set theory. | `ALIGNED` | C0R11 task card。 | M and adequacy still required。 |',
      'KC-000062': '| `KC-000062` | Pattern matching yielded the hybrid Zeno source; source pages and controls then restrict its conclusion. | `ALIGNED` | primary snapshots/cards。 | heuristic not proof。 |',
    }
    table_start=prior.index('| KC |'); head=prior[:table_start]; table=prior[table_start:]
    for ident,row in rows.items(): table=replace_row(table,ident,row).rstrip('\n')
    return head+table+'\n'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args();root=ROOT.resolve()
    plan=R.plan(root,profile='research')
    if (root/f'.codex/research/hott/sessions/{SESSION_ID}').exists():raise SystemExit('SESSION_EXISTS')
    texts={p:read(root,p) for p in mutable(root)}; state=json.loads(texts[R.STATE]); revision=state['revision']+1
    for index_rel in ('方向追踪.md','全景视野.md'):
        doc=projection_edit.load(root,index_rel)
        projection_edit.replace_in_index(doc,'source_state_revision: 311',f'source_state_revision: {revision}')
        projection_edit.replace_in_index(doc,'projection_generation: 20261005-zfc-mss-final-receipts-311',f'projection_generation: 20261005-zfc-c0r9-r11-{revision}')
        texts[index_rel]=doc['index_text'];texts.update(doc['shards'])
    ddoc=projection_edit.load(root,'方向追踪.md');dsh='方向追踪/002 - 治理与用户方向.md'
    old=next(x for x in ddoc['shards'][dsh].splitlines() if x.startswith('| `DIR-U-ZFC-META-SUBTHEORY-ADEQUACY` |'))
    new='| `DIR-U-ZFC-META-SUBTHEORY-ADEQUACY` | bare ZFC 或明确 ZFC-founded foundation context 对连续统／极限子理论的完成提升是否承担 bridge 审查责任；C0R9--C0R11以ZFC extension、ZFC non-standard representability和shared hybrid Zeno task校准该问题 | 研究发起人 2026-10-04 Goal；F-053；KC-000003、KC-000018、KC-000059 | `ACTIVE_CORE_RESEARCH / C0R11_SHARED_SIMULATION_TASK_CANDIDATE / BARE_ZFC_LINK_AND_ADEQUACY_UNPAID / C6_NOT_RELEASED` | `ZENO`、`RUSSELL`、`COMPUTATIONAL_LEGITIMACY`、`THEORY_ECONOMY` | `OUT-U-ZFC-MSS-REPRESENTATION-C375-C378`；`OUT-U-ZFC-HYBRID-ZENO-C0R9-R11` | C0R11 gives a shared language-level standard/operational task candidate; next only asks whether a source pays the same task and a bare-ZFC foundation bridge. | C0R9--C0R11 cards；F-053 |'
    projection_edit.replace_in_shard(ddoc,dsh,old,new);texts['方向追踪.md']=ddoc['index_text'];texts.update(ddoc['shards'])
    pdoc=projection_edit.load(root,'全景视野.md');psh='全景视野/003 - 当前机器证明包与原生重放.md'
    anchor=next(x for x in pdoc['shards'][psh].splitlines() if x.startswith('| `OUT-U-ZFC-MSS-REPRESENTATION-C375-C378` |'))
    row='| `OUT-U-ZFC-HYBRID-ZENO-C0R9-R11` | C0R9--C0R11 source screens: ZFC-extension hybrid operational time, ZFC non-standard representability, and Bliudze--Furic shared bouncing-ball simulation task | `DIR-U-ZFC-META-SUBTHEORY-ADEQUACY` | Benveniste et al. 2012; Kanovei--Lyubetskii 2007; Bliudze--Furic 2014 | `SOURCE_SUPPORTED_COMPARATIVE_CONTROLS / SHARED_SIMULATION_TASK_CANDIDATE / BARE_ZFC_LINK_UNPAID` | source distinguishes standard-real Zeno semantic boundary from non-standard operational repair; source also shows ZFC can define non-standard extension structures | not a bare-ZFC theorem, physical reality verdict, user Zeno/circle SameQ, or C6 result | C0R9--C0R11 cards and snapshots |'
    projection_edit.replace_in_shard(pdoc,psh,anchor,anchor+'\n'+row);texts['全景视野.md']=pdoc['index_text'];texts.update(pdoc['shards'])
    note='''### `C0R9`–`C0R11`：hybrid Zeno 与 bare-ZFC subtraction（2026-10-05）

Benveniste et al. provide a ZFC-extension operational-time control; Kanovei--Lyubetskii source pays ZFC non-standard representability; Bliudze--Furic provide a shared bouncing-ball standard-time / operational-repair semantic task. The remaining unpaid fields are bare-ZFC responsibility and same Q with the user’s physical task. Current successor: `C0-SUCCESSOR-RESELECTION-011`.

'''
    for rel in ('MEMORY/001 - 当前执行队列.md',R.PREFIX+'FRONTIER.md',R.PREFIX+'RESUME.md'):
        texts[rel]=prepend(texts[rel],'### `C0R9`–`C0R11`：hybrid Zeno 与 bare-ZFC subtraction（2026-10-05）',note)
    log='MEMORY/003 - 当前验证状态与顺序日志.md'
    if SESSION_ID not in texts[log]:texts[log]+=f'\n\n{SESSION_ID}：C0R9--C0R11 sources distinguish ZFC-extension operational time, ZFC non-standard representability, and a shared hybrid bouncing-ball task. No C6 result; successor C0R11.\n'
    sources=[
      'audit/ZFC-META-SUBTHEORY-ADEQUACY-001-C0-CANDIDATE-MANIFEST.md','audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0-SUCCESSOR-RESELECTION-009-TASKCARD.md','audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0-SUCCESSOR-RESELECTION-010-TASKCARD.md','audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0-SUCCESSOR-RESELECTION-011-TASKCARD.md','audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R9-HYBRID-NONSTANDARD-COMPARATIVE-CONTROL.md','audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R10-NSA-ZFC-SUBTRACTION-SCREEN.md','audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R11-BOUNCING-BALL-SHARED-CONSUMER-CANDIDATE.md','sources/external/zfc-meta-subtheory-c0r9-hybrid-nonstandard-20261005/README.md','sources/external/zfc-meta-subtheory-c0r10-kanovei-lyubetskii-2007-20261005/README.md','sources/external/zfc-meta-subtheory-c0r11-bliudze-furic-2014-20261005/README.md','认知闭包/ZFC-META-SUBTHEORY-ADEQUACY-001.md','dev-docs/ZFC元理论子理论充分性最终闭环SOP.md']
    state['revision']=revision;state['latest_session']=SESSION_ID;state['records'][SESSION_ID]={'depends_on':[],'evidence_status':'C0R9_R11_SOURCE_COMPARATIVE_CONTROLS_WITH_SCOPE / CORE_C6_NOT_RELEASED','full_sources':sources,'kind':'session','lifecycle_status':'HISTORICAL','path':f'.codex/research/hott/sessions/{SESSION_ID}/SESSION.md','path_mode':'document','related_records':[PREVIOUS],'scope':'Source-only C0R9--C0R11 screens distinguish a ZFC extension operational-time semantics, ZFC representability of non-standard universe, and a shared hybrid bouncing-ball simulation task. They do not establish bare-ZFC adequacy, user SameQ, physical OriginDone or C6.','source_hashes':{p:sha((root/p).read_bytes()) for p in sources},'status':'complete'}
    texts[R.STATE]=json.dumps(state,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
    base=f'.codex/research/hott/sessions/{SESSION_ID}/'
    texts[base+'SESSION.md']=f'''# {SESSION_ID}

> **Role:** `RESEARCH_GENERATION`.
> **Tier:** `T3` — C0R9--C0R11 source comparison; no core theorem.

## Result

- A ZFC extension supports an explicit hybrid operational-time interface.
- A ZFC source supports construction of non-standard extension structures.
- A shared bouncing-ball language task exhibits a standard-real Zeno semantic boundary and a non-standard local repair.

These facts leave bare-ZFC foundation adequacy and user-level same-Q unpaid. Next: C0R11 shared-consumer screen.
'''
    texts[base+'RUNS.json']=json.dumps({'next':'C0-SUCCESSOR-RESELECTION-011: establish or reject a shared standard/operational task and bare-ZFC bridge.','role':'RESEARCH_GENERATION','schema_version':'hott-research-runs/v1','session_id':SESSION_ID,'status':'C0R9_R11_SOURCE_CONTROLS_NO_C6','tier':'T3','verification':[{'command':'original PDF visual checks plus source snapshots','scope':'source identity and field cards','status':'PASS_WITH_SCOPE'}]},ensure_ascii=False,sort_keys=True,indent=2)+'\n'
    texts[base+'CORE_COGNITION_AUDIT.md']=audit(root)
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SESSION_ID,'authorization':'User authorized continued ZFC research, source acquisition, durable writeback, exact-path Git commits and push; this checkpoint preserves source controls without a core verdict.','load_profile':'research','task_ids':[],'files':[{'path':p,'expected_sha256':sha((root/p).read_bytes()) if (root/p).is_file() else None,'text':texts[p]} for p in sorted(texts)]}
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PREPARED','snapshot':plan['snapshot'],'revision':revision,'session_id':SESSION_ID,'files':len(payload['files'])},ensure_ascii=False))
if __name__=='__main__':main()
