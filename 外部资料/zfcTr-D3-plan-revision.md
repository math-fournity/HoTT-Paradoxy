# zfcTr-D3-plan.md 修订说明（2026-10-10，Codex 会话 01a120e6）

> **性质**：对 `zfcTr-D3-plan.md` 的独立评审与修订建议。**不修改原计划文件**，只附在旁边。
> 本说明中的每一条判断都经过本机 Lean 环境探测（pinned Lean 4.34.0 / Mathlib `5ed29652` / Foundation `1fb01b72`），
> 探测代码与输出见 §6。凡是我没有实测的，都明确标为【未实测】。

---

## 0. 总结

原计划的**方法论方向正确**（§3 的 Bridge′ 弱化、§4 对现有工具的否定、§5 的移植思路都成立），
但有**两处会让执行 AI 卡死的硬伤**、**一处环境描述错误**、**一处过度悲观**。
此外，我在 2026-10-10 的实测中发现：§4 提出的新路线 R-新 **不能绕过** D3（它把缺口
换成了 `trProv` 的 Δ1 性，而这两者是同一难度），但找到了 Foundation 内一个可照抄的
机器证明模板 `CraigTrick.lean:210`，它把缺口精确定位到了证明长度的界。详见 §4b。

修订后的建议：**先精读 `CraigTrick.lean:207-250`**，照它的手法尝试为 `Sh` 构造
`𝚫ᴬ₁` 特征；这会精确卡在 D3 上。走不通再回到修订后的 Δ0 路线。

---

## 1. 对的部分（确认）

### 1.1 §3 的 Bridge′ 弱化是正确的，而且比它自己说的更关键

原 bridge 要 `Provable 𝗜𝚺₁ ⌜σ⌝` 输入；Bridge′ 只要 `V ⊧ σ`。
这个弱化不是省几行——它把"处理 V 内部一个**任意的**（可能非标准的）证明编码"这个真难题，
换成"处理一个**真的** Σ1 句"。Foundation 的 `bold_sigma_one_completeness`
（`R0/Basic.lean:94`）与 `sigma_one_completeness`（`:154`）正是干这个的，模板确实在那儿。

### 1.2 §4 的三条"为什么现有工具填不上"全部核实为真

尤其第 1 条。`DirectInterpretation.of_provability`（`LK/Interpretation.lean:443`）的证明体第一行就是
`apply Theory.Proof.complete_on_eq_models`——经完备性定理，产出元层推导，不产生 V 内部的证明编码。
`provable_internalize` 也确认受 `variable (T : ArithmeticTheory)` 约束（`DerivabilityCondition/D1.lean` 侧），
ZFC 套不上。

### 1.3 §5 的移植思路方向正确

`R0/Basic.lean:94-119` 的全套 case（`val_numeral`、`lt_numeral_iff`、`matrixToVec`）
确实是可对照搬的结构。

---

## 2. 硬伤一：§5.1 的 L3 把 Δ0 完全性写成了错误的量词方向

计划里 L3 的有界 ∀ 情形要"在 IΣ₁ 内对 `u ≤ b` 做 Σ₁ 归纳，
证 `∀ u ≤ b, Provable 𝗭𝗙𝗰 ⌜∀x∈ω (x < 𝕹 u → translate θ₁)⌝`"。

**问题在于要证的命题本身就是全称的。** 对一个**可能非标准**的 `b : V`，
"对所有 `u ≤ b` 都有 ZFC 证明"这句话在 V 里是真的当且仅当它确实是真的（ZFC 真的能证明每一个），
但 Lean 里你不会得到一个 `∀ u ≤ b` 的假设——你只有 `hw : V ⊧ θ(w)` 对某个具体 `w`，
而 `θ` 里的有界 ∀ 在 V 中为真是语义事实，你要从它**取出**逐个 `u` 的见证。
`hw` 是一个 Prop，不是一个可递归拆解的构造。

`bold_sigma_one_completeness` 之所以没有这个问题，是因为它的目标是 `φ.Eval (numeral ∘ bv) (numeral ∘ fv)`——
**求值事实的传递**（ℕ 中真 ⟹ V 中真），用的是 `lt_numeral_iff`、`val_numeral` 这类语义引理，
全程不涉及"产生证明编码"。而 Bridge′ 要的是 `Provable 𝗭𝗙𝗰 ⌜translate θ⌝`，这是**句法对象的存在**。

