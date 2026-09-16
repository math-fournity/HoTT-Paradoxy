# Cubical Gödel 基础设施：从可检查证明关系到自然数证明码

> Evaluation：`CUBICAL-GODEL-PROOF-CHECKER-001`
> Proof chain：`PF-CUBICAL-GODEL-PROOF-CHECKER-001` → `PF-CUBICAL-GODEL-PROOF-SERIALIZATION-001` → `PF-CUBICAL-GODEL-FORMULA-BITCODE-001` → `PF-CUBICAL-GODEL-PROOF-BITCODE-001` → `PF-CUBICAL-GODEL-NAT-PROOF-CODE-001`
> Classifier bridge：`PF-CUBICAL-GODEL-PROOF-SEARCH-CLASSIFIER-001`
> Claims：`MP-CGI-EQUALITY-001`、`MP-CGI-CHECK-SOUND-001`、`MP-CGI-CHECK-COMPLETE-001`、`MP-CGI-TRUNCATED-PROVABILITY-001`、`MP-CGI-CONTROLS-001`
> 当前 Gödel 阶段：`EXTERNAL_NAT_PROOF_PREDICATE_AND_EFFECTIVE_CLASSIFIER_COMPLETE; UNIVERSALITY_AND_STRONG_REPRESENTABILITY_OPEN`
> 门禁：`MACHINE_PROVED_LOCAL_UNCOMMITTED`

## 1. 为什么先做 proof checker

Gödel 不完备性中的 `Prov_T(n)` 不是任意名为“可证明”的谓词。它必须来自一个有效呈现的对象理论，其具体证明对象可以
由有限程序检查。需要分开两项能力：

```text
check a supplied proof candidate
                    ≠
find a proof candidate or decide that none exists
```

本评价在 Cubical Agda 中闭合第一项，同时刻意不宣称第二项。

## 2. 对象理论

对象公式为：

```agda
data Fml : Type where
  atom : ℕ → Fml
  bot : Fml
  _⇒_ : Fml → Fml → Fml
```

indexed derivation `⊢ φ` 包含 Hilbert K、S 与 modus ponens：

```agda
data ⊢_ : Fml → Type where
  axK : (φ ψ : Fml) → ⊢ (φ ⇒ (ψ ⇒ φ))
  axS : (φ ψ χ : Fml) →
        ⊢ ((φ ⇒ (ψ ⇒ χ)) ⇒ ((φ ⇒ ψ) ⇒ (φ ⇒ χ)))
  mp : ⊢ (φ ⇒ ψ) → ⊢ φ → ⊢ ψ
```

这使 Agda 的类型索引本身保证 derivation 正确，却还不是一个从普通 code 接收输入的 checker。为此另定义无索引 `RawProof`；
它的 MP node 显式存储预期 antecedent/consequent，由 `check` 验证子树、结论形状与公式相等。

## 3. 公式相等检查

`eqNat`/`eqF` 是总 Bool 函数，并机器证明：

```agda
eqNat-refl  : (n : ℕ) → eqNat n n ≡ true
eqNat-sound : eqNat m n ≡ true → m ≡ n
eqF-refl    : (φ : Fml) → eqF φ φ ≡ true
eqF-sound   : eqF φ ψ ≡ true → φ ≡ ψ
```

checker soundness 因而不依赖“相等看起来明显”；每次 Bool 相等成功都转成 Cubical Path，再用 `subst` 把子 derivation 搬到
MP 所要求的精确公式。

## 4. Checker soundness 与 completeness

机器检查的 soundness 是：

```agda
check-sound : (p : RawProof) → check p ≡ true → ⊢ conclusion p

checkAgainst-sound : (p : RawProof) (φ : Fml) →
                     checkAgainst p φ ≡ true → ⊢ φ
```

反方向通过 `erase` 给出：

```agda
erase : ⊢ φ → RawProof
conclusion-erase : conclusion (erase d) ≡ φ
check-erase : check (erase d) ≡ true
checkAgainst-erase : checkAgainst (erase d) φ ≡ true
```

于是：

```agda
Checked φ = Σ[ p ∈ RawProof ] checkAgainst p φ ≡ true

derives→checked : ⊢ φ → Checked φ
checked→derives : Checked φ → ⊢ φ
```

这里证明了两个总函数，不声称 proof-relevant 类型在所有 Path 上等价。这个限制防止把“同一可证明命题的不同 proof tree”
提前压成无差别对象。

## 5. HoTT 的 provability 层

对象理论的“存在某个可检查 proof”定义为 mere proposition：

```agda
Provable φ = ∥ Checked φ ∥₁
```

