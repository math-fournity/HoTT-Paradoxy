# 有哥德尔路线

> 研究发起人要的两个结果之一。2026-10-05（dev-notes 0115）【原话】：“1、无哥德尔的思路。2、有哥德尔的思路。”

## 目标

- **原问**：【原话】十三条 [11]（KC-000073）：“我们能够从元思维，甚至是元元思维上借鉴哥德尔的巧妙思路来完成同样的证明吗？……可能是神似，而不是形似的。”
- **要证的判词**：十三条 [4][6][8]（KC-000066、KC-000068、KC-000070）。
  - bare ZFC 在时间维度上的理论观察力不完备，“不是没有时间维度的观察力，只是没有完备的观察力”；
  - Q／P／A／B；
  - ZFC-1 = ZFC + A = ZFC + P；
  - 魔鬼交易。
- **取法**【解释】：
  - 接受 = bare ZFC 自己的可证性；
  - 原过程完成 = 过程停机（依据研究发起人的口径：KC-000010、KC-000024、KC-000065）；
  - 对角点由 Kleene 递归定理构造，不写进前提；
  - “时间维度 = 过程的逐步运行”是解释桥，不是定理。

## 状态

| 节 | 内容 | 状态 | 证据 |
|---|---|---|---|
| 1 | 抽象层：满足标准元性质的有效理论上，有过程形式的哥德尔 I、魔鬼交易、跑者，以及 Z0 的可推导条件形式 | ✅ | [`godel-q/CLAIM.md`](../../HoTT/formal/claude-cg001/godel-q/CLAIM.md)：C-84–C-94，5 个运行 |
| 2 | 真实 𝗭𝗙𝗖 是有效理论：公理有 Δ1 表示，有数字，永不停句可枚举，𝗭𝗙𝗖 ⊳ 𝗥₀，Σ1 完全 | ✅ | [`godel-q-zfc/CLAIM.md`](../../HoTT/formal/claude-cg001/godel-q-zfc/CLAIM.md)：C-95–C-98 |
| 3 | 每一刻看得见、永远看不见；对角过程的两句都独立 | ✅ | C-99、C-100 |
| 4 | 魔鬼交易；𝗭𝗙𝗖 + A = 𝗭𝗙𝗖 + P | ✅（跑者部分在旧接口 ΦH 上以“到达句”参数为条件；在新接口 ΦS 上无条件，C-118） | C-99、C-101、C-118；A ⟺ P 的闭包条件形式见 C-116 |
| 5 | 与 Foundation 自带的不完备定理交叉核对 | ✅ | C-102 |
| 6 | Z0：𝗭𝗙𝗖 证明不了自己的矛盾搜索永不停 | ◐ **影子形式不带前提 ✅**（`𝗭𝗙𝗖 ⊬ (Sh.craig.consistent)ᵗ`，C-120）；**内部化：除一条消去外全部成为定理**（C-121、C-122；入口障碍已清除 C-390；第 2 层公式保持性地基已证 C-391；`hAll` 支的公式层义务已收缩到一条桥 C-404） | C-103；C-109、C-110、C-111、C-119、C-120（影子形式无条件），[`godel-q-zfc-z0-translate/CLAIM.md`](../../HoTT/formal/claude-cg001/godel-q-zfc-z0-translate/CLAIM.md)；C-121、C-122 与唯一阻塞引理 [`godel-q-zfc-z0-full/CLAIM.md`](../../HoTT/formal/claude-cg001/godel-q-zfc-z0-full/CLAIM.md)；C-390（宇宙多态桥 + `bwd` 归约）[`CLAIM-Z0-UNIBRIDGE.md`](../../HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/CLAIM-Z0-UNIBRIDGE.md)；C-391（第 2 层公式保持性地基）[`CLAIM-Z0-W8-LAYER2-FORMULA.md`](../../HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/CLAIM-Z0-W8-LAYER2-FORMULA.md)；见 [02 节](02-Z0-条件形式与剩余三步.md) |
| 7 | 把跑者的“到达”句写成集合语言，并在 𝗭𝗙𝗖 中证明等价 | ✅（新的停机公式 ΦS；到达句是算术写法） | C-117、C-118，[`godel-q-zfc-runner-arrival/CLAIM.md`](../../HoTT/formal/claude-cg001/godel-q-zfc-runner-arrival/CLAIM.md)；见 [03 节](03-跑者的到达句.md) |

