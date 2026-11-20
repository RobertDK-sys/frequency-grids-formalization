# Exact lattice counting and the finite band obstruction

## 1. Notation and conventions

Put
\[
L=\log 2,\qquad \Delta=\frac{2\pi}{L}=9.0647202836543876\ldots,
\qquad \alpha_t=\arcsin |s_2(t)|,\qquad \phi_t=\frac{\alpha_t}{L}.
\]
Thus \(0<\alpha_t<\pi/2\), \(\alpha_t\) is strictly increasing, and
\(0<\phi_t<\Delta/4\). Where the band hypothesis (c) is used, assume
\(\pi/3\le \alpha_t\le\pi/2\), equivalently
\(\Delta/6\le\phi_t\le\Delta/4\). In fact, the supplied monotonicity and
\(|s_2(1)|=0.94282328\ldots>\sqrt3/2\) give
\(\alpha_1>\pi/3\) and \(\alpha_t\in[\alpha_1,\pi/2)\) for **every** \(t\).
Consequently the band conclusions below need no \(t\le589\) restriction.

There are three useful counting conventions. Write
\[
A_t=\{|b(t,k,\sigma)|:k\in\mathbb Z\setminus\{0\}\}
\]
(the next lemma shows that this is independent of \(\sigma\)), and let
\(D_M(T)\) be the number of **distinct** points of
\(\cup_{1\le t\le M}A_t\) in \([0,T]\). Let \(C_M(T)\) be the corresponding
count with \((t,\sigma,k)\) multiplicity. For comparison, let \(P_M(T)\) count
triples with \(0<b(t,k,\sigma)\le T\), without taking absolute values.

## 2. Exact structure of the absolute lattice

**Lemma 1.** For every \(t\),
\[
A_t=\{j\Delta-\phi_t:j\ge1\}\cup\{j\Delta+\phi_t:j\ge1\}. \tag{1}
\]
The two sign choices \(\sigma=\pm1\) give exactly the same set \(A_t\). Every
point in (1) has precisely two representations with \(t\) fixed, one for each
sign choice. Furthermore, all points in (1) are distinct, and
\(A_t\cap A_u=\varnothing\) for \(t\ne u\).

**Proof.** Since \(\arcsin\) is odd,
\(b(t,k,\sigma)=(\sigma\alpha_t-2\pi k)/L=\sigma\phi_t-k\Delta\).
For \(\sigma=+1\), positive and negative \(k\) give respectively
\(j\Delta-\phi_t\) and \(j\Delta+\phi_t\) after taking absolute values, with
\(j\ge1\). The case \(\sigma=-1\) gives the same two families, with the two
signs of \(k\) interchanged. All these numbers are positive because
\(j\Delta-\phi_t>3\Delta/4\).

If \(j\Delta+\varepsilon\phi_t=l\Delta+\eta\phi_u\), where
\(\varepsilon,\eta\in\{-1,1\}\), multiplication by \(L\) gives
\[
2\pi(j-l)=\eta\alpha_u-\varepsilon\alpha_t. \tag{2}
\]
The right side has absolute value at most \(\pi\), whereas the left side is an
integral multiple of \(2\pi\). Hence \(j=l\) and
\(\eta\alpha_u=\varepsilon\alpha_t\). If \(t=u\), this also implies
\(\varepsilon=\eta\), proving distinctness within \(A_t\). If \(t\ne u\), the
strict monotonicity and positivity of \(\alpha_t\) make the last equality
impossible, whether \(\varepsilon=\eta\) or not. Finally, for each point and
fixed \(t\), the construction above supplies one \(k\) for each sign choice and
no other representation. \(\square\)

In particular, merely taking absolute values does not double the number of
independent frequencies: it identifies the two sign-labelled lattices.

**Lemma 2 (exact counting formula).** If \(T\ge\Delta/4\), then
\[
D_M(T)=\sum_{t=1}^M\left(
\left\lfloor\frac{T-\phi_t}{\Delta}\right\rfloor+
\left\lfloor\frac{T+\phi_t}{\Delta}\right\rfloor\right), \tag{3}
\]
and \(C_M(T)=2D_M(T)\). Moreover \(P_M(T)=D_M(T)\) exactly. Consequently
\[
2M\frac{T}{\Delta}-2M<D_M(T)\le 2M\frac{T}{\Delta},
\]
so
\[
D_M(T)=\frac{ML}{\pi}T+O(M),\qquad
C_M(T)=\frac{2ML}{\pi}T+O(M), \tag{4}
\]
with respective signed errors in \((-2M,0]\) and \((-4M,0]\).

