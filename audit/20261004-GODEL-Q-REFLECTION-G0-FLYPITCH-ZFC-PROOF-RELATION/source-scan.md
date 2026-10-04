# Flypitch source scan：proof reflection 与哥德尔式 self-reference 的边界

> 固定 source：`flypitch/flypitch@d72904c17fbb874f01ffe168667ba12663a7b853`。
>
> 身份：`SOURCE_INSPECTION_DERIVATIVE / NOT_A_KERNEL_REPLAY`。

本扫描只澄清 current source 中几个容易被名字误导的结构；它不改变该项目尚未在本机用 Lean 3.4.2 重放的事实。

## 检查的 source 事实

| 位置 | 实际对象 | 对 GODEL-Q 的含义 |
|---|---|---|
| `src/fol.lean` | `fol.prf Γ f` 是 Lean 中的 proof tree；`sprovable T f := Nonempty (T ⊢ f)`；`substitution` 将一个**已给的 Lean proof**运输到代换后的公式。 | 给出 M 层 syntax/proof/substitution；未给对象理论内部的 `Prov_T`。 |
| `src/fol.lean` | `reflect_prf_lift1` 从 lifted-context proof 通过 substitution 得到原公式 proof。 | 这是 host proof 的 lifting inversion，不是“理论证明自身可证明性”的反射，也不是 diagonal fixed point。 |
| `src/parse_formula.lean` | `has_reflect` 和 quotation syntax 用于 Lean meta elaboration，把宿主值转成 Lean expressions。 | 是 Lean meta-level reification helper；不能冒充 ZFC 内 quotation。 |
| `src/summary.lean` | 唯一包含 `godel` 字样的 current theorem 是 `godel_completeness_theorem : T ⊢' ψ ↔ T ⊨ ψ`。 | 这是 source 命名的 Gödel completeness theorem；它不是 incompleteness、Gödel numbering、quote 或 fixed point。 |
| `old/` | 包含早期 reflection experiments。 | 历史源文件不属于 `src/` current proof path，不能替 current ZFC proof relation 支付对象层义务。 |

## 有界搜索结果

在 `src/` 与 `old/` 上冻结搜索 `gödel|godel|quote|quotation|arithmeti[sz]|diagonal|fixed.?point|self.?ref|reflect|provability predicate|proof predicate`。结果包含以上的 proof-lifting、Lean meta reflection、Gödel completeness 名称和历史实验；未出现一个当前 source 中可定位的 `Formula/Proof → Nat` Gödel numbering、ZFC 内 provability predicate、对象层 quotation 或 fixed-point theorem。

这里的“未出现”只覆盖这个 commit、这些关键词和已审读的 source 角色。它不证明 Flypitch、其他版本或数学上不存在可用编码。

## 结论

Flypitch 是一个比外部字符串 checker 更强的 M 层 ZFC syntax/proof-relation control，却仍没有达到 GODEL-Q 的 target-specific G2：它不能把 `reflect`、`substitution` 或 `godel_completeness_theorem` 误读成 ZFC 对自身 proof relation 的算术化与自指。parent `OriginDone`／`ρ`／bridge 仍没有 source owner。