各条的细节见 [01 节](01-已证-过程观察的不完备.md)。

## 边界

- 不推出 ZFC ⊢ ⊥。矛盾在 𝗭𝗙𝗖 + P 中。
- 同一个“永远看不见”另有一条不经对角点的证明：无哥德尔路线的图灵路线，CG001-C-104、C-105（第 02 章）。哥德尔路线指名一个漏点 d；图灵路线证明漏点无穷且列不全。
- 𝗭𝗙𝗖 一致与数字句 Σ1 可靠，来自 Lean 元层的 `Universe` 模型（要用宇宙）。它们不是 𝗭𝗙𝗖 内部可证的事。
- 芝诺、H0、Z0 的“同一个 Q”：2026-10-09 起在一个有单价性的内核里写成同一类型、同一程序（C-112、C-113），Z0 在那里是参数；“完整任务合同下相同”仍未做（见 [04-同一个Q](../04-同一个Q/README.md)）。
- 哥德尔、Kleene、Turing、Löb 的数学是经典结果。新的是读法与综合，以及把它们落到 Foundation 的 𝗭𝗙𝗖 上所需的部分。没有做过文献查重，外部复核没有发生。

## 下一步（按顺序）

1. ~~Z0 的前提 (a)：`𝗜𝚺₁ ⪯ Sh`~~：✅ 已证（C-109、C-110），得到全部 𝗣𝗔。
2. ~~Z0 的前提 (b)~~：✅ 翻译可计算（C-119），`Sh.RE` 与 Z0 的影子形式无条件（C-120）。
3. (c) 内部化：2026-10-09（CG-007 W8）把步骤 (c) 收窄成一条精确的 Lean 引理 `zfcTr_D3_internalize`——“𝗭𝗙𝗼 证明了 σ 的翻译，就能证明‘𝗭𝗙𝗸 证明了 σ 的翻译’这句话的翻译”。显式可证性谓词 `𝔅Z(x) := Provable 𝗭𝗙𝗸 (iT 0 x)` 下的 D1、D2、一致性句等价、Σ1 层级、以及 D3 在标准模型 ℕ 中的正对照都已成为定理；该引理一旦成立，完整形式 `𝗭𝗙𝗸 ⊬ (𝗭𝗙𝗸.consistent)ᵗ` 立即随之成立（C-122）。引理本身未证，见 [`godel-q-zfc-z0-full`](../../HoTT/formal/claude-cg001/godel-q-zfc-z0-full/)。
- **2026-10-11 复核**：W8 把内部化固定成的 `zfcTr_D3_internalize`（`Z0Blocked.lean`，仍带 `sorry`）经 C-390 `bwd_of_shcraig_elim` 精确归约为一条消去 `ShCraigElim`（`Provable Sh.craig ⌜σ⌝ → Provable 𝗭𝗙𝗖 ⌜translate σ⌝`）。本机实物核对：`ShCraigElimSetup.induction_setup` 仍 10 个 `sorry` 骨架。剩余工作 = 填该归纳的 8 个支（andIntro/orIntro/axL/cutRule 易；shiftRule/allIntro/exsIntro 需照 iT_neg 写 iT_setShift/iT_substs1；axm 需读 CraigTrick.lean）。专供外部 AI 的包见 `外部资料/Z0-D3-攻关包-网络完备版/`。
- **2026-10-11 清缓存强制重编译更正（Claude 会话）**：上条中"`ShCraigElimNegLaw.iT_neg` 已 0-sorry 编译"**不成立**——它仍 **exit 1**（`line 93/99` 两处 `rw [← ih …]` 形状不匹配，在 `all`/`exs` 两支；文件 99 行、0 个 `sorry`）。另：`NegInvolution.neg_neg_code` 经同法核实为 **exit 0**、`#print axioms` 仅三条标准公理，**但尚未出正式收据**。详见根 `AGENTS.md`「CG-007 真实进度基准」条与 `HANDOFF-2026-10-11-CODEX-W8-D3.md`。
- **2026-10-11 归纳七支接线（新收据 CG001-C-400）**：`ShCraigElimBranches.lean` 的 `isFormulaSet_translateSeq`、`hWk`、`hVerumIntro`、`hAxL`、`hAnd`、`hOr`、`hCut` **七个支全部无 sorry**（run `20261011-CG001-Z0-W8-BRANCHES-02`，`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0 B、七条引理公理报告只有三条标准公理）。其中 `hAxL`/`hCut` 正是 C-398 的直接消费者（用 `iT_neg` 把 `iT 0 (neg p)` 换成 `neg (iT 0 p)`）；`hAnd`/`hOr` 用 `translateSeq_insert` + `iT_and`/`iT_or`。**仍缺三支**：`hAll`/`hExs`/`hShift` 需要 `iT` 与 `setShift`/`substs1` 的相容律，本机实测**不存在**（`shift` 的构造原子支用 `termShiftVec`、量词支不加 `domZero`，与 `iT` 不同构，比 `iT_neg` 复杂）；`axm` 支需要 `codeOfREPred` 的一般 V 表示引理。`zfcTr_D3_internalize` 仍未证。
- **2026-10-11 `iT`/`shift` 相容律已证（新收据 CG001-C-402）**：`ITShift.iT_shift`（`iT n (shift p) = shift ℒₛₑₜ (iT n p)`）**九支全证、零 sorry**，公理仅三条标准公理；run `20261011-CG001-Z0-W8-SHIFT-COMPAT-01`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0 B、`--rerun` `EXACT_EXIT_STDOUT_STDERR_MATCH`）。支撑链：`ShiftConjunct` 十六引理（**`shift_conjunct` 的跨会话三次失败关闭**——参数序陷阱：`shift_substs` 的 `n` 是长度、`m` 是层数，与 `IsSemitermVec` 定义顺序相反）→ `IVeShift.iVE_shift`（项层，func 支用 `sigma1_induction` + `shift_ve2` + `resultVec` 点相容）→ `IVeShift.iTR_shift`（原子层）→ `ITShift.iT_shift`。这**推翻**了此前「`iT`-`setShift` 相容律不存在、比 `iT_neg` 复杂」的判定。
- **2026-10-11 `hShift` 接线（新收据 CG001-C-403）**：`TranslateSeqShift.translateSeq_setShift` + `ShCraigElimBranches.hShift` + `ShCraigElimInduction` 的 `shiftRule` 支。**归纳接线数 6 → 7**；待补从 4 支降到 3 支（`allIntro` 的 `setShift` 半边随之解决，剩 `free` 半边；`exsIntro`；`axm`）。**注意**：`induction_setup_Q` 本身仍带 `sorryAx`（3 个未证标记），7/10 是**支**数，不是定理数。
- **2026-10-11 `iT_neg` 已证（新收据 CG001-C-398）**：`ShCraigElimNegLaw.iT_neg`（一般相容律 `iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)`，V 内任意公式码）**九个支全部证出**，0 个 `sorry`、`#print axioms` 仅三条标准公理；run `20261011-CG001-Z0-W8-ITNEG-01`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0 B）。归纳谓词带 `param = n` 护罩；`rel`/`nrel` 要 `IsUTermVec`，`and`/`or` 用 `conv_rhs` + `congrArg₂`，`all`/`exs` 用 `result_*` + `nth_adjoin_zero` + `conv_rhs` 归形 + 正向 `ih`。**这解锁了 `hAxL`/`hCut`/`hShift` 的接线，但三支尚未接进 `ShCraigElimSetup.induction_setup`**；`ShCraigElim` 的 10 个支仍未填，`zfcTr_D3_internalize` 仍未证。
- **2026-10-12 `iT`-`termSubst` 相容律（T1）进行中，语句层纠正一处类型错误**：本工作单元新建 `ITSubsts1.lean`，把 `hAll` 归约到的那条桥 `B(q)` 拆成「项层子律 T1 + 九支组装」。**关键纠正**：`subst` 是**公式层**操作（`UformulaRec1`），作用在项上时**不按项构造归约**；`iVE 0 (subst ℒₒᵣ ?[^&0] t)` 的内层代换作用在**项** `t` 上，正确写法是 `iVE 0 (termSubst ℒₒᵣ ?[^&0] t)`。写成 `subst` 时 `rw [termSubst_bvar]` 永远找不到 occurrence——这不是策略问题，是**语句问题**（此前会话的工作台把它记成了策略问题）。正确形态：
  `subst ℒₛₑₜ (^#a ∷ ?[^&0]) (iVE 1 t) = subst ℒₛₑₜ ?[^#a] (iVE 0 (termSubst ℒₒᵣ ?[^&0] t))`（`t` 层 1）。
  **已过核**（exit 0）：bvar、fvar、`ve0`（`k = 0`）三支 + 向量层工具（`isSemitermVec_a0`/`_a`/`_0`、`subst_ve0_body`/`_₁`、`rhs_bvar`/`rhs_fvar`、`termSubstVec_two`、`subst_eqAtom_cons`/`_a0`/`_a`、`resultVec_two_eq`、`subst_qqAlls_two`、`subst_imp`、`subst_conjunct`）。**`ve2` 支（`k = 2`，绑定子）未完成**：归纳谓词已改成 `∀ a < m` 形式（`definability` 接受），目标形状已由探针 `ProbeVe2.lean` 实测确认，但证明在 4,000,000 heartbeat 下 `whnf` 超时（326 秒），需另找代价更低的写法。
