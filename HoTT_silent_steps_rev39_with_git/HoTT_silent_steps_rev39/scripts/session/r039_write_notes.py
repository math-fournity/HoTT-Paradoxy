#!/usr/bin/env python3
"""Persist the R039 mathematical argument, source boundaries and session records."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
R='.codex/research/hott/reviews/SILENT-STEPS-001/'
S='.codex/research/hott/sessions/S-RES-20260911-039-SILENT-STEPS/'
def put(rel,text):
 p=ROOT/rel;p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists():raise FileExistsError(p)
 p.write_text(text.strip()+'\n')
def js(x):return json.dumps(x,ensure_ascii=False,indent=2)

def main():
 put(S+'REQUEST.md','继续')
 put(R+'PROOF_NOTE.md',r'''
# R039：忽略内部停顿，不等于可以忽略发散

日期：2026-09-11。前序R038；状态revision39。
身份：纸笔推导与31项有限模型检查。没有原生HoTT/Lean/Agda/Rocq编译，没有外部独立审查，不认领原创性或HoTT内部错误。

## 0. 连续性与本轮问题

R036—38区分逐类may抽象与当前具体状态的相容提升。R038还证明：在函数外延性下，命题性的当前态提升可以向命题目标Acc消去，从而迁移终止证据；不能把截断一概当成时间信息损毁。本轮保留这一正例，不重做倒计时/逆极限反例。

新问题按R038前沿选择：当实际一步允许被匹配成零步，能否仍从“行为等价”推断必然完成？另检查一种常见定义风险：将有限地跳过停顿的规则不加限制地放入最大不动点。

三项新连接：(1) 常规发散不敏感弱互模拟保留本例的可完成性，但不保留必然完成；(2) 无限制单边余归纳跳过甚至不是等价关系，按它做集合商会合并不同返回值；(3) 真实作者源码以有限跳过计数明确防止该问题。文献规则、自己的推导和Python证据分别记账。

## 1. 明确的标号执行模型

状态F（立即完成）、S（重试）、Z（结束）、W（有限等待）。边为：

    F --done--> Z
    S --tau--> S
    S --done--> Z
    W --tau--> F

`done`是显式可观察的完成事件，不是tau；Z没有边。从Z重新询问“此后是否发生done”答案为否，这不否定到达Z之前已经出现done。程序固定从F/S/W之一开始，本轮不改变此约定。

tau*是有限零步或多步tau闭包。对可见动作a，弱匹配是tau*;a;tau*；对tau，允许匹配tau*（可零步）。对称关系B是弱互模拟，当其每对状态的每一步，都可在另一侧找到这样的有限匹配，并使后继仍在B中。这里采用不额外记录发散的标准弱互模拟定义，不把不同文献中带发散条件的变体合并。

取B包含(F,S)、(S,F)、各状态自身；可直接验证：S的tau自环由F的零步匹配，后继仍是(S,F)；两侧的done由同名done匹配，后继为(Z,Z)。所以F与S弱互模拟。W与F也弱互模拟。

MayDone(s)：存在有限执行，在某一边发出done。
MustDone(s)：每条最大执行都在有限位置发出done。没有公平调度假设；非done死锁是失败。

MayDone(F)、MayDone(S)、MayDone(W)均成立。MustDone(F)与MustDone(W)成立；S具有常值无限执行S,S,...，每一步均为tau，故MustDone(S)不成立。其无限反例由n↦S及自环直接定义，不是观察一段时间以后猜测。

这不证明S永远不能完成：它也可以立即done。被否定的是“所有运行必然完成”。若另行加入公平性排除永久忽略done的调度，改变的是允许的执行集合，必须重新声明业务合同。

本例所有有限可见trace都是空迹或[done]。差别不在删除了done，而在无穷多个内部步可以逐个被零步匹配。每次匹配都有限、代表也能相容，但匹配链未必取得任何进度；这是与R038代表重选/有限前缀不相容不同的机制。

## 2. 真正接入HoTT：MustDone不能从该商上无条件恢复

固定上述有限状态集合与其弱互模拟等价关系~，形成集合商Q。由F~S，商中有[F]=[S]。

有限图上定义mustFlag:F↦1、W↦1、S↦0、Z↦0。若存在m:Q→Bool满足对每个源状态s有m([s])=mustFlag(s)，沿[F]=[S]应用m便得到1=0。因此无此保持规格的下降函数。

同样可以用命题族MustDone，若要求商上族与各源MustDone双向对应，会将F的证明转为S的证明，与明确的tau无限轨迹冲突。这里不必判断所有无限系统的终止性。

相反，mayFlag在这个商上恒定于等价类，可以下降；有限等待W也没有破坏MustDone。

HoTT Book §6.10集合商递归正是要求源函数尊重关系。它不会自动提供m。因此，“商中相等”没有在标准HoTT中推出F/S具有同一个强完成合同。成立的是：这个过程等价不适合作为该合同下的替换原则；正确使用时是规格边界，不是核心矛盾。

R038的Acc迁移要求每条抽象边对应具体当前态的一步。将这一条件削弱成可零步的有限路径，源Acc就不足以阻止目标无限空转，本例给出直接反例。正向补充可采用发散保持的等价，或为零步匹配设置严格下降的良基预算；后者不能靠每次任意重置而允许无限单边跳过。

## 3. 第二项检查：返回值型Delay与反复跳过规则

固定确定性Delay型：now(a)或later(p)。omega=later(omega)表示持续的内部计算。coinductive Delay是这里明确指定的对象语义；本轮不宣称Book HoTT自动包含任何未声明的原生coinductive机制。

收敛p⇓a由归纳规则定义：now(a)⇓a；p⇓a推出later(p)⇓a。因此收敛证据是有限的。对其证据归纳，可证明omega没有任意值的收敛证据。

一个保结果的等价定义是：

    p ≈result q := Πa. (‖p⇓a‖ ↔ ‖q⇓a‖).

它忘掉有限停顿次数，但直接保留有限返回的存在及其值；由定义和归纳，有later^n(now(a))≈result now(a)，omega不等价于now(a)。没有把“所有Delay值可有效判等”写成这个定义的一部分。

作者Xavier Leroy的真实Coq源码提供另一种equitermination表示：最大关系的收敛分支要求两边有同一值的归纳收敛证据；无限的later分支必须双边同时前进。文件中明确给出terminates_equi与diverges_equi等证明。它是普通Coq共享计算片段，不能称为本轮HoTT内核证明。

## 4. 一个错误定义怎样合法地产生错误的“等价”证书

试验关系Bad定义为以下算子的最大不动点：

    F(R)(p,q) :=
      [p=now(a)且q=now(a)]
      或 [p=later(p')且R(p',q)]
      或 [q=later(q')且R(p,q')].

不同于有限跳过，这三个分支全部按最大不动点解释。Bad不是标准HoTT身份，也不是我们声称某个实际库采用了的定义。

对任意q，关系{(omega,q)}已是一个post-fixed relation：omega展开一步还是omega，永远使用左跳过分支。因此Bad(omega,q)。对称地Bad(q,omega)。特别地：

    Bad(now(0),omega)，Bad(omega,now(1)).

但Bad(now(0),now(1))不成立：外层都是now，没有单边later可跳，也没有相同结果分支。

故Bad根本不满足传递性。一个不断产出“跳过”节点的证明对象可以是此错误关系的合法余归纳证明；这不使被比较的计算真的返回。证明定义的正确性与关系是否符合“等价/交付”的预期，是两项任务。

### 4.1 不依赖无限类型也可内化的有限版本

取三个状态r0、r1、o，r0立即返回0，r1立即返回1，o的唯一内部后继为o。对这三个状态的九个有序对按上述算子取最大不动点，得到恰好七对：只排除(r0,r1)、(r1,r0)。有限集合上可通过有限次删除实现，不需要新公理。

若按这个关系生成集合商（或先取其等价闭包再取商），商中有[r0]=[o]=[r1]。因此不存在一个读取商结果的f:Q→Bool，满足f([r0])=0与f([r1])=1。

这不等于在Bool中已经证明0=1。商Q本来允许把不同源元素合并；只有再强加不尊重关系的结果读取函数，才会产生冲突。标准商消去不会无条件发放这个函数。

### 4.2 有限循环证书不是“实际返回”的证书

本轮程序检查一个post-fixed关系证书{(spin,ret0)}时，确实会有限通过Bad规则；同时其Delay执行语义通过可达循环证明spin不返回。它也拒绝{(ret0,ret1)}。

这没有伪造矛盾：两次检查的目标命题不同。把“Bad规则通过”改标成“完成结果相同”，才是未经证明的提升。与之前错误AI模拟器不同，本轮明示每个检查器的精确目标并提供反例，不称其为HoTT type checker。

## 5. 一手正向保护：有限单边预算，而非禁止全部无限行为

Leroy源码还提供带自然数索引的bisim关系。单边跳过使预算减一；双边同时later可重新选择有限预算。源码的说明明确指出，不得允许单边跳过被无限使用，否则now与bottom会被关联。

本轮仅实现该规则的有限循环证书检查：
- (later(now(0)),now(0))：预算1的单边跳过接预算0的now，接受。
- (omega,now(0))：声称永远单边跳过却保持同一预算，拒绝。
- (omega,omega)：每次两边都前进，可以用有限图描述无限双边展开，接受。

从带预算证书获得安全关系，需要对单边预算归纳；不能将“自然数索引存在”本身当作正确性定理。一般保收敛性也有直接证明：对左侧有限收敛证据归纳，将每个有限跳过批次消去到对应的右侧收敛证据。未证明一般循环证书的最优预算或效率。

因此，“任意有限停顿可忽略”与“一个证明可以无限地承诺再忽略一步”有不同语义。无限地生成验证理由，不能代替有限交付；同样，明确描述无限计算的数据也不自动是非法数据。

## 6. 范围：不同弱等价不能混成一个术语

确定性Delay上的≈result保存是否返回及返回值；它可以忘记全部有限耗时。
非确定系统的普通发散不敏感弱互模拟允许保留可能完成，却不保留所有执行必然完成。
Bad单边最大关系更弱，甚至不传递，不能冒用“标准弱互模拟等价”的名字。

三者必须按定义与量词分类。名词里有“weak”“忽略tau”“商”，不自动说明它保留或破坏哪种完成性。

MayDone≠MustDone；非Done死锁≠无穷tau；有限预算耗尽≠发散；source code hash相同≠所有语义定理自动通过。

本轮数学不要求物理时空离散，也不认定一个抽象已经给出真实硬件执行。普通HoTT及不同partiality/cubical/guarded扩展分开。部分性单子的HoTT研究本来就区分强/弱等价及其额外选择原则；本轮只阅读了该论文摘要，不冒充完成了QIIT规则的全篇审计。

## 7. 实际程序验证

scripts/research/r039_silent_steps.py实现：正规有限Delay图的精确执行分类；Bad/Good算子的有限最大不动点；Bad的最小不动点对照；有限post-fixed证书；带预算的循环关系证书；LTS的零步tau闭包、弱匹配和最大弱互模拟；有限图上的may/must事件判定。

31项unittest全部通过。包括全部1—3节点的144个确定性Delay图，将Good最大关系与逐输入精确终止/循环分类比较。该分类使用穷尽有限图与实际重复状态，不使用超时判为发散。测试另含假now证书、未知节点、非法后继、bool/Nat混同等负例。

有限模型结果不证明无穷Delay全集的可判定性；任意n或任意无限展开的论证在正文。没有原生工具可用，本轮不添加一份未经运行的“完成形式化”占位。31项不是31个HoTT定理。

## 8. 下一步与停止重复条件

本轮已完成R038约定的停顿等价检查。不要继续更换自环名字或放大图数量，也不自动回到R016不透明ua。

后续具有判别力的问题应是：在已经保返回结果的确定性部分性语义中，顺序组合与实际竞争/超时操作是否都能下降到同一等价商？若竞争操作依赖完成先后，其类型与正确性应明确指出额外观察，不能把默认商消去当作race实现。先核一项真正的操作及规约，不另建巨大工具平台。

RP-B01原生模型、R026规约与环境问题、自指/依赖路径各轮原证据继续保留。本轮与它们不竞争创建新总纲。

## 9. 认知与来源状态

继承revision38完整Git，原87项records与旧原文不改。当前计划433份、3,218,894字节，未完整进入本轮上下文；核心闭包与三问只取得了标明范围的局部读取。因此FULL_COGNITION=BLOCKED/NOT_CERTIFIED，不声称全文门禁通过，不虚构本轮发生压缩。当前是有界局部研究的保全；原全文加载政策没有削减。

来源正文通过web阅读。容器尝试下载三份一手源均发生DNS失败，错误完整记录；SOURCES.md提供实际读取范围的人工转述，不冒充下载原文件。没有继续用失败下载阻塞数学推导，也没有称源文件已经完整归档。
''')
 put(R+'SOURCES.md',r'''
# R039 来源与阅读范围

1. Xavier Leroy, *Semantics of divergence, second part*, Module Partiality.
   https://xavierleroy.org/cdf-mech-sem/CDF.Partiality.html
   实际web阅读全文的相关定义与证明：delay/omega与归纳terminates L8—59；equi、terminates_equi、diverges_equi L86—159；受限单边跳过与自然数索引L160—202。用于区分有限跳过与无限单边跳过，以及共同收敛的正向实现。非HoTT原生代码；本轮没有在Coq重编译。文档正文引用仅用自己的转述；不是原始字节下载存档。
2. HoTT Book固定commit 578b85cc8d586b1677ec4335148adeb443057d24, hits.tex §6.10。
   https://raw.githubusercontent.com/HoTT/book/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex
   本地文件HoTT/theory-schema/upstream/book-578b85cc/hits.tex。集合商递归需要尊重关系，不能为不保持返回值/必然完成的源操作免费提供下降。
3. Rob van Glabbeek, Bas Luttik, Nikola Trčka, *Branching Bisimilarity with Explicit Divergence*, arXiv:0812.3068；Fundamenta Informaticae 93(4), 2009。
   https://arxiv.org/abs/0812.3068
   阅读摘要/作者出版页面，用于明确“额外保持发散”是既有语义区分。本轮F/S的普通弱互模拟证明由正文直接给出，没有声称读过整篇PDF或实现其全部branching条件。arXiv HTML获取失败。
4. Thorsten Altenkirch, Nils Anders Danielsson, Nicolai Kraus, *Partiality, Revisited*, arXiv:1610.09254 / FoSSaCS 2017。
   https://arxiv.org/abs/1610.09254
   仅摘要：Delay、强/弱等价、可数选择与HoTT启发的QIIT部分性单子。没有以摘要认证本轮全部规则，没有宣称全篇或代码审计完成。arXiv HTML获取失败。

全部网络核对日期2026-09-11。容器原始下载独立失败，见artifacts/r039/sources/FETCH_RECEIPT.json；web读取成功与容器下载失败不是同一次操作。未编造源hash，实际本地固定Book源码哈希由RESEARCH_MANIFEST登记。
''')
 put(R+'PLAN.md',r'''
# R039 接续

本轮silent-step族已有正反结论，暂停追加同类自环与有限图穷举。下一候选：选择实际部分性结果等价与一个race/timeout操作，检查操作能否尊重该等价并沿商下降；顺序bind与竞争择先不能因为共享monad名称就归为同一合同。优先一个可检查的最小实例与作者源码，不先造新整个平台。

保留：R038当前态Acc迁移正例；R036虚假抽象路径；R033—34路径作用；R029—32反射与依赖范围；RP-B01原生工作、R026规约问题。

新结论维持PAPER_CHECKED / finite-tests-only / no-core-error / novelty-not-claimed。若没有新自然过程或规则连接，不因本轮数据更多便升级成目标悖论。完整认知加载仍未认证，不能用本计划替换433份全文。
''')
 claims=[
  dict(id='R039-C1',statement='F与S发散不敏感弱互模拟，MayDone同真，MustDone不同。',status='PAPER_PROVED_WITH_FINITE_CHECK'),
  dict(id='R039-C2',statement='按该等价的集合商不支持保原规格的mustFlag下降；done没有被删除。',status='PAPER_PROVED'),
  dict(id='R039-C3',statement='无限单边跳过的最大关系可关联spin与任何now值，但不传递；商闭包合并0/1结果。',status='PAPER_PROVED_WITH_FINITE_CHECK'),
  dict(id='R039-C4',statement='收敛保持型Delay等价和受限单边跳过提供正向保护。',status='PRIMARY_SOURCE_AND_LOCAL_ARGUMENT'),
 ]
 put(R+'CLAIMS.json',js(dict(round='R039',claims=claims,native='NOT_RUN',originality='KNOWN_CORE_NOT_CLAIMED',HoTT_internal_inconsistency=False,physical_bridge='MODEL_ONLY')))
 put(S+'SESSION.md',r'''
# R039 有界研究会话

用户请求：继续。继承revision38，最后研究为R038。当前研究停顿/弱等价，未改模型、未创建Work、未启动其他AI，无push与后台。

实际动作：读取当前入口和R038原证明；选定具体LTS及Delay关系；核对一手作者源码；源码先写scripts，再运行31项测试与结果生成；保留三份DNS失败。核心新增与反解释见reviews/SILENT-STEPS-001/。

源规则、自己推导与有限程序分别记录。没有原生HoTT证明；没有认领标准核心错误、已有软件漏洞或原创性。新工作经本地Git与原checkpoint提交后回读。

完整全文认知计划433份、3,218,894字节未完成，BLOCKED_FULL_COGNITION；没有假称压缩导致，也不取消原政策。旧记录保持原字节。本轮成果作为待复核有界局部延续。
''')
 put(S+'RESEARCH_DELTA.md',r'''
# 本轮差量

不是再证明每步来源不同；本轮有限弱匹配都从当前状态出发，但可零步，无限链可能永不产生匹配进度。不是再次删除Done；Done是双方显式共同动作，改变的是may/must与发散观察。

向HoTT的具体连接是商消去respect：弱等价不保持的MustDone不能免费下降；Bad生成的商不能保不同now返回标签。相反，实际一手Delay定义以归纳收敛与有限跳过预算避免假终止。

31项有限测试支持实现，无界结论见独立纸笔。旧87项记录不变，前沿切换不关闭旧问题。
''')
 put('artifacts/r039/RESEARCH_MANIFEST.json',js({p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in [
 R+'PROOF_NOTE.md',R+'CLAIMS.json',R+'SOURCES.md',R+'PLAN.md','scripts/research/r039_silent_steps.py','scripts/tests/test_r039_silent_steps.py','scripts/session/run_logged.py','artifacts/r039/TEST_EXECUTION.json','artifacts/r039/RESULTS.json','artifacts/r039/MODEL_EXECUTION.json','HoTT/theory-schema/upstream/book-578b85cc/hits.tex']}))
 print('R039 notes saved; no old mathematical records modified.')
if __name__=='__main__':main()
