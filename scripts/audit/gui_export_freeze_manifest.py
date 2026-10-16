#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUI 导出全行覆盖资产回收 · Phase 0/1 冻结与收据工具。

合同出处：SOP=GUI-EXPORT-ASSET-RECOVERY-SOP
  - 002 片 §1（行/字节定义）§2（Phase 0 身份冻结）§3（diff 式区间对齐）§5（manifest schema）
  - 003 片 §2-§3（收据哈希必须由脚本按行区间精确计算）
  - 004 片 §4（验证脚本合同，本脚本是其数据源）

行定义：content.split(b'\\n')；若末元素为空字符串则不计行数（002 §1）。
块哈希：raw[offsets[start-1]:offsets[end]]——首行首字节到末行换行符（若有）的连续切片。

对齐方法：git diff --no-index --unified=0（002 §3.2 允许的两法之一），解析 hunk 得到
极大相同行运行；≥3 行判 SHARED，其余 UNIQUE；多源候选按（长度降序，来源阅读顺序升序）
贪心选择不重叠区间；任何不确定一律 UNIQUE（002 §3.2.3 保守方向）。

用法：
  python3 -B scripts/audit/gui_export_freeze_manifest.py              # Phase 0+1，写 manifest.json
  python3 -B scripts/audit/gui_export_freeze_manifest.py --verify     # 只重算身份与 manifest 比对
  python3 -B scripts/audit/gui_export_freeze_manifest.py --receipt --rid R0001 --kind READ \
      --tag dev-08 --start 1 --end 400 --seq 1 --salient 9 --notes 'notes/dev-08.md#R0001' \
      [--class user_turn=1,codex_mid=2,...] [--reason '...'] [--append]
