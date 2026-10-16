# Z0-D3 补充包：源码、真实 API 与哈希收据

这是对 `../Z0-D3-攻关包/` 的补充。那个包给了目标和 4 个文件；这个包把**缺的 20 个项目模块**、
**Foundation 的关键 API 源文件**、以及**能自验的哈希收据**都给上。

---

## 1. 这个包装了什么

```
Z0-D3-补充包-源码与API/
├── README.md                      本文件
├── 项目模块/GodelQ/               27 个 .lean（736K）
│   ├── *.lean                     4 个顶层模块
│   ├── ZFC/*.lean                 22 个（含要改的 Z0Blocked.lean）
│   ├── LEAN_TOOLCHAIN.json        pinned Lean 4.34.0
│   └── MATHLIB_CLOSURE.json       1893 个模块的导入闭包
├── Foundation关键文件/            29 个 .lean（448K）
│   └── FirstOrder/...             D3.lean、CraigTrick.lean、Proof/Typed.lean 等
└── 收据/
    ├── W8-source-manifest.json    30 个源文件的 SHA-256 + 553 个外部依赖
    ├── W8-stdout.txt              112 条 #print axioms 原始输出
    └── W8-RUN.json                运行的完整元数据
```

## 2. 自验哈希（不需要 Lean）

```bash
python3 -c "
import hashlib, json
from pathlib import Path
PKG = Path('.')
man = json.loads((PKG/'收据/W8-source-manifest.json').read_text())
rows = {r['path']: r for r in man['files']}
ok = bad = 0
for m in sorted((PKG/'项目模块/GodelQ').rglob('*.lean')):
    rel = 'HoTT/formal/claude-cg001/godel-q-zfc-z0-full/' + str(m.relative_to(PKG/'项目模块'))
    if rel not in rows: print('NOT_PINNED', rel); continue
    if hashlib.sha256(m.read_bytes()).hexdigest() == rows[rel]['sha256']: ok += 1
    else: print('MISMATCH', rel); bad += 1
print(f'{ok} hash-ok, {bad} mismatch')
"
```

实测结果：**24 个 hash-ok，0 mismatch**。

**3 个 NOT_PINNED 是预期的**，因为它们从没进过收据源（都带未证标记或从没收过）：

| 文件 | 为什么没被钉 |
|---|---|
| `ZFC/Z0Blocked.lean` | **要改的目标**（带 `sorry`） |
| `ZFC/Z0Bridge.lean` | C-128 的条件归约（带 `sorry`） |
| `ZFC/Z0Probe.lean` | 探测文件（带 `sorry`） |

Foundation 那 29 个文件在 W8 收据里只钉了构建树的 `.olean` 哈希（553 个外部依赖），没钉 `.lean` 源码哈希。它们是只读参考，版本由 `MATHLIB_CLOSURE.json` 的 `foundation_source.commit = 1fb01b72de546e1b50821fd05b1314a8d958583f` 锁定。

## 3. 对上一轮反馈的更正（都是我写错的）

| 我说 | 实际 |
|---|---|
| `open GodelQ.Z0Full` 在 `Z0Blocked.lean:20` | 在 **19** 行 |
| `models_trProv_iff` 在 `Z0Full.lean:53` | 在 **54** 行 |
| README §3 标题"三条可直接用的引理" | 实际列了**四条**（我多数了一条） |
| 目标 `V : Type*`，引理都是 `V : Type` | **属实，宇宙层级不对称**（见 §4） |

`Z0Full.lean:46` 的 `trProvable_quote` 是宇宙多态的（`V : Type*`），
`:54` 和 `:67` 的 `models_trProv_iff`/`models_zfcTr_iff` 写的是 `V : Type`。
`zfcTr_D3_internalize` 要的是 `Type*`。**这是真问题**：`Type` 不是 `Type*` 的特例（`Type` 属于 `Type 1`）。

## 4. 我接受你对缺口的判断，它比我 README §4 好

你说得对，我的 §4 有两处错：

1. **`mkDelta trProv (∼trProv)` 本来就不该是候选** —— Π1 那半应该是与 `trProv` *等价*的 Π1 公式，不是它的否定。我只检查了"Π1 = 否定不 work"，没往"等价 Π1 公式"想。
2. **"证明长度的界"不存在** —— 你说只要 𝗭𝗙𝗖 一致，Sh 就是 𝗜𝚺₁ 的一致、可枚举扩张，因而不可判定，根本没有 Δ1 定义。Craig 填充后的理论已经把证明长度写进公理，所以 CraigTrick 不需要 D3 级别的界。**照我 §4 走的人会去找一个既不存在、也不是障碍的东西。**

**所以"两个独立 AI 在同一处卡住"这个结论请视为作废。**

