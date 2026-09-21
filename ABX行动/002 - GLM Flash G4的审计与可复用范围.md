<!-- governance-shard:v2
logical_id: ABX-ACTION
shard_id: 002
index: ../ABX行动.md
-->

# GLM Flash G4的审计与可复用范围

## 1. 已核实的工作身份

GLM 的 ZCode 会话是 `sess_7cb03240-9567-4a2e-9061-b6f0273cd09b`，模型日志与 SQLite 原生可见文本的既有审查位于[ZCode 7cb 会话成果吸收审查](../Astra继续尝试/ZCode-7cb会话成果吸收审查.md)。用户指定的当天 `log/zcode-2026-09-21.jsonl` 只含无正文的 request 元数据；完整会话正文的历史核查使用私有 `model-io-sess_7cb…` 与只读 SQLite 快照。ABX 记录这一区别，避免把元数据日志当成完整对话证据。

Flash/G4 的四个已保存模块及其既有 run 都存在，当前源码哈希与 2026-09-20 审查的 `SOURCE-MANIFEST.json` 一致：

| 模块 | 内核接受的精确内容 | 可复用身份 | 不构成 |
|---|---|---|---|
| `RingOrigin.agda` | `SourceCarrier C p = Σ x:C, ¬(x=p)`、给定排除证据的配对和整数正例 | “富化表示可以携带排除证据”的正控制 | 圆/开区间模型、两个端点、来源历史、从裸 `N` 恢复 `p` |
| `NoBreakoutFromBare.agda` | `¬ ((x:C) → ¬(x=p))`，证明体为 `f p refl` | 排除“所有点都不等于指定 p”的过强规格 | 忘却接口、裸 `N` 的恢复失败、一般参数性元定理 |
| `BreakpointBridge.agda` | 同一 `ExcludedCarrier` 的恒等函数 | 两条研究线可以复用“排除证据”这一检查形状 | 圆环和实数/切割的任务桥 |
| `CutAsSourceCarrier.agda` | `(q:C) → (q≠r) → (q≠r)` 的恒等延伸 | 谓词应用的正控制 | 实际 GOLD L/U cut、序结构、来源或复原任务 |

四个历史 run 的来源与收据资格已被既有审查重放为 `PASS_WITH_SCOPE`。这证明指定 Agda 项被 kernel 接受，不证明 GLM 对“胚型”“断点三件套”“自动丢来源”或“植入现场”的自然语言解释。

## 2. GLM 的价值

GLM 做对了三件重要的准备工作：

1. 把“来源信息”从口头直觉变成可携带数据的方向；
2. 为富化数据、排除证据和具体非空实例保存了可重放的正控制；
3. 明确把真实消费者检索列为后续义务，而没有让最初 `RingOrigin` 直接声称发现了 HoTT 缺陷。

这些资产应作为 ABX 的控制和历史证据保留，不必重写或重跑同一模块。

## 3. 必须纠正的四个跳跃

1. `Σ x:C, x≠p` 的 `p` 是外部参数；它没有把 `p` 从对象内部“取出”，更没有编码完整去点圆的来源历史。
2. `no-breakout-from-bare` 否定的是每个 `x` 都避开已给 `p` 的不可能规格；它没有定义 `U`、没有输入裸 `N`，也没有声明恢复目标。
3. `bridge x = x` 只是同一类型上的恒等函数；没有建立 `√2` 与圆环、GOLD 与来源对象或两项 Done 的保真翻译。
4. univalence/等价不会自动丢失一个已经纳入 Σ/record 的字段；只有明确的 `U` 或实际消费者忽略该字段时，才可能出现 ABX 要检验的信息丢失。

因此 Flash/G4 是 `CONTROL_AND_HEURISTIC_INPUT`，不是 ABX 的已完成第三弹，也不是被旧 `Spec_A`／`Spec_B` 审计否定的同一命题。

## 4. 与已有 Astra 控制的关系

`NativeSourceContract.agda` 是 ABX 的必要反向控制：它实际使用同胚等价/运输，却让 `Satisfies` 依赖完整 `Denotes`，并证明裸 `nRich` 不满足。`NativeTaskIntegration.agda` 也把同一对象对置于不同操作合同中。ABX 必须把这些结果当作“理论可以保住 R”的正例，而不是绕开它们去制造失配。

## 5. 已知技术取舍不能替代 ABX 的 K

GLM 的会话把 Book §11.2 的 universe/Ω 讨论、`SingleOmega` 的项目内 B1a 充分性和 cubical canonicity 叙述成“共同体知情地使用非现实元素并分层处理”。这个表述需要收窄。Book 确实公开讨论 universe bookkeeping、resizing、mere-proposition LEM 和 initial σ-frame 等选择，但没有将它们命名为非现实性危机；`SingleOmega` 是项目形式化名，B1a 只证明给定它的充分性，反向必要性仍是 conjecture。

同样，Book 拒绝的 `LEM∞` 是对所有类型的朴素排中；它同时区分可一致加入的 hProp-LEM。Huber 的 cubical 论文证明特定 cubical calculus 的 canonicity，而不是证明该 calculus 的 univalence 已破坏 canonicity。故这些来源不能替代 ABX 的真实 K。详细审计见[已知技术取舍与非现实性解释审计](../audit/abx-action-20260921/ABX-已知技术取舍与非现实性解释审计.md)。
