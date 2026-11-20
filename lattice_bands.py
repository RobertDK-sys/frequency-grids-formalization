#!/usr/bin/env python3
"""Reproduce the band and finite-t calculations in lattice_verdict.md.
Only mpmath and the formulas stated in the problem are used.
"""
import argparse
import mpmath as mp

mp.mp.dps = 80
LOG2 = mp.log(2)
DELTA = 2 * mp.pi / LOG2
ALO = mp.pi / (3 * LOG2)
AHI = mp.pi / (2 * LOG2)
# Extra digits are standard numerical values; using the digits in the question
# instead changes none of the reported conclusions at the displayed precision.
GAMMAS = tuple(mp.mpf(x) for x in (
    "14.134725141734693790",
    "21.022039638771554993",
    "25.010857580145688763",
    "30.424876125859513210",
    "32.935061587739189691",
))

def f(u, t):
    return u**2 - 24*t**2*(1-u)**2*(1+3*u**2-u**3)

def u_of_t(t):
    """Bisect the stated equivalent equation on 0<u<1."""
    t = mp.mpf(t)
    lo, hi = mp.mpf(0), mp.mpf(1)
    assert f(lo, t) < 0 and f(hi, t) > 0
    for _ in range(260):
        mid = (lo + hi)/2
        if f(mid, t) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi)/2

def phase(t):
    return mp.asin(mp.sqrt(u_of_t(t))) / LOG2

def band_distance(x):
    """Distance to the closure of the union of all bands in fact (c)."""
    candidates = []
    # Centers outside this range cannot improve on the closest center.
    j0 = int(mp.floor(x/DELTA))
    for j in range(max(1, j0-2), j0+4):
        for sign in (-1, 1):
            p, q = sorted((j*DELTA + sign*ALO,
                           j*DELTA + sign*AHI))
            d = max(p-x, x-q, mp.mpf(0))
            candidates.append((d, j, sign, p, q))
    return min(candidates, key=lambda z: z[0])

def lattice_distance(x, t_values):
    """Exact formula, evaluated numerically over the supplied finite t set."""
    candidates = []
    j0 = int(mp.floor(x/DELTA))
    phases = [(t, phase(t)) for t in t_values]
    for j in range(max(1, j0-2), j0+4):
        for sign in (-1, 1):
            for t, a in phases:
                candidates.append((abs(x-(j*DELTA+sign*a)), t, j, sign))
    return min(candidates, key=lambda z: z[0])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tmax", type=int, default=100)
    parser.add_argument("--all-distances", action="store_true",
                        help="O(tmax) phases per target; use only for small tmax")
    parser.add_argument("--null-coverage", action="store_true",
                        help="reproduce the random-target null calibration table")
    args = parser.parse_args()
    print("Delta =", mp.nstr(DELTA, 40))
    print("phase interval =", mp.nstr(ALO, 30), mp.nstr(AHI, 30))
    for j in range(1, 5):
        print("j =", j,
              "lower =", mp.nstr(j*DELTA-AHI, 20), mp.nstr(j*DELTA-ALO, 20),
              "upper =", mp.nstr(j*DELTA+ALO, 20), mp.nstr(j*DELTA+AHI, 20))
    print("a(1) =", mp.nstr(phase(1), 40),
          "|s2(1)| =", mp.nstr(mp.sqrt(u_of_t(1)), 40))
    print("Distances to band closures (d, gamma, j, sign):")
    for n, g in enumerate(GAMMAS, 1):
        d, j, sign, p, q = band_distance(g)
        print(n, mp.nstr(d, 35), j, sign,
              "interval", mp.nstr(p, 20), mp.nstr(q, 20))
    c = 3*DELTA-GAMMAS[2]
    print("phase required for an exact lower-band match to gamma_3 =",
          mp.nstr(c, 40))
    for t in (35, 36):
        a = phase(t)
        print("t =", t, "a =", mp.nstr(a, 40),
              "b = 3Delta-a =", mp.nstr(3*DELTA-a, 40),
              "b-gamma_3 =", mp.nstr(3*DELTA-a-GAMMAS[2], 35))
    if args.all_distances:
        ts = range(1, args.tmax+1)
        print("Finite lattice distances for t = 1,...,", args.tmax)
        for n, g in enumerate(GAMMAS, 1):
            d, t, j, sign = lattice_distance(g, ts)
            print(n, "d =", mp.nstr(d, 35), "t =", t,
                  "j =", j, "sign =", sign)
    if args.null_coverage:
        L, U = mp.mpf('12.63'), mp.mpf('34.44')
        print("Null coverage in W = [12.63,34.44]")
        for e in ('0.0001', '0.00035445089123626978', '0.001', '0.0022', '0.01', '0.1'):
            length = covered_length(args.tmax, e)
            p = length/(U-L)
            print("eps", e, "covered_length", mp.nstr(length, 30),
                  "p", mp.nstr(p, 30), "P_all_5", mp.nstr(p**5, 20),
                  "P_at_least_1_5", mp.nstr(1-(1-p)**5, 20))

# Kept separate from main() so importing the formulas has no side effects.
def covered_length(tmax, epsilon, window=(mp.mpf('12.63'), mp.mpf('34.44'))):
    """Length of W intersected with the union of epsilon-balls about Lambda_T."""
    L, U = window
    eps = mp.mpf(epsilon)
    phases = [phase(t) for t in range(1, tmax+1)]
    intervals = []
    jmax = int(mp.ceil(U/DELTA)) + 1
    for j in range(1, jmax+1):
        for sign in (-1, 1):
            for a in phases:
                b = j*DELTA + sign*a
                p, q = max(L, b-eps), min(U, b+eps)
                if p <= q:
                    intervals.append((p, q))
    intervals.sort()
    total = mp.mpf(0)
    if intervals:
        p, q = intervals[0]
        for r, s in intervals[1:]:
            if r <= q:
                q = max(q, s)
            else:
                total += q-p
                p, q = r, s
        total += q-p
    return total

if __name__ == "__main__":
    main()
