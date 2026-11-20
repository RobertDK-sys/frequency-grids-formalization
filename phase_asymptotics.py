"""Reproducible calculations for the phase-map expansion.
All logarithms are natural; no data outside this file are used.
"""
import math
A = math.sqrt(72.0)
L = math.log(2.0)
AINF = math.pi/(2*L)
C = A**(-0.5)/L
D = -C/(12*A)

def R(v):
    return math.sqrt(1.0-v+v**3/3.0)/(1.0-v)

def root_v(t):
    # t >= 1; H(v)=A*v*R(v) is strictly increasing on (0,1).
    target = 1.0/t
    lo, hi = 0.0, min(0.5, 1.0/(A*t))
    assert A*hi*R(hi) >= target
    for _ in range(100):
        mid = (lo+hi)/2
        if A*mid*R(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

def phase_data(t):
    v = root_v(t)
    deficit = math.asin(math.sqrt(v))/L
    return v, AINF-deficit, deficit

def main():
    print(f"A={A:.15f} C={C:.15f} D={D:.15f} a_inf={AINF:.15f}")
    print("t   v   v*t   a_t   deficit   deficit*sqrt(t)/C   gap_to_next")
    for t in [1,2,3,4,5,10,20,50,100,589,1000,10000,100000,1000000]:
        v,a,d = phase_data(t)
        gap = d-phase_data(t+1)[2]
        print(f"{t:7d} {v:.12e} {v*t:.12f} {a:.12f} {d:.12e} "
              f"{d*math.sqrt(t)/C:.12f} {gap:.12e}")
    print("second-order check: (d-C/sqrt(t))*t^(3/2), D=", D)
    for t in [10,100,1000,10000,100000]:
        d=phase_data(t)[2]
        print(t, (d-C/math.sqrt(t))*t**1.5)
    print("gap ratio gap/(C/(2*t^(3/2)))")
    for t in [1,2,10,100,1000,10000]:
        gap=phase_data(t)[2]-phase_data(t+1)[2]
        print(t, gap/(C/(2*t**1.5)))

    # Check all proved bounds at every integer through 10000.  These are
    # numerical checks of the stated formulas, not substitutes for the proof.
    max_gap = (0.0, None)
    for t in range(1, 10001):
        v, a, d = phase_data(t)
        dn = phase_data(t+1)[2]
        gap = d-dn
        assert 1/(A*t+1) < v < 1/(A*t)
        assert 1/(L*math.sqrt(A*t+1)) < d < 1/(L*math.sqrt(A*t-1))
        lower = ((A*t+1)**-0.5-(A*(t+1)-1)**-0.5)/L
        G = ((A*t-1)**-0.5-(A*(t+1)+1)**-0.5)/L
        assert 0 < lower < gap < G
        if gap > max_gap[0]:
            max_gap = (gap, t)
    print("all scalar/deficit/gap bounds passed for 1<=t<=10000")
    print("largest computed gap and its left index:", max_gap)
    print("first midpoint's distance from every integer phase:", max_gap[0]/2)
    first_gap_lb = ((A+1)**-0.5-(2*A-1)**-0.5)/L
    print("rigorous lower bound on first gap:", first_gap_lb)

    def G(t):
        return ((A*t-1)**-0.5-(A*(t+1)+1)**-0.5)/L
    tau = 0.0022
    direct_T = next(T for T in range(1,1000) if G(T)/2 <= tau)
    closed_T = math.ceil((1+((A+2)/(4*L*tau))**(2/3))/A)
    print("tau", tau, "direct G certificate T", direct_T,
          "G(T)/2", G(direct_T)/2, "closed-form certificate T", closed_T)

if __name__ == '__main__':
    main()
