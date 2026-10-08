#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUI 导出全行覆盖资产回收 · 验证脚本（D1 的机器裁判）。

合同出处：SOP=GUI-EXPORT-ASSET-RECOVERY-SOP 002 片 §4（验证脚本合同）、004 片 §1-§2。

检查项：
  [1] 重算八文件身份 → 与 manifest 比对（任一改变 → FAIL 并提示 002 §2 失效流程）
  [2] 重放 Phase 1 对齐 → 与 manifest.alignment 逐条比对；每条 SHARED 区间逐字节重验相等；
      区间全覆盖、不重叠、Σ=行数（002 §3.2.4 断言）
  [3] 账本每条 READ/RELOAD 收据：按行区间重算字节切片哈希比对；READ 区间 ⊆ UNIQUE；
      RELOAD 不限（可指向 SHARED，003 §5）；rid 唯一；区间单调性不做要求（RELOAD 可回跳）
  [4] 全行归类：UNIQUE 行 ∩ READ∪RELOAD 区间 = covered；remainder = D − covered
  [5] 抽样（004 §1）：按冻结种子重算每文件 K=20 行；
      --final 时与 coverage.json 的 quotes 逐条比对（引文=行原文或前200字符规则）
  [6] 输出 coverage.json（机器）+ stdout 明细（人类）；exit 0 iff 全 PASS

用法：
  python3 -B scripts/audit/verify_gui_line_coverage.py            # 常规（执行期增量验证）
  python3 -B scripts/audit/verify_gui_line_coverage.py --final    # 终期（含引文比对；remainder≠0 → FAIL）
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gui_export_freeze_manifest as freeze  # noqa: E402

REPO = freeze.REPO
OUT_DIR = freeze.OUT_DIR
MANIFEST = freeze.MANIFEST
LEDGER = freeze.LEDGER
COVERAGE_JSON = OUT_DIR / "coverage.json"

LEDGER_DATA_KINDS = {"READ", "RELOAD"}
LEDGER_META_KINDS = {"SESSION_START", "RESUME", "FILE_DONE", "CHECKPOINT", "CORRECTION",
                     "PROTOCOL_NOTE", "REALIGN"}
QUOTE_MAX = 200  # 004 §1.3：>200 字符 → 前 200 + 总字符数 + 整行 SHA-256


def quote_line(line_bytes: bytes) -> dict:
    """按 004 §1.3 规则生成引文对象。"""
    try:
        text = line_bytes.decode("utf-8")
    except UnicodeDecodeError:
        text = line_bytes.decode("utf-8", "replace")
    if len(text) <= QUOTE_MAX:
        return {"verbatim": text}
    return {"head200": text[:200], "chars": len(text),
            "sha256": hashlib.sha256(line_bytes).hexdigest()}


