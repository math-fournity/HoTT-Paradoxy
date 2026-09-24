# C01真实来源的责任式重建稿

> HUMAN_AUTHORED_STAGE_OUTPUT；从INPUT-MANIFEST的S1–S4及reading-blocks指定顺序实际读出后写成，先保存本稿，再打开本单元冻结的旧关系表作对照。A此前见过C01和旧图，故不是盲测、fresh独立发现或方法因果效果试验。此稿是不可冒充当前覆盖总图的阶段证据；最终采纳关系回覆盖owner。

研究对象是固定Book段落与原生Cubical C01如何分担形成、关系表达和递归资格。重建方法以“哪个消费者需要哪份条件”为线索，不以文件相邻或S1–S5固定深度分组。已证事实只沿C327–330引用，其余为源码报告/问题。

## 1. 先识别责任，而非五层标签

|单元|成员/精确来源|分组理由、独立问题和边界|
|---|---|---|
|U-QUAL|S2:7–16的WFRec/Acc/WellFounded，S2:26–45的access/WFI；S1原行887–968为书式参照|同一关系上的资格供给与递归使用。形成了A或R并不在这些接口中直接给wf参数；本层问“供给谁的Acc，给哪个consumer”。书式与原生配置不能自动同一。|
|U-STAGES|S4:19–27的Stage/NatStep/StageStep；S4:29–50的有限资格和Stages.map/stepPreserved|一个带关系及有向嵌入的参数族。问成员间到底保留什么：源码声明保边，而不是终点/Acc的无条件转移。n为任意自然数，非有限测试前缀。|
|U-CARRIER|S3:19–22的SeqColim/incl/push，S4:52–53的Total|把阶段呈现及嵌入统一成HIT载体。独立问“形成了什么路径识别、是否另带递归资格”；载体构造子本身没有StageStep或Acc参数。不能把它当关系/资格结果的总括。|
|U-EDGE|S4:55–59的TotalStep及S4:66–68的terminalStep|全局边由同一阶段n、两个端点a/b、StageStep证据及两条incl路径联合给出，再作PT。这是独立于载体形成的关系解释中层；仅知道各参与者分别出现还没有同一联合见证。边方向为从b到a。|
|U-GROW-QUAL|U-QUAL、U-STAGES、U-CARRIER、U-EDGE；S4:63–77显式terminal链和非Acc证明|真正的跨构造资格问题。即使每阶段正常且嵌入保边，本层仍问TotalStep是否有Acc；C327–329给出本族结果。本单元可有上述多层子问题，也与正常对照共享U-QUAL/载体/关系像角色。|
|U-FROZEN-RANK|S4:81–92的Constant/FrozenTotal/rank，S4:94–110的FrozenStep/rankStep/frozenAccessible|同样有合成与关系像，但选恒定阶段、identity map；rank对push的定义与该输入相容，rankStep连接边与NatStep。问“哪份共同证据真正贯通到全局资格”；C330给本恒定族正常结果，不是任意rank-transfer定理。|
|U-CONFIG|S1开头A为set、关系入Prop；S2的A:Type ℓ、关系:Type ℓ′；S3/S4原生HIT构造|共享配置责任。原生Acc定义比本书段落的输入叙述更一般；C01明确在Cubical实现上核证。若把Total结果提升为该书式集合关系实例，仍须提供所需carrier层级/关系及翻译，不能只凭同名Acc。这里不判该翻译不可能。|
|U-TASK|S4:5–6说明非操作/物理完成承诺；Acc、Full family与Frozen的不同输入|形式资格到任务完成的解释责任。源码没有物理时钟，也没有“读取完成值后再扩图”的运行过程；它可作版本依赖理想活动的模型，但不能用冻结Done与无界Done偷造同任务矛盾。|

这些是当前固定材料中人工找到的八个责任单元，不是穷尽语义单元，也不是八个独立新数学结果。U-GROW-QUAL含中层U-EDGE；U-FROZEN-RANK内部有rank下降连接；U-QUAL被增长/恒定两路线共同使用。它们形成重叠的有向组织，不是文件树或严格FCA格。

## 2. 关系必须保住的联合/次序/背景

1. **Q-CALL**：`wf : WellFounded R`、同一个R上的递归步骤和输入x一起供给WFI。把别的R′的wf搬来，原接口并未授权。
2. **STAGE-MAP**：Stage n、StageStep n、fsuc、StageStep(suc n)与stepPreserved共同说明一个有向映射。反转关系/映射不是改个箭头就保结论。
3. **HIT-IDENTIFICATION**：同一个Stages决定incl与push；push连接该阶段点与其map像。它是HIT路径识别，不是运行日志中的“后来发生”。
4. **JOINT-EDGE**：`n,a,b,edge,pa,pb`在同一个Sigma/同一Stages中联合。a/b/edge来源、incl目标和关系方向必须一起记录，不能只画无条件pairwise边。
5. **QUALIFICATION-CHAIN**：terminalStep为同一个TotalStep逐k给边，再由Acc消去得到C329。finite-stage资格不能直接填进这个consumer的参数位；错误赋值控制另有真实拒绝。
6. **RANK-PAYMENT**：Constant.map选identity、rank的push分支、FrozenStep定义和rankStep共同供给frozenAccessible。删除这个中层而仅保“stage有Acc、用了HIT”会遗漏正常结果依赖的证据。
7. **CONFIG-BOUNDARY**：Book set/Prop叙述、原生Type级Acc及具体HIT必须标配置。将书式条件自动套给全部原生目标，或反向把原生实例视为书式全文验证，都是未提供的连接。
8. **TASK-BOUNDARY**：关系资格、给定proof checking和实际依赖任务完成分开；每个比较保留输入族/观察/Done。

这八条是关系实例，不是完备关系分类。未知的自然consumer或更强解释仍OPEN，不能从本源码没有它推HoTT不能有它。

## 3. 暂时删去中层会怎样

删U-EDGE：仍可列出Stage、Acc、SeqColim，甚至C327/328都在，但无法知道C329是哪份关系、边如何来自原阶段，原任务保真问题被隐藏。

删U-FROZEN-RANK里的rankStep连接：仍看见有限Stage和FrozenTotal两个对象，却不能仅由它们的存在给出C330的资格；正常控制的决定性背景被抹去。

删U-CONFIG：Book与库的同名概念容易混成单一规则表，失去“本结论究竟在哪个配置成立”的问题。

以上是对当前源码依赖与覆盖表达的反事实审查，不声称删掉文档会使已存在的数学定理变假。接下来对照旧表，检查哪些是保留、细化或真正未定位的信息；不为证明方法有效而强造差异。
