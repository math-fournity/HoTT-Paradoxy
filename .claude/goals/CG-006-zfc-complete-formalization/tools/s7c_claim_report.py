import json, collections, sys
d = json.load(open(sys.argv[1]))
ids = sorted({int(k) for r in d.values() for k in list(r["claims"].keys())+list(r["pkgs"].keys())})
for n in ids:
    variants = collections.defaultdict(list)
    for ref, r in d.items():
        t = r["claims"].get(str(n)); p = r["pkgs"].get(str(n))
        if t or p:
            variants[(t or "")[:80]].append((ref.replace("origin/",""), ",".join(r["proofs"].get(str(n), []))[:70], ",".join(p or [])[:70]))
    mark = "COLLISION" if len([k for k in variants if k]) > 1 else ""
    print(f"C-{n} {mark}")
    for k, v in variants.items():
        print(f"   [{k or '(no matrix row)'}]\n      refs={sorted({x[0] for x in v})}\n      proofs={sorted({x[1] for x in v if x[1]})} pkgs={sorted({x[2] for x in v if x[2]})}")
