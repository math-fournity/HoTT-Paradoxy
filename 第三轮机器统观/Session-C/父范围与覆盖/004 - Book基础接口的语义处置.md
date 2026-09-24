<!-- governance-shard:v2
logical_id: MO3-C-PARENT-COVERAGE
shard_id: 004
index: ../父范围与覆盖.md
-->

# Book基础接口的语义处置

> HUMAN_EDITED；2026-09-24；Session C。以固定Book第一章及formal基础规则检查理论便利、条件与消费者的联系。下列REVIEWED仅为实际原典语义审查；书中定理保持SOURCE_REPORTED_NOT_REPLAYED，未由C重新机器证明。C-BASE-01的生成与判别见过程002；全父范围仍未完成。

## 1. 实际来源与分母

preliminaries.tex已从1连续读至2044 EOF：1–357、358–727、728–1061、1062–1380、1381–1720、1721–2044。SHA256为`c459282fc0b789cd6f11a4a7bf401fcb1074c12c417b63fccdeee25927ed99d9`，138454bytes。formal.tex本Session初次全文已读1259行；本单元再次连续读1–974，分1–340、341–712、713–974，SHA256为`e621484e2e457e70536a92367cca452f34df8ecfc9a17a3bdf0e4ee67e5f0cec`。没有修改原典。

统一locator根是[固定Book源码](../../../HoTT/theory-schema/upstream/book-578b85cc/)；版本为578b85cc8d586b1677ec4335148adeb443057d24。Schema C01–11正文亦已回核；Schema的中文说明不替代这些一手段落。数学“可证明/不可证明”等在本片仅转述固定源的表述，不能引用为C新机器定理。

## 2. 十二编号节与未编号内容的实审

各行ID同时是公开来源判断ID `J-BASE-S-<ID>`。观察任务是AI用来检查规则作用的解释；除明示的C-BASE-01外，不把每行又算一个新悖论。REVIEWED不表示已完成所有后继问题。

