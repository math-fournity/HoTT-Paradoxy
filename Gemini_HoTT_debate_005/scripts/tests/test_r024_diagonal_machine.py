from __future__ import annotations
import random, sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.research.r024_diagonal_machine import (
    SET, COPY, ADD, MUL, INC, DECJZ, JUMP, HALT, LOOP, State, Returned,
    program, encode, decode, diag, compile_diagonal, pair, T, step, run,
    parity_word, winding_word,
)


def const(n):
    return program(((SET, 0, n, 0), (HALT, 0, 0, 0)))


class RegisterMachineTests(unittest.TestCase):
    def test_initial_zero_omission(self):
        self.assertEqual(State.initial(0).registers, ())
        self.assertEqual(State.initial(9).registers, ((0, 9),))

    def test_invalid_python_values_rejected(self):
        for x in (-1, True, 1.2, '2'):
            with self.assertRaises(ValueError): decode(x)

    def test_invalid_instructions_rejected(self):
        for p in [((8,0,0,0),), ((HALT,0,1,0),), ((SET,0,-1,0),), ((SET,0,0),)]:
            with self.assertRaises(ValueError): program(p)

    def test_primitive_instructions(self):
        p=program(((SET,1,3,0),(COPY,2,1,0),(ADD,2,2,1),(MUL,2,2,1),(INC,2,0,0),(HALT,2,0,0)))
        self.assertEqual(run(p,0,20)['value'],19)

    def test_countdown_terminates(self):
        p=program(((DECJZ,0,2,1),(JUMP,0,0,0),(HALT,0,0,0)))
        self.assertEqual(run(p,12,40)['value'],0)
        self.assertEqual(run(p,12,3)['status'],'FUEL_EXHAUSTED_UNKNOWN')

    def test_halting_is_absorbing(self):
        self.assertEqual(step(const(0),Returned(5)),Returned(5))

    def test_invalid_counter_nonterminal(self):
        s=State(50,())
        self.assertEqual(step(const(1),s),s)
        self.assertNotIsInstance(s,Returned)

    def test_unknown_is_not_divergence(self):
        self.assertEqual(run(program(((INC,0,0,0),(JUMP,0,0,0))),0,31)['status'],'FUEL_EXHAUSTED_UNKNOWN')

    def test_selfloop_witness(self):
        r=run(LOOP,0,20)
        self.assertEqual((r['status'],r['cycle_length']),('REPEATED_NONTERMINAL',1))

    def test_code_roundtrip(self):
        for p in [(),LOOP,const(0),const(1),const(2),((HALT,0,0,0),),compile_diagonal(const(1))]:
            self.assertEqual(decode(encode(p)),program(p))

    def test_total_parser_for_small_numerals(self):
        for n in range(4096):
            p=decode(n)
            self.assertEqual(program(p),p)

    def test_certificate_convention(self):
        c=encode(const(7))
        self.assertFalse(T(c,0,0,7)); self.assertFalse(T(c,0,1,7))
        self.assertTrue(T(c,0,2,7)); self.assertTrue(T(c,0,7,7))
        self.assertFalse(T(c,0,7,6))

    def test_diagonal_pair(self):
        for y in range(100): self.assertEqual(pair(y,y),2*y*(y+1))

    def test_diag_literal_copy_and_size(self):
        for h in [(),LOOP,const(0),const(1)]:
            d=compile_diagonal(h)
            self.assertEqual(len(d),2*len(h)+9)
            self.assertEqual(decode(diag(encode(h))),d)

    def test_h0_branch(self):
        for y in range(20): self.assertEqual(run(compile_diagonal(const(0)),y,100)['value'],0)

    def test_h1_branch(self):
        for y in range(20): self.assertEqual(run(compile_diagonal(const(1)),y,100)['status'],'REPEATED_NONTERMINAL')

    def test_nonbinary_result_explicit(self):
        for n in (2,3,9): self.assertEqual(run(compile_diagonal(const(n)),4,100)['value'],2)

    def test_input_relocation(self):
        h=program(((HALT,0,0,0),))
        for y in range(6):
            expected=pair(y,y)
            self.assertEqual(run(compile_diagonal(h),y,100)['value'],0 if expected==0 else 2)

    def test_other_registers_start_zero(self):
        h=program(((HALT,1,0,0),))
        self.assertEqual(run(compile_diagonal(h),9,100)['value'],0)

    def test_fallthrough_preserved(self):
        h=program(((SET,0,0,0),))
        self.assertEqual(run(compile_diagonal(h),2,100)['status'],'REPEATED_NONTERMINAL')

    def test_bad_jump_not_into_postlude(self):
        for target in (1,2,100):
            h=program(((JUMP,target,0,0),))
            self.assertEqual(run(compile_diagonal(h),2,100)['status'],'REPEATED_NONTERMINAL')

    def test_h_divergence_preserved(self):
        self.assertEqual(run(compile_diagonal(LOOP),5,80)['status'],'REPEATED_NONTERMINAL')

    def test_conditional_zero_branch(self):
        h=program(((DECJZ,0,1,3),(SET,0,0,0),(HALT,0,0,0),(SET,0,1,0),(HALT,0,0,0)))
        self.assertEqual(run(compile_diagonal(h),0,80)['value'],0)
        self.assertEqual(run(compile_diagonal(h),1,80)['status'],'REPEATED_NONTERMINAL')

    def test_diagonal_actual_code_input(self):
        for v in (0,1):
            c=diag(encode(const(v)))
            r=run(decode(c),c,100)
            self.assertEqual(r['status'],'HALTED' if v==0 else 'REPEATED_NONTERMINAL')

    def test_decidable_T_alone_insufficient(self):
        # Countermodel to a *weaker* hypothesis: every numeral denotes const0.
        trivial_T=lambda c,x,n,v: n>=1 and v==0
        chi=lambda c,x: 1
        self.assertTrue(all(trivial_T(c,x,1,0) and chi(c,x)==1 for c in range(5) for x in range(5)))
        # const1 realizes chi under this trivial numbering only if number1 means
        # const1, which it does not. Instead let code0=>const0, all others const1:
        relation=lambda c,x,n,v: n>=1 and v==(0 if c==0 else 1)
        self.assertTrue(all(relation(1,pair(c,x),1,chi(c,x)) for c in range(5) for x in range(5)))
        # All programs halt: no diagonal code can have the required 1=>diverge law.
        self.assertTrue(all(relation(d,d,1,0 if d==0 else 1) for d in range(5)))


class PathWordTests(unittest.TestCase):
    def test_unit_and_loop(self):
        self.assertEqual(parity_word(('unit',)),0)
        self.assertEqual(parity_word(('loop',)),1)

    def test_inverse(self):
        w=('inverse',('loop',))
        self.assertEqual(winding_word(w),-1); self.assertEqual(parity_word(w),1)

    def test_concat_inverse(self):
        w=('concat',('loop',),('inverse',('loop',)))
        self.assertEqual(winding_word(w),0); self.assertEqual(parity_word(w),0)

    def test_square(self):
        w=('concat',('loop',),('concat',('loop',),('loop',)))
        self.assertEqual(parity_word(('concat',w,w)),0)

    def test_arbitrary_hott_term_not_in_word_syntax(self):
        with self.assertRaises(ValueError): parity_word(('transport',('ua','not'),True))

    def test_words_not_native_transport(self):
        words=[('unit',),('loop',)]
        rng=random.Random(2401)
        for _ in range(400):
            a=rng.choice(words)
            w=('inverse',a) if rng.randrange(2) else ('concat',a,rng.choice(words))
            self.assertEqual(parity_word(w),winding_word(w)%2)
            words.append(w)


if __name__=='__main__': unittest.main(verbosity=2)