并得到：

```agda
derives→provable : ⊢ φ → Provable φ
provable→mereDerives : Provable φ → ∥ ⊢ φ ∥₁
```

命题截断使“可证明性”不依赖具体选择哪一棵 proof tree。它也明确保留计算边界：从 `Provable φ` 不能用普通 truncation recursor
提取一个 raw proof，除非目标本身是 proposition。因而本包没有从 mere existence 构造 proof-search 程序。

## 6. 固定控制

`kRaw` 是一个 K-axiom raw proof，`checkAgainst` 计算为 `true`。`badMp` 把不具有预期 implication conclusion 的子树放入
MP node，`check` 计算为 `false`。两条控制均是文件内可归约的 machine-checked Path：

```agda
kRaw-checks : ... ≡ true
badMp-rejected : check badMp ≡ false
```

## 7. 证明门禁

| 项目 | 结果 |
|---|---|
| Sources | `MiniProofChecker.agda`、`ProofSerialization.agda`、`FormulaBitCode.agda`、`ProofBitCode.agda`、`NatProofCode.agda` |
| Claim specs | `CLAIM.md`、`SERIALIZATION_CLAIM.md`、`FORMULA_BITCODE_CLAIM.md`、`PROOF_BITCODE_CLAIM.md`、`NAT_PROOF_CODE_CLAIM.md` |
| Agda / Cubical | 2.8.0-3d04bac / v0.9 |
| Canonical runs | `20260914-CUBICAL-GODEL-PROOF-CHECKER-001`、`...PROOF-SERIALIZATION-001`、`...FORMULA-BITCODE-001`、`...PROOF-BITCODE-001`、`...NAT-PROOF-CODE-001` |
| Native result | 五包均 exit 0 / stderr 0 / `KERNEL_ACCEPTED_WITH_SCOPE` |
| Matrix | 五个 package row + 20 个 claim row；每包精确 rows frozen |
| Independent rerun | 五包均 `PASS_WITH_SCOPE`; exact index snapshot 和 exact exit/stdout/stderr match |
| Git | `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

## 8. 数值编码链已经闭合到哪里

后续四包没有假设一个抽象编码函数，而是逐层构造并证明它：

1. `ProofSerialization.agda` 把有限 raw proof tree 变成 postfix token list，并由显式 stack parser 往返解码；
2. `FormulaBitCode.agda` 给 `atom/bot/imp` 公式一个有限、自定界的 Bool code，证明带任意 suffix 的 parser 定理；
3. `ProofBitCode.agda` 给 K/S/MP token 加二位 tag，把公式 payload 改成位串，并用一元 token-count prefix 得到完全由 Bool 组成的 proof code；
4. `NatProofCode.agda` 定义 `codeBits : List Bool → ℕ`、总 `decodeProofNat : ℕ → Maybe RawProof` 与 `checkProofNat : ℕ → Fml → Bool`，证明 proof-code 往返、单射和 checker commutation。

最终得到：

```agda
codeProof-roundtrip : (p : RawProof)
  → decodeProofNat (codeProof p) ≡ just p

codeProof-injective : (p q : RawProof)
  → codeProof p ≡ codeProof q → p ≡ q

NatChecked φ = Σ[ c ∈ ℕ ] checkProofNat c φ ≡ true