|来源ID及精确范围|关键规则、收益与取舍|现实/假想解释与语义判别、联系及未答|覆盖／研究轴|
|---|---|---|---|
|B01.01，preliminaries4–174|以类型统合对象与证据；区分a:A、Id与判断相等；上下文按依赖排序；规则式核心与后续公理分开。|资格表让已声明对象供后续构造使用，省去重复描述；不等于物理生产完成。检视含自由变量的表达、交换有依赖的声明、把内部否定施于typing judgment等读法，均缺原规则许可。连接C01–03、A00/A02.CTX/STRUCT；元理论断言待A04精确系统。|REVIEWED／SOURCE_REPORTED|
|B01.02，175–357|函数以构造/应用/β/η给出，不以关系图定义；capture-avoiding替换及α改名保绑定，currying减少原始构造。|同一配方可用于多个输入；重复引用是否意味着资源重复由C-BASE-01专查。源例f(y)不能让自由y被λy捕获，说明替换不是裸文本替换。连接Π、Σ和共享环境；未测任何编译器实现。|REVIEWED／SOURCE_REPORTED|
|B01.03，358–436|累积宇宙与typical ambiguity节省层级书写；层级仍需一致，无同层所有类型，也无本版本内族λi.U_i。|一张类型目录可进入更大目录，不给同层任意自收录许可。以省略下标后回填的过程检查“看似自指”与实际资格；Notes另列Tarski/内部层级选择，resizing交D04。未声称新证Type-in-Type矛盾。|REVIEWED／SOURCE_REPORTED|
|B01.04，437–529|Π按输入改变输出类型，形成/λ/应用/β/η；多参数依赖顺序，宇宙多态身份函数与swap例有类型参数。|按申请对象给其匹配规格；统一函数是随输入取得结果的规则，不是全部申请已运行。将相关参数互换与独立参数swap区分；连接B01.06的构造性选择及C-W-01，未把所有族压成W执行。|REVIEWED／SOURCE_REPORTED|
|B01.05，530–727|积/单位：形成、引入、递归、依赖消去、β；Σ/单位的η在此为命题性质而非新增判断规则。|两份材料打包与根据包的整体规格处理是不同消费者；仅有非依赖recursor不自动给任意dependent eliminator。章中给出的uniqueness证明和正控制支持来源审查，尚不替跨编码的计算保真。|REVIEWED／SOURCE_REPORTED|
|B01.06，728–869|Σ的第二分量类型依赖第一分量；snd要依赖消去。ac拆分已有g:Πx.Σy.R(x,y)，没有从截断存在免费取值。|带证书的产品包与生产证书的过程分开；每次调g的不可变值语义与一次性生成器不是同一输入。结构magma/pointed magma须保carrier及操作数据。连接C-BASE-01、B01.11及D03；Book3 AC仍待实审。|REVIEWED／SOURCE_REPORTED|
|B01.07，870–958|A+B携分支及数据；左右消去分别给齐；0可形成但无构造子，空消去先需a:0。|分流交付保留来源一侧，合并输出不等于忘掉输入标签。空输入的处理规程不提供空输入本身。不能把0合法形成当作有闭项，亦不由无构造子证明整个系统一致。|REVIEWED／SOURCE_REPORTED|
|B01.08，959–1061|Bool两构造；可用1+1实现；用Bool上的Σ编码和、Π编码积；后者依赖funext且计算相等强度不同。Bool不等所有命题真值。|替换数据格式可以保两路读取，却未必保同一个dependent consumer的原有计算接口。新增接口C-BASE-02待审，不被本行REVIEWED关闭；Bool判定函数也不认证任意命题可判定。|REVIEWED／QUESTION（编码接口）；其余SOURCE_REPORTED|
|B01.09，1062–1204|Nat由0/suc及递归、归纳、β指定；高阶函数值让表达范围不止一阶原始递归。|有限指令长度是输入，递归结果不是所有长度实例已执行；源dbl/add/assoc展示实际递归假设如何消费。固定步数与资源上限不同。连接B01.10、ex:ackermann、Book5；没有超时或全称终止新判词。|REVIEWED／SOURCE_REPORTED|
|B01.10，1205–1265|pattern matching作为消去原则的缩写；递归调用受可翻回原则的限制，任意自调用不自动有资格。|一份看似循环的配方要先找到下降输入或其它原规则；源中增大参数递归是作者的拒绝说明，不是C运行出的不可停机见证。连接ASK、定义精化与后续general induction。|REVIEWED／SOURCE_REPORTED|
|B01.11，1266–1546|proof-relevant PAT；合取/析取/蕴含/否定/Π/Σ；logical iff与type equivalence不同，内¬0与元一致性不同。|证明可作可引用证据，实物消费资格仍需桥。Source明确inhabited是给特定元素而未命名，不是仅有描述；∀Σ前提已给选择。hProp/截断/LEM/AC由Book3单列，不能用本节替全逻辑。|REVIEWED／SOURCE_REPORTED|
|B01.12，1547–1849|Id formation/refl/transport后果、unbased J与based J；家族端点可变，不能对两个固定端点只留refl；J到based的此证明升一层宇宙，另有无宇宙练习；disequality与positive apartness区分。|路径解释保端点的可变范围；抽走一端再缩绳不是固定双端的同一操作。不是历史圆环全案模型。Book2的路径代数/传输、Book7 K/UIP和Book11 apartness仍要各自审；本行不重证J等价。|REVIEWED／SOURCE_REPORTED|
|U.B01.NOTES，1850–1936|MLTT变体、intensional/extensional、UIP/K、Πη/Ση、funext、模式匹配、Russell/Tarski、累积规则/子类型/显式提升、directed层级/Uω/内部层级等命名选择。|这些是固定版作者给出的比较，不是2026软件现状。判断相等和类型同一的选择改变消费者接口，不能统称一种HoTT。纳入§4的配置差异，未安装/复证所有比较系统。|REVIEWED／SOURCE_REPORTED|
|U.B01.EXERCISES，1937–2044 EOF|共16项，按§3保留所有题和联系；它们提供跨节义务，不因“练习”排除。|题目存在不是题目已被C证明；其中iterator和Bool积的计算强度进入C-BASE-02，语义审查已完成，后继核证未完成。末尾编辑器标注不含数学内容。|REVIEWED／QUESTION或SOURCE_REPORTED，非新proof|

## 3. 全部练习的归组理由与剩余

