# bare ZFC 的 Q 理论精度：本轮收尾裁决

> **身份：** F049_CLOSEOUT / SOURCE_BOUND_APPLICATION_INTERFACE_CONTROL / NOT_A_BARE_ZFC_INCONSISTENCY。
>
> **执行合同：** [BARE-ZFC-Q-PRECISION-SOP](../dev-docs/BareZFC理论精度Q形式化SOP.md)。
>
> **结论范围：** SEP、IEP、Norton 的冻结来源分母，以及 C-364 的有限 completion-contract model。

## 1. 研究问题与已完成的工作

用户所说的 bare ZFC “理论精度不够”，本轮被保持为下列可证伪问题：

    ZFC 可以表示时间、阶段、序列与过程；
    但一个被实际用来宣布“解答”的基础性 application interface，
    是否把 FormalDone 和 OriginDone 区分开，
    并要求支付从前者到后者的 completion bridge？

这避开两种错误收缩：

1. 不把“ZFC 的语言没有时间 primitive”改写成“ZFC 无法编码过程”；
2. 不把一个来源中未支付的 bridge 改写成 ZFC 对象语言的矛盾。

P0–P3 与 M2/M3 已全部按该范围执行。得到的不是 ZFC 推出 False，而是一个有明确来源边界的接口结论。

## 2. P0–P3 裁决

| 层 | 已核验事实 | 判词 |
|---|---|---|
| P0：语言／基础位置 | SEP 将 ZFC 固定为 equality 加 membership 的一阶公理系统，同时说明数学对象和 relations 可被表示为集合。 | P0_LANGUAGE_FIXED / BARE_SEMANTIC_COMPLETION_INTERFACE_UNDERDETERMINED |
| P1：过程合同 | IEP 把带 Choice 的 ZF 支撑的标准实分析放入 Standard Solution；Norton 给出 strict 与 revised completion 的不同合同。 | P1_APPLICATION_CONTRACT_FIXED_WITH_SCOPE / SOURCE_APPLICATION_OWNER_ONLY |
| P2：投影与控制 | C-364 构造两个同样输出 coarse resolved 的 contract worlds，但 OriginDone 相反；并给出 rich contract view 和 finite code view 正控制。 | P2_INTERFACE_RELATIVE_C364_MACHINE_PROVED |
| P3：归因 | Norton 明示删去严格 first/last action 条件，而不是证明 revised completion 保持 strict OriginDone。 | P3_EXPLICIT_TASK_SWITCH / BRIDGE_UNPAID_BY_THIS_SOURCE |

这四行共同导出：

    SOURCE_APPLICATION_INTERFACE_CONTROL_COMPLETE
    BARE_SEMANTIC_INTERFACE_UNDERDETERMINED_WITH_SCOPE

其中“underdetermined”不是把未知包装成发现。它有具体含义：当前一手来源定义了 ZFC language 和一个 ZFC-supported Standard Solution application，却没有定义一个可归于 bare ZFC 本身的 semantic completion interface。因此研究者可以对该 application view 证明精度边界，不能将它叫作 bare-ZFC defect theorem。

## 3. C-364：机器证明了什么

[BareZFCPrecision.lean](../HoTT/formal/bare-zfc-q-precision/BareZFCPrecision.lean) 的精确 kernel 结论是：

1. 固定 standardResolutionView 把 strictOriginal 与 revisedTask 都映成同一个 resolved；
2. 这两个 world 都有 FormalDone，但只有后者有 OriginDone；
3. 因而没有任何只读取 standardResolutionView 的 decoder 能决定 OriginDone；
4. 同一个 coarse view 也不能支付全域 FormalDone 到 OriginDone 的 bridge；
5. 直接保存 contract 的 rich view，以及一个明示的有限 process code，都能决定 OriginDone。

