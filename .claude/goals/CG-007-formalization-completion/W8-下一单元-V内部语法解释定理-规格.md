# W8 下一单元：V 内部的语法解释定理（← 方向的精确任务规格）

> 状态：`LAYER1_DONE_LAYER2_STARTED`。2026-10-10 由 WorkBuddy 会话（Agent 模式）写下，同日晚按用户"开始"执行了开工探针。
> 本文件规定"要证什么、缺什么、按什么顺序做"。**第 1 层已确认无需新做；第 2 层已开工并定位到第一个必做子任务。**
> 依据：`形式化追踪/01-有哥德尔路线/02-Z0-条件形式与剩余三步.md` 的末两节、`HoTT/formal/claude-cg001/godel-q-zfc-z0-full/CLAIM.md` §4/§8。

## 1. 要证的命题

唯一目标（三者等价，任选其一作为入口）：

```lean
-- (a) 缺口本身
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V)

-- (b) C-128 的 bridge（(a) 由它 + sigma_one_complete 得到）
--     ∀ V σ, Σ1 σ → Provable 𝗜𝚺₁ ⌜σ⌝ → Provable 𝗭𝗙𝗖 ⌜σᵗ⌝

-- (c) keyE 的 ← 方向
--     𝗜𝚺₁ ⊢ provabilityPred Sh.craig σ 🡒 zfcTr σ
```

**(c) 是最容易陈述、也最容易卡住的**：它是"V 内部的语法解释定理"。

## 2. 为什么它绕不开（已核实的障碍）

| 现成工具 | 为什么不够 |
|---|---|
| `DirectInterpretation.of_provability`（`LK/Interpretation.lean:443`） | 经 `Theory.Proof.complete_on_eq_models` —— **完备性定理，语义**；不产生非标准 V 里的证明编码 |
| `WeakerThan.pbl` | 元层；搬不进非标准 V |
| `Derivable.of_ss`（`Syntax/Proof/Basic.lean:841`） | **只在同一语言内**弱化（`T.Δ₁Class ⊆ U.Δ₁Class`），ℒₒᵣ → ℒₛₜ 跨不过去 |
| `Derivation.sound`（`Syntax/Proof/Coding.lean:336`） | **只对 `d : ℕ`（标准）**成立；V 内部的 d 可能非标准 |
| `T.standardProvability.HBL3` | 只对 `ArithmeticTheory` + `𝗣𝗔⁻ ⪯ T`；`𝗭𝗙𝗖` 不是算术理论 |

## 3. 缺的零件（按依赖顺序）

**第 1 层：`arithTrln.translate` 的语法交换律 —— ✅ 已确认无需新做（2026-10-10 开工探针实测）**

- `arithTrln.translate` 是 `→ˡᶜ`（`LogicalConnective.Hom`），所以 `⊤/⊥/⋏/⋎/∼/🡒` 的交换律**自动具备**
  （`rfl` / `simp` 直接通过）。
- 更重要的：**内部化**版本 `iT` 已经由项目自己的 `GodelQ/ZFC/InternalTranslate.lean` 做好，包含
  `iT_rel` / `iT_nrel` / `iT_verum` / `iT_falsum` / `iT_and` / `iT_or` / `iT_all` / `iT_exs`，
  以及正确性定理 `iT_quote : iT (n:V) ⌜φ⌝ = ⌜arithTrln.translate φ⌝`（对每个 `φ : Semisentence ℒₒᵣ n`）。
- 第 2 层要用的"翻译沿公式结构"的地基因此**已经有了**，不必重写。

**第 2 层：V 内部的推导翻译 —— 已开工，第一个必做子任务已定位**

**不要显式构造"翻译推导"的函数。** 用 `Derivation Sh.craig` 的**归纳**，结论写成
`∀ s, Derivable Sh.craig s → Derivable 𝗭𝗙𝗖 (sᵗ)`，逐规则消。归纳原理已确认可用：

```lean
Fixpoint.Construction.induction (c := construction T) [StrongFinite V c]
  (hP : {Γ := Γ.coe, rank := 1}-Predicate P)              -- P 必须是 Σ1 谓词
  (hstep : ∀ C, (∀ x ∈ C, c.Fixpoint v x ∧ P x) → ∀ x, c.Φ v C x → P x)
  : ∀ x, c.Fixpoint v x → P x
```

