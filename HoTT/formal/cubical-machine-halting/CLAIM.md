# Cubical machine halting and concrete divergence claims

> Proof ID：`PF-CUBICAL-MACHINE-HALTING-001`
> Theory：Cubical Agda 2.8.0 with Cubical library v0.9
> Source：`MachineHalting.agda`

## Exact claims

### `MP-CMH-HALTS-001`

Under the definitions of `Instr`, `Program`, `Config`, `step`, `iterate`, `isFinal` and the propositionally truncated `Halts` in the source:

```agda
halt-now : Halts haltProgram initial
```

The witness uses step index `zero`, because `haltProgram` maps every label to `halt`.

### `MP-CMH-DIVERGES-001`

Under the same definitions:

```agda
loop-diverges : Diverges loopProgram initial
```

Expanding `Diverges`, the exact quantified proposition is:

```agda
(n : ℕ) →
  isFinal loopProgram
    (iterate n (step loopProgram) initial)
  ≡ false
```

`loopProgram` maps every label to `inc0 zero`, so `isFinal` reduces to `false` for every finite index.

### `MP-CMH-NOT-HALTS-001`

Under the same definitions:

```agda
loop-not-halts : ¬ Halts loopProgram initial
```

The proof eliminates the propositional truncation into `⊥`: any finite witness says the finality Bool is `true`, while `loop-diverges` says the same Bool is `false`.

## Assumptions and structure

- No postulate is introduced by this source.
- The file enables Cubical Agda and the standard checker-enforced fragment through its exact `OPTIONS` line.
- `Halts` uses Cubical library propositional truncation; the machine transition and concrete divergence invariant otherwise remain at set/proposition level.
- The proof terms `halt-now`, `loop-diverges` and `loop-not-halts` themselves complete checking. The modeled `loopProgram`, rather than the proof checker, is the object shown to lack a finite halting witness.

## Prohibited extrapolation

These claims do not establish:

- undecidability of the halting problem for all programs;
- existence or nonexistence of a universal machine for this `Program` representation;
- a Gödel sentence, provability predicate or incompleteness theorem;
- a HoTT-specific cause of divergence;
- a contradiction in HoTT or Cubical Agda;
- a same-task comparison with a physical or social process;
- any theorem about all possible notions of machine, time or computation.
