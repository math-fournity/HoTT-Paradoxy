#!/usr/bin/env python3
"""Write this round's public mathematics, evidence identities, and loading limits.
All source-generation logic is preserved in scripts before it is invoked.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]
DRAFT=ROOT/'artifacts/r017/draft'
SID='S-ANS-20260910-017-LOCAL-EXECUTION'
PROOF = r'''# R017：局部完成证书与全域总性——ASK不能无声扩大任务

状态：待复核局部纸笔研究＋保存源码后的有限运行。不是已认证HoTT悖论，不是机器内核证明。
研究族：先证明全部未来调用可终止，才允许执行当前已知可结束的调用，是否是一项实际必要的类型义务？

## 0. 本轮先行维护与真实差量

用户要求将禁止inline代码写入当前AGENTS，并继续工作。完整rev16 ZIP恢复到可写工作目录，继承已有.git四个提交，不重新初始化历史。先修改原代码政策、删除“临时先运行后补存”的例外，再本地提交；随后所有新加载、实验、测试、记录、checkpoint与制包代码都先保存到scripts再按路径调用。没有解释器-c、-e、stdin执行或notebook新代码运行。

R016已经区分opaque-ua的非规范正常形与发散，并给出有限运输链的证书保留。该已知呈现边界不是本轮重复主线。
本轮增量：
1. 基于真实Π/Σ/自然数递归与唯一选择规则，构造按当前输入证据求值的总函数，不需要程序全域总性。
2. 提出一个精确的程序包装P_(M,u)：所有程序在输入0都一步返回；其全域总性恰与M(u)不停机等价。
3. 将“万能全域批准”加强到仅要求最终批准所有真正总的程序；在有效通用模型下，连这个单向完全性也不可能。
4. 用有限状态/寄存器语法与有界解释器实现包装，分别检查正常终止、证书验证、未知燃料耗尽和真正的非终态自环。
5. 给出HoTT内部的局部证书与收敛域正例，排除“HoTT强制当前调用先获全域许可”的泛化。

## 1. 先固定问的到底是哪件事

任务L：给定程序p、当前输入x和一份有限执行证据，验证并返回本次的输出。
任务G：给定程序p，先取得它对所有输入都结束的证书，再允许执行某个当前调用。

G可以是一项明确且有用的全域接口；它不是L的同义表达。本轮检验的是从L到G的无必要升级，而不是否认全域总函数的意义。
ASK需要说明当前要求的范围。不能把“有一份证明即可核查”写成“系统能为任意真命题找到证明”，也不能把“没有全域证书”写成“已知当前调用不合法”。

## 2. 用HoTT能合法表示的语法和有限步语义作为对象

固定一个有效的、确定性的程序语法Code与集合类型Config、初始函数init(p,x)、单步函数step。终止配置带自然数输出，且为吸收状态。

step: Config -> Config 是处理一个有限代码/配置的总函数。无限执行是研究对象的行为，不是step函数自身递归不终止。

定义迭代：
  iter(0,c)=c,
  iter(suc t,c)=step(iter(t,c)).
它沿Nat结构递归，正是Book formal.tex 383—409允许的类型构造，而非在理论内偷偷加入无条件fix。

定义E(p,x,t,v)：“从init(p,x)运行t步已经处于返回v的终止状态”。固定有限t后，E可由有限模拟核对；程序是否最终结束仍未因此可判定。

可携带原始有限证据：
  RunCert(p,x) := Σ(t:Nat). Σ(v:Nat). E(p,x,t,v).
该类型可以合法形成而没有元素。形成它不预设任何程序都结束。

不同证书可以报告同一个值：终止配置吸收后，可取更大的t。所以RunCert不自动是命题，不得把确定性误说成“任意执行证书都相等”。

## 3. 正向定理：只凭当前输入的证书，就能构造正确的局部求值

定义命题化的收敛和输出关系：
  Conv(p,x) := || RunCert(p,x) ||,
  R(p,x,v) := || Σ(t:Nat). E(p,x,t,v) ||,
  Out(p,x) := Σ(v:Nat). R(p,x,v).

### 3.1 Out是命题，而RunCert不必是

若两个有限执行证据给出v和v'，取max(t,t')，由确定性和终止吸收性质得到v=v'。
从截断存在中消去到该等式是合法的，因为Nat为集合，v=v'是命题。R的每个纤维又是命题，故Σ的相等规则给出isProp(Out(p,x))。

### 3.2 合法消去

给定(t,v,e):RunCert，构造(v,|(t,e)|):Out。
因为Out已是命题，可沿截断消去得到：
  finish_p,x: Conv(p,x) -> Out(p,x).
再投影其自然数值。

这使用Book logic.tex §3.9的唯一选择技巧：先以附加条件唯一刻画答案，再向命题型消去，最后投影。未从任意截断类型非法选择原始执行历史。

于是定义：
  Dom(p) := Σ(x:Nat). Conv(p,x),
  evalOnDom_p: Dom(p) -> Nat.

它是一个完整的HoTT函数，定义域是已提供局部收敛证据的输入。不存在前置义务“先证明p对所有Nat都终止”。

显式RunCert输入还可直接投影，无需命题截断。对来自实际有限轨迹的证书，验证程序只回放有限步。
对一个由不透明公理提供的Conv项，本节只给出数学项及规格，不能无条件宣称任意公理化实现都能求值出数值；R016的计算界限继续有效。

### 3.3 这是自然的最大合格输入域，而不是隐藏的万能批准器

若另一种输入资格A(x)带有已给定的映射
  a_to_conv: Πx. A(x) -> Conv(p,x),
就有保留原输入的映射
  (x,a) |-> (x,a_to_conv(x,a)) : Σx A(x) -> Dom(p).

任何带有同样运行正确性证明的输出函数，都与evalOnDom沿此映射所得函数逐点相等；原因是Out的答案唯一。
这里说的是相对于已提供证据的因子化，不是一个算法能决定全部Dom成员，更不是一个自动给所有收敛输入产生证书的总函数。

### 3.4 全域总性究竟做什么

  Tot(p) := Π(x:Nat). Conv(p,x).
得到Tot后当然可以在所有Nat上求值：evalOnDom(x,tot(x))。
反过来，若某个函数同时给出每个输入上的真实执行正确性/收敛证据，就能构造Tot。

因此，全球域函数接口与局部有证据输入接口承担不同的规格。HoTT的Π规则要所有域元素都有输出，是对其所写域负责，并不禁止使用更精确的Σ域。

## 4. 一个所有当前调用都立即结束的程序族

在一般有效程序模型中，给定代码M及固定输入u，构造有限代码P_(M,u)：

  对输入n=0：直接返回0。
  对输入n>0：只模拟M(u)前n步；
      若在这个界限内观察到停机，进入固定的永久自循环；
      否则返回0。

有限模拟本身必定结束。P不是被不加证明地声明成HoTT的Nat->Nat总函数；它是Code中的语法对象。它的step及有限迭代仍是HoTT中合法的总函数。

### 4.1 当前调用统一有证据

  Π(M:Code). Π(u:Nat). RunCert(P_(M,u),0)
可统一构造：判断zero分支后立即Done(0)，不调用M，不等待M，也不查看M是否全域终止。

具体解释器的计数为一条包装机转换；这是模型中的步数，不是物理时间常数。

### 4.2 全域总性却要求检查无限未来

  Tot(P_(M,u)) <-> ¬ Halt(M,u),
其中Halt(M,u)为M(u)具有某个有限停机证据。

若M(u)从不结束，任何有限n都检测不到停机，因此P(n)返回0。
若M(u)在h步结束，取n>0且n>=h，P(n)就进入永久自循环，不可能给出收敛证据。
在HoTT内部的构造性表达中，使用有限模拟的可判定分支、截断向命题消去和显式自环不终止证明即可给出相应两个方向；没有把“未见停机”整体升级成不可判定判断的答案。

终止时刻采用HALT指令也占一步的约定h>=1。即便另一语义允许h=0，取n=h+1即可，本论证不依赖边界约定。

## 5. 不只是不存在完备判定器，连“所有真总程序最终都批准”也办不到

本节是关于有效通用程序模型的元层反证。前提明确包括：有效代码枚举、统一有限模拟、上述包装的有效构造，以及可编程的对角化。它不是仅凭两条小寄存器指令枚举证明机器通用性。

假设有一个有效批准程序G：
1. 一旦G(P_(M,u))批准，就保证P_(M,u)对全部输入终止（可靠性）；
2. 每个真正总的P_(M,u)，G都会在某个有限时刻批准（正向完备性）。
对非总输入，G可以不返回，不要求它总是拒绝。

由§4，G便半判定了M(u)不停止。M(u)停止本身可通过逐步运行来半判定。
将两个过程公平交替：一个每次推进一步M(u)，另一个每次推进一步G(P_(M,u))。若M停则前者最终见到；若M不停则由完备性后者最终批准。两者都可靠，于是得到总的停机判定H。

对角化：构造D(y)，若H(y,y)说停机就永久循环，否则立即停止；在自己的代码d上，H(d,d)的两种答案都与D(d)矛盾。因此G不能同时满足两项。

### 有限可检查证明系统的推论

若一个固定系统S具有有效枚举的有限证明/证书，并对本程序族的总性判断可靠，则可枚举其证书、运行验证器，从而半判定哪些P获得了全域许可。
若它为每一个语义上真正总的P都提供证书，就构成不可能的G。
所以至少有语义上真正总的P不能获得该固定系统中的全域证书；但P(0)仍具有统一的一步局部证书。

这里需要相关语义可靠性，不能以“形式系统一致”无条件替代。也没有选定一个具体HoTT实现、构造一个已独立证明在其中不可证的具体程序。我们得到的是上述清楚前提下的一般存在/不完备覆盖结果。

这个现象的完成困难来自怎样的接口升级：为了执行已拿到局部证书的P(0)，先要求拿到Tot(P)。这会把本来立即返回的任务接到另一项更强、不能被统一完全保证的任务上。

## 6. 有限测试全部绿，为什么仍不构成全域资格

对任意有限测试上界K，选择一个恰在K+1步停机的M。
则所有n<=K的P(n)返回0；而P(K+1)进入永久自循环。

因此，看到任意固定的初段测试全部成功，不足以确认此程序族的Tot。
这是按K可直接构造反例的一般纸笔事实。程序中只检查K=0..8，用来检测边界实现，未从九个例子外推一般定理。

它也不意味着测试没用：局部有限执行证书可靠地确认它实际检查的那个输入。问题在于把已检查输入范围扩大为全部Nat。

## 7. 实际程序与有限检查

scripts/research/r017_local_execution.py定义：
- 明确的HALT/INC/DECJZ/JUMP寄存器语法、合法跳转和配置；
- 确定性单步及吸收终态；
- 有界执行器和有限轨迹验证器；
- P_(M,u)的branch/probe/spin/done包装状态；
- 仅对可达的非终态固定配置提供显式自环证据。

每个执行都给fuel。FUEL_EXHAUSTED不解释成发散；只有可达spin状态c且step(c)=c，才产生独立自环证据。一个一直增加寄存器的运行可以耗尽fuel而不重复配置；代码不会给它伪造循环证明。

有限全集：两寄存器、两条指令，每条有16种合法选择，共256个程序；固定输入u=0..3，包装输入n=0..8，共9216次运行。
其中1024个n=0调用都恰一步返回，未模拟M；正输入中6746次返回、1446次给出可达spin见证。
42项单元测试通过，包括伪造证书、改输入、改程序、错误输出、燃料边界、终态padding、多份证书同一值、无进展与发散的区分、以及scripts-first政策。

该实验不实现一般HoTT内核，没有以有限程序库证明通用停机不可判定，也没有实测一个完备总性证明器。

## 8. 反向核查及目标适配

1. HoTT的合法Π构造要求域内所有输入有值，但没有要求所有关于Code的提问都先取得Tot。
2. 局部原始RunCert、局部Conv以及有证据的Dom均给出成功接口。
3. 对有限step、有限证书验证，外部M可以无限运行；这不使step和验证器自身不终止。
4. 如果规格原来就要求一个全域正确总函数，要求Tot并非不必要的负担；不能偷偷把原任务缩成输入0来指控它。
5. 若原任务只要求当前已完成调用，追加Tot是被检验的建模/接口选择，不是已证明HoTT强制的规则。
6. 一个特定M很容易判明不停机，不反驳§5关于所有M的统一保证；一个固定S不能覆盖全部真Tot也不意味着所有局部证明都无效。

本轮没有找到实际HoTT软件或原书规则强制这种坏Gate的证据。故结果为：局部证书的正向构造＋过强全域批准的条件障碍，仍未命中“真实理论操作制造完成困难”的全部对应。

这使当前分支获得明确停止重复的理由：不再追加不同P_M例子来宣称发现新悖论。下一项应检查具体的递归/定义准入接口，而不是重新假设一个万能总性门禁。
特别保留一个有区分力的方向：同一有限函数的实现身份是否必须与任意给定的partial代码整体等价，才允许使用其局部结果？如无这种实际承诺，应收束该指控并转移搜索方向。

## 9. 来源与认识/运行边界

本轮只使用工作目录中的固定原书来源与已完成的研究记录，没有外部联网检索。
formal.tex 198—219的结构递归规定、383—409的Nat归纳/计算、1143—1171的限定系统proof-checking说明；logic.tex 801—838的唯一选择；CORE_RULES C05/C06/C09/C17。完整摘录与sha见SOURCE_EXCERPTS.md/SOURCES.json。

不把原书对基础系统的检查/规范化结论扩张到全部HoTT及未来演算；不声称这个标准计算论反证有新颖性。内核、独立专家和全领域文献比较NOT_RUN。

本次确实重新输出了指定第五闭包第1—2416行与三问第1—619行，包括所有附件。按当前STATE完整加载集合为122文档、1546017字节，91页；本轮只输出前12页并定点回查本任务原规则和R016，未完成剩余动态全文。工具不认证模型完整性，不伪报发生了本轮未观测的压缩。
因此本研究继续以待复核局部纸笔记录保全，不宣称业务Skill全部前置通过。明确授权的AGENTS修改、保存代码、Git管理和checkpoint可分别核验；没有为放行研究删改强制加载表、旧开放记录或治理引擎。
'''


def sha(b):return hashlib.sha256(b).hexdigest()
def write(path,text):
    p=DRAFT/path
    if p.exists():raise RuntimeError(f'Will not overwrite {p}')
    p.write_text(text,encoding='utf-8')


def main():
    DRAFT.mkdir(parents=True,exist_ok=True)
    write('PROOF_NOTE.md',PROOF)
    source_ranges={
        'HoTT/theory-schema/upstream/book-578b85cc/formal.tex':[(198,219),(383,409),(1143,1178)],
        'HoTT/theory-schema/upstream/book-578b85cc/logic.tex':[(801,838)],
        'HoTT/theory-schema/CORE_RULES.md':[(103,161),(186,206),(353,365)],
    }
    sources=[]; excerpts=['# R017实际所用规则摘录\n\n仅局部读取，不冒称本轮审查完整HoTT元理论。\n']
    for rel,ranges in source_ranges.items():
        p=ROOT/rel; raw=p.read_bytes();lines=raw.decode().splitlines()
        sources.append({'path':rel,'sha256':sha(raw),'line_ranges':ranges,'role':'local pinned source'})
        for first,last in ranges:
            excerpts.append(f'\n## {rel} lines {first}–{last}\n\n')
            excerpts.append('\n'.join(f'{i} | {lines[i-1]}' for i in range(first,min(last,len(lines))+1))+'\n')
    write('SOURCE_EXCERPTS.md',''.join(excerpts))
    write('SOURCES.json',json.dumps({'sources':sources,'web_search':False,'metatheory':'Self-contained conditional computability argument; no broad field novelty review'},ensure_ascii=False,indent=2)+'\n')
    claims=[
        ('T1','RunCert可有限核验，不需要全域Tot','PAPER_CONSTRUCTION_AND_FINITE_TESTS','model-local computation'),
        ('T2','以Conv为资格的Dom中可构造evalOnDom','PAPER_PROOF','HoTT set fragment; explicit truncation and deterministic value'),
        ('T3','所有P_(M,u)(0)一步返回，Tot(P)当且仅当M(u)不停止','PAPER_PROOF_AND_FINITE_INSTANCES','Exact bounded-probe family, not arbitrary original HoTT terms'),
        ('T4','有效通用模型不存在可靠且对真Tot正向完备的全域批准器','CONDITIONAL_METATHEOREM','Effective universality and semantic soundness explicitly assumed; no finite certification'),
        ('T5','任意有限测试前缀不保证全域Tot','PAPER_PARAMETRIC_COUNTEREXAMPLE','K-indexed construction; tested K=0..8'),
        ('TARGET','实际HoTT接口强制坏的全域准入','NOT_ESTABLISHED','HoTT局部证书正例保留，不指控核心已经如此'),
    ]
    write('CLAIMS.json',json.dumps({'session_id':SID,'task_version':'local-global/v1','claims':[{'id':a,'statement':b,'status':c,'scope':d} for a,b,c,d in claims],
               'formal_kernel':'NOT_RUN','independent_review':'NOT_RUN','originality':'STANDARD_MECHANISM_NOT_CLAIMED_NEW',
               'full_business_cognition':'NOT_PASSED_DYNAMIC_SET_INCOMPLETE','stable_claim_matrix_modified':False},ensure_ascii=False,indent=2)+'\n')
    result=json.loads((ROOT/'artifacts/r017/RESULTS.json').read_text())
    write('FINITE_RESULTS.json',json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    execution=json.loads((ROOT/'artifacts/r017/execution/01-tests.json').read_text())
    count=int(re.search(r'Ran (\d+) tests',execution['stderr']).group(1))
    assert count==42 and execution['exit_code']==0
    plan=json.loads((ROOT/'artifacts/r017/cognition/PLAN.json').read_text())
    emitted=sorted(int(p.stem.split('-')[1]) for p in (ROOT/'artifacts/r017/cognition').glob('emitted-*.json'))
    write('LOADING_EVIDENCE.json',json.dumps({'snapshot':plan['snapshot'],'documents':len(plan['documents']),'total_bytes':plan['total_bytes'],
         'total_pages':91,'pages_emitted':emitted,'full_cognition_gate':'NOT_PASSED','reason':'Remaining dynamic complete texts not emitted; no invented compaction event',
         'fifth_closure_lines':[1,2416],'three_questions_lines':[1,619],'raw_page_metadata_path':'artifacts/r017/cognition','mandatory_policy_unchanged':True},ensure_ascii=False,indent=2)+'\n')
    scripts=['scripts/research/r017_local_execution.py','scripts/tests/test_r017_local_execution.py',
             'scripts/session/r017_cognition.py','scripts/session/register_scripts_only_policy.py','scripts/tools/restore_rev16.py']
    write('CODE_AND_RUNS.json',json.dumps({'scripts':[{'path':p,'sha256':sha((ROOT/p).read_bytes())} for p in scripts],
         'tests':count,'test_execution':'artifacts/r017/execution/01-tests.json','experiment_execution':'artifacts/r017/execution/02-finite-model.json',
         'new_code_execution':'saved files invoked by path; no inline interpreter code','scope':'finite operational model only'},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'draft':str(DRAFT),'files':[p.name for p in DRAFT.iterdir()],'tests':count,'claim_count':len(claims)},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
