# The `b`-lattice against the Riemann zeros: a consolidated verdict

**Provenance.** This note consolidates the eight reports of swarm `smwoq6yh5` (8 members,
`moonshotai/kimi-k3.1-pro`, reasoning effort `max`, 8/8 solutions accepted after review, 0
rejected). The member reports, their scripts and their numerical outputs are preserved verbatim
in `paper/swarm/m1 … m8/`; every constant quoted below was recomputed independently by the
reviewer before acceptance, and the checks are recorded in §6.

**Scope.** Two distinct questions are separated throughout. (Q1) Does the frequency lattice of
"Algebraic Frequency Grids, Harmonic Resonances and Primality" (vf4) explain the zeros of `ζ`,
or the features measured in two published NMR experiments? (Q2) What can legitimately be
inferred, statistically, from those measurements? This note answers Q1 negatively with several
independent obstructions and answers Q2 by exhibiting the only defensible test. It does **not**
question the published measurements, whose agreement with `γ_n` on `12.6 ≤ t ≤ 34.4` is not at
issue.

## 1. Setting and notation

For `t ≥ 1` let `s₂(t) ∈ (−1,0)` be the root of

```
E(s,k₃) = |8s⁶ − 24s⁴ + 24s² − 8|^(2/3) (24k₃²s⁶ − 72k₃²s⁴ − 24k₃²) + 4s⁴ = 0,   k₃ = −t,
```

equivalently `u² = 24t²(1−u)²(1+3u²−u³)` with `u = s²`; the root is unique and `t ↦ |s₂(t)|` is
strictly increasing from `0.94282328…` to `1` (proved in `FrequencyGrids/Uniqueness.lean`). Put

```
L = ln 2,   Δ = 2π/L = 9.064720283654388…,   α_t = arcsin|s₂(t)|,   a_t = α_t/L,
b(t,k,σ) = (σ α_t − 2kπ)/L,   σ ∈ {−1,+1},  k ∈ ℤ∖{0}.
```

Facts established before the swarm, and used throughout: `|b| ≥ 3π/(2L) = 6.7985…` for every `k ≠ 0`
and every `t`; and `α_t ∈ [π/3, π/2)` for every `t ≥ 1` (from `α₁ > π/3` and monotonicity), so
`a_t ∈ [Δ/6, Δ/4)`. Both are now formalised (`abs_b_ge`, `arcsin_abs_s2_ge` in
`FrequencyGrids/Band.lean`).

## 2. The exact shape of the lattice

**Two branches, one centre (m5, m2, m1, m4, independently).** Because `arcsin` is odd,

```
b(t,k,σ) = σ a_t − kΔ,   so   Λ := {|b|} = {A_{j,t}, C_{j,t} : j ≥ 1, t ≥ 1},
A_{j,t} = jΔ − a_t,   C_{j,t} = jΔ + a_t,
```

and the signed lattice is `{±A_{j,t}, ±C_{j,t}}`; each magnitude has exactly two raw `(k,σ)`
representatives. Taking absolute values identifies the two sign-labelled lattices, it does not
double them.

**Sharp endpoints (m5, certified).** `A_{j,t}` decreases and `C_{j,t}` increases in `t`, with
`a₁ = 1.775960717579081`, and

```
A_{1,1} = 7.288759566075307,   C_{1,1} = 10.840681001233468,
inf Λ = 3π/(2L) = 6.798540212740791   (a limit, not attained).
```

Below `12` only the two sequences `A_{1,t}`, `C_{1,t}` occur, so `Λ ∩ (0,12)` is two discrete
sequences, not two filled intervals.

**No mode is dense in a band (m6, m5).** The consecutive gaps `g_t = a_{t+1} − a_t` satisfy
`g_t ~ C/(2t^{3/2})` with `C = 1/(72^{1/4} L) = 0.495269307316804`, and `g₁ = 0.141758854787`.
Hence the band is **not** an `0.0022`-net — `0.0022` is only the average spacing; a `0.0022`-net
(spacing `≤ 0.0044`) first holds at `t = 15`, and there is a hard hole of half-width `0.0709`
(rigorous bound `0.0537`) near `t = 1`.

