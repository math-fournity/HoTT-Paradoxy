#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUI-ASSET 自检 helper（设计者工具；多战役基座版，2026-10-07）

模式一 · token 覆盖检查（每块第 5 拍自查 / 回填验收 / 终期复跑）：
  python3 -B scripts/audit/gui_asset_token_check.py --tag dev-08 --start 1 --end 5957 \
      [--base audit/GUI-ASSET-RECOVERY] [--notes notes/dev-08.md] [--ledger assets-ledger.md] \
      [--whitelist A,B,...] [--log]
  --base：战役工作目录（默认第一战役 audit/GUI-ASSET-RECOVERY；复算重读战役用
  audit/GUI-ASSET-REAUDIT）。--log 把结果追加到 <base>/token-log.jsonl。

模式二 · protocol-echo 锚句校验（压缩/会话边界后的执行力度证明）：
  python3 -B scripts/audit/gui_asset_token_check.py --echo-file <文件> \
      --echo-kind RESUME|SESSION_START|CL_BR|REAUDIT_RESUME|REAUDIT_SESSION_START|REAUDIT_CL_BR|<其他非空串> \
      [--base audit/GUI-ASSET-REAUDIT] [--anchors-file PROTOCOL-ANCHORS.json]
  锚表只存 SHA-256 与提示；全匹配才 OK；提交原文存档至 <base>/echo/ 并追加 <base>/echo-log.jsonl。
  --anchors-file 相对 --base 解析（默认 PROTOCOL-ANCHORS.json）。

退出码：0 = 通过/全覆盖或全豁免；1 = 缺失或锚未全匹配；2 = 输入/身份错误。
"""
import argparse
import collections
import hashlib
import json
import re
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
VERDICT = re.compile(r"\b[A-Z][A-Z0-9]{2,}(?:_[A-Z0-9]+)+\b")
GATES = re.compile(r"\b(?:D-L\d+[A-Z]?|L[0-9]+[a-z]?|H0\d\d|RK-0|P[0-9]-F-\d+)\b")


def utcnow() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def token_mode(args, base: Path) -> int:
    manifest = base / "manifest.json"
    if not manifest.exists():
        print(f"manifest.json 不存在（{manifest}）：先执行该战役的 Phase 0/1")
        return 2
    man = json.loads(manifest.read_text(encoding="utf-8"))
    fd = {f["tag"]: f for f in man["files"]}
    if args.tag not in fd:
        print(f"unknown tag {args.tag}")
        return 2
    p = REPO / fd[args.tag]["path"]
    raw = p.read_bytes()
    if hashlib.sha256(raw).hexdigest() != fd[args.tag]["sha256"]:
        print("REFUSE: 语料文件相对 manifest 已改变")
        return 2
    lines = raw.decode("utf-8").split("\n")
    if not (1 <= args.start <= args.end <= len(lines)):
        print(f"bad range {args.start}-{args.end} (L={len(lines)})")
        return 2

    notes_path = base / (args.notes or f"notes/{args.tag}.md")
    hay = notes_path.read_text(encoding="utf-8") if notes_path.exists() else ""
    if args.ledger:
        lp = base / args.ledger
        if lp.exists():
            hay += "\n" + lp.read_text(encoding="utf-8")
    wl = {w.strip() for w in args.whitelist.split(",") if w.strip()}

    tok = collections.Counter()
    for i in range(args.start - 1, args.end):
        for m in VERDICT.findall(lines[i]):
            if len(m) >= 8:
                tok[m] += 1
        for m in GATES.findall(lines[i]):
            tok[m] += 1
    missing = sorted((t for t in tok if t not in hay and t not in wl), key=lambda t: -tok[t])
    exempt = sorted((t for t in tok if t in wl and t not in hay))
    total, covered = len(tok), len(tok) - len(missing)
    pct = 100.0 * covered / total if total else 100.0
    print(f"tag={args.tag} L{args.start}-{args.end}: token类={total} 覆盖={covered} ({pct:.1f}%) "
          f"未豁免缺失={len(missing)} 豁免且缺失={len(exempt)}")
    for t in missing:
        print(f"  MISSING {t} x{tok[t]}")
    for t in exempt:
        print(f"  EXEMPT  {t} x{tok[t]}")
    if args.log:
        rec = {"kind": "TOKEN", "tag": args.tag, "start": args.start, "end": args.end,
               "total": total, "covered": covered, "missing": len(missing), "ts": utcnow()}
        with (base / "token-log.jsonl").open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return 0 if not missing else 1


def echo_mode(args, base: Path) -> int:
    anchors_path = base / (args.anchors_file or "PROTOCOL-ANCHORS.json")
    if not anchors_path.exists():
        print(f"锚表不存在：{anchors_path}")
        return 2
    anchors = json.loads(anchors_path.read_text(encoding="utf-8"))["anchors"]
    ep = Path(args.echo_file)
    if not ep.exists():
        print(f"echo 文件不存在：{ep}")
        return 2
    lines = [l.rstrip("\r") for l in ep.read_text(encoding="utf-8").split("\n")]
    hashes = {hashlib.sha256(l.encode("utf-8")).hexdigest() for l in lines if l.strip()}
    results, ok_all = [], True
    for a in anchors:
        ok = a["sha256"] in hashes
        ok_all &= ok
        results.append((a["id"], a["hint"], ok))
    matched = sum(1 for _, _, ok in results if ok)
    (base / "echo").mkdir(exist_ok=True)
    archive = base / "echo" / f"{args.echo_kind}-{utcnow().replace(':', '')}.txt"
    archive.write_text("\n".join(lines), encoding="utf-8")
    rec = {"kind": "ECHO", "echo_kind": args.echo_kind, "ts": utcnow(),
           "anchors_total": len(anchors), "anchors_matched": matched, "ok": ok_all,
           "archive": archive.relative_to(base).as_posix()}
    with (base / "echo-log.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"protocol-echo[{args.echo_kind}] base={base.name}: 锚句 {matched}/{len(anchors)} 匹配；存档 {archive.name}")
    for aid, hint, ok in results:
        print(f"  {'PASS' if ok else 'FAIL'} {aid} ({hint})")
    return 0 if ok_all else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="audit/GUI-ASSET-RECOVERY",
                    help="战役工作目录（repo 相对）；REAUDIT 战役用 audit/GUI-ASSET-REAUDIT")
    ap.add_argument("--tag")
    ap.add_argument("--start", type=int)
    ap.add_argument("--end", type=int)
    ap.add_argument("--notes")
    ap.add_argument("--ledger")
    ap.add_argument("--whitelist", default="")
    ap.add_argument("--log", action="store_true", help="token 结果落 <base>/token-log.jsonl")
    ap.add_argument("--echo-file", help="切换到 protocol-echo 模式：执行者摘出的锚句文件")
    ap.add_argument("--echo-kind", help="边界类型（自由字符串，非空；如 RESUME/CL_BR/REAUDIT_RESUME）")
    ap.add_argument("--anchors-file", help="锚表文件名（相对 --base，默认 PROTOCOL-ANCHORS.json）")
    args = ap.parse_args()
    base = REPO / args.base
    if args.echo_file:
        if not args.echo_kind or not args.echo_kind.strip():
            print("--echo-kind 必填（非空）")
            return 2
        return echo_mode(args, base)
    if not (args.tag and args.start and args.end):
        print("需要 --tag/--start/--end（或改用 --echo-file 模式）")
        return 2
    return token_mode(args, base)


if __name__ == "__main__":
    sys.exit(main())
