#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检查 mineru_md/ 下 9 份 full.md 与 _upload/ 9 份 PDF 的对应关系。

仅作完整性证书的机器侧自检；不评估 OCR 质量、不调用 Sub Agent。
"""
import os, sys, hashlib

ROOT = "/Volumes/D/HoTT_AI_HANDOFF_20260911"
BASE = "docs/罗素解决考古/搜索原始响应-20261017"
UP   = os.path.join(ROOT, BASE, "_upload")
MD   = os.path.join(ROOT, BASE, "mineru_md")

NINE = [
    "zermelo1908-pp261-281.pdf",
    "rieger-foundation.pdf",
    "probe-mineru-test.pdf",
    "probe-clean.pdf",
    "kanamori.pdf",
    "kunen1980_part01_p001-163.pdf",
    "kunen1980_part02_p164-325.pdf",
    "enderton1977_part01_p001-150.pdf",
    "enderton1977_part02_p151-289.pdf",
]

ok = 0
for n in NINE:
    src = os.path.join(UP, n)
    md  = os.path.join(MD, n.replace(".pdf", ".md"))
    if not os.path.isfile(src):
        print(f"  [MISS PDF] {n}")
        continue
    if not os.path.isfile(md):
        print(f"  [MISS MD ] {n}  (expected {os.path.basename(md)})")
        continue
    sz_pdf = os.path.getsize(src)
    sz_md  = os.path.getsize(md)
    h_pdf  = hashlib.sha256(open(src, "rb").read()).hexdigest()[:16]
    if sz_md < 1000:
        print(f"  [TOO SMALL] {n}  pdf={sz_pdf} {h_pdf}  md={sz_md}")
        continue
    print(f"  [OK       ] {n:45s} pdf={sz_pdf:>9d} {h_pdf}  md={sz_md:>9d}")
    ok += 1
print(f"\n{ok}/{len(NINE)} PASS")
sys.exit(0 if ok == len(NINE) else 1)