**V 内部推导只有 10 条规则**（`Bootstrapping/Syntax/Proof/Basic.lean:412` 的 `blueprint`，
全部是 `{Γ := 𝚺, rank := 0}`）：

| # | 规则图 | 形状 | 翻译支的要点 |
|---|---|---|---|
| 1 | `axLGraph` | `p ∈ s ∧ ∼p ∈ s` | 直接翻译（`translate` 保持 `∼`） |
| 2 | `verumIntroGraph` | `⊤ ∈ s` | 直接翻译（`translate ⊤ = ⊤`） |
| 3 | `andIntroGraph` | `⊢ p,s` 与 `⊢ q,s` ⟹ `⊢ p⋏q,s` | 直接翻译（保持 `⋏`） |
| 4 | `orIntroGraph` | `⊢ p,q,s` ⟹ `⊢ p⋎q,s` | 直接翻译（保持 `⋎`） |
| 5 | `allIntroGraph` | `⊢ free p, setShift s` ⟹ `⊢ s`（`^∀p ∈ s`） | **需处理相对化**：`translate(^∀p) = ∀(D → pᵗ)`，故要先由 `⊢ pᵗ(a)` 得 `⊢ D(a) → pᵗ(a)`，再一般化；本征变量/新鲜性条件要单独证 |
| 6 | `exsIntroGraph` | `⊢ p[t], s` ⟹ `⊢ ^∃p, s` | **需处理项代入**：`translate(p[t])` 与 `translate(p)[?]` 的关系要单独证 |
| 7 | `wkRuleGraph` | `⊢ s'` ⟹ `⊢ s`（`s' ⊆ s`） | 需 `s'ᵗ ⊆ sᵗ`（集合翻译的单调性） |
| 8 | `shiftRuleGraph` | `setShift s = s` ⟹ `⊢ s` | 需翻译与 `setShift` 相容 |
| 9 | `cutRuleGraph` | `⊢ p,s` 与 `⊢ ∼p,s` ⟹ `⊢ s` | 直接翻译（`cut`） |
| 10 | `axmGraph` | `p ∈ s ∧ p ∈ T` | **唯一用到 𝗭𝗙𝗖 的地方**：由 `mem_craig_codes_iff` 得 `p = ρ.padding k` 且 `reWitness(k, ⌜ρ⌝)`；由 `reWitness_spec` + `Sh.reCh` 语义得 `zfcTr ρ`，即 V 手里**已有** `ρᵗ` 的一条 𝗭𝗙𝗖 推导；再用 `ρ.padding k = ρ ⋏ ⊤^k` 接回来 |

**第一个必做子任务（也是所有支的公共前置）：sequent 翻译 `s ↦ sᵗ`**

**这是本轮新发现的障碍。** sequent **不是树，是"码的指数和"**：
`Sequent.quote Γ = ∑ φ ∈ Γ, Exp.exp ⌜φ⌝`（`Syntax/Proof/Coding.lean:24`），
`bitSubsetDef` 也印证这是位集表示。所以"把 sequent 里每个公式换成它的翻译"**不是逐点操作**，
必须：

1. 给出一个 **Σ1 可定义**的 `translateSeq : V → V`（对 `s` 这个自然数做**强递归**），
   满足 `bitTest (translateSeq s) ⌜φᵗ⌝ ↔ bitTest s ⌜φ⌝`，以及单元素情形 `translateSeq {φ} = {φᵗ}`；
2. 证明它是 Σ1 谓词（`Fixpoint.Construction.induction` 要求 `P` 是 `{Γ := Γ.coe, rank := 1}-Predicate`）。

`translateSeq` 一旦有，`P s := (derivable 𝗭𝗙𝗖).val/[translateSeq s]` 就是 Σ1 谓词，归纳可以开跑。

**第 3 层：组装**

`bridge` / `keyE←` / `zfcTr_D3_internalize`，然后接 `Z0Full.zfc_z0_full_of_D3_internalize`，最后按 `BUILD.md` 出正式收据（`capture_run.py`，含负控制）。

## 4. 已知的"看起来能省但省不掉"的坑

