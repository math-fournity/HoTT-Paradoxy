# GZ-005：cctt 的受限输入域 R4 资格化

本包检验一个版本固定的 Cartesian Cubical Type Theory 实现，能否为
`R4-HOTT-CALCULUS-BRIDGE-001` 提供**受限的对象层 checker 输入域**。它
不把 cctt 的一般 checker 成功等同于逻辑证明，也不将 cctt 本身当成
Gödel `Prov_T` 的实现。

## 固定目标

- 上游：`AndrasKovacs/cctt@3695c69efbd5e4cbb4b92a8980f5cdae9874072a`；
- 特征：Nat、Path、`Glue`、`coe`、`hcom`；
- 上游 checker：由 `stack --system-ghc build` 构建的 `cctt`；
- 受限接口：

```text
ClosedProofAccept_cctt(source) :=
  RestrictedProfile(source)
  ∧ cctt CLI finishes
  ∧ its output contains no upstream ERROR diagnostic
  ∧ its output contains a checked-definitions marker
```

`restricted_profile.py` 先去除注释和字符串，再拒绝 hole、`undefined`、
import，以及本地 top-level definition 图中的环。它是透明的项目筛选器，
不是 cctt parser、termination checker、semantic model 或 proof kernel。cctt
命令的 exit status 也不是本包的充分验收 oracle，因为当前冻结版本的 CLI
会在打印类型 `ERROR` 后返回 0；本包显式检查其诊断文本。

## 对照

| 文件 | 上游 checker 的预期 | 受限 profile 的预期 | 用途 |
|---|---:|---:|---|
| `Positive.cctt` | 无 `ERROR` 诊断，且出现检查完成标记 | 接受 | Nat、Path、Glue、`coe`、`hcom` 正控制 |
| `Hole.cctt` | 无 `ERROR` 诊断，且出现检查完成标记（由实际 run 核验） | 拒绝 | 证明诊断成功不能单独充当封闭证明 |
| `Recursive.cctt` | 无 `ERROR` 诊断，且出现检查完成标记（由实际 run 核验） | 拒绝 | 证明未终止 top-level recursion 必须在接口外排除 |
| `TypeError.cctt` | 有 `ERROR` 诊断 | 可通过结构筛选 | 证明 profile 不冒充 typechecker；CLI 仍可能返回 exit 0 |

`Recursive.cctt nf loop` 的固定两秒观察窗仅报告本次正常化观察是否完成；
它不证明一般的“永不终止”。

## 非结论

本包不会证明：cctt 的全体输入都可终止、cctt 是完整 HoTT calculus、其
rules 可有效编码为对象层证明谓词、Gödel 固定点在 cctt 内成立，或 bare
ZFC 的理论精度存在缺失。它只给 G1/R4 后续对 `Accept` 领域的一个受限、
可复现输入合同。
