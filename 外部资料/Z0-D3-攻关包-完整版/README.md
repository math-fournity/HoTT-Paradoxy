# Z0-D3 攻关包 · 完整版（给下一个 AI 的攻关基础）

> 本目录是 `外部资料/Z0-D3-攻关包-最小完整版` 的**补全版**。最小版只带了 169 个
> Foundation 源文件，而项目闭包（`MATHLIB_CLOSURE.json`）在固定 commit `1fb01b72` 下
> 实际依赖 **308 个** Foundation 模块。本目录把缺失的全部 308 个 Foundation 源文件补齐，
> 并附上可逐文件 fetch 的 GitHub 原始地址清单，让下一个 AI 能在一个完备、可编译的基础上
> 专攻数学证明，而不是卡在“缺模块 / 看不清 API”。

## 1. 这个目录里有什么

```
Z0-D3-攻关包-完整版/
├── Foundation/                 # Foundation 全量源码 308 个 .lean（commit 1fb01b72）
│                               #   直接用，无需联网；与最小版同名文件逐字一致
├── Project/                    # 目标证明包 godel-q-zfc-z0-full 全量（45 个 .lean + 配置）
│                               #   与仓库 HoTT/formal/claude-cg001/godel-q-zfc-z0-full 逐字一致
├── Plans/                      # 三份计划/评审原文
│   ├── PLAN-zfcTr-D3.md        #   原始攻坚方案 zfcTr-D3-plan.md
│   ├── PLAN-REVISION-2.md      #   第二位 AI 的修订
│   └── PLAN-REVIEW-3.md        #   第三份独立评审（含本机实测）
├── FOUNDATION_MODULES.md       # 308 个模块名 + 相对路径 + GitHub 原始地址表
└── foundation_modules_urls.txt # 同上，纯 URL 一行一个（curl 批处理用）
```

## 2. 这个计划（zfcTr-D3-plan.md）对不对？——给研究发起人的判断

**结论：方向对，但对“缺口是什么、有多大”的定位在后续评审中已被修正。**

- 原始方案 §3 的 Bridge′ 弱化（把 D3 收成 `V ⊧ σ → Provable 𝗭𝗙𝗖 ⌜translate σ⌝`）是
  **关键正确洞察**，C-128 已证明这个弱化形式；
- 原始方案 §5 想“移植 ~1080 行 Σ1 完全性”，**后来被证明不必做**：Foundation 的
  `DerivabilityCondition/D3.lean` 已经把 Craig 化后理论的 D3 完整机器证明做完，
  且对 `Sh.craig` 直接 `inferInstance` 可用（见 PLAN-REVIEW-3.md §2 的三条实测）；
- 所以真实缺口比原始方案估计的小得多：不是“重做 Σ1 完全性”，而是
  **一条句法等价的一个方向**（`keyE` 的 `bwd`，即 `ShCraigElim`）。
  但“小”是相对 1080 行而言——它仍然是一条尚未机器证明的精确引理，不是措辞问题。

原始方案 §4 对 `of_provability` 语义性的否定、§8 的验收标准，均被后续评审确认正确，
可直接采用。详见 `Plans/PLAN-REVIEW-3.md`。

## 3. 真正的缺口（给下一个 AI 的精确目标）

唯一剩下的阻塞引理（带 `sorry`，不进收据源）：

```lean
-- HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/Z0Blocked.lean:29
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) := by sorry
```

归约链（已证部分，见 `Project/GodelQ/ZFC/Z0UniBridge.lean` 与 CLAIM.md）：
`ShCraigElim`（C-390/391/392/393/394/396/397 等已逐文件收据）
经 `bwd_of_shcraig_elim` 归约到 `bwd`，再归约到 `keyE`，最后到上面的 D3。

**当前最后一步 = 证明 `ShCraigElim`，即把 `Sh.craig` 的推导编码沿翻译变成 `𝗭𝗙𝗖` 的推导编码。**
它需要在 `Project/` 里新增文件（不得改 `Z0Full.lean` 的定理类型），按
`BUILD.md` 的拓扑序加入编译，证完后再用 `capture_run.py` 抓收据（它拒绝含 `sorry` 的源）。

## 4. 复现环境与工具

- Lean 4.34.0（`/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0`）；
  其他机器用 `leanprover/lean4:v4.34.0`。
- Foundation 源码：`/Volumes/D/HoTT-toolchain-cache/foundation-src`（commit `1fb01b72`）。
- Foundation 构建产物（olean）：`/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean`。
- 增量编译脚本：`/tmp/d3build/devbuild.py`，以及仓库内
  `.claude/goals/CG-007-formalization-completion/tools/capture_run.py`、
  `verify_cg001_run.py`（详见 `Project/README.md` 与 `BUILD.md`）。
- 配置锁：`Project/LEAN_TOOLCHAIN.json` 与 `Project/MATHLIB_CLOSURE.json`（commit 固化）。

## 5. 给下一个 AI 的 GitHub 地址（可联网时按需 fetch）

- 仓库：`https://github.com/FormalizedFormalLogic/Foundation`
- 固定 commit：`1fb01b72de546e1b50821fd05b1314a8d958583f`
- 单文件原始地址模板：
  `https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/<commit>/<相对路径>`
- 完整 308 条清单见 `FOUNDATION_MODULES.md`（表）与 `foundation_modules_urls.txt`（批处理）。
- 验证：本机已对 `D3.lean` 该地址 `curl` 返回 200 / 8708 bytes。

## 6. 你（下一个 AI）要解决的，严格说只有一件事

在 `Project/` 的包内，把 `ShCraigElim`（`∀ σ, Provable Sh.craig ⌜σ⌝ (V) →
Provable 𝗭𝗙𝗖 ⌜translate σ⌝ (V)`）证成无 `sorry` 的定理，并按 F-011 门禁抓到收据。
一旦它通过，`Z0Full.zfc_z0_full_of_D3_internalize` 立即给出 Z0 完整形式
`𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ`，整个“形式化与机器证明”主线即告完成。
其余 8 个方向（图灵路线、时间结构、C6、HoTT 一侧、同一个 Q、抽象层综合、分支形式包、更早形式化）
在 `形式化追踪/README.md` 中均已标记 ✅ 或条件完成，无需你处理。