"""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
EXPORT_DIR = REPO / "git-worktree对话录"
OUT_DIR = REPO / "audit" / "GUI-ASSET-RECOVERY"
MANIFEST = OUT_DIR / "manifest.json"
LEDGER = OUT_DIR / "ledger.jsonl"

# 阅读顺序（逻辑分叉树，根优先；002 片 §3.2.1）
READ_ORDER = ["dev-08", "dev-03", "dev-04", "dev-02", "dev-06", "dev-07", "dev-01", "dev-09"]
MIN_RUN = 3  # ≥3 行才判 SHARED；<3 行相同运行按义务行读（002 §3.2.2）
SEED_LABEL = "GUI-ASSET-RECOVERY-v1"
SEED_FORMULA = ('seed = sha256("%s" + sha256(concat(file_sha256_hex for tag in sorted(tags))))'
                % SEED_LABEL)
DIFF_METHOD = ("git-diff --no-index --unified=0 --diff-algorithm=myers "
               "--no-indent-heuristic --no-color")


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def find_path(tag: str) -> Path:
    hits = sorted(EXPORT_DIR.glob("%s - *.md" % tag))
    if len(hits) != 1:
        raise SystemExit("ERROR: tag %s matched %d files" % (tag, len(hits)))
    return hits[0]


def split_lines(raw: bytes):
    """返回 (lines, offsets)；offsets[i] = 第 i+1 行首字节偏移，offsets[L] = len(raw)。"""
    parts = raw.split(b"\n")
    if parts and parts[-1] == b"":
        parts.pop()
    offsets = []
    pos = 0
    for p in parts:
        offsets.append(pos)
        pos += len(p) + 1
    offsets.append(pos)
    return parts, offsets


def chunk_sha256(raw: bytes, lines, offsets, start: int, end: int) -> str:
    """块 (start..end)（1 基含端点）的精确字节切片 SHA-256。"""
    assert 1 <= start <= end <= len(lines)
    return hashlib.sha256(raw[offsets[start - 1]:offsets[end]]).hexdigest()


def git_blob(path: Path):
    try:
        out = subprocess.run(["git", "ls-files", "-s", "--", str(path.relative_to(REPO))],
                             cwd=REPO, capture_output=True, text=True, check=True).stdout.strip()
        return out.split()[1] if out else None
    except Exception:
        return None


# ---------------------------------------------------------------- Phase 1 对齐

def git_diff_hunks(path_a: Path, path_b: Path):
    """跑 git diff --no-index -U0，返回 [(a_start,a_count,b_start,b_count), ...]（1 基）。"""
    cmd = ["git", "diff", "--no-index", "--unified=0", "--diff-algorithm=myers",
           "--no-indent-heuristic", "--no-color", "--src-prefix=a/", "--dst-prefix=b/",
           str(path_a), str(path_b)]
    proc = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    if proc.returncode not in (0, 1):
        raise SystemExit("git diff failed (%d): %s" % (proc.returncode, proc.stderr[:500]))
    hunks = []
    for ln in proc.stdout.splitlines():
        if ln.startswith("@@"):
            body = ln.split("@@", 2)[1]  # like " -12,3 +15,0 @@ ctx"
            seg = [s for s in body.split() if s.startswith(("-", "+"))]
            def parse(s):
                s = s[1:]
                return (int(s.split(",")[0]), int(s.split(",")[1])) if "," in s else (int(s), 1)
            a_s, a_c = parse(seg[0])
            b_s, b_c = parse(seg[1])
            hunks.append((a_s, a_c, b_s, b_c))
    return hunks


def same_runs_from_hunks(hunks, La: int, Lb: int):
    """把 hunk 序列转换为相同行运行 [(a_start,a_end,b_start,b_end)]（1 基含端点）。

    空侧 hunk（count=0）位置在该行号之后：same 可含 a_start；消耗推进 a_start+1。
    """
    runs = []
    pa, pb = 1, 1
    for a_s, a_c, b_s, b_c in hunks:
        a_same_end = a_s if a_c == 0 else a_s - 1
        b_same_end = b_s if b_c == 0 else b_s - 1
        if a_same_end >= pa and b_same_end >= pb:
            # 长度恒等由 diff 语义保证；不一致则抛错（防解析 bug 静默漏读）
            if (a_same_end - pa) != (b_same_end - pb):
                raise SystemExit("PARSE BUG: same-run length mismatch %r" % ((a_s, a_c, b_s, b_c),))
            runs.append((pa, a_same_end, pb, b_same_end))
        pa = a_s + a_c if a_c > 0 else a_s + 1
        pb = b_s + b_c if b_c > 0 else b_s + 1
    if pa <= La and pb <= Lb:
        if (La - pa) != (Lb - pb):
            raise SystemExit("PARSE BUG: tail same-run mismatch")
        runs.append((pa, La, pb, Lb))
    return runs


def align_all(file_data):
    """file_data: {tag: {path,lines,offsets,...}}。按 READ_ORDER 对齐，返回 per-tag ranges。

    ranges: [{start,end,status,src} ...] 全覆盖不重叠；src=[tag,s,e]。
    """
    covered = []  # 已进入内容库的 tag（阅读顺序）
    per_file = {}
    for tag in READ_ORDER:
        cur = file_data[tag]
        candidates = []  # (length, order_idx, f_start, f_end, src_tag, s_start, s_end)
        for oi, g in enumerate(covered):
            hunks = git_diff_hunks(file_data[g]["path"], cur["path"])
            for a_s, a_e, b_s, b_e in same_runs_from_hunks(hunks, file_data[g]["lines_n"], cur["lines_n"]):
                n = b_e - b_s + 1
                if n >= MIN_RUN:
                    candidates.append((n, oi, b_s, b_e, g, a_s, a_e))
        # 贪心：长度降序、来源阅读顺序升序、起点升序
        candidates.sort(key=lambda c: (-c[0], c[1], c[2]))
        chosen = []  # (f_start, f_end, src_tag, s_start, s_end) sorted by f_start
        for n, oi, f_s, f_e, g, s_s, s_e in candidates:
            if any(not (f_e < c[0] or f_s > c[1]) for c in chosen):
                continue
            chosen.append((f_s, f_e, g, s_s, s_e))
        chosen.sort()
        # 与上一轮（若有）重验逐字节相等——防贪心/解析错位
        for f_s, f_e, g, s_s, s_e in chosen:
            n = f_e - f_s + 1
            if s_e - s_s + 1 != n:
                raise SystemExit("ALIGN BUG: len mismatch %s %d-%d" % (tag, f_s, f_e))
            for k in range(n):
                if cur["lines"][f_s - 1 + k] != file_data[g]["lines"][s_s - 1 + k]:
                    raise SystemExit("ALIGN BUG: byte mismatch %s L%d vs %s L%d"
                                     % (tag, f_s + k, g, s_s + k))
        # 全覆盖区间表
        ranges = []
        pos = 1
        for f_s, f_e, g, s_s, s_e in chosen:
            if f_s > pos:
                ranges.append({"start": pos, "end": f_s - 1, "status": "UNIQUE"})
            ranges.append({"start": f_s, "end": f_e, "status": "SHARED", "src": [g, s_s, s_e]})
            pos = f_e + 1
        if pos <= cur["lines_n"]:
            ranges.append({"start": pos, "end": cur["lines_n"], "status": "UNIQUE"})
        per_file[tag] = ranges
        covered.append(tag)
    return per_file


# ---------------------------------------------------------------- Phase 0/1 主流程

def load_files():
    file_data = {}
    for tag in READ_ORDER:
        p = find_path(tag)
        raw = p.read_bytes()
        lines, offsets = split_lines(raw)
        file_data[tag] = {
            "path": p, "raw": raw, "lines": lines, "offsets": offsets,
            "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw), "lines_n": len(lines),
            "title_line": lines[0].decode("utf-8", "replace")[:200] if lines else "",
        }
    return file_data


def phase01():
    file_data = load_files()
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO,
                          capture_output=True, text=True, check=True).stdout.strip()
    # 抽样种子（002 §2.3）：sha256(label + sha256(按 tag 排序拼接的个体哈希))
    inner = hashlib.sha256(
        "".join(file_data[t]["sha256"] for t in sorted(READ_ORDER)).encode()).hexdigest()
    seed = hashlib.sha256((SEED_LABEL + inner).encode("utf-8")).hexdigest()

    alignment = align_all(file_data)
    per_file = []
    D = 0
    for tag in READ_ORDER:
        ranges = alignment[tag]
        u = sum(r["end"] - r["start"] + 1 for r in ranges if r["status"] == "UNIQUE")
        s = sum(r["end"] - r["start"] + 1 for r in ranges if r["status"] == "SHARED")
        fd = file_data[tag]
        assert u + s == fd["lines_n"], "interval cover assert failed for %s" % tag
        D += u
        per_file.append({
            "tag": tag, "lines": fd["lines_n"], "unique_lines": u, "shared_lines": s,
            "unique_ranges": [[r["start"], r["end"]] for r in ranges if r["status"] == "UNIQUE"],
            "ranges": ranges,
        })
    manifest = {
        "schema": "gui-asset-recovery/manifest/v1",
        "frozen_at": utcnow(), "head": head,
        "seed": seed, "seed_formula": SEED_FORMULA,
        "diff_method": DIFF_METHOD, "min_run": MIN_RUN,
        "files": [{
            "tag": t, "path": str(file_data[t]["path"].relative_to(REPO)),
            "sha256": file_data[t]["sha256"], "bytes": file_data[t]["bytes"],
            "lines": file_data[t]["lines_n"], "title_line": file_data[t]["title_line"],
            "blob": git_blob(file_data[t]["path"]),
        } for t in READ_ORDER],
        "alignment": {"method": DIFF_METHOD, "order": list(READ_ORDER), "per_file": per_file},
        "obligation_lines": D,
        "total_lines_all_files": sum(file_data[t]["lines_n"] for t in READ_ORDER),
        "sample": {"k_per_file": 20,
                   "rule": "h=sha256(seed+tag+':'+str(line_1based)); sort by hex asc, tie by line asc; take K"},
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    print("MANIFEST WRITTEN: %s" % MANIFEST)
    print("head=%s seed=%s" % (head, seed[:16]))
    print("T=%d  D=%d  (=%.1f%% of T)" % (manifest["total_lines_all_files"], D,
          100.0 * D / manifest["total_lines_all_files"]))
    for pf in per_file:
        print("  %-7s lines=%6d unique=%6d shared=%6d unique_ranges=%d" %
              (pf["tag"], pf["lines"], pf["unique_lines"], pf["shared_lines"], len(pf["unique_ranges"])))


def verify_identity():
    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    ok = True
    for f in man["files"]:
        p = REPO / f["path"]
        raw = p.read_bytes()
        h = hashlib.sha256(raw).hexdigest()
        match = (h == f["sha256"]) and (len(raw) == f["bytes"])
        lines, _ = split_lines(raw)
        match = match and (len(lines) == f["lines"])
        print("  %-7s %s (%d lines)" % (f["tag"], "MATCH" if match else "CHANGED", len(lines)))
        ok = ok and match
    print("IDENTITY: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def sample_lines(manifest) -> dict:
    """确定性抽样（004 §1.2）：每文件 K 行。返回 {tag: [line,...]} 行号升序展示。"""
    seed = manifest["seed"]
    out = {}
    for f in manifest["files"]:
        tag, L = f["tag"], f["lines"]
        scored = []
        for i in range(1, L + 1):
            h = hashlib.sha256(("%s%s:%d" % (seed, tag, i)).encode("utf-8")).hexdigest()
            scored.append((h, i))
        scored.sort()  # hex 升序，天然并列几乎不可能；tie 由第二键行号升序打破
        out[tag] = sorted(i for _, i in scored[:manifest["sample"]["k_per_file"]])
    return out


# ---------------------------------------------------------------- 收据辅助

def interlock_check(args, man, lines, offsets, raw):
    """003 片 §9.9 收据互锁（裁决 #2；fail-closed）。四前置全满足才返回，否则退出非零。"""
    errs = []
    # ① seq 连续：与账本末条 READ/RELOAD 的 seq +1
    last_seq = None
    if LEDGER.exists():
        for ln in LEDGER.read_text(encoding="utf-8").splitlines():
            try:
                r = json.loads(ln)
            except json.JSONDecodeError:
                continue
            if r.get("kind") in ("READ", "RELOAD"):
                last_seq = r.get("seq")
    if last_seq is None:
        if args.seq != 1:
            errs.append("①seq=%d 但账本无 READ/RELOAD（应为 1）" % args.seq)
    elif args.seq != last_seq + 1:
        errs.append("①seq=%d 不连续（账本末条 READ/RELOAD seq=%d）" % (args.seq, last_seq))
    # ② notes 已含本 rid 节（### <rid> 头，或批次节的「本节收据」行列明本 rid）
    notes = OUT_DIR / "notes" / ("%s.md" % args.tag)
    ntext = notes.read_text(encoding="utf-8") if notes.exists() else ""
    has_section = ("### %s " % args.rid) in ntext or ("### %s·" % args.rid) in ntext
    has_listing = re.search(r"本节收据[：:][^\n]*\b%s\b" % re.escape(args.rid), ntext)
    if not (has_section or has_listing):
        errs.append("②notes/%s.md 无 %s 节或本节收据列名" % (args.tag, args.rid))
    # ③ token-log 已含同 tag 覆盖本区间的记录
    tlog = OUT_DIR / "token-log.jsonl"
    tok_ok = False
    if tlog.exists():
        for ln in tlog.read_text(encoding="utf-8").splitlines():
            try:
                r = json.loads(ln)
            except json.JSONDecodeError:
                continue
            if (r.get("kind") == "TOKEN" and r.get("tag") == args.tag
                    and r.get("start", 10**9) <= args.start and r.get("end", 0) >= args.end):
                tok_ok = True
                break
    if not tok_ok:
        errs.append("③token-log.jsonl 无 %s 覆盖 L%d-%d 的记录（先跑 --log）"
                    % (args.tag, args.start, args.end))
    # ④ assets-ledger 含锚定于本区间的条目，或 notes 本节含显式「已读无资产」
    al = OUT_DIR / "assets-ledger.md"
    asset_ok = False
    if al.exists():
        for ln in al.read_text(encoding="utf-8").splitlines():
            if not ln.startswith("| A-"):
                continue
            for m in re.finditer(r"%s:L(\d+)" % re.escape(args.tag), ln):
                if args.start <= int(m.group(1)) <= args.end:
                    asset_ok = True
                    break
            if asset_ok:
                break
    no_asset = False
    if has_section or has_listing:
        # 在本 rid 所属节的文本内查「已读无资产」——批次节时以节内任一出现为准
        no_asset = "已读无资产" in ntext
    if not (asset_ok or no_asset):
        errs.append("④assets-ledger 无锚定 L%d-%d 的条目且 notes 无「已读无资产」"
                    % (args.start, args.end))
    if errs:
        print("INTERLOCK REFUSE %s %s:%d-%d" % (args.rid, args.tag, args.start, args.end))
        for e in errs:
            print("  " + e)
        sys.exit(3)


