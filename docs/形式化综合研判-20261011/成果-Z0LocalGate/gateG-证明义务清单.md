# gateG 证明义务清单（给下一会话的施工图）

> 2026-10-11，CG-009。目标：`gateG : 𝗜𝚺₁ ⊢ □Craig(zfcTr G) 🡒 zfcTr(zfcTr G)`，
> 其中 `G := gödel zfcTr`、`□Craig σ := provabilityPred Sh.craig σ`。
> 一旦 `gateG` 无 sorry 过核，Z0 完整形式立即成立（`zfc_z0_full_of_reverse_at_godel`，已证）。
>
> **先说边界**（诚实性修正后的准确版本）：门的**陈述**收缩到单句，但**证明义务不因此变小**——
> 仍要消去 `zfcTr G` 的**任意**（可能非标准）推导 d。下表是完整义务分解。

## 义务的展开（从门到可施工的引理）

`gateG` 经 `complete 𝗜𝚺₁` 化到语义：对任意 `V ⊨ 𝗜𝚺₁`，
`V ⊨ □Craig(zfcTr G) → V ⊨ zfcTr(zfcTr G)`。
左边经 `models_iff` 即 `Provable Sh.craig ⌜zfcTr G⌝`——**V 中存在一个推导编码 d**。
右边经 `models_zfcTr_iff` 即 `Provable 𝗭𝗙𝗖 ⌜translate(zfcTr G)⌝`——V 中要**构造**一个 ZFC 推导编码。

于是全部义务 = 在 V 内，从"∃d. DerivationOf Sh.craig d {⌜zfcTr G⌝}"出发，产出
"∃d'. DerivationOf 𝗭𝗙𝗖 d' {⌜translate(zfcTr G)⌝}"。

## 义务分解（按依赖序）

### O1. 推导归纳机件（已就绪）

- `Derivation.induction1`（`Proof/Basic.lean:642`）给出 10 条规则支；
- 归纳不变量须取 **sequent 层** `Q d := Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`
  （`ShCraigElimPredicate.lean:65`，Σ1 谓词已证）——**不是**旧 `P`（单公式码，类别错）；
- **设计缺口（必须先解决）**：`translateSeq` 对开放 sequent 裸译；翻译正确性只对
  域内自由赋值成立（`Interpretation.lean:255–278` 的 `ε : ξ → π.Model M`）。
  需要**带自由变量定义域护罩的不变量**（详见审计报告 §3.2）。这是 O2–O6 全部支的前提。

### O2. 规则支（10 条，逐条义务）

| 支 | 需要的零件 | 现状 |
|---|---|---|
| `wkRule` | `Derivable.wk` + `translateSeq_mono` | ✅ 已证（`ShCraigElimBranches.lean`） |
| `verumIntro` | `iT_verum` | ✅ 已证（同上） |
| `andIntro` | `iT_and` + `Derivable.and_m` | 零件齐，未组装 |
| `orIntro` | `iT_or` + `Derivable.or_m` | 零件齐，未组装 |
| `axL` / `cutRule` | 一般码 `iT_neg`（`iT n (neg p) = neg (iT n p)`） | **未过核**（canonical 活跃修复中；本会话定位病灶：`exs` 支的 `exsChanges` 对齐 + `or` 支心跳） |
| `shiftRule` | `iT` 与 `setShift` 相容 | 未证 |
| `allIntro` | `iT` 与 `free`/`setShift` 相容 + 相对化护罩 | 未证 |
| `exsIntro` | `iT` 与 `substs1` 相容；`iVE` 输出是**公式**不是项 | 未证（结构上最难） |
| `axm` | **O3（Craig 证书桥）** | 未证 |

### O3. Craig 证书桥（核心，唯一的"ZFC 公理"接触点）

`axm` 支拿到：`p ∈ Sh.craig.Δ₁Class`，即（经 `IsCraigAxiom` 展开）
`p = q ⋏ qqVerums s ∧ V ⊨ Sh.reWitness(s, q)`（`CraigTrick.lean:207–234`）。
需要产出：`Provable 𝗭𝗙𝗖 (iT 0 p)`。

**已知可用**（本会话逐条核过）：
- `Theory.reWitness_spec`（`CraigTrick.lean:106`）：`V ⊨ T.reCh.val ↔ ∃w, V ⊨ T.reWitness.val`
  ——**对任意 V**，把 reWitness 接回 reCh；
- `Sh.RE`（`TranslateRE.lean:49`）——给出 `Sh.reCh` 的存在。