1. **`Sh.reCh` 不是 `trProv`**。实测：`Sh.reCh.val` 展开为 `mkSigma (codeOfREPred (Encodable.encode '' Sh))`，`trProv.val` 展开为 `mkSigma (∃¹ iTDef/[#0,↑0,#1] ⋏ (provable 𝗭𝗙𝗖)/[#0])`。两者**不是**同一个公式（`rfl` 失败），只是内容相同。所以第 2 层 `axm` 那一支要先补一条"`codeOfREPred` 的一般 V 表示引理"（`codeOfREPred_spec` 只在 ℕ 层）。
2. **不能只做 → 方向**。`zfcTr.HBL3` 需要两个方向；只做 → 只能得到 `zfcTr σ → □_{Sh.craig}(zfcTr σ)`，仍差 `□_{Sh.craig}(zfcTr σ) → zfcTr (zfcTr σ)`。
3. **不能把 `𝔅 := 𝗭𝗙𝗖.standardProvability` 搬到 `T₀ = 𝗜𝚺₁`**：`Provability T₀ T` 要求 `T₀ ⪯ T`，而 `⪯` 是同语言关系，`𝗜𝚺₁ ⪯ 𝗭𝗙𝗖` 类型不过。
4. **`Diagonalization 𝗭𝗙𝗖` 这条岔路已看过**：即便有，`𝔅 : Provability 𝗭𝗙𝗖 𝗭𝗙𝗖` 需要一条**集合论语言**的可证性公式，而 Foundation 的 `provabilityPred` 是算术公式（`Semisentence ℒₒᵣ 1`），套不上。

## 5. 环境与迭代

```bash
# 工作副本（不要直接改收据源）
cp -R <repo>/HoTT/formal/claude-cg001/godel-q-zfc-z0-full /tmp/d3build/src/
# 当前宿主不允许嵌套沙箱，用 devbuild.py 的无沙箱变体
python3 -B /tmp/d3build/devbuild_ns.py /tmp/d3build/src/godel-q-zfc-z0-full <模块…>
```
- Lean 4.34.0；Foundation 源码 `/Volumes/D/HoTT-toolchain-cache/foundation-src`（`1fb01b72`）；
  olean 在 `foundation-build-1fb01b72-v4.34.0/`**`lib/lean`**（不是 `.lake/build/lib/lean`）。
- 全链 24 模块冷启动约 60 s，增量几乎瞬时。模块清单见包内 `BUILD.md`。
- 探针文件（`GodelQ/ZFC/Probe*.lean`）**不进收据源**。

## 6. 停止条件

- 若第 1 层做完后第 2 层被证明不可行（例如规则翻译需要 𝗭𝗙𝗖 内的归纳而 𝗜𝚺₁ 供不起），
  照实写明卡点，把最小可续状态留在这个文件里，**不要**为了"完成"收窄命题。
- 无论做到哪一层，`C-120` 的影子形式（`𝗭𝗙𝗖 ⊬ (Sh.craig.consistent)ᵗ`）无条件成立，不受影响。

---

## 6. 追加（2026-10-10 晚，Codex 会话 01a120e6，本机实测）

规格 §1(c) 只列了 `keyE` 的 `←` 方向。补一条**已经免费**的方向，让下一单元的范围更准：

### → 方向已证，无需任何工作

```lean
theorem fwd (τ : ArithmeticSentence) :
    𝗜𝚺₁ ⊢ (↑(zfcTr τ) 🡒 (↑(provabilityPred (Theory.craig Sh) (zfcTr τ)) : Sentence ℒₒᵣ)) :=
  FFL.FirstOrder.Arithmetic.provable_sigma_one_complete (T := Sh.craig) (zfcTr_sigma1 τ)
```

**本机 exit 0，无 `sorry`。** 依据：`zfcTr τ` 是 Σ1 句（`GodelQ.Z0Full.zfcTr_sigma1` 已证），
直接套 Foundation 的 `provable_sigma_one_complete`。这与规格 §2 表中的
`T.standardProvability.HBL3` 无关（那条要 `ArithmeticTheory`），用的是
`Bootstrapping.Arithmetic.provable_sigma_one_complete`（namespace 重开了 `Arithmetic`）。

### 因此 `keyE` 的 `←` 方向单独承担了全部 D3

规格 §4.2「不能只做 → 方向」的判断成立且可以更强：→ 方向**已经是定理**，
所以下一单元从第一天起就只需要攻 `←` 方向，不必在两者间分配。

