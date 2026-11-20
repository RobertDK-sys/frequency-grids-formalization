"""Reproducible calculations for phase_variant_obstruction.md.
Requires only Python's standard library. Inputs are the five ordinates as
printed in the problem statement; increasing their precision changes none
of the reported inequalities.
"""
import math

L = math.log(2.0)
DELTA = 2.0 * math.pi / L
# Riemann-zeta ordinates, rounded as supplied in the question.
GAMMAS = [14.1347, 21.0220, 25.0109, 30.4249, 32.9351]

print(f"L       = {L:.15f}")
print(f"Delta   = {DELTA:.15f}")
print(f"Delta/4 = {DELTA/4:.15f}")
print("n       gamma          gamma/Delta    dist_to_full_bands  theta_n       q_n=doubled-arcsin")
for n, gamma in enumerate(GAMMAS, 1):
    x = gamma / DELTA
    j = math.floor(x + 0.5)  # nearest positive integer; no ties here
    residual = gamma - j * DELTA
    theta = L * residual
    # Distance to the union of [(ell-1/4)Delta,(ell+1/4)Delta].
    distances = [abs(gamma - a) for ell in range(1, 6)
                 for a in ((ell - 0.25) * DELTA, (ell + 0.25) * DELTA)]
    distance = 0.0 if abs(residual) <= DELTA/4 else min(distances)
    q = abs(math.sin(theta/2.0))
    sigma = 1 if theta >= 0 else -1
    reconstructed = (2*sigma*math.asin(q) + 2*math.pi*j)/L
    print(f"{n}  {gamma:13.7f}  {x:14.9f}  {distance:19.9f}  {theta:13.9f}  {q:18.12f}")
    assert abs(reconstructed-gamma) < 1e-12
    if abs(residual) <= DELTA/4:
        assert abs(theta) <= math.pi/2
    assert abs(theta) <= math.pi
print("Bands for the unmodified arcsin phase, arbitrary 0<=q<=1:")
for j in range(1, 5):
    print(f"j={j}: [{(j-.25)*DELTA:.12f}, {(j+.25)*DELTA:.12f}]")
