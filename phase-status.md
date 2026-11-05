# Phase status: vf4 formalization, extension round

Status of the twelve requested steps.  Phases 0, A and B are complete and committed; Phase C
is partly complete; Phases C8, C9 and D are not done, with the obstruction stated.

| phase | step | status |
|---|---|---|
| 0 | `.gitignore` + one commit per file group + paper | **done** (13 commits) |
| A1 | audit of every declaration against vf4 | **done** — `paper/statement-audit.md` |
| A2 | non-vacuity | **done** — `modeSet T ≠ ∅` for `T ≥ 100`, hypothesis witnesses, refutation instantiated at `X ≡ 0` |
| A3 | `scripts/check.sh` | **done** — build, forbidden-construct scan, `#print axioms` gate; 132 theorems, only the three standard axioms |
| B4 | `Re Σ n^{-1+iθ} ≥ H_⌊X⌋/50` for `|θ| log X ≤ 1.55` | **done** — `FrequencyGrids/Estimate.lean` |
| B5 | `r_j ≥ 1/50 > δ` from a close neighbour | **done** — `offRatio_ge_of_close`, `Noff_eq_card_of_close` |
| C6 | strict monotonicity of `f`, uniqueness of `s2`, monotone `t ↦ |s2 t|` | **done** — `FrequencyGrids/Uniqueness.lean` |
| C7 | no collisions, `N_R = N_tot` unconditionally, drop collision hypotheses | **done** — by a route that needs no monotonicity |
| C8 | triplet and distinct-frequency matrices coincide; one diagnostic | **not done** (depends on C7); the matrix-level identity is `rfl` (`gramMatrix_eq_gramOf`), the eigenvalue transport is the missing step |
| C9 | `t_max` as a parameter | **done** — `FrequencyGrids/Parametric.lean`: `latticeSetOf` (`2·tmax`), `modeSetOf`, `NtotalOf` with `6·tmax` error, `modeSet = modeSetOf 100` (rfl) |
| D+ | brackets through `arcsin` (`Neighbour.lean`) | **done** — `arcsin\lb sub\lb le`, `inv\lb sqrt\lb le`, `abs\lb s2\lb mem\lb 1..10`, `abs\lb s2\lb gap\lb 1..9`, `inv\lb sqrt\lb bound\lb 1..9` |
| D | §6.4.8: `N_off = #modeSet` at `t_max = 10, X = 5000, δ = 1e-2` | **partly**: the reduction (`Noff_eq_card_of_close`), the certificate mechanism (`s2_mem_of_sign_change`) and the ten certified brackets of `s2(1..10)` to `4·10⁻⁶` are proved; the neighbour search over the 420/2180 frequencies is not |
| E | docs and commits | **partly** — Phase B and the audit are documented and committed; the phases that are not done are not documented as done |

## C7 without C6

C7 does not need uniqueness.  Rigidity reduces a collision to `|s2 t| = |s2 t'|`; both roots are
negative, so that makes them the *same* real number `s`, and then `E(s,−t) = 0 = E(s,−t')` reads
`u² = 24t²(1−u)²(1+3u²−u³) = 24t'²(1−u)²(1+3u²−u³)` with `u = s² ∈ (0,1)` and
`(1−u)²(1+3u²−u³) > 0`, forcing `t² = t'²`.  Hence `t ↦ |s2 t|` is injective
(`abs_s2_injective`), `HasCollision T` is false for every `T` (`not_hasCollision`), and
`N_R = N_tot` unconditionally (`NR_eq_Ntotal`).  The "no collision" hypotheses have been removed
from `NR_sub_le_Nvan`, `NvanLittleO.eventually_le_NR` and `not_NvanLittleO_of_le_NR`, so the
refutation `X ≤ c·N_R, c < 1 ⇒ NvanLittleO fails` is now hypothesis-free.

What remains of C6 is the *strict monotonicity* of `f` and hence *uniqueness* of `s2(t)` for each
`t` — needed only if one wants `s2` to be choice-independent (an audit point, not a proof
dependency: no statement above depends on which root is chosen).

## C6 closed

`Uniqueness.lean` proves `rootRat_strictMonoOn` (via `deriv_rootRat`, `deriv_rootRat_log` and the
crude bounds `2/(u(1-u)) >= 8`, `(6u-3u²)/(1+3u²-u³) <= 3`), `root_iff`, `exists_unique_root_grid`,
`s2_unique` (no dependence on `Classical.choose`), `abs_s2_strictMono`, and
`s2_mem_of_sign_change` (rational brackets certify enclosures of `s2`).

## What blocks C6 (historical note)

The mathematics is settled and elementary.  With `u = s²`, `E(s,k₃) = 0` (for `s ∈ (−1,0)`,
`k₃ ≠ 0`) is equivalent to

```
u² = 24 k₃² (1−u)² (1 + 3u² − u³),
```

i.e. to `f(u) = 24k₃²` where `f(u) = u²/((1−u)²(1+3u²−u³))`.  On `(0,1)`, `f > 0` and

```
f'/f = 2/(u(1−u)) − (6u−3u²)/(1+3u²−u³) ≥ 8 − 3 = 5 > 0
```

by the two crude bounds `2/(u(1−u)) ≥ 8` (since `u(1−u) ≤ 1/4`) and
`(6u−3u²)/(1+3u²−u³) ≤ 3` (numerator `≤ 3`, denominator `≥ 1`).  So `f` is strictly increasing
and the root is unique; `t ↦ |s₂ t|` is then strictly increasing because `t ↦ 24t²` is.

Equivalently, an explicit computation gives