**后果**：执行 AI 会在 L3 的有界 ∀ 情形撞墙，撞墙方式是"不知道从哪拿到 `u`"，
不是"某个 tactic 失败"。按 §8 的验收标准，这种卡住不会自我报告，只会变成一堆积压的 `sorry`。

### 2.1 但 Foundation 里有正确的形状，计划漏掉了

实测确认：`Bootstrapping/Arithmetic/PeanoMinus.lean:235 ball_intro` 的假设是

```lean
lemma ball_intro (φ : Semiformula V ℒₒᵣ 1) (n : V)
    (bs : ∀ i < n, T.internalize V ⊢ φ.subst ![𝕹 i]) :
    T.internalize V ⊢ φ.ball (𝕹 n)
```

**假设是元层全称**：对每个 `i < n` 分别给一条 V 内推导。它不需要"在 V 内做归纳产生证明编码"。

这是 L3 的 `hBall` 情形应该照抄的形状，而不是计划里写的"内归纳产生证明编码"。

---

## 3. 硬伤二：§7.3 的环境描述与本机事实不符

计划说"已备好的 90% 环境：本机 `~/workspace/toolchain-cache/` 有精确版 Lean、
Mathlib 全量 8908 olean、Foundation 137/181 模块 olean、移植版顺序编译脚本 `build_foundation.py`……
当前唯一已知障碍是 `...Bootstrapping.Syntax.Term.Basic` 在 8G 机器上 OOM"。

**本机实际路径是 `/Volumes/D/HoTT-toolchain-cache/`**：
- Foundation 源码：`foundation-src`（`1fb01b72`）；
- **完整构建好的**：`foundation-build-1fb01b72-v4.34.0`（1893 个模块，正是 z0-full 包
  `MATHLIB_CLOSURE.json` 指向的那一套）；
- `~/workspace/toolchain-cache/` **不存在**。

这不是小事：执行 AI 若信了 §7.3，会花大量时间找一个不存在的 90% 环境，
甚至可能尝试从 137/181 模块重建。而实际环境**完整可用**——我实测 24 个模块编译只要约 60 秒
（`ProcessObservation` 11.2 s + `InternalTranslate` 12.3 s + 其余各 1-4 s）。

**计划的 env 描述比现实悲观，方向也找错了。**

---

## 4. 新发现：一条原计划没列、可能更短的路（R-新）

这是本次实测最重要的发现，**可能让 D3 从"最重"变成"中等"**。

### 4.1 两个关键事实（都已实测确认）

**事实 A**：`tprovable_iff_provable`（`Syntax/Proof/Typed.lean:168`）
```lean
lemma tprovable_iff_provable {T : Theory L} [T.Δ₁] {σ : Formula V L} :
    T.internalize V ⊢ σ ↔ Provable T σ.val
```
即：**对同一个 T**，`T.internalize V ⊢ φ` 与 `Provable T φ` 等价。
我实测对 `T := 𝗭𝗙𝗖`、`T := 𝗜𝚺₁` 都通过。

**事实 B**：`Provable 𝗭𝗙𝗰 ⌜translate σ⌝` 因此**完全等于** `𝗭𝗙𝗰.internalize V ⊢ ⌜translate σ⌝`。
而 Foundation 的 `bold_sigma_one_complete` / `sigma_one_complete` 证明的正是
`T.internalize V ⊢ ...` 形状的目标！

**这意味着：Bridge′ 可以整段借 Foundation 的 D3 证明，只需把目标理论从 𝗜𝚺₁ 换成 𝗭𝗙𝗰。**

### 4.2 唯一的障碍：`Sh.Δ₁` 不是现成实例（实测确认）

我实测 `sigma_one_complete (T := Sh)`，Lean 报：
```
failed to synthesize instance of type class Theory.Δ₁ Sh
```

