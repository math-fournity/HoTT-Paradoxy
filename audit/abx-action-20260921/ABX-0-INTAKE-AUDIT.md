# ABX-0：GLM Flash/G4 历史资产与当前任务的接收审计

## 审计对象和证据边界

本审计评价 ZCode 会话 `sess_7cb03240-9567-4a2e-9061-b6f0273cd09b` 的 Flash/G4 工作能否作为 ABX 的输入。用户当天 `log/zcode-2026-09-21.jsonl` 只给出 request 元数据，正文为空；完整历史审查使用同一 SID 的 `model-io` 与只读 SQLite 消息/part 视图，见[ZCode 7cb 会话成果吸收审查](../../Astra继续尝试/ZCode-7cb会话成果吸收审查.md)。原始 raw model-io 不复制进 Git；其当前路径、hash 和私有审计 locator 记在[SOURCE-IMPORT.json](SOURCE-IMPORT.json)。

本审计检查：用户 ABX 输入是否被精确保存；四个 Flash 模块/已有 run 的当前身份是否仍与历史审查一致；历史工作究竟交付了哪一级内容。它不证明原圆环模型、`H_top`、`R_origin`、实际消费者 `K` 或 HoTT 缺陷。

## 已核实资产

| 资产 | 当前可核事实 | 使用范围 |
|---|---|---|
| 用户 ABX 背景 | 外部附件与 repo snapshot 字节相同，sha256 由导入收据冻结 | 用户原意与历史 AI 引文的来源，不把引文当定理 |
| ZCode 7cb 历史工作 | 既有审查读到 SQLite 357条可见文本、624工具项；旧 raw 可见尾部与原生文本有交叉核对 | 会话发生、工作顺序和模型自述的历史证据；不认证前段全部模型请求上下文 |
| `RingOrigin` | `SourceCarrier C p := Σ x:C, ¬(x=p)`、配对与整数正例的指定 Agda 项有保存 run | 富化排除证据正控制 |
| `NoBreakoutFromBare` | `f p refl` 否定“每个 x 都避开已给 p”的规格 | 过强全域排除规格的反证控制 |
| `BreakpointBridge` | 同一 `ExcludedCarrier` 上的恒等函数 | 两条研究线的检查形状可复用 |
| `CutAsSourceCarrier` | 既有排除证据的函数族恒等延伸 | 谓词应用正控制 |

历史审查曾对四个保存 run 执行 `--rerun`，均返回 `PASS_WITH_SCOPE`；当前本轮再以不重跑模式检查其 receipt/source/index 关系。`SOURCE-MANIFEST.json` 的 13 个路径哈希与当前文件一致，说明 ABX 接收的正是被 2026-09-20 审查过的源版本。

## 判定

GLM **确实尝试过 ABX 的前身 G4**，而且留下了有价值的可重放控制和一条“不要只靠静态等价”的发现方向。它没有完成 ABX：未给出实际圆/开区间 `H_top(M,N)`，未给出来源—复原关系 `R_origin`，未固定过程性 `Done_strong`，未定义明确 forgetful map `U`，未找到真实 HoTT 使用事实 `K`，也未建立失配。

它的最重要方法性错误是从“来源可用 Σ 记录”跳到“任何只走 univalence/等价的消费者都会自动丢来源”。已携带在 Σ/record 中的字段可以随等价运输；信息丢失必须经由一个明确 U 或实际消费者的输入接口来证明。现有 `NativeSourceContract`/`NativeTaskIntegration` 正是 ABX 必须保留的反向控制。

因此 ABX 与 GLM G4 的关系是：

```text
GLM G4 = 已有的控制、命题形状和未完成线索
ABX    = 重新固定原 A/B/X 后，对 H_top、R_origin、U、K 和同一 Done 的完整候选链
```

ABX 可复用前者的 precise terms/run evidence，却不能继承其“来源胚型已等于圆环问题”“univalence 自动丢 R”“参数化控制足以延后几何”的解释。

## 反证与下一步

若未来 ABX-1 显示裸 `N` 在指定 `Done_strong` 下存在合法来源保持恢复，ABX 当前失配候选应撤回或缩窄。若固定消费者分母没有 K，只能记录有界负结论。只有一个具名 K 真正使用 `H_top`／U 并将结果当作 B 的完成时，才进入 ABX-2/4 的机器证明。
