# Z0-D3 · Foundation 全量源码包

给上一个 feedback 的补充。它说"如果你能把 Foundation 里的 D3.lean、R0/Basic.lean、CraigTrick.lean、
Proof/Typed.lean 和缺的 20 个模块也给我"——**这个包把导入闭包里全部 167 个 Foundation 模块都给上了**，
一个不缺。

## 1. 自验（不需要 Lean）

```bash
python3 verify_coverage.py
```

实测输出：

```
Foundation closure modules : 167
Foundation source files     : 169
MISSING                     : 0
project modules hash-ok     : 24
project modules mismatch    : 0
project modules not pinned  : 3  (Z0Blocked / Z0Bridge / Z0Probe - all carry unproved markers)
RESULT: COMPLETE
```

它自己算出的 140 个缺失清单（第一档 19 / 第二档 77 / 第三档 44）**全部在包内**，另附旧包里那 29 个
它没数到的（`DerivabilityCondition/D{1,2,3}.lean`、`PeanoMinus.lean`、`EquationalTheory.lean`、
`R0/{Basic,Representation,Independence}.lean`、`LK/*` 9 个、`Tarski/HierarchicalDefinability/*` 3 个、
`Definability/*` 5 个、`Syntax/Classical/BoundingHierarchy.lean`）。

包内 169 个 = 167（闭包内）+ 2 个闭包外（`R0.Independence`、`LK.ForcingInterpretation`，
这两个正是它指出不在闭包内的，保留无害）。

## 2. 结构

```
Z0-D3-Foundation全量源码/          201 个文件，3.5M
├── README.md                    本文件
├── verify_coverage.py           自验脚本，不需要 Lean
├── Foundation/                  169 个 .lean（2.6M）—— 真正的 Foundation 源码树
├── 项目模块/GodelQ/              27 个 .lean（736K）—— 本项目的全部模块
│   ├── LEAN_TOOLCHAIN.json      pinned Lean 4.34.0 (commit 293d5d0c)
│   └── MATHLIB_CLOSURE.json     1893 模块导入闭包 + 聚合 SHA-256
└── 收据/
    ├── W8-source-manifest.json  30 个源文件 SHA-256 + 553 个外部依赖
    ├── W8-stdout.txt            112 条 #print axioms 原始输出
    └── W8-RUN.json              运行元数据（scope、non_goals、时长）
```

## 3. 关于缺的 1893 个模块

`项目模块/MATHLIB_CLOSURE.json` 里 1893 个条目 = 167 Foundation + 1726 Mathlib/deps。
**本包只给 Foundation 那 167 个源码**，Mathlib 的 1726 个 `.lean` 没有给（太大，十几 GB 级；
而且它们是上游，版本由 `mathlib_source.commit = 5ed29652…` 锁定）。

如果要在没有构建树的情况下验证，`收据/W8-source-manifest.json` 的
`external_dependencies`（553 项）钉住了每个 `.olean` 的字节数与 SHA-256，但那是构建产物不是源码。
**结论不变：沙箱里没有 Foundation/Mathlib 构建树，就只能做源码分析，不能编译。**

## 4. 编译次序（24 个本项目模块，如果要试）

见 `../Z0-D3-攻关包/收据/BUILD.md`，那里列了 24 个模块的依赖次序。
最后一个 `ZFC/Z0Blocked.lean` 是要改的（第 35 行 `sorry`）。

## 5. 缺口位置（按它的定位，我 README §4 已作废）

它重新定位的缺口，我核实后认同：

```lean
-- 对 Σ1 句 σ：V ⊧ σ → TrProvable ⌜σ⌝   （目标取 σ := zfcTr τ，用 zfcTr_sigma1）
```

路径：对显式的 Σ1 定义 `trProv` 做 Craig 化得 T'，则 `V ⊧ σ → Provable T' ⌜σ⌝` 直接得到；
缺反方向 `Provable T' x → TrProvable x`，即在 V 里对任意算术 Tait 推导归纳、
把每条规则翻成 𝗭𝗙𝗖 推导。这就是 `of_provability` 靠完备性语义做掉、却搬不进 𝗜𝚺₁ 的那一步。

对应本包的源码位置：

| 要写的东西 | 对应的既有模板（本包内） |
|---|---|
| Tait 推导的规则清单 | `Foundation/.../Bootstrapping/Syntax/Proof/Typed.lean`（640 行） |
| `theta(φ[t])` 与 `exists y (varEq_t y ∧ theta φ y)` 的 𝗭𝗙𝗖 内等价 | `.../Bootstrapping/Syntax/Formula/Functions.lean` 的 `subst_*` 系列 + `InternalTranslate.lean` 的 `iT_quote` |
| 项的全性 `exists! y ∈ ω, varEq_t(y)` 对 t 归纳 | `.../Bootstrapping/Syntax/Term/Functions.lean` + `项目模块/GodelQ/ZFC/InternalTranslate.lean` 的 `iVE_quote` |
| Craig 化的 𝚫ᴬ₁ 构造 | `.../Bootstrapping/Syntax/CraigTrick.lean`（342 行） |
| ω 对加法乘法封闭 | `DerivabilityCondition/EquationalTheory.lean`（547 行）+ D1 |

## 6. 我坚持的一条更正

它说"Foundation 的 `sigma_one_complete` 要 Δ1 表示的算术理论"——这条对，但要补一句：
`DerivabilityCondition/D3.lean:170` 的 `sigma_one_complete` 前提是 `[Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T]`，
而 Craig 化后的 T' 满足 `[T'.Δ₁]`（这正是 `CraigTrick.lean:220` 的
`Theory.IsCraigAxiom.defined` 实例所给），但 `[𝗣𝗔⁻ ⪯ T']` **未必**自动成立——
Craig 化通常保持定理集，所以若 `𝗣𝗔⁻ ⪯ T` 则 `𝗣𝗔⁻ ⪯ T'`；这一条要先确认而不是假设。
