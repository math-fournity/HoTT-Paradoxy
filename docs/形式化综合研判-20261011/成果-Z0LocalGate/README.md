# 成果：Z0 的最小完成门（Z0LocalGate）

> 2026-10-11，CG-009 会话自研方向。源文件 `Z0LocalGate.lean`（sha256 `a50f7d4e…`），
> 本会话 pinned Lean 4.34.0 + Foundation `1fb01b72` 编译 **exit 0**，
> 四条定理 `#print axioms` 均仅 `[propext, Classical.choice, Quot.sound]`。
>
> **状态：本会话私有探针级成果**（未入 dev、未走收据流程）。价值在数学信息，不在治理身份。

## 这是什么

把本会话审计报告 §8.1 的发现形式化：**最终 Z0（`𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)ᵗ`）不需要全称的
`ShCraigElim`（对所有算术句 σ 做 `Sh.craig` 推导消去），只需要 Gödel 句
`G := gödel zfcTr` 处的一次单句实例。**

十四条定理（全部过核、全部公理干净；最终 sha256 `24ea1cb1…`）：

| 定理 | 陈述 |
|---|---|
| `con_unprovable_of_local_D3` | 通用：`T ⊬ 𝔅.con` 只需 `d3G : T₀ ⊢ 𝔅 G 🡒 𝔅(𝔅 G)` 一条（不需要全称 `HBL3`）；D1/D2/对角化/一致性照旧 |
| `zfc_z0_full_of_local_D3` | 实例化：`𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)ᵗ` ⇐ `𝗜𝚺₁ ⊢ zfcTr G 🡒 zfcTr(zfcTr G)` 一条前提 |
| `local_D3_of_elim_at_godel` | 归约：**单句消去**（只在 G 上）⇒ 局部 D3 |
| `zfc_z0_full_of_elim_at_godel` | **闭环：最终 Z0 ⇐ 单句消去**（一个句子，而非全部 σ） |
| `bwd_at_godel_of_elim_at_godel` | elim@G ⇒ bwd@G（经 fwd；bwd@G 门不更强） |
| `zfc_z0_full_of_bwd_at_godel` | 最终 Z0 ⇐ `bwd@G`——单句、单方向、不经 `Sh.craig` 的跨模型实例 |
| `d3G_of_reverse_at_godel` | 单句反向桥 ⇒ d3G（bd4295b5 的 image 门，只在 G 上） |
| `zfc_z0_full_of_reverse_at_godel` | 最终 Z0 ⇐ 单句反向桥 |
| `zfc_z0_full_of_keyE_at_image` | **规范形状对接**：最终 Z0 ⇐ `keyE` 的单句实例 `𝗜𝚺₁ ⊢ zfcTr(zfcTr G) 🡘 provabilityPred Sh.craig (zfcTr G)` |
| `fwd_at_G` | `zfcTr G → □Craig(zfcTr G)`（Σ1 完全性免费实例） |
| `craig_D3_at_image` | `□Craig(zfcTr G) → □Craig(□Craig(zfcTr G))`（Sh.craig 的 D3 在该句处，免费） |
| `gate_of_elim_at_godel` | elim@G ⇒ gateG |
| `zfc_z0_full_of_gate_bot` | **第二个单句面（⊥ 门）**：最终 Z0 ⇐ `𝗜𝚺₁ ⊢ □Craig(⊥) 🡒 zfcTr ⊥`（bd4295b5 方向的修复写法：`contra` 显式 MP、去 `change`） |
| `elim_at_godel_of_gate` | **等价闭环：gateG ⇒ elim@G**（配合上一条 = gateG ⟺ elim@G） |
| `gateG_standard` | **正对照：门在标准模型 ℕ 上成立**——门不是假的，全部困难在非标准模型 |

**精度修正（探针证实）**：`keyE@image` 的**正向**（`zfcTr(zfcTr G) → □Craig(zfcTr G)`）**不是免费的**——`V ⊨ zfcTr(zfcTr G)` 只给"V 内有 ZFC 推导"，接不上 Σ1 完全性。单句 iff 并不比单句反向蕴含更弱；完成门以反向（gateG）为准。

## 为什么重要

- 所有并行会话（Codex、WorkBuddy）当前都在攻**全称** `ShCraigElim` / 全称 `keyE`。
  本成果证明：**只对 `zfcTr G` 这一个句子的实例成立就够了**——而且可以取规范形状
  （`zfc_z0_full_of_keyE_at_image`），与追踪文档里的"唯一缺口 `keyE`"直接对接。
- **收缩的是陈述强度与接口，不是（必然的）证明工作量**——这一点必须说准：
  - **陈述层面**：确实严格更弱。全称 `keyE`/`ShCraigElim` 要对所有 σ 双向成立；
    这里只需要一个句子、一个方向，且与 Foundation 第二定理链的接口只需这一个实例
    （`con_unprovable_of_local_D3` 展示第二定理的证明体只消费 G 处的 D3）。
  - **证明层面**：门的证明仍要消去 **`zfcTr G` 的任意（可能非标准的）推导 d**——
    d 的结构、其中间 sequent 与所用公理都不因结论句固定而变简单。因此
    Craig 证书桥、定义域护罩、规则归纳这三项核心义务在该句上**依然全部存在**，
    规模与全称版很可能同量级。**不要把本成果读成"工作量已缩小"**；
    它的价值是：接口更弱、目标更聚焦（一个具体句子），且排除了若干绕路
    （如全称 iff、非必要的双向）。
- 与 bd4295b5 的 `zfc_z0_full_of_reverse_at_bottom`（⊥ 处反向桥）是**不同句子上的同类收缩**：
  那条在 ⊥ 上，这条在 Gödel 句 G 上；G 版本的优势是与 Foundation 第二定理链的
  `gödel_spec`/`unprovable_gödel` 直接衔接，不需另接 `craig_consistent_unprovable_of_RE`。

## 建议的后续（本会话方案 P1-2 修订版）

1. 把本文件搬入正式包（新文件、不改既有）+ 收据。
2. **攻 `keyE@image` 的单句实例**（`zfc_z0_full_of_keyE_at_image` 的前提），而不是全称 `keyE`：
   目标是一个句子、一个方向——但注意（见上）该句的推导 d 仍是任意的，归纳机件与全称版同源。
3. 审"单句实例是否也避不开 Craig 证书桥"——大概率仍需，且需要的仍是**处理任意推导 d** 的能力
   （不是"一条给定见证"：V 里的见证由 `Provable` 的存在量词给出，可能非标准）。

## 用法与边界

- 源码可整体复制进 `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/`（新文件，不改任何既有文件）；
  依赖只有 `GodelQ.ZFC.Z0Full`。
- **不得**把条件定理读成 D3 已证：`local_D3_of_elim_at_godel` 的前提 `elim` 仍是假设。
- **不得**把本成果读成"工作量已缩小"：收缩的是陈述与接口，不是消去归纳本身（见"为什么重要"）。
- 建议后续（P1-2 修订版）：攻 `elim` 的单句实例，而非全称 `ShCraigElim`；
  或先审"单句实例是否也避不开 Craig 证书桥"（大概率仍需要，且仍需处理任意推导 d）。

## 复现

```bash
# 在 dev 主检出（授权后）或本 worktree 私有目录：
python3 -I <会话私有 verify 脚本> # 见 ../verify_candidates.py 的同款 env 构造
# 或照 BUILD.md：把文件放入包内，按拓扑序 devbuild 后 #print axioms
```

本会话实测命令与输出留档：`.cg009-verification/`（同一 env 构造）。
