# GZ-008：来源对应 cubical proof-code fragment

> **身份：** `ROUTE_UNIT_RECORD / GODEL-ZFC-CONVERGENCE-SOP / G1-R4`。
>
> **状态：** `LOCAL_CLOSED_WITH_SCOPE / GZ-009_SUCCESSOR_REQUIRED`。

## 1. Parent gap

GZ-007 已证实不能把 cart-cube 的 semantic model、redtt 的 executable core 和 TTasQIIRT 的
intrinsic syntax 拼成一个未实际存在的 full HoTT proof relation。当前可以诚实推进的下一步是：
构造一个**项目定义但 source-corresponding**的最小 fragment，明确证明其中哪一个 Gödel前提已经
成为机器对象，哪些仍没有。

## 2. 冻结 fragment `CCTTmini₀`

```text
Ty    ::= Nat | Path Ty Tm Tm
Tm    ::= var Nat | zero | suc Tm | refl Tm
Ctx   ::= finite list Ty
Cert  ::= varC Nat | zeroC | sucC Cert | reflC Cert
```

`Cert` 是 closed proof-certificate syntax，`erase : Cert → Tm` 忘掉 certificate 层，
`infer : Ctx → Cert → Maybe Ty` 必须只按 `Cert` 结构递归。其成功结果的 soundness theorem 必须给出
一个明确 `HasType Ctx (erase cert) ty` derivation。

## 3. 真实 source correspondence 与限定

| `CCTTmini₀` 结构 | redtt/cctt source 对应 | 本单位不声称 |
|---|---|---|
| `Nat`, `zero`, `suc` | redtt `data nat`/`suc`、cctt `inductive Nat`/`suc` | 完整 natural-number eliminator 或 arithmetic representation |
| `Path`, `refl` | redtt `path`/`refl`、cctt `Path`/`Refl` | cubical composition / conversion correctness |
| explicit `Cert` | 两者都**未**给这个 certificate object；本项目新增 | 这是 upstream 的 actual proof relation |
| structurally recursive `infer` | upstream checker 的有限、透明 fragment analogue | full checker totality或 soundness |

不含：universe、Π/Σ、`Glue`、`coe`、`hcom`、HIT、univalence、general substitution、
definitional equality、top-level recursion、holes、imports、meta variables。这些缺失必须被每一个
后续引用保留。

## 4. 冻结 machine targets 与 controls

1. `infer-sound`：`infer Γ c ≡ just A → HasType Γ (erase c) A`；
2. `positive-path`：给定 Nat context，`reflC (sucC (varC 0))` 产出预期 `Path Nat ... ...`；
3. `ill-scoped-negative`：空 context 的 `varC 0` 得到 `nothing`；
4. `wrong-suc-negative`：对 `reflC zeroC` 使用 `sucC` 得到 `nothing`；
5. `no-hole-no-recursion-by-construction`：`Cert` constructor set 中不存在 hole 或 recursion case。

这五项若由 kernel 检查，只能得到 `HOTT_GODEL_BRIDGE_FRAGMENT_MACHINE_PROVED` 的**fragment**
版本。它没有 `Nat` 值 Gödel编码、quotation/diagonal、proof predicate representability、independence
theorem、fixed H0 transport 或 bare-ZFC conclusion。

## 5. Required successor

成功后必须进入 `GZ-009 / R4-CCTTMINI-NAT-CODING-001`：定义 certificate 的总 Nat coding/decoding，
证明 image roundtrip，并对 malformed codes 给出明示 fallback；只有那一步才可讨论 quotation 与对角
substitution在 code 层的前提。若 GZ-008 无法在冻结 Agda toolchain 中机器检查，必须记录 exact syntax/
toolchain failure，并切换到 Lean structural control；不得直接把手写规格叫作 machine proof。

## 6. 实现与 machine evidence

实现位于 `HoTT/formal/cubical-godel-fragment/`，主命题及范围见 `CLAIM.md`。`CCTTmini.agda`
使用 `--safe --cubical`，固定以下可见对象：

```text
Ty / Tm / Ctx / Var / RawCert / Deriv / Checked
lookup / erase / check / accepts
positiveAccepted / positiveWitness / illScopedRejected / wrongSucRejected
checkedSound / checkSound
```

主 run
[`20261005-MP-CUBICAL-GODEL-FRAGMENT-001-02`](../HoTT/verification/runs/20261005-MP-CUBICAL-GODEL-FRAGMENT-001-02/RUN.json)
在固定 Agda 2.8.0-3d04bac 上 exit 0、stderr 0。它的 negative companion
`...NEG-001-02` 使用 `WrongCCTTmini.agda`，把被接受的正例要求为 `false`，在
`true != false` 处以 exit 42 被拒绝。

generic `verify_formal_proof_run.py --rerun` 已给出 `PASS_WITH_SCOPE` 与
`EXACT_EXIT_STDOUT_STDERR_MATCH`。C-370--C-374 的具体 kernel claims 和非目标已经追加到
`HoTT/CLAIM_EVIDENCE_MATRIX.md`。

### 收据合同修复

首次 `...-001-01` capture 的内核运行本身成功，但 `command_argv` 使用了绝对 proof-source
path；`verify_proof_version_closure.py` 正确拒绝其为 `LATER_COMMAND_SOURCE_MISMATCH`。这只是
版本闭合合同错误，不是 CCTTmini theorem 的反例。capture procedure 随后改为在 `cwd=repo root`
下记录项目相对 source path，并生成 `...-001-02` / `...NEG-001-02`。前一轮未提交生成物不进入
证据谱系；`-02` 是唯一候选 primary receipt。

## 7. 局部判词

```text
HOTT_GODEL_BRIDGE_FRAGMENT_MACHINE_PROVED_WITH_SCOPE
CERTIFICATE_TO_DERIVATION_SOUNDNESS_MACHINE_PROVED
FINITE_FRAGMENT_ONLY_NO_NAT_GODEL_CODING_YET
```

这一步的价值在于把“checker 接受”升级成可在类型中取回的 derivation witness；它仍没有让
`CCTTmini₀` 变成 full HoTT 或一阶算术 theory。

## 8. Required successor

GZ-009 保持本文件的 fragment、source correspondence 和 scope，不增加语言结构；只新增：

```text
RawCert ↔ Nat total coding/decoding
image roundtrip and malformed-code fallback
code-level quotation/substitution preconditions
```

随后才能讨论该 fragment 是否承受 Gödel式 diagonal shape。P/Provable representability、reflection、
independence、H0 transport、actual ZFC acceptance 和 Q attribution 仍是更高层未支付义务。
