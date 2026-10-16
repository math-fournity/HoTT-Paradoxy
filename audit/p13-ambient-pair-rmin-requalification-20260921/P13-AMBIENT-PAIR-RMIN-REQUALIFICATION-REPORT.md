# P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-001：环境操作条件作为 `R_min` 的专门化

**状态：** `R_AMBIENT_SPECIALIZATION_ACCEPTED_WITH_SCOPE / OPERATION_CLASS_SPLIT_REQUIRED / P14_AMBIENT_OPERATION_K_SUCCESSOR_DISCOVERY_NEXT / NO_ACTUAL_K / NO_NEW_HOTT_DEFECT_CLAIM`

**日期：** 2026-09-21

## 1. 判词改变凭据

P12 只选择了候选：固定 `Plane`、嵌入、闭包余集与允许操作，能否成为一个非任意的 `R_min`／`Done` 专门化。P13 的新直接证据是同一对象对上已经保存、但 P12 未完整纳入的 C-269/C-270：`DeformationCircle.lean` 给出逐时嵌入的连续曲线变形，而 C-267/C-268 只否定整平面 homeomorphism 及其有限组合。

这会改变的不是 HoTT 一致性结论，而是 P12 留下的 `R_ambient` 候选的精确含义：若不把 operation class 写入 Done，就会把“有限环境同胚不能完成”与“连续曲线嵌入可以完成”错误合并为同一命题。P13 因而检查一项更窄的、可复用的任务合同；不重新运行 Lean，也不创建新的几何定理。

## 2. 本地资产复核与学术定位

### 本地覆盖裁决

| 资产 | 覆盖裁决 | P13 采用的直接事实 | 不能推出 |
|---|---|---|---|
| C-265/C-266 | `EXACT_REUSE` | `M=circleOpen`、`N=lineOpen`，并有 `embeddedIntrinsicHomeomorph : ↥M ≃ₜ ↥N`；指定平面的闭包余集分别是一点与两个不同点。 | 通常同胚为假，或所有嵌入不等价。 |
| C-267/C-268 | `EXACT_REUSE_FOR_AMBIENT_FINITE_OPERATION` | 无整平面 homeomorphism 将一者映成另一者；任何有限 `List (Plane ≃ₜ Plane)` 的 `runAmbient` 也不能由 N 得到 M。 | 任何连续曲线变形、切割、加点、重嵌入、无限极限或物理过程都不可能。 |
| C-269/C-270 | `PARTIAL_REUSE_FOR_POSITIVE_OPERATION_CONTROL` | 存在联合连续 `F : Icc(0,1) → Ioo(0,1) → Plane`，每个时间切片是 embedding，且初末像恰为 N/M；同一见证有统一空间界。 | 此变形延伸为整平面同胚、满足所有来源历史，或是物理过程。 |
| C-275–C-277 | `PARTIAL_REUSE` | `CurvePresentation` 已保存 completion、边界和保结构 ambient transport；裸 carrier 同胚不保持端点重合。 | P13 的完整 `C,p,M,N,e,operation,Done` 对象已经作为一个统一 Lean record 被定义。 |

当前源码哈希与 C-266..C-270 的保存 source manifest 一致；三个 run 都是 `KERNEL_ACCEPTED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。这是既有经典点集几何证据的资格化，绝非原生 HoTT 证明。

### 公开来源的有界复核

本 wave 的新术语是“通过 embeddings 的 isotopy”与“ambient isotopy”的区别。公开拓扑资料把 ambient isotopy 定义为环境空间自身的、逐时 homeomorphism 的连续族，而 embeddings 的 isotopy只要求对象的每个时间切片是 embedding。参见 [Rolfsen, *Knots and Links* 的定义](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/rolfsen.pdf) 和 [MathWorld 的 ambient-isotopy 条目](https://mathworld.wolfram.com/AmbientIsotopy.html)。

这给 P13 的术语一个独立、标准的拓扑参照，但不能把其一般 isotopy-extension 结论自动应用到本例：本地模型的源是开区间，P13 没有验证任何紧致性、流形、光滑性或 extension theorem 的前提。针对 HoTT 与 ambient/isotopy 的组合检索，未发现用户精确 `C,p,M,N,e,Done` 合同的实际 HoTT consumer；记录为 `NO_EXACT_HOTT_TASK_WITHIN_DECLARED_SEARCH`，不是全局不存在结论。

## 3. 专门化后的任务合同

令 `C = sphere(0,1)`，`p = pole`，`M = circleOpen`，`N = lineOpen`，`e = embeddedIntrinsicHomeomorph`。P13 不以 `H_intrinsic(M,N)` 自己充当完成条件，而固定两个不同的 operation-sensitive Done：

```text
H_intrinsic(M,N) := ↥M ≃ₜ ↥N

