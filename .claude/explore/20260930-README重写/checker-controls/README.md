# 负控制：README 检查脚本（2026-09-30，最终版本上重跑）

每个控制把 README（索引加七个分片）复制到临时目录，只改一处，再用 `--readme` 指向副本运行。期望退出码：旧快照为 3，其余为 1；真实 README 为 0。原始输出在同目录的 `.txt` 文件里（临时目录路径已替换为占位符）。

- neg-id：期望 1，实际 1，一致；报出：FAIL ids: DIR DIR-U-NOT-A-DIRECTION not found in its owner 
- neg-quote-block：期望 1，实际 1，一致；报出：FAIL quotes: 002 - 我们在找什么.md:17: not verbatim in KC-000048: 我觉得你还没有理解到一种精髓，就是悖论对理论的攻击角度，比如芝诺悖论对理论的攻击 
- neg-quote-inline：期望 1，实际 1，一致；报出：FAIL quotes: 003 - 历史.md:40: not verbatim in KC-000049: 我就是要和你认真探讨归因啊！ 
- neg-verdict：期望 1，实际 1，一致；报出：FAIL quotes: README.md:28: not verbatim in rulings.md: 本repo复苏了芝诺悖论的幽灵和罗素悖论的幽灵，并且找到的HoTT理论的问题。 
- neg-stale：期望 3，实际 3，一致；报出：STALE snapshot: state_revision is 289, owner says 290 
- neg-route：期望 1，实际 1，一致；报出：FAIL routes: direction DIR-W-ATTACHED-HISTORY is not on the route map 
- neg-path：期望 1，实际 1，一致；报出：FAIL paths: 001 - 当前入口与关键文件.md:88: missing path `history/不存在.md` 
- neg-link：期望 1，实际 1，一致；报出：FAIL paths: 001 - 当前入口与关键文件.md:18: missing link target ../不存在.md 
- 真实 README：期望 0，实际 0
