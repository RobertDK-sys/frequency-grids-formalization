#!/usr/bin/env python3
"""Directed-rounding checks of the phase brackets used in lattice_verdict.md."""
import mpmath as mp
from lattice_bands import phase, u_of_t, DELTA, GAMMAS

mp.mp.dps = 100
mp.iv.dps = 90

def interval(x):
    return mp.iv.mpf(mp.nstr(x, 95))

def certified_u(t):
    # The unique root is bracketed by points on which f has a strict sign.
    u = u_of_t(t)
    delta = mp.mpf('1e-70')
    left, right = interval(u-delta), interval(u+delta)
    tt = interval(t)
    def fi(x):
        return x**2 - 24*tt**2*(1-x)**2*(1+3*x**2-x**3)
    fl, fr = fi(left), fi(right)
    assert fl < 0, (t, fl)
    assert fr > 0, (t, fr)
    return mp.iv.mpf([left, right])

def certified_phase(t):
    u = certified_u(t)
    # arcsin(sqrt(u)) = atan2(sqrt(u), sqrt(1-u)) for 0 < u < 1.
    return mp.iv.atan2(mp.iv.sqrt(u), mp.iv.sqrt(1-u)) / mp.iv.log(2)

def show(name, value):
    print(name, '=', mp.nstr(value, 35), 'width =', mp.nstr(value.delta, 8))

a35, a36, a100 = map(certified_phase, (35, 36, 100))
show('a35', a35)
show('a36', a36)
show('a100', a100)
D = 2*mp.iv.pi/mp.iv.log(2)
gamma3 = mp.iv.mpf('25.010857580145688763')
c = 3*D - gamma3
show('required phase c', c)
assert a35 < c < a36
print('CERTIFIED: a35 < c < a36; monotonicity then makes t=35,36 the only possible nearest integers.')
b36 = 3*D-a36
show('abs(b36-gamma3)', abs(b36-gamma3))
# For the four excluded targets, the nearest points for t<=100 all use a100.
g = [None] + [mp.iv.mpf(x) for x in (
    '14.134725141734693790', '21.022039638771554993',
    '25.010857580145688763', '30.424876125859513210',
    '32.935061587739189691')]
checks = [2*D-a100-g[1], g[2]-(2*D+a100),
          g[4]-(3*D+a100), 4*D-a100-g[5]]
for n, d in zip((1, 2, 4, 5), checks):
    show('t<=100 gap gamma%d' % n, d)
    assert d > 0
