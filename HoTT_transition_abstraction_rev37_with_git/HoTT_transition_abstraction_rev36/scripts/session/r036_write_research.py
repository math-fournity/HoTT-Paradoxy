#!/usr/bin/env python3
"""Persist this round's complete derivation, claims and actual evidence scope."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
R='.codex/research/hott/reviews/TRANSITION-ABSTRACTION-001/'
S='.codex/research/hott/sessions/S-RES-20260911-036-TRANSITION-ABSTRACTION/'
def put(path,text):
 p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists():raise FileExistsError(p)
 p.write_text(text,encoding='utf-8')
def js(o):return json.dumps(o,ensure_ascii=False,indent=2)+'\n'
PROOF=r'''# R036：状态商产生虚假无限执行——有限过程、相容见证与完成性

状态：PAPER_DERIVATION + EXACT_FINITE_MODEL_CHECK；原生HoTT内核未运行，原创性不声称。来源、治理对齐与新数学构造分别保存。
本轮任务：用户明确解除R035暂停，先将已有计算能力／共享界限／特定新增失真同步治理，再继续寻找。不是新的Gemini来信。

## 0. 本轮差量与问题身份

以前已分别检查Done被删除后的无限流接口、经典数学分类与有效算法的分离、反射覆盖和依赖迁移。本轮不重复它们。

我们保留一个可以在有限步完成的**同一具体过程**、同一个初态、同一个Done判定。然后采用常见的“只保留状态类别；两个类别之间有边，当且仅当某两个代表之间有具体边”的理论化。

结果：每条抽象边都确实有具体来源，但由这些边自由拼接的抽象运行，可能没有任何相容的具体运行。本例连两条边的前缀就无法提升，不需要讨论无限选择、连续时空或算法不可判定。

因此，明确区分两种使用：
(1) 把抽象图当作保守的可能行为过近似：正确；发现抽象无限路径只意味着需检查或细化。
(2) 把它当作原过程的精确执行谱，并从抽象无限路径宣布原过程不能完成：错误；本例直接反驳这种提升。

本轮找到了(2)的具体反例机制，没有证明标准HoTT或某个库强制采用(2)。这个共享的抽象验证问题不是HoTT独有的新悖论。它仍然是用户方向A中可以明确检验的“指定理论化额外增加完成障碍”。

## 1. 指定理论与执行语义

使用自然数、有限归纳类型、Π、Σ、身份类型；为表达命题性的关系像可使用命题截断。没有LEM、停机神谕、单价性、一般选择或不透明数据公理。模型可在HoTT中表达，但Python不是HoTT内核。

具体状态为三个不同构造子：
  S = {a,b,d}。
初态a。Done(s) iff s=d。唯一的非终态执行边是：
  R(a,b), R(b,d)。
没有其它边，特别是R(d,d)不成立。Done之后不再计执行步；若另外用吸收态表示终止，必须把终止后自环从“未完成执行”中排除，不能误报它为不终止。

这是例如一个私有计数器从2减到0的过程：a为剩2步，b为剩1步，d为已结束。公开状态只报告“工作中／已完成”。这些是模型语义，不声称物理硬件没有资源成本。

令r(a)=2,r(b)=1,r(d)=0。每条具体边严格降低r，所有可达非Done状态都有后继，故每次从a开始的最大执行恰为a,b,d，并在两步结束。

任务是：从指定初态开始，**所有最大执行是否到达Done**。这不是“是否存在一种可以完成的执行”，也不要求预知外部环境。

## 2. 状态抽象与HoTT中合法的关系像

Q={w,D}，alpha(a)=alpha(b)=w，alpha(d)=D。
此映射的核关系只将a,b识别，可把Q视为这个有限关系的集合商的具体呈现。也可以直接定义Q为二元素归纳类型，无需先建立完整HIT工程。

观察保持是精确的：Done(s) iff DoneQ(alpha(s))。本轮没有擦除Done。

定义命题值的抽象转移：
  E(u,v) := || Σ x:S Σ y:S.
                  (alpha(x)=u) × R(x,y) × (alpha(y)=v) ||。

从R(a,b)得到e_ww:E(w,w)；从R(b,d)得到e_wD:E(w,D)。有限分类得知除此之外没有边。

E(w,w)是**执行关系的自环**，不是把HoTT身份类型refl当成一次物理操作。每次使用这条抽象边，只断言存在某个具体来源；它没有声明当前实际代表就是那个来源。

每条具体边确实映为一条抽象边，故每条具体有限轨迹都有抽象像。这是正向模拟；不蕴含反向执行提升。

## 3. 合法抽象无限路径，以及长度2的具体不可提升证据

定义beta:Nat→Q，beta(n)=w。定义每一步的证据为e_ww。于是：
  Πn. E(beta(n),beta(n+1))。
这是一个有限定义的无穷路径对象，不需要先完成无穷次执行或进行无穷选择。它永不到达DoneQ。

所以抽象图不满足“所有最大执行最终完成”。在明确的抽象执行器上，一直选自环可产生实际无限抽象执行；相同判断不能直接转用于具体执行器。

更强：抽象前缀w,w,w已经没有从a开始的具体提升。

假设提升为s0,s1,s2，s0=a，每对邻居满足R，并alpha(si)=w。
R(a,s1)迫使s1=b；R(b,s2)迫使s2=d；但alpha(d)=D≠w。矛盾。

用相容代表集合可有限复核：
  W0={a}；
  Wi+1={t | 存在s∈Wi，R(s,t)，且alpha(t)=beta(i+1)}。
本例W1={b}，W2=∅。

反之，原来的a,b,d映成w,w,D，始终有相容提升。有限程序正常结束和抽象模型有无限路径，可以在同一HoTT片段里分别成立，不矛盾。

## 4. 问题不只是忘了一个字段，而是存在见证的拼接不成立

每条抽象边都可能提供：
  R(x0,y0), R(x1,y1)，
并知道alpha(y0)=alpha(x1)。
但具体两步执行要求y0=x1（或一份明确的允许接续证据），不是只有它们的类别相同。

本例每次e_ww都来源a→b。第一次完成后代表是b；第二次却重新选择了a作为起点。这个隐含重选就是未被原过程授权的“回到较早进度”。

这不是线性逻辑禁止复制证明。抽象的关系命题当然可以重复使用。错误是在解释时把“某个代表可以走这一条边”当成“当前这个代表可以再次走这一条边”。

可以用两个步骤关系精确表达：
  ConcreteTwo(u,w) := ||Σx,y,z.
       alpha(x)=u × R(x,y) × R(y,z) × alpha(z)=w||；
  AbstractTwo(u,w) := ||Σv:Q. E(u,v) × E(v,w)||。
总有ConcreteTwo→AbstractTwo；在u=w=工作中时，右侧有证据，左侧为空。因此一般没有反向构造。

用关系复合记号，先将R沿alpha作存在像后复合，相当于在两条R之间允许插入核关系K(y,x')≡alpha(y)=alpha(x')；它不再要求中间代表相同。

所以真正不交换的是：
  先保留完整相容轨迹、再取其像
与
  先逐边取存在像、再自由形成轨迹。

甚至保留全部每条边的具体见证表，也不能仅凭独立选择恢复相容执行；本例边表完全已知而缺口仍存在。需要保存前一条边的终点与后一条边起点之间的依赖。

## 5. 一个精确的有限判据：商图无环与可下降的等级

设S,Q为有明确有限枚举的集合，alpha:S→Q满射，R为可判定有限关系，E为上面的存在像。这里谈**全部节点上的执行关系**，不是只谈某一初态的可达部分。

以下条件等价（有限算法和结构证明，不依赖一般排中律）：
(A) 抽象图(Q,E)无非空有向环；
(B) 存在rbar:Q→Nat，使每条E(u,v)都有rbar(v)<rbar(u)；
(C) 存在r:S→Nat，在每条R边上严格下降，并且在alpha纤维上恒定。

A→B：在有限DAG上，取从每个节点出发的最长路径边数。无环路径不能重复顶点，因此长度≤|Q|-1；有限枚举/拓扑递归给出rbar。
B→A：若有环，将严格不等式沿环连接，得到n<n。
B→C：取r=rbar∘alpha，直接下降且纤维恒定。
C→B：有限枚举为每个类别取代表；纤维恒定保证结果与代表无关。也可将值唯一刻画，使用命题截断消去到命题型的唯一值图。每条E边的严格不等式是命题，故可从其实际见证证明并合法消去。

注意：无环只保证没有无限转移；要使所有最大执行到达指定Done，还要排除可达非Done死锁。具体源若所有非Done都有后继、且Done谓词在纤维内一致，则商上的非Done类也有后继。不能只用无环替代这个条件。

针对某一初态，可限制到抽象可达子图并明确相应的原像范围。不可将全图结论与指定初态结论混同。代码有一个“不可达处存在环，但初态执行完成”的正例。

本例r(a)=2,r(b)=1，而alpha(a)=alpha(b)，所以原等级不能下降到Q。更强，不存在任何严格下降且纤维恒定的r，因为R(a,b)要求r(b)<r(a)，纤维恒定却要求相等。

## 6. 整个有限链上的一般化及最小性

考虑有限链s0→s1→...→sN，唯一Done为sN。
若alpha合并了两个不同非Done状态si,sj（i<j），那么中间这段非空具体链的像从alpha(si)回到同一类别，形成非空抽象闭路。反复该闭路给出不结束的抽象执行。全部这些类别从初态都可达。

因此，在这个指定链族中，任何非平凡且Done保真的状态合并，都会引入虚假的非终止执行；保留每一阶段则没有。对一般分支系统不能这样推广：两个同层分支状态可以安全合并，代码给出了实例。

最小三状态例满足：源确定、所有具体状态可达、Done被精确保留。两状态的同类有限终止系统只有一个非Done和一个Done，保真合并不能把它们合起来，故没有这种状态合并反例。这个最小性依赖已声明条件，不是针对所有可能过程表达的绝对最小性。

## 7. 同理论内的修复与最强反解释

### 7.1 不删除进度／等级
使用alpha'(s)=(alpha(s),r(s))或直接保留三个状态，E'严格降低r，最大执行仍完成。等级不必是墙钟时间，也不要求知道真实物理耗时。它只是原程序实际用于前进且不可无声重置的阶段信息。

### 7.2 按当前代表集合推进
保留Wi并按实际关系更新，收到w,w后当前代表只能是b；再要求w就得到空集合，而不会重新允许a。这一有限路径提升检查检测虚假反例。

### 7.3 明确反向提升条件
如果额外给出：
  Πs,v. E(alpha(s),v) → Σt. R(s,t) × alpha(t)=v，
则可以沿任一有限抽象路径从当前代表逐步提升。本例该条件在(b,w)和(a,D)失败。前者解释无限自环，后者说明抽象图还允许过早结束的虚假一步。
若讨论无限提升，不能省略给定见证函数或相应选择条件；本轮仅用显式有限构造，不依靠无限提升定理。

### 7.4 “这只是合理保守抽象”
正确。这是必须保留的最强反解释：may抽象有意允许额外行为，抽象中发现反例应先验证其可行性。声称它已经证明原程序发散，是无依据提升。本轮没有发现HoTT核心要求这种错误解释。

### 7.5 “增加公平性就能结束”
若声明持续使能的退出边最终必须被选择，可能排除本例无限自环。但这是一项新调度条件，不由裸E自动得到；即便如此，任意长但有限的工作中前缀仍可能不提升，原两步上界也未恢复。不能靠改变合同假装原有保真已经成立。

## 8. 与最新认识、历史轮次及公开文献的关系

R035要求区别共有计算界限与额外失真。本例源、商、反例检测均有限且可判定，没有一般停机不可判定；原HoTT完全可以证明两种模型的差别。因此不将计算不完备性当成病因。

与R014相比，Done仍然可见；消费者不是只获无限流的神秘黑箱。与R033—34相比，不要求擦除路径后恢复它的原作用，也不诉诸全宇宙的相干选择不可能。新机制是把逐条可实现的边错误地拼成整体可实现的轨迹。

抽象模型中的spurious counterexample/spurious path是已有研究方向。本轮是项目内新的清楚实例及判据应用，不声称原创。Ball 2004说明过近似允许比源更多行为，反例需要再验证；Fan/Holte的Spurious Path Problem直接讨论抽象新增路径。这些外部来源用于机制身份与研究比较，不替代本文具体证明，也不冒充已部署HoTT系统的错误证据。

按三层成果交付：
- 理论选择：合法的有限分类与命题性关系像；
- 局部边界：存在像与轨迹组合一般不可交换；
- 目标对应：明确的两步过程经这种理论化出现无法完成路径，但只有把may模型错误当作精确模型，才会对原过程得出错误结论。真实物理案例／某HoTT实现强制采用错误解释仍OPEN。

## 9. 实际验证与未完成项

28项单元测试实际通过；完整关系表、严格下降等级、环证书、提升集合与负输入全部保留。额外枚举状态数2—6的线性链、所有Done保真状态分区，共75个分区；每个长度中只有保留所有阶段的分区仍普遍结束。一般链族结论由§6直接证明，不从75个样本外推。

无穷抽象执行由beta(n)=w及e_ww的有限定义证明。非提升由两步的有限矛盾证明。没有把任何超时当作发散；代码没有运行至超时的“演示循环”。

原生Lean/Agda/Rocq未运行，本轮不增加一份未编译草稿来冒充进度。完整HoTT内部化与独立审查开放；对证明规则、数据类型的表示已明确，不伪称Python是内核。

## 10. 下一项自主动作与停止重复条件

此族已有最小正反例、等级判据及具体证据，下一轮不再更换状态标签或增加分区样本。更值得检查：一个实际的时间/历史抽象或反射规约，是否逐边保存“可发生”却在组合时需要同一状态的相容见证；给出有限路径提升函数或实际失败点。

若只得到合理may过近似和正确拒绝，就将此族作为表示边界保留，转向另一项任务；不把找不到错误解释说成所有系统安全，也不把合理保守性改名为理论失败。RP-B01原生对应、R026规约和全部旧正反结果继续保留，研究无需等待外部AI。
'''
SOURCES='''# R036 来源与使用范围

## 当前任务与继承资料
R035/REQUEST.md、ASSESSMENT.md：用户暂停及“逻辑＋几何＋程序／共享界限”的怀疑与助手评估，逐字保留并纳入第五闭包§22。
R036/REQUEST.md：当前恢复与治理对齐授权。
R014/PROOF_NOTE.md：已全文回查，不把本轮重新写成Done擦除或黑箱无限流。
R034/PROOF_NOTE.md：已回查，统一MereMove障碍保持原状态，不在本轮重证。
三问、第五闭包、AGENTS、业务Skill及时间owner：当前owner对齐，不变更既有加载引擎或原用户文稿。

## 一手规则
锁定HoTT Book commit 578b85cc8d586b1677ec4335148adeb443057d24：
- HoTT/theory-schema/upstream/book-578b85cc/logic.tex：命题截断、消去至命题与唯一选择；本轮用来说明关系像和等级下降的合法消去。
- HoTT/theory-schema/upstream/book-578b85cc/hits.tex §6.10：集合商；本轮可用显式二元素归纳类型呈现该有限商，不要求完整商实现。
- 公开读取hits.tex成功；同commit的logic.tex一次web cache miss，规则回到已提供本地固定源码，不将失败的web请求当成功。

## 机制比较（不是本文证明的替代）
1. Thomas Ball. Formalizing Counterexample-driven Refinement with Weakest Preconditions. MSR-TR-2004-134, December 2004.
https://www.microsoft.com/en-us/research/publication/formalizing-counterexample-driven-refinement-with-weakest-preconditions/
仅使用其对过近似和虚假反例问题的说明；网页摘要一处refinement句子疑有笔误，不据此推导。
2. GaHee Fan and Robert C. Holte. The Spurious Path Problem in Abstraction. SOCS proceedings article.
https://ojs.aaai.org/index.php/SOCS/article/view/18356
检索到摘要说明spurious paths可以并不伴随spurious states；年份未作为本轮结论前提，不混用网页迁移日期与论文历史年份。

本轮没有读取PDF、没有OCR，没有原生证明助手运行，没有外部专家或其它AI调用。所有新代码保存到scripts后才调用。
'''
PLAN='''# R036 接续计划

本轮完成：更新十项当前owner；实际检查一个三状态完成性失真模型，并形成关系像/组合、有限等级判据与最强正解释。

下一项有判别力的问题：在一个明确的解释或抽象程序中，是否能够给抽象有限轨迹提供“保持当前代表”的提升，而不是每条边重新选存在见证？优先尝试一个实际可运行的带状态规约；只在其自称精确或要从抽象反例转回源时要求提升，不能把它强加给合理过近似。

不再做：扩大此例状态数、重写trap或单价Bool求值器、重复证明通用停机不可判定。若只能看到诚实的may摘要，就保留边界并换题。RP-B01原生形式化未完成，不因本轮旁支而关闭；同理R026语义忠实性和R034相干选择保持原身份。

当前不要启动外部AI或新通信。全量认知加载未通过，记录有界接续范围；不以新的摘要替代要求中的原文，也不篡改政策来宣称已经通过。
'''
def main():
 put(R+'PROOF_NOTE.md',PROOF)
 put(R+'SOURCES.md',SOURCES)
 put(R+'PLAN.md',PLAN)
 claims=[
 ('T1','具体三状态过程两步完成','FINITE_EXACT_PLUS_PAPER','S={a,b,d}; only a→b→d'),
 ('T2','Done保真的关系像存在无限自环轨迹','PAPER_CONSTRUCTION_AND_LOOP_CERTIFICATE','E=existential relation image; beta constant w'),
 ('T3','抽象两步w,w,w无实际初态提升','FINITE_EXACT_PLUS_PAPER','same source initial a'),
 ('T4','有限商图无环等价于存在纤维恒定的严格下降自然数等级','PAPER_DERIVATION_NOT_NATIVE_CHECKED','finite explicit sets; surjective alpha; all graph, not just initial'),
 ('T5','有限线性链任意非平凡Done保真合并引入虚假非终止','PAPER_DERIVATION_WITH_BOUNDED_PARTITION_TESTS','linear chain; nonterminal states merged'),
 ('B1','该机制不是共有停机不可判定造成','DIRECT_SCOPE_JUDGMENT','finite decidable example'),
 ('B2','不是HoTT内核矛盾或已证实际软件漏洞','NOT_CLAIMED','honest may abstraction admits spurious counterexamples')]
 put(R+'CLAIMS.json',js({'schema':'r036-local-claims/v1','claims':[{'id':i,'statement':t,'status':s,'scope':q} for i,t,s,q in claims],
   'native_validation':'NOT_RUN','originality':'NOT_CLAIMED','physical_correspondence':'FINITE_PROGRAM_MODEL_ONLY','full_cognition':'NOT_CERTIFIED'}))
 put(S+'RESEARCH_DELTA.md','本轮完整研究为[PROOF_NOTE](../../reviews/TRANSITION-ABSTRACTION-001/PROOF_NOTE.md)。不从共有计算界限推断理论失真；新构造在有限域内分离完整轨迹像与逐边存在像的自由组合。28项测试通过；一般判据为纸笔，非原生内核证明。\n')
 paths=[R+'PROOF_NOTE.md',R+'SOURCES.md',R+'PLAN.md',R+'CLAIMS.json','scripts/research/r036_transition_abstraction.py','scripts/tests/test_r036_transition_abstraction.py','artifacts/r036/RESULTS.json','artifacts/r036/TEST_EXECUTION.json']
 put('artifacts/r036/RESEARCH_MANIFEST.json',js({'files':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'test_count':28,'finite_partition_count':75,'finite_tests_not_general_proof':True}))
 print(js({'written':paths,'status':'PAPER_AND_FINITE_EVIDENCE_SAVED'}))
if __name__=='__main__':main()
