# Statement audit: `FrequencyGrids` against vf4

Scope: every top-level declaration of `FrequencyGrids/` (178 definitions and theorems; 124
theorems) compared with *Algebraic Frequency Grids, Harmonic Resonances and Primality* (vf4),
§5.1, §6.4.2–6.4.13, §6.5.2, §7.2–7.5, §10.  Method: reconstruct the paper's definitions from
its formulas and from the Python of §6.4.2–6.4.7, then read each Lean statement (including the
bodies of meaning-carrying definitions) against them.  Proof status is reported separately;
every theorem below is `sorry`-free and rests only on `propext`, `Classical.choice`,
`Quot.sound` (`scripts/check.sh`).

## A. Definitions that match exactly

| Lean | vf4 | note |
|---|---|---|
| `charPoly`, `E` | §6.5.2.1, §7.2 | `k3` free instead of `k3 = -t`; generalization |
| `b t k σ = (arcsin(σ∣s2 t∣) − 2kπ)/ln 2` | §3.1, §7.2 | identical formula |
| `b_step`, `b_step_uniform` | §3.1, §6.4.1 | step `−2π/ln 2`, independent of t,k,σ |
| `kSet α T` (with `mem_kSet_iff`) | §6.4.2 | `k ≠ 0 ∧ ∣b∣ ≤ T`, by ceilings/floors |
| `phaseDefect`, `Nphase`, `Nphase_eq_zero` | §6.4.1 | `N_phase = 0` for every truncation |
| `gramMatrix`, `gramOf` | §6.4.4 | `G_ij(X) = Σ_{n≤X} n^{−1−i(b_i−b_j)}` |
| `offRatio r_j = I_j/∣G_jj∣` | §6.4.4 | `∣G_ji∣` vs `∣G_ij∣`: equal, `G` is Hermitian (proved) |
| `Nvan` (clamped eigenvalues, relative threshold) | §6.4.7 | `max(λ,0)` reproduced; `(G+G*)/2 = G` proved |
| `etaR` | §6.5.2.1 | identical formula |

## B. Mismatches

| # | Lean | vf4 | mismatch | status |
|---|---|---|---|---|
| 1 | `s2 : ℕ → ℝ` | `_get_s2(t)`, all `t ≥ 1` | selector defined only for `1 ≤ t ≤ 589` (narrow interval); `s2 t = 0` otherwise | open; every use carries `1 ≤ t ≤ 589`. To be removed (uniqueness of the root). |
| 2 | `latticeSet = Icc 1 100 × sigmaSet` | `t_max` is a parameter: 100 in §6.4.3, **10** in §6.4.8 | `t_max = 100` hardcoded | open: parameters of the §6.4.8 experiment are not reachable. |
| 3 | `NR T` = cardinality of the image of `b` | `count_NR` de-duplicates by `round(b,12)` | exact equality instead of 1e-12 rounding | deliberate; the rounding is a numerical device, and the lattice proves collision-free. |
| 4 | `modeSet T` | `R_B(T)` | index set right, but `T : ℝ` (paper: integer) and horizon floored `⌊X⌋` in the sums | generalization; for natural `X` identical (`gramOf_nat_eq_mul_conjTranspose`). |
| 5 | `b` total on `k : ℤ` | only `k ≠ 0` | `b` is also defined at `k = 0`; the exclusion lives in `kSet`/`modeSet` | harmless: no theorem uses `b t 0 σ` as a frequency. |
| 6 | `σ : ℝ` with `σ ∈ sigmaSet` as hypothesis | `sign ∈ {1,−1}` | carrier is `ℝ`, membership as a premise | harmless: every statement that needs `±1` carries `σ ∈ sigmaSet`; `b_step` is in fact stronger. |
| 7 | `Sf t K n = Σ_σ Σ_{0<∣k∣≤K} Σ_{m≤n} m^{−1/2−ib}` | `S_f` sums over a *handful of bases* (1/2, 1/3, primes, the candidate `n`) | different formula | deliberate model of "partial harmonic sums"; the criterion below is the one requested. |
| 8 | `ResonancePredicate = Re(S_f(n−1)·S_f(n+1)) < 0` | code has both `(S_avant*S_apres).real < 0` and `Re S_f36 * Re S_f38 < 0` | the first variant is formalized | as specified in the task. |
| 9 | `PrimalityCriterionConjecture` fixes `t = 1`, `K = 10` | sweeps `t ≤ 100` and several base pairs `(k_a,k_b)` | one instance of the sweep | deliberate: a single falsifiable statement. |
| 10 | `b_collision_structure` assumes `t, t' ≤ 589` | collision analysis §6.4.9 has no such hypothesis | hypothesis is an artefact of mismatch 1 | to be removed once `s2` is the root in `(−1,0)`. |
| 11 | `NR_sub_le_Nvan` assumes no collisions | §6.4.13 claims the bound unconditionally | hypothesis is an artefact of mismatch 1/3 | removed once collisions are excluded (`NvanFreq_ge` is already unconditional on the distinct-frequency index). |
| 12 | `E_left_pos` (t ≤ 589) / `E_left_neg` (t ≥ 590) | §7.2 asserts the bracket `(−0.9999,−0.0001)` for all `t ≥ 1` | the paper is wrong from `t = 590`; the root still exists in `(−1,0)` | proved; reported in the document, Remark 3.3. |
| 13 | `exists_root_unit (k3 ≠ 0)` | `t ≥ 1` | slightly stronger | harmless. |
| 14 | `NvanLittleO`, `NoffLittleO`, `EtaTendsToOne` take `X : ℝ → ℕ` | `X = X(T)` an integer cutoff | `T` is real in the formalization | generalization; `T` integral is the paper's case. |