**Phase accumulation (m6, exact).** With `A = √72` and `v_t = 1 − s₂(t)²`,

```
1/t = A v_t √(1 − v_t + v_t³/3)/(1 − v_t),   1/(At+1) < v_t < 1/(At),
d_t := π/(2L) − a_t = C t^{−1/2} − C/(12A) t^{−3/2} + O(t^{−5/2}).
```

This is what makes thresholds such as `t_*(6.8) = 115107.4989868134` rigorous rather than
numerical, and it explains why the low bands are sparse at `t = 1` and dense only at the
accumulation point.

## 3. The lattice cannot meet the zeta ordinates

**m2's band theorem, and it is equation-independent.** For any phase `θ` with `|θ| ≤ π/2` and any
`k ≠ 0`, a positive `b = (θ − 2kπ)/L` has `k = −j`, `j ≥ 1`, and `b = jΔ + θ/L` with
`|θ|/L ≤ Δ/4`. Therefore

```
Λ ⊆ ⋃_{j≥1} [(j − ¼)Δ, (j + ¼)Δ],
```

with equality when all phases are available, and every gap `((j+¼)Δ, (j+¾)Δ)` of length
`Δ/2 = 4.5324` is empty. **This uses only `|arcsin| ≤ π/2`**: it is unaffected by changing the
characteristic equation, enlarging `t_max`, taking more roots or either sign. This is formalised
as `abs_b_band`, together with the exact deviation identity `abs_b_sub_centre`
(`||b| − jΔ| = |arcsin(σ|s₂ t|)|/L`) and its sharpened form `abs_b_sub_centre_ge`
(`Δ/6 ≤ ` deviation for `1 ≤ t ≤ 589`).

| ordinate | nearest band edge | distance to the whole band union |
|---|---|---|
| `γ₁ = 14.1347251417` | `2Δ − Δ/4 = 15.8632604964` | `1.7285353547` |
| `γ₂ = 21.0220396388` | `2Δ + Δ/4 = 20.3956206382` | `0.6264190005` |
| `γ₃ = 25.0108575801` | **inside** band `j = 3` | `0` |
| `γ₄ = 30.4248761259` | `3Δ + Δ/4 = 29.4603409219` | `0.9645352040` |
| `γ₅ = 32.9350615877` | `4Δ − Δ/4 = 33.9927010637` | `1.0576394760` |

Consequently (m1 Theorem 1, m5, m2): for every `ε < 0.626419000549182` **at most one** of the five,
namely `γ₃`, can be within `ε` of the lattice, for arbitrary `t` and a different `t` per target;
no `t_max`, including `t_max → ∞`, can match all five to better than `1.7285353547`.

**The one hit, exactly (m1, m7).** `γ₃` lies in band `j = 3`; an exact match would need
`a_t = 3Δ − γ₃ = 2.183303270817474`, bracketed by `a₃₅ = 2.182487786973` and
`a₃₆ = 2.183657721709`, so no integer `t` matches. The nearest is
`|b(36,−3,−1)| = 25.01050312925445`, at distance `0.000354450891236` (next: `0.00081548` at
`t = 35`). One isolated approximation among many candidates.

**The `6.5 ± 0.3` window is cutoff-dependent (m5) — and this corrects an earlier overstatement.**
`6.5` itself is unattainable, since `6.5 < inf Λ = 6.79854`, and `dist(6.5, Λ) = 0.29854` is an
infimum. But the *window* `[6.2, 6.8]` is **not** empty when `t` is unbounded: it contains
`A_{1,t}` for every `t ≥ 115108`, with `t_*(6.8) = 115107.4989868134`, so
`A_{1,115107} = 6.8000000032` against `A_{1,115108} = 6.7999999968`. It is empty precisely when
`M ≤ 115107`, which covers `t_max = 100` and `589`. By contrast `[7.3, 7.9]` is empty for **every**
`t`, with margin `7.3 − A_{1,1} = 0.0112404339`.

