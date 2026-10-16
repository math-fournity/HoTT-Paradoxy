# M1-A 修订记录

## 2026-10-04：C-365 收据输入收敛与 primary recapture

旧 primary `-05` 把 package README 与总 SOP 纳入 source manifest。它们用于路由、范围说明和
current planning，却不被 Agda 的 `command_argv` 读取；后续 F1/M3 路线更新使旧 run 出现
README/SOP hash drift，掩盖了实际 theorem source 的稳定性。

capture 现只冻结 `H0TraceObservation`、负控制、三个实际 imported H0 modules、toolchain、package-local
claim 和 capture procedure，并让 command 使用 canonical project-relative source path。`-06` / `NEG-06`
是这个最小充分输入集的 primary recapture。该修复不改动 C-365 命题或 Agda imports；它仅使 proof receipt
的输入身份与实际 kernel invocation 一致。

## 2026-10-04：C-365 的实际 transitive import 闭包

`-06` 在 version verifier 中暴露出一个真实依赖遗漏：Agda stdout 显示
`QuestioningDelay.agda` 实际检查了 `UniverseHasNoLevel.agda`，但旧 capture 的 `UPSTREAM`
只列出三份直接邻近模块。该模块不是可忽略的审计程序，而是 H0 universe `never` theorem 的
transitive proof input。

因此它被加入 capture 的 source manifest，并以 `-07` / `NEG-07` 重放。此 revision 扩大的是
实际 kernel 依赖闭包，不以 allowlist 绕过依赖检查。

## 2026-10-04：C-366 外部 Lean 的 toolchain dispatch 更正

`H0ProcessRepresentation` 的首个外部 capture `-001-01` 使用了用户全局的
elan launcher；虽然 external Foundation checkout 本身冻结在目标 commit，
该 launcher 在 `lake env` 下实际选择了 Lean 4.34.1，而该项目的
`lean-toolchain` 指定 Lean 4.34.0。首个 run 因而保留为可检查的历史尝试，
但不进入 primary evidence。

capture 随后改为在冻结 checkout 中经 `elan which lean` 和 `elan which lake`
解析 project-local toolchain，再以这些绝对 binary 路径执行。`-001-02` 与
`-NEG-001-02` 已确认 4.34.0。随后 `-001-03` 又暴露证据 registry 的一个真实
互操作要求：外部 Lake cwd 使 command receipt 只记录绝对 source path，不能与
canonical project-relative `source` 字段作机械同一性核对。capture 改为
`lake --dir <external-root> env <pinned-lean> <relative-source>`，故 `-001-04` 与
`-NEG-001-04` 既保持 external project，又把实际检查的项目 source 以 canonical
relative path 留在 command receipt 中，成为唯一 primary evidence。该修正不改变
C-366 的定理文字，只修复实际运行环境、输入身份与 registry 的一致性。

`-001-04` 随后还暴露了一个证据边界问题：capture 把不断演进的 package README 和总 SOP
纳入 source manifest，尽管它们不是 Lean elaboration 的输入。这样未来的路线文字更新会制造
伪造的 theorem-source drift。capture 因而只冻结 Lean source、negative control、package-local
claim scope、toolchain declaration 和 capture procedure；`-001-05` 与 `-NEG-001-05` 是采用这一
最小充分输入集后的 primary evidence。README/SOP 仍作为路由和需求 owner 被维护，但不再改变
本定理的已检查输入身份。

## 2026-10-04：trace 的点态来源更正

最初草稿把 `universeQuestioningNeverAnswers` 用作 `funExt` 的点态输入。Cubical Agda 拒绝该项：前者的类型是 `¬ Questioning.Halts`，不是逐 fuel 的 `runFor … ≡ nothing`。

修正为导入同一 fixed H0 包已经给出的

```text
universeQuestioningRunsNothing :
  (judge : Judge (Type ℓ-zero)) (n : ℕ) →
  runFor n (question (Type ℓ-zero) judge) ≡ nothing
```

此修正没有弱化命题；它把 trace projection 的证明直接接到 C-78 的正确 pointwise theorem。主运行和负控制均在修正后重新捕获。

## 2026-10-04：canonical 运行收据升级

最初的 `-001-01` 和 `-NEG-001-01` 已完整编译并保留，但它们的 source manifest 使用了旧的 external-dependency 字段，不能通过当前通用 `verify_formal_proof_run.py`。不改写历史收据；修复 capture schema 后重放为 `-001-02` 和 `-NEG-001-02`，其中 binary 与 cubical extracted tree 都按通用 verifier 的字段完整登记。随后，索引前更正了 `CLAIM.md` 的 canonical run locator；为使 manifest 与所有当前 proof inputs（含总SOP）相符，最终 canonical recapture 使用 `-001-05` 和 `-NEG-001-05`。`-03`作为同一 source identity 的已验证 replay、`-04`作为总SOP更新前的主运行留存。
