# N2 审计：W51×RP-B01 的对象层→执行层提取接口

> 文档身份：`CURRENT AUDIT EVIDENCE / DEFENSE_WORKS (SCOPED)`
> 日期：2026-09-12
> 触发：N1 bounded negative 后，STATE 把第一工作包路由为 N2
> 目标：审计真实证明助手/编译/提取入口是否把“命题 LEM 下的数学分类 `χ`”承诺为“同规格统一有效交付”
> 结论：**在被审计的接口中判 `DEFENSE_WORKS`——对象层函数可以类型检查，但默认执行层拒绝交付实现（Agda postulate 生成运行时错误桩；Lean 求值与 `#eval!` 均拒绝 noncomputable 定义）。没有任何被审计接口作出统一有效交付承诺。**

## 0. 审计集合与限制

| 接口 | 版本/入口 | 本轮可核层级 | 结果 |
|---|---|---|---|
| Agda 类型检查 + MAlonzo 编译 | Agda 2.8.0-3d04bac（`/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/agda`） | 实际运行 type check 与 `--compile`；检查 MAlonzo 生成的 Haskell | 类型层接受；生成的 `lem` 是 `error "postulate evaluated"`；`--compile` 走到 GHC 步骤时因本机无 `ghc` 中止（环境限制，不改变生成物证据） |
| Lean 4 求值/编译 | Lean 4.33.1（`/Users/aurolafly/.elan/bin/lean`） | 实际运行 `lean LemClassifier.lean` | 类型层接受 `noncomputable` 分类器；`#eval` 与 `#eval!` 都拒绝编译该定义；直接对 `P ∨ ¬P` 做大消去到 `Bool` 还被内核的 Prop 消去限制挡住 |
| Coq/Rocq extraction | `coqtop`/`coqc`/`rocq`/`rocqtop` 均不在 PATH | NOT_AVAILABLE | 未审计 |
| GHC 后端 | `ghc` 不在 PATH | NOT_AVAILABLE | Agda 编译无法完成最终链接，但 MAlonzo Haskell 已生成 |

审计限制：本审计只覆盖上述版本与入口；不证明“任何接口/任何版本都不可能作出统一有效交付承诺”。四组控制中第 4 组（显式神谕/用户实现）未在本环境成功构建；其机制以接口的显式开关为准，而不是默认行为。

## 1. Agda：类型层接受，执行层生成“postulate evaluated”错误桩

实验源：`evidence/agda/LemClassifier.agda`（931 bytes，SHA-256 `5809301f70f17a96a78f9b3e3f813ee38081c454267a21f2580b55eb6046a063`）：

```agda
postulate
  lem : (P : Set) → P ⊎ (P → ⊥)

chi : (P : Set) → Bool
chi P with lem P
... | inj₁ _ = true
... | inj₂ _ = false
```

### 1.1 类型检查

命令（工作目录 `evidence/agda/`）：

```text
agda --ignore-interfaces -i . LemClassifier.agda
```

结果：exit 0，输出 `Checking LemClassifier (...)`。对象层分类器与两个控制函数都是良类型的。

### 1.2 MAlonzo 编译

命令：

```text
agda --compile --compile-dir=./out --ignore-interfaces -i . LemClassifier.agda
```

结果：exit 42；MAlonzo 已生成 Haskell，随后在调用 `ghc` 时中止：

```text
Compiling LemClassifier (...) to ./out/MAlonzo/Code/LemClassifier.hs
Calling: ghc -O -Werror -i./out ... --make -fwarn-incomplete-patterns
ghc: createProcess: posix_spawnp: does not exist (No such file or directory)
```

生成的 Haskell（`evidence/agda/out/MAlonzo/Code/LemClassifier.hs`，1809 bytes，SHA-256 `6a8a59ff0426a1860dc86a8816a8f9185bb9abdb0d4618e1079ed880fdf599a9`）给出决定性证据：

```haskell
-- LemClassifier.lem
d_lem_32
  = error
      "MAlonzo Runtime Error: postulate evaluated: LemClassifier.lem"
```

`chi` 的实现是 `case coe d_lem_32 erased of ...`：一旦求值到 `lem`，运行时立刻报错；默认编译不伪造一个 LEM 值，也不提供有效实现。

显式 `{-# COMPILE GHC lem = ... #-}` 一类 pragma 属于第 4 组控制：用户自行提供实现并承担合同变化，不是默认交付。

## 2. Lean：内核消去限制 + noncomputable 求值拒绝

实验源：`evidence/lean/LemClassifier.lean`（806 bytes，SHA-256 `910ab13b0604575fb72aa68a79a80277d827ae1c647428d2fe5c9dab3aac9577`）。

第一版直接对公理证明做模式匹配：

```lean
noncomputable def chi (P : Prop) : Bool :=
  match lem P with
  | Or.inl _ => true
  | Or.inr _ => false
```

Lean 4.33.1 直接拒绝：

```text
error(nested.lean.propRecLargeElim): ... recursor `Or.casesOn` can only eliminate into `Prop`
```

说明：从 `Prop` 证明消去到 `Bool`（`Type`）本身就不被内核允许；必须经 `Classical` 的非计算路径。

最终版本使用显式经典接口：

```lean
open Classical
noncomputable def chi (P : Prop) : Bool :=
  if P then true else false
```

