#!/usr/bin/env python3
"""Finite implementation checks, not formal proofs of noncomputability."""
from __future__ import annotations
from dataclasses import replace
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
from scripts.research.r017_local_execution import (
    Instruction,Machine,Config,Wrapper,WrapperState,natural,initial,step,run_base,
    check_certificate,output_from_certificate,wrapper_initial,wrapper_step,
    run_wrapper,check_wrapper_certificate,check_wrapper_prefix,spin_certificate,
    local_zero_certificate,delayed_halt,two_instruction_machines,
)

class MachineTests(unittest.TestCase):
    def setUp(self):
        self.halt=Machine(1,(Instruction('HALT'),))
        self.spin=Machine(1,(Instruction('JUMP',target=0),))

    def test_natural_rejects_bool(self):
        with self.assertRaises(ValueError):natural(True,'n')
    def test_negative_input(self):
        with self.assertRaises(ValueError):initial(self.halt,-1)
    def test_empty_machine_rejected(self):
        with self.assertRaises(ValueError):Machine(1,())
    def test_out_of_bounds_register(self):
        with self.assertRaises(ValueError):Machine(1,(Instruction('HALT',reg=1),))
    def test_bad_jump(self):
        with self.assertRaises(ValueError):Machine(1,(Instruction('JUMP',target=1),))
    def test_bad_zero_target(self):
        with self.assertRaises(ValueError):Machine(1,(Instruction('DECJZ',zero=1),))
    def test_unknown_opcode(self):
        with self.assertRaises(ValueError):Machine(1,(Instruction('BOGUS'),))
    def test_zero_fuel_is_not_nontermination(self):
        r=run_base(self.halt,2,0)
        self.assertEqual(r.status,'FUEL_EXHAUSTED');self.assertEqual(r.transitions,0)
        self.assertEqual(run_base(self.halt,2,1).output,2)
    def test_halt_is_one_transition(self):
        r=run_base(self.halt,7,1)
        self.assertEqual((r.status,r.transitions,r.output),('HALTED',1,7))
    def test_increment(self):
        p=Machine(1,(Instruction('INC',target=1),Instruction('HALT')))
        self.assertEqual(run_base(p,5,2).output,6)
    def test_decrement_zero_branch(self):
        p=Machine(1,(Instruction('DECJZ',target=0,zero=1),Instruction('HALT')))
        self.assertEqual(run_base(p,0,2).output,0)
        self.assertEqual(run_base(p,4,6).output,0)
    def test_unbounded_increment_does_not_fake_cycle(self):
        p=Machine(1,(Instruction('INC',target=0),))
        r=run_base(p,0,6)
        self.assertEqual(r.status,'FUEL_EXHAUSTED')
        self.assertEqual(len(set(r.trace)),7)
    def test_terminal_is_absorbing(self):
        c=step(self.halt,initial(self.halt,3))
        self.assertEqual(step(self.halt,c),c)
    def test_invalid_config(self):
        with self.assertRaises(ValueError):step(self.halt,Config(2,(0,)))
    def test_valid_certificate(self):
        r=run_base(self.halt,4,1)
        self.assertTrue(check_certificate(self.halt,4,r.trace))
        self.assertEqual(output_from_certificate(self.halt,4,r.trace),4)
    def test_empty_certificate(self):
        self.assertFalse(check_certificate(self.halt,0,()))
    def test_wrong_input_certificate(self):
        r=run_base(self.halt,4,1)
        self.assertFalse(check_certificate(self.halt,5,r.trace))
    def test_wrong_program_certificate(self):
        r=run_base(self.halt,4,1)
        self.assertFalse(check_certificate(self.spin,4,r.trace))
    def test_forged_output_certificate(self):
        r=run_base(self.halt,4,1)
        bad=r.trace[:-1]+(replace(r.trace[-1],output=9),)
        self.assertFalse(check_certificate(self.halt,4,bad))
    def test_nonterminal_is_not_certificate(self):
        r=run_base(self.spin,0,5)
        self.assertFalse(check_certificate(self.spin,0,r.trace))
        with self.assertRaises(ValueError):output_from_certificate(self.spin,0,r.trace)
    def test_padding_can_make_two_certificates_same_value(self):
        r=run_base(self.halt,4,1)
        padded=r.trace+(r.trace[-1],)*3
        self.assertTrue(check_certificate(self.halt,4,padded))
        self.assertEqual(output_from_certificate(self.halt,4,padded),4)
        self.assertNotEqual(r.trace,padded)
    def test_fuel_bound_enforced(self):
        with self.assertRaises(ValueError):run_base(self.spin,0,100001)
    def test_delayed_halt_exact_time(self):
        for h in range(1,10):
            with self.subTest(h=h):
                p=delayed_halt(h)
                self.assertEqual(run_base(p,0,h-1).status,'FUEL_EXHAUSTED')
                self.assertEqual(run_base(p,0,h).transitions,h)
    def test_finite_program_enumeration_distinct(self):
        ps=two_instruction_machines()
        self.assertEqual(len(ps),256);self.assertEqual(len(set(ps)),256)

