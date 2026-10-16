# ZFC-COFORGE-005-P1：L0–L7 可解释重跑

> **身份：** `EXTERNAL_CLI_BEHAVIOR_PROBE / P1_EXPLAINABLE_BLIND_REPLAY / NOT_A_ZFC_RESULT`。
>
> **结论：** `SOURCE_CONSUMER_GAP / NO_ZFC_Q_ON_NEUTRAL_CARD`。更新后的 P1 在中性静态 ZFC card 上没有用裸 membership relation 伪造真实 consumer；它明确指出下一步所缺的是 source-defined input/output/Done contract。

## 运行身份

| 字段 | 记录 |
|---|---|
| CLI | `codex-cli 0.157.0` |
| 工作根 | `/tmp/pattern-p-zfc-coforge-005-p1-l7` |
| 模型请求 / effort | `gpt-5.6-terra` / `max` |
| sandbox / approval | `read-only` / `never` |
| session | `01a0fcfd-e6f5-7ff2-a3ac-b920081a0b48` |
| 输入 | 中性 ZFC card + P1 L0–L7 + E0–E7 可复核输出要求；禁止项目历史、网络、命令和写入 |

## 代理的公开 E0–E7 理由链

### E0/E1：范围与事实

代理只把 card 中的集合、membership、幂集存在条件、有界 Separation、Replacement 与 Foundation 当作可用材料。它特别保留了两个限制：幂集在 card 中是存在／membership characterisation，而不是全局可执行 constructor；card 也没有 formula coding/satisfaction 或 construction machine。

### E2/E3：候选集与字段映射

| 路线 | `u/F` | `C` | `Q` | 角色 |
|---|---|---|---|---|
| A | 已给 a 和 card-supplied p，其中 p 的成员为 a 的子集 | **无 source-defined consumer** | `b∈p` | 最接近的幂集 membership 路线 |
| B | a 与其 p | **无 source-defined consumer** | `p∈p` | Foundation 控制邻近项 |

它拒绝把 Separation 的“using a formula”扩展为 formula truth/satisfaction 任务，因为 card 明示缺该能力。

### E4：逐门结果

路线 A 在 L0/L1/L4 仍有对象级、native formation 与基础接口资格；但在 L2b、L5、L7 失败：membership characterisation 没有给出 consumer task／Done，因而也没有 source demand 或 positive completion prerequisite。路线 B 另被 direct self-loop exclusion 拦住。A 的非反身性没有补出缺失的 consumer contract。

### E5：true / false / blocked

代理给出的最小链是 `a set → card supplies some p → atomic query b∈p`。它区分：

- true 只是 positive relation fact；
- false 也没有被 card 定义成任务失败或未完成；
- blocked 是任何要求构造 p、决定查询或消费结果的实际程序都超出 card。

所以该 card 上没有可以冻结的 `I/O/Done`，也没有可交给 P2/P3 的同一 Q。

### E6：反事实

代理给出的精确缺失 source fact 是：对满足幂集条件的 `(a,b,p)`，source 提供内部任务 `VerifyPowerMember(a,b,p)`，其成功 Done 必须产出正的 `b∈p` judgment。只有这一类规则才会同时提供 C、actual demand 和正 Done 前提。

### E7：判词

```text
SOURCE_CONSUMER_GAP
```

## 主研究者判词与范围

这次重跑在 L7 之外发现了更早的断裂：裸 relation 甚至未必能通过 L2。它因此驱动 L2b/consumer contract 的新增，并把下一来源需求收紧为“版本固定的真实 ZFC consumer source”。这不证明 ZFC 没有任何消费者，也不表明 Power Set 已被放弃；它仅证明当前中性卡不足以让 P1 产生受合同约束的 Q。