运行 `lean LemClassifier.lean` 的实际输出：

```text
true
LemClassifier.lean:20:0: error(lean.dependsOnNoncomputable): failed to compile definition, consider marking it as 'noncomputable' because it depends on 'chi', which is 'noncomputable'
LemClassifier.lean:24:0: error(lean.dependsOnNoncomputable): failed to compile definition, consider marking it as 'noncomputable' because it depends on 'chi', which is 'noncomputable'
```

三行分别对应：

1. `#eval haltWithin 5` → `true`（控制 1：有限步/平凡检测有效）；
2. `#eval chi True` → 拒绝编译 noncomputable 定义（控制 3：经典分类器没有默认有效实现）；
3. `#eval! chi True` → 同一拒绝（本轮 `#eval!` 没有绕过；显式 `implemented_by`/`unsafe` 属于第 4 组控制，未构建成功）。

## 3. 可用性矩阵

| 工具 | 状态 |
|---|---|
| Agda 2.8.0 | 可用；type check 与 MAlonzo 生成可用 |
| Lean 4.33.1 | 可用；求值/编译拒绝已实测 |
| GHC | `NOT_AVAILABLE`（Agda 最终链接未完成） |
| Coq/Rocq | `NOT_AVAILABLE` |

## 4. RP-B01 WP3 的四组控制

| 控制 | 本轮证据 | 判定 |
|---|---|---|
| 1. 有限步停机检测 | Lean `haltWithin 5` → `true`；Agda `haltWithin` 生成常量 `true` | 正例：可有效实现 |
| 2. 经典分支返回相同常量 | `equalConst` 是良类型经典函数；数学常值函数 `fun _ => true` 有平凡有效实现 | 正例：LEM 使用本身不等于不可实现；分离点只在停机相关分支 |
| 3. 停机相关分类器 `χ` | Agda：postulate 生成 `error "postulate evaluated"`；Lean：`#eval`/`#eval!` 拒绝 noncomputable | 默认接口拒绝，判 `DEFENSE_WORKS` |
| 4. 显式神谕/用户实现 | Agda `COMPILE` pragma / Lean `implemented_by`、`unsafe` 等显式开关；本轮未构建 | 合同变化，不能算默认交付；保持 NOT_RUN |

## 5. 判定与范围

判定：`DEFENSE_WORKS (SCOPED)`。

- 被审计接口不把命题 LEM 下的数学分类 `χ` 承诺为同规格统一有效交付；
- 它们要么在运行时把 postulate 变成错误，要么在求值时拒绝 noncomputable 定义；
- 内核还对 `Prop → Bool` 的大消去设置独立限制；
- `B01-TARGET`（是否存在自然 HoTT 使用流程作出这种升级）在本次接口集合内仍未找到，但本轮不再只是“未找到接口”，而是给出了接口级拒绝的直接证据。

重开条件：

1. 某版本/后端默认把 postulate/公理提取为可运行实现，且不要求用户显式实现；
2. 某真实 HoTT/类型论消费者在同一任务中把 `noncomputable`/postulate 分类器当作可执行交付；
3. 出现新的提取语义（例如带计算规则的公理、tabulation 后端）改变上述默认行为。

## 6. 下一工作包 N3：R036/R038 原生 Cubical 升级

N1 与 N2 分别把 A 线（结果商 consumer）与 B 线（提取接口）在固定集合内关闭为 documented boundary / defense。按 RP-B01 WP4 的“保存保护、转向新机制”原则，下一工作包固定为：

> **N3：把 R036/R038 的商/当前态提升/极限比较边界升级到原生 Cubical Agda**——固定状态商、Done 保真、当前态 lift 与 limit 比较接口，机器证明（或反驳）相应 lift/limit no-go，并保留正向控制。

完成判据与停止条件：

- 至少产生一组新的 source/run/index 证据（F-011）；预期判词最多为 `REPRESENTATION_BOUNDARY`；
- 如果只是把有限模型换个名字重证、没有新机制或新接口，记录该结果并停止该子方向；
- 只有同时出现自然 consumer 与同任务资格升级，才允许向 `NATURAL_USAGE_MISMATCH` 升级。

## 7. 证据锚点

- `evidence/agda/LemClassifier.agda`（SHA-256 `5809301f…`）；
- `evidence/agda/out/MAlonzo/Code/LemClassifier.hs`（SHA-256 `6a8a59ff…`）；
- `evidence/lean/LemClassifier.lean`（SHA-256 `910ab13b…`）；
- Agda 工具链身份：`HoTT/formal/partiality-race-timeout/TOOLCHAIN.json`；
- Lean 版本：`Lean (version 4.33.1, arm64-apple-darwin24.6.0, commit 819816b2e0a3bf405af45ae5c7af2491d8f5bee6, Release)`；
- 上游：`理解章节/C5-十机证明后的悖论距离与自然消费者审计-20260912.md`；`audit/natural-consumer审计-20260912.md`；`workspace/.codex/research/hott/candidates/RP-B01/PLAN.md`；`workspace/.codex/research/hott/candidates/RP-B01/CLAIMS.json`。

## 8. 本轮不升级声明

本审计没有新增数学 claim，没有升级任何既有 claim，没有把 `DEFENSE_WORKS` 写成“HoTT 完全无法被滥用”，也没有启动 ERCF-3 或修改 `MP-*` 包状态。
