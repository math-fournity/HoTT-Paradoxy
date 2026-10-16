# D09-C-369：Foundation Lean 第一不完备性 R3 —— 本机重放（此前 `SOURCE_REPORTED_NOT_REPLAYED`）

> **证明包**：`MP-FL-FOUNDATION-INCOMPLETENESS-R3-REPLAY-001`（`dev` 上的重放包；
> 原件在 `dev-09:HoTT/formal/external-foundation-incompleteness/`，`MP-FOUNDATION-INCOMPLETENESS-R3-001`）。
>
> **目标包**：CG-007（`.claude/goals/CG-007-formalization-completion/`），单元 W9c。
> 本机 Codex 会话 `01a120e6`，2026-10-10。
>
> **理论变体**：Foundation Lean 4 中的 first-order arithmetic；不是 exact HoTT calculus，
> 也不是 ZFC 对象语言。经典逻辑。
>
> **身份**：机器证明（**重放**，范围见 §4、§7）。它把此前判为
> `SOURCE_REPORTED_NOT_REPLAYED` 的 D09-C-369 变成 `dev` 上可重放的收据。

## 0. 为什么要重放

`dev-09` 上的原包（D09-C-369）有一个正运行与一个负控制，但**其运行依赖一个已不存在的
`/tmp` Foundation 检出**，因此 `形式化追踪/05-分支上的形式包/README.md` 判它
`SOURCE_REPORTED_NOT_REPLAYED`，并写"需要一份本机可用的 Foundation 检出才能重执行"。

本机恰好有那份检出：`/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/`
（Foundation `1fb01b72`，1893 模块）。因此本包把它重放。

## 1. 精确命题（与原件 CLAIM-R3-FOUNDATION-INCOMPLETENESS.md 一致）

在冻结来源的 `FFL.FirstOrder.Arithmetic.incomplete` 中，给定

```text
T : ArithmeticTheory
[T.Δ₁] [𝗥₀ ⪯ T] [T.SoundOnHierarchy 𝚺 1]
```

Lean 证明 `Entailment.Incomplete T`。`GodelQ/Qualification.lean` 检查四个声明并打印其 kernel axioms：

| 声明 | 前提 |
|---|---|
| `incomplete` | `[T.Δ₁] [𝗥₀ ⪯ T] [T.SoundOnHierarchy 𝚺 1]` |
| `incomplete_of_RE` | `[T.RE] [𝗥₀ ⪯ T] [T.SoundOnHierarchy 𝚺 1]` |
| `exists_true_but_unprovable_sentence_of_sigma1sound` | `[T.Δ₁] [𝗥₀ ⪯ T] [T.SoundOnHierarchy 𝚺 1]` |
| `exists_true_but_unprovable_sentence_of_RE_of_sigma1sound` | `[T.RE] [𝗥₀ ⪯ T] [T.SoundOnHierarchy 𝚺 1]` |

**本机实测结果**：四条 `#check` 的类型与原件声明逐字一致；四条 `#print axioms`
均为 `[propext, Classical.choice, Quot.sound]`。

## 2. 负控制

`GodelQ/WrongMissingSoundness.lean` 故意省略 `T.SoundOnHierarchy 𝚺 1`：

```lean
theorem wrong_incomplete_without_sigma1_soundness
    (T : ArithmeticTheory) [T.Δ₁] [𝗥₀ ⪯ T] :
    Entailment.Incomplete T := incomplete T
```

**本机实测**：Lean 在缺该 typeclass 实例处拒绝，报
`failed to synthesize instance of type class T.SoundOnHierarchy 𝚺 1`（exit 1）。
这证明本包没有把 source theorem 的 soundness 前提静默抹去。

## 3. 与原件的差异（必须知道）

| 项 | dev-09 原件 | 本包 |
|---|---|---|
| 路径 | `HoTT/formal/external-foundation-incompleteness/{Qualification,WrongMissingSoundness}.lean` | `HoTT/formal/claude-cg001/external-foundation-incompleteness/GodelQ/{同名}` |
| 文件内容 | — | **逐字节相同**（SHA-256 已核，见 `source-manifest.json`） |
| 模块名 | `Qualification` / `WrongMissingSoundness` | `GodelQ.Qualification` / `GodelQ.WrongMissingSoundness` |
| 为什么换目录 | — | `make_pins.py` 与 `capture_run.py` 只扫 `GodelQ/` 下的源；换目录不改内容 |

**dev-09 分支上的原件一字未动。**

## 4. 外部 pin 的差异（诚实记录，这是本包唯一的降级点）

| 项 | dev-09 pin | 本机可用 |
|---|---|---|
| Foundation commit | `f3972f4204fc61e1b736ed843415894c83f35508` | `1fb01b72de546e1b50821fd05b1314a8d958583f` |
| Lean | `v4.34.0` | `v4.34.0`（同一 toolchain） |

- `f3972f42` 正是 `1fb01b72` 的**父提交**；
- 两者的 diff 只有：新增 `FirstOrder/SetTheory/TransitiveClosure.lean`（134 行）+ `Foundation.lean` 加一行 import；
  **未触碰** `FirstOrder.Incompleteness.First` 及其导入闭包中的任何模块；
- dev-09 pin 的三个配置文件（`lakefile.toml`、`lake-manifest.json`、`lean-toolchain`）
  与 `f3972f42` 上的同名文件 **SHA-256 逐字节一致**（已核）。

**因此**：本重放在源码层与原件等价，但**不是**对原 `/tmp` checkout 的逐字节重执行。
判词是"本机重放的机器证明"，不是"原运行的精确重放"。

## 5. 它支付什么、不支付什么

**支付**：一个版本固定的一阶算术 proof system 中，编码、quote、substitution、provability、
固定点句与一致性前提如何形成可机器检查的第一不完备性结果——并且这份支付现在在 `dev` 上
**有可重放收据**。

**不支付**（与原包 CLAIM §"它不支付"一致）：

- exact HoTT calculus 的 object-level proof code、arithmetic interpretation、representability 或 independent sentence；
- HoTT 的 Path、univalence、HIT 对该机制是否必要；
- bare ZFC 的 `Accept_ZFC`、completion policy、`FormalDone → OriginDone` bridge；
- 芝诺、圆环或 fixed H0 与此一阶算术任务的同一性；
- ZFC 的对象语言矛盾，或 bare ZFC 理论精度不足的最终判词。

## 6. 运行

见 `HoTT/verification/runs/20261010-CG001-FFL-INCOMPLETENESS-R3-REPLAY-01/`（正运行）与
`.../-NEG-01/`（负控制），两者用
`.claude/goals/CG-007-formalization-completion/tools/capture_run.py` 抓取，
驱动 `zfc_lean_check.py` 复用 CG-006 冻结版（编译前核对每个模块的 SHA-256，禁网沙盒）。

## 7. 禁止外推

1. 不把本包的一阶算术不完备性说成 ZFC 对象语言上的结果；ZFC 上的对应结果是
   CG001-C-95–C-102（`HoTT/formal/claude-cg001/godel-q-zfc/`）。
2. 不声称本重放是原运行的逐字节重执行（见 §4）。
3. 不把 `T.SoundOnHierarchy 𝚺 1` 说成自动成立的前提；本包的负控制正是为了钉住它。
4. 不减损 `arithmetic strength`、`representability` 与 `soundness` 条件作为显式 theorem assumptions 的身份。
