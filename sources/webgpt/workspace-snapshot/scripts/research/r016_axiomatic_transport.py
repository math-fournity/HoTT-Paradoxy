#!/usr/bin/env python3
"""R016 operational calibration: a typed Bool/lambda/opaque-UA fragment.

This is NOT a HoTT kernel or a definitional elaboration of every Book rule.
UA is deliberately represented by an opaque Bool-universe path constant.
The second mode is explicit proof-guided rewriting, NOT judgemental beta-UA,
NOT a cubical implementation, and NOT evidence of general normalization.
Standard library only; importing has no I/O or process/network side effects.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import itertools
import json
from pathlib import Path
from typing import Union


@dataclass(frozen=True)
class BoolType:
    pass


@dataclass(frozen=True)
class BoolUniversePathType:
    """The one selected endpoint pair Bool =_U Bool; no general universes."""
    pass


@dataclass(frozen=True)
class Arrow:
    domain: Type
    codomain: Type


Type = Union[BoolType, BoolUniversePathType, Arrow]
BOOL = BoolType()
BOOL_PATH = BoolUniversePathType()


@dataclass(frozen=True)
class Bit:
    value: int

    def __post_init__(self):
        if type(self.value) is not int or self.value not in (0, 1):
            raise ValueError('A Bit is the integer 0 or 1, not an arbitrary truthy value')


@dataclass(frozen=True)
class Var:
    index: int

    def __post_init__(self):
        if type(self.index) is not int or self.index < 0:
            raise ValueError('A de Bruijn index must be a nonnegative integer')


@dataclass(frozen=True)
class Lam:
    domain: Type
    body: Term


@dataclass(frozen=True)
class App:
    function: Term
    argument: Term


@dataclass(frozen=True)
class If:
    condition: Term
    when_true: Term
    when_false: Term


@dataclass(frozen=True)
class ReflBool:
    pass


@dataclass(frozen=True)
class UaBool:
    """Opaque path for a supplied finite bijection, not all isEquiv syntax."""
    table: tuple[int, int]

    def __post_init__(self):
        if not isinstance(self.table, tuple) or len(self.table) != 2:
            raise ValueError('Expected a two-entry tuple')
        if any(type(x) is not int for x in self.table) or set(self.table) != {0, 1}:
            raise ValueError('UA input must be a bijection of Bool')


@dataclass(frozen=True)
class CoeBool:
    path: Term
    argument: Term


Term = Union[Bit, Var, Lam, App, If, ReflBool, UaBool, CoeBool]


def show_type(t: Type) -> str:
    if t == BOOL:
        return 'Bool'
    if t == BOOL_PATH:
        return 'Bool =_U Bool'
    if isinstance(t, Arrow):
        return f'({show_type(t.domain)} -> {show_type(t.codomain)})'
    raise TypeError('Unsupported type')


def valid_type(t: Type) -> bool:
    return t in (BOOL, BOOL_PATH) or (isinstance(t, Arrow) and valid_type(t.domain) and valid_type(t.codomain))


def type_of(t: Term, context: tuple[Type, ...] = ()) -> Type:
    if not all(valid_type(a) for a in context):
        raise TypeError('Invalid context type')
    if isinstance(t, Bit):
        return BOOL
    if isinstance(t, Var):
        if t.index >= len(context):
            raise TypeError(f'Unbound de Bruijn variable {t.index}')
        return context[t.index]
    if isinstance(t, Lam):
        if not valid_type(t.domain):
            raise TypeError('Invalid lambda domain')
        return Arrow(t.domain, type_of(t.body, (t.domain,) + context))
    if isinstance(t, App):
        ft, at = type_of(t.function, context), type_of(t.argument, context)
        if not isinstance(ft, Arrow) or ft.domain != at:
            raise TypeError('Application type mismatch')
        return ft.codomain
    if isinstance(t, If):
        if type_of(t.condition, context) != BOOL:
            raise TypeError('Boolean eliminator requires Bool')
        a, b = type_of(t.when_true, context), type_of(t.when_false, context)
        if a != b:
            raise TypeError('Conditional branch type mismatch')
        return a
    if isinstance(t, (ReflBool, UaBool)):
        return BOOL_PATH
    if isinstance(t, CoeBool):
        if type_of(t.path, context) != BOOL_PATH or type_of(t.argument, context) != BOOL:
            raise TypeError('Transport endpoint mismatch')
        return BOOL
    raise TypeError(f'Unknown term {type(t).__name__}')


def shift(t: Term, delta: int, cutoff: int = 0) -> Term:
    if isinstance(t, Var):
        if t.index >= cutoff:
            if t.index + delta < 0:
                raise ValueError('Negative shifted variable')
            return Var(t.index + delta)
        return t
    if isinstance(t, Lam):
        return Lam(t.domain, shift(t.body, delta, cutoff + 1))
    if isinstance(t, App):
        return App(shift(t.function, delta, cutoff), shift(t.argument, delta, cutoff))
    if isinstance(t, If):
        return If(shift(t.condition, delta, cutoff), shift(t.when_true, delta, cutoff), shift(t.when_false, delta, cutoff))
    if isinstance(t, CoeBool):
        return CoeBool(shift(t.path, delta, cutoff), shift(t.argument, delta, cutoff))
    if isinstance(t, (Bit, ReflBool, UaBool)):
        return t
    raise TypeError('Unknown term')


def substitute(t: Term, index: int, replacement: Term) -> Term:
    if isinstance(t, Var):
        return replacement if t.index == index else t
    if isinstance(t, Lam):
        return Lam(t.domain, substitute(t.body, index + 1, shift(replacement, 1)))
    if isinstance(t, App):
        return App(substitute(t.function, index, replacement), substitute(t.argument, index, replacement))
    if isinstance(t, If):
        return If(substitute(t.condition, index, replacement), substitute(t.when_true, index, replacement), substitute(t.when_false, index, replacement))
    if isinstance(t, CoeBool):
        return CoeBool(substitute(t.path, index, replacement), substitute(t.argument, index, replacement))
    if isinstance(t, (Bit, ReflBool, UaBool)):
        return t
    raise TypeError('Unknown term')


def beta(body: Term, argument: Term) -> Term:
    return shift(substitute(body, 0, shift(argument, 1)), -1)


def show(t: Term) -> str:
    if isinstance(t, Bit):
        return 'true' if t.value else 'false'
    if isinstance(t, Var):
        return f'#{t.index}'
    if isinstance(t, Lam):
        return f'(lambda:{show_type(t.domain)}. {show(t.body)})'
    if isinstance(t, App):
        return f'({show(t.function)} {show(t.argument)})'
    if isinstance(t, If):
        return f'(if {show(t.condition)} then {show(t.when_true)} else {show(t.when_false)})'
    if isinstance(t, ReflBool):
        return 'refl_Bool'
    if isinstance(t, UaBool):
        return 'ua(identity)' if t.table == (0, 1) else 'ua(not)'
    if isinstance(t, CoeBool):
        return f'coe({show(t.path)}, {show(t.argument)})'
    raise TypeError('Unknown term')


def permutation_term(table: tuple[int, int]) -> Term:
    UaBool(table)  # Validate that the supplied data describe a bijection.
    return Lam(BOOL, If(Var(0), Bit(table[1]), Bit(table[0])))


def step(t: Term, mode: str = 'BASIC') -> tuple[Term, str] | None:
    """Leftmost-outermost strong reduction, or explicitly stronger theorem rewriting."""
    if mode not in ('BASIC', 'PROOF_GUIDED_REWRITE'):
        raise ValueError('Unknown evaluation mode')
    if isinstance(t, App) and isinstance(t.function, Lam):
        return beta(t.function.body, t.argument), 'BETA'
    if isinstance(t, If) and isinstance(t.condition, Bit):
        return (t.when_true if t.condition.value else t.when_false), 'IOTA_BOOL'
    if isinstance(t, CoeBool) and isinstance(t.path, ReflBool):
        return t.argument, 'IOTA_TRANSPORT_REFL'
    if isinstance(t, CoeBool) and isinstance(t.path, UaBool) and mode == 'PROOF_GUIDED_REWRITE':
        return App(permutation_term(t.path.table), t.argument), 'PROPOSITIONAL_UA_BETA_REWRITE_NOT_KERNEL_REDUCTION'
    if isinstance(t, Lam):
        r = step(t.body, mode)
        return (Lam(t.domain, r[0]), 'UNDER_LAMBDA/' + r[1]) if r else None
    if isinstance(t, App):
        r = step(t.function, mode)
        if r:
            return App(r[0], t.argument), 'FUNCTION/' + r[1]
        r = step(t.argument, mode)
        return (App(t.function, r[0]), 'ARGUMENT/' + r[1]) if r else None
    if isinstance(t, If):
        for attr in ('condition', 'when_true', 'when_false'):
            r = step(getattr(t, attr), mode)
            if r:
                args = {k: getattr(t, k) for k in ('condition', 'when_true', 'when_false')}
                args[attr] = r[0]
                return If(**args), attr.upper() + '/' + r[1]
        return None
    if isinstance(t, CoeBool):
        r = step(t.path, mode)
        if r:
            return CoeBool(r[0], t.argument), 'PATH/' + r[1]
        r = step(t.argument, mode)
        return (CoeBool(t.path, r[0]), 'TRANSPORT_ARGUMENT/' + r[1]) if r else None
    if isinstance(t, (Var, Bit, ReflBool, UaBool)):
        return None
    raise TypeError('Unknown term')


def normalize(t: Term, mode: str = 'BASIC', fuel: int = 1000) -> dict:
    if type(fuel) is not int or fuel < 0:
        raise ValueError('fuel must be a nonnegative integer')
    if mode not in ('BASIC', 'PROOF_GUIDED_REWRITE'):
        raise ValueError('Unknown evaluation mode')
    try:
        ty = type_of(t)
    except (TypeError, ValueError) as exc:
        return {'status': 'ILL_TYPED', 'error': str(exc), 'trace': [], 'mode': mode}
    current, trace = t, []
    while True:
        nxt = step(current, mode)
        if nxt is None:
            canonical = (ty == BOOL and isinstance(current, Bit)) or isinstance(current, (Lam, ReflBool, UaBool))
            return {'status': 'VALUE' if canonical else 'NORMAL_NONCANONICAL',
                    'type': show_type(ty), 'initial': show(t), 'normal_form': show(current),
                    'value': current.value if isinstance(current, Bit) else None,
                    'steps': len(trace), 'trace': trace, 'mode': mode,
                    'divergence_proved': False}
        if len(trace) >= fuel:
            return {'status': 'FUEL_EXHAUSTED', 'type': show_type(ty), 'initial': show(t),
                    'current': show(current), 'steps': len(trace), 'trace': trace, 'mode': mode,
                    'divergence_proved': False}
        target, rule = nxt
        if type_of(target) != ty:
            raise AssertionError('Subject reduction failed for this step')
        trace.append({'rule': rule, 'before': show(current), 'after': show(target)})
        current = target


def run_experiments(max_depth: int = 6) -> dict:
    if type(max_depth) is not int or not 0 <= max_depth <= 8:
        raise ValueError('max_depth must be an integer in [0, 8]')
    neg = permutation_term((1, 0))
    blocked = CoeBool(UaBool((1, 0)), Bit(0))
    examples = {
        'direct_not_false': normalize(App(neg, Bit(0))),
        'refl_transport_false': normalize(CoeBool(ReflBool(), Bit(0))),
        'opaque_ua_transport_false': normalize(blocked),
        'opaque_ua_identity_still_not_refl': normalize(CoeBool(UaBool((0, 1)), Bit(0))),
        'dependent_observer_blocked': normalize(If(blocked, Bit(0), Bit(1))),
        'discarded_transport_does_not_block': normalize(App(Lam(BOOL, Bit(0)), blocked)),
        'theorem_rewrite_recovers_true': normalize(blocked, 'PROOF_GUIDED_REWRITE'),
        'insufficient_fuel_is_not_divergence': normalize(App(neg, Bit(0)), fuel=0),
        'illtyped_transport_is_rejected': normalize(CoeBool(Bit(0), Bit(0))),
    }
    assert examples['direct_not_false']['value'] == 1
    assert examples['refl_transport_false']['value'] == 0
    assert examples['opaque_ua_transport_false']['status'] == 'NORMAL_NONCANONICAL'
    assert examples['opaque_ua_transport_false']['steps'] == 0
    assert examples['opaque_ua_identity_still_not_refl']['status'] == 'NORMAL_NONCANONICAL'
    assert examples['dependent_observer_blocked']['status'] == 'NORMAL_NONCANONICAL'
    assert examples['discarded_transport_does_not_block']['value'] == 0
    assert examples['theorem_rewrite_recovers_true']['value'] == 1
    assert examples['insufficient_fuel_is_not_divergence']['divergence_proved'] is False
    assert examples['illtyped_transport_is_rejected']['status'] == 'ILL_TYPED'
    families = []
    for depth in range(max_depth + 1):
        count, blocked_count, canonical_count, rewrites = 0, 0, 0, 0
        for word in itertools.product(((0, 1), (1, 0)), repeat=depth):
            for bit in (0, 1):
                term, expected = Bit(bit), bit
                for table in word:
                    term = CoeBool(UaBool(table), term)
                    expected = table[expected]
                basic = normalize(term)
                proof = normalize(term, 'PROOF_GUIDED_REWRITE', 10000)
                count += 1
                assert basic['status'] == ('VALUE' if depth == 0 else 'NORMAL_NONCANONICAL')
                assert basic['steps'] == 0
                assert proof['status'] == 'VALUE' and proof['value'] == expected
                canonical_count += int(basic['status'] == 'VALUE')
                blocked_count += int(basic['status'] == 'NORMAL_NONCANONICAL')
                rewrites += sum('PROPOSITIONAL_UA_BETA_REWRITE' in x['rule'] for x in proof['trace'])
        families.append({'depth': depth, 'inputs': count, 'basic_values': canonical_count,
                         'basic_noncanonical_normal_forms': blocked_count,
                         'proof_guided_values': count, 'actual_propositional_rewrite_steps': rewrites})
    return {'schema_version': 'hott-r016-operational-fragment/v1',
            'status': 'PASS_DECLARED_FRAGMENT_ONLY', 'max_depth': max_depth,
            'family_inputs': sum(r['inputs'] for r in families),
            'basic_family_values': sum(r['basic_values'] for r in families),
            'basic_family_noncanonical': sum(r['basic_noncanonical_normal_forms'] for r in families),
            'examples': examples, 'finite_families': families,
            'scope': {'language': 'simply typed Bool/arrow fragment plus opaque Bool-universe path and coercion',
                      'ua_argument': 'actual two-element permutation data, not a general isEquiv elaborator',
                      'evaluation': 'leftmost-outermost strong beta/iota under a fixed finite step bound',
                      'proof_guided_mode': 'explicit mathematical theorem rewrite, NOT a new judgemental rule',
                      'full_hott_kernel': False, 'cubical_implementation': False,
                      'general_normalization_proof': False, 'internal_inconsistency_claim': False,
                      'undecidability_or_divergence_claim': False,
                      'external_search': False}}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--max-depth', type=int, default=6)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    if a.out.exists():
        raise SystemExit('Refusing overwrite: ' + str(a.out))
    result = run_experiments(a.max_depth)
    result['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k not in ('examples', 'finite_families')}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