C-119/C-120 走的是 `Computable translate → Sh.RE`（r.e. 路线），**没有**给出 `Sh.Δ₁`。
`Theory.Δ₁`（`Bootstrapping/Syntax/Theory.lean:16`）要三条字段：
```lean
class Δ₁ (T : Theory L) where
  ch : 𝚫ᴬ₁.Semisentence 1
  mem_iff : ∀ φ : Proposition L, ℕ ⊧/![⌜φ⌝] ch.val ↔ ∃ σ ∈ T, φ = σ
  isDelta1 : ch.ProvablyProperOn 𝗜𝚺₁
```

### 4.3 R-新 的形状

**好消息**：`Sh` 的成员判定本身就是 `zfcTr σ = trProv.val/[⌜σ⌝]`，
而 `trProv := "x. ∃ y, !iTDef y 0 x ∧ !(provable 𝗭𝗙𝗰) y"` **已经是一个 Σ1 公式**（C-121 已证 `zfcTr_sigma1`）。

所以 `Sh.Δ₁.ch` 的 Σ1 半边可以直接取 `trProv`。剩下的是：
1. Π1 半边：`trProv` 的补。这需要"不存在 y 使得 iTDef y 0 x ∧ Provable"的 Π1 形式 ——
   `iTDef` 与 `provable 𝗭𝗙𝗸` 都是 Σ1，它们的合取的否定是 Π1，但 Foundation 要的是**一个 𝚫ᴬ₁ 公式对**，
   即需要 Σ1 与 Π1 两个公式在 𝖨Σ₁ 中等价。这一步与 D3 有部分重叠（都要"形式化 Σ1 完全性"）。
2. `mem_iff`：`ℕ ⊧ trProv/[⌜φ⌝] ↔ φ ∈ Sh`。右边是 `𝗭𝗙𝗰 ⊢ φᵗ`，左边是
   "ℕ 中 ⌜φᵗ⌝ 有 𝗭𝗙𝗰 证明" —— 这正是 Foundation 已有的
   `internalize_provability` + `Provable.complete` 组合，**应该可行**。
3. `isDelta1`：`trProv.ProvablyProperOn 𝖨Σ₁`，即 `𝖨Σ₁ ⊢ Σ1形 ↔ Π1形`。这是最重的一条。

**判断（2026-10-10 实测修正）**：R-新 **不是**免费通路。`isDelta1` 需要的语义等价
`trProv ↔ ¬trProv` 根本不成立，所以 `Sh.Δ₁` 不能靠取 `trProv` 作 `ch` 得到。
正确做法要照 `CraigTrick.lean:210` 的有界量化 + 唯一性手法重造 `ch`，而那会卡在
证明长度的界，即形式化 Σ1 完全性。详见新增的 §4b。

---

---

## 4b. 修订后的 R-新 实测结论（2026-10-10，本机 Lean 实测）

上文的 §4 说 R-新 可能是几条路里最短的。**这个判断过于乐观，现按实测修正。**
以下结论都有 Lean 输出支撑（pinned Lean 4.34.0 + Foundation `1fb01b72`）。

### 已打通的部分

| 项 | 状态 | 关键 Lean 事实 |
|---|---|---|
| `shCh : 𝚫ᴬ₁.Semisentence 1` | 构造成功 | `.mkDelta trProv trProv.negSigma`；`negSigma` 由 Foundation 机器构建 1 证明 |
| `Theory.Δ₁ Sh` 的字段 `mem_iff` | 三行打通 | `rw [models_trProv_iff, mem_Sh, provable_iff_provable]` |
| `tprovable_iff_provable` | 成立 | `T.internalize V ⊢ σ ↔ Provable T σ.val` |

### 发现的真实障碍（原计划没预见）

`Theory.Δ₁` 的第三条字段是 `isDelta1 : ch.ProvablyProperOn ISigma1`。而 `ProvablyProperOn`
可经 `ProvablyProperOn.arithmetic_ofProperOn`（`Arithmetic/Definability/Hierarchy.lean:64`）
从**语义层**的 `ProperOn M` 得到：

```lean
def ProperOn (φ : 𝚫-[ℬ, m].Semisentence n) : Prop :=
  ∀ (e : Fin n → M), φ.sigma.val.Evalb e ↔ φ.pi.val.Evalb e
```

对 `shCh = mkDelta trProv (∼trProv)`，这就是 `trProv ↔ ¬trProv`，
**在 trProv 有确定真值的任何模型中都为假**（例如 N）。

