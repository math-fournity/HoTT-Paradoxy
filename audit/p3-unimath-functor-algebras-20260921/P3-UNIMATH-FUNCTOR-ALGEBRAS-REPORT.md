# P3-UNIMATH-FUNCTOR-ALGEBRAS-001：实际 SIP 消费者与圆环强完成的有界审计

> 状态：`NO_K_WITHIN_UNIMATH_FUNCTOR_ALGEBRAS_DENOMINATOR / VERSION_PINNED_SOURCE_INSPECTED / NO_NEW_MATHEMATICAL_CLAIM`。
> 分支：P3，实际消费者 `K_app`。
> 分母：UniMath `ab5f5395fbcfda0b7cb9cbc5bfcb88c4ed9ef8ab` 的 `CategoryTheory/DisplayedCats/SIP.v` 与 `Examples.v` 中 `functor_algebras` 段。
> 任务：该真实 SIP 使用点是否只用 bare H/U，却把它作为 P1 圆去点—闭图—复原任务的同一 `Done_s`？

## 1. 启动凭据、学术检查与本地资产侦察

P1 已固定 `R_min = Input + CurveData + Denotes/Satisfies + O + D`；P2 已在 Book §9.8 分母中排除规则级桥。P3 因此不能再检查书中的一般 SIP，而必须选一个真实、版本固定的库调用点。来源冻结在 `P3-UNIMATH-FUNCTOR-ALGEBRAS-SOURCE-FREEZE.json`；它记录公开 `git ls-remote` 的 master HEAD 和两个 immutable raw-source URL/sha256。

| 已有资产或来源 | P3 判定 | 为什么没有替代本分母 |
|---|---|---|
| ABX `D_ABX_2` 的 29 个本地直接消费者 | `NEARBY_ONLY` | 它只覆盖本项目 `hott-z` 的圆/区间 import 图；没有 UniMath Rocq displayed-category 源码 |
| ABX `D_ABX_3` 与 P2 Book §9.8 | `NEARBY_ONLY` | 它们审计理论规则，不是外部库中的实际调用点 |
| 本地 `SIPRepresentation` / C-124–C-128 | `PARTIAL_REUSE` | 它是已机器检查的 Bool 点结构正控制，没有真实外部 library consumer 或 P1 的 `Done_s` |
| N5 的 D1–D5、N10、agda-unimath N42 | `NEARBY_ONLY` | 分别覆盖 partiality/cost/工具链和另一份 Agda 库；不覆盖 UniMath 的 displayed categories 或这两个固定文件 |
| UniMath `SIP.v` 的 `is_univalent_disp_from_SIP_data` 被 `Examples.v` 的 `is_univalent_disp_functor_alg` 调用 | `NEW_VERSION_PINNED_CONSUMER_DENOMINATOR` | 这是本 wave 的真实调用链：具体 functor-algebra 结构定义 → SIP helper → displayed category 的 univalence 性质 |

公开文档也确认 `SIP.v` 是“HoTT Book chapter 9.8 的短证明”，并列出 `P`、`H`、`Hid`、`Hcomp`、`Hstandard` 为显式变量；`Examples.v` 把 displayed categories 说明为构造结构对象范畴的工具。这个社区检查支持选择该分母，但不把文档标题或导入本身当作 K。

## 2. 冻结调用链实际做什么

固定 `Examples.v` 的第 330–397 行在任意 category `C` 和 functor `F : C → C` 上定义：

```text
functor_alg_ob(c)     := F c --> c
functor_alg_mor(a,a',r) := (#F r) · a' = a · r
disp_cat_functor_alg  := disp_struct ... functor_alg_mor ...
is_univalent_disp_functor_alg := is_univalent_disp_from_SIP_data ...
```

同一 commit 的 `SIP.v` 第 27–68 行要求 `P`、每个 `P x` 的 set 条件、`H`、其命题性、`Hid`、`Hcomp` 和 `Hstandard`，并只给出：由这些明确条件构成的 displayed category 是 univalent，及其 total category 是 univalent。

所以这是一个**真实外部 consumer**，但它消费的是明确给出的 `functor_alg_mor` 结构保持等式，得到的也是范畴论性质 `is_univalent_disp`。它没有接收或生成 P1 的 `RichCurve`、`Input`、闭图观察、`Denotes`、`CurveRun`、`AmbientStep`、`Done_w` 或 `Done_s`。

## 3. 对 P1 强任务的逐项判定

| P1 义务 | UniMath 固定调用是否承诺 | 依据 | P3 判断 |
|---|---|---|---|
| bare carrier H/U | 否；输入是 `C`、`F`、代数对象和明确 `functor_alg_mor` | `Examples.v` 334–347；`SIP.v` 27–38 | 不存在“只拿 bare carrier”的入口 |
| 来源/闭图 `CurveData` 与 `Denotes` | 否 | 函子代数的结构字段是 `F c → c` 与交换方程 | 未消费 P1 来源/观察；不能冒充同任务 |
| 操作合同 `O` | 否 | `functor_alg_mor` 是范畴态射兼容式，不是 `CurveRun` 或 ambient motion | 不存在从一个允许操作模型到另一个的免费完成桥 |
| `Done_s = Done_w × Denotes` | 否 | 输出是 `is_univalent_disp disp_cat_functor_alg`，不是某个 input/output run 的完成证明 | 没有同一 Done 的调用或声明 |
| 结构保持 | 是，而且显式 | `Hid`、`Hcomp`、`Hstandard`；`functor_alg_mor` 的等式 | 这是防御性正控制：结构必须进入接口、满足条件后才调用 SIP |

P3 所需的 `K_app` 必须同时出现“仅以 H/U”为输入、忽略 `R_min` 字段、并把输出作为相同 `Done_s`。这个调用链三项均不满足。它不是未命中的关键词，而是带源码、版本、入口和实际 invocation 的负向实例。

## 4. P3 判词与波次定位

**判词：`NO_K_WITHIN_UNIMATH_FUNCTOR_ALGEBRAS_DENOMINATOR`.**

- **最终目标连接**：P3 检验最终见证链中的实际消费者边。这是第一个版本固定的外部库调用，而不是 Book 定理或本地玩具实例。
- **全局坐标**：P1 已固定强任务；P2 排除 SIP 的规则桥；本 wave 检验 UniMath 对 SIP 的实际使用。P4 没有理论/实现差异，因此没有启动资格。
- **实际价值**：把“实际库可能把 SIP 当成强完成”的抽象怀疑缩成可复现的源码判词：此库使用显式 `H`/结构条件以证明 univalence，未声明圆环过程完成。它也证明当前无需重做 D_ABX、旧 SIP proof 或无版本的 UniMath 搜索。
- **为何不继续这个分母**：固定调用点、版本和任务均已审清；增加更多该文件的搜索或重复读 `SIP.v` 不会改变是否存在 P1 同任务桥。
- **总体裁决**：`CLOSE_WITH_SCOPE`。P1、P2 和第一个 P3 实际消费者分母均已完成；P4 无触发，四分支 first pass 进入 `STOP_BY_DEFAULT`。只有新的版本固定消费者、用户认可的更强 `R_min`、旧证据失效或可重放的理论—实现差异可另开下一 wave。

本报告是公开源码的版本固定审计。它未下载/编译 UniMath、未验证 Rocq kernel 结果、未证明外部库全局无 K，也没有 HoTT 缺陷结论。
