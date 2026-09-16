# R2-COQ-MM2-BRIDGE-001：同核 MM2 到显式 `ProgramCode` TaskSpec 的归约

> Proof ID：`MP-COQ-MM2-PROGRAMCODE-BRIDGE-001`  
> Claim IDs：`C-214`–`C-218`  
> Kernel：Coq 8.15.2 / OCaml 4.07.1  
> Source：`MM2ProgramCodeBridge.v`  
> Upstream：Coq Library of Undecidability Proofs `coq-8.15@c486697da8cfa4b9bb11b4c53eea7d57781c0deb`

## 工作包角色

本包在一个 Coq kernel 内把上游关系式 `MM2_HALTING` 编译到一个与项目 Agda `ProgramCode` TaskSpec 同构的显式分支目标语言。它补足 C-208 只有外部 seed、C-209–C-213 只有 Agda 本地桥而没有同核 theorem transport 的缺口。

目标指令恰有显式 `incA next`、`incB next`、`decA onZero onSuc`、`decB onZero onSuc` 和 `halt`；有限表按 label 0 起查找，表外默认 `halt`；`pc_run` 按 fuel 结构递减；`PC_HALTING` 是存在有限 stage 使 `pc_final_at=true`。这些字段与 Agda TaskSpec 逐项对应，但两份源码的跨语言同一性仍由 correspondence 审计而非单个 kernel 定理保证。

## 精确主张

### `C-214`：Coq target 与查表编译

`pc_instr`、`pc_program`、`pc_lookup`、`pc_is_final`、`pc_step`、`pc_run`、`pc_final_at` 和 `PC_HALTING` 定义目标 TaskSpec。`compile_program` 在 label 0 放 `pc_halt` 哨兵，再按源 label 编译。`nth_compile_tail`、`nth_compile_program` 证明对每个程序／label 的查表保持。

### `C-215`：上游关系终止与函数式有限观察等价

本包从上游 `mm2_instr_at`/`mm2_step`/`mm2_stop`/`mm2_terminates` 出发，定义 `source_lookup/source_step/source_run/source_final_at`，并证明：

```coq
mm2_terminates program state <->
exists steps, source_final_at steps program state = true
```

前向证明把关系闭包正规化为 `clos_refl_trans_1n` 并恢复步数；反向证明在当前已停止时结束，否则用确定性函数步前进。该证明关闭了 Coq 关系语义到 Coq 函数语义的量词差异。

### `C-216`：源函数语义到显式目标语义保持

`source_final_compile`、`source_step_compile`、`source_run_compile`、`source_final_at_compile` 对所有程序、状态和有限步数证明观察、单步、运行与精确 finality 相等。证明覆盖 INC、DEC 的零／后继分支、jump 0、表外停止和 target halt 自环。

### `C-217`：同核 total many-one reduction

```coq
MM2_to_PC_HALTING : MM2_HALTING ⪯ PC_HALTING
```

reduction function `compile_problem` 是 Coq 中定义的总函数；反射性由 C-215 与 C-216 的两个等价组合得到。

### `C-218`：目标 synthetic undecidability

```coq
PC_HALTING_undec : undecidable PC_HALTING
```

该定理由 C-208 的 `MM2_HALTING_undec` 和 C-217 经 `undecidability_from_reducibility` 得到。`Print Assumptions PC_HALTING_undec` 必须输出 `Closed under the global context`。

这里仍按上游定义解释：

```coq
undecidable P := decidable P -> enumerable (complement SBTM_HALT)
```

所以 C-218 是关于 Coq target 的 synthetic implication，不是纯构造元理论中的无条件 `~ decidable PC_HALTING`。

## 与 Agda C-209–C-213 的关系

两边共享下列固定表：

| 维度 | Coq target | Agda target |
|---|---|---|
| finite table | `list pc_instr` | `ProgramCode` |
| outside lookup | `pc_halt` | `halt` |
| inc | `pc_inc_a/pc_inc_b next` | `inc0/inc1 next` |
| dec | `pc_dec_a/pc_dec_b z s` | `dec0/dec1 z s` |
| state | `nat*(nat*nat)` | `Config(pc,r0,r1)` |
| bounded run | `pc_run` | `runFor` |
| final | instruction is halt | `isFinal` |
| halting | `exists n, final_at n=true` | truncated `Σ n, finalAt n=true` |

最后一行存在逻辑表示差异：Coq 使用普通存在，Agda 使用 propositional truncation。两个内部定理都只使用 existence，不恢复最小 witness；但“它们是同一个形式命题”的跨 kernel 结论仍是审计判断，不是某一 kernel 的 path。

## 禁止外推

本包不建立：

- 无条件 `~ decidable PC_HALTING`；
- Coq target 与 Agda `ProgramCode` 的字节级或 kernel 内同一性；
- CT／EPF、s-m-n、自应用或对象内 diagonal theorem；
- Gödel／Rosser／Löb 或 exact HoTT calculus 不完备性；
- HoTT higher structure 对 reduction 的必要性；
- natural consumer、现实同任务桥梁或 HoTT 内部矛盾。

因此本包若通过，只能把 R2 提升为“外部 seed 到同核显式目标的 synthetic-undecidability reduction 已机器闭合，且 Agda 有独立同形桥”；不能把整个 Goal 或 HoTT 悖论标记完成。