### 可直接复用的已证零件（都在 `Z0-D3-攻关包-最小完整版/05-源码/Z0D3Skeleton.lean`，本机 exit 0）

| 名字 | 内容 |
|---|---|
| `shCraig_iff` | `Sh.craig ⊢ σ ↔ Sh ⊢ σ`（五行，两个 `inferInstance` 方向） |
| `models_provabilityPred_craig` | `V ⊧ provabilityPred Sh.craig σ ↔ Provable Sh.craig ⌜σ⌝` |
| `step1` | `V ⊧ zfcTr σ ⊢ Provable Sh.craig ⌜zfcTr σ⌝`（一行，`sigma_one_complete (T := Sh.craig)`） |
| `fwd` | 见上 |
| `(Sh.craig : ArithmeticTheory).Δ₁` | `inferInstance`（来自 `Sh.RE`） |
| `(Sh.craig.standardProvability).HBL3` | `inferInstance` |

### 对规格 §3 第 2 层 `axm` 分支的一个补充观察

规格 §4.1 说 `Sh.reCh ≠ trProv`、要先补“`codeOfREPred` 的一般 V 表示引理”。
这个判断正确而且比规格写得更关键：`codeOfREPred_spec` 只在 ℕ 层，
而 `axm` 分支要在 **V 内部** 用它，所以那是一条独立的、可先做可先验的子缺口。
建议把它单列成第 1.5 层，配一个负控制（ℕ 层版本与 V 层版本不能互换）。

## 7. 开工探针（2026-10-10，用户"开始"）

同目录 `W8-开工探针.lean`：本机 Lean 4.34.0 + Foundation `1fb01b72` **编译通过（exit 0）**。
它只做三件事：核对第 1 层已具备、列出 10 条规则图的精确名字与类型、核对归纳原理与 sequent 接口。
**它不是收据源，也不证明任何命题。**

实测确认的接口：

- 10 条规则图全部是 `{Γ := 𝚺, rank := 0}.Semisentence k`（Σ0）：`axLGraph`(3)、`verumIntroGraph`(2)、
  `andIntroGraph`(6)、`orIntroGraph`(5)、`allIntroGraph`(4)、`exsIntroGraph`(5)、`wkRuleGraph`(3)、
  `shiftRuleGraph`(3)、`cutRuleGraph`(5)、`axmGraph`(3)。命名空间是 `FFL.FirstOrder.Arithmetic.Bootstrapping`。
- `insertDef`/`bitSubsetDef`/`fstIdxDef` 是 Σ0；`fstIdx`/`setShift`/`free` 是 V 上的函数。
- `Derivation T : V → Prop` 与 `Derivable T : V → Prop` 都要求 `[T.Δ₁]`（`Sh.craig.Δ₁` 已有）。
- `Fixpoint.Construction.induction` 存在，且要求 `P` 是 `{Γ := Γ.coe, rank := 1}-Predicate`。

## 8. 停止条件（未变）

- 若 `translateSeq` 做出来之后某条规则支被证明不可行（例如第 5/6 支的本征变量或项代入条件在 𝗜𝚺₁ 里供不起），
  照实写明卡点，把最小可续状态留在这个文件里，**不要**为了"完成"收窄命题。
- 无论做到哪一层，`C-120` 的影子形式（`𝗭𝗙𝗖 ⊬ (Sh.craig.consistent)ᵗ`）无条件成立，不受影响。

## 9. 第二层实际进度（2026-10-10，同日晚）

### 9.1 已完成并编译通过

`HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/SeqTranslate.lean`
（**本机 exit 0，无 `sorry`**）：sequent 的翻译 `translateSeq : V → V`，把 sequent 里每个公式码
换成它的翻译码。

**做法照搬 `setShift`**：用 `sigma₁_replacement`，不是原先设想的"对 s 强递归"。

```lean
lemma translateSeq_existsUnique (s : V) :
    ∃! t : V, ∀ y, y ∈ t ↔ ∃ x ∈ s, y = iT (0 : V) x :=
  sigma₁_replacement (by definability) s
noncomputable def translateSeq (s : V) : V := Classical.choose! (translateSeq_existsUnique s)
instance translateSeq.defined : 𝚺ᴬ₁-Function₁[V] translateSeq via translateSeqGraph
```