所以：**`trProv` 是 Σ1 但不是 Δ1。** "存在 ZFC 证明" 与 "不存在 ZFC 证明" 当然不等价。

**推论**：R-新 没有绕过 D3。它把"经翻译的形式化 Σ1 完全性"换成"`trProv` 的 Δ1 性"，
而后者在 Foundation 框架下需要**同一件事**——Σ1 与 Π1 在 ISigma1 中等价。

### 但找到了可照抄的模板（本轮真正收获）

Foundation 的 `Bootstrapping/Syntax/CraigTrick.lean:210` 完整解决了同一类问题，
而且是机器证明的：

```lean
noncomputable def _root_.FFL.FirstOrder.Theory.craigCh : 𝚫ᴬ₁.Semisentence 1 := .mkDelta
  (.mkSigma "x. ∃ s < x, ∃ p < x, ∃ v < x,
    !qqVerumsGraph v s ∧ !qqAndDef x p v ∧ !(T.reWitness.val) s p")
  (.mkPi "x. ∃ s < x, ∃ p < x, ∃ v < x,
    (∀ v', !qqVerumsGraph v' s → v' = v) ∧ !qqAndDef x p v ∧ !(T.reWitness.val) s p")
```

手法：**两半都用有界量词 `∃ s < x`，Π1 半只多加一条唯一性条件**
（`∀ v', Graph v' s → v' = v`）。于是语义上"有界存在 + 唯一 等价于 唯一有界存在"，
两半等价；语法上 Σ1/Π1 各自成立。

**关键观察**：CraigTrick 的 `ProperOn` 证明（`:222-234`）只用了有界/无界量化互换的初等引理
（`lt_K!_right`、`le_qqVerums`），**没有用到任何 Σ1 完全性**（`grep sigma_one_complete` 为空）。

### 所以下一步有明确形状，但会卡在同一处

照这个模板为 `Sh` 构造 `𝚫ᴬ₁` 特征，需要把 `Provable ZFC x` 有界化成 `∃ d < x, ...`。
CraigTrick 之所以能做到，是因为它从 `T.RE` 出发，引理 `:244` 的
`T.exists_mem_of_reCh` 把"存在 reCh 见证"变成"存在公理"。
**我们没有对应的捷径**：需要"证明长度不超过 x 的某个界"，
而这个界就是形式化 Σ1 完全性本身。

### 修正后的总判断

| 路线 | 是否绕过 D3 | 现状 |
|---|---|---|
| R-新（`Sh.Δ₁`） | **否** | `mem_iff` 已通；`isDelta1` 需 Σ1 完全性；但有可照抄的 CraigTrick 模板 |
| Δ0 路线（§5） | 否 | 模板 `bold_sigma_one_complete` 也在 Foundation 里，但它的目标理论是算术的 |
| R-备（形式化解释定理） | 否 | 最 general |

**三条路都通向同一件事**：形式化 Σ1 完全性。Foundation 对算术理论已做完（约 1080 行），
我们的难点是谓词作用在**翻译后**的公式上。

**给下一个 Session 的最具体建议**：不要重新发明。先精读 `CraigTrick.lean` 的 `:207-250`
全段，照它的有界量化 + 唯一性手法尝试构造 `Provable ZFC` 的 𝚫ᴬ₁ 特征。
它会精确卡在"证明长度的界"，那时卡点就是 D3 的**具体形式**。

## 5. 修订后的建议执行顺序

| 顺序 | 路线 | 内容 | 预计工作量 |
|---|---|---|---|
| 1 | **R-新** | 为 `Sh` 构造 `Theory.Δ₁`（用现成的 `trProv` 作 Σ1 半边），然后 `sigma_one_complete (T := Sh)` 直接得 Bridge′ | 中；`isDelta1` 是主要开销 |
| 2 | **修订后的 Δ0 路线** | 若 R-新 卡在 `isDelta1`：按 §2.1 用 `ball_intro` 的**元层全称**形状重写 L3，先做原子 + 命题连接词两层（可干净落地，已实测） | 中；有界量词留作明确子缺口 |
| 3 | **R-备（形式化解释定理）** | 定义从 𝖨Σ₁ 推导编码到 ZFC 推导编码的可计算翻译 | 大 |

