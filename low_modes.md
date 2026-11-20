# Sharp global support of the lowest lattice modes

## 1. Result

Let
$$
L=\log 2,\qquad r_t=|s_2(t)|,\qquad u_t=r_t^2,\qquad
\alpha_t=\arcsin r_t .
$$
We consider the set of positive moduli
$$
\mathcal B=\left\{|b(t,k,\sigma)|:t\in\mathbb Z_{\ge1},\
\sigma\in\{-1,1\},\ k\in\mathbb Z\setminus\{0\}\right\},
$$
and write $\mathcal B_M$ for the subset with $1\le t\le M$.
The established strict increase $r_t\uparrow1$ gives
$\alpha_t\uparrow\pi/2$, strictly in $t$.

The main conclusion is the following.

**Theorem (exact branch ranges and low-window obstruction).**
For every integer $j\ge1$ and $t\ge1$, define
$$
A_{j,t}=\frac{2\pi j-\alpha_t}{L},\qquad
C_{j,t}=\frac{2\pi j+\alpha_t}{L}.
$$
Then
$$
\mathcal B=\{A_{j,t},C_{j,t}:j,t\ge1\},
$$
and the full signed lattice is $\{\pm A_{j,t},\pm C_{j,t}\}$.
For fixed $j$, $A_{j,t}$ strictly decreases and $C_{j,t}$ strictly
increases with $t$. Their exact endpoints are
$$
A_{j,t}\in\left(\frac{2\pi j-\pi/2}{L},
                  \frac{2\pi j-\alpha_1}{L}\right],\qquad
C_{j,t}\in\left[\frac{2\pi j+\alpha_1}{L},
                  \frac{2\pi j+\pi/2}{L}\right).
$$
The lower endpoint of the $A$-range and upper endpoint of the $C$-range
are a limit infimum/supremum, not values attained at finite $t$.
Interval-certified numerical values (Section 5) are
$$
\begin{aligned}
\alpha_1&=1.231002164175157007\ldots,\\
a_1:=\frac{3\pi}{2L}&=6.798540212740790714\ldots,\\
A_{1,1}&=7.288759566075307035\ldots,\\
C_{1,1}&=10.840681001233468202\ldots,\\
a_2:=\frac{7\pi}{2L}&=15.863260496395178333\ldots .
\end{aligned}
$$
Consequently:

1. **The $7.6\pm0.3$ window is completely impossible, for every $t$.**
   $$
   \mathcal B\cap[7.3,7.9]=\varnothing .
   $$
   The closest lattice modulus to $7.6$ is $A_{1,1}$, with
   $$
   \operatorname{dist}(7.6,\mathcal B)
      =7.6-A_{1,1}
      =0.311240433924692964\ldots>0.3.
   $$
   More strongly, the distance from the whole window to the lattice is
   $$
   \operatorname{dist}([7.3,7.9],\mathcal B)
      =7.3-A_{1,1}
      =0.011240433924692964\ldots .
   $$

2. **The exact ordinate $6.5$ is also impossible, but the status of its
   $\pm0.3$ window depends on the $t$-cutoff.** One has
   $$
   \mathcal B\cap[6.2,6.8]
      =\{A_{1,t}:t\ge115108\}.
   $$
   Thus $\mathcal B_M\cap[6.2,6.8]$ is empty precisely when
   $M\le115107$; for $M\ge115108$ it is
   $\{A_{1,t}:115108\le t\le M\}$. In particular it contains no
   lattice point for $t\le100$ or $t\le589$. On the other hand, any
   assertion that it is empty for *all* $t\ge1$ would be false.

3. The sharpest distance statement for the central ordinate $6.5$ is
   $$
   \operatorname{dist}(6.5,\mathcal B)
      =a_1-6.5=0.298540212740790714\ldots .
   $$
   This is an infimum, not an attained distance. For finite $M$,
   $$
   \operatorname{dist}(6.5,\mathcal B_M)=A_{1,M}-6.5.
   $$
   For example,
   $$
   A_{1,100}-6.5=0.348062278172441946\ldots,\qquad
   A_{1,589}-6.5=0.318947088747134267\ldots .
   $$
   Both exceed $0.3$. More generally,
   $$
   \operatorname{dist}([6.2,6.8],\mathcal B_M)
      =\max(A_{1,M}-6.8,0).
   $$
   In particular this distance is
   $A_{1,589}-6.8=0.018947088747134267\ldots$ for $M=589$.

In particular, the exact values $6.5$ and $7.6$ are unattainable, but
that assertion alone is not the sharpest correct tolerance statement.
The whole $7.6\pm0.3$ window is excluded independently of $t_{max}$;
the $6.5\pm0.3$ window is excluded only below the explicit cutoff above.

## 2. Complete classification of the branches

Put $j=|k|$. Since $0<\alpha_t<\pi/2<2\pi j$, direct evaluation of the
four sign possibilities gives
$$
\begin{array}{c|c|c}
 & \sigma=+1&\sigma=-1\\ \hline
k=j & -A_{j,t}&-C_{j,t}\\
k=-j& C_{j,t}& A_{j,t}
\end{array}
$$
for the *signed* value of $b(t,k,\sigma)$. This proves the displayed
classification. Each magnitude therefore occurs for two ordered pairs
$(k,\sigma)$ at fixed $j,t$.

