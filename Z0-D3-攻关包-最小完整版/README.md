# Z0-D3 攻关包 · 最小完整版（2026-10-10，Codex 会话 01a120e6）

**唯一任务**：在 Lean 4 中证明 `zfcTr_D3_internalize` 一条引理。

## 这一版比寄给你的前三版多了什么

我在本机（Lean 4.34.0 + Foundation `1fb01b72` + 完整构建树）实测并验证了：

> **Foundation 已经提供了 `Sh.craig` 的完整 D3** —— `(Sh.craig.standardProvability).HBL3`
> 由 `inferInstance` 直接合成成功。

这改变了缺口的形状：**不再**是"从零证明形式化 Σ1 完全性"（Foundation 已做完，
只需 `inferInstance`）。

**2026-10-10 晚的最新状态：缺口已压缩到一条引理的一个方向。**

- **`fwd`（已证，免费）**：`𝗜𝚺₁ ⊢ ↑(zfcTr τ) 🡒 ↑(provabilityPred Sh.craig (zfcTr τ))`
  —— 就是 Foundation 的 `provable_sigma_one_complete`（因为 `zfcTr τ` 是 Σ1 句，`zfcTr_sigma1` 已证）。
  骨架里已写成 `theorem fwd`，**无 `sorry`**。
- **`bwd`（唯一缺口）**：语义上"V 中有一条 `Sh.craig` 推导" ⊢ "V 中有一条 `𝗭𝗙𝗖` 推导"。
  `rw [models_zfcTr_iff]` 之后目标就是 `Provable 𝗭𝗙𝗖 ⌜(zfcTr σ)ᵗ⌝`。
  精确形状见 `01-先读这个/START.md` 与骨架的 `bwd`。

骨架文件 `05-源码/Z0D3Skeleton.lean` **本机编译 exit 0**：6 条引理已证，
只有 `bwd` 与 `HBL3_of_fwd_bwd` 带 `sorry`。复制它改，比从零开始快得多。

## 读的顺序（照这个来，别跳）

| 读什么 | 为什么 |
|---|---|
| `01-先读这个/START.md` | 60 秒版：目标、缺口、路线、验收 |
| `02-目标命题/GOAL.md` | 引理逐字类型 + 为什么它是唯一缺口 |
| `03-可用的已证引理/API.md` | 一条条可用的 Foundation/项目引理，都标了本机实测状态 |
| `04-攻坚路线/ROUTES.md` | 三条路线的精确判断与卡点，别重复我试过的 |
| `05-源码/Z0D3Skeleton.lean` | **已验证可编译的骨架**（复制它改） |
| `05-源码/BUILD.md` | 编译命令 |
| `06-复现环境/ENV.md` | 本机环境与替代方案 |
| `07-收据/` | W8 与 C-128 的既有收据，供你比对 |
| `PLAN-REVISION.md` | 我对原计划与上一版修订的更正（含本轮新事实） |

## 自验（不需要 Lean）

```bash
cd 05-源码 && python3 verify_coverage.py
# 期望: Foundation MISSING 0; project modules hash-ok 24, mismatch 0
```

## 不要做的事

- 读本 repo 的研究背景、读历史文档、跑任何与研究无关的测试。本包自足。
- 改 Foundation / Mathlib 源码。
- 留 `sorry` 冒充完成。卡住就把卡点写成一条精确 Lean 命题。
