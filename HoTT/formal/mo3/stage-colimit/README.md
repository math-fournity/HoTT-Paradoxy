# C01：有限阶段关系与原生直接合成中的递归资格

本包针对`Stage n=Fin(suc n)`、`StageStep n y x=(suc(fst y)≡fst x)`及嵌入`fsuc`。研究问题是：各阶段的递归资格、保边嵌入与合成对象的递归资格是否相同。当前源码已由原生Cubical Agda接受；交付状态以唯一matrix、run和两项证据校验为准，不由本README自证。

proof ID `MP-MO3-STAGE-COLIMIT-001`；claims C-327–C-330。系统为Agda2.8.0-3d04bac/Cubical0.9，`--safe --cubical --guardedness`，所有本包对象位于Type₀；标准Path/HIT/PT和Agda builtin边界保留，没有本包新postulate。

|claim|完整形式范围|关键定义|
|---|---|---|
|C-327|∀n:ℕ，∀x:Stage n，Acc(StageStep n,x)|stageWellFounded；先对NatStep按自然数构造Acc，再沿fst回拉。|
|C-328|∀n y x，StageStep n y x → StageStep(suc n)(fsuc y)(fsuc x)|stepPreserved；不是保Acc结论。|
|C-329|Total=SeqColim Stages，TotalStep由某同一阶段的真实边及两个incl端点路径的mere image定义。∀k:ℕ，Acc TotalStep(terminal k)→⊥；因此WellFounded TotalStep→⊥。|terminalStep、terminalNotAccessible、totalNotWellFounded。|
|C-330|∀bound:ℕ，使用恒定Stage bound与identity嵌入的原生SeqColim；FrozenStep同样由阶段边的mere image定义，则WellFounded FrozenStep。|Frozen.rank/rankStep/frozenWellFounded。|

主run：[20260923-MO3-STAGE-COLIMIT-001-04](../../../verification/runs/20260923-MO3-STAGE-COLIMIT-001-04/RUN.json)。首次01在缺少Sigma乘积记号导入处拒绝；02为前三项中间版本；03为含冻结正控制版本；04在同源码上补齐builtin-source输入清单后重新捕获。01/02精确旧源码在Session-A证据/W2/attempt-001、attempt-002保留；03/04源码字节相同。

错误输入控制`WrongPreservation.agda`把有限阶段的Acc直接赋给全局Acc类型；CONTROL-01实际exit42，诊断`UnequalTerms`。拒绝只证明该次错误赋值不被接受，不是一般不可表达性定理。C-330使用相同HIT合成和关系构造方法，保留“阶段不再变化”的正常情形。

外部toolchain沿`../../dedekind-omega-missile/TOOLCHAIN.json`与AGDA_LIBRARIES。`DEPENDENCY-AUDIT.json`用已有canonical reader取得03实际打印的131模块路径/哈希，声明扫描未命中这些文件中的postulate/primitive；**这不意味着没有builtin原语**。`BUILTIN-SOURCES.json`另外固定安装的36个builtin源文件（22个含显式声明）作为保守超集，不称它们全部被本命题使用。04前后哈希另核。二者均为来源/依赖边界，不是内核正确性的元证明。

解释边界：这里没有假设HoTT宣称任意直接合成都保Acc；也没有把全局无Acc等同某次程序永不结束或物理不可完成。冻结版本与不断增加依赖可能是不同任务，研究正文须核其X_i/Done。剩余步坐标与W1自然说明的完整任务桥仍须审查；不主张原创性、所有colimit的定理、原圆环回答、HoTT内部矛盾或全理论完备。C01是否具有现实相对发现价值由本轮研究另判。
