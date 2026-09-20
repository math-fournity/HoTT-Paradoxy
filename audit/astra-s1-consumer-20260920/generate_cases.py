#!/usr/bin/env python3
"""Extract the frozen actual S1 consumer chain over the original upstream S1 type."""
from pathlib import Path
import argparse, difflib, hashlib, json

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SOURCE = ROOT / 'audit/astra-remaining-20260920/source-inputs/Cubical/HITs/S1/Base.agda'
DEST = ROOT / 'HoTT/formal/astra-s1-consumer-check'
EXPECTED = 'd239935edc6f9c3da22e82a95c89471681f945f835026efd73688857351cda77'

POSTLUDE = '''
-- The copied consumer uses the actual upstream circle, not a new local HIT.
-- These bridges identify its data with the corresponding upstream functions.
helixAgreement : helix ≡ Upstream.helix
helixAgreement t base = ℤ
helixAgreement t (loop i) = sucPathℤ i

encodeAgreement : (x : S¹) (p : base ≡ x) →
  PathP (λ t → helixAgreement t x) (encode x p) (Upstream.encode x p)
encodeAgreement x p t = subst (helixAgreement t) p (pos zero)

windingAgreement : (p : ΩS¹) → winding p ≡ Upstream.winding p
windingAgreement p = encodeAgreement base p

intLoopAgreement : (n : ℤ) → intLoop n ≡ Upstream.intLoop n
intLoopAgreement (pos zero) = refl
intLoopAgreement (pos (suc n)) = cong (_∙ loop) (intLoopAgreement (pos n))
intLoopAgreement (negsuc zero) = refl
intLoopAgreement (negsuc (suc n)) = cong (_∙ sym loop) (intLoopAgreement (negsuc n))

roundTripLoop : (p : Upstream.ΩS¹) → intLoop (winding p) ≡ p
roundTripLoop = decodeEncode base

roundTripInteger : (n : ℤ) → winding (intLoop n) ≡ n
roundTripInteger = windingℤLoop

composedObservation : (p q : Upstream.ΩS¹) →
  winding (p ∙ q) ≡ winding p + winding q
composedObservation = winding-hom
'''

CHANGES = {
    'SC01': ('helix (loop i) = sucPathℤ i', 'helix (loop i) = ℤ'),
    'SC02': ('; (j = i1) → loop k } )', '; (j = i1) → base } )'),
    'SC03': ('(i = i0) → intLoop (predSuc y k) j', '(i = i0) → intLoop y j'),
    'SC04': ('decodeEncode x p = J (λ y q → decode y (encode y q) ≡ q) (λ _ → refl) p',
             'decodeEncode x p = refl'),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--case', choices=['SC00', 'SC01', 'SC02', 'SC03', 'SC04', 'SC05'], required=True)
    args = ap.parse_args()
    raw = SOURCE.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED
    original = raw.decode()
    imports = original[original.index('open import Cubical.Foundations.Prelude'):original.index('\ndata S¹')]
    core = original[original.index('-- ΩS¹ ≡ ℤ'):original.index('-- Commutativity')]
    original_core = core
    if args.case in CHANGES:
        before, after = CHANGES[args.case]
        assert core.count(before) == 1
        core = core.replace(before, after)
    wrapper = imports + '\nimport Cubical.HITs.S1.Base as Upstream\nopen Upstream using (S¹; base; loop)\n\n'
    text = '{-# OPTIONS --safe --cubical --guardedness #-}\nmodule ' + args.case + ' where\n\n' + wrapper + core + POSTLUDE
    DEST.mkdir(exist_ok=True)
    source = DEST / (args.case + '.agda')
    assert not source.exists(), 'Do not overwrite a preserved case.'
    source.write_text(text)
    row = {'case': args.case, 'source': source.relative_to(ROOT).as_posix(),
           'sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'upstream_sha256': EXPECTED,
           'upstream_core_exact_before_mutation': True,
           'shared_packaging': 'Reuse original imports and original S1/base/loop; extract exact helix through winding-hom; add bridges and actual consumers.',
           'mutation': CHANGES.get(args.case), 'state': 'GENERATED_NOT_RUN'}
    (OUT / (args.case + '.json')).write_text(json.dumps(row, ensure_ascii=False, indent=2) + '\n')
    diff = ''.join(difflib.unified_diff(original_core.splitlines(True), core.splitlines(True),
                                      fromfile='upstream-fixed-core', tofile=args.case))
    (OUT / (args.case + '.diff')).write_text(diff)
    print(json.dumps(row, ensure_ascii=False))


if __name__ == '__main__':
    main()
