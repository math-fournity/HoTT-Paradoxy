#!/usr/bin/env python3
"""R016 state update using the existing governance transaction API, never raw state edits."""
from pathlib import Path
import hashlib, importlib.util, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
SID='S-ANS-20260910-016-AXIOMATIC-COMPUTATION'
PREFIX='.codex/research/hott/'
SESSION=PREFIX+'sessions/'+SID+'/'

def sha(b):return hashlib.sha256(b).hexdigest()
def main():
    spec=importlib.util.spec_from_file_location('governance_runtime',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
    out=ROOT/'artifacts/r016/checkpoint'
    if out.exists():raise SystemExit('R016 checkpoint artifacts exist; refuse repeated commit')
    out.mkdir()
    before=rt.plan(ROOT);assert before['revision']==15,before['revision']
    state=json.loads((ROOT/(PREFIX+'STATE.json')).read_text())
    recent_git=subprocess.run(['git','rev-parse','HEAD'],cwd=ROOT,check=True,capture_output=True,text=True).stdout.strip()
    drafts=ROOT/'artifacts/r016/draft'
    files=[]
    def add(path,content):
        p=ROOT/path;files.append({'path':path,'expected_sha256':sha(p.read_bytes()) if p.exists() else None,'text':content})
    session='''# S-ANS-20260910-016-AXIOMATIC-COMPUTATION

## 用户本轮完整指令

你过程中的代码，不要扔掉，要回收到你所在的工作目录的scripts目录中，最后应该打包发给我，而且应该用git管理你的工作目录。做完这些之后，请你继续工作。

## 实际顺序与维护结果

从提供的revision15恢复新可写工作目录，先本地Git导入，再回收可得源码，两个里程碑都实际commit后才继续数学操作校准。14个顶层ZIP、10个嵌套ZIP和挂载源文件共300条来源，68份不同内容/扩展源码进入scripts/recovered。旧原路径保留，缺失R001没有冒充找回。

所有本轮采用的实验、测试、运行收据工具和checkpoint/package操作代码先落入scripts/。原Git记录不可恢复；本地新历史明确从rev15导入开始，main分支，无remote/push。

## 研究结果

固定书式公理与命题计算条款已核。b=transport_(X↦X)(ua(not),false)有Bool类型并可证b=true；不因此新增基本归约规则。一个明确primitive-ua的typed操作片段实际得到非规范正常形，而非无限归约。

直接应用等价、refl运输、丢弃未用参数和显式计算定理改写均是正向对照。任意有限已知Bool等价链可递归构造“规范值＋等于原项的证明”，所以没有证明原任务不可计算。

36项新单元测试和254个有限运输链检查通过。声明BASIC下252个非空链非规范；显式定理改写全部得到预期值。原R015纯脚本七组结果完全重现。不是完整HoTT内核、不是cubical、不是原创或独立专家验收。

## 认知／权限／失败

当前110份动态加载集合约1.48MB。闭包全文和三问连续内容曾输出，之后发生真实上下文压缩；完整业务gate NOT_PASSED。未删除任何强制加载或开放记录，数学以局部待复核保存。代码和Git维护按本轮明示授权执行。

没有访问原主机、联网查资料、创建Work、启动其它AI、改模型、运行Lean/Agda或push。一次读取小写finite_checks.py失败后按实际大小写FINITE_CHECKS.py读取；不伪称失败即缺件。所有新实际执行有stdout/stderr/exit收据。

## 证据与接续

完整论证PROOF_NOTE.md、CLAIMS.json、SOURCES.json、SOURCE_EXCERPTS.md、FINITE_RESULTS.json、R015_REPLAY.json、LOADING_EVIDENCE.json和ENVIRONMENT.json是本Session的直接正文。

实际脚本位置：scripts/research/r016_axiomatic_transport.py、scripts/tests/test_r016_axiomatic_transport.py、scripts/session/replay_r015.py；原脚本仍在旧Session。完整代码来源见scripts/RECOVERY_MANIFEST.json。

下一步不重复opaque-ua变体来虚增候选。这个固定呈现边界已有原文提醒。主探索转向局部执行证书是否被实际接口不必要地提升为全域总性要求；须固定程序编码、输入域及正向证书处理，不用“任意partial程序不能作为总函数”冒充HoTT失败。

Checkpoint文件提交与Git commit不是同一件事：本次事务保存为revision16，之后将全部变化做最终本地commit，再打包并在临时目录验证ZIP的.git及bundle均可恢复。最后的Git HEAD以交付验证文件为准，不自引用写入本文件。
'''
    add(SESSION+'SESSION.md',session)
    for p in sorted(drafts.iterdir()):
        if p.is_file():add(SESSION+p.name,p.read_text())
    newrec={'kind':'unreviewed_expository_candidate','path':SESSION+'PROOF_NOTE.md',
            'status':'review_required','depends_on':['U-GOAL-20260910-001','U-ASK-20260910-001','C-QUOTIENT-DESCENT-001'],
            'full_sources':[SESSION+n for n in ['CLAIMS.json','SOURCES.json','SOURCE_EXCERPTS.md','FINITE_RESULTS.json','R015_REPLAY.json','LOADING_EVIDENCE.json']],
            'source_hashes':{p:sha((ROOT/p).read_bytes()) for p in ['HoTT/theory-schema/upstream/book-578b85cc/formal.tex','HoTT/theory-schema/upstream/book-578b85cc/basics.tex','scripts/research/r016_axiomatic_transport.py','scripts/tests/test_r016_axiomatic_transport.py']},
            'scope':'Pinned axiomatic UA clauses, an explicitly declared operational fragment, finite certificate-guided recovery. NOT a full HoTT elaboration.',
            'target_fit_note':'Known presentation boundary, not a nontermination/incomputability theorem or confirmed reality-relative paradox.',
            'verification_note':'36 tests,254 finite chains;7 R015 finite groups reexecuted. Full cognition gate and proof-assistant/independent audit NOT_PASSED/NOT_RUN.'}
    state['records']['C-AXIOMATIC-COMPUTATION-001']=newrec
    state['records'][SID]={'kind':'session','path':SESSION+'SESSION.md','status':'review_required',
        'depends_on':['C-AXIOMATIC-COMPUTATION-001'],
        'full_sources':[SESSION+'ENVIRONMENT.json','scripts/README.md'],
        'scope':'User-authorized code preservation/local Git plus scoped research continuation',
        'source_hashes':{},'verification_note':'Transaction/file integrity only; semantic gate not certified'}
    state['revision']=16;state['latest_session']=SID
    state['active']=['U-GOAL-20260910-001','U-ASK-20260910-001','C-AXIOMATIC-COMPUTATION-001']
    if 'C-AXIOMATIC-COMPUTATION-001' not in state['review_due']:state['review_due'].append('C-AXIOMATIC-COMPUTATION-001')
    state['local_git']={'branch':'main','present':True,'history_origin':'supplied rev15 import, not original host history',
                        'pre_checkpoint_head':recent_git,'remote_count':0,'final_head':'See delivered Git repository and external packaging receipt'}
    add(PREFIX+'STATE.json',json.dumps(state,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    memory='''# MEMORY.md：ALL-Markdown 当前工作记忆

## 当前身份与状态

- 实际目录：`/mnt/data/HoTT_workspace_rev16`；提供的rev15完整613文件安全导入。已有真实本地`.git`，branch `main`，无remote。历史从本次导入开始，不冒充旧主机Git历史。
- 当前治理checkpoint：revision16；Session `S-ANS-20260910-016-AXIOMATIC-COMPUTATION`。
- 用户明确要求保全过程代码到根scripts、用Git管理、打包后继续；先完成导入与回收两个Git提交，再推进计算校准。AGENTS新增限定的代码/Git条款，业务Skill1.3.2与治理Skill1.0.0、runtime1.3.0不改。

## 共同问题与证据纪律

目标仍按第五闭包§20—21：找明确Think in HoTT使原本可完成的现实对应出现额外完成困难；一般信息丢失、人工不可能合同或内部⊥不能替代目标。ASK追踪形成、输入、完成、提取与实际承诺，不是万能停机预检。九类方向、发现/确认先于最终归因保持。

完整闭包与三问不是此记忆的可替代摘要。上下文压缩后须按原规则恢复；本轮动态110文件未完成且发生真实压缩，业务gate NOT_PASSED。下列数学仅为待复核局部纸笔与声明模型检查。

## 代码与历史恢复

scripts/RECOVERY_MANIFEST.json登记14顶层ZIP、10嵌套ZIP与挂载源码的300次来源出现，68份不同内容/扩展payload。保留原路径和每份内容SHA，未经审查不批量执行。原R001实验文件仍缺失，不用重建代码冒原运行。

所有本轮新实验、测试、回收、包装、运行记录和状态提交工具落在scripts/。旧代码的实际运行版本保存在Git里；用git log查看真实HEAD而不把本记忆中的旧哈希当最终HEAD。

## 研究前序与本轮差量

R001来源缺口、R006—008时序运输/结构正例、R010—011标签/完成证据、R014Done同域观察障碍均保持原范围，未删除或改判。R015标准商与trim规范表示、Q≃K≃真像的正向构造仍保留：不能再用同一padding反例指控商必须无限搜索。

R016按实际Book条款区分：项有类型、b=true的命题证明、基本归约和规范值交付。自建Bool/函数/opaque-ua片段中coe(ua(not),0)无基本redex且不是Bool值；它是停住的正常形，不是发散。原等价直接计算、refl运输、丢弃参数和命题定理改写均成功。

有限已知Bool等价链可以通过结构归纳，同时计算结果并组合β_UA与ap得到原项等于该结果的证明。因此本例未证明任务不可计算，属于已知计算呈现边界，不宣称新HoTT悖论。

实际36项新单元测试通过；深度0—6共254个运输链样例（252个非空链基本非规范，显式定理改写254个全返回）。每步检查该声明片段中的类型保持；不是完整HoTT内核、不是cubical实现。原R015七组有限结果已重跑，run()全部字段与归档相同。旧无界证明并未因此认证。

## 下一项行动

不继续通过换Bool例子重报opaque-ua困难。该条款本来就在固定Book中，不能把历史“open”当2026全领域现状。

独立核查本轮源到模型的elaboration边界仍开放；若未来有实际HoTT内核环境，再单独形式化该配置。主探索转向某个真实程序接口是否把局部调用的有限执行证书，不必要地替换成全部输入的总性要求。固定程序语法/评价关系，并保留局部证书正例；此下一步尚未执行。

## 实际保存与边界

Checkpoint通过既有事务机制写回；最后Git commit、fsck、ZIP与bundle恢复验证分别记录，不把版本控制当数学证明。无外部搜索、旧主机访问、Work/其他AI、模型切换或远端push；Lean/Agda/Coq未运行。

原认知闭包、三问、Schema、主张矩阵、ZCore及旧研究文件字节不变。旧MEMORY状态在Git和checkpoint before中保留。

回源：`.codex/research/hott/sessions/S-ANS-20260910-016-AXIOMATIC-COMPUTATION/`、`artifacts/execution/`、`scripts/README.md`、`DELIVERY_README.md`。STATE保全部开放问题，Q-R001-EVIDENCE/Q-FRESH/Q-CONTEXT等不因交付而关闭。
'''
    add('MEMORY.md',memory)
    frontier='''# HoTT 研究前沿 · revision16

本表为过程记忆；真值仍须依赖实际证明与规则。

| 位置 | 对象 | 当前结果 | 下一项动作 |
|---|---|---|---|
| 收敛 | C-AXIOMATIC-COMPUTATION-001 | 固定条款＋声明操作片段＋有限链证书；36测试/254样例 | 待实际内核和独立检查；不把toy模型当原书elaboration |
| 探索 | 当前执行证书与全域总性前提 | 仅已选问题，未执行 | 固定真实程序接口与评价关系；检强要求是否实际被使用，而非自行添加 |
| 深层 | ASK在理论工作过程中的证据转换 | OPEN | 精确追踪形成、操作和结果证据，不以缺少某规则直接宣告任务不可计算 |

R015商/真像/规范代表成功，R014观察合同障碍仍按旧范围保留；无坏擦除实证，不再重复全零故事。R016公理化计算校准也不宜反复改名；不透明项不归约成值不是不可停机。

本轮触及DIR02可用性、DIR03形成/交付及弱操作步骤；其它先后、成本、历史、方向、自指、运动不关闭。代码回收和Git不是数学探索方向，不以文件数算新悖论数。

完整业务认知gate本轮NOT_PASSED。当前纸笔与模型结果待复核；全称HoTT非现实性目标仍OPEN。
'''
    add(PREFIX+'FRONTIER.md',frontier)
    oldlessons=(ROOT/(PREFIX+'LESSONS.md')).read_text()
    lessons='''\n\n## R016：代码保全、本地Git与计算校准\n\n- 过程代码先保存到scripts再运行；回收按真实字节与来源保存，没找到的旧脚本不得据聊天摘要伪造。R001原码缺口仍在。\n- 本地Git历史始于本次rev15导入；它保留后续每次修改，不提供旧主机从未取得的历史。原文件被Git跟踪不等于数学正确。\n- Bool类型的非规范正常形与无限归约是不同情况。FUEL_EXHAUSTED也不证明发散。不能加一个无进展轮询器后指控HoTT本身不停止。\n- 命题计算定理不是自动kernel rewrite。本轮显式定理改写模式必须保留身份，不冒称cubical。\n- 有opaque ua的项不一定全部卡住：不需要该值的β函数可丢弃它；refl和保留e直接计算是成功对照。\n- 任意有限已知Bool等价链可同时计算规范值与构造等于原项的证明。有限链样本不能代替一般归纳；该一般论证也不覆盖任意HoTT公理闭项。\n- 自建type checker只保证明确小语言的检查，不是完整HoTT类型/宇宙/elaboration证书。36测试和R015重放都按范围引用。\n- 完整加载后真实压缩使gate失效；本轮维护结果不能修补这一语义资格。保持原要求，不暗改成摘要加载。\n'''
    add(PREFIX+'LESSONS.md',oldlessons+lessons)
    resume='''# 下一Session接续 · revision16

实际目录`/mnt/data/HoTT_workspace_rev16`；有真实.git、main、无remote。迁移后根据当前位置定位，不能再套用旧“没有Git”的历史句子。
最新Session S-ANS-20260910-016-AXIOMATIC-COMPUTATION。按照AGENTS/治理恢复完整认识；此resume不能代替指定原文，上一轮gate未通过。

已实际完成：
1. 原rev15导入Git并打基线tag；68份历史独特源码回收到scripts，300来源边保全，缺R001未伪造。
2. 所有新工具/实验在scripts，运行收据在artifacts/execution。R015源码已按原SHA重跑，七组有限run字段完全相同。
3. 固定书式univalence不增加判断等式。primitive-ua小模型typechecked；无redex/非值与发散分开，36tests和254transport词样例通过。
4. 直接e、refl、丢弃参数与显式命题改写成功。有限已知等价链可构造值＋等于原表达式的证书。
5. 上述不是完整HoTT内核、领域原创或主目标完成；正向证据阻止把已知计算条款误报为不可计算悖论。

先读本轮PROOF_NOTE、SOURCES、CLAIMS、FINITE_RESULTS与实际脚本；其它强制/动态内容仍按原加载集合。

下一项：在真实程序接口中查当前调用执行证书与全域总性假设是否被无必要地绑定。不要任意添加坏Gate；先固定代码类型/评价关系，并提供可完成的局部正例。不再重复Done/padding或opaque Bool同机制。

新代码写root scripts后运行，里程碑与结束前checkpoint＋local commit。交付包含.git及独立bundle，可复查log/fsck；最终SHA见包外验证报告，旧源码摘要不代替执行证据。无后台运行、无自动push。
'''
    add(PREFIX+'RESUME.md',resume)
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,
             'authorization':'Current user explicitly requests code recovery to scripts, local Git, packaging, then continued work. Only this writable sandbox; no remote/model/other AI.',
             'files':files}
    (out/'BASE_PLAN.json').write_bytes(rt.dump(before));(out/'PAYLOAD.json').write_bytes(rt.dump(payload))
    dry=rt.checkpoint(ROOT,before['snapshot'],payload,apply=False);(out/'DRY_RUN.json').write_bytes(rt.dump(dry))
    result=rt.checkpoint(ROOT,before['snapshot'],payload,apply=True);(out/'COMMIT.json').write_bytes(rt.dump(result))
    after=rt.plan(ROOT);(out/'FRESH_PLAN.json').write_bytes(rt.dump(after))
    assert after['revision']==16 and after['latest_session']==SID
    required=[SESSION+'PROOF_NOTE.md','scripts/research/r016_axiomatic_transport.py',SESSION+'FINITE_RESULTS.json']
    assert all(p in {e['path'] for e in after['documents']} for p in required)
    try:rt.checkpoint(ROOT,before['snapshot'],payload,apply=False)
    except rt.CognitionError as exc:
        assert str(exc)=='STALE_BASE',str(exc)
        (out/'STALE_BASE_TEST.json').write_bytes(rt.dump({'status':'PASS_REJECTED','actual_error':str(exc),'writes':False}))
    else:raise AssertionError('Stale write unexpectedly accepted')
    print(json.dumps({'checkpoint':result['status'],'revision':after['revision'],'latest':SID,
                      'fresh_documents':len(after['documents']),'fresh_bytes':after['total_bytes'],'stale_base_rejected':True,
                      'full_cognition_certified':False},ensure_ascii=False))
if __name__=='__main__':main()