- **2026-10-12 `axm` 支的引号化版本已证**：`ShCraigElimAxm.lean`（exit 0，公理仅三条标准公理）给出 `zfc_provable_of_mem_craig`（`σ ∈ Sh.craig ⟹ 𝗭𝗙𝗖 ⊢ translate σ`）、`derivable_of_provable_mem`、`hAxm_quoted`（`p = ⌜σ⌝` 时 `Q (axm s p)`）。**范围**：`p` 必须是**引号**；从 `p ∈ Sh.craig.Δ₁Class` 到 `∃ σ, p = ⌜σ⌝` 这一步对**非标准** `p` 不成立（V 层 `Δ₁Class` 只给 `V ⊧/![p] Sh.craig.Δ₁ch`）。完整 `ShCraigElim` 需要补这一步。
- **2026-10-12 五处实现陷阱（本轮实测，写进工作台备查）**：① `substs_substs` 的 `n` 是**向量长度**、`m` 是层，与 `IsSemitermVec` 定义序相反（这是 `shift_conjunct` 三次失败的同一根因）；② `subst_imp` 的参数序是 `(hp hq)`，而 `ve0` 的体是 `imp ⊤ body`，写反会静默匹配失败；③ `rw [show (2:V) = 1 + 1 by norm_num]` 产生 `0+1+1` 而非 `1+1`，与目标不匹配——`show` 的**字面量形状必须与目标逐字相同**；④ `IsUTermVec.empty` 无 `n` 参数、`IsUTermVec.empty_iff` 才做消去；⑤ `IsUTerm.fvar` 需 `(n) (x)` 两个参数，`IsSemiterm.fvar` 只需 `x`。