class WrapperTests(unittest.TestCase):
    def setUp(self):
        self.halt=Wrapper(Machine(1,(Instruction('HALT'),)),0)
        self.spin=Wrapper(Machine(1,(Instruction('JUMP',target=0),)),0)
    def test_local_zero_even_when_base_halts(self):
        r=run_wrapper(self.halt,0,1)
        self.assertTrue(check_wrapper_certificate(self.halt,0,r.trace))
        self.assertEqual((r.transitions,r.machine_steps,r.output),(1,0,0))
    def test_local_zero_even_when_base_spins(self):
        r=run_wrapper(self.spin,0,1)
        self.assertTrue(check_wrapper_certificate(self.spin,0,r.trace))
        self.assertEqual(r.machine_steps,0)
    def test_local_zero_uniform_certificate(self):
        for machine in two_instruction_machines():
            p=Wrapper(machine,3)
            c=local_zero_certificate(p)
            self.assertEqual(len(c),2)
            self.assertTrue(check_wrapper_certificate(p,0,c))
    def test_halt_base_positive_wrapper_spins(self):
        r=run_wrapper(self.halt,3,8)
        self.assertEqual(r.status,'FUEL_EXHAUSTED')
        self.assertTrue(spin_certificate(self.halt,3,r.trace))
    def test_spin_base_positive_wrapper_finishes(self):
        for n in range(1,10):
            r=run_wrapper(self.spin,n,n+2)
            self.assertEqual((r.status,r.transitions,r.machine_steps,r.output),('HALTED',n+2,n,0))
    def test_timeout_not_a_spin_certificate(self):
        r=run_wrapper(self.spin,5,2)
        self.assertEqual(r.status,'FUEL_EXHAUSTED')
        self.assertFalse(spin_certificate(self.spin,5,r.trace))
    def test_halt_at_probe_bound_is_detected(self):
        p=Wrapper(delayed_halt(4),0)
        self.assertTrue(spin_certificate(p,4,run_wrapper(p,4,6).trace))
        self.assertTrue(check_wrapper_certificate(p,3,run_wrapper(p,3,5).trace))
    def test_pending_final_probe_is_not_returned_value(self):
        r=run_wrapper(self.spin,3,4)
        self.assertEqual(r.status,'FUEL_EXHAUSTED')
        self.assertFalse(check_wrapper_certificate(self.spin,3,r.trace))
    def test_spurious_done_trace_rejected(self):
        forged=(wrapper_initial(1),WrapperState('done',0,None,0))
        self.assertFalse(check_wrapper_certificate(self.halt,1,forged))
    def test_wrong_input_wrapper_trace(self):
        c=local_zero_certificate(self.halt)
        self.assertFalse(check_wrapper_prefix(self.halt,1,c))
    def test_positive_result_certificate(self):
        r=run_wrapper(self.spin,2,4)
        self.assertTrue(check_wrapper_certificate(self.spin,2,r.trace))
    def test_spin_certificate_is_reachable_not_arbitrary_state(self):
        arbitrary=(WrapperState('spin',0,Config(0,(0,),True,0)),)
        self.assertFalse(spin_certificate(self.halt,1,arbitrary))
    def test_prefix_tests_never_prove_totality(self):
        for k in range(9):
            p=Wrapper(delayed_halt(k+1),0)
            for n in range(k+1):self.assertTrue(check_wrapper_certificate(p,n,run_wrapper(p,n,n+2).trace))
            self.assertTrue(spin_certificate(p,k+1,run_wrapper(p,k+1,k+3).trace))
    def test_all_source_data_explicit(self):
        p=Wrapper(delayed_halt(3),17)
        self.assertEqual(p.fixed_input,17)
        self.assertEqual(len(p.base.code),3)
    def test_invalid_wrapper_input(self):
        with self.assertRaises(ValueError):run_wrapper(self.spin,True,4)
    def test_invalid_probe_fails(self):
        with self.assertRaises(ValueError):wrapper_step(self.spin,2,WrapperState('probe',1,None))

class PolicyTests(unittest.TestCase):
    def test_saved_source_before_invocation(self):
        self.assertTrue((ROOT/'scripts/research/r017_local_execution.py').is_file())
        self.assertTrue(Path(__file__).is_file())
    def test_agents_no_temporary_exception(self):
        text=(ROOT/'AGENTS.md').read_text()
        self.assertIn('禁止 inline 代码',text)
        self.assertIn('不再允许“临时先执行、之后再补存”的例外',text)
        self.assertNotIn('临时探索随后实际采用时也应落为可复用脚本',text)

if __name__=='__main__':unittest.main(verbosity=2)
