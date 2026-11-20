# What variants of the frequency lattice can and cannot fit

## 1. A universal obstruction to changing only the characteristic equation

Put
\[
  L=\log 2,\qquad \Delta=\frac{2\pi}{L}=9.064720283654388\ldots .
\]
Consider every variant which retains
\[
 b=\frac{\theta-2\pi k}{L},\qquad k\in\mathbb Z\setminus\{0\},
 \qquad \theta=\arcsin(\sigma q),\quad \sigma\in\{\pm1\},\quad 0\le q\le1,
\]
but allows $q=|s_2(t)|$ to depend on $t$ in an arbitrary way. Thus this includes every change of the characteristic equation which leaves the displayed arcsine phase map and the step $\Delta$ unchanged. Let $\mathcal B_+$ be the set of all positive numbers of this form, over all $q,\sigma,k$ (and hence over every $t$ and every $t_{\max}$).

**Theorem 1 (universal bands).**
\[
 \mathcal B_+\subseteq
 \bigcup_{j=1}^{\infty}[(j-\tfrac14)\Delta,(j+\tfrac14)\Delta].
\]
If all phases $[-\pi/2,\pi/2]$ are available, equality holds. In particular,
each gap
\[
 G_j=((j+\tfrac14)\Delta,(j+\tfrac34)\Delta),\qquad j\ge1,
\]
has length $\Delta/2=4.532360141827194\ldots$ and contains no lattice point of any such variant.

**Proof.** Since $\theta\in[-\pi/2,\pi/2]$, $k\ge1$ gives $b<0$. Hence a positive $b$ has $k=-j$ with $j\ge1$, and
\[
 b=j\Delta+\frac{\theta}{L},\qquad
 \left|\frac{\theta}{L}\right|\le \frac{\pi}{2L}=\frac{\Delta}{4}.
\]
Conversely, every point of a band is obtained by taking $\theta=L(b-j\Delta)$ and an appropriate sign $\sigma$. $\square$

This argument does not use the size or density of the set of $t$'s. Taking more roots, taking $t_{\max}$ arbitrarily large, or changing the equation defining $s_2(t)$ can only remove points from these bands; it cannot fill a gap.

### Numerical consequence for the first five zeta ordinates

Using the ordinates rounded as in the question, the universal bands and distances are as follows. Here $d_+$ is distance to the whole union in Theorem 1, not merely to its actually attained discrete subset.

| $n$ | $\gamma_n$ | location | $d_+(\gamma_n)$ |
|---:|---:|---|---:|
| 1 | 14.1347 | $G_1=(11.330900354568,15.863260496395)$ | 1.728560496 |
| 2 | 21.0220 | $G_2=(20.395620638222,24.927980780050)$ | 0.626379362 |
| 3 | 25.0109 | band $j=3$ | 0 |
| 4 | 30.4249 | $G_3=(29.460340921877,33.992701063704)$ | 0.964559078 |
| 5 | 32.9351 | $G_3$ | 1.057601064 |

The accompanying `analysis.py` computes these entries from $L=\log2$, $\Delta=2\pi/L$, and the five displayed ordinates. Adding precision to the ordinates does not affect any inequality. Four ordinates therefore lie in gaps for **every** variant covered by Theorem 1, and their distances from every possible positive lattice point exceed $0.626$. This is more than $284$ times the stated $0.0022$ net spacing. For $\gamma_3$ the band condition is necessary, not an assertion that an integer $t$ attains it.

For the original construction with $1\le t\le589$, fact (c) gives still narrower bands. The same four ordinates are excluded; no use of the stronger restriction $\pi/3\le|\theta|\le\pi/2$ was needed above.

## 2. An exact fit is possible only by changing the phase law (or adding equivalent freedom)

The obstruction is not a theorem that no modification whatsoever can interpolate five numbers. The following explicit construction shows the opposite and also shows why such an interpolation is not evidence for a relation with zeta.

Let $\gamma_1,\ldots,\gamma_5$ be any five positive targets in the ranges above. Define
\[
 j_n=\operatorname{round}(\gamma_n/\Delta),\qquad
 \vartheta_n=L\gamma_n-2\pi j_n .
\]
Nearest-integer rounding gives $|\vartheta_n|\le\pi$. For these targets,
\[
 (j_1,\ldots,j_5)=(2,2,3,3,4),
\]
and, at the displayed precision,
\[
 (\vartheta_1,\ldots,\vartheta_5)
 =(-2.768943161,\ 2.004969415,\ -1.513321103,\
   2.239377732,\ -2.303869522).
\]
Now replace the arcsine phase by any map $\widetilde\theta(t,\sigma)$ satisfying $\widetilde\theta(n,+1)=\vartheta_n$ for $1\le n\le5$, and define
\[
 \widetilde b(t,k,\sigma)
 =\frac{\widetilde\theta(t,\sigma)-2\pi k}{L}.
\]
Then exactly, with no tolerance,
\[
 \widetilde b(n,-j_n,+1)=\gamma_n\qquad(1\le n\le5).
\]
For example, one may take $\widetilde\theta(t,+1)$ to be the interpolating polynomial through $(n,\vartheta_n)$ and define $\widetilde\theta(t,-1)$ arbitrarily. The construction works verbatim for any finite target list: one independently chosen phase per target gives an exact fit.

