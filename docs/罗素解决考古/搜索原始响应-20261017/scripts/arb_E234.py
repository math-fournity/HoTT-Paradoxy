import re, pathlib

def norm_ocr(txt):
    txt = re.sub(r'-\n', '-', txt)
    txt = re.sub(r'\n', ' ', txt)
    txt = re.sub(r'\s+', ' ', txt)
    return txt

for page, pat in [
    ("p261", r"Aufgabe mu\S+ in der Weise ge\S+"),
    ("p261", r"eng genug ein\S+"),
    ("p261", r"um alle Wider\S+"),
    ("p262", r"\S+ verschwinden"),
]:
    t = norm_ocr(pathlib.Path(f'zermelo1908-pages/ocr/{page}.txt').read_text(encoding='utf-8', errors='replace'))
    print(f"--- {page} ---")
    for m in re.finditer(pat, t):
        s = max(0, m.start()-70); e = min(len(t), m.end()+70)
        print(f"  …{t[s:e]}…")