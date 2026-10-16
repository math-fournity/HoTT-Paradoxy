# T-PRECISION：ACL2／Zeno 新来源入口审计

> **身份：** `T_META_SOURCE_INGRESS / CROSS_THEORY_CONTROL / NO_BARE_ZFC_CLAIM`。
>
> **冻结来源：** `chemoelectric/iris-number-system-acl2@3451a0809f23a31463b1a63d95d51b07e00b9a25`。
>
> **判词：** `ACL2_ZENO_SOURCE_INGRESS_NO_ADMISSIBLE_T_TARGET_WITH_SCOPE`。

## 1. 为什么它有资格成为新入口

此前 T 的 current denominator 已经审查 `set.mm`、Foundation generic Gödel、H0 trace、Zermelo sequence
representation 与 IEP/Norton completion contract。新的公开搜索返回了一个不同理论的候选：其 README 同时声称
ACL2 的 machine checking，并把“Zeno's Dichotomy”描述为 physical path 的 finite rational step completion。

这使它有机会回答 T 的一个真实问题：同一版本固定来源是否实际同时提供

```text
Process / ρ / Accept / OriginDone / Bridge
```

而不是只提供 proof checking 或只提供哲学性的 Zeno 叙述。

## 2. 本轮先验 TaskPrecisionCard

| 字段 | 冻结候选 | 成功需要的支付 |
|---|---|---|
| 理论／checker | ACL2 book 的 `iris_number_system.lisp` | source pin、可运行 checker 或认证 receipt。 |
| Process | README 所称 `G_omega` 上的 physical path。 | 代码中与该过程对应的输入域和语义。 |
| OriginDone | physical path 在有限步完成。 | 明确的完成谓词。 |
| Accept | ACL2 certification / certified book acceptance。 | 当前版本实际 certification 或 source-defined accepted artifact。 |
| ρ | physical path 到 ACL2 checker input 的保真编码。 | 来源定义的映射及任务保持。 |
| Bridge | accepted theorem/book 可交付 physical OriginDone。 | 同一 source 的明确 bridge。 |

若任一源只给实现、README 叙述或一个不同任务的算术引理，候选必须被拒绝为 T-Meta/T-ZFC 的入口；不能由本项目补造 bridge。

## 3. 固定源码与直接读取

本轮先以 `git ls-remote` 固定远端 HEAD，再 shallow clone 到隔离临时目录。冻结文件 hash：

| 文件 | SHA-256 |
|---|---|
| `README.md` | `9bcd51d21ac1471ae453202f8a38762ea069b8401dce6464186d5304e563bc30` |
| `iris_number_system.lisp` | `0da118b101948a4bdd9355d3b8027b7fcaf1924b5a81da5d60d8a5bebea083c6` |

README 的相关主张是：every physical path on `G_omega` resolves in a finite rational step count，且建议用户
在 ACL2 REPL 内执行 `(certify-book "iris_number_system" 0 t)`。但这是一份 repository README 的自述，
不是本轮已经取得的 certification receipt。

源码的对应定义与 theorem 是：

```lisp
(defun zeno-dichotomy-steps (dist omega) (* dist omega))

(defthm zeno-dichotomy-resolution
  (implies (and (rationalp dist) (posp omega))
           (rationalp (zeno-dichotomy-steps dist omega))))
```

因此其实际声明的 theorem 只给出 `dist * omega` 的 **rationality**。它没有定义 physical path 的状态、
没有给有限自然数步数、没有建立 `dist * omega` 是 step count、没有把该值连到路径终点，也没有定义
`Accept(ρ(path)) → OriginDone(path)`。

`finite-duration` 同样只在 rational `dist` 和正 rational `speed` 的假设下证明 `/ dist speed > 0`。它不构成
一个关于任意物理过程、芝诺序列或 original completion contract 的 bridge。

## 4. 运行与反控制

当前 host 未发现 `acl2`、`sbcl`、`ccl` 或 `clisp` binary。没有安装或伪造 ACL2 环境；故本轮不把 README 的
“machine checked”写成已本地重放。

即使将来 exact ACL2 certification 成功，以下控制仍必须保留：

1. ACL2 book 是与 bare ZFC 不同的基础／实现环境；
2. certification 首先支付的是该 book 的 proof-checking task；
3. 必须从实际 theorem 的 input/output 补出 physical Process、`ρ`、OriginDone 与 bridge；
4. 只有同一 source 的这种支付才可能使它成为 T 的 cross-theory actual target，仍不能直接成为 bare-ZFC instance。

## 5. 裁决、作用与重开

```text
ACL2_ZENO_SOURCE_INGRESS_NO_ADMISSIBLE_T_TARGET_WITH_SCOPE
README_PHYSICAL_CLAIM_NOT_LINKED_TO_CODED_PROCESS_WITH_SCOPE
ACL2_CERTIFICATION_NOT_REPLAYED_ON_CURRENT_HOST
DIFFERENT_FOUNDATION_CONTROL
CURRENT_T_PRECISION_SOURCE_DENOMINATOR_RETAINS_CLOSED_WITH_SCOPE
```

这不是对 ACL2、ACL2 book 或其作者科学主张的数学反驳。它只说明：在固定 commit 中，README 的 process-level
宣称与可读 Lisp theorem 的 formal content 没有构成 T 所要求的同一任务 bridge。

重开条件是版本固定的 ACL2 certification receipt，加上同一 source 支付 physical path model、finite-step
OriginDone、`ρ` 和 accepted theorem 到该完成谓词的 bridge。若未来支付成功，先把它作为 **T 的跨理论实例**
审查；不跨层写成 ZFC 结论。

## 6. 外部入口

- [冻结仓库](https://github.com/chemoelectric/iris-number-system-acl2/tree/3451a0809f23a31463b1a63d95d51b07e00b9a25)
- [README](https://github.com/chemoelectric/iris-number-system-acl2/blob/3451a0809f23a31463b1a63d95d51b07e00b9a25/README.md)
- [ACL2 book](https://github.com/chemoelectric/iris-number-system-acl2/blob/3451a0809f23a31463b1a63d95d51b07e00b9a25/iris_number_system.lisp)
