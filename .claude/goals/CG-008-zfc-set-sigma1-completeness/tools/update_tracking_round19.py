#!/usr/bin/env python3
"""Record round 19 in 形式化追踪/ (line-01 README + 99-更新日志)."""
from pathlib import Path

R = Path("形式化追踪")

LOG_LINE = (
    "| 2026-10-13 | 有哥德尔路线 | CG-008 P3 第二十三轮（本会话）：**round 19 收据化 + "
    "两条收窄合成核对为**正交**，不是「靶子又小一圈」**。**① 收据**：run "
    "`2026-10-13-CG001-CG008-AXSTEP-SPLIT-01`，proof_id `MP-CG001-GODEL-Q-ZFC-Z0-CG008-014`，"
    "claims `CG001-C-143`/`CG001-C-144`；97 源（闭包由导入图算出，末个 = `CG008TargetShape.lean`）、"
    "553 外部件 pin 校验通过、stderr 0 B、exit 0；verifier `verify_cg001_run.py --rerun` "
    "**PASS_WITH_SCOPE**（`replay = EXACT_EXIT_STDOUT_STDERR_MATCH`），全部定理公理只有 "
    "propext、Classical.choice、Quot.sound。**② 合成核对**（`CG008TargetShape.lean`，`b1a19fbb`）："
    "`godel_is_standard` —— `gödel`（`ProvabilityAbstraction/Basic.lean:188`）是**元层定义**，"
    "故 `⌜𝐆⌝` 是**标准**码；于是 002-Step 的单实例收窄（B）**没有**绕开非标准码那道墙（A）。"
    "**两条收窄正交**：B 减少的是「需要多少条 D3」，A 减少的是「证一条 D3 需要什么」；"
    "合起来是「只需证 `𝐆` 上这一条，而证它时只剩非标准公理码那一支」，**不是**「`𝐆` 的非标准码」"
    "（`𝐆` 没有非标准码）。另机器化：`z0_of_finalTarget`（`FinalTarget` ⟹ 完整形式 Z0，经单实例定理，"
    "**不需整族 `MinimalGap`**）与 `finalTarget_of_minimalGap`（**单向**）。"
    "**③ 工具坑（已修）**：收据 manifest 的 `external_dependencies` 必须是 "
    "`{label,local_path,bytes,sha256}` **行**的 list，不是 `make_z0_pins.py` 返回的 dict"
    "（原先在 `EXTERNAL_DEPENDENCY_ROW_INVALID` 被拒）；另 capture 的源清单原先从 /tmp 读，"
    "已改为读仓库内 `CG-008/tools/z0_r20_closure.txt`（**不要依赖 /tmp**）。"
    "**仍未证**：`hD3G`、`MinimalGap`（= C）、`AxStep_induction`、`FinalTarget`、单实例；"
    "`Z0Blocked.lean:65` 的未证标记仍在。**完整形式 Z0 未证成，不交付** | 本次工作 |\n"
)

ROW_TAIL_OLD = "见 [02 节](02-Z0-条件形式与剩余三步.md) |"

ROW_TAIL_NEW = (
    "见 [02 节](02-Z0-条件形式与剩余三步.md)。**2026-10-13（CG-008 P3 第十九/二十三轮）**："
    "缺口劈成「有限 / 归纳」两半且**有限半边与标准码支已证**（`axStep_finite_proved`、"
    "`axStep_standard_code`），故缺口精确到**非标准的归纳实例码**；两条收窄（非标准码 × 单实例）"
    "经机器核对为**正交**；run `2026-10-13-CG001-CG008-AXSTEP-SPLIT-01` 收据化"
    "（97 源、553 外部件、verifier PASS_WITH_SCOPE）|"
)

STEP3_ANCHOR = "缺口=ZFC 内部化 Σ1 完全性（集合论 D3），Foundation 无集合论版本，因此**不交付 Z0 为已证**；"

STEP3_NEW = (
    STEP3_ANCHOR
    + "**2026-10-13 起缺口进一步精确到 `AxStep_induction` 的「非标准归纳实例码」一支**"
    + "（有限半边与标准码支均已证，见本轮 99-更新日志）；"
)


def main() -> None:
    log = R / "99-更新日志.md"
    t = log.read_text(encoding="utf-8")
    log.write_text(t + LOG_LINE, encoding="utf-8")

    rm = R / "01-有哥德尔路线/README.md"
    tr = rm.read_text(encoding="utf-8")
    assert ROW_TAIL_OLD in tr and STEP3_ANCHOR in tr
    tr = tr.replace(ROW_TAIL_OLD, ROW_TAIL_NEW, 1).replace(STEP3_ANCHOR, STEP3_NEW, 1)
    rm.write_text(tr, encoding="utf-8")
    print("tracking updated")


if __name__ == "__main__":
    main()