def load_ledger():
    if not LEDGER.exists():
        return []
    recs = []
    for i, ln in enumerate(LEDGER.read_text(encoding="utf-8").splitlines(), 1):
        ln = ln.strip()
        if not ln:
            continue
        try:
            recs.append(json.loads(ln))
        except json.JSONDecodeError as e:
            raise SystemExit("LEDGER PARSE FAIL line %d: %s" % (i, e))
    return recs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--final", action="store_true", help="终期模式：抽样引文比对 + remainder 必须=0")
    args = ap.parse_args()

    results = {"checks": [], "pass": True}
    def check(name, ok, detail=""):
        results["checks"].append({"name": name, "ok": bool(ok), "detail": detail})
        print("[%s] %s%s" % ("PASS" if ok else "FAIL", name, (" — " + detail) if detail else ""))
        if not ok:
            results["pass"] = False

    man = json.loads(MANIFEST.read_text(encoding="utf-8"))

    # [1] 身份
    fd_all = freeze.load_files()
    id_ok = True
    for f in man["files"]:
        d = fd_all[f["tag"]]
        if (d["sha256"] != f["sha256"] or d["bytes"] != f["bytes"]
                or d["lines_n"] != f["lines"]):
            id_ok = False
            print("  identity mismatch: %s" % f["tag"])
    check("1_identity", id_ok,
          "T=%d D=%d seed=%s" % (man["total_lines_all_files"], man["obligation_lines"],
                                 man["seed"][:16]))

    # [2] 对齐重放
    replay = freeze.align_all(fd_all)
    al_ok = True
    shared_verified = 0
    pf_map = {pf["tag"]: pf for pf in man["alignment"]["per_file"]}
    for tag in freeze.READ_ORDER:
        if replay[tag] != pf_map[tag]["ranges"]:
            al_ok = False
            print("  alignment replay mismatch: %s" % tag)
        lines = fd_all[tag]["lines"]
        pos = 1
        for r in pf_map[tag]["ranges"]:
            if r["start"] != pos:
                al_ok = False
            if r["end"] < r["start"] or r["end"] > fd_all[tag]["lines_n"]:
                al_ok = False
            if r["status"] == "SHARED":
                g, s_s, s_e = r["src"]
                n = r["end"] - r["start"] + 1
                if s_e - s_s + 1 != n:
                    al_ok = False
                else:
                    seg_a = lines[r["start"] - 1:r["end"]]
                    seg_b = fd_all[g]["lines"][s_s - 1:s_e]
                    if seg_a != seg_b:
                        al_ok = False
                        print("  SHARED byte mismatch: %s %d-%d vs %s %d-%d"
                              % (tag, r["start"], r["end"], g, s_s, s_e))
                    else:
                        shared_verified += n
            pos = r["end"] + 1
        if pos - 1 != fd_all[tag]["lines_n"]:
            al_ok = False
    check("2_alignment_replay", al_ok, "shared_bytes_verified=%d lines" % shared_verified)

    # UNIQUE 行集合与区间表
    unique_spans = {t: [tuple(x) for x in pf_map[t]["unique_ranges"]]
                    for t in freeze.READ_ORDER}
    D = man["obligation_lines"]

    # [3] 账本收据
    recs = load_ledger()
    lines_of = {t: fd_all[t]["lines"] for t in freeze.READ_ORDER}
    raw_of = {t: fd_all[t]["raw"] for t in freeze.READ_ORDER}
    off_of = {t: fd_all[t]["offsets"] for t in freeze.READ_ORDER}
    rids = set()
    hash_ok, span_ok, meta_ok = True, True, True
    covered = {t: set() for t in freeze.READ_ORDER}
    receipts_by_tag = {t: 0 for t in freeze.READ_ORDER}
    n_read = n_reload = 0
    # 003§3 纠错语义的机器实现：CORRECTION 可带 voids:[rid]，
    # 被 void 的 READ 在 hash/3b/coverage 中跳过（账本仍保留原收据，append-only）。
    voided = set()
    for rec in recs:
        if rec.get("kind") == "CORRECTION":
            for v in rec.get("voids", []) or []:
                voided.add(v)
    for rec in recs:
        k = rec.get("kind")
        if k in LEDGER_META_KINDS:
            continue
        if k not in LEDGER_DATA_KINDS:
            meta_ok = False
            print("  unknown ledger kind: %r" % k)
            continue
        if rec["rid"] in voided:
            print("  VOIDED by CORRECTION: %s %s:%d-%d"
                  % (rec["rid"], rec.get("file_tag"), rec["start"], rec["end"]))
            continue
        if rec["rid"] in rids:
            meta_ok = False
            print("  duplicate rid: %s" % rec["rid"])
        rids.add(rec["rid"])
        t = rec["file_tag"]
        if t not in lines_of:
            span_ok = False
            continue
        s, e = rec["start"], rec["end"]
        h = freeze.chunk_sha256(raw_of[t], lines_of[t], off_of[t], s, e)
        if h != rec["chunk_sha256"]:
            hash_ok = False
            print("  hash mismatch: %s %s:%d-%d" % (rec["rid"], t, s, e))
        if k == "READ":
            for a, b in unique_spans[t]:
                lo, hi = max(s, a), min(e, b)
                if lo <= hi:
                    covered[t].update(range(lo, hi + 1))
            # READ 必须完全落在 UNIQUE 内
            for ln in range(s, e + 1):
                if not any(a <= ln <= b for a, b in unique_spans[t]):
                    span_ok = False
                    print("  READ outside UNIQUE: %s %s:%d" % (rec["rid"], t, ln))
                    break
            n_read += 1
        else:
            n_reload += 1
            if not rec.get("reload_reason"):
                meta_ok = False
                print("  RELOAD missing reason: %s" % rec["rid"])
        receipts_by_tag[t] += 1
    check("3_receipt_hash", hash_ok)
    check("3b_receipt_span", span_ok)
    check("3c_ledger_meta", meta_ok,
          "read=%d reload=%d meta=%d" % (n_read, n_reload, len(recs) - n_read - n_reload))

    # [4] remainder
    covered_total = sum(len(v) for v in covered.values())
    remainder = D - covered_total
    per_file_rows = []
    for t in freeze.READ_ORDER:
        u = pf_map[t]["unique_lines"]
        c = len(covered[t])
        per_file_rows.append({
            "tag": t, "lines": fd_all[t]["lines_n"], "shared": pf_map[t]["shared_lines"],
            "unique": u, "covered": c, "remainder": u - c,
            "receipts": receipts_by_tag[t],
            "covered_pct": round(100.0 * c / u, 1) if u else 100.0,
        })
    cov_ok = remainder == 0 if args.final else True
    check("4_coverage%s" % ("_final" if args.final else ""), cov_ok,
          "D=%d covered=%d remainder=%d" % (D, covered_total, remainder))
    for row in per_file_rows:
        print("    %-7s unique=%6d covered=%6d remainder=%5d receipts=%3d" %
              (row["tag"], row["unique"], row["covered"], row["remainder"], row["receipts"]))

    # [5] 抽样
    sample = freeze.sample_lines(man)
    quotes = {}
    sample_detail = "k=%d/file seed frozen" % man["sample"]["k_per_file"]
    if args.final:
        cov = json.loads(COVERAGE_JSON.read_text(encoding="utf-8")) if COVERAGE_JSON.exists() else {}
        q_ok = bool(cov.get("quotes"))
        for t in freeze.READ_ORDER:
            for ln in sample[t]:
                q = quote_line(lines_of[t][ln - 1])
                quotes.setdefault(t, {})[str(ln)] = q
                got = (cov.get("quotes") or {}).get(t, {}).get(str(ln))
                if got != q:
                    q_ok = False
                    print("  quote mismatch: %s:%d" % (t, ln))
        check("5_sample_quotes", q_ok, sample_detail)
    else:
        print("[SKIP] 5_sample_quotes (非终期) — %s" % sample_detail)

    # [6] 汇总输出
    out = {
        "schema": "gui-asset-recovery/coverage/v1",
        "generated_at": freeze.utcnow(), "final": bool(args.final),
        "manifest_seed": man["seed"], "head": man["head"],
        "total_lines": man["total_lines_all_files"], "obligation_lines": D,
        "covered": covered_total, "remainder": remainder,
        "per_file": per_file_rows,
        "receipt_counts": {"read": n_read, "reload": n_reload},
        "sample_lines": sample,
        "quotes": quotes if args.final else None,
        "checks": results["checks"], "overall": results["pass"],
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    COVERAGE_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\nOVERALL: %s  (coverage.json written; remainder=%d%s)" %
          ("PASS" if results["pass"] else "FAIL", remainder,
           "; FINAL 要求 remainder=0" if args.final else ""))
    sys.exit(0 if results["pass"] else 1)


if __name__ == "__main__":
    main()
