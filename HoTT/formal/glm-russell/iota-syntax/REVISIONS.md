# iota-syntax 包修订记录

> 本包的 `CLAIM.md` 与三个 `.agda` 源文件已进入运行收据（`20260926-GLM-IOTA-SYNTAX-01/-NEG-01` 的 source-manifest 哈希），按项目规则不改已收据文件；范围的修订与后续尝试写在这里。

## 2026-09-26：GR-1a 审计回函的处置与 C01 第一次补完尝试（会话 S-GOV-20260926-GLM-WORKSPACE-01）

同行评审（`GLM-5.3-Flash/审计回应/20260926-GR1a同行评审-回应.md`）对 Q3 给出 C01 的补完路线（建议级）。处置与尝试记录：

1. **路线的两个前提已机器核实**：
   - `cong f refl ≡ refl` 是**定义性**的（独立小实验 `/tmp/DeflTest.agda` 通过：`test1 f x = refl` 编译过）——因此 q 的一般子句 `cong (λ x → cond x v w) (q u) ∙ step (val u) v w` 在头为字面量时，前缀定义性地成为 `refl`。
   - `lUnit : (p : x ≡ y) → p ≡ refl ∙ p`（GroupoidLaws）方向恰好提供 `refl ∙ X` 的墙；`isSetRetract val lit (λ t → sym (q t)) isSetBool` 收尾可用（签名已核）。
2. **第一次实现（hcomp + lUnit 墙 + squareLeft 基）编译失败**，错误定位在墙系统的**角落相容性**：`(i=i0, j=i1)` 角上 `lUnit X j k` 的 k-变化与 `j=i1` 墙的常值冲突；`(i=i0, j=i0)`、`(i=i1, j=i1)` 两角同样冲突（后者还涉及抽象 `q t` 在 `i1` 处不归约）。结论：所需不是"一步粘贴"，而是一个完整的**单位-结合三维填充子**（关联 `refl ∙ (p ∙ r)` 与 `p ∙ r` 两个复合的呈现）。候选工具：`compPath-unique`（Prelude 147 行：任意两个带填充子的复合相等）、`doubleCompPath-filler`、或手写三立方。
3. **按证据纪律回退**：尝试代码已从源文件移除，`RealisticIotaSyntax.agda` 恢复到收据版本（sha256 `d3ecaf91…` 与 run-01 source-manifest 一致），保证精确重放完整性。C01 保持开放，阻塞点由"边界相干方块"细化为"单位-结合三立方填充子的角落相容呈现"。
4. **范围修订（采纳评审 Q2/Q4/§3）**，因 CLAIM.md 已入哈希，记录于此：
   - CLAIM"这对 GR-1 意味着什么"第 2 条与审计请求 §4.2 的"无论 C01 结果如何"表述**作废**，以 CLAIM"禁止外推"第一条的弱表述为准；载荷理由由"成员是有限树"更换为**"终止且无回路的地面重写系统（β 路径沿规模严格下降、无闭合回路），其词项模型即正则形集合（本片段为 Bool）"**（评审 Q2，更强）；"有限树"本身挡不住悬挂式构造子。
   - art（环点 loop）与 swap（开路径）的类比补半句：两者都注入非平凡认同、对证明无影响，但形状不同（评审 §3）。
   - 真实等式判据并立操作化版本：**可定向为终止且局部合流的地面重写系统**（评审 Q1a）；本片段两条判据一致，swap/art 在两条下都判人工。
   - 查重邻接：C-67 CLAIM"差量"一节登记的 S07/E14 覆盖格（当时 UNREVIEWED）是本包真正的邻接风险，留给后续核对。
5. **未做**：C01 第二次尝试（compPath-unique 路线）；版本闭合（本地提交待用户授权，push 另需授权）。

## 2026-09-26（续）：C01 第二次尝试的侦察结论（用户授权本地提交后，同会话）

用户授权本地提交（`80ea8181`/`c0e220e5`）并确认执行序与评审一致（GR-1b 先于 M1）。据此对 Q3 路线做第二次有界侦察：