```
f'(u) = u(1−u)(2 + 7u³ − 3u⁴) / ((1−u)²(1+3u²−u³))²  > 0   on (0,1),
```

all four factors being positive there.

What is missing is the Lean formalization of this derivative step.  `strictMonoOn_of_deriv_pos`
needs `0 < deriv f u` on `(0,1)`, and computing `deriv` hits a reproducible instance mismatch in
this Mathlib: `hasDerivAt_id`, `.mul`, `.pow` produce `HasDerivAt` terms carrying the
`NormedAlgebra.toNormedSpace`-based `Module ℝ ℝ` structure, while the same statement elaborated
in the project carries `Semiring.toModule`; the two are propositionally but not definitionally
equal, so `exact`/`simpa` fail and `convert` leaves an instance-equality goal
(`Real.instAddCommGroup = Real.normedCommRing.toAddCommGroup`) plus eta-expansion goals.  The
`deriv`-level statements do work (statements about `deriv` are instance-free, and `HasDerivAt.deriv`
transfers), and the pattern that succeeds is

```lean
have h := (hasDerivAt_id u).mul (hasDerivAt_id u)
have hd : deriv (id * id : ℝ → ℝ) u = 1 * id u + id u * 1 := h.deriv
rw [show (fun y : ℝ => y*y) = (id * id : ℝ → ℝ) from by funext y; simp]
rw [hd]; simp only [id_eq]; ring
```

so the step is mechanical but needs this boilerplate for each of the five pieces (numerator,
`(1−u)²`, `1+3u²−u³`, denominator, quotient).  An algebraic alternative — factoring
`v²(1−u)²g(u) − u²(1−v)²g(v)` by `(v−u)` — gives the cofactor
`u⁴v² + u³v³ − 5u³v² + u²v⁴ − 5u²v³ + 7u²v² − 2uv + u + v`, which vanishes at `(1,1)` and is
positive on `(0,1)²`, so it is not more tractable for `nlinarith`.

## D: what is newly in place (Neighbour.lean)

`arcsin_sub_le` (MVT: `arcsin a - arcsin b ≤ (a-b)/√(1-a²)` for `0<b≤a<1`), `inv_sqrt_le`
(`1/√(1-a²) ≤ R` from `1 ≤ R²(1-a²)`), the ten lifted brackets `abs_s2_mem_1..10`
(`|s2 t| ∈ (lo_t, hi_t)`), the nine gap bounds `abs_s2_gap_1..9`
(`|s2(t+1)| - |s2 t| ≤ g_t`, e.g. `0.028153` for `t=1`), and the nine reciprocal-sqrt bounds
`inv_sqrt_bound_1..9`.  Numerically all nine gaps satisfy
`g_t · R_t / ln 2 ≤ 0.1699 < 0.18 < 1.55/log 5000`, so `|b(t+1,k,σ) - b(t,k,σ)| ≤ 1.55/log 5000`
is within reach of these lemmas — assembling it, and the edge analysis, is the remaining step.

## D: what was already in place

`Noff_eq_card_of_close` (Phase B) reduces `N_off = #modeSet` at `t_max = 10, X = 5000` to a
purely geometric statement: every mode has another mode within `1.55/log 5000 ≈ 0.182`.
`s2_mem_of_sign_change` (C6) turns rational sign changes into enclosures of `s2`, and
`Enclosure.lean` now provides certified brackets of width `4·10⁻⁶` for `s2(1),…,s2(10)`.  What is
still missing is the last mile: propagating those brackets through
`b = (arcsin(σ|s2|) - 2kπ)/log 2` (needs bounds on `arcsin` on `[-0.9999,0.9999]`, on `π` and on
`log 2`), enumerating the 420 modes at `T=100` (2180 at `T=500`) and checking each against the
threshold.  That is a large but mechanical computation; it is not done here, and no claim about
`N_off` at the §6.4.8 parameters is made.

## What blocks D

* **C9 (`t_max` a parameter).**  `t_max = 100` is baked into `latticeSet` and hence into
  `modeSet`, `Ntotal`, `NR`, every Gram matrix and every counting statement, and into the
  document's constants (`200`, `600`, `44.13`).  Parameterizing it is a mechanical but
  repository-wide refactor of roughly forty statements and their proofs.
* **D (§6.4.8).**  `Noff_eq_card_of_close` reduces the claim to: every mode of `modeSet T`
  (at `t_max = 10`, `X = 5000`) has another mode within `1.55/log 5000 ≈ 0.182`.  Proving that
  requires (i) certified rational enclosures of `s₂(1),…,s₂(10)` — which C6 would make
  canonical — and (ii) a finite but large comparison over the 420 modes at `T = 100` and the
  2180 at `T = 500`.  Neither the enclosure generator nor C9's parameterization exists yet, so
  the finite verification is out of reach in this round.  Note that C6 is what would make the
  enclosures *certificates*: without uniqueness, a rational bracket can certify that *a* root
  lies in an interval, but not that the root `s₂` used by the Gram matrix is that one.

## What is in place for D

`Noff_eq_card_of_close` (Phase B) is exactly the bridge: given the geometric hypothesis, it
concludes `N_off = #modeSet` for every `δ < 1/50`, hence in particular `δ = 10^{-2}`.  The
missing input is the finite geometric verification.  Nothing in Phase D's conclusion about
`η_R` is claimed: `η_R = 1 − (N_off + N_van)/N_R ≤ 1 − N_off/N_R = 0` follows from
`N_off = N_R`, but since `N_R < X` at these parameters the rank bound gives no information on
`N_van`, so the sign of `η_R` is not determined by what is proved here.
