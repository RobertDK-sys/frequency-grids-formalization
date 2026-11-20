#!/usr/bin/env python3
"""Reproduce the numerical constants in statistical_test.md."""
from scipy.stats import norm

ALPHA = 0.05
DELTA = 0.1
GAMMA = [14.134725141734694, 21.022039638771555,
         25.01085758014569, 30.424876125859513,
         32.93506158773919]


def z_bonferroni(m):
    return norm.ppf(1.0 - ALPHA / (2.0 * m))


print("grid spacing if 55 equally spaced points span [12.63,34.44]")
print(f"h = {(34.44-12.63)/54:.15f}")
print()

print("preassigned five-target analysis")
z5 = z_bonferroni(5)
s = 0.02
r = DELTA - z5*s
p = 2*norm.cdf(r/s)-1
print(f"z_5 = {z5:.12f}")
print(f"delta/z_5 = {DELTA/z5:.12f}")
print(f"margin at s=0.02 = {r:.12f}")
print(f"single-target power = {p:.12f}")
print(f"independent all-five power = {p**5:.12f}")
print(f"dependence-robust lower bound = {1-5*(1-p):.12f}")
print()

print("look-elsewhere illustrations")
for label, m in [
    ("fixed mapping, 5", 5),
    ("120 settings, fixed mapping", 120*5),
    ("one setting, monotone best five of ten", 5*252),
    ("one setting, unrestricted injection from ten", 5*30240),
    ("120 settings, monotone best five of ten", 120*5*252),
    ("120 settings, unrestricted injection from ten", 120*5*30240),
]:
    z = z_bonferroni(m)
    print(f"{label}: M={m}, z={z:.12f}, delta/z={DELTA/z:.12f}")

print()
print("Sidak check for five independent targets")
q = (1-ALPHA)**(1/5)
z_sidak = norm.ppf((1+q)/2)
print(f"per-target two-sided coverage = {q:.15f}")
print(f"z_Sidak = {z_sidak:.12f}")


def fieller_set(theta, cov, alpha=ALPHA):
    """Coefficients of q(x)=A*x^2+B*x+C defining the Fieller set.

    The returned set is {(x): A*x^2+B*x+C <= 0}, up to roundoff.
    theta is (theta0,theta1,theta2), and cov is its known 3x3 covariance.
    Here x=(t-t0)/h, so the minimum is x=-theta1/(2*theta2).
    This function is a reproducible implementation of equation (4).
    """
    import numpy as np
    theta = np.asarray(theta, dtype=float)
    cov = np.asarray(cov, dtype=float)
    z = norm.ppf(1-alpha/2)
    b, c = theta[1], theta[2]
    vbb, vbc, vcc = cov[1, 1], cov[1, 2], cov[2, 2]
    A = 4*c*c - z*z*4*vcc
    B = 4*b*c - z*z*4*vbc
    C = b*b - z*z*vbb
    return float(A), float(B), float(C)


if __name__ == "__main__":
    # A curvature well separated from zero gives a bounded interval here.
    coeffs = fieller_set([0.2, 0.01, 1.0],
                         [[0.01, 0, 0], [0, 0.0004, 0], [0, 0, 0.0001]])
    print()
    print("Fieller polynomial coefficients for documented example:", coeffs)