def append_receipt(args):
    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    fd = {f["tag"]: f for f in man["files"]}
    if args.tag not in fd:
        raise SystemExit("unknown tag %s" % args.tag)
    p = REPO / fd[args.tag]["path"]
    raw = p.read_bytes()
    lines, offsets = split_lines(raw)
    if hashlib.sha256(raw).hexdigest() != fd[args.tag]["sha256"]:
        raise SystemExit("REFUSE: file %s changed vs manifest" % args.tag)
    if not (1 <= args.start <= args.end <= len(lines)):
        raise SystemExit("bad range %d-%d (L=%d)" % (args.start, args.end, len(lines)))
    if args.append and not args.no_interlock:
        interlock_check(args, man, lines, offsets, raw)
    cc = {}
    if args.klass:
        for kv in args.klass.split(","):
            k, v = kv.split("=")
            cc[k.strip()] = int(v)
    rec = {
        "rid": args.rid, "kind": args.kind, "file_tag": args.tag,
        "start": args.start, "end": args.end, "n_lines": args.end - args.start + 1,
        "chunk_sha256": chunk_sha256(raw, lines, offsets, args.start, args.end),
        "seq": args.seq, "ts": utcnow(),
        "class_counts": cc, "salient_n": args.salient,
        "notes_ref": args.notes, "reload_reason": args.reason,
    }
    line = json.dumps(rec, ensure_ascii=False)
    if args.append:
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        with LEDGER.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")
        print("APPENDED %s %s:%d-%d sha=%s" % (args.rid, args.tag, args.start, args.end,
                                               rec["chunk_sha256"][:16]))
    else:
        print(line)


