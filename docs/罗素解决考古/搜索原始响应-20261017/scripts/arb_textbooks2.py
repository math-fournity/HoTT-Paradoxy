import re, pathlib, subprocess

md_dir = pathlib.Path('mineru_md')

def norm(t):
    return re.sub(r'\s+', ' ', t)

_cache = {}
def pdf_text(pdf):
    if pdf not in _cache:
        _cache[pdf] = norm(subprocess.run(['pdftotext', '-layout', pdf, '-'],
                       capture_output=True, text=True).stdout)
    return _cache[pdf]

def md_text(*names):
    key = tuple(names)
    if key not in _cache:
        _cache[key] = norm("\n".join((md_dir / n).read_text(encoding='utf-8', errors='replace') for n in names))
    return _cache[key]

claims = [
    ("T4-Enderton-Th2A", "enderton1977.pdf", ("enderton1977_part01_p001-150.md", "enderton1977_part02_p151-289.md"),
     "We can now use the argument of Russell's paradox to show that the class V of all sets is not itself a set"),
    ("T4b-Enderton-Th2A-stmt", "enderton1977.pdf", ("enderton1977_part01_p001-150.md", "enderton1977_part02_p151-289.md"),
     "There is no set to which every set belongs"),
    ("T5-Enderton-Mirimanoff", "enderton1977.pdf", ("enderton1977_part01_p001-150.md", "enderton1977_part02_p151-289.md"),
     "The idea first appeared in a 1917 paper by Mirimanoff"),
    ("T5b-Enderton-vN1925", "enderton1977.pdf", ("enderton1977_part01_p001-150.md", "enderton1977_part02_p151-289.md"),
     "the axiom was listed explicitly in von Neumann"),
    ("T6-Enderton-vH", "enderton1977.pdf", ("enderton1977_part01_p001-150.md", "enderton1977_part02_p151-289.md"),
     "Zermelo's 1908 paper giving the first axiomatization of set theory is included"),
    ("T7-Rieger-diagonal", "rieger-foundation.pdf", ("rieger-foundation.md",),
     "diagonalizes out"),
    ("T8-Rieger-restricts", "rieger-foundation.pdf", ("rieger-foundation.md",),
     "ZF restricts the notion of set more than is necessary to avoid the paradoxes"),
    ("T8b-Rieger-summary", "rieger-foundation.pdf", ("rieger-foundation.md",),
     "it can be rigorously proved that ZF restricts the notion of set more than the paradoxes demand"),
    ("T9-Kanamori-mainpurpose", "kanamori.pdf", ("kanamori.md",),
     "The main purpose of Zermelo's [1908a] axiomatization of set theory"),
    ("T10-Kanamori-Husserl", "kanamori.pdf", ("kanamori.md",),
     "Zermelo's independent discovery of the argument for Russell's Paradox is substantiated in a note dated 16 April 1902"),
    ("T11-Kanamori-firstresult", "kanamori.pdf", ("kanamori.md",),
     "the first result of his axiomatic theory was just the result in the Husserl note"),
]

print(f"{'ID':30} {'pdftotext':10} {'MinerU':8} 判定")
print("-" * 66)
for cid, pdf, mds, sent in claims:
    s = norm(sent)
    in_pdf = s in pdf_text(pdf)
    in_md = s in md_text(*mds)
    v = "OK 双管线一致" if in_pdf and in_md else "!! 需仲裁"
    print(f"{cid:30} {'Y' if in_pdf else 'N':10} {'Y' if in_md else 'N':8} {v}")
    if not (in_pdf and in_md):
        for label, src in [("PDF", pdf_text(pdf)), ("MD", md_text(*mds))]:
            key = sent.split()[0].strip("'\"")
            i = src.find(key)
            if i >= 0:
                print(f"   [{label}] …{src[max(0,i-50):i+200]}…")
            else:
                print(f"   [{label}] 首词未命中")