已证的引理：`mem_translateSeq_iff`、`translateSeq_empty`、`translateSeq_insert`
（`translateSeq (insert x s) = insert (iT 0 x) (translateSeq s)`）、`translateSeq_union`、
`translateSeq_mono`。

**这一步把第 2 层原定的"第一个必做子任务"关掉了。**

### 9.2 另一个关键发现：归纳原理现成

`Foundation/FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:642` 的
`Derivation.induction1` **把 10 条规则支逐条列成了假设**：

```lean
lemma induction1 (Γ : Polarity) {P : V → Prop} (hP : Γᴬ_[1]-Predicate P) {d}
    (hd : Derivation T d)
    (hAxL : ∀ s, IsFormulaSet L s → ∀ p ∈ s, neg L p ∈ s → P (axL s p))
    (hVerumIntro : ∀ s, IsFormulaSet L s → ^⊤ ∈ s → P (verumIntro s))
    (hAnd : ...) (hOr : ...) (hAll : ...) (hExs : ...)
    (hWk : ...) (hShift : ...) (hCut : ...)
    (hRoot : ∀ s, IsFormulaSet L s → ∀ p ∈ s, p ∈ T.Δ₁Class → P (axm s p)) : P d
```

所以第 2 层**完全落在"填 10 个 case"上**，归纳谓词取
`P d := Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`（Σ1，`by definability` 可过）。

### 9.3 还缺什么（精确清单，按依赖顺序）

**没有一条已证；`derivable_translateSeq` 尚未证明。**

| # | 缺的引理 | 形状 | 备注 |
|---|---|---|---|
| 1 | **公式保持** | `IsSemiformula ℒₒᵣ n p → IsSemiformula ℒₛₑₜ n (iT n p)` | 每个 case 都要用（`Derivation.*` 构造子都要求 `IsFormulaSet`）。`InternalTranslate.lean` 里**没有**。可用 `UformulaRec1.Construction.semiformula_result_induction`（`Formula/Basic.lean:1578`）证；该原理覆盖 rel/nrel/verum/falsum/and/or/all/exs，**不含 neg/imp**（它们是从核心连接词派生的） |
| 2 | `iT_neg` / `iT_imp` | `iT n (neg p) = neg (iT n p)` 等 | `axL`/`cut` 支要用；`InternalTranslate.lean` 里没有 |
| 3 | `iT` 与 `shift` 的相容 | `iT n (shift p)` 与 `shift (iT n p)` 的关系 | `all`/`shift` 支要用。注意翻译会改变 de Bruijn 结构（每个量词多引入一个约束变量），不是平凡交换 |
| 4 | `iT` 与 `substs1` 的相容 | `iT (substs1 t p)` 与 `substs1 (iT t) (iT p)` | `exs` 支要用 |
| 5 | `iT` 与 `free` 的相容 | `(free p)ᵗ` 与 `free (pᵗ)` | `all` 支要用 |
| 6 | **`axm` 支** | `derivable_translateSeq_of_axm` | 唯一用到 𝗭𝗙𝗖 的地方。需要 `codeOfREPred` 的**一般 V 表示引理**（`codeOfREPred_spec` 只在 ℕ 层）；拿到后由 `mem_craig_codes_iff` + `reWitness_spec` 得 `zfcTr ρ`，即 V 手里已有的 `ρᵗ` 的 ZFC 推导 |
| 7 | 10 个 case 的组装 | `derivable_translateSeq` | 依赖 1–6 |

第 1 条是最关键的瓶颈：**它一过，`axL`/`verumIntro`/`wk` 三支应当直接可做**。

## 10. 第 1 条（公式保持）的进一步拆解（2026-10-10 晚）

`iT.construction`（`InternalTranslate.lean:231`）的输出形状已核清：

```lean
rel n k R v := iTR n k R v
nrel n k R v := neg ℒₛₑₜ (iTR n k R v)
verum _ := ^⊤          falsum _ := ^⊥
and _ _ _ y₁ y₂ := y₁ ^⋏ y₂          or _ _ _ y₁ y₂ := y₁ ^⋎ y₂
all _ _ ys := ^∀ (imp ℒₛₑₜ domZero ys.[0])
exs _ _ ys := ^∃ (domZero ^⋏ ys.[0])
```

