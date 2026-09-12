"""Publish bounded R033 research through the inherited cognition runtime."""
from pathlib import Path
import copy, hashlib, importlib.util, json, subprocess, sys
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[2]
P='.codex/research/hott/'
R=P+'reviews/SELF-REFERENCE-005/'
SID='S-RES-20260911-033-DEPENDENT-MIGRATION'
RID='P-DEPENDENT-MIGRATION-033'
OUT=ROOT/'artifacts/r033/checkpoint'

def js(x): return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def save(name,data):
    p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists(): raise FileExistsError(p)
    p.write_text(js(data),encoding='utf-8')
def runtime():
    spec=importlib.util.spec_from_file_location('r033_checkpoint_runtime',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);return m

def main():
    state0=json.loads((ROOT/(P+'STATE.json')).read_text())
    if state0['revision']!=32: raise RuntimeError('Expected revision32')
    save('STATE_BASE.json',state0)
    owner='HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md'
    index='scripts/README.md'
    for rel in [owner,index,'MEMORY.md',P+'STATE.json',P+'FRONTIER.md',P+'LESSONS.md',P+'RESUME.md']:
        dest=OUT/'originals'/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes((ROOT/rel).read_bytes())
    with (ROOT/owner).open('a',encoding='utf-8') as f:
        f.write('''
## 12. 2026-09-11 R033：依赖迁移必须保留路径作用，不只保留端点

实质记录：`.codex/research/hott/reviews/SELF-REFERENCE-005/PROOF_NOTE.md`。R032非依赖公理桥接不能直接当作一般依赖替换：x:A,y:B(x)需要纤维映射；若要求身份保持，需p:x=x′及q:transport(p,y)=y′。第三项z:D(x,y)沿整个Σ提升路径迁移。真正的Π纤维函数自动满足transport自然性，外部局部函数表不能据局部类型合格就冒充这种函数。

有限C2集合值模型中，翻转Bool族的4张自映射仅恒等/取反2张相容；平凡Bool族到翻转族没有全局自然变换。HoTT圆双覆盖无截面给出对应纸笔反证。该例不是绕行难度或stuck新机制。

布尔宇宙自路径refl与ua(not)同端点却对false产生不同运输；将路径压成仅存在且要求保持每条原路径作用不能成立。Σ总空间中(Bool,false)=(Bool,true)也不推出固定Bool中false=true。三元素交换复合顺序不同确实产生不同值，证明HoTT在此处保留顺序作用，非证明物理耗时或全部历史已被保存。

在set值族、funext、命题截断条件下，transport经仅存在的端点相等因子化⇄所有回路作用平凡：必要性比较refl；充分性以平行路径作用常值和唯一像构造解码。无需LEM/选择；不是任意高阶值类型的一阶相干充分定理。可保留最小作用不变量，不要求无限记录全部历史。

29项有限测试通过；共享Agda参数化运输源码未编译。没有完整扩展R032对象语法，也没有找到标准规则强迫坏擦除或认证新现实相对悖论。下一步仅选一个真正依赖身份的有限语法声明核编码/解释，不再扩充同类群作用表。完整动态认知未加载完且实际发生压缩，继续保留有界局部记录身份。
''')
    with (ROOT/index).open('a',encoding='utf-8') as f:
        f.write('''
## R033 · 依赖上下文与路径作用

- `research/r033_dependent_migration.py`：有限C2群胚的集合值作用、纤维表自然性、Σ第二分量检查、路径遗忘与非交换顺序。不是HoTT检查器。
- `tests/test_r033_dependent_migration.py`：29项正反检查。
- `research/r033_formal/DependentMigration.agda`：参数化Σ路径、第三项迁移、自然性及路径擦除条件反证；未编译。
- `session/r033_restore.py`、`r033_context.py`：ZIP保全、实际输入输出及工具探针。
- `session/r033_checkpoint.py`、`r033_verify.py`、`r033_deliver.py`：原治理器交接、既有文件保护与Git/ZIP恢复验证。

源码先落盘后调用；实际结果及stdout/stderr在`artifacts/r033/`。一般定理依纸笔证明，有限模型数据不能替代原生HoTT证明。
''')
    rt=runtime();base=rt.plan(ROOT);state=copy.deepcopy(state0)
    state['revision']=33;state['latest_session']=SID
    impacted=[]
    for rid in base['review_required']:
        rec=state['records'][rid]
        if rec.get('status')!='review_required':
            rec['status']='review_required';impacted.append(rid)
            rec['dependency_change_note']='R033 owner append: dependent migration scope; old proof evidence retained, not recertified.'
    sources=[R+n for n in ['REQUEST.md','PROOF_NOTE.md','PLAN.md','SOURCES.md','CLAIMS.json']]+[
        'scripts/research/r033_dependent_migration.py','scripts/tests/test_r033_dependent_migration.py',
        'scripts/research/r033_formal/DependentMigration.agda','artifacts/r033/RESULTS.json',
        'artifacts/r033/TEST_EXECUTION.json','artifacts/r033/CONSTRUCTION_EXECUTION.json','artifacts/r033/NATIVE_PROBE.json']
    hashes={rel:sha(ROOT/rel) for rel in sources}
    state['records'][RID]={'kind':'scoped_research','path':R+'PLAN.md','status':'review_required',
        'depends_on':['P-RESTRICTED-REFLECTION-032'],'full_sources':sources,'source_hashes':hashes,
        'scope':'Dependent Sigma migration, naturality and exact set-valued transport-erasure criterion; finite groupoid diagnostics',
        'formal_status':'PAPER_PROOFS_AND_29_PYTHON_TESTS_AGDA_NOT_RUN',
        'workflow_status':'FULL_DYNAMIC_COGNITION_INCOMPLETE_ACTUAL_COMPACTION',
        'reality_bridge':'PATH_ACTION_ERASURE_BOUNDARY_NOT_ATTRIBUTED_TO_STANDARD_HOTT_AS_MANDATORY'}
    sp=P+'sessions/'+SID+'/SESSION.md'
    state['records'][SID]={'kind':'session','path':sp,'status':'review_required',
        'depends_on':[RID,state0['latest_session']],'full_sources':sources,'source_hashes':hashes,
        'scope':'Continuation of actual R032 dependent-context next step, no new external AI input'}
    state['active']=list(dict.fromkeys([RID]+state['active']))
    state['review_due']=list(dict.fromkeys(state['review_due']+[RID,SID]+impacted))
    state['local_git'].update(inherited_head='d06c13832fb315a3d1a441164f8ad9e4d6b85c71',
        pre_checkpoint_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        history_origin='Inherited full revision32 Git; no reinitialization',final_head='See actual HEAD and R033 delivery verification')
    memory=f'''# MEMORY · revision33

当前工作副本 `{ROOT}`，继承revision32完整Git。最新Session `{SID}`。无新Gemini信件、外部AI、Work任务或push。

## 目标与连续性
双向现实相对目标不变；不是只找HoTT内部矛盾，也不能将人为坏接口的反例归罪于核心。原77项记录保留。R001来源缺件、RP-B01原生内化、R026规约、R027环境、R028范围、R029—031自指和R032受限迁移保持原状态。

## 本轮差量
进入x:A,y:B(x)的语义级依赖迁移，给出纤维映射及Σ身份第二分量；第三个依赖值沿整个提升路径迁移。自然性由真正Π函数的路径归纳得到，不是所有外部局部表都能组成全局依赖函数。

布尔翻转族4张局部自表仅2张全局相容；平凡族到翻转族无相容映射。端点相同的refl与ua(not)可改变值，Σ总空间相等不推出固定纤维相等。三元素交换直接表明复合次序可以参与transport结果。

集合值族中，完整transport能仅依赖“端点相等存在”⇄所有回路作用平凡；充分方向用唯一像消去，不需LEM/选择，但不认证不透明项的有效实现。完整语法路径可被足够的作用不变量替代，不将全部历史当每个任务的必备输入。

## 证据范围
论文式推导见reviews/SELF-REFERENCE-005/PROOF_NOTE.md。29项有限C2模型单元测试与构造结果均通过；不是HoTT内核。Agda共享参数化文件未编译，PATH没有相关工具，有界下载探针DNS失败。不宣称完整依赖语法解释器、新原创定理或HoTT悖论成立。

## 认知恢复
本轮计划363份/2865496字节。核心闭包和三问实际12块输出，截断部分补读；随后真实压缩，动态全集未加载。当前是有界局部接续，不认证完整业务Skill，不修改全文要求。

## 下一动作
把最小身份/依赖声明接回R032对象语法，检查“仅知道相等存在”是否真的被所选翻译用作保持原依赖值的路径。不再扩大C2/S3样本，不把模型中的任意局部表当实际HoTT项。原生工具可用后再编译已有Agda；研究不依赖Gemini。
'''
    frontier='''# 研究前沿 · revision33

R033已把R032非依赖迁移推进到Σ依赖证据与自然性。端点不足以确定路径作用，集合值族上的安全路径遗忘⇄回路作用平凡已写出两个构造方向。HoTT实际保留非交换复合作用，不能笼统说它删除一切顺序。

当前缺口：完整依赖对象语法/解释/翻译尚未实现；所述坏擦除没有被归属于标准HoTT。新的实际问题必须由具体语法与解释生成，而不是继续将局部任意函数表当依赖Π项。

下一最小动作：只增加一个依赖身份声明，连通R032证书迁移与R033路径作用，追查某个明确反射接口在只保留截断相等后是否误承诺原值保持。若只是我们自行删除数据，不再重复包装成理论失败。RP-B01原生闭包和R026规约线仍开放。
'''
    lessons=(ROOT/(P+'LESSONS.md')).read_text()+'''
## R033 · 全局依赖函数、路径与数据迁移

- 局部每个纤维都给一个有类型的函数表，不自动成为全局Π函数；真正的依赖函数自动满足transport自然性。
- 身份保持比“产生新的合法值”强；Σ路径需p和被p运输后的第二分量等式，第三项须沿总路径搬运。
- 两条路径端点相同不保证作用相同，且HoTT可以区分操作先后。不能把数学transport等式直接当作基本归约日志。
- 对set值族，安全擦除全部路径作用当且仅当回路作用平凡；数据任务可只保留作用不变量，不强制永久保存所有历史。
- 一阶群胚模型中的自然性充分条件，不是任意高阶类型的全部相干充分定理。
- 标准双覆盖无截面是局部与全局的构造障碍，不是绕行复杂度、不停机或标准HoTT已经批准坏接口。
'''
    resume=f'''# 接续 revision33

最新Session {SID}。本页不替代原治理要求。

先恢复R032非依赖迁移与R033 reviews/SELF-REFERENCE-005/完整证明。核心是Σ路径第二分量、自然性、路径遗忘判据及回路作用。29测试只覆盖有限群胚集合值模型；Agda未编译。没有新HoTT悖论认证。

下一项必须回到一个实际身份依赖声明/对象语法，不再追加同类局部表或停机案例。审查同一原任务需要保持的是哪条路径的作用，而非仅仅重新给出某个同类型值。旧77记录保留，RP-B01/R026—032不消失。全部代码先写scripts再调用，本地Git不push。
'''
    session=f'''# {SID}

## 身份与输入
用户当前消息逐字为“继续”。恢复revision32完整ZIP与Git；当前副本{ROOT}。没有外部AI、Gemini通信、主机本地任务或远端提交。

## 实际读取与范围
根AGENTS、治理/业务Skill、核心闭包与三问、MEMORY/RESUME、R032证明和共享代码、Schema及反射专题实际读取。核心12块曾输出且有补读；随后实际上下文压缩。363份动态全集未完整载入。不以文件收据认证理解，不取消全文要求，保存有界局部研究。

## 实际研究和执行
新代码先保存scripts。有限C2群胚Action验证单位、复合与双射；相容纤维映射检查、Σ路径目标检查、18个有限作用及三元素顺序对照；29单元测试全部通过，结果与原始stdout/stderr保存。无新增模拟HoTT求值器。Agda文件未编译。

## 数学判断
从R032非依赖桥接进入具体Σ和transport责任。P1/P2/P4标准规则应用；P5 set值下两个构造性方向含唯一像论证。HoTT保留路径复合作用顺序，坏擦除规格不可实现不等于内部矛盾。没有完整依赖对象语言机器证明或现实悖论认证。

## 保存与下一步
先有本地Git保全提交，当前通过原checkpoint更新五状态与Session。只追加专题和scripts索引；原闭包/三问/Skills/Schema/矩阵/旧数学源码保持字节。新记录将连到R032、所有原记录保留。下一项有限身份依赖语法接口，不再扩大同类模型样本。
'''
    values={'MEMORY.md':memory,P+'FRONTIER.md':frontier,P+'LESSONS.md':lessons,P+'RESUME.md':resume,
            P+'STATE.json':js(state),sp:session}
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,
      'authorization':'User continues; inherited explicit scripts-first, local Git and persistence authorization. Bounded local continuation.',
      'files':[{'path':rel,'text':text,'expected_sha256':sha(ROOT/rel) if (ROOT/rel).exists() else None} for rel,text in values.items()]}
    save('BASE.json',base);save('PAYLOAD.json',payload)
    save('DRY.json',rt.checkpoint(ROOT,base['snapshot'],payload,apply=False))
    result=rt.checkpoint(ROOT,base['snapshot'],payload,apply=True);save('COMMIT.json',result)
    after=rt.plan(ROOT);save('AFTER.json',after)
    paths={d['path'] for d in after['documents']}
    required=set(sources+[sp,'MEMORY.md',P+'reviews/SELF-REFERENCE-004/PROOF_NOTE.md',P+'reviews/EARLY-GEMINI-001/ASSESSMENT.md'])
    if not required<=paths: raise AssertionError('Missing routed material: '+repr(required-paths))
    try: rt.checkpoint(ROOT,base['snapshot'],payload,apply=False)
    except rt.CognitionError as e:
        if str(e)!='STALE_BASE': raise
        save('STALE.json',{'status':'REJECTED','error':str(e)})
    else: raise AssertionError('stale snapshot accepted')
    summary={'status':result['status'],'revision':after['revision'],'snapshot':after['snapshot'],
       'previous_records':len(state0['records']),'current_records':len(state['records']),
       'all_prior_ids_retained':set(state0['records'])<=set(state['records']),
       'old_records_newly_flagged':impacted,'documents':len(after['documents']),
       'required_new_and_prior_sources_routed':True,'full_business_cognition':'INCOMPLETE','native_formal':'NOT_RUN'}
    save('SUMMARY.json',summary);print(js(summary))
if __name__=='__main__': main()
