# Bool函数编码积的条件计算接口

本包研究固定Book §1.8/§2.9/§5.5所提示的一个窄问题：以Bool→Nat表示两个自然数后，指定依赖消去器的命题β证据和直接判断化简是否相同。`MP-MO3-COVERAGE-ENCODED-PAIR-001`、C-342–343只陈述以下精确片段，不担保整个HoTT、物理完成或所有编码。

`EncodedPair.agda`使用本地Bool、Nat与intensional Id构造子，Agda2.8.0-3d04bac以`--safe --without-K --exact-split`接受。没有数学库、record η、Cubical Path、UA、HIT、postulate或未解元变量。`WithExt`显式接收Bool索引Set族上的dependent ext及其恒等律ext(λx.refl)=refl，故依赖β是条件定理；本包不证明这些假设存在或一致，不把Book的来源定理伪称此处已导出。

精确结果：

- C-342：给定上述ext/ext-id，对所有C:Encoded→Set、d:Πa,b:Nat.C(pair a b)、a,b:Nat，指定`encoded-elim C d (pair a b)`与`d a b`之间有`encoded-β`。`η-canonical`与`delivered-zero`是该假设下的辅助和实例。
- C-343：原始data pair的依赖β和编码后的直接左投影β均由`refl`给出，不依赖ext假设。
- NEG02：在同假设、同输入和同表达式上，以裸`refl`替换命题β证据，实际核在WrongJudgmental:14以`UnequalTerms`拒绝，exit42。它只证明这次检查的边界，不是一般无归约定理，更不是不终止证明。

正反控制保留同一数据。若原任务只是读取左分量，`projection-β`已给直接完成方式；不能把“指定的运输实现不直接化简”偷换为“这个任务在理论内无法完成”。若任务明确要求某旧consumer原有判断β，需把该接口要求单独列出，不能只给等价/命题路径便宣告满足。当前判词为计算接口区别，无合格现实相对见证。

原典对照：固定Book578b85cc的preliminaries959–1061/1978–1983，basics1568–1705及1191–1237，induction566–751。源文本明确命题/判断计算区别；本包没有重证w_d≃w_s≃w_h或全部编码定理。新增的`ext-id`不是秘密自动规则；它是Book2.9提到的命题恒等律在本包中的显式输入。

## 实际运行与证据

primary为`HoTT/verification/runs/20260924-MO3-COVERAGE-ENCODED-PAIR-001-02/`，exit0，无warning；控制为同前缀`NEG02`，exit42。五件套、source snapshots、index-row-manifest均在各run中保存。较早01/NEG01使用Builtin类型，实际也分别接受/拒绝；随后为了让数学来源完全在本包可见，改为本地同形构造，保留原run及at-run source-snapshot，不重绑旧hash。仅02登记primary。

共享capture_agda_proof_run.py硬编码环境为Cubical Path/HIT，不能忠实描述本次without-K片段。因此使用本包有限capture.py：独立复制已锁定Agda数据到fresh缓存，`--no-libraries --ignore-interfaces`执行给定源码，原件独占写入。它不是新的研究平台或共享治理修改；不用任何账户或全局配置。捕获manifest含36份builtin源码作为运行数据保守超集，primary02 stdout只列本地EncodedPair，不能说全部builtin都被证明使用。

当前两个证据检查已通过：verify_formal_proof_run给PASS_WITH_SCOPE；selected verify_proof_version_closure --evidence-only给LOCAL_EVIDENCE_PASS_NOT_VERSION_CLOSED。对应原始结果在Session-C/证据/B02/PROOF-CHECKS.json。Git闭合另核，不由本README自证。历史全registry Coq错配未修，也不是本包的数学依赖。

## 复现与边界

核TOOLCHAIN的binary字节/hash与当前数据路径后，使用`python3 -B HoTT/formal/mo3-coverage/encoded-pair/capture.py <全新20260924-MO3-COVERAGE-ENCODED-PAIR-…ID> EncodedPair.agda`捕获新run。原命令也在RUN.json，可用于固定环境重放；临时缓存不可得时应重新复制并产生新run，不改旧receipt。不能覆盖primary或为了得到PASS改变NEG02预期。

本包SOP反思：分母固定为一个表示与指定消费者；策略来自原规则取舍；研究者未代D；负结果限该refl检查；原典更宽内部化/coherence未由本包关闭；core未变；无方法漂移，reflection=no-plan-change；实际控制阻止把接口差别讲成任务绝对不可完成。全量KC/扩展与父范围处置在本单元Session-C记录继续归档。