If it is desired to retain an arcsine superficially, use instead
\[
 \widetilde b(t,k,\sigma)
 =\frac{2\arcsin(\sigma q_t)-2\pi k}{L},
\]
and choose
\[
 q_n=|\sin(\vartheta_n/2)|,\qquad
 \sigma_n=\operatorname{sgn}\vartheta_n .
\]
Because $|\vartheta_n|\le\pi$, $2\arcsin(\sigma_nq_n)=\vartheta_n$, and hence $\widetilde b(n,-j_n,\sigma_n)=\gamma_n$. The required $q_n$ are, respectively,
\[
 0.982691705737,\ 0.842810879195,\ 0.686497055786,\
 0.899964843051,\ 0.913552557015 .
\]
For instance, the equation $s+q_n=0$ has root $s_2(n)=-q_n$; any less trivial characteristic equations with the same roots would do as well. `analysis.py` verifies all five reconstructions numerically.

**Interpretation.** This proves logical possibility, not explanatory content. Five continuously selectable phases have been used to encode five ordinates, after also selecting $j_n$ and $\sigma_n$. The fit has no residual degree of freedom and makes no prediction about a sixth ordinate. A non-vacuous hypothesis must freeze the characteristic equation and phase map independently of the targets, specify the tolerance and comparison rule in advance, and then be tested on targets not used to select the variant. Under that requirement, Theorem 1 rules out every variant which changes only the characteristic equation.

## 3. Envelopes and alternating coefficients do not evade the support obstruction

The following elementary lemmas delimit two other proposed modifications.

**Lemma 2 (nonvanishing envelope).** Let $A,E$ be real- or complex-valued functions on an interval $I$, and put $H=EA$. If $E(x)\ne0$ for every $x\in I$, then
\[
 \{x\in I:H(x)=0\}=\{x\in I:A(x)=0\}.
\]
The same equality holds with $H,A$ replaced by their absolute values. If zeros of $H$ are allowed anywhere, then in general $Z(H)=Z(A)\cup Z(E)$: any additional zeros belong to the envelope.

**Proof.** A product vanishes exactly when at least one factor vanishes; nonvanishing $E$ removes the second alternative. $\square$

Thus multiplying by a smooth, nonzero, slowly varying envelope cannot move a true zero or create a new one. It can move a nonzero local minimum of a noisy curve, but that is a different claim from locating a zero and must not be substituted for it.

**Lemma 3 (alternating weights).** For arbitrary scalar weights $w_{t,k,\sigma}$, the support of
\[
 \sum_{t,k,\sigma}w_{t,k,\sigma}\,\delta_{b(t,k,\sigma)}
\]
is a subset of the unweighted lattice. It is exactly the set of locations whose total coefficient (after combining repeated locations) is nonzero. Thus changing weights, including alternating their signs, changes amplitudes and may delete a location by cancellation, but never moves a location to a new $b$. Zeros of an associated Fourier sum $\sum w_{t,k,\sigma}e^{ixb(t,k,\sigma)}$ are zeros in the new variable $x$; they are not points of the $b$-lattice. Calling such zeros a coincidence with lattice points would conflate the two variables.

## 4. Sharp verdict for the listed variants

* **Different characteristic equation, same arcsine phase and $\Delta$:** cannot reproduce $\gamma_1,\gamma_2,\gamma_4,\gamma_5$ at all, by Theorem 1.
* **Other $t_{\max}$, alternating coefficients, or a nonvanishing envelope:** cannot fill the gaps or move the corresponding supported frequencies/true zeros, by Theorem 1 and Lemmas 2--3.
* **Genuinely different phase law:** can reproduce all five exactly, as Section 2 demonstrates. A phase law fitted in this way is a reparametrization of the targets, not an explanation. The meaningful question for any proposed variant is therefore whether its phase law was fixed independently and successfully predicts held-out frequencies at a predeclared tolerance.

Nothing here concerns the experimental coherence on $t\in[12.63,34.44]$. The conclusions are solely about coincidence with the mathematical $b$-lattice and about modifications of that lattice.
