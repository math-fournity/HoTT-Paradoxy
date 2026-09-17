# S-RES-20260916-166-V2-STAGE1-FRAGMENT-EXTENDED

身份：PREMISE-001 step-5 **V2 L2-cofibration 片段阶段 1（片段扩展验收）**——ground 语义模块 + 自测 + Agda mirror 逐项一致性（修订片 015 §5 / §3.4）。
角色：AI 全自动执行（修订片 009）+ 强制审计层；外部 AI 追溯审计为终局复核。**不邀请用户介入。**

## 本单元产出

1. **canonical 分母单一来源**（引擎 commit `4428c48`）：把 `ground_values()`（289 ground 值）
   与 `declared_op_lists()`（11 条 op-list，含 `DECLARED_PARTNER` / `DECLARED_CONTINUATION`）收进
   `machine_overview/v2_cofibration.py` 作唯一来源；此前自测与生成器各自维护字面量（阶段 1 执行中
   因此暴露 4 个 `NameError`）。完整 selftest **142/142**（94 基线 + 48 V2），跑时 63.6s，无回归。
2. **stage-1 ground agreement PASS**（引擎 commit `9729d9f`，收据 `20260916-V2-STAGE1-AGREEMENT-001`）：
   289 ground × 11 op-list = **3179 条 applyOps**（穷尽，非抽样）逐项对照——Python 侧由
   `v2.apply_ops` 算期望 Obs，渲染 `V2GroundAgreement.agda`（654,939 bytes），由 Cubical Agda 2.8.0 +
   cubical v0.9 原生核类型检查，`KERNEL_ACCEPTED` / exit 0 / 30.8s；`groundAgreement : checkAll ≡ true`
   与 `sepAgreement : sepAll ≡ true` 均由 **refl** 消解。**这是定义式检查**：任一期望观测与核自身求值
   不符即类型检查失败（该失败本身就是验证）。
3. **11 条 designated controls 全部一致**（3 正控制 G-b/G-c/G-a + 5 负控制 + 3 个 L1 共享类可达性），
   期望值全部由 `v2.separates` 现算，无手写字面量。
4. **判词 `FRAGMENT_EXTENDED_WITH_SCOPE`**（修订片 015 §5）：**工程能力验收，不是数学结论**，
   `registers_new_claim:false`，不进 `HoTT/CLAIM_EVIDENCE_MATRIX.md`，不计 GEN-001 族数。
5. **修订片 016**（commit `e36bdd4`）：阶段 1 收据化 + 作用域披露 + 忠实性警戒升级为
   机械证明 + `DENOMINATOR_SINGLE_SOURCE` 纪律（本单元 reflection）。

## 纪律

- **作用域边界必须随收据传播**：applyOps 穷尽 3179 条；`separates` 只查 11 条 designated controls，
  **非 289² 全对**（全对需 ~918k 条 `SepResult` 字面量，超出可行单模块）；控制集在
  `tests/test_v2_cofibration.py::SeparationTest` 与 `v2_agreement.designated_controls()` 两处独立钉住。
- **忠实性警戒（015 §3.4）本单元机械确认**：mirror 库 §8-9 在点集模型内证明布尔等式并给出
  **DM3 三元链反模型**（`dm3NonBoolean : ¬ (dm3Meet da (dm3Neg da) ≡ d0)`），即点集模型对区间 `I`
  的 De Morgan 理论**可靠但不完备**。Python 点集模型只能当**枚举器**；oracle verdict 必须由
  Agda 真实区间 `I` 给出；任何"点集模型判分离 ⇒ 结论"的推理一律禁止（F-011 加严）。
- 两阶段**分开提交、分开登记**（015 §5）：本单元只登记阶段 1；阶段 2（`GEN-001-V2-1` 首族链）
  尚未开始，不由本 checkpoint 授权执行。
- Git：引擎 `4428c48`（canonical 分母）+ `9729d9f`（stage-1 agreement）；
  主 repo `e36bdd4`（修订片 016）；本 checkpoint revision 165->166。不 push、不 tag。
