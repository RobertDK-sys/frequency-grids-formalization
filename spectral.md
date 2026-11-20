# Fixed frequency grids have an atomic difference spectrum

## Scope and verdict

This note proves a spectral obstruction, rather than another counting bound. Let

\[
\Delta=\frac{2\pi}{\log 2}=9.064720283654388\ldots .
\]

A **fixed finite common-step grid** is obtained from finitely many progressions \(\phi_j+\Delta\mathbb Z\) by deleting at most finitely many points and, if desired, restricting to the positive axis. The positive part of every fixed-\(t_{\max}\) \(b\)-grid in the question has this form.

We prove:

1. The two-sided Fourier transform is a Dirac comb supported on \((\log 2)\mathbb Z\); an exact finite-window version follows from geometric series.
2. The ordered pair-difference measure, normalized by the grid's own mean spacing, converges to an explicit **purely atomic** measure. Same-progression pairs give an atom of mass at least \(1\) at every nonzero integer multiple of \(J\), where \(J\) is the number of progressions.
3. Thus it cannot have the absolutely continuous GUE pair correlation. More directly at zeta scaling, if every sufficiently large zeta ordinate has a **distinct** representative on such a grid within fixed \(\varepsilon<\delta_{\min}/2\), where \(\delta_{\min}\) is its least positive gap, then the precisely stated zeta pair-correlation conjecture below fails. Exact eventual containment needs no separate injectivity assumption. This implication is **conditional**: GUE pair correlation for zeta is unproved.

This is a non-vacuous formulation of a putative full-spectrum explanation: it predicts every sufficiently large gap, not just five fitted ordinates. It does **not** rule out five or ten finite near-coincidences. Also, the pair-correlation formula for a whole grid does not by itself describe an arbitrarily selected sparse subset. Finite claims need the separate tolerance and multiple-testing analyses.

## 1. Definitions and two elementary lemmas

Let \(J<\infty\), and suppose \(\phi_1,\ldots,\phi_J\) are distinct modulo \(\Delta\). Put

\[
\Lambda=\bigcup_{j=1}^J(\phi_j+\Delta\mathbb Z),\qquad
\Lambda_T=\Lambda\cap(0,T],\qquad N(T)=|\Lambda_T|,\qquad c=J/\Delta .
\]

The union is disjoint. All asymptotic statements below remain true, with the same limit measure, after deleting finitely many points.

**Lemma 1 (counting with explicit error).** For every progression and interval \(I\subset\mathbb R\), the number of its points in \(I\) differs from \(|I|/\Delta\) by at most \(1\). Consequently

\[
|N(T)-cT|\le J,\qquad N(T)=cT+O(1).
\]

Thus \(c^{-1}=\Delta/J\) is the asymptotic mean spacing.

**Proof.** Use the floor-function count for an arithmetic progression and sum over \(J\) progressions. \(\square\)

Define

\[
\delta_{ij}=\min_{n\in\mathbb Z}|\phi_j-\phi_i+n\Delta|\quad(i\ne j),
\qquad
\delta_{\min}=\min\bigl(\Delta,\min_{i\ne j}\delta_{ij}\bigr).
\]

**Lemma 2 (least gap).** \(\delta_{\min}>0\), and any two distinct points of \(\Lambda\) differ by at least \(\delta_{\min}\).

**Proof.** Each \(\delta_{ij}>0\) because phases are distinct modulo \(\Delta\), and there are finitely many pairs. Same-progression differences are nonzero multiples of \(\Delta\); cross-progression differences have the displayed form. \(\square\)

If \(t_{\max}\) grows with height or \(J=\infty\), these lemmas need not hold. In the actual construction \(a_t:=\arcsin|s_2(t)|\to\pi/2\). For fixed \(k,\sigma\),
\(b(t,k,\sigma)\to(\sigma\pi/2-2k\pi)/\log2\). Hence infinitely many integer \(t\), without \(t_{\max}\), produce accumulation points rather than a locally finite set. Finiteness is essential to the spectral formulation.