The monotonicity and endpoint formulas follow immediately from
$\alpha_t\uparrow\pi/2$. For modes below $12$, only $j=1$ can occur.
Indeed, for $j\ge2$,
$A_{j,t}>a_j\ge a_2>12$ and
$C_{j,t}>2\pi j/L\ge4\pi/L>12$. For $j=1$,
$C_{1,t}<5\pi/(2L)=11.330900354567984524\ldots$. Hence
$$
\mathcal B\cap(0,12)=\{A_{1,t}:t\ge1\}\cup\{C_{1,t}:t\ge1\}.
$$
These are two discrete sequences, not two filled intervals. In
particular,
$$
\mathcal B\cap(0,a_1]=\varnothing,\qquad
\mathcal B\cap(A_{1,1},C_{1,1})=\varnothing .
$$
This sharpens the coarse bands obtained by replacing $\alpha_1$ by
$\pi/3$.

## 3. Exact inversion in the $t$-parameter

For $0<u<1$, put $q(u)=1+3u^2-u^3$. The equivalent characteristic
equation gives the positive relation
$$
t=\tau(u):=\frac{u}{\sqrt{24}\,(1-u)\sqrt{q(u)}}.
$$
Here $q\ge1$, $q'(u)=3u(2-u)\le3$, and
$$
\frac{\tau'(u)}{\tau(u)}
 =\frac1u+\frac1{1-u}-\frac{q'(u)}{2q(u)}
 \ge 4-\frac32>0.
$$
Thus $\tau$ is continuous and strictly increasing. This gives an exact
way to locate any prescribed value on the $A_{1}$ branch: if
$$
\alpha_* =2\pi-Lb_*\in[\alpha_1,\pi/2),\qquad
u_*=\sin^2\alpha_*,
$$
then $A_{1,t}=b_*$ exactly when $t=\tau(u_*)$ in the real-$t$
extension, and the integer sequence crosses $b_*$ at
$t_*=\tau(u_*)$.

For $b_*=6.8$, directed-rounding interval evaluation of these formulas
gives
$$
\begin{aligned}
\alpha_*&=1.569784479371958372888\ldots,\\
u_*&=0.999998976165142106025836\ldots,\\
t_*&=115107.498986813436070816\ldots .
\end{aligned}
$$
The reproduction script prints a rigorous enclosure of $t_*$ lying
strictly between $115107$ and $115108$. Since $A_{1,t}$ decreases and
always remains greater than $a_1>6.2$, this proves part 2 of the
Theorem. As a numerical cross-check,
$$
\begin{aligned}
A_{1,115107}&=6.800000003164072033\ldots,\\
A_{1,115108}&=6.799999996823099448\ldots .
\end{aligned}
$$

For $7.6$, the formal inverse angle would be
$2\pi-7.6L=1.015266734924002125\ldots<\alpha_1$, outside the actual
branch range. For $6.5$, it would be
$2\pi-6.5L=1.777728633539941966\ldots>\pi/2$, also outside the range.
These formulas explain both exact-value obstructions, while the branch
classification is what rules out every other $j$.

## 4. A nearby value at $7.05$ is not an extrapolation result

The following is a reproducible numerical observation, separate from
the window theorem. Inverting $A_{1,t}=7.05$ gives
$$
t_*(7.05)=3.859362032342699976\ldots .
$$
The adjacent integer values are
$$
A_{1,3}=7.083538424512691884\ldots,\qquad
A_{1,4}=7.045562354904956364\ldots ,
$$
so the closest lattice modulus to $7.05$ is $A_{1,4}$, at distance
$0.004437645095043635\ldots$. Thus a lattice point near $7.05$ does
indeed exist. This deterministic proximity by itself says nothing
about a measured trough, a recurrence in the experimental coherence,
or a zeta zero; those require a separate prediction and statistical
test. It also does not alter the exclusion of $[7.3,7.9]$.

## 5. Numerical certification and reproducibility

Run
```bash
python3 reproduce.py
```
in this directory. The output is saved in `certificate.txt`.

The value at $t=1$ is not based merely on an unverified root finder.
The script evaluates, with exact rational arithmetic,
$$
F_1(u)=24(1-u)^2(1+3u^2-u^3)-u^2
$$
at $888915/10^6$ and $888916/10^6$, obtaining respectively a positive
and a negative exact rational. Together with the established uniqueness
of the root, this proves
$$
0.888915<u_1<0.888916.
$$
It then uses directed-rounding interval arithmetic and
$\arcsin\sqrt u=\operatorname{atan2}(\sqrt u,\sqrt{1-u})$ to enclose
$\alpha_1,A_{1,1},C_{1,1}$. In particular its certified enclosure for
$A_{1,1}$ is contained in
$$
[7.2887590048,\ 7.2887613005],
$$
which is enough to prove every strict inequality involving $7.3$ and
$7.6$ above. The same interval method certifies the integer cutoff for
$6.8$. Remaining decimals are 80-digit evaluations of the explicit
formulas, with the polynomial residual checked in the script.

### Optional asymptotic check

If $\delta_t=\pi/2-\alpha_t$, then $1-u_t=\sin^2\delta_t$ and
$q(u_t)\to3$. Therefore
$$
t\sim\frac1{\sqrt{72}\,\delta_t^2},\qquad
A_{1,t}-a_1=\frac{\delta_t}{L}
 \sim\frac1{72^{1/4}L\sqrt t}.
$$
This is consistent with the large cutoff needed to reach $6.8$ and
again shows why $a_1$ itself is only a limit, not a finite-$t$ mode.
