#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the curated tree of the `main` branch from a commit of the `dev` branch.

The main branch holds only what supports the conclusions (researcher, 2026-09-30: "把当前这个repo的main分支整理好，
然后改名为dev分支，然后把main分支腾出来。专门放支撑结论的关键性内容。").  Everything is read from one source
commit, never from the working tree, so the result is determined by (commit, spec):

* docs, proof packages, toolchain records and run receipts listed in scripts/release/main-release-spec.json;
* a closure check: every source file named in an included receipt's source-manifest.json must be included and
  must have the recorded SHA-256 at the source commit, or the build fails;
* CLAIMS.md, copied verbatim from three places on dev (two sections of HoTT/CLAIM_EVIDENCE_MATRIX.md, the
  goal-local relay rows and the claim one-liners of the Claude master index), plus a generated run table;
* README.md from scripts/release/main-README.md, tools/replay.py from scripts/release/replay.py;
* RELEASE-MANIFEST.json: every file with its SHA-256 and role, the runs, the units, and the paths that the
  documents mention but that stay on dev.

Usage:
  python3 -B scripts/release/build_main_release.py --source <commit-ish> --out <empty directory>
The output directory may already contain a `.git` entry (a worktree of the main branch); nothing else.
Exit 0 on success; any closure, hash or extraction problem aborts with a message.
"""
from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[2]
SPEC = "scripts/release/main-release-spec.json"
README_TEMPLATE = "scripts/release/main-README.md"
REPLAY = "scripts/release/replay.py"
GITIGNORE = "_build/\n*.agdai\n*.olean\n__pycache__/\n"


def git(*args: str) -> bytes:
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True).stdout


def blob(commit: str, path: str) -> bytes:
    try:
        return git("show", f"{commit}:{path}")
    except subprocess.CalledProcessError:
        raise SystemExit(f"MISSING_AT_SOURCE:{path}")


def tracked(commit: str, prefix: str) -> list[str]:
    out = git("ls-tree", "-r", "-z", "--name-only", commit, "--", prefix).decode("utf-8")
    return sorted(p for p in out.split("\0") if p)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def section(text: str, heading: str) -> str:
    """Body of a level-2 section: the lines after `heading` up to the next level-2 heading."""
    lines = text.split("\n")
    starts = [i for i, line in enumerate(lines) if line.strip() == heading]
    if len(starts) != 1:
        raise SystemExit(f"SECTION_NOT_UNIQUE:{heading}:{len(starts)}")
    body = []
    for line in lines[starts[0] + 1:]:
        if line.startswith("## "):
            break
        body.append(line)
    return "\n".join(body).strip("\n")


def table_rows(text: str, first_cells: list[str]) -> list[str]:
    rows = []
    for cell in first_cells:
        hits = [line for line in text.split("\n") if line.startswith(f"| `{cell}` |") or line.startswith(f"| {cell} |")]
        if len(hits) != 1:
            raise SystemExit(f"ROW_NOT_UNIQUE:{cell}:{len(hits)}")
        rows.append(hits[0])
    return rows


def path_mentions(text: str) -> set[str]:
    found = set()
    for m in re.finditer(r"`([^`\n]+)`", text):
        found.add(re.sub(r"[:：]\d[\d,–\-]*$", "", m.group(1).strip()).rstrip("/"))
    for m in re.finditer(r"\]\(([^)\n]+)\)", text):
        target = m.group(1).strip().strip("<>").split("#")[0]
        if target and not re.match(r"[a-z]+://", target):
            found.add(target)
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", required=True, help="commit-ish on dev to build from")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    commit = git("rev-parse", "--verify", f"{args.source}^{{commit}}").decode().strip()
    commit_date = git("show", "-s", "--format=%cI", commit).decode().strip()
    spec = json.loads(blob(commit, SPEC))
    repo = spec["repository"]

    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    leftovers = [p.name for p in out.iterdir() if p.name != ".git"]
    if leftovers:
        raise SystemExit(f"OUTPUT_NOT_EMPTY:{leftovers[:5]}")

    files: dict[str, dict] = {}

    def add(path: str, role: str) -> None:
        if path in files:
            return
        data = blob(commit, path)
        files[path] = {"role": role, "data": data}

    for path in spec["docs"]:
        add(path, "CONCLUSION_DOCUMENT")
    for package in spec["packages"]:
        members = tracked(commit, package)
        if not members:
            raise SystemExit(f"EMPTY_PACKAGE:{package}")
        for path in members:
            add(path, "PROOF_PACKAGE")
    for path in spec["files"]:
        add(path, "TOOLCHAIN_RECORD")

    on_dev_closure = {row["path"]: row["reason"] for row in spec.get("closure_on_dev", [])}
    on_dev_seen: dict[str, dict] = {}
    runs = []
    for run_id in spec["runs"]:
        prefix = f"HoTT/verification/runs/{run_id}"
        members = tracked(commit, prefix)
        if not members:
            raise SystemExit(f"MISSING_RUN:{run_id}")
        for path in members:
            add(path, "RUN_RECEIPT")
        record = json.loads(blob(commit, f"{prefix}/RUN.json"))
        manifest = json.loads(blob(commit, f"{prefix}/source-manifest.json"))
        for row in manifest.get("files", []):
            path = row["path"]
            if path not in files and path in on_dev_closure:
                if sha(blob(commit, path)) != row["sha256"]:
                    raise SystemExit(f"SOURCE_HASH_MISMATCH:{run_id}:{path}")
                entry = on_dev_seen.setdefault(path, {"path": path, "sha256": row["sha256"], "reason": on_dev_closure[path],
                                                      "dev_url": f"{repo}/blob/dev/{quote(path, safe='/')}", "named_by_runs": []})
                entry["named_by_runs"].append(run_id)
                continue
            if path not in files:
                if spec.get("auto_closure"):
                    add(path, "AUXILIARY_DEPENDENCY")
                else:
                    raise SystemExit(f"CLOSURE_MISSING:{run_id}:{path}")
            if sha(files[path]["data"]) != row["sha256"]:
                raise SystemExit(f"SOURCE_HASH_MISMATCH:{run_id}:{path}")
        exit_code = record.get("exit_code")
        if not isinstance(exit_code, int):
            raise SystemExit(f"RUN_WITHOUT_EXIT_CODE:{run_id}")
        claims = record.get("claim_ids") or []
        if isinstance(claims, str):
            claims = [claims]
        runs.append({
            "run_id": run_id, "proof_id": record.get("proof_id"), "claim_ids": claims,
            "proof_assistant": record.get("proof_assistant"), "recorded_status": record.get("status"),
            "recorded_exit": exit_code, "expected": "accepted" if exit_code == 0 else "rejected",
            "captured_cwd": record.get("cwd"),
        })

    # units: a run belongs to a unit when one of its claim ids matches one of the unit's patterns
    units = {}
    for key, unit in spec["units"].items():
        members = [r["run_id"] for r in runs
                   if any(fnmatch.fnmatch(c.replace("`", ""), pat) for c in r["claim_ids"] for pat in unit["claims"])]
        units[key] = {"title": unit["title"], "claims": unit["claims"], "runs": members}
    unassigned = [r["run_id"] for r in runs if not any(r["run_id"] in u["runs"] for u in units.values())]

    # CLAIMS.md
    cs = spec["claims_sources"]
    parts = [
        "# 命题与证据",
        "",
        f"> 本文件由 `dev` 上的 `scripts/release/build_main_release.py` 从提交 `{commit[:8]}` 生成，不在本分支修改。第 1、2 节逐字取自 `dev` 上共享证据矩阵 "
        "`HoTT/CLAIM_EVIDENCE_MATRIX.md` 的两节（不含原标题行）；第 3 节逐字取自 `dev` 上的目标内索引草稿与 Claude 总索引；第 4 节由各运行的收据生成。"
        "文中 `formal/…`、`verification/runs/…` 指本分支 `HoTT/` 下的同名路径；其余过程文件的路径在 `dev` 上（见 README 第 5 节）。",
        "",
    ]
    titles = ["## 1. 罗素线与 UR：追问程序、邻近对照与截断对照", "## 2. Cloud-Opus 的审计与补完：宇宙塔的一般 n、高阶归纳类型证书、GLM 线与跨平台重放"]
    order = [1, 0]  # the Claude section first, then the Cloud-Opus section
    sections = cs["matrix_sections"]
    for title, idx in zip(titles, order):
        src = sections[idx]
        parts += [title, "", f"> 来源：`dev` 上 `{src['file']}` 的“{src['heading'][3:]}”一节。", "",
                  section(blob(commit, src["file"]).decode("utf-8"), src["heading"]), ""]
    relay = cs["relay_rows"]
    relay_text = blob(commit, relay["file"]).decode("utf-8")
    one = cs["claim_one_liners"]
    one_text = blob(commit, one["file"]).decode("utf-8")
    parts += [
        "## 3. 芝诺线、Delay 语义与共用对照",
        "",
        "> 这些命题的行在 `dev` 上的目标内索引里（`.claude/goals/CG-001-targeted-overview/relay.md` 的 R1 草稿），尚未登记进共享矩阵；"
        "每个运行另有逐字节重放的输出，在 `dev` 上的 `.claude/goals/CG-001-targeted-overview/verification/`。命题全文与禁止外推以各包的 `CLAIM.md` 为准。",
        "",
        "### 3.1 证明包与运行（逐字）",
        "",
        "| Package ID | Claim IDs | 源码 | 证据 | 判词 |",
        "|---|---|---|---|---|",
        *table_rows(relay_text, relay["proof_ids"]),
        "",
        "### 3.2 命题一句话（逐字）",
        "",
        "| 命题 | 一句话 | 包 |",
        "|---|---|---|",
        *table_rows(one_text, one["claims"]),
        "",
        "## 4. 运行清单",
        "",
        "| 运行 | 证明 | 命题 | 证明器 | 记录的结局 | 单元 |",
        "|---|---|---|---|---|---|",
    ]
    for r in runs:
        member_of = "、".join(k for k, u in units.items() if r["run_id"] in u["runs"]) or "—"
        claims = "、".join(c.replace("`", "") for c in r["claim_ids"]) or "—"
        parts.append(f"| `{r['run_id']}` | `{r['proof_id']}` | {claims} | {r['proof_assistant']} | "
                     f"{'接受' if r['expected'] == 'accepted' else '被拒（预期）'}，exit {r['recorded_exit']}，`{r['recorded_status']}` | {member_of} |")
    claims_md = ("\n".join(parts).rstrip("\n") + "\n").encode("utf-8")

    # paths that the documents mention but that stay on dev
    included = set(files)
    mentioned = set()
    for path in spec["docs"]:
        text = files[path]["data"].decode("utf-8")
        base = os.path.dirname(path)
        for token in path_mentions(text):
            for candidate in (token, os.path.join(base, token)):
                norm = os.path.normpath(candidate)
                if norm in (".", "") or norm.startswith(".."):
                    continue
                if git("ls-tree", commit, "--", norm).strip():
                    mentioned.add(norm)
                    break
    def in_release(path: str) -> bool:
        return path in included or any(p.startswith(path.rstrip("/") + "/") for p in included)
    on_dev = sorted(p for p in mentioned if not in_release(p) and git("ls-tree", commit, "--", p).strip())
    rows = ["| 路径 | 在 `dev` 上 |", "|---|---|"]
    for p in on_dev:
        kind = "tree" if git("ls-tree", commit, "--", p).decode().split()[1] == "tree" else "blob"
        rows.append(f"| `{p}` | [打开]({repo}/{kind}/dev/{quote(p, safe='/')}) |")
    dev_table = "\n".join(rows)

    link_rewrites: dict[str, list] = {}
    for path in spec["docs"]:
        text = files[path]["data"].decode("utf-8")
        base = os.path.dirname(path)
        changed = []

        def fix(m: "re.Match[str]") -> str:
            raw = m.group(2)
            target = raw.strip()
            bracketed = target.startswith("<") and target.endswith(">")
            bare = target[1:-1] if bracketed else target
            if re.match(r"[a-z]+://", bare) or bare.startswith("#"):
                return m.group(0)
            file_part, _, anchor = bare.partition("#")
            norm = os.path.normpath(os.path.join(base, file_part))
            if in_release(norm) or not git("ls-tree", commit, "--", norm).strip():
                return m.group(0)
            kind = "tree" if git("ls-tree", commit, "--", norm).decode().split()[1] == "tree" else "blob"
            url = f"{repo}/{kind}/dev/{quote(norm, safe='/')}" + (f"#{anchor}" if anchor else "")
            changed.append({"from": bare, "to": url})
            return f"{m.group(1)}({url})"

        new_text = re.sub(r"(\[[^\]\n]*\])\(([^)\n]+)\)", fix, text)
        if changed:
            files[path]["data"] = new_text.encode("utf-8")
            files[path]["role"] = "CONCLUSION_DOCUMENT_LINKS_TO_DEV"
            link_rewrites[path] = changed

    replay_py = blob(commit, REPLAY)
    accepted = sum(1 for r in runs if r["expected"] == "accepted")
    generated = {
        "CLAIMS.md": claims_md,
        "tools/replay.py": replay_py,
        ".gitignore": GITIGNORE.encode("utf-8"),
    }
    file_total = len(files) + len(generated) + 2  # + README.md and RELEASE-MANIFEST.json
    readme = blob(commit, README_TEMPLATE).decode("utf-8")
    for key, value in {"REPO": repo, "SOURCE_COMMIT": commit, "SOURCE_SHORT": commit[:8], "RUN_TOTAL": str(len(runs)),
                       "RUN_ACCEPTED": str(accepted), "RUN_REJECTED": str(len(runs) - accepted),
                       "FILE_TOTAL": str(file_total), "DEV_PATHS_TABLE": dev_table}.items():
        readme = readme.replace("{{" + key + "}}", value)
    if "{{" in readme:
        raise SystemExit("README_PLACEHOLDER_LEFT")
    generated["README.md"] = readme.encode("utf-8")

    manifest = {
        "schema_version": "hott-paradoxy-main-release/v1",
        "release_id": spec["release_id"],
        "repository": repo,
        "source": {"branch": spec["dev_branch"], "commit": commit, "commit_date": commit_date, "spec": SPEC,
                   "spec_sha256": sha(blob(commit, SPEC))},
        "purpose": spec["purpose"],
        "authorization": spec["authorization"],
        "principle": spec["principle"],
        "counts": {"files": file_total, "runs": len(runs), "runs_accepted": accepted, "runs_rejected_as_expected": len(runs) - accepted},
        "units": units,
        "runs_without_unit": unassigned,
        "runs": runs,
        "paths_mentioned_but_on_dev": on_dev,
        "receipt_sources_kept_on_dev": sorted(on_dev_seen.values(), key=lambda e: e["path"]),
        "document_links_rewritten_to_dev": link_rewrites,
        "files": [{"path": p, "role": v["role"], "bytes": len(v["data"]), "sha256": sha(v["data"]), "source": "dev:" + commit[:8]}
                  for p, v in sorted(files.items())]
                 + [{"path": p, "role": "GENERATED", "bytes": len(d), "sha256": sha(d)} for p, d in sorted(generated.items())],
    }
    generated["RELEASE-MANIFEST.json"] = (json.dumps(manifest, ensure_ascii=False, indent=1) + "\n").encode("utf-8")

    for path, entry in files.items():
        target = out / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(entry["data"])
    for path, data in generated.items():
        target = out / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    (out / "tools/replay.py").chmod(0o755)
    print(json.dumps({"status": "BUILT", "source": commit, "files": file_total, "runs": len(runs), "accepted": accepted,
                      "units": {k: len(u["runs"]) for k, u in units.items()}, "runs_without_unit": unassigned,
                      "paths_on_dev": len(on_dev)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
