# C0B4：Metamath set.mm 的 object-level ZFC 连续统／级数子理论盘点

> **身份：** `C0B_INDEPENDENT_FORMALIZATION_INVENTORY / SOURCE_REPLAYED_EXTERNAL_FORMAL_THEOREM / NOT_A_CORE_VERDICT`。
>
> **TaskCard：** [C0B4](ZFC-META-SUBTHEORY-ADEQUACY-001-C0B4-TASKCARD.md)。
>
> **判词：** `SETMM_OBJECT_LEVEL_ZFC_FOUNDED_GEOMETRIC_S_FOUND / IEP_TO_SETMM_PROMOTION_UNPAID / C0B4_LOCAL_LEAF_CLOSED`。

## 1. 冻结的来源身份

| field | fixed evidence |
|---|---|
| database | `metamath/set.mm@160ebb63ec17ff00a809520a420c92914a424622`，raw `set.mm` SHA-256 `d8420798…d5026b2a`，51,466,065 bytes。 |
| source location | 外置、用户已保存的只读 cache `/Volumes/D/HoTT-downloads/godel-q-setmm-160ebb/set.mm`；其身份由已有 [20261004 source replay receipt](../HoTT/verification/runs/20261004-SOURCE-REPLAY-SETMM-OBJECT-CODING-001/RUN.json) 与 manifest 固定。 |
| axiom base | source在 `ZF (ZERMELO-FRAENKEL) SET THEORY` section明示ZF构造；同文件 `ax-ac`注释明示加入Choice后为ZFC。这里的 M 是该数据库的 ZFC-founded object-theory context；本卡不断言每一条分析 theorem最小依赖于Choice。 |
| verifier evidence | 本轮 [20261005 source replay](../HoTT/verification/runs/20261005-SOURCE-REPLAY-SETMM-GEO-LIMIT-001/RUN.json)以同一raw source和fixed `metamath-exe@9898f5d…`重新验证全部47,917条 `$p` proofs（exit 0），随后输出`geoihalfsum`的axiom traceback；该实物只证明固定数据库的proof check，不自动变成 P/Q/Bridge。 |

## 2. 实际 object-level S

冻结 source 的 analysis section给出以下对象层资产：

| label / definition | source-level content | C0 字段 |
|---|---|---|
| `df-rlim` / `rlim` | 以实数 epsilon-style条件定义函数的实意义极限。 | real-limit language。 |
| `df-sum` | 对上整数索引集，用 partial sums的limit定义无限和。 | series / FormalDone machinery。 |
| `df-seq` | 将输入 `1, 1/2, 1/4, 1/8,…`变为 partial sums；source comment明说这类sequence趋于2的说明。 | sequence representation。 |
| `geoihalfsum` | theorem：`sum_ k e. NN ( 1 / ( 2 ^ k ) ) = 1`；它是与用户半程级数最接近的固定 object-level theorem。 | geometric-series `FormalDone` candidate。 |

因此，与 C0B2/C0B3不同，当前 `set.mm` 版本**确实**给出可准入的 object-level S；这不是网页目录或 generic proof acceptance。上述 `geoihalfsum` 的精确 proof属于本轮全库 verifier replay覆盖的范围。

## 3. 仍未支付的字段

| core field | current status | reason |
|---|---|---|
| `Q_model` / exact FormalDone mapping | `PARTIAL` | `geoihalfsum`给 infinite series value；仍须C2B4逐字段比较它与C2C的`remaining`／partial-sum model。 |
| `Q_physical` | `UNPAID` | source没有 runner/path/time physical target contract。 |
| `P` | `UNPAID` | 本次 current IEP page search对 `Metamath`、`Mizar`、`formalization`均无文本命中；这只说明该固定页面不消费这些 formalizations，不主张历史上绝无其他 consumer。 |
| `Bridge/Adequacy` | `UNPAID` | object-level theorem不自动说明物理运动或user finite-stage Done。 |

这一步严格区分两种看起来相近的事：`set.mm` database verifier接受proof，和`geoihalfsum`作为**对象层数学 theorem**存在。前者继续是控制；后者才是F-B可继续检验的 S。

## 4. 自动后继

进入 **C1B4：set.mm M→S foundation relation and theorem-dependency card**，随后才可 C2B4 逐字段审计 `geoihalfsum` 与 user/C2C Q 的 model fidelity。没有 IEP-to-set.mm P 时，C3B4必须明确关闭该 promotion route，不能以同一几何级数文字跳过。
