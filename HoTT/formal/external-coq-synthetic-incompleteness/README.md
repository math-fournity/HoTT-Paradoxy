# Coq synthetic essential incompleteness / Robinson Q 重放包

本目录冻结 `uds-psl/coq-synthetic-incompleteness` 的 `csl@cd7d8490f8542bfe85658c465bcb26b2ed163f53`，用于 `R3-SOURCE-REPLAY-001`。它是一般一阶算术/可枚举形式系统的机器化不完备性基准，不是 HoTT calculus 实例。

## 来源与许可证

- `upstream-cd7d849.tar.gz`：由 exact commit 的 `git archive` 生成，再以 gzip `mtime=0` 压缩；2,019,830 bytes，SHA-256 `5ffbeb284cbff764e8b11b6ac3aa1a1feb558c5b1372f60527e26581547c7c8a`；
- `SOURCE_TREE_MANIFEST.json`：807 个 tracked files / 7,423,361 bytes / derived tree SHA `d9dd001b0dcfcab4d183b01f0eeed9d16d12c09b576507ea7fc45c87505680ca`；
- `CeCILL_LICENSE.txt`：上游许可证原件，同时包含在 source archive 中；
- `SOURCE_ARCHIVE.json` 与 `IMPORT.json`：archive、manifest、license 和证据边界收据。

`scripts/audit/import_coq_synthetic_incompleteness.py` 是 archive/import 的 canonical manager。`validate` 不依赖外部 worktree；重新生成才需要 exact clean source checkout。

## 工具链与目标

`TOOLCHAIN.json` 固定 derived Docker image `hott-coq-synthetic-incompleteness:cd7d849`，Coq 8.15.2 / OCaml 4.07.1、Equations 1.3+8.15、Smpl 8.15、MetaCoq Template `dev+8.15@9493bb6`。`Dockerfile` 保存重建 recipe。

重放目标：

```text
make FOL/Incompleteness/fol_incompleteness.vo
```

`Qualification.v` 随后加载并打印：

- `self_halting_diverge`；
- `recursively_separating_diverge`；
- `insep_essential_incompleteness`；
- `epf_mu_ctq`；
- `Q_incomplete`；
- 后三者的 `Print Assumptions`。

运行：

```bash
python3 -B scripts/audit/import_coq_synthetic_incompleteness.py validate
python3 -B scripts/audit/replay_coq_synthetic_incompleteness.py
```

完整数学范围、前提和禁止外推见 `CLAIM-R3-SYNTHETIC-INCOMPLETENESS.md`。形成 F-011 交付证据后，run 必须进入 `HoTT/verification/runs/`，并在 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 登记 C-244–C-249。

## 边界

源码在 Coq 中形式化一般 first-order logic、Robinson Q 与 synthetic incompleteness。构建成功不会提供 `is_universal theta`、`CTQ`、Peirce 或对象理论一致性前提的 inhabitant，也不会把 `T` 实例化为 HoTT。对 HoTT 的 R4 连接仍须完成 `.codex/research/hott/R3-R4-GODEL-RETURN-001.md` 的逐义务矩阵。
