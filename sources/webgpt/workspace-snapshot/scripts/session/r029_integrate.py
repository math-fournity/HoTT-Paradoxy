#!/usr/bin/env python3
"""Integrate a bounded self-reference review; preserve old history and use original checkpoint engine."""
from pathlib import Path
import copy, datetime, hashlib, importlib.util, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
P='.codex/research/hott/'
R=P+'reviews/SELF-REFERENCE-001/'
SID='S-REVIEW-20260911-029-SELF-REFERENCE'
OUT=ROOT/'artifacts/r029'
def sha(data): return hashlib.sha256(data).hexdigest()
def jt(v): return json.dumps(v,ensure_ascii=False,indent=2)+'\n'
def save(rel, data):
    path=ROOT/rel
    if path.exists(): raise FileExistsError(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(data if isinstance(data,str) else jt(data),encoding='utf-8')
def update(rel, fn):
    path=ROOT/rel; old=path.read_bytes(); new=fn(old.decode()).encode()
    save('artifacts/r029/before/'+rel,old.decode())
    if path.read_bytes()!=old: raise RuntimeError('Concurrent source edit: '+rel)
    path.write_bytes(new)
def hs(paths): return {p:sha((ROOT/p).read_bytes()) for p in paths}
def main():
    prior=json.loads((ROOT/(P+'STATE.json')).read_text())
    if prior['revision']!=28:raise RuntimeError('Expected revision28')
    gov='''\n## 自指问题的直接回应与探索调度（2026-09-11，revision29）\n\n用户追问“为什么慢”和“HoTT能否面对自身的自指”时，先直接交付当前判断与最小推导，不能让多年历史重述、同类有限测试或同行往返信件替代答案。该主题的当前owner继续为 `HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md`，新来源与说明见 `.codex/research/hott/reviews/SELF-REFERENCE-001/`。\n\n把语法表示/有限证据检查、指定片段解释、对包括自身的新语言全域忠实求值、真理判定与自身可靠性分开。明确编码域与输入类型、是否覆盖使用评价器自身的新项，以及实际求值等式。不从“有自指”直接推出不停机，也不把“总函数”写成瞬间返回、把宇宙层级写成运行时无限攀爬。\n\n自指/反射恢复到探索优先位；RP-B01原生模型、R026规约与资源问题继续保留，不清除旧证据或未知。同行观点用于校准，不形成派工循环；本轮无需再发信才可以推进。禁止把Gemini的“纯核心、必须通过静态检查才算目标”作为用户已批准的排他定义。现有双向目标、三层交付和全文加载规则不改。\n\n完整规范恢复与有界来信/方法评估按真实范围记录：没有完整加载全量动态材料，不声称全业务认知验收通过；不因此伪造压缩事件或重复运行安装检查。治理应保全已得成果并支持下一项有判别力的构造。\n'''
    update('AGENTS.md',lambda x:x+gov)
    topical='HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md'
    section='''\n## 8. 2026-09-11 当前重聚焦：同域反射覆盖，不是无限宇宙运行\n\n本节吸收用户两问及Gemini最新自指论述。保留§1—7的来源与旧攻击裁决；历史文章不作2026尚未解决或必然不可能的证明。正文完整分析见 `.codex/research/hott/reviews/SELF-REFERENCE-001/ASSESSMENT.md` 与 `PROOF_NOTE.md`。\n\n**可直接交付的条件界限。**令 C 为代码/可对角输入的同一类型，E:C→C→Bool。定义 d(x)=not(E(x,x))。若有 c:C 及 Πx.E(c,x)=d(x)，代 x=c 得 b=not(b)，由Bool构造子区分得Empty。这排除这一个 d 的忠实表示，也排除其命题截断存在；不需要LEM、单价性、HIT、物理时间或无限层级。它是已知Cantor/Lawvere机制的局部重建，不是首次定理或HoTT内部不一致。\n\n关键不是说任何自解释都不可能，而是检查具体语法是否同时提供E、同域自应用、形成d的闭包、d的引用和逐输入正确性。带类型解释器、部分解释器或分阶段旧层解释未必满足这些条件。强规范Fω的类型化自解释一手结果亦说明不可跳过类型/编码检查。\n\n**保留与拒绝。**保留将理论自身的求值/审查也纳入ASK的方向；拒绝“所有自元理论都必须有万能eval”“全域总性等于瞬间”“每个递归调用升宇宙”“标准HoTT已批准全能自判定器”这些未证断言。eval:Syntax→U只是未说明输入合法性和项/类型解释的签名，不能充当存在定理。\n\n**当前动作。**用一个准确的同域反射提案查四项义务：代码类型是否真为源输入、评价器是否在覆盖语言内、反向项是否被编码、正确性是否包含它。先找第一项具体缺口，再考虑阶段/类型化正例；不先重建整个编译器，也不再重复Trap样本。这个有限推导与R024共享对角思想，差量是直接核自元理论的覆盖闭包而非继续构造停机分类。\n\n**持续边界。**本轮没有原生HoTT验证、通用代码模型新证明或物理非现实性认证。无限层级是模式，不自动变成任何单个有限任务必须执行的无限过程；复杂度/规范性必须绑定具体呈现。\n'''
    def topical_edit(x):
        x=x.replace('状态：`CURRENT HISTORICAL RECOVERY + TECHNICAL CALIBRATION`','状态：`CURRENT HISTORICAL RECOVERY + SELF-REFLECTION PRIORITY (R029)`',1)
        x=x.replace('日期：2026-08-31','历史恢复日期：2026-08-31；当前问题校准：2026-09-11（§8）。',1)
        x=x.replace('5. **宇宙分层事实**：对象理论只能分层地把较低层结构作为较高层对象处理，不存在无条件同层\n   “所有类型的类型”。','5. **宇宙分层事实**：标准规则不提供无条件的同层 `U:U`。把宇宙本身当作类型需处理层级，\n   但原始语法可以编码为小型数据，不能因此断言每个语法递归或求值调用都必须升层。',1)
        return x+section
    update(topical,topical_edit)
    update('scripts/README.md',lambda x:x+'''\n## R029 · 两问回应与自指覆盖边界\n\n- `tools/bootstrap_r029.py`：恢复revision28完整Git并保存逐文件基线。\n- `session/r029_integrate.py`：保存来源、AGENTS/自指owner校准与原治理checkpoint；不更新旧数学真值。\n- `tools/r029_verify.py`：核新动态依赖与旧字节、源码和Git；不是数学内核。\n- `tools/package_workspace.py`：复用已存在的Git/ZIP/bundle完整恢复工具。\n本轮不新增求值模拟器或同类有限计数，数学部分为文档内完整纸笔推导。\n''')
    save(R+'PLAN.md','''# SELF-REFERENCE-001 当前下一动作\n\n优先问题：一个拟议的内部自评价器，到底覆盖旧语法还是包含自己及反向项的新语法？\n\n先对最小 Bool 输出写出 C、E、d、quote/correctness；只核其中一项能改变判断的准入义务。若不能提供d的合法编码，记录具体类型/阶段阻断，不称执行崩溃；若可提供则应用R029局部对角反证。部分评价允许不返回，带燃料评价返回UNKNOWN，有限层元解释只覆盖指定对象理论；分别保留正例，不让它们被“自指都一样”抹平。\n\nHoTT特定展开可检查原有self-metatheory路线中的语法替换与相干、或类型索引如何阻止上述同域闭包。历史2014文献不是当前不可能性定理。无需先对全部HoTT作安全审计，也不把待证反射完备性宣布为核心公理。\n\n退出：若只重现已知对角边界且无新的自然任务连接，准确保留并转另一机制；不能用更多测试数、路径名字或同行认可冒充突破。RP-B01原生模型仍开放，但不是本问题解释的启动门槛；R026规约与资源方向继续。\n''')
    spec=importlib.util.spec_from_file_location('r029_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
    base=rt.plan(ROOT)
    state=copy.deepcopy(prior);state['revision']=29;state['latest_session']=SID
    for rid in base['review_required']:
        state['records'][rid]['status']='review_required'
        state['records'][rid]['dependency_change_note']='R029 updates governance/self-reference owner; old results not re-certified.'
    docs=[R+p for p in ['USER_MESSAGE_LATEST.md','ASSESSMENT.md','PROOF_NOTE.md','SOURCES.md','PLAN.md']]
    state['records']['U-SELF-REFERENCE-20260911-001']={'kind':'user_direct_questions','path':docs[0],'status':'review_required','depends_on':[],
        'full_sources':[],'source_hashes':hs([docs[0]]),'scope':'Latest user two questions and quoted peer claims; peer assertions are not findings.'}
    state['records']['P-SELF-REFERENCE-001']={'kind':'research_review_and_plan','path':docs[4],'status':'review_required',
        'depends_on':['U-SELF-REFERENCE-20260911-001','P-RP-B01','A-EARLY-GEMINI-001'],
        'full_sources':[topical]+docs[1:4],'source_hashes':hs([topical]+docs[1:]),
        'paper_scope':'Conditional same-domain self-inclusive evaluator diagonal; known mechanism, no native verification',
        'formal_status':'NOT_RUN','reality_bridge':'OPEN'}
    sp=P+'sessions/'+SID+'/SESSION.md'
    state['records'][SID]={'kind':'session','path':sp,'status':'review_required',
        'depends_on':['P-SELF-REFERENCE-001',prior['latest_session']],
        'full_sources':docs+[topical],'source_hashes':hs(docs+[topical]),'scope':'Bounded user questions/review/authorized documentation; full business cognition not certified'}
    state['active']=list(dict.fromkeys(['P-SELF-REFERENCE-001']+state['active']))
    state['review_due']=list(dict.fromkeys(state['review_due']+['U-SELF-REFERENCE-20260911-001','P-SELF-REFERENCE-001',SID]))
    state['local_git'].update(inherited_head='ce5e8f3aed974ef11a252bafeb67b3d8df16bea2',pre_checkpoint_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),final_head='See actual Git HEAD and R029 delivery report',history_origin='Inherited complete revision28; no reinitialization')
    memory=f'''# MEMORY · revision29\n\n当前根 `{ROOT}`；继承revision28完整Git，旧HEAD ce5e8f3aed974ef11a252bafeb67b3d8df16bea2，保全提交5116713。最新Session：{SID}。\n\n## 用户两问与方法纠偏\n直接回答为什么慢：近期重复规则审计、Trap校准和同行往来挤占候选生成；不能用“理论防线强”全数解释，也不能将目标缩窄为纯核心已过静态检查的发散。自指/反射旧专题早已存在，现恢复优先探索。\n\n## R029吸收与边界\n保留研究理论自身评价/审查的方向。给定E:C→C→Bool，d(x)=not(E(x,x))不能在同一C有全输入忠实代码。条件对角证明完整写在reviews/SELF-REFERENCE-001/PROOF_NOTE.md；这是已知机制，没有LEM/UA/HIT/物理假设，不是已发现HoTT内部矛盾。反射范围、类型和引用闭包需真实构造。总函数不等于瞬间；宇宙不是运行时时钟；语法元理论不等于全能真理/终止审查；受限/类型化/部分自解释可成功。\n\n## 已有认识未丢失\nR001来源缺口保留；R014/015的Done负例与商/真像正例、R016非规范项、R017局部证书、R024/025代码闭包、R026规约/资源、R027Σ、R028全称Reach过强全部保留。RP-B01模型内化仍OPEN，不提升旧NOT_RUN，不重复其有限模型计数。\n\n## 本轮实际范围\n完成当前原文保全、限定一手来源核查、纸笔条件推导和治理/owner更新。没有新数学模拟器、原生HoTT/Lean验证或外部AI会话；不再等待Gemini来信。本轮只作有界两问评估，未完整加载第五闭包与全量动态集合；不称全业务gate通过，不修改全文政策。\n\n## 下一动作\n优先固定一个反射提案的代码域与对角闭包，查清第一项真实断点；随后再按该缺口选择类型化、分阶段或语法相干研究，不先要求整个HoTT模型完备。原问题的双向现实相对目标与九方向不改。\n'''
    frontier='''# HoTT 研究前沿 · revision29\n\n## 当前探索优先：自指/反射覆盖\n用户直接要求审视理论自身。已有最小条件对角E/d/Rep，但原生具体语法的同域覆盖桥梁仍OPEN。接下来查代码与输入的类型一致性、评价器是否在其覆盖语言、反向项是否有代码以及正确性；不能直接假设这些成立后归罪于核心。见SELF-REFERENCE-001/PLAN.md与原self-reference owner。\n\n## 保留的收敛工程\nRP-B01真实编译模拟和原生HoTT模型对应尚未完成。R024/025代码、R027/028局部全局作用域校准不再重复计数；有新工具/新反例才重做相同审计。\n\n## 非排他探索\nR026规约/资源与R027Σ有效范围继续：理论/审查者加入自身后，是新环境，旧保证不能自动覆盖新反向项。R014/R015正反结果与R016求值校准保持，不自动重开。同行通信服务共同认识而非任务调度，当前无需发出新信；九方向与双向目标保持。\n'''
    lessons=(ROOT/(P+'LESSONS.md')).read_text()+'''\n## R029 · 自指并非免疫，也不是任何自指必然崩溃\n\n- 写出反向函数d容易；决定性条件是它在同域评价器范围内的合法代码与正确性。仅需d这一项覆盖即可对角矛盾，不必假设所有数学函数可枚举。\n- 总函数不等于瞬间交付、统一截止或物理一步；无限宇宙模式不等于每次有限调用无限升层。\n- 语法编码/代换引理、类型检查、求值、完备真理和全局可靠性要分开。内化部分元理论不需要全能评价一切。\n- 类型化Fω自解释与分阶段/部分解释是反全称的对照，不能用未经类型核查的对角句否定所有自解释。\n- 原自指专题已有历史资产，不以新来信重新命名成首创；不让同行认可/反驳循环替代自主生成。\n- 原生规范性/内核范围随具体演算；Gemini新添的“必须纯核心通过静态检查”不成为用户目标的新排他条件。\n'''
    resume=f'''# 接续 revision29\n\n最新 {SID}。按原治理恢复；本页不替代第五闭包/三问及动态全文。\n\n先读SELF-REFERENCE-001原文、ASSESSMENT、PROOF_NOTE、PLAN和现有self-reference owner。本轮已直接回答用户两問并重新调度自指，不需要新Gemini认可。最小反射对角是条件已知机制，不是HoTT实际崩溃；目前真实代码域/引用闭包仍待构造。\n\nR026/027/028旧成果与全部records保留；RP-B01原生对应不关闭、不作为自指解释的万能前置。无新数学测试或原生执行，只有治理维护脚本；不伪造工具不可用的新日志。文件哈希不证明全文认识，跨Session照原要求恢复。所有新代码scripts先存再调，Git本地、无远端。\n'''
    session=f'''# {SID}\n\n## 任务与输入\n当前用户询问为什么研究缓慢、HoTT如何面对自身自指，并授权吸收有价值认识到治理与研究文档。最新版原消息完整保存在{docs[0]}，前一重复消息不被当作额外新定理。本轮继承revision28，不回退早期分支。\n\n## 实际行动\n读取根AGENTS、两项Skill、协议、MEMORY/FRONTIER/RESUME/LESSONS、完整原self-reference owner及相关计划/运行器接口。部分聚合工具输出曾截断，随后补读治理关键尾部；没有认证全动态业务全文门禁。repo-cognitive-closure技能本地缺失，未伪称执行。\n\n给出C/Bool/E/d/Rep的短条件对角证明，区别数学总性、有效总性和瞬时；核查原始HoTT规则、历史Shulman文章、2LTT及Fω自解释作者摘要。正文明确哪些是Gemini观点、我方推导或一手结果。未分析PDF；未运行原生证明助手或新增数学模拟器。\n\n## 文档变更与原因\n更新AGENTS的直接回应/自指调度规则与原self-reference owner当前§8，原文及改前字节保存。默认全文政策、第五闭包、三问、Skills、Schema、主张矩阵、旧代码和旧结果不变。新的当前工作状态仍由原checkpoint提交。\n\n## 验证身份\n纸笔条件推导：PAPER_ARGUMENT_WITH_SCOPE / KNOWN_DIAGONAL_MECHANISM。实际HoTT语法引用闭包/现实桥梁：OPEN。原生：NOT_RUN。无新候选已证内部矛盾，无原创性或全理论自洽认证。\n\n## 接续\n按PLAN直接核一项反射覆盖义务；不将下一封通信、全域模型完备或更多重复有限样本设为开工条件。治理用于记录来路，不替代研究。\n'''
    vals={'MEMORY.md':memory,P+'FRONTIER.md':frontier,P+'LESSONS.md':lessons,P+'RESUME.md':resume,P+'STATE.json':jt(state),sp:session}
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,
             'authorization':'Current user asks direct answers and integration in governance/research documents; existing scripts-first and local Git workflow retained.',
             'files':[{'path':p,'text':t,'expected_sha256':sha((ROOT/p).read_bytes()) if (ROOT/p).exists() else None} for p,t in vals.items()]}
    save('artifacts/r029/checkpoint/BASE_PLAN.json',base)
    save('artifacts/r029/checkpoint/PAYLOAD.json',payload)
    save('artifacts/r029/checkpoint/DRY_RUN.json',rt.checkpoint(ROOT,base['snapshot'],payload,apply=False))
    res=rt.checkpoint(ROOT,base['snapshot'],payload,apply=True)
    save('artifacts/r029/checkpoint/COMMIT.json',res)
    after=rt.plan(ROOT);save('artifacts/r029/checkpoint/AFTER_PLAN.json',after)
    required=set(docs+[topical,sp,'MEMORY.md',P+'reviews/EARLY-GEMINI-001/ASSESSMENT.md',P+'dialogues/GEMINI-001/rounds/008/ASSESSMENT.md'])
    assert required <= {d['path'] for d in after['documents']}
    try:rt.checkpoint(ROOT,base['snapshot'],payload,apply=False)
    except rt.CognitionError as err:
        if str(err)!='STALE_BASE':raise
        save('artifacts/r029/checkpoint/STALE_BASE.json',{'status':'REJECTED','error':str(err)})
    else: raise AssertionError('Stale input accepted')
    summary={'status':res['status'],'revision':after['revision'],'snapshot':after['snapshot'],'prior_records':len(prior['records']),
             'current_records':len(state['records']),'all_old_record_ids_preserved':set(prior['records'])<=set(state['records']),
             'required_dynamic_paths':sorted(required),'native_proof':'NOT_RUN','full_business_cognition':'NOT_CERTIFIED_BOUNDED_REVIEW'}
    save('artifacts/r029/CHECKPOINT_SUMMARY.json',summary)
    print(jt({k:v for k,v in summary.items() if k!='required_dynamic_paths'}))
if __name__=='__main__':main()