所以用 `UformulaRec1.Construction.semiformula_result_induction` 证
`IsSemiformula ℒₒᵣ n p → IsSemiformula ℒₛₑₜ n (iT n p)` 时，**八个支里六个是直接的**：

| 支 | 目标 | 现成引理 |
|---|---|---|
| `verum` / `falsum` | `IsSemiformula ℒₛₑₜ n ^⊤` / `^⊥` | `IsSemiformula.verum` / `.falsum` ✅ |
| `and` / `or` | `IsSemiformula ℒₛₑₜ n (y₁ ^⋏ y₂)` 等 | `IsSemiformula.and` / `.or`（`↔`）✅ |
| `all` / `exs` | `IsSemiformula ℒₛₑₜ n (^∀ (imp domZero y))` 等 | `IsSemiformula.all` / `.exs` + `imp` 的公式性 ⚠️ |
| **`rel` / `nrel`** | `IsSemiformula ℒₛₑₜ n (iTR n k R v)` | **要新拆**，见下 |

`iTR` 的定义（`InternalTranslate.lean:198`）：

```lean
iTR n _k R v := qqAlls (imp ℒₛₑₜ (conjunct 2 n 0 (iVE n v.[0]) ^⋏ (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤))
                            (subst ℒₛₑₜ ?[^#0, ^#1] (cRel R))) 2
```

所以要证 `IsSemiformula ℒₛₑₜ n (iTR n 2 R v)`，还要再补四件：

1. `iVE` 的公式性：`IsUTerm ℒₒᵣ n t → IsSemiformula ℒₛₑₜ n (iVE n t)`；
2. `conjunct` 的公式性；
3. `cRel R` 的公式性（`IsRel 2 R → IsSemiformula ℒₛₑₜ n (cRel R)`）；
4. `subst ℒₛₑₜ ?[^#0,^#1]` 的公式性（Foundation 应有 `IsSemiformula.subst`-类引理，未核）。

**结论**：第 1 条不是一条引理，而是**约 6 条**（8 个支 − 4 个直接可用的），其中 `rel` 支再拆成 4 条。
这是第二层最厚的一块地基；做完它，`axL`/`verumIntro`/`wk` 三支才能开动。

## 10. 第 1 条（公式保持）的进一步拆解（2026-10-10 晚）

`iT.construction`（`InternalTranslate.lean:231`）的输出形状已核清：

```lean
rel n k R v := iTR n k R v
nrel n k R v := neg ℒₛₑₜ (iTR n k R v)
verum _ := ^⊤          falsum _ := ^⊥
and _ _ _ y₁ y₂ := y₁ ^⋏ y₂          or _ _ _ y₁ y₂ := y₁ ^⋎ y₂
all _ _ ys := ^∀ (imp ℒₛₑₜ domZero ys.[0])
exs _ _ ys := ^∃ (domZero ^⋏ ys.[0])
```

所以用 `UformulaRec1.Construction.semiformula_result_induction` 证
`IsSemiformula ℒₒᵣ n p → IsSemiformula ℒₛₑₜ n (iT n p)` 时，**八个支里六个是直接的**：

| 支 | 目标 | 现成引理 |
|---|---|---|
| `verum` / `falsum` | `IsSemiformula ℒₛₑₜ n ^⊤` / `^⊥` | `IsSemiformula.verum` / `.falsum` ✅ |
| `and` / `or` | `IsSemiformula ℒₛₑₜ n (y₁ ^⋏ y₂)` 等 | `IsSemiformula.and` / `.or`（`↔`）✅ |
| `all` / `exs` | `IsSemiformula ℒₛₑₜ n (^∀ (imp domZero y))` 等 | `IsSemiformula.all` / `.exs` + `imp` 的公式性 ⚠️ |
| **`rel` / `nrel`** | `IsSemiformula ℒₛₑₜ n (iTR n k R v)` | **要新拆**，见下 |

`iTR` 的定义（`InternalTranslate.lean:198`）：

```lean
iTR n _k R v := qqAlls (imp ℒₛₑₜ (conjunct 2 n 0 (iVE n v.[0]) ^⋏ (conjunct 2 n 1 (iVE n v.[1]) ^⋏ ^⊤))
                            (subst ℒₛₑₜ ?[^#0, ^#1] (cRel R))) 2
```

