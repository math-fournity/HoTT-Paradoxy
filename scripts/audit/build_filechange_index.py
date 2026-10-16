#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FileChange 胶囊真索引生成器（设计者审计修复 F1；2026-10-07）

从八份 GUI 导出机械重扫全部 FileChange 胶囊行（固定格式：反引号路径 + em-dash + 操作），
结合 manifest 的 SHARED/UNIQUE 区间标注，产出：

  audit/GUI-ASSET-RECOVERY/D3-FILECHANGE-INDEX.md   全局唯一 (path,op) 清单＋统计
  audit/GUI-ASSET-RECOVERY/D3-FILECHANGE-TIMELINE.tsv  全量出现时间线（每行一次出现）

复现：python3 -B scripts/audit/build_filechange_index.py
"""
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BASE = REPO / "audit" / "GUI-ASSET-RECOVERY"
CAP = re.compile(r"^- `(/[^`]+)` — (\S+)")


def range_status(ranges, line):
    for r in ranges:
        if r["start"] <= line <= r["end"]:
            return r["status"]
    return "?"


def main():
    man = json.loads((BASE / "manifest.json").read_text(encoding="utf-8"))
    files = {f["tag"]: f for f in man["files"]}
    order = man["alignment"]["order"]
    ranges = {f["tag"]: f["ranges"] for f in man["alignment"]["per_file"]}
    occ = []  # (tag_order, tag, line, path, op, status)
    for oi, tag in enumerate(order):
        lines = Path(files[tag]["path"]).read_text(encoding="utf-8").split("\n")
        for i, l in enumerate(lines, 1):
            m = CAP.match(l)
            if m:
                occ.append((oi, tag, i, m.group(1), m.group(2), range_status(ranges[tag], i)))
    # 全局唯一 (path,op)
    best = {}
    counts = {}
    also = {}
    for oi, tag, i, p, op, st in occ:
        k = (p, op)
        counts[k] = counts.get(k, 0) + 1
        if k not in best or (oi, i) < (best[k][0], best[k][2]):
            best[k] = (oi, tag, i, st)
        also.setdefault(k, set()).add(tag)
    rows = sorted(best.items(), key=lambda kv: (kv[1][0], kv[1][2]))
    # 输出 TSV
    with (BASE / "D3-FILECHANGE-TIMELINE.tsv").open("w", encoding="utf-8") as f:
        f.write("file\tline\tpath\top\trange_status\n")
        for oi, tag, i, p, op, st in sorted(occ, key=lambda x: (x[0], x[2])):
            f.write(f"{tag}\t{i}\t{p}\t{op}\t{st}\n")
    # 输出 MD
    per_tag = {}
    for oi, tag, i, p, op, st in occ:
        d = per_tag.setdefault(tag, [0, 0, set()])
        d[0] += 1
        if st == "UNIQUE":
            d[1] += 1
        d[2].add(p)
    with (BASE / "D3-FILECHANGE-INDEX.md").open("w", encoding="utf-8") as f:
        f.write("# D3 附表 · FileChange 胶囊真索引（审计修复 F1）\n\n")
        f.write("> 生成：`python3 -B scripts/audit/build_filechange_index.py`（设计者，2026-10-07）；")
        f.write("机械重扫八份导出的胶囊行，SHARED/UNIQUE 依 manifest。全量出现时间线见 ")
        f.write("`D3-FILECHANGE-TIMELINE.tsv`（13,237 行）；本表为全局唯一 (path,操作) 清单。\n\n")
        f.write("## 统计\n\n| 文件 | 胶囊出现 | 其中UNIQUE段 | 涉及唯一路径 |\n|---|---|---|---|\n")
        for tag in order:
            d = per_tag.get(tag, [0, 0, set()])
            f.write(f"| {tag} | {d[0]} | {d[1]} | {len(d[2])} |\n")
        f.write(f"| **合计** | **{len(occ)}** | — | **{len({p for _, _, _, p, _, _ in occ})}** |\n\n")
        f.write(f"## 全局唯一清单（{len(rows)} 条 (路径,操作)；按首现排序）\n\n")
        f.write("| 路径 | 操作 | 首现 | 段 | 次数 | 也见于 |\n|---|---|---|---|---|---|\n")
        for (p, op), (oi, tag, i, st) in rows:
            others = sorted(also[(p, op)] - {tag}, key=order.index)
            f.write(f"| `{p}` | {op} | {tag}:L{i} | {st} | {counts[(p, op)]} | "
                    f"{' '.join(others) if others else '—'} |\n")
    print(f"occurrences={len(occ)} unique(path,op)={len(rows)} unique_paths={len({p for _, _, _, p, _, _ in occ})}")


if __name__ == "__main__":
    main()