## 2. Fourier comb and finite-window certificate

Use the convention

\[
\widehat\nu(\xi)=\int e^{i\xi x}\,d\nu(x).
\]

For \(\nu_\phi=\sum_{m\in\mathbb Z}\delta_{\phi+m\Delta}\), Poisson summation for Dirac combs gives

\[
\widehat{\nu_\phi}
 =e^{i\phi\xi}\frac{2\pi}{\Delta}
   \sum_{q\in\mathbb Z}\delta_{\xi-2\pi q/\Delta}.
\]

Therefore, distributionally,

\[
\boxed{\quad
\widehat{\sum_{j=1}^J\nu_{\phi_j}}
 =\log 2\sum_{q\in\mathbb Z}
   \left(\sum_{j=1}^J e^{i\phi_j q\log2}\right)
   \delta_{\xi-q\log2}.\quad}
\]

Deleting finitely many points subtracts a finite trigonometric sum and does not change the Dirac-comb part. This identity concerns the natural two-sided extension; a one-sided transform also has a boundary term.

For an ordinary finite-sum certificate, fix one progression and put

\[
A_T(\xi)=\sum_{x\in(\phi+\Delta\mathbb Z)\cap(0,T]}e^{i\xi x}.
\]

Its indices are consecutive. A geometric-series estimate gives

\[
|A_T(\xi)|\le \frac1{|\sin(\Delta\xi/2)|}
\quad\text{if }\xi\notin(\log2)\mathbb Z,
\]

whereas, if \(\xi\in(\log2)\mathbb Z\),

\[
|A_T(\xi)|=|\Lambda_T\cap(\phi+\Delta\mathbb Z)|=T/\Delta+O(1).
\]

Thus \(|A_T(\xi)|^2/T=O_\xi(1/T)\) off comb frequencies, while at a comb frequency it grows linearly in \(T\). These are exact finite-\(T\) statements.

## 3. Exact ordered pair-difference limit

For continuous compactly supported \(f\), define

\[
\mu_T(f)=\frac1{N(T)}
 \sum_{\substack{x,y\in\Lambda_T\\x\ne y}}
 f\bigl(c(y-x)\bigr).
\]

Equivalently, \(\mu_T=N(T)^{-1}\sum_{x\ne y}\delta_{c(y-x)}\). Define

\[
\boxed{\quad
\mu=\frac1J\sum_{\substack{1\le i,j\le J,\ n\in\mathbb Z\\
                            (i=j)\Longrightarrow n\ne0}}
 \delta_{c(\phi_j-\phi_i+n\Delta)}.\quad}
\]

Repeated atoms are added with multiplicity. Every atom location is nonzero: same-progression terms have \(n\ne0\), and cross-progression terms cannot vanish because phases are distinct modulo \(\Delta\).

**Theorem 1.** \(\mu_T(f)=\mu(f)+O_{f,\{\phi_j\},J}(1/T)\), so \(\mu_T\to\mu\) on continuous compactly supported test functions. The limit is purely atomic. Moreover, for every \(\ell\in\mathbb Z\setminus\{0\}\),

\[
\mu(\{J\ell\})\ge1.
\]

**Proof.** Fix \(i,j,n\), with \(n\ne0\) when \(i=j\), and write

\[
h=\phi_j-\phi_i+n\Delta .
\]

Choose \(x=\phi_i+m\Delta\) and \(y=\phi_j+(m+n)\Delta=x+h\). The conditions \(0<x\le T\), \(0<y\le T\) say precisely that \(x\) lies in an interval of length \(T-|h|\) if \(|h|<T\); there are no pairs if \(|h|\ge T\). Hence the number \(C_{ij,n}(T)\) of choices of \(m\) satisfies

\[
\left|C_{ij,n}(T)-\frac{T-|h|}{\Delta}\right|\le1
\qquad(T>|h|).
\]

