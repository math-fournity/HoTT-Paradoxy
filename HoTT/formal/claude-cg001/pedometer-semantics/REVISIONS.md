# pedometer-semantics 的修订记录

> 本包 `CLAIM.md` 已入运行收据的哈希（`20260925-CG001-PEDOMETER-SEMANTICS-01`、`-NEG-01`、`-NEG-02`），不改原文；措辞修订记在这里。形式命题 C-55、C-56 与负控制不受影响。同目录新增的 `DelayMonad.agda`（C-59）另有 `CLAIM-C59.md`。

## 2026-09-25 · 会话 91a6cdaa（Terra 复审 013 §2.1、§2.3；CN-031；回信 014）

1. **C-55 “同一个程序”改为“同一泛型无界搜索骨架的不同语义实例”**（接受）。P-rev、C-50、C-51、步子列表四种规格共用 `StopProgram` 的搜索骨架，各自的停机谓词、判定过程、状态与过程表示、`after` 不同。它们是固定现实任务、只改变表示前提的受控比较（对“同一任务”的含义另见回信 014 §6）。
2. **“Delay 单子”**：原文件只有 Capretta 风格的余归纳 `Delay` 对象（接受 Terra 的指正）。C-59 为同一类型补上 `return`、`bind` 与三条单子律（路径），此后“Delay 单子”有本地证明。
3. **“≡ never”的含义**：原文件把路径读作互模拟。C-59 (c) 给出内部的观察刻画：`d ≡ never` 当且仅当对一切燃料 `runFor n d ≡ nothing`。它仍不是墙钟时间或真实设备上的运行证据（接受）。
4. **P-rev、P-carry 是规格的组成**，不是 HoTT 定理推出的现实义务（接受 Terra 013 §2.1 第 4 条）。它们的来源与归属见回信 014 §4、§8。
5. **C-56 的精确读法**（接受 Terra 013 §2.3）：原族满足 `subst Ped go 0 = +1`；被证明的是拉回族 `Pedᵣ x := Ped (reverse x)` 沿 `go` 为 `−1`。这是沿类型自等价拉回后的取向翻转（gauge/orientation symmetry），不是同一个 `Ped` 对同一 `go` 同时给出 `+1` 与 `−1`。标签改为 `FORMAL_ORIENTATION_SYMMETRY_OF_BARE_PLACES_MODEL / EVENT_ORIENTATION_IS_SEMANTIC_STRUCTURE / NO_PROOF_OF_NONREAL_OR_UNACCEPTABLE_COST`。给步子命名方向是“哪次行为算事件”这一任务本来需要的语义资料；012 已写明“是否算不可接受的成本，不替用户决定”。