- **2026-10-12（续）`ve2` 支重构：426 秒 → 5.6 秒；左侧接入成功**：`ve2` 支原先写成 `iVE_subst_a0` 内的**内联大装配**，单次编译 **426 秒**且在 `whnf` 上 8,000,000 heartbeat 超时。照 `ShiftConjunct.shift_ve2` 的形状抽出独立引理 `subst_ve2`（把 `ve2` 的体只展开**一次**）后，**编译 5.6 秒**、exit 0。`ve2` 支内改为四步廉价归一（`termSubst_func` → `iVE_func`×2 → `resultVec_two_eq`×2）后调 `subst_ve2` 两次：**左侧（`n = 1`）已接入成功**，右侧（`n = 0`）剩一处。`isSemitermVec_mono` 已推广到任意语言。**残留的精确形状**：右侧 `W` 分量是 `iVE 0 (termSubstVec 2 ?[^&0] v).[i]`，`subst_ve2` 要 `iVE 0 (termSubst ?[^&0] v.[i])`——差一条 `nth_termSubstVec`；且 `iVE` 的**层参数**与 `IsSemiformula` 的**层**是两个独立的东西（右侧 `iVE 0` 的层参数是 0，而 `W` 分量的公式性在层 `0 + 1 = 1`）。文件整体 exit 0（1 个未证标记）。

- **2026-10-12（再续）`ve2` 支右侧的根因找到：向量 `?[^&0]` 的层是 0，不是 1**：`ve2` 支右侧连续三轮失败的真正原因不是策略，是**层数写错**——`?[^&0]` 的 `termBV` 是 0（fvar 不含 bvar），却写成了层 1。改对之后右侧的两个 `isSemiformula_iVE (n := 0)` 见证立刻成形。**已接线**：`termSubst_vec` 归一 → `isSemiformula_iVE` ×2 → `subst_ve2` ×2（左右两侧）→ `qVec_qVec_a0`/`qVec_qVec_a` → `simp only [conjunct]`（四个合取块展开成 8 块）。**剩余**：8 块按三层 `substs_and` 摊平——前两块（`cDomN` 槽）两侧同形，后四块正是 **T1 在 `a := 0`/`a := 1` 的实例**（即归纳假设 `ih0`/`ih1`）。源代码注释里已画好这张 8 块对照表。