**Counting obstructs a global correspondence (m7).** With `M = t_max`, `D_M(T)` the number of
distinct `|b| ≤ T` and `C_M = 2D_M` the sign-labelled count,

```
D_M(T) = Σ_{t≤M} (⌊(T−a_t)/Δ⌋ + ⌊(T+a_t)/Δ⌋),   2MT/Δ − 2M < D_M ≤ 2MT/Δ,
C_M(T) = (2M L/π) T + O(M),
```

so by Riemann–von Mangoldt, `C_M/N(T) ~ 4M L/log T`: for every fixed `M` the lattice is not
asymptotic to `N(T)`, and no injective `ε`-correspondence with all zero ordinates can exist
(otherwise `N(T) ≤ D_M(T+ε) = O_M(T)`). Cross-check with the formalisation: `C₁₀₀(100) = 4200 =
N_R = N_tot`, and `|4200 − 200·T·L/π| = 213 ≤ 600`, the `O(M)` slack proved as
`Ntotal_bounds`.

**Pair statistics are atomic, not GUE (m4).** A finite union of `J` distinct `Δ`-progressions has
Fourier transform a Dirac comb on `(ln 2)ℤ`, and its ordered pair-difference measure converges in
`O(1/T)` to a purely atomic measure with **mass `≥ 1` at every `Jℓ`, `ℓ ≠ 0`** — forced by the
same-progression pairs alone. The folded positive `|b|`-grid has `J = 2t_max` and density
`2t_max/Δ = t_max L/π = 22.0636` at `t_max = 100`, agreeing with m7's `D_M` slope. Hence no GUE
pair correlation, and — conditionally on Montgomery's conjecture — no fixed grid can injectively
approximate every large ordinate at `ε < δ_min/2`.

**Changing the equation cannot help; changing the phase law explains nothing (m2).** The band
structure depends only on the phase map and `Δ`. Conversely, with `j_n = round(γ_n/Δ)` and
`ϑ_n = Lγ_n − 2πj_n` (so `|ϑ_n| < π`), any phase law with `θ̃(n,±1) = ϑ_n` gives
`b̃(n,−j_n,±1) = γ_n` **exactly**; superficially, the doubled arcsine `2 arcsin(σ_n q_n)` with
`q_n = |sin(ϑ_n/2)|`, `σ_n = sgn ϑ_n` does the same. Five free phases encode five targets, predict
nothing about a sixth, and are a reparametrisation, not an explanation. A nonvanishing envelope
preserves the zero set, and arbitrary weights cannot move a Dirac comb's support.

## 4. The published model excludes the alleged `]0,10[` features (m8)

The source (arXiv:2511.11199, eq. (2); Nature Comms eq. (10) with `N = 16`) gives

```
L₁₆(β,t) = −Σ_{n=1}^{16} (−1)^{n+1} n^{−β−it} / Σ_{n=1}^{16} n^{−β}.
```

Directed-interval evaluation on 1700 rational cells certifies that `|L₁₆|` is positive and
**strictly decreasing** on `[6.2, 7.9]` for `β = 0.3` and `0.5` (lower bounds `0.1758575707` and
`0.2041752527`; derivative upper bounds `−0.0017668456` and `−0.0169907630`). So neither claimed
window contains a zero or a local trough of the published model. Values reproduced at 30 digits:
`|L₁₆(0.5,6.5)| = 0.2744084039357836`, `|L₁₆(0.5,7.05)| = 0.2443787494151568`,
`|L₁₆(0.5,7.6)| = 0.2220123147723519`.

