# 验证事件最小实例：命题与证明索引

Proof ID：MP-VERIFICATION-EVENT-001。

共同范围：三状态 initial/afterP/afterHistory；三条命题代码 atom/historical/current；Registered 的三个明示构造子；P=Unit。K 是该有限台账的命题截断。使用原生 Cubical Path、transport 和高阶归纳截断；未调用 univalence。用户源码没有 postulate、未解洞或终止检查覆盖。

数学状态：FORMAL_CHECKED_WITH_SCOPE。主源码由 attempt-003 接受；交付复跑为 positive-final-001。它们只认证下列精确类型。当前 proof package 位于用户授权的 repo 外隔离目录，未导入共享矩阵，LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED。

| Claim ID | 精确形式命题/符号 | 源码 | 证据 | 禁止外推 |
|---|---|---|---|---|
| EVT-01 | Step initial afterP × Step afterP afterHistory；twoEventTrace | formal/VerificationEvent.agda | positive-final-001/RUN.json | 是明示有限事件模型，不是实际设备轨迹 |
| EVT-02 | ∀ s c, K s c → Meaning s c；knowledgeSound | formal/VerificationEvent.agda | positive-final-001/RUN.json | 只证明此有限注册规则健全，不证明HoTT自身全局健全 |
| EVT-03 | Current initial；¬Current afterP；¬Current afterHistory；decideCurrent 对应 true/false | formal/VerificationEvent.agda | positive-final-001/RUN.json | 仅指定状态、固定原子与定义；不是一般知识的判定算法 |
| EVT-04 | K afterHistory historical；Historical；historicalKnownLater/historicalVerifiedLater | formal/VerificationEvent.agda | positive-final-001/RUN.json | 后来可以核查固定过去；不声称当前仍未知 |
| EVT-05 | ¬(Historical → Current afterP)；¬(Current initial ≡ Current afterP) | formal/VerificationEvent.agda | positive-final-001/RUN.json；negative-001 为拒绝校准 | 不能外推任意不同时标的命题都不同 |
| EVT-06 | ∀ F:Trunc Stage→Set, (∀s,Current s→F(inc s)) → (∀s,F(inc s)→Current s) → Empty | formal/VerificationEvent.agda | positive-final-001/RUN.json | 只否定这次完全阶段擦除的双向保真，不证明所有抽象失败 |
| EVT-07 | ∀s,Current s→stageAwareFamily s；stageAwareIdentity | formal/VerificationEvent.agda | positive-final-001/RUN.json | 保留阶段的表示正控制，不证明任何现实模型足够 |
| EVT-08 | 在显式 factivity 与 conjunction-closure 参数下，Know(A×¬Know A)→Empty；noKnownMoore | formal/VerificationEvent.agda | positive-final-001/RUN.json | 不是全套Fitch/Gödel定理，不证明HoTT存在这种全域Know算子 |

运行根为 verification/runs/。原始 stdout/stderr、环境、source-manifest、源码快照、捕获脚本与内建接口输入哈希均保留。负向 BadCast.agda 故意不通过，不能作为通过的证明源码引用。