1. **`compPath-unique` 签名已核**（Prelude 147）：`(p q r) (α β : Σ[ s ∈ x ≡ w ] PathP (λ j → p (~ j) ≡ r j) q s) → α ≡ β`——其 Σ 填充子族 `λ j → p (~ j) ≡ r j` 正是所需方块（左因子反区间族）的库内亲属；`doubleCompPath≡compPath`（217 行）给出 `refl ∙∙ p ∙∙ r ≡ refl ∙ (p ∙ r)`，即单位-结合路径 E 的库内来源。
2. **两种实例化均未闭合**：(a) (p, r, refl{z}) 实例化——我持有的 `squareLeft` 恰为其 Σ 元素的填充子（反区间后逐字匹配），但第二个 Σ 元素（边为 `refl ∙ (p ∙ r)` 的填充子）仍需构造，循环未破；(b) (refl, p∙r, refl) 实例化——填充子族退化为常值族，得到的是 2-路径等式而非 over-p 的方块。
3. **核心困难定位**：HIT 边界检查要求子句面的**定义性**匹配；一切通过 `subst`/`compPath-unique` 传递的构造在 i=0 面上留下不归约的传输项。真正需要的是一次性给出左边缘定义性等于 elaborated `refl ∙ (p∙r)` 的三立方（或改写子句消除前缀——被覆盖子句的边界一致性阻断）。
4. **候选工具余量**（供后继会话）：`compPathP`（Prelude 226，异质 PathP 组合子，签名已见首行未展开）；`compPath-unique` 的直接 hfill 内联改写；Raw-树商路线（评审的备选，其 r∘q/id 方向亦有坑，见本会话分析）。
5. **处置**：C01 保持开放；本会话上下文不足以完成三立方工程，建议在 fresh 会话（全上下文预算）中专门执行，或先做 M1（评审 Q6 的第二项，不依赖 C01）。源文件未动（仍为收据哈希版本）。

## 2026-09-26（再续）：C01 第三次尝试落地（同会话，用户指示继续）

**结果：`RealisticIotaSyntaxSet.agda` 编译通过，`realisticIotaSyntaxIsASet : isSet Tm` 机器证明成立**（GLM-R1-C01 升级为 `KERNEL_ACCEPTED_WITH_SCOPE`，运行 `20260926-GLM-IOTA-SYNTAX-02`，exit 0，19.3s，stderr 0 B，proof id `MP-GLM-RUSSELL-IOTA-002`）。

**第三次尝试的构造（供后继引用）**：前两次失败的根因——`_∙_` 的定义自带隐藏 `refl` 前缀（`p ∙ q := refl ∙∙ p ∙∙ q`），cond 子句再用 `_∙_` 造成双重前缀，`refl ∙ X` 在 hcomp 角落不归约。修正：cond 子句改用**显式三段复合** `_∙∙_`——`cong (λ x → cond x v w) (q u) ∙∙ unlift (val u) v w ∙∙ liftq (val u) v w`，其中 `unlift true v w = betaT v w`、`liftq true v w = q v`。字面量头时 cong 前缀定义性归约为 `refl`（`cong f refl ≡ refl`，已机器实验证实），于是子句值定义性地等于 `refl ∙∙ betaT t s ∙∙ q t`——恰是 `betaT t s ∙ q t`（`_∙_` 的展开式），即已证 `squareLeft` 的左边缘。路径构造子子句直接 `squareLeft (betaT t s) (q t)`，收尾 `isSetRetract val lit (λ t → sym (q t)) isSetBool`。**不需要 lUnit 粘贴，不需要三立方**——评审 Q3 的"差一步粘贴"判断在此意义上正确：差的那一步是改复合的呈现方式，不是构造新方块。

**范围与移交**：C01 仅覆盖本一阶 ι 片段（完整 β 需替换装置，未触碰）。**对 C-67(a) 读法的含义**（评审 Q4.1 预登记）：本片段内"真实等式语法是集合"已机器成立，故 C-67(a) 的 `syntax∞IsNotASet` 之非集合性在本片段对应物上完全来自 swap 式注入。是否据此修订 Opus 的 C-67(a) 表述，须经用户转 Opus 走其 REVISIONS 流程（rulings 34：GLM 不写 `.claude/`）。

## 2026-09-27：Cloud-Opus 审计修订（审计者写入；不改上文任何一句）

> 依据：委托工作单 `GLM-5.3-Flash/审计请求/20260927-委托工作单-审计修正补完交付最终卷宗.md` §3（R4、R5、R1）与 §6 写入权限。审计全文：`Cloud-Opus审计并补完GLM/02-断裂审计-逐命题（D1）.md` §2.1–2.3、`05-R2至R8处置.md` R4。三个定理的形式层都被内核接受（Linux 复现 `20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-01/-02/-NEG-01`）；断裂在声明层与控制层。

