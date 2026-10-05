# G0/G2：`mm-lean4` 的 M 层 checker implementation 控制

> **方案：** `GODEL-Q-REFLECTION-SOP`。
>
> **身份：** `RUNTIME_OBSERVED_WITH_SCOPE / META_ONLY_CHECKER_CONTROL / NONCANONICAL_TOOLCHAIN / NOT_A_GODEL_THEOREM`。

> **判词：** `META_ONLY_CHECKER_IMPLEMENTATION_SOURCE_IDENTIFIED / NONCANONICAL_POSITIVE_AND_NEGATIVE_RUNTIME_CONTROL / NO_G2_TOTALITY_SOUNDNESS_OR_T_INTERNAL_PAYMENT`。

## 1. 为什么检查这个 source

G0 已冻结 `set.mm` 的真实 proof-acceptance interface，但 G2 仍需要区分三件事：

1. 一个实际 checker program 的存在；
2. 对所有有限 input 的 termination／checker correctness theorem；
3. 该 checker 或其 proof relation 在 `T = set.mm`／ZFC 内可表示。

`digama0/mm-lean4` 是一个值得检查的 M 层控制，因为它是用 Lean 4 写成的 Metamath verifier，并且 README 直接给出检查 `set.mm` 的 command-line path。它不是当前目标的 `T`，也不会因“用 Lean 写”自动获得 correctness theorem。

## 2. 固定 source 与实际运行

| 字段 | 固定值 |
|---|---|
| source | `https://github.com/digama0/mm-lean4` |
| commit | `58123caf246f4d7afc903d8a749512449bef75c1` |
| declared toolchain | `leanprover/lean4:v4.26.0-rc2` |
| actual toolchain | `leanprover/lean4:v4.26.0` |
| source checker | `Metamath/Verify.lean` 的 `partial def check (fname : String) : IO DB` |
| positive input | `demo0.mm` from `metamath/set.mm@160ebb63…`，SHA-256 `72ed7400…` |
| negative input | 仅将 `a2` 的结论由 `t` 改为 `r`，保持 `th1` proof，SHA-256 `7fc1c309…` |

实际命令及原始输出由 [run receipt](20261004-GODEL-Q-REFLECTION-G0-MMLEAN4-META-CHECKER/RUN.json) 持有：

```text
build:    exit 0, 9 Lake jobs completed
positive: exit 0, "verified, 29 objects"
negative: exit 1, th1 的 substitution/typecode error
```

## 3. 这组控制支付和不支付什么

| GodelizationCard 项 | 结果 | 原因 |
|---|---|---|
| `M` 层 actual implementation | `RUNTIME_OBSERVED_WITH_SCOPE` | 某个固定 Lean source 在实际稳定版 toolchain 上构建并区分一正一负 input。 |
| `Check` 的全称终止性 | `NOT_PAID` | source 使用 `partial def check`；这不是 termination theorem。 |
| checker semantic soundness | `NOT_PAID` | Lean typechecking program 不等于已证明“accept → Metamath/ZFC proof sound”。 |
| `T` 内 `Proof_T` / `Prov_T` | `NOT_PAID` | source 是 M 层 executable program；没有把 relation 内部化到 `set.mm`/ZFC。 |
| quotation / substitution / fixed point | `NOT_PAID` | 没有对应 object-theory theorem 或 diag construction。 |
| parent `OriginDone / ρ / Bridge` | `NOT_APPLICABLE_TO_THIS_CONTROL` | proof-checking task 与 Zeno/circle/H0 process 不同。 |

## 4. 工具链边界

该 repo 指定 RC2。首次按照其 `lake build` 路径运行时，elan 开始请求 `v4.26.0-rc2`，但本机没有得到可执行 binary。随后使用本机已有的 `v4.26.0` 正式版完成兼容性 build/run。

因此这不是 exact-toolchain replay，也不是对 upstream 声明“10 秒可完成 `set.mm`”的本机复验。若将来需要把此 verifier 本身作为强证据，必须在 exact RC2 环境重建，并另行证明或来源支付其终止性和 soundness；即便那样，它仍不自动提供 parent process completion bridge。

## 5. 对 G0 的影响

此控制让 G0 的来源图更精确：`set.mm` 不是只有文字 policy，还有可定位的 Lean-written checker implementation。它没有消除 G0 的真正缺口：同一 source owner 尚未将 formal proof acceptance 与芝诺／圆环／fixed H0 的 `OriginDone` 接到一起。

下一项仍然是寻找统一 source consumer，而不是围绕该 checker 重复制造更复杂的 meta fixture。
