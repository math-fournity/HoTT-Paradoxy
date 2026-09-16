# G-HOTT-SYNTAX 首个精确机器切片与 2LTT 边界

日期：2026-09-14  
proof：`MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001`  
run：`20260914-MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001-01`  
claims：C-223–C-226

## 为什么没有直接采用 2017 2LTT §2.1

2LTT 论文明确说 suggested syntax 不是 complete specification；其精确对象是两个共享 context category 的 CwF 模型，term-model/initiality 的完整证明超出论文范围。它的 basic conservativity 只按 initial-model semantic view 反射 inhabitation；T1–T3 与 A1–A6 strengthenings 又改变 conversion、Nat、fibrancy、equality reflection 和模型范围。

因此把该规则列表称作“exact raw calculus、proof checker 与 enumerator 已冻结”会越级。它仍是 inner/outer 与 conservativity 的重要 primary source，但不能单独关闭 `G-HOTT-SYNTAX-001`。

## 固定的 exact slice

从论文作者页定位到 `https://bitbucket.org/akaposi/cohtt`。固定 master commit `5babc385d01500c1777ff932dd8c79299a1d766a`、Git tree `13849af00ff393300c0ae6cdd47ba6ddfa0d1cd8`；Bitbucket archive SHA-256 `f83f4b0f…` 与独立 Git export 的 91 文件、1,706,237 bytes 逐文件一致。

当前 `TT/` 20 个模块定义：

- groupoid syntax 的 `Con/Sub/Ty/Tm`；
- substitution、composition、terminal context、context extension；
- `U/El`、Π、`lam/app`、β/η；
- `U/El/Π` substitution 与 composition/identity 的二阶 coherence；
- `Sub`/`Tm` set truncation 与 `Ty` groupoid truncation；
- α-normal types、`isSetTy`；
- groupoid/set syntax 的 `isoCon/isoSub/isoTy/isoTm`。

项目 `CheckGroupoidSyntax.agda` 显式重述 `isSetTy` 与四类同构。run 先在 fresh pinned Cubical v0.9 source 上用 `--safe --cubical --guardedness --ignore-interfaces` 检查依赖与全部 TT 模块，再删除全部 cohtt interfaces，使用上游 library flags 重查 TT 模块，最后检查项目 probe。exit 0，stdout 27,134 bytes；stderr 184 bytes，仅为四个 phase 的空原始流标记。F-011 `--rerun` 为 exact stdout/stderr/exit match。

上游 `cohtt.agda-lib` 没有 `name:`，Agda 无法用 `-l` 选择；derived wrapper 只增加 `name: cohtt-replay`。把 `--hidden-argument-puns` 作为命令行全局应用并强制重解析 Cubical v0.9，会在 `Prelude.agda:610` 报 `WrongHidingInLHS`；两阶段重放先固定依赖接口、再按上游 flags 重查作者模块，保留这项配置边界。

## R4 剩余义务

该 object syntax 只有 Π、`U/El` 与 base family；没有 Nat、一般 identity/Path former、对象层 univalence/HIT、raw derivation checker、proof enumeration、arithmetic interpretation 或 fixed-point sentence。当前状态是：

```text
G_HOTT_SYNTAX_FIRST_EXACT_MACHINE_REPLAYED_SLICE
/ FULL_HOTT_CALCULUS_OPEN
/ R4_INCOMPLETENESS_OPEN
```

## 新候选

2LTT §2.7 报道：如果 outer type 的 fibrant replacement 被内在化为 context-stable `R` type former，具 formation/introduction/elimination/computation rules，则 inner level 满足 UIP；homotopical models 中逐对象 replacement 虽可存在，却通常不稳定于 base change，所以不能按该规则自然内化。

这给出 `CAND-2LTT-FIBRANT-REPLACEMENT-UIP-001`：把外部逐例过程提升为内部统一、可替换、context-natural 操作，会额外要求相干并坍缩高阶 identity。它比一般“HoTT 也有 Gödel”更接近理论经济与方向 A/B 的交叉点。当前 theorem 仍为 `SOURCE_REPORTED_NOT_REPLAYED`；下一单元应机器化最小 R rules→UIP，再以 univalence/Bool 或 circle 给反控制，并消融 context stability/crisp restriction。
