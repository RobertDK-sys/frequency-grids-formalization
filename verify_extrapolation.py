#!/usr/bin/env python3
"""Reproduce the calculations in extrapolation_verdict.md.

Requires only mpmath.  The last section uses directed interval arithmetic;
it does not read or approximate any experimental data.
"""
import mpmath as mp

mp.mp.dps = 70
mp.iv.dps = 55
iv = mp.iv

# Computed from zeta itself, rather than read from any experimental table.
GAMMA = [mp.im(mp.zetazero(n)) for n in range(1, 6)]

print('ZETA ORDINATES FROM mpmath.zetazero')
for n, gamma in enumerate(GAMMA, 1):
    print(n, mp.nstr(gamma, 60))
print('SUCCESSIVE ORDINATE GAPS')
for x, y in zip(GAMMA, GAMMA[1:]):
    print(mp.nstr(y-x, 30))
D = GAMMA[2] - GAMMA[0]
discrepancy = 2*mp.mpf('6.9') - D
print('gamma_3-gamma_1 =', mp.nstr(D, 30))
print('min_{d in [6.9,7.2],q in Z}|D-qd| =', mp.nstr(discrepancy, 30),
      '(attained at q=2,d=6.9)')
print('sharp per-point tolerance bound =', mp.nstr(discrepancy/2, 30))
print('rounding-robust bound using 14.13 and 25.01 = 1.455')
print('one-step predecessor range =',
      mp.nstr(GAMMA[0]-mp.mpf('7.2'), 30), 'to',
      mp.nstr(GAMMA[0]-mp.mpf('6.9'), 30))

print('\nUNIFORM-SCAN ALIASING EXAMPLE')
a, b = mp.mpf('12.63'), mp.mpf('34.44')
h = (b-a)/54
omega = mp.pi/h
print('h =', mp.nstr(h, 30), '; omega =', mp.nstr(omega, 30))
print('S(7.05) =', mp.nstr(mp.sin(omega*(mp.mpf('7.05')-a)), 30))

# Wei et al., Nature Communications 17, 8163 (2026), eqs. (10), (26):
# L(beta,t) = A(beta,t)/Z(beta),
# A = sum_{n=1}^{16} (-1)^(n+1) n^(-beta-it), Z=sum n^(-beta).
ns = list(range(1, 17))
logs_mp = [mp.log(n) for n in ns]
sgn_mp = [mp.mpf(1 if n % 2 else -1) for n in ns]

def scalar_values(beta, t):
    w = [mp.power(n, -beta) for n in ns]
    Z = sum(w)
    A = sum(s*wi*mp.exp(-1j*t*li)
            for s, wi, li in zip(sgn_mp, w, logs_mp))
    Ap = sum(s*wi*(-1j*li)*mp.exp(-1j*t*li)
             for s, wi, li in zip(sgn_mp, w, logs_mp))
    Rprime = 2*mp.re(Ap*mp.conj(A))/Z**2
    return abs(A/Z), Rprime

print('\nSELECTED VALUES FOR BETA=0.5, N=16')
for ts in ('6.5', '7.05', '7.6'):
    mod, _ = scalar_values(mp.mpf(1)/2, mp.mpf(ts))
    print('t =', ts, '; |L| =', mp.nstr(mod, 35))

# Interval version.  Each cell is exactly [(6200+j)/1000,(6201+j)/1000].
logs = [iv.log(n) for n in ns]
sgn = [iv.mpf(1 if n % 2 else -1) for n in ns]

def interval_bounds(lo_int, hi_int, w, Z):
    t = iv.mpf([lo_int, hi_int])/1000
    re = im = d_re = d_im = iv.mpf(0)
    for s, wi, li in zip(sgn, w, logs):
        theta = t*li
        c, sn = iv.cos(theta), iv.sin(theta)
        re += s*wi*c
        im -= s*wi*sn
        d_re -= s*wi*li*sn
        d_im -= s*wi*li*c

    def abs_lower(x):
        if x.a > 0:
            return x.a
        if x.b < 0:
            return -x.b
        return 0

    # |L| >= sqrt(abs_lower(Re A)^2+abs_lower(Im A)^2)/Z.
    mod2 = iv.mpf(abs_lower(re))**2 + iv.mpf(abs_lower(im))**2
    modulus_lower = iv.sqrt(mod2)/Z
    # Re(A' conjugate(A)) = Re(A')Re(A)+Im(A')Im(A).
    derivative = 2*(d_re*re+d_im*im)/(Z*Z)
    return modulus_lower.a, derivative.b

print('\nDIRECTED-INTERVAL CERTIFICATE ON [6.2,7.9], 1700 CELLS')
for beta in (iv.mpf(3)/10, iv.mpf(1)/2):
    w = [iv.exp(-beta*li) for li in logs]
    Z = sum(w)
    min_mod, max_der = mp.inf, -mp.inf
    min_cell = max_cell = None
    for j in range(1700):
        mod, der = interval_bounds(6200+j, 6201+j, w, Z)
        if mod < min_mod:
            min_mod, min_cell = mod, j
        if der > max_der:
            max_der, max_cell = der, j
    print('beta =', beta)
    print('  minimum cellwise lower bound on |L| =',
          mp.nstr(min_mod, 35), '; cell =', min_cell)
    print("  maximum cellwise upper bound on (|L|^2)' =",
          mp.nstr(max_der, 35), '; cell =', max_cell)