|原标签/起始行|共同作用与处置|与父问题的连接|
|---|---|---|
|composition1939；pr-to-rec1948；pr-to-ind1953|组合与投影/递归/归纳的接口；依赖η及计算方程分别审阅。|C-BASE-02保判断/命题差别；不是“同一载体就可换掉所有consumer”。|
|iterator1960；sum-via-bool1973；prod-via-bool1978|表示重组与计算强度；前者要求命题方程，和编码保所列判断方程，积编码题只要求命题方程且用funext。|已接受的高价值接口判别，待下一相关单元执行。|
|pm-to-ml1984；without-K2029；subtFromPathInd2034|J两呈现、端点范围与transport；不把禁止的K当J实例。|B01.12→B02.03/B07.02，待后两章扩大语义。|
|nat-semiring1989；fin1996；ackermann2001；add-nat-commutative2038|自然数、有限类型族与高阶递归；代数律作为命题，闭项计算与含变量方程不同。|B01.09/10、Book2/Nat与Book5；不为全面覆盖重做已有教科书算术证明。|
|neg-ldn2012；tautologies2016；not-not-lem2025|构造逻辑操作练习；¬¬LEM不等LEM。|Book3逻辑的输入边界；不靠有限Bool真值表代全类型结论。|

上述16题覆盖与机械标签清单核对，没有从分母删题。这里“归组”只共享语义说明，没有宣称不同题目等价；未要求逐题另造proof，但若后继关键结论依赖其中任一数学事实，须取得相称证明或保持来源等级。

## 4. 附录与Schema的双向映射

|附录条目|实审规则与明确差异|对应Book/Schema、结果与未答|
|---|---|---|
|A00，1–158|显式context、三类judgment、语法绑定、捕获规避；正式推导与书中非正式论证的层次。|B01.01/02→C01/02/03。REVIEWED／SOURCE_REPORTED；排版命令和索引命令按无理论含义归组。|
|A01及A01.U/PI/SIGMA/SUM/FIN/NAT/ID，159–409、433–453|无类型convertibility再限制到同类型判断；明确不含函数判断η；Π/Σ/+/0/1/Nat/based Id形成与消去、计算规则。|B01.02–12→C01/04–09/11。REVIEWED／SOURCE_REPORTED；A01.W仍沿C-W-01。A01不是正文的无差异抄写。|
|A02总说明、CTX/STRUCT，454–619|推导树及先决judgment；ctx-ext fresh，Vble，Subst1–3/Weak1–2是admissible；Δ及依赖类型同时替换；转换与合同性。|B01.01/02与C01–03，C-BASE-01。REVIEWED／SOURCE_REPORTED。610行A′无局部声明已由C03记录为排版观察，本次回源确认；不把它当获准的新自由规则，也不声称完成整个规则集元证明。|
|A02.U/PI，620–712|累积层级；Π以显式context直接形成，β与typed η，普通→作特例。|B01.03/04→C04/05。REVIEWED／SOURCE_REPORTED。层级统一不等同resizing；A01差异保持。|
|A02.SIGMA，713–765|构造器/带绑定的primitive eliminator/β；并非一定是以函数为参的函数；无判断η。|B01.05/06→C06。REVIEWED／SOURCE_REPORTED；投影编码与数据记录η不能静默跨配置。|
|A02.SUM/ZERO/UNIT，766–859|分支全给齐、0无intro/β、unit无判断η；目标C的绑定位置清楚。|B01.05/07/08→C07/08。REVIEWED／SOURCE_REPORTED；不产生现实空输入。|
|A02.NAT/ID，860–942|Nat依赖步进与替换方程；unbased J motive依赖x,y,p并同时代入refl。|B01.09/10/12→C09/11。REVIEWED／SOURCE_REPORTED；固定两端的K不由此表宣称。|
|A02.DEF，943–974|定义名携类型参数，省略参需elaboration，先精化后检查，不是内核规则自身自动推导一切。|B01.02/10→C17的定义/精化分支。REVIEWED／SOURCE_REPORTED；C17的检查/搜索/公理常量仍连A04/A03未审部分。|

Schema一级：C01–C09、C11的本页基础规则范围可标REVIEWED；C10一般归纳仍未审（仅W已审）；C12–16仍未审；C17只定义/精化分支已审而一级保UNREVIEWED；C18仍未审。C04的resizing对照、C07的截断析取对照、C11的全域K/UIP元结论分别由D04/Book3/7继续承担，不能在一条基础规则完成后销账。D/S/E未由本页升级。

