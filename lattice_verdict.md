# The finite-frequency obstruction is band exclusion, not insufficient density

## 1. Exact form of the modulus lattice

Put
\[
 \Delta=\frac{2\pi}{\log 2}=9.064720283654387619\ldots,\qquad
 a_t=\frac{\arcsin |s_2(t)|}{\log 2}.
\]
For a set \(\mathcal T\subseteq\mathbb N\), let
\[
 \Lambda_{\mathcal T}=\{|b(t,k,\sigma)|:t\in\mathcal T,\ k\in\mathbb Z\setminus\{0\},\ \sigma\in\{-1,1\}\}.
\]
This is the set to which a positive target frequency must be compared. Taking absolute values causes no loss of generality.

**Lemma 1 (two points per centre and per \(t\)).** Since \(0<a_t<\Delta\),
\[
 \boxed{\ \Lambda_{\mathcal T}=\{j\Delta+a_t,\ j\Delta-a_t:
                 j\in\mathbb N,\ t\in\mathcal T\}.\ }
\]
Thus increasing \(|\mathcal T|\) adds points inside the same phase bands; it cannot move or eliminate the bands.

*Proof.* For \(j\ge1\), the four values obtained from \(k=\pm j\) and \(\sigma=\pm1\) are
\[
 a_t-j\Delta<0,\qquad -a_t-j\Delta<0,\qquad
 a_t+j\Delta>0,\qquad -a_t+j\Delta>0.
\]
Taking absolute values of the first two gives exactly the last two. Conversely, the last two are the stated pair at centre \(j\Delta\). \(\square\)

The stipulated strict increase of \(|s_2(t)|\) to \(1\) gives
\[
 a_1\le a_t<a_\infty:=\frac{\pi}{2\log 2},\qquad
 a_1=1.77596071757908058\ldots>\frac{\pi}{3\log 2}.
\]
Consequently, the band restriction in fact (c), although stated there only for \(t\le589\), in fact applies to **every** positive integer \(t\). Define the slightly over-generous phase limits
\[
 a_-=\frac{\pi}{3\log2}=1.51078671394239794\ldots,\qquad
 a_+=a_\infty=2.26618007091359690\ldots,
\]
and the closed band union
\[
 \mathcal B=\bigcup_{j\ge1}
 \left([j\Delta-a_+,j\Delta-a_-]\cup[j\Delta+a_-,j\Delta+a_+]\right).
\]
Then \(\Lambda_{\mathbb N}\subseteq\mathcal B\). The wider set \(\mathcal B\) is used below only to make the obstruction as favourable as possible to a proposed coincidence.

## 2. An exact finite-set hitting criterion

For \(x\ge0\) and \(\varepsilon\ge0\), define
\[
 d_{\mathcal T}(x)=\inf_{\lambda\in\Lambda_{\mathcal T}}|x-\lambda|,
 \qquad
 d_{\mathcal T}(X)=\sup_{x\in X}d_{\mathcal T}(x)
\]
for a finite target set \(X\). Lemma 1 gives the directly computable formula
\[
 d_{\mathcal T}(x)=\inf_{t\in\mathcal T,\ \eta\in\{-1,1\}}\
 \min_{j\ge1}|x-j\Delta-\eta a_t|;
\]
only one or two centres \(j\Delta\) nearest to \(x\), together with the first centre if necessary, need to be checked. Hence the outer infimum is also a minimum when \(\mathcal T\) is finite.

More explicitly, define a union of phase intervals
\[
 P_{x,\varepsilon}=\bigcup_{j\ge1}
 \left([x-j\Delta-\varepsilon,x-j\Delta+\varepsilon]
 \cup[j\Delta-x-\varepsilon,j\Delta-x+\varepsilon]\right).
\]
The following elementary criterion is exact, not a heuristic.

**Lemma 2 (hitting and common-phase criteria).**

1. Some point of \(\Lambda_{\mathcal T}\) is within \(\varepsilon\) of \(x\) if and only if \(a_t\in P_{x,\varepsilon}\) for some \(t\in\mathcal T\).
2. A **single** \(t\) supplies points within \(\varepsilon\) of every \(x\in X\) if and only if
   \[
   a_t\in\bigcap_{x\in X}P_{x,\varepsilon}
   \quad\text{for some }t\in\mathcal T.
   \]
3. If \(\mathcal T\) is finite and different targets may use different \(t\), they are all within \(\varepsilon\) of the lattice if and only if \(\varepsilon\ge d_{\mathcal T}(X)\). For infinite \(\mathcal T\), the implication “within” \(\Rightarrow\varepsilon\ge d_{\mathcal T}(X)\) still holds; at equality one must additionally check attainment of the infimum.
4. If one instead allows the phase to range continuously over an interval \(I\), replace the condition \(a_t\in P_{x,\varepsilon}\) by \(I\cap P_{x,\varepsilon}\ne\varnothing\).

