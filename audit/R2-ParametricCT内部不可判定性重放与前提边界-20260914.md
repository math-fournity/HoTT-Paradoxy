# R2 Parametric CT 内部不可判定性重放与前提边界

日期：2026-09-14  
proof：`MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001`  
run：`20260914-MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001-01`  
claims：C-219–C-222

## 结果

固定 `yforster/coq-synthetic-computability@b9523cb33180dc58b227432e60045cc38615b711` 后，codeload archive 与独立 Git export 的 109 文件树一致；树为 814,289 bytes，deterministic SHA-256 `093f04f2c16c465e1a42993f5acf6137f721fa39d4ed1d755564ced39cdb4670`。目标 `Axioms/halting.vo` 的实际本地闭包为 20 个 `.v` 文件。

作者声明的目标工具链由 `coqorg/coq:8.13.2@sha256:1f69…`、Equations 1.2.3+8.13、stdpp 1.5.0 重建为本地 image ID `sha256:7e35dbf…`。Coq 串行构建目标闭包后接受：

- `EPF_SCT_halting`：`EPF_bool + SCT` 推出存在可半判定而补集不可半判定的 `K`，并给出 `~ decidable K` 与 `~ decidable (compl K)`；
- `K_nat_bool_undec`：同一前提推出 `~ decidable (compl K_nat_bool)`；
- `K_nat_undec`：同一前提推出函数恒零性质不可判定。

三个 `Print Assumptions` 均输出 `Closed under the global context`。最终 run exit 0，stdout 4,855 bytes，stderr 9,421 bytes；stderr 完整保留 Coq 8.13.2 的 deprecated-hint、deprecated-intropattern 与 require-in-module/section warnings。generic F-011 verifier 复核 external archive/tree、12 个项目源文件、matrix/index-row manifest 并 `--rerun`，结果 `EXACT_EXIT_STDOUT_STDERR_MATCH`。

## 强度判定

这一步确实比 C-208/C-218 前进：后者的 `undecidable P` 是“若 P 可判定，则某 hard complement 可枚举”的 synthetic implication；本包的结论已经是 Coq 对象语言内的 `~ decidable`。

强度仍严格是：

```text
EPF_bool 或 SCT 作为显式输入
    ⟹ internal ~ decidable
```

`Closed under the global context` 只说明证明项没有再调用未列出的全局公理；它不证明 `EPF_bool` 或 `SCT`。因此当前判词为：

```text
R2_CONDITIONAL_INTERNAL_NOT_DECIDABLE_MACHINE_REPLAYED
/ R2_AMBIENT_HOTT_UNCONDITIONAL_NOT_DECIDABLE_OPEN
/ HOTT_ESSENTIALITY_OPEN
```

## 版本失败证据

现有 Coq 8.15.2 MM2 image 缺 stdpp。补入兼容 Coq 8.15 的 stdpp 1.7.0 后，目标重建在 `Shared/ListAutomation.v:142` 的 `congruence` 证明失败；stdpp 1.12 又不兼容 Coq 8.15 的语法。它们是源脚本与工具版本边界，不是内部不可判定 theorem 的反例。最终使用作者指定的 8.13.2 时代依赖，未修改上游证明。

## 证据与限制

- package：`HoTT/formal/external-coq-parametric-ct/`；
- source/run/index：均已闭合，尚未 Git version-close；
- 固定上游树没有许可证文件，项目未复制其源码正文；本地缓存只承担研究重放，不推断再分发许可；
- 不使用 Path、univalence、HIT 或 modality；不证明 ProgramCode 的无条件不可判定、Gödel 不完备性、natural consumer、现实桥梁或 HoTT 矛盾。

下一步不是继续换机器造 loop，而是将 CT/EPF 的 universe/modality 适用域与 Oracle Modalities、cubical assemblies 对账，并寻找是否存在从 modal computation universe 到 ambient universe 的真实 consumer 提升。