## 5. 由规则与消费者生成的中层关系

本轮不是十二个叶子的结果相加。以下各单元已取得自己的来源解释；更宽数学/现实结果如表保留，不把关系标签当论证。

|单元与成员（可重叠）|本层独立问题、实际判别|处置与父影响|
|---|---|---|
|N-BASE-CONTEXT：B01.01/02/04/06、A02.CTX/STRUCT/PI/SIGMA|共享前提被两处使用时，依赖替换仍保什么？Subst同时作用于Δ和输出，重复引用旧值并无现实核销更新。C-BASE-01对照消费及只读任务。|SOURCE审查；与旧A N-CONTEXT/D1-S4同边界，SOURCE_ONLY复用，不添同义proof。|
|N-BASE-ENCODING：B01.05/08/09/12、上述六接口练习、A01/A02|换表示或减少原始构造是否保原consumer的判断计算？原典自己区分判断β/η与命题方程，不能由功能对应一并继承。|QUESTION C-BASE-02已接受待判别；与B05.05的w_d/w_s/w_h相接。整个中层研究义务未结案。|
|N-BASE-EVIDENCE：B01.06/07/11、A00、0/Σ/Π|构造、内部证据、存在及现实完成何时互相转换？source ac前提已有g；PAT witness只担其类型；空类型可形成不认证闭项/一致性。|SOURCE审查；与Book3的mere逻辑/AC和语义S01横向相接，未替它们结案。|
|N-BASE-PATH-FAMILY：B01.12三个小节、A01.ID/A02.ID、Book1 Notes|归纳省去的是哪些generic情形，而非固定纤维中的所有差异？原文端点可变与固定两端明确分开，J到based的宇宙层和无宇宙路线另记。|SOURCE审查；高阶结构由Book2/7继承待审，不因本节合法直接宣称所有路径都是refl。|
|N-BASE-SIZE：B01.03/04/11、Notes、A02.U/DEF|典型歧义与隐式参数节省书写，谁承担层级与参数复原？源明确须一致赋层，elaboration先于check；不能把较大宇宙等同同层全收录。|SOURCE审查；D04 resizing、S07内部模型仍未审，本页不提供万能精化器。|

联合/有序：N-BASE-CONTEXT必须同时给资源解释、消费者和更新环境，不能拆成dup与单次使用两个各自“成功”例；依赖顺序与消费顺序分开。反馈：把上次结果作为下次输入时，来源只允许按实际依赖替换，不替外部环境更新提供真实性；此处没有声称建立动态系统证明。共享背景：A01/A02 η、宇宙与绑定差异决定关系是否可复用。

粒度控制是本次人工语义检查：删去N-BASE-ENCODING，只保Bool/Π/积三个叶子，会丢掉§1.8及exercise的计算强度差别；恢复中层后差别有原文定位。正常控制是Σ-Bool余积编码，原题要求保判断计算；不能把积的限制按“全编码都会丢判断计算”外推。独立组织按使用者的四项责任（获得输入、完成作用、比较输出、交付证据）重新扫本章，补出Notes的层级变化、练习的iterator及based J跨宇宙等入口。此为第一章范围控制，不是Goal7 R4全父范围充分性证明。

## 6. 尚未完成与复审触发

C-BASE-02须实际核指定表示、计算规则和至少一个依赖消费者，正反控制保同任务；不允许把目前SOURCE段落当已完成原生核证。Book2全章仍未读，Book5.4/5.5已读但未审，附录A03/A04及Notes更宽语义未审；全部D/S/E与其它章节不因本片升级。本文为SOURCE层语义首遍，不是无命中退出凭证。

本片结论审计共用规则：D01–04保父范围与每行解释身份；D05–08固定源、AI类比及作者规则分别归属；D09–12数量只用于查缺、SOURCE不冒机器证明；D13–16原文对照定位差别，不作物理因果归因；D17–20未审及后继义务显式保留；D21–24不把形成/解释/读取当能力完成，必要时回源修订。每行适用性还由“未答”字段限制。原源字节改变、发现新消费者/命名分支、精确形式化推翻读法、D提出来源反例时重开相关行；单次read/hash不证明未来消费正确。
