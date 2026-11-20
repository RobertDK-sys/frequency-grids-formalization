"""Reproduce the numerical constants in low_modes.md.

Requires only Python 3 and mpmath.  The t=1 root enclosure uses exact
rational arithmetic.  The real inversion threshold is enclosed with
mpmath's directed-rounding interval arithmetic; the other decimals are
high-precision evaluations of the stated formulas.
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 80
mp.iv.dps = 60
L = mp.log(2)
PI = mp.pi


def q(u):
    return 1 + 3*u**2 - u**3


def F(t, u):
    return 24*t**2*(1-u)**2*q(u) - u**2


def t_of_u(u):
    return u/(mp.sqrt(24)*(1-u)*mp.sqrt(q(u)))


def u_of_t(t):
    t = mp.mpf(t)
    guess = mp.mpf("0.8889") if t == 1 else 1 - 1/(mp.sqrt(72)*t)
    u = mp.findroot(lambda z: F(t, z), guess)
    assert abs(F(t, u)) < mp.mpf("1e-60")
    return u


def branches(t):
    alpha = mp.asin(mp.sqrt(u_of_t(t)))
    return (2*PI-alpha)/L, (2*PI+alpha)/L


def out(name, value, digits=35):
    print(f"{name:24s} {mp.nstr(value, digits)}")


# Exact rational sign certificate for u_1 in (lo,hi).  Uniqueness of the
# root in (0,1) is one of the established facts in the problem statement.
lo = Fraction(888915, 1000000)
hi = Fraction(888916, 1000000)
for name, u in (("F1(lo)", lo), ("F1(hi)", hi)):
    value = 24*(1-u)**2*(1+3*u**2-u**3) - u**2
    print(name, "numerator =", value.numerator,
          "denominator =", value.denominator, "sign =",
          "+" if value > 0 else "-")
assert 24*(1-lo)**2*(1+3*lo**2-lo**3) - lo**2 > 0
assert 24*(1-hi)**2*(1+3*hi**2-hi**3) - hi**2 < 0

# Directed-rounding enclosures.  For 0<u<1,
# asin(sqrt(u)) = atan2(sqrt(u),sqrt(1-u)).
u_interval = mp.iv.mpf(["0.888915", "0.888916"])
alpha_interval = mp.iv.atan2(mp.iv.sqrt(u_interval),
                             mp.iv.sqrt(1-u_interval))
ivL = mp.iv.log(2)
ivPI = mp.iv.pi
b1_interval = (2*ivPI-alpha_interval)/ivL
c1_interval = (2*ivPI+alpha_interval)/ivL
print("certified alpha_1 interval:", alpha_interval)
print("certified A_{1,1} interval: ", b1_interval)
print("certified C_{1,1} interval: ", c1_interval)

# Invert b=6.8 without solving a floating-point polynomial near u=1.
alpha68 = 2*ivPI-mp.iv.mpf("6.8")*ivL
u68 = mp.iv.sin(alpha68)**2
tstar68 = u68/(mp.iv.sqrt(24)*(1-u68)*mp.iv.sqrt(mp.iv.mpf(1)
                 +3*u68**2-u68**3))
print("certified t_*(6.8) interval:", tstar68)
assert tstar68.a < 115108 and tstar68.b > 115107
assert tstar68.a > 115107 and tstar68.b < 115108

print("\nPoint evaluations (80-digit arithmetic):")
out("A_infty", 3*PI/(2*L))
out("C_infty", 5*PI/(2*L))
out("A_2 infimum", 7*PI/(2*L))
out("Delta", 2*PI/L)
alpha1 = mp.asin(mp.sqrt(u_of_t(1)))
out("alpha_1", alpha1)
out("A_{1,1}", (2*PI-alpha1)/L)
out("C_{1,1}", (2*PI+alpha1)/L)
out("7.6-A_{1,1}", mp.mpf("7.6")-(2*PI-alpha1)/L)
out("7.3-A_{1,1}", mp.mpf("7.3")-(2*PI-alpha1)/L)
out("A_infty-6.5", 3*PI/(2*L)-mp.mpf("6.5"))
for t in (3, 4, 100, 589, 115107, 115108):
    a, c = branches(t)
    out(f"A_{{1,{t}}}", a)
    if t in (1, 4, 100, 589):
        out(f"C_{{1,{t}}}", c)

# Exact real-t inversions at two specified b values.
for b in (mp.mpf("6.8"), mp.mpf("7.05")):
    alpha = 2*PI-b*L
    u = mp.sin(alpha)**2
    out(f"t_*({b})", t_of_u(u))
    out(f"u_*({b})", u)

print("7.05-A_{1,4} =", mp.nstr(mp.mpf("7.05")-branches(4)[0], 35))
print("A_{1,3}-7.05 =", mp.nstr(branches(3)[0]-mp.mpf("7.05"), 35))