所以要证 `IsSemiformula ℒₛₑₜ n (iTR n 2 R v)`，还要再补四件：

1. `iVE` 的公式性：`IsUTerm ℒₒᵣ n t → IsSemiformula ℒₛₑₜ n (iVE n t)`；
2. `conjunct` 的公式性；
3. `cRel R` 的公式性（`IsRel 2 R → IsSemiformula ℒₛₑₜ n (cRel R)`）；
4. `subst ℒₛₑₜ ?[^#0,^#1]` 的公式性（Foundation 应有 `IsSemiformula.subst`-类引理，未核）。

**结论**：第 1 条不是一条引理，而是**约 6 条**（8 个支 − 4 个直接可用的），其中 `rel` 支再拆成 4 条。
这是第二层最厚的一块地基；做完它，`axL`/`verumIntro`/`wk` 三支才能开动。

### 10.1 复核：第 10 节里两条其实已有现成引理（2026-10-10 晚）

本机 `#check` 实测：

- `IsSemiformula.imp`（`↔` 形式）✅ —— `all`/`exs` 支不需要新引理；
- `IsSemiformula.neg`（`→` 形式）✅ —— `nrel` 支不需要新引理；
- `IsSemiformula.subst : IsSemiformula L n p → IsSemitermVec L n m w → IsSemiformula L m (subst L w p)` ✅
  —— 第 10 节的第 4 条（`subst` 的公式性）**已有**；
- `IsSemiformula.isUFormula` ✅

**因此第 1 条实际只需新证 3 条**：

1. `IsUTerm ℒₒᵣ n t → IsSemiformula ℒₛₑₜ n (iVE n t)`（`iVE` 的公式性）；
2. `conjunct` 的公式性；
3. `IsRel 2 R → IsSemiformula ℒₛₑₜ n (cRel R)`（`cRel` 的公式性）。

`IsSemiformula.substs` / `.bShift` / `.isUTerm` 未在 `IsSemiformula` 命名空间下找到（可能名字不同），
第 5 节里 `iT` 与 `substs1`/`shift`/`free` 的相容仍待核。

### 10.1 复核：第 10 节里两条其实已有现成引理（2026-10-10 晚）

本机 `#check` 实测：

- `IsSemiformula.imp`（`↔` 形式）✅ —— `all`/`exs` 支不需要新引理；
- `IsSemiformula.neg`（`→` 形式）✅ —— `nrel` 支不需要新引理；
- `IsSemiformula.subst : IsSemiformula L n p → IsSemitermVec L n m w → IsSemiformula L m (subst L w p)` ✅
  —— 第 10 节的第 4 条（`subst` 的公式性）**已有**；
- `IsSemiformula.isUFormula` ✅

**因此第 1 条实际只需新证 3 条**：

1. `IsUTerm ℒₒᵣ n t → IsSemiformula ℒₛₑₜ n (iVE n t)`（`iVE` 的公式性）；
2. `conjunct` 的公式性；
3. `IsRel 2 R → IsSemiformula ℒₛₑₜ n (cRel R)`（`cRel` 的公式性）。

`IsSemiformula.substs` / `.bShift` / `.isUTerm` 未在 `IsSemiformula` 命名空间下找到（可能名字不同），
第 5 节里 `iT` 与 `substs1`/`shift`/`free` 的相容仍待核。

## 11. 第二层（三）：三条新引理已证（2026-10-10 晚，提交见下）

新增 `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/SeqTranslateFormula.lean`
（**本机 exit 0，无 `sorry`**）：

| 引理 | 内容 | 状态 |
|---|---|---|
| `isSemiformula_cRel` | `IsSemiformula ℒₛₑₜ 2 (cRel R)` | ✅ 已证 |
| `isSemiformula_cDomN` | `IsSemiformula ℒₛₑₜ 1 (↑cDomN : V)` | ✅ 已证 |
| `isSemiformula_cFunc_zero` | `IsSemiformula ℒₛₑₜ 1 (cFunc 0 0)` | ✅ 已证（2 元情形同法） |