- **2026-10-12（再续）项层子律 T1 完整证出（四支全证、零 sorry、零 sorryAx）**：`ITSubsts1.iVE_subst_a0` (`subst ℒₛₑₜ (^#a ∷ ?[^&0]) (iVE 1 t) = subst ℒₛₑₜ ?[^#a] (iVE 0 (termSubst ℒₒᵣ ?[^&0] t))`，`t` 层 1，`3 ≤ m`，`a < m`) 编译 **exit 0**、`#print axioms` **无 sorryAx**、43 条引理。bvar/fvar/`ve0`/`ve2` 四支全证。**两个关键发现**：① **层数根因**——向量 `?[^&0]` 的层是 **0**（fvar 不含 bvar）而非 1，这是 `ve2` 支右侧连续失败的真正原因；② **`subst` 与 `termSubst` 之别**——`iVE 0` 参数里的内层代换作用在**项**上，公式层 `subst` 不按项构造归约，必须写 `termSubst ℒₒᵣ`；此前工作台把它记成策略问题，实为**语句问题**。`ve2` 支的做法：两侧各推两层 `qqAlls` 后，四个 `conjunct` 逐个 `subst_conjunct`，结论项两侧逐字相同，两个 `y` 槽即归纳假设 `a := 0`/`1`。**下一步**：把 T1 组装成公式层桥 `iT_substs1`（九支），再接线 `hAll`。**尚未出 F-011 收据**。

- **2026-10-12 `hAll` 支的唯一公式义务 `hkey` 完整证出（新收据 CG001-C-404）**：`ProbeHAllRoute.lean` 此前已把 `ShCraigElim` 归纳步第 2 支（`allRule`）的全部构造性内容归约到一条公式恒等式；本轮在 `GodelQ/ZFC/HAllKey.lean` 把它完整证出：`free ℒₛₑₜ (imp domZero (iT 1 p)) = imp (subst ℒₛₑₜ ?[^&0] ↑cDomN) (iT 0 (free ℒₒᵣ p))`（`p` 层 1）。run `20261012-CG001-Z0-W8-HALLKEY-01`：`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0 B、`--rerun` `EXACT_EXIT_STDOUT_STDERR_MATCH`；`#print axioms` 仅三条标准公理。证法四步全是既有引理的重排（`free` 展开 → `shift_imp`/`shift_domZero` → `← iT_shift` → `subst_imp` + **桥 `B`**）。**因此 `hAll` 支只剩桥 `B(q)`（`iT_substs1`）一条公式义务**——即第 2 层的剩余缺口从「整支」收缩到「九支公式层桥」。`subst_imp` 随之从 `ITSubsts1.lean` 抽到新的干净文件 `GodelQ/ZFC/SubstImp.lean`（原因：F-011 驱动要求源清单内无未证明占位，而 `ITSubsts1.lean` 仍在建桥）。**两个新的 V 字面量陷阱**（已就地记入文件头）：① `V` 是抽象 `ORingStructure`，`0+1` 与 `1` **不是** definitional equal，须 `have e : (0:V)+1 = 1 := by norm_num; rw [← e]`；② `isSemiformula_domZero (n := 0)` 会把 `V` 的 universe 塌到 `0`，写 `(domZero (V := V))` 拉回。