## C. Index sets, `k ≠ 0`, `∣b∣ ≤ T`, distinct frequencies — point by point

* **Index sets.** `modeSet` membership is characterized exactly
  (`mem_modeSet`): `t ∈ [1,100]`, `σ ∈ {−1,1}`, `k ≠ 0`, `∣b∣ ≤ T`.  The ranges `1 ≤ t` and
  `t ≤ 100` come from `latticeSet`; nothing silently widens them.
* **`k ≠ 0`.** Enforced in `kSet` (`erase 0`) and visible in `mem_kSet_iff` — not in `b`.
* **`∣b∣ ≤ T`.** `mem_kSet_iff` proves `k ∈ kSet α T ↔ k ≠ 0 ∧ ∣b_α(k)∣ ≤ T`, so the cutoff is
  an exact equivalence, not an approximation; `modeSet` then filters by membership.
* **Horizon `⌊X⌋` vs `X`.** `gramMatrix`, `gramOf`, `kLo/kHi` and the counting lemmas all use
  `⌊X⌋₊` for the number of terms; `card_kSet_bounds` and `Ntotal_bounds` are stated in `T`, not
  `⌊T⌋`, since only the frequency cutoff enters there.  For natural cutoffs the two agree
  (`gramOf_nat_eq_mul_conjTranspose`).
* **`N_R` on distinct frequencies.** `NR` is the cardinality of the image of the triplet set
  under `b` (`Counting.lean`), and `freqSet` is that same image as a finset with
  `card_freqSet : #freqSet T = NR T` definitionally; the distinct-frequency Gram matrix
  `gramFreq` is indexed by it.

## D. Non-vacuity

* `modeSet T ≠ ∅` for every `T ≥ 100`: the mode `(t,k,σ) = (1,1,1)` satisfies
  `∣b(1,1,1)∣ ≤ 2π/ln 2 < 100`.  Certified in Lean (scratch file, not part of the library,
  to respect the "no Lean changes in Phase A" instruction).
* `δ = 0` witnesses every `0 ≤ δ` side condition; `Ntotal T − ⌊X⌋ ≤ Nvan T X 0` was
  instantiated.
* The refutation `not_NvanFreqLittleO_of_le_NR` was instantiated at `X ≡ 0`, `c = 1/2`,
  giving the genuine theorem `¬ NvanFreqLittleO (fun _ => 0)`.
* **Not known satisfiable:** the hypothesis `NvanLittleO X` of
  `NvanLittleO.eventually_le_Ntotal/le_NR`.  That hypothesis *is* the conjecture; only its
  contrapositive (the refutation) is usable, and that is what is stated as a theorem.

## E. Proof status

`scripts/check.sh`: build; no `sorry`/`admit`/`native_decide`/`axiom`; `#print axioms` on all
124 theorems yields only `propext`, `Classical.choice`, `Quot.sound`.  The two genuine uses of
`Classical.choice` are the root selector `s2` and Mathlib's spectral theorem; the first is
rendered choice-independent by the uniqueness result of Phase C.
