# Back-extrapolation and the alleged troughs in $]0,10[$

## Scope and source formula

This note concerns only the extrapolation away from the measured interval. It does **not** question the reported agreement at the five zeta ordinates in $[12.63,34.44]$.

The relevant primary source is Wei et al., *Nature Communications* **17**, 8163 (2026), [doi:10.1038/s41467-026-74935-8](https://doi.org/10.1038/s41467-026-74935-8). Equation (10) gives the finite-system coherence, and equation (26) specifies $N=16$ for the experiment:

$$
L_{16}(\beta,t)=\frac{A_\beta(t)}{Z_\beta},\qquad
A_\beta(t)=\sum_{n=1}^{16}(-1)^{n+1}n^{-\beta-it},\qquad
Z_\beta=\sum_{n=1}^{16}n^{-\beta}.
\tag{1}
$$

Figure 4 plots this coherence for $\beta=0.3$ and $\beta=0.5$; open circles are experimental values and solid lines are numerical calculations. The accompanying text says that polynomial fitting was used to extract the reported experimental zero locations. A positive, $t$-independent experimental rescaling would not affect any zero or trough location below.

There are three distinct questions: what the finite samples imply, whether a single-beat recurrence fits them, and what equation (1) itself says below the scan. They have three separate, decisive answers.

## 1. Finite samples do not determine a backward extrapolation

**Proposition (non-identifiability).** Values of a smooth curve at finitely many nodes impose no restriction on its value at another point unless a further model class is imposed.

**Proof with an explicit bounded entire example.** Suppose the 55 scan nodes are uniform:

$$
t_j=a+jh,\qquad a=12.63,\quad h=\frac{34.44-12.63}{54}
=0.403888888888\ldots,\quad 0\le j\le54.
$$

Define

$$
S(t)=\sin\!\bigl(\omega(t-a)\bigr),\qquad
\omega=\frac{\pi}{h}=7.778358702148\ldots .
$$

Then $S(t_j)=0$ for every node and $|S(t)|\le1$ for every real $t$. Nevertheless,

$$
S(7.05)=0.5472337307248309\ldots .
$$

For any candidate real-valued curve $f$ and any $c$, the curve $f_c=f+cS$ has exactly the same 55 sampled values, while $f_c(7.05)-f(7.05)=0.5472337307\ldots c$. The perturbation is entire and bounded on the whole real line. On nonuniform distinct nodes, the normalized polynomial $\prod_j(t-t_j)$ gives the same conclusion without the uniformity assumption. $\square$

Local polynomial fits used to locate minima supply no additional global model. Consequently, Figure 4's data cannot, by themselves, certify either the existence or the nonexistence of a feature near $7.05$. The next sections show that the asserted *single-beat* extrapolation is inconsistent, and that the *published numerical model* actually excludes the alleged troughs.

## 2. The proposed step is incompatible with the trough positions

A two-frequency complex beat $C_1e^{i\omega_1t}+C_2e^{i\omega_2t}$ has squared modulus

$$
C+2\operatorname{Re}\!\left(C_1\overline C_2e^{i(\omega_1-\omega_2)t}\right).
$$

Unless it is constant, all its successive local minima therefore form one arithmetic progression. The following stronger statement also allows skipped minima and a different step at each recurrence.

**Theorem (spacing obstruction).** Let $d_j\in[6.9,7.2]$ be arbitrary, and suppose $\gamma_1$ and $\gamma_3$ are each approximated to within $\varepsilon$ by points linked by $q\ge1$ such steps. Then

$$
\varepsilon\ge1.4619337807945025.
$$

Even using only the quoted rounded values $14.13$ and $25.01$, and allowing their rounding errors, one has $\varepsilon\ge1.455$.

**Proof.** The exact ordinates give

$$
D=\gamma_3-\gamma_1=10.876132438410994973\ldots .
$$

A $q$-step displacement lies in $[6.9q,7.2q]$. For $q=1$ its distance from $D$ is at least $D-7.2=3.6761324384\ldots$; for $q=2$ it is at least $13.8-D=2.9238675615890050\ldots$; and for $q\ge3$ it is at least $6.9q-D\ge9.8238675615\ldots$. Two errors of size at most $\varepsilon$ can change the endpoint difference by at most $2\varepsilon$, proving the first bound.

If all that is assumed is that the true endpoints round to $14.13$ and $25.01$, then $D\in[10.87,10.89]$. The corresponding three lower bounds are $3.67$, $2.91$, and $9.81$, hence $2\varepsilon\ge2.91$. $\square$

The successive gaps between the exact ordinates are computationally

$$
6.8873144970,\quad 3.9888179414,\quad
5.4140185457,\quad 2.5101854619,
$$

so the numerical obstruction is not surprising. No fit quality or choice of phase can repair it within a single-beat model. In particular, tolerance $0.3$ is impossible, even with skipped recurrences.

Finally, subtracting one putative step from $\gamma_1$ gives only

$$
\gamma_1-d\in[6.9347251417,\;7.2347251417].
$$

The value $7.05$ lies inside this range, but that is merely consistency with a one-step subtraction, not an independent test. Moreover, $|7.05-6.5|=|7.05-7.6|=0.55$, so $7.05$ belongs to neither $6.5\pm0.3$ nor $7.6\pm0.3$.

## 3. Equation (1) excludes every trough in $[6.2,7.9]$

The two alleged neighborhoods are $[6.2,6.8]$ and $[7.3,7.9]$. A directed-interval computation proves a stronger statement covering both.

**Computer-assisted theorem.** For $N=16$ and each $\beta\in\{0.3,0.5\}$, $R_\beta(t)=|L_{16}(\beta,t)|^2$ is strictly decreasing throughout $[6.2,7.9]$. In particular, $|L_{16}|$ has no zero and no local minimum anywhere in either alleged neighborhood. The cellwise-certified bounds are

| $\beta$ | lower bound for $|L_{16}|$ on $[6.2,7.9]$ | upper bound for $R_\beta'$ on $[6.2,7.9]$ |
|---|---:|---:|
| $0.3$ | $0.1758575707$ | $-0.0017668456$ |
| $0.5$ | $0.2041752527$ | $-0.0169907630$ |

**Verification.** Partition $[6.2,7.9]$ into the 1700 rational cells $[(6200+j)/1000,(6201+j)/1000]$, $0\le j<1700$. On each cell, evaluate interval enclosures of

$$
\operatorname{Re}A=\sum s_nw_n\cos(t\log n),\quad
\operatorname{Im}A=-\sum s_nw_n\sin(t\log n),
$$

and of $\operatorname{Re}A'=-\sum s_nw_n\log n\sin(t\log n)$ and $\operatorname{Im}A'=-\sum s_nw_n\log n\cos(t\log n)$, where $s_n=(-1)^{n+1}$ and $w_n=n^{-\beta}$. The identities

$$
|L_{16}|=\frac{\sqrt{(\operatorname{Re}A)^2+(\operatorname{Im}A)^2}}{Z_\beta},
\qquad R_\beta'=\frac{2(\operatorname{Re}A'\operatorname{Re}A+\operatorname{Im}A'\operatorname{Im}A)}{Z_\beta^2}
$$

turn those enclosures, using directed rounding, directly into lower modulus bounds and upper derivative bounds. The smallest cellwise modulus bounds and largest cellwise derivative bounds are those in the table. The program is `verify_extrapolation.py`; its complete output is `verification.txt`. It uses only formula (1), not any unpublished or digitized data.

As an independent numerical display, high-precision evaluation at $\beta=0.5$ gives

$$
|L_{16}(0.5,6.5)|\simeq0.2744084039357836,
$$

$$
|L_{16}(0.5,7.05)|\simeq0.2443787494151568,\qquad
|L_{16}(0.5,7.6)|\simeq0.2220123147723519.
$$

These values are diagnostics; the exclusion of troughs follows from the interval certificate, not from sampling these three points.

For the thermodynamic *exact-zero* interpretation there is an even shorter conclusion. The zeta factor in equation (10) has its first positive ordinate at $\gamma_1=14.134725\ldots$. At $\beta=0.5$, the other factor $1-2^{1-\beta-it}$ cannot vanish, because $|2^{1-\beta-it}|=2^{1-\beta}=\sqrt2\ne1$. Hence there is no thermodynamic zeta-induced coherence zero in $]0,10[$ either.

## Verdict

* **As a data-only prediction,** the back-extrapolation is not identifiable; the experiments below $t=12.63$ simply supply no observations.
* **As a single-beat recurrence with step $6.9$–$7.2$,** it is mathematically refuted by $\gamma_1$ and $\gamma_3$ alone, even allowing skipped beats and generous rounding.
* **As a statement about the published 16-level numerical curves,** it is false: those curves are strictly decreasing and bounded away from zero throughout both alleged windows.
* **As a statement about exact thermodynamic zeta zeros,** it is false because $\gamma_1$ is already the first positive ordinate.

Accordingly, no formulation $F$ based on “extending Figure 4 backward by a $6.9$–$7.2$ recurrence” is simultaneously well posed, nonvacuous, and consistent with the published model. A different low-time model could always be proposed, but it would require new equations and new low-time evidence; it cannot be inferred from this recurrence or from the lattice.