**Proof.** Equation (3) counts the permissible positive integers \(j\) in the
two families in (1); Lemma 1 justifies summing without any inclusion-exclusion
correction. The condition \(T\ge\Delta/4\) ensures that both floor arguments
are nonnegative for every \(t\). The multiplicity statement is also Lemma 1.
For \(P_M(T)\), \(\sigma=+1\) contributes only \(j\Delta+\phi_t\), whereas
\(\sigma=-1\) contributes only \(j\Delta-\phi_t\); hence its summand is again
exactly the summand in (3). Finally use \(x-1<\lfloor x\rfloor\le x\).
\(\square\)

For \(M=100\), the two slopes in (4) are
\[
\frac{100L}{\pi}=22.0635600152651593\ldots,\qquad
\frac{200L}{\pi}=44.1271200305303187\ldots.
\]
These are asymptotic densities, not assertions of equidistribution inside the
bands.

### Local spacing and multiplicity

Within one \(A_t\), consecutive points alternate between the gaps
\[
2\phi_t=\frac{2\alpha_t}{L},\qquad \Delta-2\phi_t.
\]
Under hypothesis (c), both lie in \([\Delta/3,2\Delta/3]\), and their mean is
\(\Delta/2\). After normalization by the mean spacing, the empirical nearest
neighbour spacing law for a fixed \(t\) is therefore the two-point law giving
mass \(1/2\) to each of
\[
\frac{2\alpha_t}{\pi}\in[2/3,1],\qquad
2-\frac{2\alpha_t}{\pi}\in[1,4/3].
\]
It is not a continuous GUE spacing law. This statement does **not** extend to
a positive minimum gap for the superposition of different \(t\)'s: points from
different \(A_t\) can be arbitrarily close. A valid bound for the
superposition is that an interval of length \(\ell\) contains at most
\(2(\lfloor\ell/\Delta\rfloor+1)\) distinct points per \(t\), and at most twice
as many with sign multiplicity.

## 3. The five low zeta ordinates: a stronger finite obstruction

Under (c), equation (1) puts every absolute lattice point in
\[
\mathcal E=\bigcup_{j\ge1}\left(
\left[\frac{2\pi j-\pi/2}{L},\frac{2\pi j-\pi/3}{L}\right]
\cup
\left[\frac{2\pi j+\pi/3}{L},\frac{2\pi j+\pi/2}{L}\right]
\right). \tag{5}
\]
This is only an envelope: membership in \(\mathcal E\) does not imply that a
point is attained by any particular finite set of \(t\)'s. Nonmembership, on
the other hand, is an exact obstruction for every \(t\), \(k\), and \(\sigma\)
to which (c) applies.

The following values use the standard high-precision ordinates; replacing them
by the four-decimal values in the question changes none of the conclusions.
For an ordinate outside (5), the last column is its distance to the **whole
envelope**, not merely to the points attained for \(t\le100\) or \(t\le589\).
For \(\gamma_3\), which is inside the envelope, it instead records the distance
to the nearest band endpoint.

| ordinate | location relative to (5) | relevant/nearest band endpoint | endpoint distance |
|---|---|---:|---:|
| \(\gamma_1=14.1347251417\ldots\) | outside | \(15.8632604964\ldots\) | \(1.7285353547\ldots\) |
| \(\gamma_2=21.0220396388\ldots\) | outside | \(20.3956206382\ldots\) | \(0.6264190005\ldots\) |
| \(\gamma_3=25.0108575801\ldots\) | inside the \(j=3\) lower band | \(24.9279807800\ldots\) | \(0.0828768001\ldots\) |
| \(\gamma_4=30.4248761259\ldots\) | outside | \(29.4603409219\ldots\) | \(0.9645352040\ldots\) |
| \(\gamma_5=32.9350615877\ldots\) | outside | \(33.9927010637\ldots\) | \(1.0576394760\ldots\) |

For example, the exact bound for \(\gamma_2\) is
\[
\gamma_2-\frac{4\pi+\pi/2}{L}
=\gamma_2-\frac{9\pi}{2\log2}
=0.626419000549\ldots,
\]
and the next band begins at \(24.9279807800\ldots\), so no other band is
closer. The other rows follow from the same explicit endpoint formulas.