主 run [20261004-MP-BARE-ZFC-Q-PRECISION-001-03](../HoTT/verification/runs/20261004-MP-BARE-ZFC-Q-PRECISION-001-03/RUN.json) 使用 Lean 4.34.1 core，exit 0、stderr 0，十个所选定理均打印为无公理。proof-run verifier 的精确重放结果为 EXACT_EXIT_STDOUT_STDERR_MATCH。

反向控制 [NEG-004](../HoTT/verification/runs/20261004-MP-BARE-ZFC-Q-PRECISION-NEG-004/RUN.json) 故意让 constant coarse view 解码 strict OriginDone；Lean 在 False ↔ True 分支拒绝。

## 4. H095 的独立来源映射

H095 使用项目外、只读、禁网的 Codex App Server worker：

| 约束 | 观察到的结果 |
|---|---|
| 模型 | gpt-5.6-terra / max |
| source payload | 只包含冻结 SEP／IEP／Norton facts 与 TaskCard |
| 权限 | read-only、network disabled、approval never |
| 副作用 | 0 command、0 file change、0 approval request |
| 终态 | 正常完成；公开 E0–E7 MatchTrace 完整 |

它独立选择 application interface 为 resolution / bridge 责任的唯一有来源位置，而拒绝把 bare ZFC syntax 当作 bridge obligation 的来源。完整的 NodeCard、payload、公开结果和 trajectory 范围记录见 [H095 report](20261004-P-DAG-SOURCE-095-BARE-ZFC-Q-PRECISION-Terra-Max.md)。

该运行的 raw wire 没有完整 isolated AGENTS 正文，因而 L1 保持 NOT_FULLY_CERTIFIED；这并不被“模型输出合理”覆盖。source-input preflight、精确 model/effort/start fields、无工具与正常终态均有独立收据。

## 5. 本轮没有证明的事

以下句子仍然不能从现有证据得到：

- bare ZFC 在对象语言中矛盾；
- bare ZFC 无法表示时间、程序、数列或含 process contract 的集合；
- 所有极限理论或所有 Standard Solution 都没有保留原过程；
- Zeno／圆环与固定 HoTT Q 已经是同一个完整 Q；
- ZFC 已被证明在时间维度上理论精度不足。

最后一句是用户提出的理论假说，当前被收紧到一个清晰的下一来源条件，而没有被错误宣布为数学定理。

## 6. 形式化证据卫生与治理修复

本轮捕获过程中发现两项真实的工具链问题，并没有把它们当作数学结果：

1. 初版 main capture 将 JSON 末尾写成 literal backslash-n，使 run -01、-02 的 JSON 无法被 registry 读取；修复后 -03 才是有效主 run。
2. Lean 的 expected-negative diagnostic 写入 stdout；初版 NEG-001 只查 stderr，因此把正确拒绝误记为 unexpected。捕获器修正后，最终使用 NEG-004；中间 NEG-002/-003 保留为 source snapshot 演进前的历史尝试。

此外，数学证明治理 verifier 曾要求纯导航性质的 .codex/AGENTS.md 和 local-session skill 复制根 marker。实际架构已要求二者路由到根 AGENTS／PROTOCOL；verifier 已改为检查这一 routing relation，并补充两个 fail-closed tests。六个治理测试和静态 verifier 均通过。

## 7. F-049 的当前状态与重开条件

F-049 在本 SOP 的当前分母内已到合法终点：

    CLOSED_WITH_SCOPE
    SOURCE_APPLICATION_INTERFACE_CONTROL_COMPLETE
    BARE_SEMANTIC_INTERFACE_UNDERDETERMINED_WITH_SCOPE

只有以下任一事实可以重开：

1. 一份版本固定的一手 source 明确把 bare-ZFC formal acceptance 本身提升为同一原过程或物理 Done；
2. 该 source 未给 FormalDone 到 OriginDone 的 bridge/payment；
3. 研究发起人给出一个不同且稳定的 OriginDone 合同，令当前 two-world control 不再保真。

在这些条件出现前，继续累积同样的 toy projection、仅重复“ZFC 没有时间 primitive”或仅增加相似 Zeno 综述，都不会推进 F-049。