**关键机制**（这是第 10.1 节三条为什么之前看着难的答案）：
`cRelN`/`cDomN`/`cFuncN` 全都定义成 **ℕ 层**的引号（`⌜φ⌝ : ℕ`），而
`Sentence.quote_isSemiformula` 说的是 **V 层**的引号（`⌜φ⌝ : V`）。桥接引理是

```lean
Sentence.coe_quote_eq_quote (σ : Semisentence L n) : (↑(⌜σ⌝ : ℕ) : V) = ⌜σ⌝   -- Formula/Coding.lean:440
```

搬过去之后 `Sentence.quote_isSemiformula` 直接可用。

**仍未做**：`conjunct` 的公式性、`iVE` 的公式性（`iVE.blueprint` 三支：`bvar`/`fvar`/`func`，
后两支再分 `ve0`/`ve2`）、`iTR` 的公式性、以及第 1 条公式保持性本身。第 5 节那批
（`iT` 与 `substs1`/`shift`/`free` 的相容）仍待核。

### 11.1 又两条已证（同文件）

| 引理 | 内容 | 状态 |
|---|---|---|
| `isSemitermVec_shiftVec` | `IsSemitermVec ℒₛₑₜ (n:V) (b + n) (shiftVec b n)`（对 `n : ℕ` 归纳） | ✅ 已证 |
| `isSemitermVec_single_bvar` | `i < n → IsSemitermVec ℒₛₑₜ 1 n ?[^#i]` | ✅ 已证 |

用的现成件：`IsSemitermVec.cons_iff`、`IsSemitermVec.singleton`、`IsSemitermVec.termBShiftVec`、
`IsSemiterm.bvar`、`shiftVec_succ`，以及 **`lt_add_self_add_one (a b : V) : a < b + a + 1`**
（`PeanoMinus.lean:14`，`omega` 在 𝗜𝚺₁ 模型上不работает，要用它）。

`shiftVec` 的层级已核实：`shiftVec b n = [^#b, …, ^#(b+n-1)]`，故 `conjunct b n i y` 的层级是 `b + n`
（这与 `iTR` 里 `conjunct 2 n 0 y` 出现在 `qqAlls … 2` 体内、层级 `n+2` 相符）。

**下一步**：`isSemiformula_conjunct`（用 `IsSemiformula.subst` 两次 + `IsSemiformula.and`，
向量 `^#i ∷ shiftVec b n` 由 `cons_iff` 拼），然后 `iVE` 三支、`iTR`、公式保持性。

### 11.2 `shiftVec` 引理升级到 `n : V`：卡在 Σ1 谓词义务（2026-10-10 晚）

`conjunct` 的 `n` 是**任意 V 元素**（`iTR` 里是层数参数），所以第 11.1 节的 `n : ℕ` 版本不够。
V 上的归纳原理找到了：

```lean
ISigma1.sigma1_succ_induction : ({Γ := 𝚺, rank := 1}-Predicate P) → P 0 → (∀ x, P x → P (x+1)) → ∀ x, P x
```

（注意它要求 `V↓[ℒₒᵣ] ⊧* 𝗜𝚺⁺₁`，不是 `𝗜𝚺₁`。）

**两个卡点**：

1. **`definability` 处理不了部分应用**。第一个义务是
   `{Γ := 𝚺, rank := 1}-Predicate fun n => IsSemitermVec ℒₛₑₜ n (b + n) (shiftVec b n)`，
   它内部要证 `{Γ := 𝚺, rank := 1}.DefinableFunction fun v => shiftVec b (v 78)`
   —— 即 `shiftVec` 固定第一个参数后的 1 元版本。`shiftVec_defined` 是 `𝚺ᴬ₁-Function₂`，
   `definability` 没有把部分应用拼出来（`aesop` 到深度上限）。
   **出路**：手写这个 Σ1 谓词实例——用 `IsSemitermVec.definable' 𝚺 0 : 𝚺ᴬ_[1]-Relation₃`
   与 `shiftVec_defined` 的复合，或给 `definability` 一个局部 `have`。
2. **心跳**：直接 `definability` 会在 `whnf` 上超时（默认 200000）；需要 `set_option maxHeartbeats`。

`conjunct` 的公式性（`isSemiformula_conjunct`）在此之后即可拼装：
`IsSemiformula.subst` 两次（向量分别是 `?[^#i]` 与 `^#i ∷ shiftVec b n`）+ `IsSemiformula.and`。
