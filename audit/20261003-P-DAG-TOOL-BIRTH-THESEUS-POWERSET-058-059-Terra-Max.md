# P-DAG Tool-Birth 058–059：真实幂集消费者与忒修斯最终裁定

> **身份：** `HISTORY_INSENSITIVE_POWERSET_CONSUMER_NEGATIVE_CONTROL / FINAL_TOOL_BIRTH_NOT_ENOUGH_EVIDENCE / NOT_A_POWERSET_ATTACK_OR_NEW_TOOL_RESULT`。

## 1. H058：Mathlib NFA 是实际的幂集消费者

冻结来源为：

```text
/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/
mathlib4-5ed2965256430c3649e86755f9576b54eca72435/
Mathlib/Computability/NFA.lean
SHA-256: 42d15719f191c3125a1ec01be3f655471469df419420fdb76ad87ac1b342ab02
```

source 同时提供两种不同表示：

```text
Path                    concrete path for a word
evalFrom S x : Set σ    all possible ending states
acceptsFrom S           word accepted iff an accepting endpoint exists in evalFrom S x
```

它还明确给出 endpoint membership 与某条 concrete `Path` 存在之间的 bridge。因此 H058 可以完整填一个实际 task card：

| 字段 | 来源范围内的内容 |
|---|---|
| 输入 | initial state set `S` 与 word `x` |
| 表示转换 | possible paths → endpoint set `evalFrom S x` |
| consumer | `acceptsFrom S` 的 language membership |
| Done | endpoint set 中存在 accepting state |
| 路径历史 | `Path` 单独保留，但 acceptance 不要求比较路径身份 |

结论不是“历史不重要”。结论是：对这个**同一语言接受任务**，endpoint-set abstraction 正确地只保留“至少一条接受路径存在”的观察量；不同 Path 的持续身份不属于 Done。它是忒修斯／Power Set 思路的实际负控制。

## 2. H059：含真实消费者的最终 sealed-pack arbiter

H059 仅消费 H054 snapshot-loss clue、H055 history-preserving control、H056 bare extensionality/Power Set source、H058 NFA source。最终 ledger 为：

```text
P1: no actual history-sensitive consumer
P2: extensionality/power source has no trace or provenance judgment
P3: NFA endpoint abstraction is correct for existential acceptance, not identity Done
composition: history-preserving representation is a possible repair, not source-backed tool
Tool-Birth: NOT_ENOUGH_EVIDENCE
```

arbiter 明确拒绝三种过度结论：

```text
not OLD_TOOL_FIELD_GAP (no actual identity task yet)
not DERIVED_TOOL_CANDIDATE (no source says its composition is required)
not UNCONTAINED_PATTERN_CANDIDATE (no three independent distortion witnesses)
```

## 3. 当前 Power Set / Theseus 判词

```text
bare Power Set attack: NOT_LOCATED
new numbered tool: NOT PROPOSED
conditional interface: Trace–Snapshot–Identity only
current Tool-Birth verdict: NOT_ENOUGH_EVIDENCE
```

这不是否认忒修斯之船的研究价值。它把研究对象从“Power Set 是否没有历史”精确改为：

> 是否存在一个 source-defined consumer，把多个具有不同 immutable lineage 的过程压成同一 snapshot，并仍把 snapshot equality 当作“同一持续对象”的完成答案？

当前 source 没有这个 consumer。NFA source 反而提供一个反例：它压掉具体路径，却正确地保持了本任务唯一需要的可达／接受观察。

## 4. 运行与 trajectory 证据

| node | profile | terminal / elapsed | wire SHA-256 / terminal | 结论范围 |
|---|---|---|---|---|
| H058 | pinned local source-match | PASS / 65.102s | `8b0c9735ef5ba45d052469026980d83aa6c3ca207a3f5b1c90edab6970371220` / `:630` | actual history-insensitive powerset consumer negative control |
| H059 | sealed-pack source-match arbiter | PASS / 78.447s | `8e0fe96e58efcfd0863f66a839a9650dbd8938de7a963fc696a792f96ec0e191` / `:576` | final Tool-Birth `NOT_ENOUGH_EVIDENCE` |

两节点固定 `gpt-5.6-terra / max`、read-only、`approval=never`、project-external private root，prompt-input / exact start echo PASS，且 `0 command / 0 file change / 0 approval request`。两条 private wire均经 `session_trajectory.py` 的 `catalog → tree → coverage → assistant terminal inspect`。H058/H059 都跨越一个60秒观察窗并自然终态，没有自动中断。

## 5. 重开条件

只有一个固定 source 同时给出下列事实，才重开这条线：

1. history/provenance 到 snapshot 的明确 projection；
2. 一个 consumer 的输入、观察与 Done；
3. consumer 必须就“continuation vs reconstruction”给出不同答案；
4. consumer 却只得到 snapshot equality 或被禁止使用已存在的 lineage；
5. history-preserving control 不能保持该 same-task Done。

在此之前，不应把 NFA、extensionality、Power Set 或忒修斯名称的相似性升级为 ZFC Q、P4 或理论缺陷。