1. **GLM-R1-C02：见证不陈述所声称的事实（实质性越界）。** CLAIM L15/L20 说"`val` 的两个 βι 子句逐字是 `refl`……`valReflT`/`valReflF` 见证"。但见证的类型是
   `valReflT : (t s : Tm) → Path (Path Bool (val (cond (lit true) t s)) (val t)) refl refl`，
   其中**没有路径构造子 `betaT`**：内层 `refl` 能写出，只说明两端点定义性相等；外层 `refl ≡ refl` 随即恒成立，与 `val` 在 `betaT` 上做了什么无关。机器演示（`HoTT/formal/cloud-opus-glm-audit/glm-repairs/IotaC02Faithful.agda`，运行 `20260927-COPUS-GLM-REPAIR-01`）：
   - 忠实形式成立：`valBetaT-refl : (t s : Tm) → cong val (betaT t s) ≡ refl`、`valBetaF-refl`（证明为 `refl`；COPUS-GLM-FIX-C02a）；
   - GLM 的陈述形式在**人工等式** `art` 处照样成立：`glmFormHoldsAtArt : Path (Path Type (f boolTy) (f boolTy)) refl refl`；而忠实形式在 `art` 处被驳斥：`faithfulFormFailsAtArt : ¬ (cong f art ≡ refl)`（COPUS-GLM-FIX-C02b）。
   结论：GLM 声称的**事实为真**，但原见证不能区分真实等式与人工等式，因而不能充当"真实等式判据由此机器化"的证据。以后引用 C02 一律用忠实形式 COPUS-GLM-FIX-C02a；`valReflT/F` 只作"端点定义性相等"的记录。

2. **GLM-R1-C03：标题与 L21 的"必须"越界；负控制不检验论证。**
   - 形式内容是一个注入实例：加入一条被解释为 `ua flipNotEquiv` 的人工等式后 `¬ isSet TmA`。"非落定**必须**人工注入"是对一切非落定来源的全称断言，形式内容不支持（CLAIM 自己的"禁止外推"也与标题的"必须"相抵）。改读为："注入一条被解释为非平凡自等价的人工等式，**足以**破坏集合性。"
   - 负控制 `WrongArtIsRefl` 被拒的理由（`art i != boolTy`）是真的，但它只说明 `art` 不**定义性**等于 `refl`，不检验 C03 的论证。补充近失控制 `HoTT/formal/cloud-opus-glm-audit/glm-repairs/IotaC03NegTrivialInterp.agda`：把 `art` 的解释换成常路径（`f' (art i) = Bool`）后，GLM 的证明脚本逐字被拒（`cong f' art` 是 `refl`，不是 `ua flipNotEquiv`；运行 `20260927-COPUS-GLM-REPAIR-NEG-03`）。这说明 C03 依赖人工等式的**非平凡解释**。

3. **GLM-R1-C01：形式无断裂，读法越界。** `realisticIotaSyntaxIsASet : isSet Tm` 成立。但 `Tm` 同构于 `Bool`（`val (lit b)` 定义性等于 `b`，`q : t ≡ lit (val t)` 已在 `RealisticIotaSyntaxSet.agda` 中证明），没有上下文、依赖、替换；GN-002 修订块二"本片段内'理论自身的表述完全落定（集合）'是机器定理"是命名放大。改读为："一个同构于 Bool 的两等式玩具 HIT 语法是集合（机器定理）；它不是'理论自身的表述'。"另注：`Tm` 本身是 HIT（`betaT/betaF` 是路径构造子），HITScan 负证书 `NegCertIota` 如实点名 `Tm`（运行 `20260927-COPUS-HITSCAN-NEG-01`）。

4. **上节（2026-09-26 再续）末段"C-67(a) 的 `syntax∞IsNotASet` 之非集合性在本片段对应物上完全来自 swap 式注入"**：限定在本玩具片段内成立；不能外推为"C-67(a) 的非集合性不是自指的固有代价"。真实类型论完整语法（含替换、β、η）不截断时是否为集合仍开放。对 Opus C-67(a) 读法的修订提案见 `Cloud-Opus审计并补完GLM/09-致Opus差量报告与patch提案（D6）.md` P3（经用户转交，本会话不写 `.claude/`）。

5. **收据**：GLM 原收据哈希锁定，不改。原 `source-manifest.json` 不是 canonical schema；canonical 形式的 Linux 复现见上列运行，由 `Cloud-Opus审计并补完GLM/tools/verify_copus_run.py --rerun` 逐字节重放核验（结果：`Cloud-Opus审计并补完GLM/11-收据核验结果.json`）。