- **2026-10-12 桥 `iT_substs1` 原子支核心引理 `subst_iTR` 已证（exit 0，2.7 秒）**：`subst w (iTR n 2 R v) = qqAlls (imp (subst (qVec (qVec w)) (conjunct 2 n 0 (iVE n v.[0]) ⋏ (conjunct 2 n 1 (iVE n v.[1]) ⋏ ⊤))) (subst (termSubstVec 2 (qVec (qVec w)) ?[^#0,^#1]) (cRel R))) 2`（新文件 `GodelQ/ZFC/SubstITR.lean`）。证法照 `subst_ve2`：`iTR` 展开 → `subst_qqAlls_two` → `subst_imp` 拆 `imp` → `substs_substs` 并成**一次**代换。**四个 `conjunct` 故意不在本引理内做**（留给调用方，那是 `ve2` 支走过的路）。**尚未出 F-011 收据**：它 import 在建的 `ITSubsts1.lean`，驱动会拒；收据等 `iT_substs1` 整体完成。
- **2026-10-13 核验更正：桥 `iT_substs1` 编译实测 exit 1 / 10 处 error / 仍含 `sorryAx`**：同一文件的**工作副本 0 个文本 `sorry`**，但 `devbuild_ns.py` 实测 `## lean GodelQ/ZFC/ITSubsts1.lean (497.8s, exit 1)`，10 处 error；`#print axioms` 三个名字（`iT_substs1`、`iT_substs1'`、`conjunct_rename_second_gen`）都带 `sorryAx`。日志留档 `HoTT/verification/runs/20261013-CG001-Z0-W8-BRIDGE-STATE-01.txt`。**方法论教训**：**「文件里没有 `sorry` 这个词」不等于「证出了」**——把空着的支填进类型不匹配的见证，产出的是 error + `sorryAx`，比留着 `sorry` 更难诊断。进度判定一律以真实 kernel 运行为准。**协作状态**：该文件另有 Claude 会话在本 worktree 活跃重构（02:03 / 02:14 / 02:24 / 02:34 四次保存，16–22 个并发 lean 进程）；按项目规则未插手。


- **2026-10-13 舰队协调：桥 `B(q)` 是四线共用的同一引理；`exsIntro` 裁决走可证蕴含路线**：
  Master 逐字核对确认：本线的 `iT_substs1` ≖ 一般律 `iT_subst_open` 的 m=0 实例
  （`QvecVOr 0 = QvecV 0 = ?[^&0]`）≖ iShift 的 `iT_free_eq` ≖ 9276 的 `iT_free` 中段
  ≖ 本线 `hkey_probe` 的假设 `hB`。**全舰队（iShift 的 hAB、9276 的 hAll、本线的 hkey 接线）都在等这一座桥。**
  结构发现（影响 all/exs 支）：m=0 桥的 all 支下降一层后，子目标 = 一般律在 **m=1**、层 2 子公式的实例
  （`qVec (QvecVOr m) = QvecVOr (m+1)` 递归闭合）；公式深度无界 ⟹ **「all/exs 差一层」不是包装 bug，是承重现象**，m=0 无法在没有一般律（或等价归纳装置）下完成。
  这与本线 10-12 记录（「原子支层齐，剩余是 T1 的层泛化版与量词支 +1 错位」）是同一结论的另一条推导路径。
  **协调决定**：001-Step 升为一般律主承重线（∀m 含 0）；本线保留 m=0 装配作对照/验证；谁先完成全体采纳。
  **`exsIntro` 裁决备案**：走**可证蕴含**路线 `ZFC ⊢ iT 0 (subst ?[t] p) → ∃x (x ∈ ω ∧ iT 1 p)`——
  最终定理十支不变，中间引理形状属证明工程；若该形状使归纳结构不成立再升级研究发起人。**已报用户。**

- **2026-10-13 `subst_iTR` 自包含化并出收据（CG001-C-405）——一个可复用的解锁模式**：
  `subst_iTR`（桥原子支的核心工具引理）此前已证（2.7s exit 0）但**无法出收据**：
  它 import 在建的 `ITSubsts1.lean`，而 F-011 驱动要求源清单内无未证明占位。
  本轮把 `subst_iTR` 唯一用到的两条 helper（`qqAlls_two`/`subst_qqAlls_two`、`isSemitermVec_mono`，
  共三条短证）**搬进 `SubstITR.lean` 使其自包含**，收据随即可得：
  `20261013-CG001-Z0-W8-SUBSTITR-01`，`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0 B、33 源文件、
  `--rerun` `EXACT_EXIT_STDOUT_STDERR_MATCH`、`#print axioms` 三条标准公理。
  **可复用模式**：凡「已证但被在建文件拖住收据」的引理，先查它真正用到几条 helper；
  若只有两三条，搬进本文件自包含比等上游便宜得多。**本舰队其他线可能有同样情形。**
  **禁止外推**：这是桥**一个支**所需的工具引理；桥本体（九支组装）仍未通。

  **2026-10-13（本线停止点，Master 已确认）**：桥 `iT_substs1` 的工作副本与
  类型读取探针已提交并推送（`511d2c8e`，分支 `codex/cg007-w8-d3`）。
  **真实状态：exit 1、13 error、1 处显式 sorry（`nrel` 支）——不可用，不要当已完成引用。**
  已跑通的部分：六支（verum/falsum/and/or/all/exs）归约链；
  `rel` 支的数学内容（`conjunct_rename_second_gen`，由本线 T1 一步给出）；
  `rel`/`nrel` 的剩余 error **全部是层数字面量对齐，无数学问题**。
  **总根源（给接手者）**：`termSubstVec` 要求 `w` 的长度 = `v` 的层（同一个 `n`），
  而 `?[^&0]` 长度恒 1 ⟹ 必须先用 `n = 1` 把层数具体化。
  三条已排掉的假路线（`subst ?[^&0] domZero = domZero` 假；同层朴素交换律假；
  `∀ w` 版使谓词变 Π1 用不了）记在 `ITSubsts1.lean` 的提交信息里。
  接手：语法路线 001-Step/001-Flash（一般律 `iT_subst_open`，未证）、语义路线 004-Step。