Three further independent facts: data at 55 points do not determine any interpolant off the nodes
(the `∏_j(t−t_j)` witness, or a bounded entire sine in the uniform idealisation); a chain of steps
in `[6.9,7.2]` cannot link `γ₁` and `γ₃` unless the per-point error is at least
`1.4619337807945025` (`1.455` from rounded inputs), since `γ₃ − γ₁ = 10.876132438`; and no
thermodynamic `ζ`-induced coherence zero exists below `γ₁`, because at `β = 1/2` the factor
`1 − 2^{1−β−it}` cannot vanish (`|2^{1/2−it}| = √2`).

## 5. What may be inferred from the measurements (m3)

A retrospective agreement computed as though targets, windows, interpolation and matching rule
had been fixed in advance is not a valid `p`-value when those choices were made from the same
curves. The defensible formulation is a **prospective equivalence test**:

> `F_{A,δ,α}`: lock an algorithm `A` and an ordered injective target map before acquiring data;
> acquire fresh raw replicates in pre-specified target and control windows; at familywise level
> `α`, exhibit simultaneous confidence sets for the true minima that lie inside
> `(λ_j − δ, λ_j + δ)` for every `j`, with a pre-specified control criterion.

Concretely: exact Fieller sets for a quadratic-regression vertex; the three-point formula
`SE(τ̂) ≈ σ/(√2|q''|h)` (so horizontal precision is not the vertical error bar, and `|L|` behaves
like `C|t−τ|` at a complex zero, so a parabola on `|L|` is biased); Equivalence not non-rejection;
level proof by the union bound with no independence needed. Numbers: `J = 5`, `z₅ = 2.575829303549`,
`δ/z₅ = 0.038822448313` at `δ = 0.1`, per-target power `0.984656608348` at `s = 0.02`, all five
`0.925601393312` (independent) and `≥ 0.923283041738` (arbitrary dependence); look-elsewhere
`M = 5 Σ_a |M_a|` with `252 = C(10,5)` and `30240 = (10)₅`, giving `z₆₀₀ = 3.934605861560`
(`δ/z = 0.0254155`) and `z₁₅₁₂₀₀ = 5.105060997068` (`δ/z = 0.0195884`, where `s = 0.02` becomes
infeasible at `δ = 0.1`). Nested target sets add no multiplicity: for `Λ₁ ⊆ Λ₂`,
`{D₁ ≤ r} ⊆ {D₂ ≤ r}`, so enlarging `t_max` or a `k`-range with everything else fixed is free.

A random-target null, if one is wanted, must be stated: for `X_i` uniform on `W`, hits are
`Binomial(m,p)` with `p = λ(merged ε-neighbourhood ∩ W)/λ(W)` (Poisson-binomial for unequal
windows), and `p_band(ε) = 1/6 + 4ε/Δ`. These are null calibrations, **not** `p`-values for the
fixed `ζ` targets.

## 6. Review record

Each report was checked by reading the files, running the scripts, and recomputing the constants
independently at 30–60 digits. Two source checks were made against primary material: the Nature
Communications PDF (`t₁…t₅` "extracted through polynomial fitting"; error bars one s.d. from
repeated experiments) and the arXiv HTML of 2511.11199 (eq. (2), transcribed correctly up to a
global sign that does not affect `|L|`).

Cross-checks between independent members: the same `C = 1/(72^{1/4}L)` from m6 (phase
asymptotics) and m5 (branch endpoint asymptotics); the same `t_max L/π` slope from m7 (counting)
and m4 (density); the same five band distances from m1, m5 and m7 computed by three different
routes; `D_M = 2100` from m7's formula against a brute-force count.

Corrections imposed during review, now incorporated above:

1. m2's theorem covers only variants that keep the arcsine phase and `Δ`; it is not a statement
   that no modification whatsoever can fit.
2. The `6.5 ± 0.3` window is not empty for unbounded `t` (m5); only the exact value `6.5` is
   excluded. An earlier reviewer statement to the contrary was wrong.
