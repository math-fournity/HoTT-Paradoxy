# 对 zfcTr-D3-plan.md 的独立评审（Codex 接管版，2026-10-11）

## 0. 直接回答：原计划对吗？

方向对，但“缺口形状”已被后续工作进一步收窄，且原计划 §5 的“经翻译的 Σ1 完全性移植（L1–L5，~1080 行）”
主攻路线已被证明**不必做**——真正剩下的是更窄的 `ShCraigElim` 归纳消去。

## 1. 与原计划的偏差

原计划把缺口写成“重做经翻译的 Σ1 完全性”（§5）。但 C-390（Z0UniBridge.lean）已把 Z0 完整形式
归约为 `ShCraigElim`，而 `ShCraigElim` 经 `bwd_of_shcraig_elim` 归约到原 `zfcTr_D3_internalize`。
即：缺口已收成“对 Sh.craig 的推导编码做结构归纳消去”，不必移植 Foundation 的 bold_sigma_one_complete。

## 2. 对三个接力误传的纠正（本机实测）

1. neg 律未编译过（含 sorry）—— 不是“已证”。见 STATUS.md。
2. Foundation 模块齐全（308 个），第三方 AI 的“缺 140 个”是无网络沙箱假象。
3. 八方向已闭合，只剩 ShCraigElim。

## 3. 修订后的最小路线

1. 修 ShCraigElimNegLaw.lean 的 and/or/all/exs 支（见 ROUTES.md §1）。
2. 填 induction_setup 的 8 个 sorry 支（hAnd/hOr 用 iT_and/iT_or + Derivable.and_m/or_m；
   hAxL/hCut 用 iT_neg；hAll/hExs/hShift 需照 iT_neg 写 iT_setShift/iT_substs1；
   axm 读 CraigTrick.lean）。
3. 接成无 sorry 的 ShCraigElim；Z0Blocked.lean 的 sorry 改为引用它。
4. 抓 F-011 收据、更新 形式化追踪/ 与矩阵。

## 4. 不要走的路

原计划 §5 的 ~1080 行 Σ1 完全性移植（已由 ShCraigElim 取代）；不要试图把 provable_internalize
推广到 ZFC（需要集合论语言的 Σ1 完全性，更难）。
