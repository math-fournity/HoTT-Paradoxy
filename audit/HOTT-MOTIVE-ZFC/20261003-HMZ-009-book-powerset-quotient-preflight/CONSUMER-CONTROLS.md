# HMZ-009：Power Set quotient 的 consumer / payment 对照

## 候选共享任务

| 字段 | Book 所支持的最小表述 | 当前来源状态 |
|---|---|---|
| `u` | 一个 set \(A\) 与其 equivalence relation \(R\)。 | `SOURCE_REPORTED`，但不是 Book 所给的 ZFC object-language encoding。 |
| `F_Z` | 以 \(\mathcal P(A)\) 的子集表出 equivalence classes。 | `CONSTRUCTION_BRIDGE_PARTIAL`：Book 给数学描述；Metamath/Shulman给 formation-level controls。 |
| `F_HoTT` | `A/R` 的 set-quotient，或 predicates \(P:A\to\mathsf{Prop}\) 的 \(A\sslash R\)。 | `SOURCE_REPORTED`。 |
| `C` | Book 叙述一种 quotient construction。 | `SOURCE_DESCRIBED_CONSTRUCTION_ONLY`；没有独立、版本固定的 ZFC actual consumer。 |
| `I/O/Done` | Input：\(A,R\)；operation：形成等价类／quotient；output：a quotient; Done：得到可与 set-quotient 对照的 quotient construction。 | quotient-style output 可定位；但没有一个 ZFC consumer 自己声明的 observation/Done。 |

## P / 同一任务审查

```text
P1 L0 (theory-internal object): PARTIAL
  A,R and a quotient occur in a mathematical construction, but the source does
  not present their bare-ZFC object-language declaration.
P1 L1 (formation): PARTIAL
  Power Set / subset formation is source-traceable, not an uninspected “all at once”.
P1 L2 (actual consumer): FAIL_FOR_Q_ADMISSION
  Book exposition is not the required independent ZFC consumer contract.
P2 Bind/Form/Bridge/Reenter: NOT SUPPLIED
  The sources describe formation and comparison, not a same-object negative reentry.
P3 pending/admission/operator/Done: NOT SUPPLIED
  No source says that an as-yet-unformed quotient or Power Set is used to validate
  its own formation, nor supplies a corresponding lifecycle.
same task: PARTIAL
  Both sides concern quotient-style output; source does not preserve H0's higher
  sameness subject/process/observation/Done.
```

## 明示 payment / 控制

| 控制 | 来源事实 | 对当前 Q 的作用 |
|---|---|---|
| `C+`：Power Set 与 subset formation | Metamath/Shulman 明示 Formation rules；Book明确使用 Power Set-subset construction。 | 不能把“有一个 Power Set”本身改写成尚未支付。 |
| `C+`：universe / resizing | `hits.tex:1295–1297`、`setmath.tex:363–367`。 | Book不把 class construction的universe代价藏掉。 |
| `C−`：external versus internal quotient | `setmath.tex:487–499`。 | 两种 construction route 的交付条件不同，不能强作同一 P-facing Done。 |
| `C−`：HoTT 内部 \(V\) | `setmath.tex:1755–1761`。 | HoTT model of ZFC的 Power Set 不是 bare ZFC-side problem。 |

## 反事实与重开

本预检的状态会在且仅在下列情形改变：找到一手、版本固定的 ZFC／集合论实践或形式化来源，其中同一 \(A,R\) quotient 任务有明确 `C/I/O/Done`，并能检验该 consumer 是否在其 Power Set、Separation、representative、universe 或其它 formation payment 尚未落定时，已经把同一对象交给后续判断／算符。一个仅说明 quotient 存在、Power Set 可形成或 HIT 更方便的来源不改变本卡。
