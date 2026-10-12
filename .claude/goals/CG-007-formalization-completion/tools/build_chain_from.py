#!/usr/bin/env python3
"""build_chain_from.py <package-dir> <entry-module>

按 import 传递闭包计算出编译次序并打印（每个模块一行）。
用法：
    python3 -B build_chain_from.py <pkg> GodelQ/ZFC/ShCraigElimSetupQ.lean

配合 devbuild_ns.py 重建整个依赖链（缓存被清掉时很有用）：
    MODS=$(python3 -B build_chain_from.py <pkg> <entry>)
    python3 -B devbuild_ns.py <pkg> $MODS
"""
import io, re, sys, pathlib

pkg = pathlib.Path(sys.argv[1]).resolve()
entry = sys.argv[2]
root = pkg

seen, order = [], []

def imps_of(path):
    out = []
    for line in io.open(root / path, encoding="utf-8").read().split("\n"):
        m = re.match(r"^import\s+(\S+)", line)
        if m:
            rel = m.group(1).replace(".", "/") + ".lean"
            if (root / rel).exists():
                out.append(rel)
    return out

def visit(path):
    if path in seen:
        return
    seen.append(path)
    for d in imps_of(path):
        visit(d)
    order.append(path)

visit(entry)
print("\n".join(order))