def main():
    try:
        _main()
    except SystemExit as e:
        if e.code not in (None, 0):
            # 互锁/合同拒绝（SystemExit(3) 等）已打印人类可读原因，安静退出
            sys.exit(e.code)
        raise


def _main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true", help="只核验身份")
    ap.add_argument("--sample", action="store_true", help="打印冻结种子的每文件 K=20 抽样行")
    ap.add_argument("--receipt", action="store_true", help="生成/追加一条收据")
    ap.add_argument("--rid"); ap.add_argument("--kind", default="READ")
    ap.add_argument("--tag"); ap.add_argument("--start", type=int); ap.add_argument("--end", type=int)
    ap.add_argument("--seq", type=int, default=0); ap.add_argument("--salient", type=int, default=0)
    ap.add_argument("--notes", default=None); ap.add_argument("--class", dest="klass", default="")
    ap.add_argument("--reason", default=None); ap.add_argument("--append", action="store_true")
    ap.add_argument("--no-interlock", action="store_true",
                    help="跳过 §9.9 收据互锁（仅 CORRECTION 复刻等非推进用途）")
    args = ap.parse_args()
    if args.receipt:
        append_receipt(args); return
    if args.verify:
        sys.exit(verify_identity())
    if args.sample:
        man = json.loads(MANIFEST.read_text(encoding="utf-8"))
        print(json.dumps(sample_lines(man), ensure_ascii=False, indent=1)); return
    phase01()


if __name__ == "__main__":
    main()
