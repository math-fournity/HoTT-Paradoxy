# T2：一次性授权能力与普通 Cubical 上下文的最小对照

> 状态：`FORMAL_STATEMENT_FROZEN / PROOF_SOURCE_PERSISTED / RUN_NOT_YET_CAPTURED`
>
> 候选：`T2-ONESHOT-AUTHORIZATION-CODE-001`。
>
> Proof ID：`MP-TERRA-T2-ONESHOT-001`。

## 对象、理论变体与任务边界

本包使用 Cubical Agda 2.8.0-3d04bac 与 Cubical library v0.9，选项为
`--safe --cubical --guardedness`。它只固定两种小型表示：

```text
bare model:       Code → Token
stateful model:   Code → Server → Reply × Server
```

现实任务的来源对照是 OAuth 2.0 authorization-code grant：同一个授权码不得被
client 使用超过一次；重复使用时 authorization server 必须拒绝请求。这里的
`Server` 只是可检查的模型状态，不是对 OAuth server、PKCE、TLS、client binding、
并发原子性、数据库或安全性质的实现。

## 形式命题

| Claim | Cubical Agda 命题 | 精确支持范围 |
|---|---|---|
| `C-354` | `duplicate : {A : Type} → A → A × A`，且 `duplicate authorizationCode ≡ (authorizationCode, authorizationCode)`。 | 一个普通 Cubical 乘积接口允许同一 `Code` 值同时作为两个分量出现；它是**可复制数据表示**的事实。 |
| `C-355` | 在指定的 bare `pureRedeem : Code → Token` 中，`pureTwice authorizationCode ≡ (accessToken, accessToken)`。 | 这个具体纯接口会把两个使用位置都算作成功；不是关于全部纯函数的定理。 |
| `C-356` | 同一个 `duplicatedCode` 的两份分量按顺序作用于同一个 `Server`：首次 result 是 `granted accessToken`，第二次是 `denied`，最终 state 为 `consumed` 且 log 是 `[grantAttempt, denialAttempt]`。 | 一个显式 stateful server transition 能让同一外部 code 输入的第一次兑换成功、第二次拒绝，并在同一 primitive transition 中留下可观察的两个尝试。 |

## 禁止外推

- 不证明 HoTT Book 的全部正式规则、所有 Cubical 系统或每个现实类型都有同样的产品/资源语义；
- 不证明 OAuth server 的生产安全性、并发线性化、抗重放、PKCE/TLS、认证、令牌撤销或审计保留；
- 不证明 ordinary HoTT 在任何表示中都不能静态保证一次性使用；更不证明“它必然不能表示一次性任务”；
- 不证明量化／线性类型扩展与 HoTT 的全部兼容性；
- 不证明现实相对 HoTT 悖论。它是 T2 的 bare-interface 负控制和 stateful 同任务正控制。
