#!/usr/bin/env python3
"""Keep the initial successful prototype, then add explicit type-grammar checks."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'scripts/research/r026_early_ideas_checks.py'
old=p.read_text()
backup=ROOT/'scripts/history/r026_early_ideas_checks_v0.py'
if backup.exists():raise FileExistsError(backup)
backup.parent.mkdir(parents=True,exist_ok=True);backup.write_text(old)
needle='def merge(left: Counter, right: Counter, linear: bool) -> Counter:'
replacement='''def validate_type(ty):
    if isinstance(ty, Atom) and isinstance(ty.name, str) and ty.name:
        return
    if isinstance(ty, Arrow):
        validate_type(ty.domain); validate_type(ty.codomain); return
    if isinstance(ty, Tensor):
        validate_type(ty.left); validate_type(ty.right); return
    raise Rejected('Malformed type outside the declared grammar')

'''+needle
assert old.count(needle)==1
new=old.replace(needle,replacement)
new=new.replace("    if isinstance(term, Var):\n", "    for ty in env.values():validate_type(ty)\n    if isinstance(term, Var):\n",1)
new=new.replace("    if isinstance(term, Lam):\n", "    if isinstance(term, Lam):\n        validate_type(term.domain)\n",1)
new=new.replace('    inferred, used = infer(term, env, linear)','    validate_type(target)\n    inferred, used = infer(term, env, linear)',1)
new=new.replace("      'untyped_payload':expect_rejected(lambda:infer(None,{}))}","      'untyped_payload':expect_rejected(lambda:infer(None,{})),\n      'fake_type':expect_rejected(lambda:infer(Lam('x', None, Var('x')),{})),\n      'fake_environment':expect_rejected(lambda:infer(Var('x'),{'x':None}))}")
p.write_text(new)
print('Saved v0; final checker now validates all declared types. First execution record remains unchanged.')
