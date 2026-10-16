# R3-R4-GODEL-RETURN-001：从独立句机器核到 exact HoTT calculus 的保真桥

状态：`ACTIVE / TASKSPEC_FROZEN / IMPLEMENTATION_NOT_STARTED`  
父目标：`A-HOTT-MACHINE-OVERVIEW-GOAL-002`  
前置：`CE-MAP-001 = CE_MAP_V1_COMPLETE_WITH_SCOPE`  
证据纪律：R3、R4、HoTT 必要性和现实相对解释分别验收；任何尚未过 F-011 的命题只登记为 `QUESTION` 或 `CONJECTURE`。

## 1. 为什么现在回到 Gödel

CE-MAP 将 C-227–C-243 的三个 internalisation no-go 归为同一机制 pattern，并确认 crisp/global、degenerate+transport、pointwise-fibrant input 等受限接口能够完成来源系统声明的真实任务。这条线仍可能产生新的 consumer-specific 失配，但当前最高判别力不再来自重复构造同型 no-go，而来自尚未闭合的另一块：一个 exact HoTT calculus 能否承载有效语法、证明谓词、算术表示、对角化和独立句。

本任务不把一般 Gödel 不完备性自动记作 HoTT 悖论。它要机械回答两件不同的事：

1. **R3**：是否已有一个精确、有效、足够强且一致性条件明确的对象理论，在当前 repo 中能够从源码和 kernel run 重放独立句；
2. **R4**：能否把 R3 的每项前提保真连接到一个具名 HoTT calculus，而不是只把普通算术或证明搜索写在 HoTT/Agda/Coq 宿主中。

## 2. 冻结输入

- C-157–C-187：当前 Cubical Agda proof-code、编码、parser、formula infrastructure 与已记录 blocker；
- C-223–C-226：`akaposi/cohtt@5babc385` groupoid syntax exact slice；
- `audit/imports/machine-overview-ce-map-20260915/source/evaluations/COQ-SYNTHETIC-INCOMPLETENESS-REPLAY-001/`：外部 worktree 中已冻结到 main 的 Coq build/source/replay manifests 与报告；
- `audit/imports/machine-overview-ce-map-20260915/source/evaluations/CUBICAL-GODEL-PROOF-CHECKER-001/REPORT.md` 与 `CUBICAL-SYNTHETIC-INCOMPLETENESS-001/REPORT.md`：既有候选、失败和范围；
- `audit/literature/LIT-CLASSICS-001/mineru/Kirst-Peters-2023-Godel-Without-Tears/full.md`、O’Connor 2005、Gödel 1931、Rosser 1936、Kleene 1938、Löb 1955 与 Lawvere 1969 的已冻结全文；
- `LIT-HOTT-COMPUTABILITY-001` 中 2LTT/groupoid-syntax/Extension Types 路线；
- `audit/ce-map/CE-MAP.json` 通过 manager query 的 R3/R4/SELF_REFERENCE 未覆盖 cells；不得全文预载巨型 JSON。

外部 worktree、论文或历史 AI 报告只能是来源。进入当前结论的 proof source、run、failure 和对应关系必须保存到 main。

## 3. R3 精确验收

先选择一个当前可重放的最小对象理论与作者实现，优先顺序：

1. 已冻结 `COQ-SYNTHETIC-INCOMPLETENESS-REPLAY-001` 的 exact source commit/toolchain；
2. Kirst–Peters 的 Robinson `Q` Coq 实例；
3. `agda-godel-tree` 的 Basic Recursive Arithmetic；
4. Lean Foundation 的独立实现作 differential holdout。

R3 只有在以下内容全部机器化时才关闭：

- 语法与 derivation/proof predicate 有总 checker 或可枚举证明关系；
- 编码/解码与 substitution/diagonal 所需往返性质；
- 理论有效性/可枚举性、足够表达力与一致性或 soundness 前提逐项显式；
- 构造具名句 `G_T`，机器证明条件式 `T ⊬ G_T`，若目标是 Rosser 强度则另证明 `T ⊬ ¬G_T`；
- bounded proof/refutation search 的每一步终止；对 `G_T` 的无界搜索不完成只能由上面的不可证明性定理推出，不能从一次 timeout 推出；
- `Print Assumptions` 或相应 kernel dependency closure、正负 controls、exact replay 与 F-011 receipt。

## 4. R3→R4 保真义务矩阵

对选定 exact HoTT calculus 建立一张逐项矩阵；每行只能是 `PRESENT_MACHINE_PROVED`、`PRESENT_SOURCE_REPORTED_NOT_REPLAYED`、`ABSENT_BY_DEFINITION`、`OPEN` 或 `NOT_APPLICABLE`：