*Proof.* For the branch \(j\Delta+a_t\), the inequality \(|x-j\Delta-a_t|\le\varepsilon\) is equivalent to \(a_t\in[x-j\Delta-\varepsilon,x-j\Delta+\varepsilon]\). For the branch \(j\Delta-a_t\), it is equivalent to \(a_t\in[j\Delta-x-\varepsilon,j\Delta-x+\varepsilon]\). Taking a union proves (1), and intersecting these conditions proves (2). For finite \(\mathcal T\), every \(d_{\mathcal T}(x)\) is attained and the finite target maximum is attained, proving (3). Part (4) is the same inequality with a continuously variable phase. \(\square\)

This settles the existence question for any explicitly listed \(t\)-set and tolerance: sort the finitely many relevant phases and test interval membership. No probabilistic or density argument is needed.

## 3. Four of the five zeta ordinates are outside every band

The following calculation uses only the closed band union \(\mathcal B\), and therefore also covers every finite or infinite set of integer \(t\)-values.

| target | closest band | distance to closed band; positive values are lattice lower bounds |
|---|---:|---:|
| \(\gamma_1=14.13472514173469\ldots\) | lower \(j=2\), starting at \(2\Delta-a_+=15.86326049639518\ldots\) | \(1.72853535466048\ldots\) |
| \(\gamma_2=21.02203963877155\ldots\) | upper \(j=2\), ending at \(2\Delta+a_+=20.39562063822237\ldots\) | \(0.626419000549183\ldots\) |
| \(\gamma_3=25.01085758014569\ldots\) | inside lower \(j=3\) band | \(0\) (no band exclusion) |
| \(\gamma_4=30.42487612585951\ldots\) | upper \(j=3\), ending at \(3\Delta+a_+=29.46034092187676\ldots\) | \(0.964535203982753\ldots\) |
| \(\gamma_5=32.93506158773919\ldots\) | lower \(j=4\), starting at \(4\Delta-a_+=33.99270106370395\ldots\) | \(1.05763947596476\ldots\) |

For example, the first and last entries are respectively
\[
 2\Delta-a_+-\gamma_1,
 \qquad 4\Delta-a_+-\gamma_5.
\]
The other three positive band distances have analogous explicit formulas. Checking the adjacent band endpoints in the table proves that there is no closer band; all gaps are many orders of magnitude larger than the rounding error in the listed ordinates. The script `lattice_bands.py` reproduces every entry at 80-digit working precision. Using only the ordinates rounded to the digits supplied in the question does not change any displayed bound.

**Theorem 1 (sharp band-exclusion verdict).** Let each target be allowed its own \(t\in\mathbb N\), its own sign and its own nonzero \(k\). Then:

* if \(\varepsilon<0.626419000549182\), **at most one** of \(\gamma_1,\ldots,\gamma_5\), namely \(\gamma_3\), can be within \(\varepsilon\) of the modulus lattice;
* in particular, at tolerance \(0.3\) the other four are impossible;
* no choice of \(t_{\max}\), including \(t_{\max}\to\infty\), can make all five agree at tolerance smaller than \(1.728535354660484\);
* a joint lattice explanation of the five ordinates is therefore false for the original construction, independently of point density or of how many \(t\)-values are retained.

The first threshold is sharp for the closed band envelope: its value is exactly \(\gamma_2-(2\Delta+a_+)\), and points \(2\Delta+a_t\) approach that endpoint as \(t\to\infty\). It is not an artefact of truncating \(t\).

### The one possible match

For \(\gamma_3\), the only relevant branch is \(3\Delta-a_t\). An exact match would require
\[
 c:=3\Delta-\gamma_3=2.18330327081747409\ldots=a_t.
\]
Interval evaluation of the equation stated in the question gives
\[
 a_{35}=2.18248778697307106\ldots<c<
 a_{36}=2.18365772170871036\ldots .
\]
Thus no integer \(t\) gives an exact match. Strict monotonicity also proves that only \(t=35\) and \(t=36\) need to be compared for the best approximation over **all** positive integers. The latter gives
\[
 b(36,-3,-1)=3\Delta-a_{36}=25.01050312925445249\ldots,
\]
and hence
\[
 \boxed{\ |b(36,-3,-1)-\gamma_3|
       =0.00035445089123626978\ldots.\ }
\]
At \(t=35\), the error is \(0.00081548384440303616\ldots\); every other integer \(t\) is farther away. So there is one excellent isolated lattice approximation, but it does not extend to a five-target relation.