- **2026-10-14 `axm` 支引号化版本 + `Z0Full` 条件形式：独立编译核验并出收据（CG001-C-406）**：
  应 Master 征询「Z0Full 还有哪些支带 sorry」，本机全链实测：
  `ShCraigElimAxm.lean`（75 行）与 `Z0Full.lean`（145 行）**均 0 个未证标记、exit 0**。
  `Z0Full` 七条：`zfcTr_con_iff`（影子一致性句与 `𝗭𝗙𝗖.consistent` 可证等价）、`zfcTr_sigma1`、
  `sh_z0_full [zfcTr.HBL3]`、`zfc_z0_full [zfcTr.HBL3]`、`zfc_z0_full_of_D3_internalize`、
  正对照 `zfcTr_D3_standard`（D3 在标准模型 ℕ 中成立）。
  `ShCraigElimAxm` 三条：`zfc_provable_of_mem_craig`、`derivable_of_provable_mem`、`hAxm_quoted`。
  收据 `20261014-CG001-Z0-AXM-Z0FULL-01`：`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0 B、30 源文件、
  `--rerun` `EXACT_EXIT_STDOUT_STDERR_MATCH`，公理全为三条标准公理。
  **禁止外推**：`zfc_z0_full` 带 `[zfcTr.HBL3]` 类型类前提、`zfc_z0_full_of_D3_internalize`
  以 `zfcTr_D3_internalize` 为前提——**D3 本身仍未证，缺口不在 Z0Full 而在 Z0Blocked**。
  另：`hAxm_quoted` 是**引号化**版本；9276 的 `RootKey`（若对任意 `p`）是**更强**命题，
  两者是**特例与一般**的关系，不是取代——**一般版本仍未证**。

4. ~~跑者的到达句~~：✅ C-117、C-118（CG-007 W5）。实分析版（在 ℒₛₑₜ 中构造实数）没有做，见 [03 节](03-跑者的到达句.md)。
5. ~~同一个 Q 并列进一个内核~~：✅ C-112、C-113（第 04 章）。
6. ~~想法 T 的一般形式、P 的两侧~~：✅ C-114、C-116（第 07 章）。

可能的方向见 [04 节](04-可能的推进方向.md)。

## 线头

- **GUI 对话**：
  - 主干 `dev-08/0112`–`0122`：哥德尔路线出生，GODEL-Q-REFLECTION-SOP，T-PRECISION-DIAGONAL-SOP；
  - `dev-09/0003`–`0014`：想法 T、T-OBS、T-DIAG、GODEL-ZFC-CONVERGENCE-SOP；
  - `dev-01/0010`–`0013`。
  - 倒查用 `python3 .claude/goals/CG-006-zfc-complete-formalization/tools/gui_backtrace.py dev-09`。
- **GPT 的前作**：
  - C-368：T-DIAG 的条件性对角核，`HoTT/formal/t-precision-diagonal/`；
  - C-369：set.mm 附录 C 的变量扩展，`HoTT/formal/godel-q-reflection/`；
  - 收敛 SOP：`origin/dev-09:dev-docs/哥德尔式ZFC理论精度收敛闭环SOP.md`，其中 C1、C2、C3 三个判词值互斥。
- **目标包与笔记**：CG-005（`.claude/goals/CG-005-godel-q-synthesis/`）、CG-006（`.claude/goals/CG-006-zfc-complete-formalization/`）；CN-065、CN-067、CN-068（`.claude/思考与发现/`）。
