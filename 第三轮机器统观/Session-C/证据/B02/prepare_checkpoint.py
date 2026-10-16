#!/usr/bin/env python3
"""Prepare this B02 owner transaction; canonical runtime performs all writes."""
from pathlib import Path
import json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'.codex/tools'));sys.path.insert(0,str(ROOT/'scripts/audit'))
import cognition_runtime as cr
import projection_edit as pe
C='第三轮机器统观/Session-C/';TASK='MO3-COVERAGE-C'
SID='S-RES-20260924-MO3-C-B02';PREV='S-RES-20260924-MO3-C-B01-ALIGN'
def main():
 assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()=='e9ad36a7bc66b4fee4f190307b845a8526d789d4'
 assert not subprocess.check_output(['git','diff','--cached','--name-only'],cwd=ROOT)
 s=json.loads((ROOT/cr.STATE).read_text());assert s['revision']==288 and s['latest_session']==PREV and SID not in s['records']
 tx=json.loads((ROOT/f'.codex/cognition/checkpoints/{PREV}/transaction.json').read_text())
 assert all(cr.sha((ROOT/x['path']).read_bytes())==x['new_sha256'] for x in tx['rows'])
 plan=cr.plan(ROOT,profile='research',task_ids=[TASK]);docs={p:pe.load(ROOT,p) for p in ('MEMORY.md',cr.DIRECTION,cr.PANORAMA,cr.ESSAY)}
 texts={p:(ROOT/p).read_text() for p in cr.MUTABLE if p not in docs}
 m='MEMORY/001 - 当前执行队列.md';old=next(l for l in docs['MEMORY.md']['shards'][m].splitlines() if l.startswith('当前执行Goal7 / MO3-COVERAGE-C'))
 current='当前执行Goal7 / MO3-COVERAGE-C，C为唯一续做研究integrator。Book1/2、基础附录及Book5.5已有来源语义处置，具体条目从Session-C父范围owner读取；原典读取不等新机器证明。C342–343的Bool函数编码积条件依赖β/原始pair与直接投影控制已原生核证，primary02与NEG02、矩阵/registry及e9ad36a精确Git关系保全；无合格现实相对命中。C-BASE-02更宽iterator/W-Nat/相干及Cubical接口仍待处理，不能由小包代全部义务。下一Book3全章，先最高指示全文、KC47/48和公开生成；其余Book/扩展/模型/父充分性未完成。父范围PARENT_SCOPE_INCOMPLETE，整体命中未定，无C最终seal，D未审；旧A及四包原件只读。当前事务/revision回STATE与canonical result。'
 pe.replace_in_shard(docs['MEMORY.md'],m,old,current)
 pe.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：Book2/5.5 SOURCE审查及C342–343精确native子包；NEG02拒绝裸refl、投影控制保同题，父范围未完成。更宽计算义务保留，下一Book3；reflection=no-plan-change，revision289。\n')
 for p in (cr.PREFIX+'FRONTIER.md',cr.PREFIX+'RESUME.md'):
  assert texts[p].count(old)==1;texts[p]=texts[p].replace(old,current,1)
 for p in (cr.DIRECTION,cr.PANORAMA):
  w='direction' if p==cr.DIRECTION else 'outcome'
  pe.replace_in_index(docs[p],'source_state_revision: 288','source_state_revision: 289')
  pe.replace_in_index(docs[p],f'projection_generation: 20260924-{w}-288',f'projection_generation: 20260924-{w}-289')
 ds='方向追踪/002 - 治理与用户方向.md'
 oldrow=next(l for l in docs[cr.DIRECTION]['shards'][ds].splitlines() if l.startswith('| `DIR-U-MO3-COVERAGE-C`'))
 newrow=oldrow.replace('`OUT-MO3-C-R0`, `OUT-MO3-C-B01`','`OUT-MO3-C-R0`, `OUT-MO3-C-B01`, `OUT-MO3-C-B02`').replace('Book1基础首遍后继续Book2及C-BASE-02；其余父范围/独立充分性挑战未完','Book2/5.5来源及编码子结果后继续Book3；更宽C-BASE-02及父充分性未完')
 pe.replace_in_shard(docs[cr.DIRECTION],ds,oldrow,newrow)
 pe.append_to_shard(docs[cr.PANORAMA],'全景视野/002 - 治理、门禁与骨架结果.md','| `OUT-MO3-C-B02` | Book2/5.5源审查及编码积计算接口 | `DIR-U-MO3-COVERAGE-C` | 全章15节/19题/Notes、C342–343 primary02与NEG02、精确Git/索引 | `SOURCE_AND_SCOPED_NATIVE / PARENT_SCOPE_INCOMPLETE` | 条件命题β、primitive/projection控制及指定refl拒绝；同题投影可完成，不报失配 | 更宽编码/配置与其余父范围未完；非完整Book翻译、非不终止、D未审 | 第三轮机器统观/Session-C/过程与结果/003 - 编码积的依赖消去与计算接口.md；HoTT/formal/mo3-coverage/encoded-pair/README.md |\n')
 next_action='R1/R2：Book第3章全章逻辑首遍，先最高指示全文、KC47/48及公开生成；由PAT/mere命题/截断/逻辑原则/选择/大小的真实消费者补父范围。C-BASE-02更宽iterator/W-Nat/相干/Cubical接口保显式待办，C342–343只精确子结果；不再打磨同义W/票据/编码例子。'
 s['revision']=289;s['latest_session']=SID
 s['execution_control'].update(last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',next_minimal_verification=next_action,app_goal_completion_eligible=False)
 for rid,w in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:s['records'][rid]['projection_generation']=f'20260924-{w}-289';s['records'][rid]['scope']='C Book1/2 and selected appendix source review plus exact encoded-pair proof; parent scope incomplete.'
 rec=s['records'][TASK];rec['execution_control']['next_minimal_verification']=next_action
 additions=[C+'父范围与覆盖/005 - Book路径与相等消费者的语义处置.md',C+'过程与结果/003 - 编码积的依赖消去与计算接口.md',C+'执行记录/003 - Book第二章与编码计算核证.md',C+'审计/B02/CORE_COGNITION_AUDIT.md',C+'证据/B02/GENERATION.md',C+'证据/B02/PROOF-CHECKS.json','HoTT/formal/mo3-coverage/encoded-pair/README.md','HoTT/formal/mo3-coverage/encoded-pair/EncodedPair.agda','HoTT/formal/mo3-coverage/encoded-pair/TOOLCHAIN.json','HoTT/verification/runs/20260924-MO3-COVERAGE-ENCODED-PAIR-001-02/RUN.json','HoTT/verification/runs/20260924-MO3-COVERAGE-ENCODED-PAIR-001-02/source-manifest.json']
 additions += [str(p.relative_to(ROOT)) for p in sorted((ROOT/C/'审计/B02/CORE_COGNITION_AUDIT').glob('*.md'))]
 rec['full_sources']=list(dict.fromkeys(rec['full_sources']+additions));rec['source_hashes']={p:cr.sha((ROOT/p).read_bytes()) for p in rec['full_sources']}
 rec['revalidation']='B02 actual full-source semantic review, conditional native proof C342–343 with controls, and explicit unclosed wider interfaces; no parent completion.'
 sb=cr.PREFIX+'sessions/'+SID+'/'
 s['records'][SID]={'kind':'session','path':sb+'SESSION.md','lifecycle_status':'HISTORICAL','status':'complete_with_scope','evidence_status':'BOOK2_SOURCE_REVIEW_AND_SCOPED_ENCODING_PROOF','depends_on':[],'related_records':[TASK,PREV],'full_sources':[sb+x for x in cr.SESSION_REQUIRED_FILES],'source_hashes':{},'scope':'Book2/5.5 source review and exact proof subunit only; wider C-BASE-02 and parent scope incomplete.'}
 texts[cr.STATE]=cr.dump(s).decode()
 ar=ROOT/C/'审计/B02/CORE_COGNITION_AUDIT';blocks=re.split(r'^### (KC-\d{6})\n',(ar/'001 - 核心认知逐项回评.md').read_text(),flags=re.M)
 audit=f'# {SID} 完整兼容审计\n\ncore-cognition-generation-8；48 KC；完整分片见{C}审计/B02/CORE_COGNITION_AUDIT.md。G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持。\n\ncore_change: NO\ndirection_change: YES\npanorama_change: YES\nessay_change: NO\nupdate_decision: source review and scoped native proof; parent incomplete\ncross_conflicts: no promotion of typing rejection to nontermination or global mismatch\nunresolved: wider C-BASE-02 and remaining parent sources/relations\n\n|KC ID|姿态|relation|assessment and evidence|next and falsifier|\n|---|---|---|---|---|\n'
 for i in range(1,len(blocks),2):
  kid,b=blocks[i:i+2];f=dict(l[2:].split(': ',1) for l in b.splitlines() if l.startswith('- ') and ': ' in l)
  audit+=f"| `{kid}` | {f['工作姿态']} | {f['relation']} | {f['实际证据与关系理由']} | {f['下一选择及反证条件']} |\n"
 assert len(cr._audit_v1_kc_rows(audit))==48
 essay=(ar/'002 - 阐释消费与航向反思.md').read_text();audit+='\n'+essay[essay.index('# 阐释消费与航向反思'):]
 session=f'# {SID}\n\n固定Book第二章及5.5的来源审查、编码积计算接口原生条件核证。\n\n- host: Codex desktop\n- model: 用户Astra选择，未认证后端\n- tier: T3\n- role: RESEARCH_GENERATION / sole C integrator\n- load_receipt: {C}执行记录/003 - Book第二章与编码计算核证.md；snapshot {plan["snapshot"]}\n- parent: PARENT_SCOPE_INCOMPLETE\n- reflection: no-plan-change\n\nC342–343/primary02通过两个证据检查及e9ad36a selected Git；NEG02为控制不注册数学反定理。原始01/NEG01保留。\n下一：{next_action}\n\n|element_usage|本次用途与边界|\n|---|---|\n|最高指示/core|503行全文、KC47/48及十四题/三呈现/迁移|\n|原典|Book2全2699行、5.5全文，SOURCE不冒全体新证明|\n|native/F-011|精确源/raw run/index/registry/Git，条件前提明确|\n|正反控制|projection保同题，NEG02不冒不终止|\n|canonical writer|48KC完整兼容bundle，原件不改|\n\nT01–05范围不变；T06–12仅新授权证明片段/私有运行缓存，无全局配置更改；T13–17实际原生/证据核验；T18–21无发布；T22–24current进度与源pin；T25治理不改；T26精确提交，无他人index。事务只认canonical result。\n'
 runs={'schema_version':'hott-session-runs/v1','session_id':SID,'kernel_runs':['HoTT/verification/runs/20260924-MO3-COVERAGE-ENCODED-PAIR-001-'+x for x in ('01','02','NEG01','NEG02')],'primary_run':'HoTT/verification/runs/20260924-MO3-COVERAGE-ENCODED-PAIR-001-02','claim_ids':['C-342','C-343'],'proof_subject_commit':'e9ad36a7bc66b4fee4f190307b845a8526d789d4','status':'EXACT_CONDITIONAL_PROOF_AND_CONTROLS','parent_coverage':'PARENT_SCOPE_INCOMPLETE'}
 rows=[]
 for d in docs.values():rows+=pe.payload_rows(d,ROOT)
 rows += [{'path':p,'expected_sha256':cr.sha((ROOT/p).read_bytes()),'text':t} for p,t in texts.items()]
 for n,t in [('SESSION.md',session),('RUNS.json',cr.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:rows.append({'path':sb+n,'expected_sha256':None,'text':t})
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':[TASK],'authorization':'User Goal7 sole C integrator and continue; own research/proof/current-state delta only, preserve A/D/sources and unrelated dirty.','files':rows}
 out=ROOT/C/'证据/B02/checkpoint-payload.json'
 with out.open('xb') as f:f.write(cr.dump(payload))
 print(json.dumps({'snapshot':plan['snapshot'],'payload':str(out.relative_to(ROOT)),'state_applied':False},ensure_ascii=False))
if __name__=='__main__':main()
