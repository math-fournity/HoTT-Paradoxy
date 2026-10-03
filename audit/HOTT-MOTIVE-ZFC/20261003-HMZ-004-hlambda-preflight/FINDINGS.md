# HMZ-004：预检结论

Voevodsky 2006 的文本是值得保留的原典，因为它明确讨论了 type-system 的等价、模型、不完备性、proof compiler
和 extension proof obligation。然而，这些都处在 Hλ／Coq-like system 与其到 ZF/ZFT 的外部验证关系中。

本项目当前要找的是：ZFC 自己在同一对象上，是否先使用一个仍待 formation/legitimacy 检查的对象，并在现实或
同一任务完成条件下产生 P 的张力。Hλ 预检没有给出：

- ZFC 对象语言中的候选 `u_Z`；
- 该对象的 ZFC formation `F_Z`；
- source-defined ZFC consumer `C_Z`；
- 同一 `I/O/Done`；
- same-object reentry、admission loop 或未付完成义务。

因此，启动完整 HMZ run 会把作者的技术图景误当作 ZFC 问题来源，违反 Phase-1 的 source admission 规则。
处置为 `ADMISSION_REJECTED_WITH_SCOPE`。这不评价 Hλ 的数学正确性，也不排除将来有新 ZFC consumer source
能使它成为配对材料。