**缺口**：`V ⊨ Sh.reCh(q) → Provable 𝗭𝗙𝗖 (iT 0 q)` 的一般 V 联系**不存在**：
`reCh` 底层 `codeOfREPred` 经 `Classical.epsilon` 选择，其正确性规格只约束 ℕ
（`Representation.lean:268–277, 347–359`）。ℕ 上的等价不提升为 IΣ₁ 内可证等价。
**候选解法**（审计报告 §4 建议，均未实现）：
1. 显式带证书的 Craig 公理化（不用 `codeOfREPred` 的任意选择）；
2. 若只做 G 门：审 `Sh.craig` 推导在 `⌜zfcTr G⌝` 上的**具体**结构是否绕开一般表示问题
   （注意：仍要处理任意 d，但 d 的结论句固定，或可对"结论为 zfcTr G 的 Craig 公理"
   做更窄的表示引理）；
3. 换影子理论：用显式 `trProv` 生成公理集（自 Craig 化），使证书来源可证。

### O4. 翻译义务（`translateSeq` 相关）

- `translateSeq` 本体 + 四条引理：✅ 已证（`SeqTranslate.lean`）；
- 公式保持性 `isSemiformula_iT`：✅ 已证（C-391 收据）；
- **开放 sequent 的域护罩**：见 O1 的设计缺口。

### O5. 组装与收口

- `derivable_translateSeq`（10 支全接）⇒ `ShCraigElim` ⇒ `gateG` ⇒
  `zfc_z0_full_of_reverse_at_godel` ⇒ 完整 Z0；
- 收据：`capture_run.py` + `verify_cg001_run.py --rerun`；编号从 C-391 起（以 integrator 账本为准）。

## 与全称版的关系（为什么仍值得先做 G 门）

1. **接口**：`gateG` 的消费者是已证的第二定理链（`con_unprovable_of_local_D3`），
   只需这一个实例——不必先完成全称 `ShCraigElim` 的接口改造；
2. **排除绕路**：全称 iff 版 `keyE` 的正向不免费（本会话探针证实），单句反向是规范门；
3. **风险同源**：O1 的设计缺口与 O3 的证书桥是全称版同样要过的关——
   在 G 门上解决一次，全称版可直接复用同一机件。

## 更新（2026-10-11 晚，CG-009 后续）：义务已精确化为五条 + 一条归约

`GateBranches.lean`（sha256 `73ed816c…`，14 条声明全过核）已把 gateG 的义务全部固定为：

```
iT_neg : ∀ n p, IsSemiformula ℒₒᵣ n p → iT n (neg p) = neg (iT n p)
tshift : translateSeq (setShift s) = setShift (translateSeq s)
hall   : 全称规则翻译保持        hexs : 存在规则翻译保持
axmBridge : ∀p ∈ Sh.craig.Δ₁Class, Provable ZFC (iT 0 p)
```

并给出**归约 `tshift_of_ishift`**（已过核）：`tshift ⇐ ishift`，其中
`ishift : iT 0 (shift x) = shift (iT 0 x)`（元素级 `iT`/`shift` 相容）。

**对 `ishift` 的结构分析（本会话）**：`iT` 给每个量词**多引一个 `domZero` 约束变量**
（`iT_all : iT n (^∀ p) = ^∀ (domZero → iT (n+1) p)`），而 `Shift` 的 `all` 支不引新变量
（`shift (^∀ p) = ^∀ (shift p)`）。两边的量化结构因此逐层错位一个 `domZero`。
- 原子层分析：`iVE` 为项引入自己的值变量（`#z ↦ eqAtom ^#(z+1)`），项移位的 +1 与
  值变量的偏移恰好抵消（`iVE (shift t) = shift (iVE t)` 在原子层成立）；
- 复合层：`subst(shiftVec)` 与 `shift` 对约束变量的作用可交换（`j+b+1 = j+1+b`）；
- **判断**：`ishift` 很可能为真，但证明是**跨 `iT`/`iVE` 与 `shift` 的双结构互归纳**
  （含 `conjunct`/`ve2` 的层数记账）——这是继 `iT_neg` 之后最值得攻的一条。
  未证；不得当已证使用。

## 建议的第一批动作（照序执行）

1. 定 O1 的带护罩不变量形状（一页设计 + 一个探针编译）；
2. 组装 `andIntro`/`orIntro`（零件齐，可立即做）；
3. 跟 canonical 的 `iT_neg` 修复（本会话已给病灶定位：`exs` 支 `exsChanges` 对齐、
   `or` 支心跳 → 建议 `ih 0 (by simp) (by simp [iT.construction])` 写法 + 40M 心跳）；
4. 做 O3 的候选 2/3 小规模实验（G 句上的 Craig 公理结构）；
5. `shiftRule`/`allIntro`/`exsIntro` 单独攻（de Bruijn 结构变化，非平凡）。