Therefore \(C_{ij,n}(T)/N(T)=1/J+O_h(1/T)\). If \(f\) is supported in \([-A,A]\), only triples with \(|h|\le A/c\) contribute, a finite set independent of \(T\). Summing over it proves the convergence statement. The diagonal terms give

\[
\frac1J\sum_{i=1}^J\sum_{n\ne0}\delta_{cn\Delta}
 =\sum_{n\ne0}\delta_{Jn},
\]

which proves the atom bound. \(\square\)

**Check (\(J=1\)).** The formula gives \(\mu=\sum_{n\ne0}\delta_n\), as direct counting in an arithmetic progression confirms. In general, diagonal atoms at \(J\ell\) survive every phase choice and all possible cross-progression coincidences.

### Application to the actual \(b\)-grid

Fix \(t_{\max}\), write \(L=\log2\), \(a_t=\arcsin|s_2(t)|\), \(\phi_t=a_t/L\), and \(\phi_{t,\sigma}=\sigma\phi_t\). Taking \(k=\pm j\) with \(j\ge1\) in the definition of \(b\) gives the exact folded representation

\[
A_t:=\{|b(t,k,\sigma)|:k\ne0,\ \sigma=\pm1\}
=\{j\Delta-\phi_t,\ j\Delta+\phi_t:j\ge1\}.
\]

This is the positive part of the two progressions \(\phi_{t,\sigma}+\Delta\mathbb Z\), apart from finitely many omitted \(k=0\) terms. Each point of \(A_t\) has two raw \((k,\sigma)\) representatives, one with \(b>0\) and one with \(b<0\).

The phases are distinct modulo \(\Delta\). Indeed, \(0<a_t<\pi/2\) is strictly increasing in \(t\), and all differences \(\phi_{t,\sigma}-\phi_{u,\tau}\) lie in \((-\pi/L,\pi/L)=(-\Delta/2,\Delta/2)\). Such a difference is in \(\Delta\mathbb Z\) only if zero, ruled out by strict monotonicity and the signs.

Thus the distinct positive \(|b|\)-grid has \(J=2t_{\max}\), density \(c=2t_{\max}/\Delta=t_{\max}\log2/\pi\), and Theorem 1 applies. For \(t_{\max}=100\),

\[
J=200,\qquad c=22.063560015265157\ldots,
\]

with same-progression atoms at \(u=200,400,600,\ldots\). Counting raw \((k,\sigma)\) modes instead of distinct positive ordinates doubles positive-point multiplicities; after analogous normalization this changes atom weights, not their existence.

## 4. Precise comparison with GUE pair correlation

Let

\[
g(u)=1-\left(\frac{\sin(\pi u)}{\pi u}\right)^2,
\qquad g(0)=0.
\]

