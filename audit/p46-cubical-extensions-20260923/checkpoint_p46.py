#!/usr/bin/env python3
"""Canonical P46 source-qualification checkpoint, no new proof claims."""
import argparse,hashlib,importlib.util,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
SID='S-RES-20260923-ASTRA-P46-EXTENSIONS';BASE=f'.codex/research/hott/sessions/{SID}/'
RID='R-P46-THEORY-EXTENSIONS-20260923';TASK='P46-CUBICAL-AND-EXTENSION-BOUNDARIES-001';NEXT='P47-THEORY-INSPECTION-SYNTHESIS-001'
PARENT='R-HOTT-FOUR-TRACK-PLAN-20260921';SHARD='HoTT理论充分检视/008 - P46立方规则与相关扩展的边界.md';EVID='audit/p46-cubical-extensions-20260923/EVIDENCE.json'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as E
def replace_row(doc,path,key,value):
    ls=doc['shards'][path].splitlines(keepends=True);ii=[i for i,l in enumerate(ls) if l.startswith('| `'+key+'` |')];assert len(ii)==1;ls[ii[0]]=value+'\n';doc['shards'][path]=''.join(ls)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');a=ap.parse_args()
    s=json.loads((ROOT/R.STATE).read_text());assert s['revision']==266
    h=json.loads((ROOT/R.HEAD).read_text());assert all(sha(p)==v for p,v in h['tracked'].items())
    plan=R.plan(ROOT,profile='governance');assert not plan['review_required'];(HERE/'PLAN.json').write_bytes(R.dump(plan))
    changed={'goal.md','feature-list.md','HoTT后续研究总体方案.md','HoTT后续研究总体方案/005 - 当前第一步与交接.md','goal-3-工作路径树/001 - 原初目标与当前工作树.md'}
    owner=s['records'][PARENT];assert {p for p,v in owner['source_hashes'].items() if (ROOT/p).is_file() and sha(p)!=v}==changed
    for p in changed:owner['source_hashes'][p]=sha(p)
    owner['revalidation']=owner['revalidation'].replace('Revision264: P45 computational','Revision266: P45 computational')+' Revision267: P46 extension contracts qualified; next P47 synthesis. P45 log metadata corrected without changing original transaction.'
    owner['status']='theory_inspection_in_progress';owner['evidence_status']='P46_EXTENSIONS_REVIEWED / P47_NEXT / GOAL_ACTIVE';owner['related_records']=list(dict.fromkeys(owner['related_records']+[RID,NEXT,SID]))
    s['records'][TASK].update(lifecycle_status='CLOSED',status='source_review_complete',evidence_status='SOURCE_INSPECTED_WITH_SCOPE',resolution={'reason':'Cubical and extension interface scopes reviewed; explicit deep exclusions retained; P47 performs scope synthesis and ranking.','evidence':[SHARD,EVID]})
    s['records'][RID]=dict(kind='result',path=SHARD,lifecycle_status='CLOSED',status='source_review_complete',evidence_status='SOURCE_INSPECTED_WITH_SCOPE / NO_NEW_MATH',depends_on=[],full_sources=[SHARD,EVID],source_hashes={p:sha(p) for p in [SHARD,EVID]},related_records=[TASK])
    s['records'][NEXT]=dict(kind='research_task',path='HoTT理论充分检视.md',lifecycle_status='CURRENT',status='ready',evidence_status='NOT_EXECUTED',depends_on=[],full_sources=['HoTT理论充分检视.md','HoTT后续研究总体方案/006 - 理论充分检视的首轮范围与验收.md'],related_records=[RID])
    s['records']['A-PREMISE-001']['source_qualification']+=' P46: dimension meta-equality is not intrinsic I decidability; guarded, clocked, crisp, quantitative and phase contexts retain distinct conditions. Old sources/runs unchanged.'
    s['records']['P40-THEORY-INSPECTION-FIRST-001']['evidence_status']='DECLARED_FAMILIES_SOURCE_REVIEWED / GLOBAL_SYNTHESIS_AND_RANKING_OPEN'
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='P46_REFLECTION_COMPLETE',depends_on=[],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']],related_records=[RID,NEXT])
    s['revision']=267;s['latest_session']=SID
    nxt='P47-THEORY-INSPECTION-SYNTHESIS-001. Audit overall006 seven semantic criteria across eight fields, four critical interactions, old premise qualifications and exclusions. Compare targeted-process leads, prior coverage and unknown impacts; close this first-pass goal only after integrated acceptance and justified ranking. No automatic general engine scan.'
    s['execution_control'].update(status='THEORY_INSPECTION_P46_COMPLETE_P47_NEXT',next_minimal_verification=nxt,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_status_observed='active')
    s['projection']['status']='THEORY_INSPECTION_IN_PROGRESS / P46_EXTENSIONS / P47_NEXT / GOAL_ACTIVE'
    docs={p:E.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    msg='第006片检视推进到P46：Cubical、guard/clock、shape/crisp、资源及内部模型接口已按各自侧条件审查，E01–E15有相称审查或明确排除。下一P47整体范围验收、遗漏审计和候选排序；无新数学claim，active goal继续。入口：HoTT理论充分检视008；revision267。'
    mp='MEMORY/001 - 当前执行队列.md';old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0];E.replace_in_shard(docs['MEMORY.md'],mp,old,msg)
    lp='MEMORY/003 - 当前验证状态与顺序日志.md'
    E.replace_in_shard(docs['MEMORY.md'],lp,'S-RES-20260923-ASTRA-P45-METATHEORY：P45十一文件来源及逻辑/实数能力分析；第四弹/P17复用；P46下一；revision264。','S-RES-20260923-ASTRA-P45-METATHEORY：P45计算/元理论/模型源文范围审计，6个本地来源身份；P46下一；revision266。（P46纠正此前复制残留；旧事务原件保留。）')
    E.append_to_shard(docs['MEMORY.md'],lp,f'\n{SID}：P46扩展规则与上下文条件审查；P47综合验收下一；revision267。\n')
    for p,kind in [('方向追踪.md','direction'),('全景视野.md','outcome')]:
        E.replace_in_index(docs[p],'source_state_revision: 266','source_state_revision: 267');E.replace_in_index(docs[p],f'projection_generation: 20260923-{kind}-266',f'projection_generation: 20260923-{kind}-267');docs[p]['index_text']=docs[p]['index_text'].replace('THEORY_INSPECTION_P45_REVIEWED_P46_NEXT','THEORY_INSPECTION_P46_REVIEWED_P47_NEXT')
        s['records']['I-DIRECTION-PORTFOLIO-20260912' if kind=='direction' else 'I-OUTCOME-PANORAMA-20260912'].update(projection_generation=f'20260923-{kind}-267',semantic_status='THEORY_INSPECTION_P46_REVIEWED_P47_NEXT',scope='P46 extension interface review complete; P47 integrated scope audit and ranking next.')
    d='方向追踪/002 - 治理与用户方向.md'
    replace_row(docs['方向追踪.md'],d,'DIR-U-HOTT-FOUR-TRACK','| `DIR-U-HOTT-FOUR-TRACK` | 理论检视P46完成、P47综合验收下一 | active goal、KC2/40/47/48 | `IN_PROGRESS / P47_NEXT` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-P46-THEORY-EXTENSIONS` | 八领域/七义务、旧资格与候选排序 | HoTT理论充分检视；revision267 |')
    E.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-P46-THEORY-EXTENSIONS` | 立方/扩展规则与观察边界 | `DIR-U-HOTT-FOUR-TRACK` | 固定论文/Agda2.8文档/既有控制 | `SOURCE_INSPECTED_WITH_SCOPE / NO_NEW_MATH` | face/clock/crisp/shape/phase与结构相容条件分层 | 非全部扩展组合或原生翻译证明，无现实桥 | {SHARD}；revision267 |\n')
    pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=re.sub(r'^16\. 理论充分检视继续：.*$','16. 理论充分检视继续：P40–P46声明源文范围完成，下一P47整体七项语义/关键交互验收、旧资格与排序。',docs['全景视野.md']['shards'][pp],flags=re.M)
    rows=[]
    for doc in docs.values():rows+=E.payload_rows(doc,ROOT)
    seen={r['path'] for r in rows}
    for p in R.MUTABLE:
        if p in seen:continue
        t=(ROOT/p).read_text()
        if p==R.STATE:t=R.dump(s).decode()
        elif p.endswith('FRONTIER.md'):t=re.sub(r'^- 第006片检视推进到P45：.*$','- '+msg,t,flags=re.M)
        elif p.endswith('RESUME.md'):t=re.sub(r'^第006片检视推进到P45：.*$',msg,t,flags=re.M)
        rows.append(dict(path=p,expected_sha256=sha(p),text=t))
    m=json.loads((ROOT/'核心认知.manifest.json').read_text());focus={2:'地图E族逐项处置',3:'新增规则保留侧条件',5:'具体任务先于归因',6:'时间不等同tick或密度',9:'各演算时间/方向规则定位',10:'边界非内部矛盾',11:'时序可用性进入上下文',15:'用户强解释保留为可反驳起点',18:'资源与phase显式分层',21:'无新kernel结果',23:'later/clock规则有直接出处',24:'可用性与全过程完成区分',29:'经济收益须实际连任务',30:'扩展的理论取舍回源',31:'不能由一种受限上下文推出全域不可表达',35:'原X桥未被扩展名词替代',36:'内部模型不等总真理判定',37:'最终见证仍未得',38:'不推断作者心理',39:'旧代理模型尚无原生翻译',40:'知识谱由版本化来源校准',43:'P6/P33/C92–99复用避免路径依赖',44:'拓扑/时间解释可研究但未验证物理',45:'形式区间不自带现实桥',46:'下一整体排序回到研究问题',47:'抽象省略与实际保留条件区分',48:'敏感点锚定真实引入/消去规则'}
    aud=[f'# {SID} 核心认知审计','',f"- identity: {s['current_core']['generation']} / 48 KC",'- core_change: NO','- direction_change: YES; P46扩展接口源文完成、P47综合验收下一。','- panorama_change: YES; 仅来源审计与范围纠偏。','- essay_change: NO','- update_decision: checkpoint及理论覆盖/树更新；不改冻结源文或旧run。','- cross_conflicts: 不同扩展条件不能无桥相加；P45日志复制残留已纠正，历史收据保留。','- unresolved: 其他理论领域和现实桥开放；writer分片事务兼容缺口不变。','','| KC | 主题 | relation | 立场与理由 | 证据 | 后继及反证条件 |','|---|---|---|---|---|---|']
    for i,u in enumerate(m['units'],1):
        rel='TENSION' if i==37 else 'ALIGNED' if i in focus else 'NOT_TOUCHED';why=focus.get(i,'本wave限定扩展接口来源资格，未检验此主题数学命题')
        aud.append(f"| `{u['id']}` | {u['semantic_label']} | `{rel}` | {why} | {SHARD} | P47综合验收；若精确来源提供无条件强桥或新同任务反例则重评；未触及项不外推 |")
    aud+=['','## 扩展认知与全波次反思','001统一推理的收益与条件；002各上下文限制；003原X不替换；004具体演算回源；005时序/物理时间分层；006旧代理控制范围；007P6/P33复用；008现实解释仍须桥；009规则敏感点服务针对过程。',f'完整Goal-3十问/五项价值/六项航向、SOP八项与覆盖回评在{SHARD} §7。CLOSE_WITH_SCOPE后active goal继续P47。','', '## 加载与证据边界','core8与四件套按PROTOCOL v3复认revision266收据，HEAD.tracked无hash变化；本审计逐48KC登记立场，抽查KC47/48完整原文并完整重读goal-3。扩展论文及官方合同按EVIDENCE精确段落读取；goal3/KC47–48每波重读；P6/P33/C92–99与P42按范围复用。本wave没有新的proof claim或kernel run，原始数学结论不由源文审查提升。完整48KC单文件兼容审计，非嵌套分片事务。']
    ses=f'# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3 research/state\n- load_receipt: revision266收据复认及HEAD.tracked哈希一致；PLAN.json={plan["snapshot"]}；goal3与KC47/48完整重读。\n- status: P46_SOURCE_REVIEW_COMPLETE\n- authorization: 用户active goal完成006，本地研究与checkpoint；禁Sub Agent/push/tag。\n- element_usage: core/SOP=航向；各扩展论文/官方合同=来源；旧控制=查重对象；旧源码=控制查重；STATE=接续；无新kernel。\n- next: {NEXT}\n\nreflection=no-plan-change；完整反思与影响见{SHARD}。\n'
    ses+='\n- known_gap: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001；使用PROTOCOL允许的完整48KC单文件兼容bundle，不宣称嵌套分片已原子写入。\n'
    bundle={'SESSION.md':ses,'RUNS.json':R.dump(dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],new_kernel_runs=[],evidence=EVID)).decode(),'CORE_COGNITION_AUDIT.md':'\n'.join(aud)+'\n'}
    rows += [dict(path=BASE+p,expected_sha256=None,text=t) for p,t in bundle.items()]
    pay=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='governance',task_ids=[],authorization='用户active goal执行006，P46扩展源文审查及反思完成，接P47；不push/tag。',files=rows)
    (HERE/'PAYLOAD.json').write_bytes(R.dump(pay));res=R.checkpoint(ROOT,plan['snapshot'],pay,apply=a.apply);(HERE/('APPLY.json' if a.apply else 'DRY-RUN.json')).write_bytes(R.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