### Exact finite computation for \(t\le100\)

Minimising the formula in Lemma 1 over \(1\le t\le100\) gives the stronger finite-set distances below. The positive representative \(j\Delta+\eta a_t\) is unique in each case; the displayed \((t,k,\sigma)\) is one of its two preimages under \(|b|\), related by the sign symmetry in Lemma 1.

| target | nearest \((t,k,\sigma)\) | \(d_{\{1,\ldots,100\}}(\gamma_n)\) |
|---|---:|---:|
| \(\gamma_1\) | \((100,-2,-1)\) | \(1.77805742009213578\) |
| \(\gamma_2\) | \((100,-2,+1)\) | \(0.67594106598083408\) |
| \(\gamma_3\) | \((36,-3,-1)\) | \(0.00035445089123627\) |
| \(\gamma_4\) | \((100,-3,+1)\) | \(1.01405726941440468\) |
| \(\gamma_5\) | \((100,-4,-1)\) | \(1.10716154139641511\) |

For the four targets outside the bands, monotonicity identifies the nearest endpoint and shows that it comes from \(t=100\); for \(\gamma_3\), use the bracket above. It follows exactly that
\[
 d_{\{1,\ldots,100\}}(\{\gamma_1,\ldots,\gamma_5\})
 =1.77805742009213578\ldots .
\]
The file `interval_checks.txt` records directed-rounding enclosures for the phase bracket and the four finite-\(t\) gaps. These computations are numerical evaluations of the stated algebraic equation, not fits to experimental data.

## 4. Exact near-coincidence probabilities under a specified null model

The zeta ordinates are fixed numbers, so there is no natural frequentist probability that a particular \(\gamma_n\) equals a lattice point. A probability can nevertheless be assigned to an explicitly defined random-target null. The following version avoids inventing a random model for the phases \(a_t\), which are deterministic.

Fix, **before looking at target locations**, a finite \(\mathcal T\), a tolerance \(\varepsilon\), and a bounded measurement window \(W\) of positive length. Let
\[
 C_{\mathcal T,\varepsilon}
 =\{x\in W:d_{\mathcal T}(x)\le\varepsilon\},
 \qquad
 p_{\mathcal T,\varepsilon,W}
 =\frac{\lambda(C_{\mathcal T,\varepsilon})}{\lambda(W)},
\]
where \(\lambda\) is Lebesgue measure. By Lemma 1, \(C_{\mathcal T,\varepsilon}\) is the intersection with \(W\) of a finite union of intervals \([\lambda-\varepsilon,\lambda+\varepsilon]\), with overlaps merged and with the window boundaries applied. Its measure is therefore exactly computable; multiplicities and overlapping lattice points must not be counted twice.

**Lemma 3 (null distribution).** If \(X_1,\ldots,X_m\) are independent uniform random variables on \(W\), then their hit indicators are independent Bernoulli variables with mean \(p=p_{\mathcal T,\varepsilon,W}\). Consequently,
\[
 \Pr(\text{all }m\text{ hit})=p^m,\qquad
 \Pr(\text{exactly }r\text{ hit})=\binom mr p^r(1-p)^{m-r},
\]
and \(\Pr(\text{at least one hit})=1-(1-p)^m\).

More generally, if \(X_i\) is uniform on its own fixed window \(W_i\), put
\[
 p_i=\frac{\lambda(\{x\in W_i:d_{\mathcal T}(x)\le\varepsilon\})}{\lambda(W_i)}.
\]
The hit count is Poisson-binomial: with \(Q_0^{(0)}=1\) and \(Q_r^{(0)}=0\) for \(r>0\),
\[
 Q_r^{(i)}=(1-p_i)Q_r^{(i-1)}+p_iQ_{r-1}^{(i-1)}.
\]
The probability that all hit is \(\prod_i p_i\), and the probability of at least one is \(1-\prod_i(1-p_i)\).

*Proof.* For a common window \(W\), a hit is precisely the event \(X_i\in C_{\mathcal T,\varepsilon}\); for individual windows, use their respective hit regions displayed above. The uniform law gives its probability as the stated length ratio, and independence of the target variables gives independence of the indicators. The recurrence conditions on whether target \(i\) hits. \(\square\)

As an illustration, take \(W=[12.63,34.44]\) and \(\mathcal T=\{1,\ldots,100\}\). Exact union-of-intervals evaluation gives:

| \(\varepsilon\) | \(p_{\mathcal T,\varepsilon,W}\) | probability all five random targets hit | probability at least one hits |
|---:|---:|---:|---:|
| \(0.0001\) | \(0.00457588262265\) | \(2.0062\times10^{-12}\) | \(0.02267098\) |
| \(0.00035445089123627\) | \(0.01279439147891\) | \(3.4285\times10^{-10}\) | \(0.06235580\) |
| \(0.001\) | \(0.02271729525994\) | \(6.0504\times10^{-9}\) | \(0.10854163\) |
| \(0.0022\) | \(0.03287300359560\) | \(3.8388\times10^{-8}\) | \(0.15390811\) |
| \(0.01\) | \(0.06133230723678\) | \(8.6785\times10^{-7}\) | \(0.27128224\) |
| \(0.1\) | \(0.14032856590903\) | \(0.00005441648\) | \(0.53047094\) |

These are **null calibration numbers only**, not \(p\)-values for the fixed zeta targets. For the actual five targets the deterministic theorem already gives four failures and one close hit. The second row uses the actual \(\gamma_3\) approximation tolerance: under this random-target null, at least one comparably close hit among five has probability \(0.0623558\), so the isolated close point is not by itself strong anti-null evidence. The exact union calculation is important at larger tolerances because the increasing phases cluster near \(a_+\), so multiplying a nominal point count by \(2\varepsilon\) would overcount covered length.

For perspective, if instead all phases were allowed to fill the whole interval \([a_-,a_+]\) and the target law were uniform modulo \(\Delta\), then for \(0\le\varepsilon<a_-\) (before the first neighbouring bands merge),
\[
 p_{\rm band}(\varepsilon)
 =\frac{2(a_+-a_-)+4\varepsilon}{\Delta}
 =\frac16+\frac{4\varepsilon}{\Delta},
\]
because \(a_+-a_-=\Delta/12\). This follows by measuring two expanded bands in one period. It is an upper-envelope calculation, not the finite-\(t\) probability computed above.

Keep the target windows and laws fixed, and suppose one searches a prespecified collection of \(q\) settings \(\alpha=(\mathcal T_\alpha,\varepsilon_\alpha)\), declaring success when any setting has all \(m\) targets hit. The same null gives the distribution-free selection bound
\[
 \Pr(\text{any success})\le\sum_{\alpha=1}^q p_\alpha^{\,m},
\]
where \(p_\alpha\) is the corresponding hit fraction in the fixed target window. No independence between settings is required. For a different success event, replace \(p_\alpha^m\) by its exact binomial or Poisson-binomial probability. A tolerance, window, or \(t\)-range chosen after inspecting the answers is not calibrated by the unadjusted single-setting probabilities; scanning windows additionally requires one joint law for the targets across all scanned windows.

## 5. Precise formulations and verdict

A mathematically legitimate formulation is:
\[
 F(\mathcal T,X,\varepsilon):\qquad
 \forall x\in X\ \exists\lambda\in\Lambda_{\mathcal T}
 \quad |x-\lambda|\le\varepsilon .
\]
It is nonvacuous, has the exact phase criterion of Lemma 2, and is decided by a finite interval calculation for every finite \(\mathcal T\). For \(X=\{\gamma_1,\ldots,\gamma_5\}\), it is false whenever \(\varepsilon<1.728535354660484\), even with \(\mathcal T=\mathbb N\); the finite-\(t\) threshold can be larger and is \(1.778057420092136\) for \(\mathcal T=\{1,\ldots,100\}\). If one additionally requires a common \(t\), the intersection criterion in Lemma 2 applies.

There is also a true, explicit, very narrow statement:
\[
 F(\mathbb N,\{\gamma_3\},0.000355)
\]
holds, witnessed by \(b(36,-3,-1)\). But the sharp correct general relation of this lattice to the five zeta ordinates is only **band-limited, pointwise approximation**. It cannot be a joint explanation of the five frequencies: four fail before density, mesh size, or experimental resolution enters the discussion. This conclusion concerns only the claimed lattice correspondence; it makes no assertion against the published coherence measurements or their minima.

## Reproduction

From this directory:

```bash
python3 lattice_bands.py --all-distances --tmax 100
python3 lattice_bands.py --null-coverage --tmax 100
python3 verify_intervals.py
```

`lattice_bands.py` uses high-precision bisection on
\[
 u^2-24t^2(1-u)^2(1+3u^2-u^3)=0,\qquad 0<u<1,
\]
then evaluates \(a_t=\arcsin(\sqrt u)/\log2\). It also computes the exact null coverage lengths by sorting and merging intervals. `verify_intervals.py` brackets roots using strict interval signs of the polynomial and uses directed-rounding interval arithmetic for the transcendental evaluations. No unpublished or experimental data file is used.
