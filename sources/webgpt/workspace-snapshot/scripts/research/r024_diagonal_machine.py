"""A concrete, deterministic natural-register machine and a literal diagonal compiler.

This is executable semantics testing, NOT a HoTT kernel and NOT a proof by finite
search of undecidability. No HALTS/ORACLE/CALL primitive is available. A candidate
program is copied into the output with register and jump relocation.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

SET, COPY, ADD, MUL, INC, DECJZ, JUMP, HALT = range(8)
Instr = tuple[int, int, int, int]
Program = tuple[Instr, ...]
LOOP: Program = ((JUMP, 0, 0, 0),)


def nat(n: int) -> int:
    if type(n) is not int or n < 0:
        raise ValueError('Expected a natural number, excluding bool')
    return n


def program(items: Iterable[Instr]) -> Program:
    out = tuple(tuple(i) for i in items)
    for i in out:
        if len(i) != 4 or any(type(x) is not int or x < 0 for x in i) or i[0] > HALT:
            raise ValueError(f'Malformed instruction: {i!r}')
        op, a, b, c = i
        if op in (INC, JUMP, HALT) and (b or c):
            raise ValueError('Noncanonical unused operands')
        if op in (SET, COPY) and c:
            raise ValueError('Noncanonical unused operand')
    return out


def gamma(n: int) -> str:
    b = bin(nat(n) + 1)[2:]
    return '0' * (len(b) - 1) + b


def encode(p: Program) -> int:
    p = program(p)
    bits = '1' + gamma(len(p)) + ''.join(gamma(x) for i in p for x in i)
    return int(bits, 2)


def decode(code: int) -> Program:
    """Total decoding: noncanonical/invalid numeral denotes an explicit self-loop.

    Each scan is bounded by the input bit length. This is not an evaluation of
    the encoded program. No source program can run during parsing.
    """
    nat(code)
    bits = bin(code)[3:]  # strip 0b and the leading framing bit
    pos = 0

    def read() -> int:
        nonlocal pos
        start = pos
        while pos < len(bits) and bits[pos] == '0':
            pos += 1
        width = pos - start + 1
        if pos + width > len(bits):
            raise ValueError('Incomplete gamma code')
        value = int(bits[pos:pos + width], 2) - 1
        pos += width
        return value

    try:
        count = read()
        if count > (len(bits) - pos) // 4:
            return LOOP
        p = program(tuple(tuple(read() for _ in range(4)) for _ in range(count)))
        if pos != len(bits) or encode(p) != code:
            return LOOP
        return p
    except ValueError:
        return LOOP


def pair(a: int, b: int) -> int:
    a, b = nat(a), nat(b)
    return (a + b) * (a + b + 1) // 2 + b


@dataclass(frozen=True)
class State:
    pc: int
    registers: tuple[tuple[int, int], ...]

    @staticmethod
    def initial(x: int) -> 'State':
        return State(0, ((0, nat(x)),) if x else ())


@dataclass(frozen=True)
class Returned:
    value: int


Config = State | Returned


def step(p: Program, s: Config) -> Config:
    """One total, deterministic transition; completed outputs are absorbing."""
    if isinstance(s, Returned):
        return s
    if not 0 <= s.pc < len(p):
        return s  # invalid counter is a nonterminal fixed configuration
    regs = dict(s.registers)
    op, a, b, c = p[s.pc]
    val = lambda k: regs.get(k, 0)
    pc = s.pc + 1
    if op == SET:
        regs[a] = b
    elif op == COPY:
        regs[a] = val(b)
    elif op == ADD:
        regs[a] = val(b) + val(c)
    elif op == MUL:
        regs[a] = val(b) * val(c)
    elif op == INC:
        regs[a] = val(a) + 1
    elif op == DECJZ:
        if val(a) == 0:
            pc = b
        else:
            regs[a] = val(a) - 1
            pc = c
    elif op == JUMP:
        pc = a
    elif op == HALT:
        return Returned(val(a))
    else:
        raise ValueError('Call program() to validate the syntax before step()')
    return State(pc, tuple(sorted((k, v) for k, v in regs.items() if v)))


def run(p: Program, x: int, fuel: int) -> dict:
    p = program(p)
    s: Config = State.initial(x)
    seen: dict[State, int] = {}
    for n in range(nat(fuel) + 1):
        if isinstance(s, Returned):
            return {'status': 'HALTED', 'steps': n, 'value': s.value}
        if s in seen:
            return {'status': 'REPEATED_NONTERMINAL', 'steps': n,
                    'cycle_start': seen[s], 'cycle_length': n - seen[s]}
        seen[s] = n
        if n == fuel:
            return {'status': 'FUEL_EXHAUSTED_UNKNOWN', 'steps': n}
        s = step(p, s)
    raise AssertionError('unreachable')


def T(code: int, x: int, n: int, v: int) -> bool:
    """Bounded certificate predicate: returned v at OR BEFORE step n.

    Absorption intentionally makes this monotone in n; it is NOT 'first halt at
    exactly n'. The unbounded halting proposition existentially quantifies n,v.
    """
    p = decode(code)
    s: Config = State.initial(x)
    for _ in range(nat(n)):
        s = step(p, s)
    return s == Returned(nat(v))


def compile_diagonal(h: Program) -> Program:
    """D_h(y): run h(pair(y,y)); 1 => loop; 0 => return 0; other => return 2.

    Divergence of h is preserved by literal inlining. The compiler inspects
    only the finite syntax, never h's behavior. All h registers move by +3.
    Each old instruction occupies two slots, making relocation explicit.
    """
    h = program(h)
    base = 4
    trap = base + 2 * len(h)
    post = trap + 1
    address = lambda k: base + 2 * k if 0 <= k < len(h) else trap
    out: list[Instr] = [
        (SET, 1, 1, 0),
        (ADD, 2, 0, 1),
        (MUL, 2, 0, 2),
        (ADD, 3, 2, 2),  # R3 = 2*y*(y+1) = pair(y,y); other R>=3 zero
    ]
    for i, (op, a, b, c) in enumerate(h):
        follow: Instr = (JUMP, address(i + 1), 0, 0)
        if op == HALT:
            inst = (COPY, 0, a + 3, 0)
            follow = (JUMP, post, 0, 0)
        elif op == SET:
            inst = (SET, a + 3, b, 0)
        elif op == COPY:
            inst = (COPY, a + 3, b + 3, 0)
        elif op in (ADD, MUL):
            inst = (op, a + 3, b + 3, c + 3)
        elif op == INC:
            inst = (INC, a + 3, 0, 0)
        elif op == DECJZ:
            inst = (DECJZ, a + 3, address(b), address(c))
        elif op == JUMP:
            inst = (JUMP, address(a), 0, 0)
        else:
            raise ValueError(op)
        out.extend((inst, follow))
    out.extend([
        (JUMP, trap, 0, 0),
        (DECJZ, 0, post + 3, post + 1),
        (DECJZ, 0, trap, post + 2),
        (SET, 0, 2, 0),
        (HALT, 0, 0, 0),
    ])
    return program(out)


def diag(code: int) -> int:
    return encode(compile_diagonal(decode(code)))


def parity_word(word: tuple) -> int:
    """Compiles a separate finite path-word syntax. NOT native HoTT reduction."""
    match word:
        case ('unit',): return 0
        case ('loop',): return 1
        case ('inverse', w): return parity_word(w)
        case ('concat', a, b): return parity_word(a) ^ parity_word(b)
        case _: raise ValueError('Not an explicit finite path word')


def winding_word(word: tuple) -> int:
    match word:
        case ('unit',): return 0
        case ('loop',): return 1
        case ('inverse', w): return -winding_word(w)
        case ('concat', a, b): return winding_word(a) + winding_word(b)
        case _: raise ValueError('Not an explicit finite path word')
