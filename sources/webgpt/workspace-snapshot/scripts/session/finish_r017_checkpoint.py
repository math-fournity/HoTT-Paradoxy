#!/usr/bin/env python3
"""R017 controlled state update. Uses the existing transaction API; no raw STATE edits.
Only new Session files and the five permitted working-memory files are written.
The emitted set is checked for routing, not claimed as read into model context.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
SID = 'S-ANS-20260910-017-LOCAL-EXECUTION'
CANDIDATE = 'C-LOCAL-EXECUTION-001'
PREFIX = '.codex/research/hott/'
SESSION = PREFIX + 'sessions/' + SID + '/'

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def git(*args: str) -> str:
    return subprocess.run(['git', '-c', 'core.hooksPath=/dev/null', '-c', 'core.fsmonitor=false', *args],
                          cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()

def main():
    spec = importlib.util.spec_from_file_location('r017_governance_runtime', ROOT / '.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = rt
    spec.loader.exec_module(rt)
    out = ROOT / 'artifacts/r017/checkpoint'
    if out.exists():
        raise SystemExit('Checkpoint record directory exists; do not repeat or overwrite')
    out.mkdir()
    before = rt.plan(ROOT)
    if before['revision'] != 16:
        raise SystemExit('Expected revision16; refuse stale assumptions')
    state = json.loads((ROOT / (PREFIX + 'STATE.json')).read_text())
    old_records = json.loads(json.dumps(state['records']))
    files = []
    def add(path, text):
        p = ROOT / path
        files.append({'path': path, 'expected_sha256': sha(p.read_bytes()) if p.exists() else None, 'text': text})

    request = (ROOT / 'artifacts/r017/policy/USER_REQUEST.txt').read_text()
    add(SESSION + 'USER_REQUEST.txt', request)
    add(SESSION + 'SESSION.md', '''# S-ANS-20260910-017-LOCAL-EXECUTION

## 本轮用户指令

记录到当前工作目录下面的AGENTS.md中：你以后不要写inline的代码，所有代码都应该通过写入scripts目录后进行调用。然后继续下面的工作。

## 实际操作顺序

上传的rev16目录是稀疏挂载；使用完整rev16 ZIP恢复可写工作副本，继承其.git及原四个commit。恢复脚本先写scripts/tools/restore_rev16.py再调用，没有新建虚构Git历史。

先通过scripts/session/register_scripts_only_policy.py原位修改AGENTS，保存改前原文、用户指令和diff，commit b3575a8。删掉临时先执行后补存例外，涵盖所有新代码。随后源码、测试、加载、证据和状态工具均先保存scripts再按路径运行。新的代码与初稿、实测输出已commit 6c1c528；后续修订保留初稿历史。

## 研究产物

HoTT中确定性运行的输出图Out为命题（原始RunCert不必唯一），可从局部Conv合法消去得到唯一输出，构造Dom(p)=Σx Conv(p,x)上的总求值。不存在核心要求把全部输入Tot前置于这个局部合同。

在有效程序语法中构造P_(M,u)：输入0立即返回；正输入只模拟M(u)前n步，发现停机即进入永久自环，未发现则返回。因此所有P(0)都有统一一步证书；Tot(P)与M(u)不停止等价。

可靠且最终批准全部真Tot的有效全域批准器不存在，证明用有效通用模型和对角化。有效证明系统的相关推论额外需要语义可靠性。没有从有限枚举推出这些元定理，没有指控某个HoTT库实际采用此坏Gate。

42项测试通过；256程序、4固定输入、9包装输入构成9216次实际运行。1024个zero调用无需模拟M；6746正输入返回，1446有可达非终态自环证据。fuel耗尽只表示未知，没有伪报发散。九个有限前缀反例只是一般K构造的实例。

## 认识与权限边界

本轮实际发出第五闭包1—2416行、三问1—619行的全文；动态集合为122文档/1546017字节、91页，实际发出前12页。初稿之后实际发生压缩且没有完成压缩后重新全文读取。因此full business cognition NOT_PASSED，数学继续为待复核局部记录，不声称独立理解、HoTT内核或原创验收。

没有删除强制加载、修改旧闭包/三问/Skills/Schema/主张矩阵/数学源码/旧研究记录，未联网、未访问原主机、未运行Lean/Agda/Coq、未创建Work/其它AI、未改模型、未push。维护与Git按用户明示授权执行。

## 保存与下一步

PROOF_NOTE、SOURCES、SOURCE_EXCERPTS、CLAIMS、FINITE_RESULTS、LOADING_EVIDENCE、CODE_AND_RUNS及ENVIRONMENT记录本轮范围。新源在scripts/research/r017_local_execution.py和scripts/tests/test_r017_local_execution.py，实际argv/stdout/stderr/exit在artifacts/r017/execution。

不再仅重复人工加上Tot门禁的反例。下一项必须追查实际定义/递归准入是否要求不必要的全域代码等价或总性；若没有真实承诺，保留局部证书成功结果，转到其它ASK/时间接口。原任务本来要求全域总函数时Tot合法，不能改成局部任务来指控它。

本次revision17通过原治理事务API提交，后做本地Git commit与包外恢复验证。最终HEAD见Git/交付验证，不自引用写进本文件。无后台工作承诺。
''')
    draft_paths = []
    for p in sorted((ROOT / 'artifacts/r017/draft').iterdir()):
        if p.is_file():
            add(SESSION + p.name, p.read_text())
            draft_paths.append(SESSION + p.name)
    code_paths = ['scripts/research/r017_local_execution.py', 'scripts/tests/test_r017_local_execution.py']
    local_sources = ['HoTT/theory-schema/upstream/book-578b85cc/formal.tex',
                     'HoTT/theory-schema/upstream/book-578b85cc/logic.tex']
    state['records'][CANDIDATE] = {
        'kind': 'unreviewed_expository_candidate', 'path': SESSION + 'PROOF_NOTE.md',
        'status': 'review_required', 'depends_on': ['U-GOAL-20260910-001','U-ASK-20260910-001','C-AXIOMATIC-COMPUTATION-001'],
        'full_sources': [p for p in draft_paths if not p.endswith('/PROOF_NOTE.md')] + code_paths,
        'source_hashes': {p: sha((ROOT/p).read_bytes()) for p in local_sources + code_paths},
        'scope': 'Current-input execution certificates and HoTT convergence-domain positive construction; conditional universal-model totality approval obstruction.',
        'target_fit_note': 'No actual HoTT rule/software shown to impose the bad totality gate. Standard mechanism; not a confirmed HoTT paradox.',
        'verification_note': '42 finite tests;9216 wrapper runs. Infinite metatheorem separately argued; no kernel/independent audit. Full cognition gate NOT_PASSED.'
    }
    state['records'][SID] = {
        'kind':'session','path':SESSION+'SESSION.md','status':'review_required','depends_on':[CANDIDATE],
        'full_sources':[SESSION+'USER_REQUEST.txt', SESSION+'ENVIRONMENT.json'],
        'source_hashes':{},
        'scope':'Actual scripts-first AGENTS amendment, inherited local Git and scoped R017 continuation.',
        'verification_note':'Checkpoint integrity is separate from cognition and mathematics.'
    }
    for record_id, record in old_records.items():
        assert state['records'][record_id] == record, record_id
    state['revision']=17
    state['latest_session']=SID
    state['active']=['U-GOAL-20260910-001','U-ASK-20260910-001',CANDIDATE]
    for record_id in (CANDIDATE,SID):
        if record_id not in state['review_due']:
            state['review_due'].append(record_id)
    state['local_git']={'branch':git('branch','--show-current'),'present':True,
        'history_origin':'Inherited supplied rev16 .git, whose earliest imported base is revision15; no original-host history invented.',
        'inherited_head':'b07ac7ecc084a58be814995931b9706f955e4d95',
        'pre_checkpoint_head':git('rev-parse','HEAD'), 'remote_count':len(git('remote').splitlines()),
        'final_head':'See actual repository and package-external delivery verification'}
    add(PREFIX+'STATE.json',json.dumps(state,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    environment={'schema_version':'hott-r017-environment/v1','workspace':str(ROOT),
                 'restored_archive':'/mnt/data/HoTT_workspace_rev16_with_git.zip','git':state['local_git'],
                 'python':sys.version,'scripts_first':'EVERY_NEW_PROGRAM_SAVED_BEFORE_INVOKING',
                 'full_cognition_gate':'NOT_PASSED','proof_assistant':'NOT_RUN','external_search':False,
                 'other_AI_started':False,'remote_push':False}
    add(SESSION+'ENVIRONMENT.json',json.dumps(environment,ensure_ascii=False,indent=2)+'\n')
    add('MEMORY.md','''# MEMORY.md：ALL-Markdown 当前工作记忆

## 当前身份与状态

实际可写目录`/mnt/data/HoTT_workspace_rev17`，从完整rev16 ZIP恢复1767文件，继承其真实.git四个commit。branch main，无remote/push，未重新git init。历史最早为旧rev15导入，不冒充从未取得的旧主机历史。

当前checkpoint revision17，最新Session `S-ANS-20260910-017-LOCAL-EXECUTION`。用户明确要求禁止inline代码；AGENTS已经原位修改并先行commit b3575a8。所有新代码包括临时诊断、文档/加载/checkpoint/打包都先写根scripts再按路径调用；没有“先跑再补存”例外。源码与研究实测先提交6c1c528，最终HEAD以实际Git为准。

## 共同问题与证据纪律

第五闭包§20—21和三问v4仍拥有目标：明确Think in HoTT怎样使原本能完成的现实对应多出完成困难；不以一般信息损失、人工不可能合同或内部Empty替代目标。ASK追踪形成、输入、完成、提取与真实承诺，不是通用停机预检。九方向、发现/确认先于最终归因保持。

本轮指定第五闭包2416行与三问619行曾完整输出；122文档/1546017字节动态集合只输出前12/91页，初稿后实际发生上下文压缩，没有完成压缩后的全文恢复。业务gate仍NOT_PASSED，下述为待复核纸笔和有限模型检查。没有暗改加载政策或关闭旧待复核记录以减少必读量。

## 代码与历史

68份回收源码、300条来源映射仍按原字节保全；未找到的R001原码仍缺失，不能从摘要伪造复现。当前新增研究、42测试、加载、修改、证据、审计和checkpoint工具都在scripts。运行证据在artifacts/r017/execution；初稿后修订也有Git痕迹。

## 本轮研究差量

已核真实Π/Σ、自然数有限迭代与唯一选择。RunCert(p,x)=ΣtΣv E(p,x,t,v)可以有不同padding证书，但确定性使Out(p,x)=Σv||Σt E||为命题。由Conv=||RunCert||向Out合法消去，得到Dom(p)=Σx Conv(p,x)上的总evalOnDom。当前有证据输入不需要全部输入Tot；不透明Conv证明未必在任意公理化kernel中可直接求值，R016边界保留。

有限程序包装P_(M,u)：n=0一步返回0；n>0只模拟M(u)前n步，若发现停机则进入永久自环，否则返回0。全部P(0)有统一当前执行证据，但Tot(P)当且仅当M(u)不停止。对有效通用模型，不存在可靠且最终批准全部真Tot的统一批准器；相关证书系统推论需语义可靠性，不只一致性。

实际42项测试通过；256基础程序×4固定输入×9包装输入=9216次运行。1024个zero调用均一步完成且不模拟M；6746正输入正常返回、1446具有可达非终态固定点证据。燃料耗尽不等于发散。九个K前缀反例仅核实施边界，无界结果另有纸笔证明。没有运行HoTT内核、外审或原创性验证。

R001来源、R006—008时序/结构、R010—011标签与证书、R014—015Done/商/真像、R016不透明ua和有限证书链全部保留原身份。不能把这些正向保全结果遗忘，重新对同一接口声称理论必然失效。

## 下一项行动

本轮没有找到实际HoTT系统强制当前调用先取得Tot的证据。当前局部Σ域是正例；若任务本来要求全域总函数，Tot要求合理。不要继续通过换P_M故事把条件Gate障碍包装成真实HoTT悖论。

下一项只针对实际定义/递归准入或程序表示接口：是否必须先把整个partial代码与一个全域函数对齐，才允许使用已经有有限证书的局部结果？必须找真实规则/声明，保留域限制和有限评价正例。若无此承诺则收束这项指控、轮换其它ASK/时间机制。

## 保存、运行和权限

代码先落盘的政策是此次真实变更，不是建议。没有外部搜索、旧主机访问、Work/其他AI/模型切换、远端push、依赖安装、Lean/Agda/Coq执行。Git和checkpoint互补：前者管源码历史，后者管动态认知；两者不认证数学。

本轮只改变授权AGENTS、五个工作状态及交付/脚本索引，新增本Session/运行/工具文件。第五闭包、三问、Skills、Schema、主张矩阵、数学源码和旧Session未改。前一MEMORY在Git与事务改前字节中保留。

直接回源：本Session PROOF_NOTE/CLAIMS/SOURCES/FINITE_RESULTS/LOADING_EVIDENCE，scripts/README，artifacts/r017。最终包和bundle的真实HEAD与字节验证在包外JSON，不在文档中伪造循环自身hash。全部旧开放事项保留。
''')
    add(PREFIX+'FRONTIER.md','''# HoTT 研究前沿 · revision17

过程记忆，不替代原主张矩阵与直接证据。

| 位置 | 当前对象 | 实际结果 | 下一项动作 |
|---|---|---|---|
| 收敛 | C-LOCAL-EXECUTION-001 | 局部证书/唯一输出/收敛域正向构造；P_M全域准入条件障碍；42测试和9216运行 | 独立核推演，不能把有限code模型说成kernel |
| 探索 | 真实定义/递归准入中的局部任务范围 | 尚未找到坏Gate实际承诺 | 对具体规则做源到规格绑定；不再人为附加万能Tot再证明困难 |
| 深层 | ASK义务怎样跨理论操作保留 | OPEN | 反例和正例一起保留；范围、证据、输入资格不混同 |

本轮触达DIR01依赖范围、DIR02可用、DIR03形成/交付、DIR04终止。其它成本、历史、方向、自指、运动保持，不因近几轮计算族长期失踪。三个位置不是三个AI。

P(0)成功不证明所有P(n)成功；一般Tot不完全批准不证明当前合法提问应被拒绝。RunCert可能多份，Out才唯一。HoTT能在Σ域内表达当前证据，不强制坏Gate。

R015标准商与真像保全、R016证明与归约区分继续作为成功/排除结果。全称HoTT非现实性目标仍OPEN。完整业务认知gate本轮未通过，局部论证待复核。
''')
    old_lessons=(ROOT/(PREFIX+'LESSONS.md')).read_text()
    add(PREFIX+'LESSONS.md',old_lessons+'''

## R017：代码先落盘、局部证书与全域许可

- 所有新增代码必须先写scripts再调用；没有“临时先执行后补存”例外。写源码的heredoc不执行代码；解释器stdin或notebook现场算法不采用。旧脚本版本与失败记录保留。
- 已有Git包应恢复继承，不新init后冒称旧历史。原rev16四个commit完整继承；新政策在研究前先行提交。
- RunCert含步数/轨迹，即使确定性也可能多份。只由确定性证明输出图Out为命题，再合法消去Conv，不能错误宣称所有证书proof-irrelevant。
- Dom(p)=Σx Conv(p,x)提供正确局部求值，Tot(p)服务全域规格。current ASK不应无声升级成万能Totality Gate。
- 不批准某个Tot可以意味着未知，不等于当前输入非法；proof checking与主动发现证明是不同任务。
- 对真Tot可靠且正向完备的有效批准器已足以矛盾，未必需要对否定输入总拒绝。但论证需要有效通用模型和相关语义可靠性，不是有限检查或仅一致性。
- 每个有限测试前缀全通过，仍能有下一输入自环；具体自环以可达非终态fixed configuration证明，fuel耗尽仍是UNKNOWN。
- 条件坏Gate不等于已识别实际HoTT错误；保持局部正例并寻找真实规格，不能只换程序继续讲同一机制。
- 本轮核心全文输出后实际压缩，动态全集也未发完。不能以Git/测试/旧读取字节收据补成完整认知通过；不修改强制加载以掩盖边界。
''')
    add(PREFIX+'RESUME.md','''# 下一Session接续 · revision17

实际根`/mnt/data/HoTT_workspace_rev17`；真实.git/main继承rev16，无remote。最新Session S-ANS-20260910-017-LOCAL-EXECUTION。

首要政策：root AGENTS禁止inline执行新代码。研究、临时工具、测试、加载、状态、打包全部先保存scripts再路径调用。历史程序在其它路径时由已保存scripts包装器核SHA调用，不把字符串当代码执行。

按AGENTS与两Skill全文恢复。此resume不能替代第五闭包/三问/动态记录；本轮122文档加载未完成且发生压缩，gate未通过。不得跳过未读而声称理解完整。

已完成的局部结果：RunCert可有限验证；其output graph Out为命题；Conv->Out可消去；Dom(p)=Σx Conv输入域内有总求值。不需要全程序Tot。P_(M,u)(0)统一一步结束，但Tot(P)恰等于M(u)不停止；不存在可靠且对所有真Tot最终批准的有效Gate（明示通用/可靠性前提）。

代码scripts/research/r017_local_execution.py，测试scripts/tests/test_r017_local_execution.py：42测试/9216wrapper runs真实完成，fuel未知不冒充发散。无限定理未内核化，标准机制不称原创。旧所有源码原路径与68回收副本均保留。

下一动作：核具体递归/定义准入接口是否确实将当前已证调用绑到全域代码等价/总性。先查实际规则，允许缩小域、以代码为数据的有限评价；如无坏承诺就收束而非反复追加P_M例子。不得误把完整Nat->Nat规格的合法Tot要求说成坏Gate。

先读本Session PROOF_NOTE/CLAIMS/SOURCES/FINITE_RESULTS/LOADING_EVIDENCE，再沿真实依赖继续。脚本先行、里程碑checkpoint和本地Gitcommit、交付ZIP/bundle实际恢复。无后台工作、无自动push/其他AI。
''')
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,
        'authorization':'Current user explicitly requests root AGENTS prohibit inline code, all new code under scripts before execution, then continue; prior local Git and final package authorization retained. No remote/other AI/model changes.',
        'files':files}
    (out/'BASE_PLAN.json').write_bytes(rt.dump(before))
    (out/'PAYLOAD.json').write_bytes(rt.dump(payload))
    dry=rt.checkpoint(ROOT,before['snapshot'],payload,apply=False)
    (out/'DRY_RUN.json').write_bytes(rt.dump(dry))
    result=rt.checkpoint(ROOT,before['snapshot'],payload,apply=True)
    (out/'COMMIT.json').write_bytes(rt.dump(result))
    after=rt.plan(ROOT)
    (out/'FRESH_PLAN.json').write_bytes(rt.dump(after))
    assert after['revision']==17 and after['latest_session']==SID
    required=[SESSION+'PROOF_NOTE.md',SESSION+'FINITE_RESULTS.json',*code_paths]
    actual={e['path'] for e in after['documents']}
    assert all(p in actual for p in required),required
    try:
        rt.checkpoint(ROOT,before['snapshot'],payload,apply=False)
    except rt.CognitionError as exc:
        assert str(exc)=='STALE_BASE',str(exc)
        (out/'STALE_BASE_TEST.json').write_bytes(rt.dump({'status':'PASS_REJECTED','actual_error':str(exc),'writes':False}))
    else:
        raise AssertionError('Stale write accepted')
    print(json.dumps({'status':result['status'],'revision':after['revision'],'latest_session':SID,
        'fresh_documents':len(after['documents']),'fresh_bytes':after['total_bytes'],
        'new_sources_routed':True,'old_records_preserved':True,'stale_base_rejected':True,
        'full_cognition_certified':False},ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
