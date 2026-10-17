import re, pathlib, subprocess

root = pathlib.Path('.')
md_dir = root / 'mineru_md'

def norm(t):
    t = re.sub(r'\s+', ' ', t)
    return t

# pdftotext 全文（-layout 保结构）
def pdf_text(pdf):
    return norm(subprocess.run(['pdftotext', '-layout', str(pdf), '-'],
                capture_output=True, text=True).stdout)

claims = [
    ("T1-Enderton-blocked", "enderton1977.pdf", "enderton1977_part01_p001-150.md",
     "These two sorts of disaster will be blocked in precise ways in our axiomatic treatment"),
    ("T1b-Enderton-avoided", "enderton1977.pdf", "enderton1977_part01_p001-150.md",
     "will be avoided by adherence to entrance requirements"),
    ("T1c-Enderton-communicated", "enderton1977.pdf", "enderton1977_part01_p001-150.md",
     "It was communicated by Bertrand Russell in 1902 to Gottlob Frege"),
    ("T2-Kunen-unfortunately", "kunen1980.pdf", "kunen1980_part01_p001-163.md",
     "Unfortunately, such a scheme is inconsistent by the famous Russell paradox"),
    ("T2b-Kunen-fortunately", "kunen1980.pdf", "kunen1980_part01_p001-163.md",
     "Fortunately in mathematical applications it is sufficient"),
    ("T3-Kunen-theorem52", "kunen1980.pdf", "kunen1980_part01_p001-163.md",
     "such a y such that"),
]

cache = {}
for cid, pdf, md, sent in claims:
    if pdf not in cache:
        cache[pdf] = pdf_text(pdf)
    pt = cache[pdf]
    mdt = norm((md_dir / md).read_text(encoding='utf-8', errors='replace'))
    in_pdf = norm(sent) in pt
    in_md = norm(sent) in mdt
    v = "OK 双管线一致" if in_pdf and in_md else "!! 需仲裁"
    print(f"{cid:28} pdftotext={'Y' if in_pdf else 'N'} MinerU={'Y' if in_md else 'N'}  {v}")
    if not (in_pdf and in_md):
        # 打印近似上下文帮助仲裁
        for label, src in [("PDF", pt), ("MD", mdt)]:
            key = sent.split()[0]
            i = src.find(key)
            if i >= 0:
                print(f"   [{label}] …{src[max(0,i-40):i+180]}…")
            else:
                print(f"   [{label}] 首词未命中")