**Corollary 1.** No lattice in the stated construction can approximate all
five ordinates simultaneously to tolerance less than \(0.6264\), for any
\(t_{max}\), including an unbounded choice of \(t\). In particular,
accuracy \(0.0022\) is impossible. Four of the five targets are excluded by
(5); only \(\gamma_3\) passes this necessary band test. Extending \(t_{max}\),
choosing either sign, using alternating signs, or multiplying amplitudes by an
envelope cannot remove this obstruction: these operations either leave (1)
unchanged, select a subset of it, or leave the frequency locations unchanged.

The table is deliberately not phrased as a claim that \(\gamma_3\) is exactly
attained. It is not excluded by the envelope; that weaker statement is all the
band argument proves.

## 4. Rigorous counting obstruction for a global zeta correspondence

Let
\[
N(T)=\#\{\rho:\zeta(\rho)=0,\ 0<\operatorname{Im}\rho\le T\},
\]
counting zeros with multiplicity. The Riemann--von Mangoldt theorem, which
does not assume the Riemann Hypothesis, states
\[
N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T)
\quad(T\to\infty),
\]
and in particular \(N(T)\sim(T/2\pi)\log T\). Comparing this with (4) gives
\[
\frac{D_M(T)}{N(T)}\sim\frac{2ML}{\log T},\qquad
\frac{C_M(T)}{N(T)}\sim\frac{4ML}{\log T}. \tag{6}
\]
Thus, for every **fixed** \(M\), neither counting function is asymptotic to
\(N(T)\), and the lattice cannot be an asymptotic enumeration of all zeta zero
ordinates.

A tolerance version is equally precise. Fix \(\varepsilon>0\), and suppose
that for arbitrarily large \(T\) there were an injection \(\iota_T\) from the
zero ordinates \(0<\gamma\le T\) into distinct absolute lattice points of
\(\cup_{t\le M}A_t\), with \(|\iota_T(\gamma)-\gamma|\le\varepsilon\).
Then all images lie in \([0,T+\varepsilon]\), forcing
\[
N(T)\le D_M(T+\varepsilon)=\frac{ML}{\pi}T+O_{M,\varepsilon}(1),
\]
which contradicts Riemann--von Mangoldt for sufficiently large \(T\). Using
sign-labelled images instead only replaces \(D_M\) by \(C_M\) and does not
change the conclusion.

This obstruction has two essential limits. First, it concerns an injective
correspondence with **all** zeros, not an arbitrary statement that some zeros
are near some lattice points. Second, it fixes \(M\); allowing \(M\) to grow
with \(T\) changes (4). At the experimental scale the lattice is much denser
than the zeta sequence, so a high density or a few close matches is not evidence
of a spectral correspondence. For the five low ordinates, Section 3 supplies
the relevant finite obstruction directly and does not depend on any asymptotic
argument.

## 5. Verdict for variants

For fixed phase law and step \(\Delta\), equations (1), (3), and (6) are exact
structural statements. Position-preserving modifications cannot produce a
global zeta enumeration or repair the finite band failures. No universal
impossibility claim is legitimate for an unrestricted choice of a new phase map
or characteristic equation: one can always fit finitely many ordinates by
choosing their residues modulo a new step as phases. Such a fit is a new,
data-parametrized construction, not a consequence of the given \(b\)-lattice.
A nonvacuous possibility theorem for a variant must therefore fix its phase law
independently of the target ordinates and account for its number of free
phases; the obstruction above applies whenever the original range (c) and step
are retained.

## 6. Reproducibility of the numerical checks

`phase_check.py` evaluates
\[
f_t(u)=u^2-24t^2(1-u)^2(1+3u^2-u^3)
\]
by bisection on \(0<u<1\), computes \(\alpha_t=\arcsin\sqrt u\), and searches
(1). It uses 60 decimal digits. With \(M=100\), the nearest computed absolute
lattice points to \(\gamma_1,\ldots,\gamma_5\) are at distances
\[
1.7780574201,\quad0.6759410660,\quad0.0003544508912,\quad
1.0140572694,\quad1.1071615414.
\]
With \(M=589\), they are
\[
1.7489422307,\quad0.6468258766,\quad0.0003544508912,\quad
0.9849420800,\quad1.0780463520.
\]
The small distance for \(\gamma_3\) is attained at \(t=36,j=3\) in the minus
family of (1), with \(|b|=25.01050312925445\ldots\). These are numerical
attained-point calculations, in contrast to the exact envelope bounds in
Section 3. They illustrate why a single close point among many candidates does
not rescue simultaneous agreement.
