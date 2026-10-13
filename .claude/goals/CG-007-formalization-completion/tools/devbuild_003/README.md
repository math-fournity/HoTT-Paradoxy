# devbuild_003：本会话（🌟 003 - Step）的隔离编译缓存

## 为什么存在

`devbuild_ns.py` 把 `_state.json` 与 `.olean` 写在**同一份**共享缓存目录
（`.claude/goals/CG-007-formalization-completion/tools/devbuild_ns/<pkg>/`）。
两个会话同时在 `cg007-w8-d3` 上编译时会互相覆盖，产出**假错误 / 假回归**
（舰队记录：003-Flash 曾观测到一次「20 错误」回归，根因即此）。

## 用法

与本会话无关的会话请继续用 `devbuild_ns.py`。本会话用：

```
python3 -B .claude/goals/CG-007-formalization-completion/tools/devbuild_003/devbuild_ns.py \
    HoTT/formal/claude-cg001/godel-q-zfc-z0-full <GodelQ/... .lean> ...
```

唯一改动：`build = SCRATCH / "devbuild_003" / pkg.name`（其余逻辑与上游逐字相同）。

## 边界

- 这是**开发迭代**用的。正式收据仍走 `capture_run.py`（沙箱 + 独立临时目录，本就不共享缓存）。
- 本目录可整体删除重算，不是证据。
