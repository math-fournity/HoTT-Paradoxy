# GODEL-Q-REFLECTION：形式化资产

本目录保存 GODEL-Q-REFLECTION-SOP 使用的本项目形式化资产。

- `FoundationGodelBaseline.lean` 是对冻结 `Foundation@f3972f…` 中通用 Gödel第一／第二不完备性 theorem 的最小 import/axiom wrapper；它固定需要的 ArithmeticTheory、可定义性／可枚举性、算术强度、一阶 soundness／consistency 与 standard provability 前提。
- `SetMMAppendixCGenerated.lean` 是 `MACHINE_MANAGED_CANONICAL` 输入：唯一生成器为 `scripts/audit/generate_setmm_appendix_c_vocabulary.py`，它从 pinned raw `set.mm@160ebb…` 提取 `$v/$f` vocabulary。不要手工编辑。
- `SetMMAppendixCVarExtension.lean` 是 `MP-GODEL-Q-SETMM-APPENDIX-C-VAR-EXTENSION-001` 的 M 层正控制：它证明 source vocabulary 可嵌入按每个 source type 都有 countably infinite fresh family 的扩张；`WrongSetMMFiniteVocabulary.lean` 必须被拒绝，以确认 raw/fresh 两层不会混同。正、负运行由两个 `capture_setmm_appendix_c_var_extension*.py` 捕获器产生。

这些资产都不实例化 actual `set.mm` 为 ZF 内 `mFS` object，不支付 `mPPSt/mThm` proof-trace adequacy、`Prv`、对角化、bare ZFC、芝诺／圆环／fixed H0 的 process contract、`OriginDone`、`ρ` 或 completion bridge。精确命题与禁止外推见各自 `CLAIM.md` 或 source audit。