R_ambient^fin(D) :=
  (Plane, C, p, M ↪ C, N, e,
   closure(M) ∖ M = {p},
   closure(N) ∖ N = {lineEmbed 0, lineEmbed 1},
   Op_fin = List (Plane ≃ₜ Plane))

Done_ambient^fin(D, hs) := runAmbient hs N = M

R_curve(D) :=
  (same Plane, C, p, M, N, e,
   Op_curve = jointly-continuous F with every F_t an embedding)

Done_curve(D, F) := range(F_0) = N ∧ range(F_1) = M
```

| `OriginDirectedDiagram` 字段 | P13 中的具体承载 | 已有证据 |
|---|---|---|
| Static：`C,p,M↪C,N,e` | 指定单位圆、`pole`、两个实平面子集和 `embeddedIntrinsicHomeomorph` | C-265/C-266 |
| boundary / closure | `closure M ∖ M` 是单点，`closure N ∖ N` 是两个不同点 | C-266 |
| Process / operation-spec（负控制） | `runAmbient : List (Plane ≃ₜ Plane) → Set Plane → Set Plane` | C-268 |
| Observation / `Done_ambient^fin` | `runAmbient hs N = M`；对任意有限 `hs` 为假 | C-267/C-268 |
| Process / operation-spec（正控制） | `curveMotion` 的联合连续、逐时 embedding 族 | C-269 |
| Observation / `Done_curve` | 初像精确为 N，末像精确为 M | C-269；C-270 另给统一空间界 |

两个 Done 的真值不同不是矛盾：它们量化的 operation class 不同。`H_intrinsic` 也不蕴含任一 Done。这个区分是 P13 的核心结果。

## 4. 判定

`R_AMBIENT_SPECIALIZATION_ACCEPTED_WITH_SCOPE` 成立，但其完整名称应是“**环境—操作敏感的专门化**”，不是“环境差异使 N 一般不能变成 M”。它不是纯 `RESTATEMENT_ONLY`，原因有三点：

1. P6 的字段矩阵只一般地要求 operation-spec/Done；P13 将它们绑定到两个有独立标准术语、同一输入对和相反实际控制的 operation classes。
2. C-268 的有限环境操作反控制与 C-269 的曲线嵌入正控制给出因果对照：去掉“整平面 homeomorphism”限制确实改变 Done，而不是只改变叙述。
3. 这个合同可成为 future-K 的判别器：一个真实 HoTT 使用处若只得到 `H_intrinsic`，却把它作为 `Done_ambient^fin` 或 `Done_curve`，则可按 P7 的五项准入条件审计；目前没有发现这样的 K。

## 5. 波次定位、停止与 P14

1. **最终目标连接：** P13 收紧 P1/P6 的 R 端，使“来源—操作—复原”不再停留在静态字段清单，而有一个固定的操作/完成对照。
2. **全局坐标：** 它是对象理论线的受限专门化；不替代 P2 规则桥、P3 实际消费者或 P4 实现审计。
3. **实际价值：** 它否定了“同胚自动意味着可完成”与“环境反控制意味着绝对不可完成”两种过强读法，减少 future-K 审计中的换题风险。
4. **为何不继续 P13：** 当前源、命题、操作、反控制和正控制均已固定；再次重跑 Lean 或追加同义字段不能改变判词。
5. **后继：** `P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-001`。它必须在未审的、版本固定的 HoTT/立方/相关形式库或论文调用中寻找实际 K：输入是否仅有 `H_intrinsic`/bare equivalence，输出是否被宣称为 P13 的某个 `Done`，以及代码是否实际忘却 operation/closure 数据。

**裁决：** `SWITCH_BRANCH / R_AMBIENT_SPECIALIZATION_ACCEPTED_WITH_SCOPE`。P14 尚未启动。P13 没有找到实际 K、没有新数学定理、没有理论—实现差异，也没有 HoTT 缺陷结论。

## 6. 禁止外推

- 本结论不说通常拓扑把 M/N 判错；内在 homeomorphism 正控制仍保留。
- 不说所有现实或数学操作均不能、或均能将 N 变为 M。
- 不把 `curveMotion` 的连续 embedding isotopy 偷换成 ambient isotopy；也不将未验证的 isotopy-extension theorem 用作本例推理。
- 不把经典 Lean 证明、标准拓扑术语或未命中的 HoTT 检索写成 HoTT 理论命题、实际 K 或 HoTT 缺陷。
