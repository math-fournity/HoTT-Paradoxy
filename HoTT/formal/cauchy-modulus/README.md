# MP-CAUCHY-MODULUS-001：Cauchy modulus 边界

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS`

本包把 N7 选定的 Cauchy modulus 候选做成最小原生 Cubical 机器构造：**按极限值取商的 Cauchy 表示保留 limit，但忘掉表示中携带的 modulus；任何从商出发的函数都不能统一恢复该 modulus。把 modulus 加入同一性判据后，modulus 可以下降（正控制）。**

## 固定构造

- 序列 `Seq = ℕ → Bool`；
- 带 modulus 的 Cauchy 表示 `Cauchy = Σ[ s ∈ Seq ] Σ[ N ∈ ℕ ] (∀ n → le N n → s n ≡ s N)`；
- `seq c`、`mod c`、`lim c = seq c (mod c)`；
- `c0 = (constTrue , 0 , ·)`、`c1 = (constTrue , 1 , ·)`；
- 商 `Q = Cauchy / _≈_`，其中 `c ≈ d := lim c ≡ lim d`（只看极限值）；
- 细化关系 `c ≈' d := (mod c ≡ mod d) × (lim c ≡ lim d)`，商 `Q' = Cauchy / _≈'_`。

## 冻结命题（`C-129`–`C-133`）

| claim | 形式化结果 |
|---|---|
| `C-129` | limit 下降到商：存在 `C-129-limit : Q → Bool`（正控制：商保留极限值）。 |
| `C-130` | `c0 ≈ c1`（两者极限都是 `true`），但 `mod c0 ≢ mod c1`（`0 ≢ 1`）。 |
| `C-131` | 不存在 `f : Q → ℕ` 同时满足 `∀ c → f [c] ≡ mod c`（统一 modulus 恢复 no-go）。 |
| `C-132` | 细化商有 `C-132-modulus-refined : Q' → ℕ`（把 modulus 纳入同一性后可以下降；正控制）。 |
| `C-133` | 细化关系不识别两个表示：`¬ (c0 ≈' c1)`。 |

## 解释边界（判词）

判词：`CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS`（第二级结构性结果）：

- “按极限值取商”保留的是极限值，不是给定的 modulus；后者属于表示数据；
- 消费者若需要 modulus（例如做有界/十进制提取），必须保留代表或把 modulus 加入同一性判据（`C-132` 正控制），否则无法从商中统一恢复；
- 这不是 HoTT 内部矛盾；理论正确区分“序列的极限值”与“该序列在给定表示中使用的 modulus”；
- 与 N6 partial/strict 边界的区别：这里的缺口是 modulus 表示的同一性，不是 partial/total 判定；与 race/timeout 的区别：这里没有完成先后竞争，只有表示/同一性。

## 不证明（非目标）

- 不构造完整 Cauchy reals 或外部 Real 库；本包是最小 `ℕ → Bool` 序列实例；
- 不形式化十进制展开或实际数值打印；
- 不证明任何真实库/系统在没有 modulus 时错误地提取有界/十进制观察量；
- 不主张原创性（Cauchy 表示的 modulus 依赖是标准现象）。

## 外部 Real 库接口审计（N9 固定子项）

本地 Cubical v0.9 不包含 `Real`/Cauchy 实数模块（只有 `Rationals`）；因此本包使用自包含最小模型。外部 Real 库接口（如 agda-unimath）若可获取，将在 `audit/cauchy-modulus机器证明实施证据-20260912.md` 中按版本与接口签名单独登记；不可获取时明确记为 `NOT_AVAILABLE`。

## 证明身份

- proof ID：`MP-CAUCHY-MODULUS-001`
- claim IDs：`C-129`–`C-133`
- source：`CauchyModulus.agda`
- toolchain：`TOOLCHAIN.json` + `AGDA_LIBRARIES`
- final run：`20260912-MP-CAUCHY-MODULUS-001-01`
- index：`../../CLAIM_EVIDENCE_MATRIX.md`

Agda 2.8.0/Cubical v0.9 在 `--safe --cubical --guardedness --ignore-interfaces` 下实际接受本文件；运行原件、外部依赖哈希与命令在 `../../verification/runs/20260912-MP-CAUCHY-MODULUS-001-01/`。当前未获 Git commit/tag 授权，因此不能称 `MACHINE_PROVED_VERSION_CLOSED`。
