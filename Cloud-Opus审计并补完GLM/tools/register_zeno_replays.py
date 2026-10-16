#!/usr/bin/env python3
"""Append evidence-index and matrix rows for the 16 Zeno-line Linux replays (Cloud-Opus, 2026-09-27).

Run once, from the repository root, after tools/capture_zeno_line_replays.sh; prints the rows of
appendix A of docs/社区审计提交/01-芝诺悖论的幽灵.md.  Not idempotent (appends)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNS = ROOT / "HoTT/verification/runs"
PAIRS = [
    ("SST-FINITE-LEVELS", "CG001-C-62", "sst-finite-levels/SSTLevels.agda", "sst-finite-levels/WrongFace.agda"),
    ("WILD-SST", "CG001-C-64", "wild-sst/WildSST.agda", "wild-sst/WrongSpinCoherent.agda"),
    ("WILD-SST-LEAN", "CG001-C-65", "wild-sst-lean/WildSSTUIP.lean", "wild-sst-lean/WrongRoute.lean"),
    ("WILD-SST2", "CG001-C-66", "wild-sst/WildSST2.agda", "wild-sst/WrongSurfTrivial.agda"),
    ("SELF-INTERPRETATION", "CG001-C-67", "self-interpretation/SelfInterpretation.agda", "self-interpretation/WrongFlipIsIdentity.agda"),
    ("WILD-SST-P4", "CG001-C-68", "wild-sst/WildSSTP4Flat.agda", "wild-sst/WrongSurfMoveTrivial.agda"),
    ("WINDING-COCYCLE", "CG001-C-69", "wild-sst/WindingCocycle.agda", "wild-sst/WrongSpinWCocycle.agda"),
    ("WILD-SST-LEVELS", "CG001-C-70", "wild-sst/WildSSTP4Levels.agda", "wild-sst/WrongS2Groupoid.agda"),
]
CLAIM_TEXT = {
    "CG001-C-62": "`SST≤0 … SST≤5 : Type₁` 与平凡居民（外部生成器逐层打印）",
    "CG001-C-64": "`WildSST`、`Coh₂`、`setsCohere`；`spin`：两条路线绕 1 圈与 2 圈，`spinIncoherent : ¬ Coh₂ spin`",
    "CG001-C-65": "Lean 4（UIP）：`theorem coh2 (S : WildSST) : Coh2 S := fun _ _ _ _ _ _ _ => rfl`",
    "CG001-C-66": "`surf≢refl`；`flat` 上两个不同的六边形填充；`Deg₃` 对一个成立、对另一个不成立",
    "CG001-C-67": "玩具语法自解释两难：`faithful∞`、`syntax∞IsNotASet`、`noFaithfulForFacts`",
    "CG001-C-68": "一般第二级相干 `Coh₃`（P₄）：`notCoh₃ : ¬ Coh₃ flatSurfᵢ`、`coh₃Trivial : Coh₃ flatTrivialᵢ`",
    "CG001-C-69": "圆周值结构上 `Coh₂` ⇔ 绕数上闭链方程；`spinW` 不相干、`uniformW` 相干",
    "CG001-C-70": "集合 ⇒ `Coh₂ᵢ`；群胚 ⇒ `Coh₂ᵢ` 为命题且 `Coh₃` 成立；`flatS¹` 数据唯一",
}


def run_info(run_id):
    d = json.loads((RUNS / run_id / "RUN.json").read_text(encoding="utf-8"))
    stage = d.get("rejection_stage")
    tag = d.get("agda_error_tag")
    return d["exit_code"], d["status"], round(d["duration_seconds"]), stage, tag, d.get("outcome_matches_expectation")


def main():
    idx_proof, idx_run, idx_claim, mat_pkg, mat_claim, appendix = [], [], [], [], [], []
    for name, claim, pos_src, neg_src in PAIRS:
        pid, nid = f"MP-CG001-{name}-001", f"MP-CG001-{name}-NEG-001"
        prun, nrun = f"20260927-COPUS-REPLAY-CG001-{name}-01", f"20260927-COPUS-REPLAY-CG001-{name}-NEG-01"
        pe, ps, pt, _, _, pm = run_info(prun)
        ne, ns, nt, nstage, ntag, nm = run_info(nrun)
        why = ntag or nstage or "?"
        idx_proof.append(f"| `{pid}` | `HoTT/formal/claude-cg001/{pos_src}` | 接受 | Opus 原 proof id（{claim}），本会话 Linux 重放（芝诺线） |")
        idx_proof.append(f"| `{nid}` | `HoTT/formal/claude-cg001/{neg_src}` | 拒绝 | Opus 原负控制，本会话 Linux 重放 |")
        idx_run.append(f"| `{prun}` | {pid} | exit {pe}（{pt} s），{ps} |")
        idx_run.append(f"| `{nrun}` | {nid} | exit {ne}，{ns}（`{why}`） |")
        idx_claim.append(f"| `{claim}` | {CLAIM_TEXT[claim]} | Opus 原运行 `20260926-CG001-{name}-01`、`-NEG-01`；本会话 Linux 重放 `-REPLAY-CG001-{name}-01`、`-NEG-01` | 【数学事实】Opus 的主张，本会话只重放 |")
        mat_pkg.append(f"| `{pid}` | `{claim}` | `formal/claude-cg001/{pos_src}` | `verification/runs/{prun}/`；exit {pe} | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |")
        mat_pkg.append(f"| `{nid}` | `{claim}` 负控制 | `formal/claude-cg001/{neg_src}` | `verification/runs/{nrun}/`；exit {ne}，`{why}` | `NEGATIVE_CONTROL_REJECTED` |")
        mat_claim.append(f"| {claim} | {CLAIM_TEXT[claim]} | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-{name}-01`、`{prun}`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |")
        appendix.append(f"| {claim} | `{prun}` | exit {pe}，{ps}（{pt} s） | `{nrun}` | exit {ne}，{ns}，`{why}` | {'是' if (pm and nm) else '否'} |")
    idx = ROOT / "Cloud-Opus审计并补完GLM/证据索引.md"
    s = idx.read_text(encoding="utf-8")
    s += ("\n### 4.4 芝诺线（Opus 的 A7）Linux 重放（2026-09-27，为社区审计稿 01 捕获）\n\n"
          "> 捕获命令 `tools/capture_zeno_line_replays.sh`；proof id 与 claim id 是 Opus 的（CG-001 目标内索引），原 macOS 收据不动。\n\n"
          "| proof id | 源文件 | 预期 | 说明 |\n|---|---|---|---|\n" + "\n".join(idx_proof) + "\n\n"
          "| run id | proof id | 结果 |\n|---|---|---|\n" + "\n".join(idx_run) + "\n\n"
          "| claim | 形式命题（摘） | 证据 | 身份 |\n|---|---|---|---|\n" + "\n".join(idx_claim) + "\n")
    idx.write_text(s, encoding="utf-8")
    mat = ROOT / "HoTT/CLAIM_EVIDENCE_MATRIX.md"
    m = mat.read_text(encoding="utf-8")
    m += ("\n#### 芝诺线（Opus 的 A7：无穷相干）的 Linux 重放（2026-09-27）\n\n"
          "> 为 `docs/社区审计提交/01-芝诺悖论的幽灵.md` 捕获。Agda v2.8.0 Linux 资产 + cubical v0.9（逐字节一致）；Lean 4.34.0 Linux 资产（与原工具链同一源码 commit）。Opus 的原运行 `20260926-CG001-*` 保持原样。\n\n"
          "| Package ID | Claim IDs | 源码 | 证据 | 判词 |\n|---|---|---|---|---|\n" + "\n".join(mat_pkg) + "\n\n"
          "| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |\n|---|---|---|---|---|\n" + "\n".join(mat_claim) + "\n")
    mat.write_text(m, encoding="utf-8")
    print("\n".join(appendix))
    print("registered", len(PAIRS), "pairs")


if __name__ == "__main__":
    main()
