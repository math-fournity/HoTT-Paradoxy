#!/usr/bin/env python3
"""Prepare the B01 transaction once; only cognition_runtime applies owners."""
from pathlib import Path
import hashlib, json, re, subprocess, sys
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / '.codex/tools'))
sys.path.insert(0, str(ROOT / 'scripts/audit'))
import cognition_runtime as cr
import projection_edit as pe
C = '第三轮机器统观/Session-C/'
SID = 'S-RES-20260924-MO3-C-B01'
PREV = 'S-RES-20260924-MO3-C-R0-READY'
TASK = 'MO3-COVERAGE-C'
BASE = '5a4ab25fb106d0f82b5268f42cc7038d0ed953f3'

def sha(b): return hashlib.sha256(b).hexdigest()
def replace_once(s, a, b):
    assert s.count(a) == 1, ('replace_count', a[:80], s.count(a))
    return s.replace(a, b, 1)
def exclusive(p, data):
    with p.open('xb') as f: f.write(cr.dump(data))

def main():
    assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip() == BASE
    assert not subprocess.check_output(['git','diff','--cached','--name-only'],cwd=ROOT)
    s = json.loads((ROOT / cr.STATE).read_text())
    assert s['revision'] == 286 and s['latest_session'] == PREV and SID not in s['records']
    tx = json.loads((ROOT / f'.codex/cognition/checkpoints/{PREV}/transaction.json').read_text())
    assert all(sha((ROOT / r['path']).read_bytes()) == r['new_sha256'] for r in tx['rows'])
    assert not (ROOT / cr.PREFIX / 'sessions' / SID).exists()
    p = cr.plan(ROOT, profile='research', task_ids=[TASK])
    out = ROOT / C / '证据/B01'
    # Byte qualification does not certify reading/understanding. Actual ranges
    # are the source of the separate human execution record.
    initial = json.loads((ROOT / C / '证据/R0/INPUT-IDENTITY.json').read_text())['four_set']
    current_hashes = {r['path']:r['new_sha256'] for r in tx['rows']}
    four = []
    for r in initial:
        actual = sha((ROOT / r['path']).read_bytes())
        expected = current_hashes.get(r['path'], r['sha256'])
        four.append({'path':r['path'],'actual':actual,'expected':expected,'match':actual==expected})
    assert all(r['match'] for r in four)
    source = []
    for f in ['preliminaries.tex','formal.tex']:
        rel = 'HoTT/theory-schema/upstream/book-578b85cc/' + f
        b = (ROOT / rel).read_bytes()
        source.append({'path':rel,'sha256':sha(b),'bytes':len(b),'lines':len(b.splitlines()),
                       'this_unit_read_ranges':[[1,2044]] if f=='preliminaries.tex' else [[1,974]],
                       'read_claim_owner':C+'执行记录/002 - Book第一章与附录基础接口首遍.md'})
    receipt = {'status':'INPUT_IDENTITIES_MATCH','base_head':BASE,'base_revision':286,
               'four_set':four,'source':source,'kernel_replayed':False,
               'model_understanding':'NOT_CERTIFIED_BY_TOOL'}
    exclusive(out / 'INPUT-IDENTITY.json', receipt)
    docs = {x:pe.load(ROOT,x) for x in ('MEMORY.md',cr.DIRECTION,cr.PANORAMA,cr.ESSAY)}
    texts = {x:(ROOT/x).read_text() for x in cr.MUTABLE if x not in docs}
    m = 'MEMORY/001 - 当前执行队列.md'
    old = next(l for l in docs['MEMORY.md']['shards'][m].splitlines() if l.startswith('当前用户启动Goal7'))
    current = ('当前执行Goal7 / MO3-COVERAGE-C，C为唯一续做研究integrator。已完成R0精确复用及Book第一章/附录基础接口来源首遍：十二编号节、Notes/16练习、A00–A02和C01–09/C11基础规则有语义处置；REVIEWED不等机器证明。C-BASE-01与旧上下文/库存来源边界重合，不新写同义proof；C-BASE-02表示/计算接口为已接受待核义务，连接Book2的Π/Σ/funext及Book5.5。下一Book2全章与该接口，先重读最高指示和KC47/48并公开生成。其它Book、附录后段、D/S/E及内部路线仍未完成；父范围PARENT_SCOPE_INCOMPLETE，命中未定，无C seal，D未审。旧A只读，四包精确复用不继承整体完成；无新kernel run。当前版本/事务以STATE及canonical result为准。')
    pe.replace_in_shard(docs['MEMORY.md'],m,old,current)
    pe.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：Book1/基础附录来源语义首遍及双向映射；C-BASE-01来源重复、C-BASE-02计算接口待核；无新kernel或父范围完成，reflection=no-plan-change；revision287。\n')
    for rel in (cr.PREFIX+'FRONTIER.md',cr.PREFIX+'RESUME.md'):
        texts[rel]=replace_once(texts[rel],old,current)
    for rel in (cr.DIRECTION,cr.PANORAMA):
        word='direction' if rel==cr.DIRECTION else 'outcome'
        pe.replace_in_index(docs[rel],'source_state_revision: 286','source_state_revision: 287')
        pe.replace_in_index(docs[rel],f'projection_generation: 20260924-{word}-286',f'projection_generation: 20260924-{word}-287')
    ds='方向追踪/002 - 治理与用户方向.md'
    line=next(x for x in docs[cr.DIRECTION]['shards'][ds].splitlines() if x.startswith('| `DIR-U-MO3-COVERAGE-C`'))
    new=line.replace('`OUT-MO3-C-R0`','`OUT-MO3-C-R0`, `OUT-MO3-C-B01`').replace('从固定父范围逐项实审、精确复用与独立充分性挑战','Book1基础首遍后继续Book2及C-BASE-02；其余父范围/独立充分性挑战未完')
    pe.replace_in_shard(docs[cr.DIRECTION],ds,line,new)
    ps='全景视野/002 - 治理、门禁与骨架结果.md'
    pe.append_to_shard(docs[cr.PANORAMA],ps,'| `OUT-MO3-C-B01` | C的Book1与附录基础接口语义首遍 | `DIR-U-MO3-COVERAGE-C` | 固定Book全章2044行、formal基础规则、逐项/双向映射及候选查重 | `SOURCE_REVIEW / PARENT_SCOPE_INCOMPLETE` | C-BASE-01为来源边界重复；C-BASE-02编码/计算接口义务已接受未执行 | source审查不冒机器证明；余章/扩展/整体充分性未完；无新kernel | 第三轮机器统观/Session-C/父范围与覆盖/004 - Book基础接口的语义处置.md；第三轮机器统观/Session-C/审计/B01/CORE_COGNITION_AUDIT.md |\n')
    next_action = 'R1/R2：Book第2章全章来源首遍，按真实消费者组织路径/Σ/Π/funext等；承接C-BASE-02表示替换与判断/命题计算接口，连接Book5.5后执行相称核证。新理论单元先全文重读最高指示、KC47/48及公开生成。其它父范围与C-BASE-02未关闭，不复活旧W或票据同义proof。'
    s['revision']=287;s['latest_session']=SID
    s['execution_control'].update(last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',next_minimal_verification=next_action,app_goal_status_observed='paused_at_resume_query; user explicitly continued; no resume tool mutation',app_goal_completion_eligible=False)
    for rid,word in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:
        s['records'][rid]['projection_generation']=f'20260924-{word}-287'
        s['records'][rid]['scope']='Goal7 C source review increment through Book1/basic appendix, parent scope incomplete; no new kernel run.'
    r=s['records'][TASK];r['execution_control']['next_minimal_verification']=next_action
    additions=[C+'执行记录.md',C+'执行记录/002 - Book第一章与附录基础接口首遍.md',C+'父范围与覆盖/004 - Book基础接口的语义处置.md',C+'过程与结果/002 - 基础判断与可重复使用的对象.md',C+'审计/B01/CORE_COGNITION_AUDIT.md',C+'证据/B01/INPUT-IDENTITY.json']
    additions += [str(f.relative_to(ROOT)) for f in sorted((ROOT/C/'审计/B01/CORE_COGNITION_AUDIT').glob('*.md'))]
    r['full_sources']=list(dict.fromkeys(r['full_sources']+additions))
    r['source_hashes']={x:sha((ROOT/x).read_bytes()) for x in r['full_sources']}
    r['revalidation']='Actual Book1/basic appendix semantic review and new C-BASE-02 obligation; refreshed own modified owner pins. No parent-completion or mathematical upgrade.'
    sb=cr.PREFIX+'sessions/'+SID+'/'
    s['records'][SID]={'kind':'session','path':sb+'SESSION.md','lifecycle_status':'HISTORICAL','status':'complete_with_scope','evidence_status':'BOOK1_BASIC_APPENDIX_SOURCE_REVIEW_WITH_OPEN_INTERFACE','depends_on':[],'related_records':[TASK,PREV],'full_sources':[sb+x for x in cr.SESSION_REQUIRED_FILES],'source_hashes':{},'scope':'Source review unit only; C-BASE-02 and parent research remain incomplete.'}
    texts[cr.STATE]=cr.dump(s).decode()
    ar=ROOT/C/'审计/B01/CORE_COGNITION_AUDIT'
    blocks=re.split(r'^### (KC-\d{6})\n',(ar/'001 - 核心认知逐项回评.md').read_text(),flags=re.M)
    legacy=f'# {SID} 完整兼容审计\n\ncore-cognition-generation-8；48 KC。完整人审分片为{C}审计/B01/CORE_COGNITION_AUDIT.md；嵌套writer缺口G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001未修。\n\ncore_change: NO\ndirection_change: YES\npanorama_change: YES\nessay_change: NO\nupdate_decision: Book1 source review and open C-BASE-02; parent incomplete\ncross_conflicts: source versus machine proof kept distinct\nunresolved: remaining parent scope and actual encoding consumer verification\n\n|KC ID|姿态|relation|assessment and evidence|next and falsifier|\n|---|---|---|---|---|\n'
    for i in range(1,len(blocks),2):
        kid,b=blocks[i:i+2];fields={}
        for l in b.splitlines():
            if l.startswith('- ') and ': ' in l:
                k,v=l[2:].split(': ',1);fields[k]=v
        legacy+=f"| `{kid}` | {fields['工作姿态']} | {fields['relation']} | {fields['实际证据与关系理由']} | {fields['下一选择及反证条件']} |\n"
    assert len(cr._audit_v1_kc_rows(legacy))==48
    essay=(ar/'002 - 阐释消费与航向反思.md').read_text()
    legacy+='\n'+essay[essay.index('# 阐释消费与航向反思'):]
    session=f'# {SID}\n\n研究对象为固定Book1/基础附录；来源语义首遍与候选归因，非新数学证明。\n\n- host: Codex desktop\n- model: Astra（用户选择，未认证后端）\n- tier: T3\n- role: RESEARCH_GENERATION / sole integrator\n- load_receipt: {C}执行记录/002 - Book第一章与附录基础接口首遍.md；snapshot {p["snapshot"]}\n- parent: PARENT_SCOPE_INCOMPLETE\n- reflection: no-plan-change\n\n精确成果及完整来源行见{C}父范围与覆盖/004 - Book基础接口的语义处置.md。C-BASE-01查重停来源边界；C-BASE-02新研究义务待执行。\n\n下一：{next_action}\n\n|element_usage|用途及边界|\n|---|---|\n|最高指示/core|实际重读、14题/三呈现/迁移及48KC回评|\n|原典/Schema|来源到处置双向映射，SOURCE非新证明|\n|SOP|本章广度增量后回父范围，no-plan-change|\n|canonical writer|本SID唯一事务，分片writer缺口保持|\n|Git|仅C自有路径和受控owner，不混其他dirty|\n\nT01–05目标未改；T06–12无业务演算/配置/schema改动；T13–17增加来源/范围证据，无新kernel；T18–21无部署外发；T22–24更新C当前进度；T25不改治理；T26精确本地提交。宿主状态查询曾为paused，用户继续授权已生效，不伪称已工具恢复。\n'
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'kernel_runs':[],'status':'SOURCE_REVIEW_ONLY','evidence':[C+'证据/B01/INPUT-IDENTITY.json',C+'父范围与覆盖/004 - Book基础接口的语义处置.md'],'parent_coverage':'PARENT_SCOPE_INCOMPLETE'}
    files=[]
    for d in docs.values():files+=pe.payload_rows(d,ROOT)
    for rel,t in texts.items():files.append({'path':rel,'expected_sha256':sha((ROOT/rel).read_bytes()),'text':t})
    for name,t in [('SESSION.md',session),('CORE_COGNITION_AUDIT.md',legacy),('RUNS.json',cr.dump(runs).decode())]:files.append({'path':sb+name,'expected_sha256':None,'text':t})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':[TASK],'authorization':'User Goal7 sole C integrator and explicit continue; exact own source review/current-owner update, preserve A/D/sources and unrelated dirty.','files':files}
    exclusive(out/'checkpoint-payload.json',payload)
    print(json.dumps({'snapshot':p['snapshot'],'payload':str((out/'checkpoint-payload.json').relative_to(ROOT)),'proposed_revision':287,'state_applied':False},ensure_ascii=False))

if __name__=='__main__':main()
