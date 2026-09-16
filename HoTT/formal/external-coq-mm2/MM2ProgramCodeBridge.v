From Coq Require Import List Arith Lia.
From Coq Require Import Relations.Relation_Operators Operators_Properties.
Import ListNotations.

Require Import Undecidability.Synthetic.Undecidability.
Require Import Undecidability.MinskyMachines.MM2.
Require Import Undecidability.MinskyMachines.MM2_undec.

Set Implicit Arguments.

(* A Coq presentation of the project's finite ProgramCode TaskSpec. *)

Inductive pc_instr : Type :=
  | pc_inc_a : nat -> pc_instr
  | pc_inc_b : nat -> pc_instr
  | pc_dec_a : nat -> nat -> pc_instr
  | pc_dec_b : nat -> nat -> pc_instr
  | pc_halt : pc_instr.

Definition pc_program := list pc_instr.
Definition pc_state := (nat * (nat * nat))%type.

Definition pc_lookup (program : pc_program) (label : nat) : pc_instr :=
  nth label program pc_halt.

Definition pc_final_instr (instruction : pc_instr) : bool :=
  match instruction with
  | pc_halt => true
  | _ => false
  end.

Definition pc_is_final (program : pc_program) (state : pc_state) : bool :=
  pc_final_instr (pc_lookup program (fst state)).

Definition pc_step_instr (instruction : pc_instr) (state : pc_state) : pc_state :=
  match instruction, state with
  | pc_inc_a next, (_, (a, b)) => (next, (S a, b))
  | pc_inc_b next, (_, (a, b)) => (next, (a, S b))
  | pc_dec_a on_zero on_suc, (_, (0, b)) => (on_zero, (0, b))
  | pc_dec_a on_zero on_suc, (_, (S a, b)) => (on_suc, (a, b))
  | pc_dec_b on_zero on_suc, (_, (a, 0)) => (on_zero, (a, 0))
  | pc_dec_b on_zero on_suc, (_, (a, S b)) => (on_suc, (a, b))
  | pc_halt, state => state
  end.

Definition pc_step (program : pc_program) (state : pc_state) : pc_state :=
  pc_step_instr (pc_lookup program (fst state)) state.

Fixpoint pc_run (steps : nat) (program : pc_program) (state : pc_state) : pc_state :=
  match steps with
  | 0 => state
  | S steps => pc_run steps program (pc_step program state)
  end.

Definition pc_final_at (steps : nat) (program : pc_program) (state : pc_state) : bool :=
  pc_is_final program (pc_run steps program state).

Definition PC_PROBLEM := (pc_program * pc_state)%type.

Definition PC_HALTING (problem : PC_PROBLEM) : Prop :=
  match problem with
  | (program, state) => exists steps, pc_final_at steps program state = true
  end.

(* Functional presentation of the upstream relational MM2 semantics. *)

Definition source_lookup (program : list mm2_instr) (label : nat) : option mm2_instr :=
  match label with
  | 0 => None
  | S offset => nth_error program offset
  end.

Definition source_is_final (program : list mm2_instr) (state : pc_state) : bool :=
  match source_lookup program (fst state) with
  | None => true
  | Some _ => false
  end.

Definition source_exec (instruction : mm2_instr) (state : pc_state) : pc_state :=
  match instruction, state with
  | mm2_inc_a, (label, (a, b)) => (S label, (S a, b))
  | mm2_inc_b, (label, (a, b)) => (S label, (a, S b))
  | mm2_dec_a jump, (label, (0, b)) => (S label, (0, b))
  | mm2_dec_a jump, (label, (S a, b)) => (jump, (a, b))
  | mm2_dec_b jump, (label, (a, 0)) => (S label, (a, 0))
  | mm2_dec_b jump, (label, (a, S b)) => (jump, (a, b))
  end.

Definition source_step (program : list mm2_instr) (state : pc_state) : pc_state :=
  match source_lookup program (fst state) with
  | None => state
  | Some instruction => source_exec instruction state
  end.

Fixpoint source_run (steps : nat) (program : list mm2_instr) (state : pc_state) : pc_state :=
  match steps with
  | 0 => state
  | S steps => source_run steps program (source_step program state)
  end.

Definition source_final_at (steps : nat) (program : list mm2_instr) (state : pc_state) : bool :=
  source_is_final program (source_run steps program state).

Lemma nth_error_mm2_instr_at program offset instruction :
  nth_error program offset = Some instruction ->
  mm2_instr_at instruction (S offset) program.
Proof.
  intros H.
  apply nth_error_split in H as (left & right & -> & Hlength).
  exists left, right. split; [reflexivity | lia].
Qed.

Lemma mm2_instr_at_nth_error program instruction label :
  mm2_instr_at instruction label program ->
  exists offset,
    label = S offset /\ nth_error program offset = Some instruction.
Proof.
  intros (left & right & -> & Hlabel).
  exists (length left). split; [lia |].
  rewrite nth_error_app2 by lia.
  rewrite Nat.sub_diag. reflexivity.
Qed.

Lemma mm2_atom_source_exec instruction state target :
  mm2_atom instruction state target ->
  target = source_exec instruction state.
Proof.
  intros H. destruct H; reflexivity.
Qed.

Lemma mm2_step_from_nth_error program offset instruction a b :
  nth_error program offset = Some instruction ->
  mm2_step program (S offset, (a, b))
    (source_exec instruction (S offset, (a, b))).
Proof.
  intros H. exists instruction. split.
  - now apply nth_error_mm2_instr_at.
  - destruct instruction; destruct a; destruct b; constructor.
Qed.

Lemma source_final_false_step program state :
  source_is_final program state = false ->
  mm2_step program state (source_step program state).
Proof.
  destruct state as [[|offset] [a b]].
  - intros H. unfold source_is_final, source_lookup in H.
    discriminate.
  - destruct (nth_error program offset) as [instruction|] eqn:Hlookup.
    + intros _. unfold source_step, source_lookup. simpl. rewrite Hlookup.
      now apply mm2_step_from_nth_error.
    + intros H. unfold source_is_final, source_lookup in H.
      simpl in H. rewrite Hlookup in H. discriminate.
Qed.

Lemma mm2_step_source_complete program state target :
  mm2_step program state target ->
  source_is_final program state = false /\
  target = source_step program state.
Proof.
  intros (instruction & Hinstruction & Hatom).
  destruct state as [label [a b]].
  apply mm2_instr_at_nth_error in Hinstruction as
    (offset & Hlabel & Hlookup).
  simpl in Hlabel. subst label.
  change
    ((match nth_error program offset with
      | Some _ => false
      | None => true
      end) = false /\
     target =
       match nth_error program offset with
       | Some operation => source_exec operation (S offset, (a, b))
       | None => (S offset, (a, b))
       end).
  rewrite Hlookup.
  split; [reflexivity |].
  now apply mm2_atom_source_exec.
Qed.

Lemma source_final_true_stop program state :
  source_is_final program state = true ->
  mm2_stop program state.
Proof.
  intros Hfinal target Hstep.
  apply mm2_step_source_complete in Hstep as (Hfalse & _).
  rewrite Hfinal in Hfalse. discriminate.
Qed.

Lemma source_stop_final_true program state :
  mm2_stop program state ->
  source_is_final program state = true.
Proof.
  intros Hstop.
  destruct (source_is_final program state) eqn:Hfinal; [reflexivity |].
  exfalso. apply (Hstop (source_step program state)).
  now apply source_final_false_step.
Qed.

Lemma source_functional_to_relational program state steps :
  source_final_at steps program state = true ->
  mm2_terminates program state.
Proof.
  revert state. induction steps as [|steps IH]; intros state Hfinal.
  - exists state. split.
    + apply rt_refl.
    + now apply source_final_true_stop.
  - simpl in Hfinal.
    destruct (source_is_final program state) eqn:Hnow.
    + exists state. split.
      * apply rt_refl.
      * now apply source_final_true_stop.
    + destruct (IH (source_step program state) Hfinal) as
        (target & Hreach & Hstop).
      exists target. split; [|exact Hstop].
      eapply rt_trans.
      * apply rt_step. now apply source_final_false_step.
      * exact Hreach.
Qed.

Lemma source_reaches_run program state target :
  clos_refl_trans _ (mm2_step program) state target ->
  exists steps, target = source_run steps program state.
Proof.
  rewrite clos_rt_rt1n_iff.
  intros H. induction H as [state | state middle target Hstep Hreach IH].
  - exists 0. reflexivity.
  - destruct IH as (steps & ->).
    apply mm2_step_source_complete in Hstep as (_ & ->).
    exists (S steps). reflexivity.
Qed.

Lemma source_relational_to_functional program state :
  mm2_terminates program state ->
  exists steps, source_final_at steps program state = true.
Proof.
  intros (target & Hreach & Hstop).
  apply source_reaches_run in Hreach as (steps & Htarget).
  exists steps. unfold source_final_at.
  rewrite <- Htarget. now apply source_stop_final_true.
Qed.

Lemma mm2_terminates_source_iff program state :
  mm2_terminates program state <->
  exists steps, source_final_at steps program state = true.
Proof.
  split.
  - apply source_relational_to_functional.
  - intros (steps & H). eapply source_functional_to_relational. exact H.
Qed.

(* Compiler from upstream MM2 into the explicit-branch target language. *)

Definition compile_instr (label : nat) (instruction : mm2_instr) : pc_instr :=
  match instruction with
  | mm2_inc_a => pc_inc_a (S label)
  | mm2_inc_b => pc_inc_b (S label)
  | mm2_dec_a jump => pc_dec_a (S label) jump
  | mm2_dec_b jump => pc_dec_b (S label) jump
  end.

Definition compile_observed (label : nat) (observed : option mm2_instr) : pc_instr :=
  match observed with
  | None => pc_halt
  | Some instruction => compile_instr label instruction
  end.

Fixpoint compile_tail (label : nat) (program : list mm2_instr) : pc_program :=
  match program with
  | [] => []
  | instruction :: rest =>
      compile_instr label instruction :: compile_tail (S label) rest
  end.

Definition compile_program (program : list mm2_instr) : pc_program :=
  pc_halt :: compile_tail 1 program.

Lemma nth_compile_tail program base offset :
  nth offset (compile_tail base program) pc_halt =
  compile_observed (base + offset) (nth_error program offset).
Proof.
  revert base offset. induction program as [|instruction rest IH];
    intros base [|offset]; simpl; try reflexivity.
  - now rewrite Nat.add_0_r.
  - rewrite IH. replace (S base + offset) with (base + S offset) by lia.
    reflexivity.
Qed.

Lemma nth_compile_program program label :
  pc_lookup (compile_program program) label =
  compile_observed label (source_lookup program label).
Proof.
  destruct label as [|offset]; [reflexivity |].
  unfold pc_lookup, compile_program, source_lookup. simpl.
  rewrite nth_compile_tail.
  replace (1 + offset) with (S offset) by lia. reflexivity.
Qed.

Lemma source_final_compile program state :
  source_is_final program state =
  pc_is_final (compile_program program) state.
Proof.
  destruct state as [label [a b]].
  unfold source_is_final, pc_is_final.
  rewrite nth_compile_program.
  cbn [fst].
  destruct (source_lookup program label) as [instruction|];
    [destruct instruction |]; reflexivity.
Qed.

Lemma source_step_compile program state :
  source_step program state =
  pc_step (compile_program program) state.
Proof.
  destruct state as [label [a b]].
  unfold source_step, pc_step.
  rewrite nth_compile_program.
  cbn [fst].
  destruct (source_lookup program label) as [instruction|].
  - destruct instruction; destruct a; destruct b; reflexivity.
  - reflexivity.
Qed.

Lemma source_run_compile steps program state :
  source_run steps program state =
  pc_run steps (compile_program program) state.
Proof.
  revert state. induction steps as [|steps IH]; intros state; simpl.
  - reflexivity.
  - rewrite IH, source_step_compile. reflexivity.
Qed.

Lemma source_final_at_compile steps program state :
  source_final_at steps program state =
  pc_final_at steps (compile_program program) state.
Proof.
  unfold source_final_at, pc_final_at.
  rewrite source_run_compile, source_final_compile. reflexivity.
Qed.

Lemma source_target_halting_iff program state :
  (exists steps, source_final_at steps program state = true) <->
  PC_HALTING (compile_program program, state).
Proof.
  unfold PC_HALTING. split; intros (steps & H); exists steps.
  - now rewrite <- source_final_at_compile.
  - now rewrite source_final_at_compile.
Qed.

Definition compile_problem (problem : MM2_PROBLEM) : PC_PROBLEM :=
  match problem with
  | (program, a, b) => (compile_program program, (1, (a, b)))
  end.

Theorem MM2_to_PC_HALTING : MM2_HALTING ⪯ PC_HALTING.
Proof.
  exists compile_problem.
  intros [[program a] b]. unfold MM2_HALTING, compile_problem.
  transitivity (exists steps,
    source_final_at steps program (1, (a, b)) = true).
  - apply mm2_terminates_source_iff.
  - apply source_target_halting_iff.
Qed.

Theorem PC_HALTING_undec : undecidable PC_HALTING.
Proof.
  apply (undecidability_from_reducibility MM2_HALTING_undec).
  exact MM2_to_PC_HALTING.
Qed.

Check MM2_to_PC_HALTING.
Check PC_HALTING_undec.
Print Assumptions PC_HALTING_undec.