This density is absolutely continuous and vanishes at zero. It is the GUE density in equations (9)--(10) of Katz--Sarnak, *Zeroes of zeta functions and symmetry*, Bull. AMS **36** (1999), 1--26, [doi:10.1090/S0273-0979-99-00766-1](https://doi.org/10.1090/S0273-0979-99-00766-1); Katz--Sarnak explicitly describe the unrestricted statement as Montgomery's conjecture. See also Odlyzko, *Math. Comp.* **48** (1987), 273--308, [doi:10.1090/S0025-5718-1987-0866115-0](https://doi.org/10.1090/S0025-5718-1987-0866115-0). These references give provenance for \(g\); the exact hypothesis used below is defined directly, and no numerical evidence is used.

### Constant-density formulation

If a hypothetical constant-density process had GUE pair correlation in Section 3's normalization, its limiting ordered pair measure would be \(g(u)\,du\). That is incompatible with Theorem 1: around \(u=J\ell\), a sufficiently small interval has \(\mu\)-mass at least \(1\), whereas its \(g(u)du\)-mass tends to zero as the interval shrinks. This is a proof about measures, not a histogram-based refutation of a finite fit.

### Zeta-height formulation, including approximate containment

Let \(\Gamma\) be the set of distinct positive ordinates of nontrivial zeta zeros and \(N_\zeta(T)=|\Gamma\cap(0,T]|\). Put

\[
\lambda(T)=\frac1{2\pi}\log\frac{T}{2\pi},
\]

and, for fixed \(f\in C_c(\mathbb R)\),

\[
Z_T(f)=\frac1{N_\zeta(T)}
 \sum_{\substack{\gamma,\gamma'\in\Gamma\cap(0,T]\\
                 \gamma\ne\gamma'}}
 f\bigl(\lambda(T)(\gamma-\gamma')\bigr).
\]

**GUE-PC hypothesis (defined for this note).** For every fixed nonnegative \(f\in C_c\), \(Z_T(f)\to\int f(u)g(u)\,du\).

**Theorem 2 (conditional spectral obstruction).** Fix a grid \(\Lambda\) as in Section 1 and \(0\le\varepsilon<\delta_{\min}/2\). Suppose that, for every sufficiently large \(\gamma\in\Gamma\), one can choose \(x_\gamma\in\Lambda\) with \(|\gamma-x_\gamma|\le\varepsilon\) and with **pairwise distinct representatives** \(x_\gamma\). Then GUE-PC is false for this \(\Gamma\). In particular, exact eventual containment \(\Gamma\cap[T_0,\infty)\subset\Lambda\) is incompatible with GUE-PC: take \(x_\gamma=\gamma\).

**Proof.** For two distinct large ordinates, \(x_\gamma\ne x_{\gamma'}\). The triangle inequality and Lemma 2 therefore give

\[
|\gamma-\gamma'|\ge \delta_{\min}-2\varepsilon=:d>0.
\]

Suppose \(f\) is supported in \([-A,A]\). Once \(\lambda(T)d>A\), no pair of two large ordinates contributes to \(Z_T(f)\). Pairs involving the finitely many initial exceptional ordinates contribute only \(O_f(1)\) to the unnormalized sum: their physical difference intervals shrink with \(T\), and \(\Gamma\) is locally finite. Since \(N_\zeta(T)\to\infty\), \(Z_T(f)\to0\).

Choose a nonnegative, nonzero \(f\in C_c\) supported in \([1,2]\). Then \(\int f(u)g(u)du>0\), because \(g>0\) there. This contradicts the preceding paragraph under GUE-PC. \(\square\)

The argument also applies when zeta zeros form only a subset of grid points; surjectivity is not needed. The distinct-representative condition matters: without it, several ordinates could lie near the same grid point and the displayed lower gap would be unjustified. The theorem therefore makes no fixed-\(\varepsilon\) claim for a non-injective nearest-point matching.

## 5. Limits of the result

* Theorem 2 has an explicitly stated conjectural premise; it is not an unconditional proof of zeta pair correlation. Unconditional non-containment already follows from linear lattice count versus Riemann--von Mangoldt, a separate counting argument not needed above.
* Theorem 1 concerns the grid as a whole. A finite list of selected, perturbed grid points need not exhibit its atoms. In particular, \(\gamma_1,\ldots,\gamma_5\) neither confirm nor refute an asymptotic pair-correlation statement.
* The theorem does not say that *any* modification fails. If \(t_{\max}\), \(\Delta\), or phases change with height \(T\), or \(t\) is continuous, fixed-grid least-gap and finite-union arguments must be revisited. A valid variant analysis must specify those dependences.
* Alternating an overall sign does not change a coherence modulus. A nonvanishing multiplier preserves exact zeros, but a nonconstant positive envelope can move non-zero local minima; invariance of minima requires an extra derivative hypothesis.

The defensible spectral verdict is therefore narrow but sharp: **a fixed finite \(b\)-grid cannot contain the full zeta sequence exactly, or approximate it injectively with error \(\varepsilon<\delta_{\min}/2\), compatibly with GUE-PC; its own constant-density pair statistics are exactly atomic rather than GUE-like. No asymptotic spectral conclusion about five measured minima follows without further finite-sample hypotheses.**