| 义务 | 需要的实物 |
|---|---|
| `H-SYNTAX` | contexts/types/terms/substitutions/judgments 的 raw inductive 或 HIIT/QIIT syntax |
| `H-CONVERSION` | conversion/definitional equality 的可检查关系或经过保真翻译的 checker |
| `H-NAT` | Nat、0、succ、加乘及编码算术所需规则 |
| `H-ID/PATH` | 一般 identity/Path formation/elimination/computation；不能用宿主 equality 冒充对象规则 |
| `H-UNIVALENCE/HIT` | 若声称 HoTT essential，必须纳入 exact rule 或公理 schema；否则明确是弱 calculus |
| `H-PROOF-CODE` | derivation 的自然数编码、decoder、checker/enumerator 与范围 |
| `H-SUBSTITUTION` | formula/term substitution 与 free-variable/capture 纪律 |
| `H-ARITH-INTERP` | R3 算术或足够理论到 HoTT syntax 的 interpretation |
| `H-REPRESENTABILITY` | checker、substitution、编码函数在对象理论中的强表示 |
| `H-FIXPOINT` | 对角/不动点引理的对象层实例 |
| `H-INDEPENDENCE` | exact HoTT theory 的条件性独立句定理 |
| `H-EFFECTIVITY` | 公理/rule schema 是否有效可枚举；oracle/choice/resizing/quotient computation 必须显式 |

当前 C-223–C-226 只能预填 `H-SYNTAX` 的 Π/U/El/groupoid-coherence 子集；其余不得从“源文件能编译”推定。

## 5. 机器构造与不会停机的精确位置

实现两套彼此区分的程序：

1. `checkProof : Code → Formula → Bool` 或关系式等价物：对每个有限输入必须停机；
2. 公平 dovetail 的 `searchProofOrRefutation(T, φ)`：逐步枚举 proof code 并检查 `φ` 与 `¬φ`。

对一般 `φ`，搜索是部分计算。对机器证明独立的 `G_T`，如果 `T` 满足冻结前提，则两个正分支都不会被命中。可交付结论是“每个有限阶段均未命中，且独立性定理排除任何有限 proof code”，不是“运行很久所以不会停”。若编译器/宿主在检查有限 proof code 时本身不终止，那是 checker/实现缺陷，不能与 Gödel 不完备性混称。

## 6. HoTT 必要性消融

至少执行四个对照：

- `ARITHMETIC-ONLY`：删除 Path/univalence/HIT，只保留算术理论；若结果不变，则不完备性机制一般而非 HoTT 特有；
- `GROUPoid-SYNTAX-WEAK`：仅用 C-223–C-226 当前 slice；记录确切缺失义务；
- `HOTT-EXTENDED`：逐一加入 Nat、Path、univalence/HIT 或其它规则，检查 effectivity/representability 是否保存；
- `META/OBJECT`：把宿主 Agda/Coq/Lean 的函数和对象 calculus 内部可表示函数分开。

只有某个 Path/univalence/HIT/高阶构造改变独立句、证明谓词或有效性边界，并通过删除该构造的同任务消融，才能升级为 `HOTT_ESSENTIAL`。否则登记为 `GENERIC_GODEL_BOUNDARY_WITH_HOTT_INSTANCE`。

## 7. 与现实相对悖论的桥梁

即使 R4 成功，也只说明 exact HoTT calculus 的内部证明能力存在条件边界。要进入根 Goal，还必须另行冻结现实任务：现实侧实际需要什么答案、在什么输入/观察/完成标准下能够完成，以及理论抽象如何使该能力丢失或虚增。不得把“真但不可证”直接等同为“现实可完成而 HoTT 不可完成”，也不得把外部元理论知道 `G_T` 的构造误写成对象理论绕过 ASK 获得其真值。

## 8. 本轮最小完成与下一分叉

第一 bounded slice 以 `R3-SOURCE-REPLAY-001` 为目标：资格化并重放一个现有作者的完整 R3 theorem package，输出 exact theorem/assumption/source/toolchain/run 表，同时把当前 Cubical infrastructure 与它逐义务对照。完成后按结果选择：

- R3 重放成功且 HoTT 义务可实现：进入 `R4-HOTT-CALCULUS-BRIDGE-001`；
- R3 成功但现有 HoTT syntax 缺关键机制：构造最小缺口或加入一个规则的 vertical slice；
- 上游实现无法重放：保留失败收据并切换第二作者实现；
- 机制经消融完全一般：保持 Gödel 边界，但回 CE-MAP 选择 HoTT-specific 或现实 cell。

本 TaskSpec 的存在不证明 R3/R4 成立，不能完成根 Goal。