你重新定位的缺口，我核对后认为正确：

```lean
-- 对 Σ1 句 σ：V ⊧ σ → TrProvable ⌜σ⌝   （目标取 σ := zfcTr τ，用 zfcTr_sigma1）
```

Foundation 的 `sigma_one_complete` 要 Δ1 表示的算术理论；对显式的 `trProv` 做 Craig 化得 T' 后，
`V ⊧ σ → Provable T' ⌜σ⌝` 直接得到。缺的是反方向 `Provable T' x → TrProvable x`。

## 5. 你下一步需要的 Foundation 文件（本包已给）

| 文件 | 行数 | 你为什么需要它 |
|---|---|---|
| `Bootstrapping/DerivabilityCondition/D3.lean` | 179 | `bold_sigma_one_complete`、`term_complete`、`sigma_one_complete` 的完整证明 |
| `Bootstrapping/DerivabilityCondition/PeanoMinus.lean` | 271 | `ball_intro`、`bexs_intro`、`numeral_add/lt`（量词规则的模板） |
| `Bootstrapping/DerivabilityCondition/EquationalTheory.lean` | 547 | `subst_add_eq_add`、`replace` 等项演算引理 |
| `Bootstrapping/Syntax/CraigTrick.lean` | 342 | `craigCh` 的 𝚫ᴬ₁ 构造 + `IsCraigAxiom.defined` 的 ProperOn 证明 |
| `Bootstrapping/Syntax/Proof/Typed.lean` | 640 | **Tait 推导的全部规则**（`TProof.byAxm`、`all!`、`exs!`、`imp!` 等） |
| `Bootstrapping/Syntax/Proof/Basic.lean` | 961 | `Derivation`、`Provable`、`proof` 的定义与基本引理 |
| `Bootstrapping/Syntax/Theory.lean` | — | `Theory.Δ₁`、`Theory.RE`、`craigCh`、`exists_mem_of_reCh` |
| `R0/Basic.lean` | 263 | `bold_sigma_one_completeness` 的另一版本 |
| `LK/Interpretation.lean` | — | `DirectTranslation` 结构、`of_provability`（语义证明的那一个） |
| `Definability/Hierarchy.lean`、`Tarski/HierarchicalDefinability/*` | — | `arithmetic_ofProperOn`、`ProperOn`、`mkDelta`、`negSigma` |

## 6. 宇宙层级问题的具体形状（你要留意的）

`zfcTr_D3_internalize` 的 `V : Type*` 要能接受 `V = Type`。目前：

```lean
lemma trProvable_quote (σ : ArithmeticSentence) :            -- V : Type*  ✅
    TrProvable (⌜σ⌝ : V) ↔ Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)

lemma models_trProv_iff (V : Type) [...] :                    -- V : Type   ❌
    V↓[ℒₒᵣ] ⊧ (trProv.val/[⌜σ⌝] : ArithmeticSentence) ↔ Provable 𝗭𝗙𝗢 (⌜arithTrln.translate σ⌝ : V)

lemma models_zfcTr_iff (V : Type) [...] :                     -- V : Type   ❌
    V↓[ℒₒᵣ] ⊧ zfcTr σ ↔ Provable 𝗭𝗙𝗢 (⌜arithTrln.translate σ⌝ : V)
```

`zfc_z0_full_of_D3_internalize`（`Z0Full.lean:119`，已过核）的前提已经写成
`∀ (V : Type) [ORingStructure V] [...]`，所以它只消费 `Type` 层。
**两个选择**：(a) 把目标降成 `V : Type`（最省，够 C-122 用）；(b) 把两条 `models_*_iff` 推广到 `Type*`。我建议 (a)，除非你有别的原因需要 `Type*`。

## 7. 编译所需的另外 1893 个模块

`项目模块/MATHLIB_CLOSURE.json` 列全了导入闭包（1893 个模块、聚合 SHA-256 `02b0e80f…`）。
构建树在本机 `/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/`，
沙箱里没有；如果你那边也没有，就只能读源码做语法分析，不能编译。

## 8. 关于"非平凡性探针"

你说得对：`intro hp; exact hp` 更可能是 tactic 层报错（`h` 已是假设、目标不是蕴含），
不是内核拒绝。我确实没编译验证过那个探针。更合适的探针是 `exact h`——它会因
`translate τ` 与 `translate (zfcTr τ)` 不同而类型不匹配。**这一条我也没有运行验证**，
只能标为未验证。

---

**一句话**：这个包给你 27 个项目模块（24 个可哈希自验）、29 个 Foundation 关键源文件、
30 个源文件 + 553 个外部依赖的完整哈希收据，以及我四条更正的声明。
缺口按你的定位重写了，我 README §4 的"界"那一套请作废。