3. The `0.0022` spacing is an average, not a uniform net (m5, m6); `g₁ = 0.1418` and a `0.0022`-net
   first holds at `t = 15`.
4. m8's bounded-sine witness assumes uniform nodes; the actual scan steps by `0.3` with a gap
   `15.63 → 19.52`, so the `∏_j(t − t_j)` witness is the one that applies, the sine being the
   uniform idealisation.

## 7. Verdict

1. **Positions.** `γ₁, γ₂, γ₄, γ₅` lie outside every band, hence outside the lattice, for any
   `t_max`; `γ₃` alone is admissible and is not attained. The `]0,10[` frequencies `6.5` and `7.6`
   are unattainable as exact values, and no single-beat recurrence with step `6.9–7.2` can reach
   the observed troughs. These are deterministic statements, not statistical ones.
2. **Variants.** No change of the characteristic equation, `t_max`, sign convention, weight or
   nonvanishing envelope repairs this; an unconstrained phase map fits anything and therefore
   explains nothing.
3. **Global.** A fixed grid cannot enumerate or injectively approximate all zero ordinates
   (`4M ln2/log T` against `N(T)`), and its pair statistics are atomic rather than GUE.
4. **Measurements.** The published agreement on `12.6 ≤ t ≤ 34.4` stands; the extrapolation below
   `12.63` is not identified by the data; and the only defensible test of "the lattice explains
   the observed frequencies" is a locked prospective equivalence test at a pre-declared tolerance
   — which, given (1), no admissible lattice target can pass in `[6.2, 7.9]` in any case, since
   the intervals contain no lattice points at all.

## 8. Reproducibility index

| member | direction | files | command |
|---|---|---|---|
| m1 / d3 | hitting geometry, null calibration | `m1/results/lattice_verdict.md`, `lattice_bands.py`, `verify_intervals.py`, `interval_checks.txt` | `python3 lattice_bands.py --all-distances --tmax 100` |
| m2 / d5 | phase variants, exact fit | `m2/phase_variant_obstruction.md`, `analysis.py` | `python3 analysis.py` |
| m3 / d4 | prospective statistical test | `m3/statistical_test.md`, `analysis_constants.py`, `analysis_constants.txt` | `python3 analysis_constants.py` |
| m4 / d6 | pair correlation, GUE obstruction | `m4/spectral.md` | — (analytic) |
| m5 / d7 | sharp global support | `m5/low_modes.md`, `reproduce.py`, `certificate.txt` | `python3 reproduce.py` |
| m6 / d8 | phase asymptotics | `m6/phase-map-theorem.md`, `phase_asymptotics.py`, `verification.txt` | `python3 phase_asymptotics.py` |
| m7 / d1 | exact counting, injection obstruction | `m7/proof.md`, `phase_check.py`, `numerical_output.txt` | `python3 phase_check.py` |
| m8 / d2 | extrapolation, published model | `m8/results/extrapolation_verdict.md`, `verify_extrapolation.py`, `verification.txt` | `python3 verify_extrapolation.py` |

Scripts `m1`, `m3`, `m5`, `m6`, `m7` use only the standard library or `mpmath`/`scipy`; `m8` uses
directed-interval arithmetic. The formal counterpart of §3's band theorem is
`FrequencyGrids/Band.lean` (`abs_b_band`, `abs_b_sub_centre`, `abs_b_sub_centre_ge`), verified by
`scripts/check.sh`.

## 9. What is not claimed

No assertion is made against the published experiments. The pair-correlation obstruction is
conditional on Montgomery's conjecture, which is unproved. The counting obstruction fixes `M`. No
statement is made about variants whose `t_max`, `Δ` or phases vary with height, or with continuous
`t`. And no numerical `p`-value for the lattice or extrapolation claim is derivable from the
published tables: that would require the raw `(t, Ȳ, s)`, a replicate-dependence model, the fitted
curvature or covariance, and a complete record of the analyses actually tried.
