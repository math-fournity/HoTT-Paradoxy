# dedekind-omega-missile

Dedekind-Ω 簇（Book §11.2 实数完备性与 Ω 选择）双发导弹的发射包。
方案链：`PREMISE-001/008`（供给）→ `修订片 022/023/024`（判据 / 齐射 / 执行纪律）。

- `MissileOneProcessLayer.agda` —— 第一枚（过程层），已发射：
  `pell-gap-never-closes` / `gap-never-zero`，`KERNEL_ACCEPTED_WITH_SCOPE`。
- `CLAIM-PACKAGE.md` —— 精确命题、量词、假设、禁止外推、falsifier。
- `TOOLCHAIN.json` / `AGDA_LIBRARIES` —— 工具链身份与库路径（与
  `HoTT/formal/ercf-truncation-defense/` 同一 Agda 2.8.0 + cubical v0.9 身份）。

## 重跑（火控命令）

```bash
python3 scripts/audit/capture_agda_proof_run.py \
  --run-id 20260917-MP-DEDEKIND-OMEGA-M1-04 \
  --proof-id MP-DEDEKIND-OMEGA-M1 \
  --claim-id CAND-F2-7-M1 \
  --source HoTT/formal/dedekind-omega-missile/MissileOneProcessLayer.agda \
  --toolchain HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json \
  --scope "纯 Cubical Agda（--safe --cubical --guardedness，无 LEM、无 resizing、无追加公理）中证明 √2 的 Pell 最优有理夹钳序列判别式恒为交替 ±1，故对任意 n 不为 0——夹钳两端在 ℚ 上永不相遇。这是 PROCESS_DECLARATION_GAP 的过程层机械锚点，不是 HoTT 内部矛盾。" \
  --non-goal "不证明 ∀ q:ℚ, q·q≠2（全称无理性，第二枚目标）；不声称 HoTT 不一致；不声称实数完备性非现实可交付。"
```

约 30–60s（库接口已缓存；首次需编译 `Cubical.Tactics.CommRingSolver`，数分钟）。
收据写入 `HoTT/verification/runs/<run-id>/`，含 `RUN.json`、`stdout.txt`、
`stderr.txt`、`environment.txt`、`source-manifest.json`。

## 已知陷阱（三次被拒的代价，见 run -01/-02/-03）

1. `--guardedness` 必需，缺它会以 `InfectiveImport` 被拒。
2. `¬_` 不在 `Cubical.Data.Empty.Base`；在模块内 `private ¬_ : Type₀ → Type₀`。
3. cubical Path 下**不可用荒模式 `()`**；改用库引理 `znots` / `injPos` / `posNotnegsuc`。