natChecked-sound : NatChecked φ → ⊢ φ
derives→natChecked : ⊢ φ → NatChecked φ
```

所以，外部元理论中“一个自然数是否编码了 `φ` 的合格证明”现在是一个真正的总 Bool 关系；每个 derivation 都有数值 witness，任意被接受的数值 witness 都返回 derivation。这里仍没有对象语言内部的公式 `Proof_T(c, ⌜φ⌝)`，也没有证明该公式表示 `checkProofNat`。

本包还留下一个透明的计算成本观察。`ℕ` 在该 Agda 定义中是一元数据；将长位串解释成普通二进制数会生成指数大小的具体 unary term。最初以较大已编码反例作 `refl` 控制时，内核持续归约数分钟。把控制改为最小 K proof 和无效码 `0` 后，完整 `--ignore-interfaces` run 在约 19 秒内结束。数学定理未改变；该观察只说明具体表示与归约策略会影响 proof checking 成本，不能据此声称发散或不完备。

`NatProofCode.agda` 的 stdout 保留一项 Cubical Agda warning：自定义归纳关系上的 `≤-trans` 对 transport 输入不具有受支持的计算规则。本包只在普通自然数不等式证明中使用它，不把该函数用于 transport；warning 仍被保留在运行原件中，没有被隐藏。

### 8.1 从 checker 到穷举 proof/refutation classifier

`PF-CUBICAL-GODEL-PROOF-SEARCH-CLASSIFIER-001` 把自然数 checker 接到 synthetic incompleteness 的 `FormalSystem` 接口。Stage `n` 检查 code `n` 是否证明 `φ` 或 `negF φ = φ ⇒ bot`；全体 stage 因而穷举所有自然数 proof candidates。

这个连接额外机器证明了：

- K/S 在任意 Boolean valuation 下有效，MP 保持真值，因而 `bot` 不可导；
- `φ` 与 `negF φ` 不可同时导出；
- 每个 `proofCore` true/false 结果分别等价于对应 `checkProofNat` 接受；
- 即使成功结果出现在不同 code/stage，它们也不能相反；
- `proofClassifier φ ⇓ true ↔ ⊢ φ`，`proofClassifier φ ⇓ false ↔ ⊢ negF φ`；
- 当前 calculus 因而给出 `HilbertSystem : FormalSystem Fml negF`。

Canonical run `20260914-CUBICAL-GODEL-PROOF-SEARCH-CLASSIFIER-001` 使用两个显式 include directories，11 个 source-manifest files，exit 0 / stderr 0，5 行 matrix 冻结并 exact replay。它消去了条件性 synthetic theorem 的 effective-classifier 参数。它没有使分类器成为总函数：独立句正对应两个方向都没有成功 stage。

## 9. 与当前 ERCF3-T3 的关系

既有 `ObjectSyntax.agda` 给出 indexed `Prov` 接口，`RepairedSyntax.agda` 已给出可解码 formula coding、code-level substitution
和 diagonal-instance shape。然而 `ProvRepresentability.agda` 通过对象 derivation constructor `repr` 直接加入表示性 schema，
没有证明一个 raw proof checker 与该对象公式之间的算术表示定理。

本评价从另一侧补足：checker 真实执行、接受与 indexed derivation 双向连接，且没有用一个名为 `repr` 的 constructor 代替
证明。现在 `RawProof` 已获得可解码、单射的自然数编码，checker-code commutation 也已完成。两条线下一步应在**对象层表示性**处合并：要么扩展本包的对象语言使其具有足够算术，要么把本 checker 结构迁移到 ERCF3 的 repaired syntax，然后证明具体编码、替换和 checker 函数由对象公式表示。

## 10. 尚缺的 Gödel 义务

| 义务 | 状态 |
|---|---|
| 对象语法 | `DONE`（小型 propositional fragment） |
| 给定 proof 的 decidable checking | `DONE` |
| checker 与 indexed derivation 双向连接 | `DONE` |
| formula 的自定界 finite Bool coding | `DONE` |
| raw proof 的自定界 finite Bool coding | `DONE` |
| raw proof 的可解码、单射 Nat coding | `DONE` |
| Nat checker 与 raw checker commutation | `DONE` |
| proof candidates 的自然数域 | `DONE`（每个 `c : ℕ` 可总检查，每个 derivation 有 code） |
| proof/refutation 的 step-indexed exhaustive classifier | `DONE`（`HilbertSystem : FormalSystem Fml negF`） |
| direct formula Nat code / formula enumeration interface | `OPEN`（generic `codeBits` 可复用，但尚未封装和索引为本包定理） |
| 足够算术表达力 | `OPEN` |
| substitution/checker 的对象层表示性 | `OPEN` |
| diagonal lemma | `OPEN` |
| Gödel/Rosser sentence | `OPEN` |
| unprovability/incompleteness theorem | `OPEN` |
| exact HoTT calculus 自身实例 | `OPEN` |

这张表防止把基础设施的多个“已完成”误写成不完备性定理已经完成。

## 11. 下一步

下一最小包不再重复外部编码或 classifier，而应固定一个足够算术的对象语言，并证明 universal self-return predicates 的 strong representability。最低接口是：

```text
RepCodeFormula(x,y)  represents y = codeFormula(x)
RepSubstitution(x,n,y) represents y = substCode(x,n)
ProofRel(c,f)        represents checkProofNat c (decodeFormula f) = true
Prov(f)              = ∃ c, ProofRel(c,f)
```

在这些对象层表示定理成立以后，才构造 substitution-aware fixed point，并按选定的 Gödel 或 Rosser 路线证明 unprovability。若最终主张指向 HoTT 本身，还必须把对象理论换成一个精确、有效呈现的 HoTT calculus，并证明前述元定理的全部假设由该 calculus 满足。现实相对结论则继续等待独立的同任务、同输入、同观察量和同完成标准桥梁。