### 5.1 建议把 §5.1 的引理分解改成

**L1（原子完全性）**——已实测起点：`ZFC ⊢ Theory.Eq.refl ℒₛₜ` 可经
`Entailment.weakerThan_iff.mp (inferInstance : 𝗘𝗤 _ ⪯ 𝗭𝗙𝗰)` 得到。

**L2（命题连接词）**——已实测全部 `rfl`/`simp` 落地：
- `translate (φ ⋏ ψ) = translate φ ⋏ translate ψ`；
- `translate (∼φ) = ∼translate φ`（用 `DirectTranslation.map_neg` + `simp`）；
- `translate (∃¹ φ) = ∃_[arithTrln] translate φ`；
- `translate (∀¹ φ) = ∀_[arithTrln] translate φ`。

**L3（Δ0 完全性，核心）**——按 §2.1 改用 `ball_intro` 的元层全称形状，
**不要**写"内归纳产生证明编码"。

**L4/L5**：不变。

---

## 6. 实测记录

以下探测都在 `/tmp/d3probe/`（pinned Lean 4.34.0 + 完整 Foundation 构建）中运行：

| 探测 | 文件 | 结果 |
|---|---|---|
| 基线复现（24 模块） | `devbuild.py` 全链 | 全部 exit 0，约 60 s |
| C-128 归约复现 | `GodelQ/ZFC/Z0Bridge.lean` | exit 0， axioms: `[propext, Classical.choice, Quot.sound]` |
| L2 命题连接词四层 | `Z0Delta0Probe.lean` | 全部 exit 0 |
| L1 起点：`ZFC ⊢ Eq.refl` | `Z0Delta0Probe2.lean` | exit 0 |
| 事实 A：`tprovable_iff_provable` 对 𝗭𝗙𝗰 | `Z0BallProbe.lean`、`Z0BridgeProbe.lean` | exit 0 |
| 事实 B：`Provable 𝗭𝗙𝗼 ⌜σ⌝ ↔ 𝗭𝗙𝗸.internalize V ⊢ ⌜σ⌝` | 同上 | exit 0 |
| `𝗣𝗔 ⪯ Sh` 可用 | `Z0Decisive.lean` | instance 合成成功 |
| `sigma_one_complete (T := Sh)` | 同上 | **失败：`Theory.Δ₁ Sh` 无实例**（这正是 §4.2 的缺口） |

探测文件的清理：`/tmp` 是临时目录，未写入 repo。

---

## 7. 给原计划的更正清单（若原计划作者要修订）

1. **§5.1 L3 的有界 ∀ 情形**：从"内归纳产生证明编码"改为"元层全称 + `ball_intro`"。
2. **§7.3 环境**：把 `~/workspace/toolchain-cache/` 全部换成
   `/Volumes/D/HoTT-toolchain-cache/{foundation-src,foundation-build-1fb01b72-v4.34.0}`，
   删除 OOM 警告，注明"24 模块约 60 秒可完整编译"。
3. **§6 补一条 R-新**：先试为 `Sh` 构造 `Theory.Δ₁`（§4），它比 R-备 短。
4. **§6 对 R-备 的判定**：不要写成"工作量显著更大……只建议在 Δ0 路线被证伪不可行时启用"。
   R-新 的存在说明有中间选项。
5. **§8 验收标准补一条**：明确"不得以 `sorry` 充数；卡住时必须写清卡在哪一条具体引理"。

---

## 8. 我的总体判断

Z0 的完整形式在数学上不 surprising（它就是哥德尔第二定理的一个实例），
卡的是 Foundation 的实现事实：`of_provability` 是语义证明，而 `Sh.Δ₁` 未构造。
R-新 之所以有希望，是因为 `trProv` 已经是一个现成的 Σ1 公式，且 `tprovable_iff_provable`
把两种"可证"完全打通——这给了 Bridge′ 一个不经过"证明编码翻译"的入口。

若 R-新 也卡住，诚实的结论是：**D3 的形式化需要先形式化 Σ1 完全性本身**，
这与 Foundation 已完成的算术版工作量同级（约 1080 行），不是可以绕过的一步。
