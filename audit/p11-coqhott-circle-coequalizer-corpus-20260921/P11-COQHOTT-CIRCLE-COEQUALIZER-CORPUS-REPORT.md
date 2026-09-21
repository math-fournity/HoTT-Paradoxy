# P11-COQHOTT-CIRCLE-COEQUALIZER-CORPUS-001：非定向 HoTT Circle/Coeq source audit

**状态：** `NOT_A_CONSUMER / DEFENSE_EXPLICIT_GLUING_AND_COHERENCE / EXPLICIT_ADMITTED_TORUS_BOUNDARY / P12_THIRD_SUCCESSOR_DISCOVERY_REQUIRED / NO_NEW_HOTT_DEFECT_CLAIM`
**固定分母：** `HoTT/Coq-HoTT@e3deab71b9cb53a22c00ab39dea4699dd2c89a13` 的 README、`Colimits/Coeq.v`、`Spaces/Circle.v`、`Spaces/Torus/Torus.v`、`Spaces/Torus/TorusEquivCircles.v`。
**范围：** version-pinned source audit；未编译 Coq-HoTT、未审计其他文件，也不把 source 文本当作 kernel replay。

## 1. 任务与直接代码事实

P11 只问：该外部非定向 HoTT library 是否把原圆环 `OriginDirectedDiagram` 的 `U_bare` 或 `H_top` 信息，当成原 `Done_s` 的完成；或者它是否明示自己的粘合数据和不同任务。

固定源码显示：

```text
Coeq(B,A,f,g)            := GraphQuotient(… f … g …)
coeq(a)                  : Coeq f g
cglue(b)                 : coeq(f b) = coeq(g b)

Circle                   := Coeq Unit Unit idmap idmap
base                     := coeq tt
loop                     := cglue tt
```

`Coeq_rec` 不只接收目标类型；它还要求从 `A` 到目标的函数以及每个 `b : B` 的明确相容路径。`Circle_ind` 同样要求 `b : P base` 与 `l : loop # b = b`。因此这里的“识别”是明确的高阶构造/路径数据，不是一个“把两个点逐步靠近到零距离”的分析极限操作。

下游 `TorusEquivCircles.v` 也没有用裸区间产生原圆。它把 `Circle_rec` 用于已有 `Circle`，显式给出 torus 的 base、两个 loops 与 square；最终构造 `Torus <~> Circle × Circle`。这是一项 synthetic homotopy 任务，未声称它完成 `C,p,M,N,e`、闭图 trace 或用户的 `Done_strong`。

## 2. P7 五项 K 判别

| 条件 | 直接证据 | 判定 |
|---|---|---|
| `K-version` | Git commit、五个 blob/SHA、源文件和 P10 freeze 固定。 | `PASS_VERSION_IDENTITY` |
| `K-input` | `Coeq` 显式接收 `B,A,f,g`；Circle 固定为 `Unit,id,id`；Circle/Torus 消去要求 base/loop/square/coherence。没有 `U_bare(OriginDirectedDiagram)` 或 `H_top(M,N)` 输入。 | `FAIL_AS_K / EXPLICIT_GLUE_INPUT` |
| `K-output` | Circle 的 `base/loop`、递归原则，以及 `Torus <~> Circle × Circle` 均可定位。 | `OUTPUT_LOCATABLE_BUT_TASK_DISTINCT` |
| `K-claim` | 五文件中没有 `OpenRealInterval`、`Punctured`、`OriginPresentation`、`Done_strong`、closure trace 或原 `C,p,M,N,e` 合同；实际注释把对象称为 Circle、Coeq、Torus 与 loops。 | `NO_SAME_TASK_DONE_CLAIM_WITHIN_DECLARED_SCOPE` |
| `K-forgetting` | `cglue`、`Coeq_rec` 的相容路径、`Circle_ind` 的 loop coherence、Torus 的 loops/surface 都是显式输入或公设；不存在把这些字段无声忘却的 source path。 | `FAIL_AS_K / DEFENSE_EXPLICIT_GLUING_AND_COHERENCE` |

因此这不是合格 K。它支持一条有限而重要的反解释：一个实际 HoTT library 在明确构造粘合对象时保留生成元与相容条件，而不会把原圆环的裸 `N` 误写为“已经恢复指定闭合过程”。

## 3. Torus 的 `Admitted` 边界

`Torus.v` 的 `Torus_rec_beta_surf` 在源文中以 `Admitted` 结束；`TorusEquivCircles.v` 的 `t2c2t` 和 `c2t2c` 使用该命题。这是一个**源代码可见的信任/未完成边界**：若该 source 被编译，Coq 对这条陈述的处理取决于其 `Admitted` 规则和项目构建设置；P11 没有运行编译器，不能声称 kernel 证明了它、拒绝了它、或该命题为假。

这也不触发 P4。P4 所需的是同一规则/输入在明确语义下的可重放实现差异，或校验器接受错误项；一个显式 `Admitted` 依赖既不是隐藏的 `U_bare→Done_s`，也不是此类实现反例。它应保留为 future trust-boundary evidence，而非 HoTT 缺陷结论。

## 4. 与既有资产的关系

- C-304 的 Cubical S¹ encode/decode 是 `PARTIAL_REUSE`：同样涉及 base/loop，却不覆盖 Coq-HoTT 的 Coeq 定义、版本或 Torus caller。
- P8/P9 是 directed/simplicial 的显式结构防御；P11 提供不同 proof assistant/library 的非定向对照。
- `N∞` 一点评紧化是 `NEARBY_NOT_SAME_TASK`，不能替代本分母或原 `C,p,M,N,e`。
- 原 `Done_weak` 的一点评紧化正控制与本 synthetic Circle 的构造都不能自动给出用户的来源—过程 `Done_strong`。

## 5. 波次定位与后继

1. **最终目标连接：** P11 直接测试 P3 的“端点粘合是否被实际 HoTT consumer 越级为原完成”的链边。
2. **全局坐标：** P10 选择非定向 source；P11 以 P7 五项准入关闭其五文件分母；P4 保持未触发。
3. **实际价值：** 新增了一个不同 proof assistant/library 的明确 glue/coherence defense，并定位一个可见 `Admitted` 信任边界，二者均不能被误写为原圆环 K。
4. **为什么停止本分母：** 五项准入中 `K-input`、`K-claim`、`K-forgetting` 已由直接 source facts否定；扩大至整个 Coq-HoTT 或重复更多 Circle callers会改变范围但不会检验新的机制。
5. **后继：** active goal 仍未完成，故下一步只能是 `P12-THIRD-SUCCESSOR-DISCOVERY-001`：重新比较未审规则、非 Circle/Coeq 实际消费者、独立更强 R/Done、理论—实现语义差异。P11 不自动指定 P13。

## 6. 禁止外推

- 未证明 Coq-HoTT 一致、已构建、完全无漏洞或完全没有 K；
- 未证明 Circle 的 coequalizer 定义等同于点集圆的删点/复原；
- 未证明 `Admitted` 命题错误、可导出矛盾或构成校验器错误；
- 未发现 HoTT 的内部矛盾、数学现实的失配证明或可公开的 HoTT 缺陷结论。
