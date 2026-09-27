# groupoid-universe 包修订记录（M1c 探索史与落地）

## 2026-09-27 凌晨：M1c 单元 2+3 落地（GLM-R3-C01 机器证明）

**`¬universeIsGroupoid : ¬ isOfHLevel 3 (Type (ℓ-suc ℓ-zero))` 编译通过**（运行 `20260926-GLM-GROUPOID-UNIVERSE-01` exit 0；负控制 exit 42 按预期拒绝）。

**关键突破（对上节侦察的三案之外的第四条路）**：
1. **边界实验更正了一个整晚的错误假设**：`PathP (λ i → r i ≡ r i) r r` 对抽象 r **完全合式**（cubical 的 PathP 边界检查接受环路端点；此前判"不合式"是错的——这正是库的 `ΣPathP` 能存在的原因）。
2. **自滑动方块的构造**：`D q := compPathL→PathP (纯路径代数 sym q ∙ q ∙ q ≡ q)`——用库的 `PathP→compPath`-族引理（Cubical.Foundations.Path:372），一切命题性，零定义性墙。
3. **KS ξ-族**：`FAM (b , q) := ΣPathP (q , D q)`——每个点自带环路数据成为该点处的环路。
4. **总装**：等值环 `loopE := equivEq (funExt FAML)`；群胚假设经 `univalence` 传递压平它；双层 `cong (cong ·)` 求值/投影到具体点 `(c₀ , τ)`；τ ≠ refl 由 `uaβ` + `a (tt,tt) = (ff,tt)` 的可计算差异给出（负控制正是它）。

**边界声明**：HIT-free 指证明的导入与构造不使用任何 HIT 类型；cubical 库的传递接口图（`--ignore-interfaces` 全量重检时）包含 `Cubical.HITs.*` 模块（如 PropositionalTruncation），属库基础设施，未进入本证明的任何构造。

## 2026-09-26 深夜（会话尾）：单元 2 的路线侦察——三条死路（已被第四条路取代，留档）

1. 死路 A（可判定族）：死于层级混淆（FAM(L): L≡L 是环路不是 L；与熄火定理一致）。
2. 死路 B（sym-映射）：死于"对称群元素恒共轭于其逆"。
3. 死路 C（ξ-族朴素呈现）：当时判为不合式——**此判断已被上述边界实验更正**；真正的问题是"如何构造"，答案见上（compPathL→PathP）。死路 C 的教训保留：KS 依赖的判断性 Ω-律在 cubical 为命题性，所以必须走库的 PathP↔复合引理而非 KS 的定义性链。
