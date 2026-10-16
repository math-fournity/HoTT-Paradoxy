"""Save a paused governance checkpoint with all previous research records unchanged."""
from pathlib import Path
import copy, hashlib, importlib.util, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
P='.codex/research/hott/'
SID='S-PAUSE-20260911-035-COMPUTATION-BOUNDARY'
S=P+'sessions/'+SID+'/'
OUT=ROOT/'artifacts/r035/checkpoint'

def js(o): return json.dumps(o,ensure_ascii=False,indent=2)+'\n'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def save(name,obj):
    f=OUT/name;f.parent.mkdir(parents=True,exist_ok=True)
    if f.exists():raise FileExistsError(f)
    f.write_text(js(obj),encoding='utf-8')
def runtime():
    spec=importlib.util.spec_from_file_location('r035_runtime',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod);return mod

def main():
    old=json.loads((ROOT/(P+'STATE.json')).read_text())
    if old['revision']!=34:raise RuntimeError('Expected revision34')
    save('STATE_BASE.json',old)
    old_memory=(ROOT/'MEMORY.md').read_text()
    old_frontier=(ROOT/(P+'FRONTIER.md')).read_text()
    old_lessons=(ROOT/(P+'LESSONS.md')).read_text()
    old_resume=(ROOT/(P+'RESUME.md')).read_text()
    # Correct only a stale current-state introduction; history remains in inherited Git.
    readme=ROOT/'README.md';text=readme.read_text()
    before=OUT/'README_BEFORE.md';before.write_text(text)
    start=text.index('## 当前ASK认识与完整接续')
    end=text.index('## 项目身份',start)
    replacement='''## 当前状态与恢复入口（2026-09-11，revision35）

**PAUSED_BY_USER：研究暂停，未关闭已有课题。**最后实际研究为R034；R035仅保存暂停点及用户关于“逻辑＋几何＋程序”和共享计算边界的新判断。详见 [MEMORY](MEMORY.md)、[暂停交接](PAUSE_HANDOFF.md) 和当前 [.codex/research/hott/STATE.json](.codex/research/hott/STATE.json)。当前Session、版本与待办以这些实际状态为准，不沿用本文件历史段落的旧Session号。

后续只有在用户要求继续时恢复研究，并按根AGENTS及既有治理Skill重新加载正文。原第五闭包、三问、两类Skill、所有旧记录及证据身份保留；新怀疑没有被登记成已证HoTT悖论，也没有以一般不完备性替换原双向现实相对目标。

关于ASK的原始来源仍在第五闭包§21及 `HoTT/sources/user-originals/ASK-合法提问与时间前提-用户完整原文-20260910.md`。本次没有启动新数学实验、证明助手、其他AI或远端操作。

'''
    readme.write_text(text[:start]+replacement+text[end:])
    rt=runtime();base=rt.plan(ROOT);save('BASE.json',base)
    unexpected=[rid for rid in base['review_required'] if old['records'][rid].get('status')!='review_required']
    if unexpected:raise RuntimeError('New dependency review required: '+repr(unexpected))
    state=copy.deepcopy(old)
    state['revision']=35;state['latest_session']=SID
    state['execution_control']={'status':'PAUSED_BY_USER','reason':'User explicitly requests pause and preservation.',
       'request_path':S+'REQUEST.md','last_research_session':old['latest_session'],
       'resume_policy':'Resume only after subsequent explicit user continuation; reload under existing governance.',
       'new_experiments_authorized':False,'background_work':False}
    sources=[S+'REQUEST.md',S+'ASSESSMENT.md',S+'SOURCES.md','PAUSE_HANDOFF.md','artifacts/r035/REQUEST_IDENTITY.json']
    hashes={rel:sha(ROOT/rel) for rel in sources}
    state['records'][SID]={'kind':'pause_checkpoint','path':S+'SESSION.md','status':'review_required',
        'depends_on':[old['latest_session']], 'full_sources':sources,'source_hashes':hashes,
        'scope':'User-requested pause, hypothesis preservation and bounded conceptual assessment; no new mathematics experiment.',
        'workflow_status':'PAUSED_BY_USER','formal_status':'NO_NEW_PROOF_OR_NATIVE_RUN',
        'cognition_status':'BOUNDED_PAUSE_ASSESSMENT_FULL_BUSINESS_LOAD_NOT_CERTIFIED'}
    state['review_due']=list(dict.fromkeys(state['review_due']+[SID]))
    state['local_git'].update(inherited_head='14aa846b39189e70e8e0e24299281392dec6812b',
       pre_checkpoint_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
       history_origin='Inherited complete revision34 Git archive; no reinitialization',
       final_head='See actual Git HEAD and external revision35 delivery verification')
    memory=f'''# MEMORY · revision35 · PAUSED_BY_USER

用户2026-09-11明确要求暂停研究并保留记录。实际副本 `{ROOT}`，来自revision34完整with_git包，继承原Git。最新Session `{SID}`；最后实际数学研究仍是R034。无新实验、无新Gemini来信/发信、无其它AI、无Work、无push、无后台工作。

## 当前暂停点与原话

完整请求、独立评估和来源在 `{S}`；可移植恢复入口是根 `PAUSE_HANDOFF.md`。全局状态有 `execution_control.status=PAUSED_BY_USER`。这不关闭任何数学开放事项，也不禁止后续用户明确“继续”时恢复。

## 本次可吸收与保留边界

“逻辑＋几何＋计算”比“HoTT绝对静态”准确；但全部历史悖论已覆盖、核心承诺物理离散性、完全对齐现实宇宙都没有得到证明。有效形式化足够一般的计算时会面对相应停机/总性与自指界限；不完备性还须固定有效公理系统、算术表达和相关证明条件。停机、总性、可判定检查、证明搜索和不完备分别记录。共享界限本身不等于理论化新增失真。

原目标仍为双向现实相对研究。用户说的是怀疑，不把它登记为全称定理或自动替换最高目标。R001缺件、RP-B01原生对应、R026规约和R029—034正反结果继续保留，所有原81条记录逐值不改。

## 恢复边界

本次是有界暂停/评估，没有执行全套业务Skill，不以机械恢复或哈希认证全文理解；不虚构本轮压缩事故。恢复应按旧协议全文读所需来源，不能拿本页替代。新增代码仍先存scripts再调用。

## 最后一轮研究记忆（R034原文，作为历史而非本轮认证）

{old_memory}
'''
    frontier='''# 研究前沿 · revision35 · PAUSED_BY_USER

当前用户暂停所有新探索，仅完成保存与新认识评估。原活动/复核队列不清空、不改数学状态；暂停是执行层状态。新用户继续后才按当前证据选下一项，不自动运行置换测试或继续Gemini派题。

原 R034 前沿完整保留如下；它是暂停前计划，不是现在正在执行的任务。

'''+old_frontier
    lessons=old_lessons+'''
## R035 · 暂停与共享边界校准

- 用户怀疑按原话保存，不能把“逻辑＋几何＋程序”升级为已分析全部悖论、已证明物理时空离散或已经验性对齐宇宙。
- 语法/类型检查、给定证书核验、任意程序停机、全域总性、固定理论不完备是不同问题。有限且正确的checker可与证明搜索/语义判定不完备并存。
- 计算限制也适用于显式时序的程序；无普遍算法不单独证明理论缺时间或偏离现实。应区分已有能力、共享限制、具体理论化新增失真。
- 暂停保存不开展新实验，不删除active/review记录，不冒充旧数学重新认证。暂停在收到后续明确继续后可解除；恢复资料和条件必须保留。
'''
    resume=f'''# 接续 revision35 · 用户暂停

当前状态 PAUSED_BY_USER，最新Session `{SID}`。本页是路由，不是完整认知替代物。

先读根 `PAUSE_HANDOFF.md` 和本Session的REQUEST/ASSESSMENT/SOURCES；最后实际研究仍为R034，旧研究资料、正反例、未编译形式化和来源缺口均在原路径。只有用户下一次明确继续，才恢复业务研究。

新判断应按三层使用：HoTT真实的计算/依赖能力；与足够强有效系统共享的计算与证明限制；某种具体理论化新增的失真。不能因识别共享界限就宣称找到了完整目标悖论，也不能据此放弃原双向目标。

暂停前R034接续内容：

{old_resume}
'''
    session=f'''# {SID}

## 身份与授权
当前用户暂停研究，要求保全恢复，并提出关于逻辑/几何/程序及共享计算边界的怀疑。原消息逐字保存在REQUEST.md。不是新的Gemini来信、不是用户要求运行新实验。

## 输入与实际恢复
从完整revision34 ZIP恢复至{ROOT}，基线HEAD 14aa846b39189e70e8e0e24299281392dec6812b。RESTORE.json记录每个原文件哈希。已读治理入口、相关owner、R031与R034完整论文说明；未重新读完全部动态语料，不声称全业务认知完成。外部repo-cognitive-closure未发现，不宣称调用。

## 本轮实际行动
仅保存、概念评估、一手来源有界核查和受控checkpoint/Git交接；没有数学实验、证明助手、工具链安装或其他AI。新的独立评估注明来源、假说、推论及未证前提。README过时revision13当前指针修订为最新暂停入口，其原文保存在Git及checkpoint/README_BEFORE.md。

## 证据变化
proof_delta=0；所有旧{len(old['records'])}项记录逐值保留；旧结论验证状态不变。当前新增的是用户认识与暂停状态，不是新的定理。共享计算界限不能自动被归类为现实失真。

## 恢复
原STATE active/review/unresolved不删除。execution_control记录暂停；后续用户明确继续可解除。R034下一动作及R001/RP-B01/R026/反射各缺口见PAUSE_HANDOFF和原记录。所有代码先存scripts再调用。包包含真实Git历史，不push。机械检查不证明模型永不遗忘。
'''
    values={'MEMORY.md':memory,P+'FRONTIER.md':frontier,P+'LESSONS.md':lessons,P+'RESUME.md':resume,P+'STATE.json':js(state),S+'SESSION.md':session}
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,
        'authorization':'Current user explicitly requests pause and preservation; inherited scripts-first/local Git rules. No new research experiments.',
        'files':[{'path':rel,'text':txt,'expected_sha256':sha(ROOT/rel) if (ROOT/rel).exists() else None} for rel,txt in values.items()]}
    save('PAYLOAD.json',payload)
    save('DRY.json',rt.checkpoint(ROOT,base['snapshot'],payload,apply=False))
    result=rt.checkpoint(ROOT,base['snapshot'],payload,apply=True);save('COMMIT.json',result)
    after=rt.plan(ROOT);save('AFTER.json',after)
    current=json.loads((ROOT/(P+'STATE.json')).read_text())
    assert all(current['records'][k]==v for k,v in old['records'].items())
    assert current['active']==old['active']
    assert current['execution_control']['status']=='PAUSED_BY_USER'
    routes={d['path'] for d in after['documents']}
    required=set(sources+[S+'SESSION.md','MEMORY.md',P+'reviews/SELF-REFERENCE-006/PROOF_NOTE.md',P+'reviews/EARLY-GEMINI-001/ASSESSMENT.md'])
    assert required<=routes, required-routes
    try:rt.checkpoint(ROOT,base['snapshot'],payload,apply=False)
    except rt.CognitionError as exc:
        if str(exc)!='STALE_BASE':raise
        save('STALE.json',{'status':'REJECTED','error':str(exc)})
    else:raise RuntimeError('Stale write accepted')
    summary={'status':result['status'],'revision':35,'execution_status':'PAUSED_BY_USER',
       'prior_records_unchanged':len(old['records']),'current_records':len(current['records']),
       'old_active_queue_preserved':True,'required_sources_routed':True,
       'planned_documents':len(after['documents']),'planned_bytes':after['total_bytes'],
       'stale_write_rejected':True,'business_cognition':'NOT_CERTIFIED_BOUNDED_PAUSE',
       'mathematical_experiments':0,'native_formal_runs':0}
    save('SUMMARY.json',summary);print(js(summary))

if __name__=='__main__':main()
