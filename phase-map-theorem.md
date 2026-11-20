# Intrinsic phase dynamics of the algebraic lattice

This note proves the large-$t$ phase law and quantitative mesh statements used in my direction. It does not assume any property of zeta zeros or experimental data. Computations are separated from the proof at the end.

## 1. Notation and exact scalar reduction

Write $L=\log 2$ (the natural logarithm), $A=\sqrt{72}$, and
$$
u_t=s_2(t)^2,\qquad v_t=1-u_t,\qquad
 a_t=\frac{\arcsin\sqrt{u_t}}{L},\qquad
 a_\infty=\frac{\pi}{2L},\qquad d_t=a_\infty-a_t.
$$
The real parameter $t\ge1$ in the algebraic equation can also be used in the intermediate steps; restricting to integer $t$ at the end gives the lattice phases. Since $u_t=1-v_t$, the stated equation for $u_t$ becomes
$$
(1-v_t)^2=24t^2v_t^2(3-3v_t+v_t^3).
$$
Both sides are nonnegative and $0<v_t<1$, so taking positive square roots yields the exact scalar equation
$$
\boxed{\quad \frac1t=A\,v_tR(v_t),\qquad
R(v):=\frac{\sqrt{1-v+v^3/3}}{1-v}.\quad} \tag{1}
$$
Also $\arccos\sqrt{1-v}=\arcsin\sqrt v$, hence
$$
\boxed{\quad d_t=\frac{\arcsin\sqrt{v_t}}L.\quad} \tag{2}
$$
Equations (1)–(2), rather than a numerical approximation of the phase map, are the basis of everything below.

For later use,
$$
R(v)^2-1=\frac{v(1-v+v^2/3)}{(1-v)^2}>0\qquad(0<v<1), \tag{3}
$$
so $R(v)>1$. Furthermore,
$$
\frac{d}{dv}\log R(v)
=\frac1{1-v}+\frac{-1+v^2}{2(1-v+v^3/3)}
=\frac{1-v+v^2-v^3/3}{2(1-v)(1-v+v^3/3)}>0. \tag{4}
$$
Indeed, $1-v>0$ and $v^2-v^3/3=v^2(1-v/3)>0$. Thus $v\mapsto AvR(v)$ is strictly increasing, goes from $0$ to $+\infty$ on $(0,1)$, and has a nonzero derivative at $v=0$ when extended analytically. This proves uniqueness of the scalar inverse and justifies the analytic asymptotic inversion in §3.

## 2. Explicit bounds valid for every $t\ge1$

**Theorem 1 (root and phase bounds).** For every $t\ge1$,
$$
\boxed{\quad\frac1{At+1}<v_t<\frac1{At}\quad} \tag{5}
$$
and
$$
\boxed{\quad\frac1{L\sqrt{At+1}}<d_t<\frac1{L\sqrt{At-1}}.\quad} \tag{6}
$$
In particular $v_t=\Theta(t^{-1})$ and $d_t=\Theta(t^{-1/2})$, with the displayed explicit constants.

**Proof.** Since $v_t<1$ and $R(v_t)>1$ by (3), equation (1) first gives $v_t<1/(At)\le1/A$. We next claim
$$
R(v)<1+v\qquad(0<v\le1/A). \tag{7}
$$
All terms are positive, so squaring shows that (7) is equivalent to
$$
1-v+v^3/3<(1-v^2)^2,
$$
or
$$
0<v(1-2v-v^2/3+v^3).
$$
Since $1/A<1/4$, on the stated interval
$$
1-2v-v^2/3+v^3>1-2v-v^2/3>1-\frac12-\frac1{48}>0,
$$
which proves (7). Equations (1), $R>1$, and (7) now give
$$
Av_t<\frac1t<Av_t\left(1+\frac1{At}\right),
$$
from which (5) follows.

For $0<x<1$, integration of the derivative of $\arcsin$ gives $\arcsin x>x$. Also
$$
\arcsin x<\frac{x}{\sqrt{1-x^2}},
$$
because the two sides agree at zero and the derivative of the right side minus the left side is $x^2(1-x^2)^{-3/2}>0$. Putting $x=\sqrt{v_t}$ and using that $v\mapsto v/(1-v)$ is increasing gives (6). $\square$

Numerically, $A=8.485281374238570\ldots$, so (5) already confines $v_t$ to a narrow relative-$O(1/t)$ interval. No unexplicated $O(1)$ constant is needed in Theorem 1.

## 3. Three-term asymptotics and consecutive gaps

**Theorem 2 (asymptotic phase law).** Put $x=(At)^{-1}$. Then
$$
\boxed{\quad v_t=x-\frac{x^2}{2}+\frac{x^3}{8}+O(x^4)\quad} \tag{8}
$$
and
$$
\boxed{\quad
 d_t=\frac1L\left(x^{1/2}-\frac1{12}x^{3/2}
                    -\frac3{160}x^{5/2}+O(x^{7/2})\right).\quad} \tag{9}
$$
Equivalently, with
$$
C:=\frac1{L\sqrt A}=\frac{72^{-1/4}}{L}
  =0.495269307316804\ldots,
$$
one has
$$
d_t=Ct^{-1/2}-\frac{C}{12A}t^{-3/2}
-\frac{3C}{160A^2}t^{-5/2}+O(t^{-7/2}). \tag{10}
$$
Consequently $a_t=a_\infty-d_t$ and the consecutive integer-phase gap
$$
g_t:=a_{t+1}-a_t=d_t-d_{t+1}
$$
satisfies
$$
\boxed{\quad g_t\sim \frac{C}{2}t^{-3/2}.\quad} \tag{11}
$$

**Proof.** A Taylor expansion at zero gives
$$
R(v)=1+\frac v2+\frac{3v^2}{8}+\frac{23v^3}{48}+O(v^4).
$$
Dividing (1) by $A$ therefore gives
$$
x=vR(v)=v+\frac{v^2}{2}+\frac{3v^3}{8}+O(v^4).
$$
The inverse is analytic near zero; reverting this series proves (8). Substitution into
$$\arcsin\sqrt v=\sqrt v\,\left(1+\frac v6+\frac{3v^2}{40}+O(v^3)\right)$$
gives
$$
\arcsin\sqrt{v_t}=x^{1/2}-\frac1{12}x^{3/2}
-\frac3{160}x^{5/2}+O(x^{7/2}),
$$
which is (9) by (2). Finally, (10) is an expansion for real $t\to\infty$. Applying it at $t$ and $t+1$ and using
$$
t^{-1/2}-(t+1)^{-1/2}=\frac12t^{-3/2}+O(t^{-5/2})
$$
proves (11); all later terms are $O(t^{-5/2})$. $\square$

For clarity, the sign of the second coefficient in (10) is negative. This is also confirmed by the independent numerical checks described below.

## 4. Explicit gap bounds and a tail-net criterion

The asymptotic $g_t\sim(C/2)t^{-3/2}$ does not by itself provide a finite-$t$ covering certificate. The following bounds do.

Define, for real $t\ge1$,
$$
H_t:=\frac{(At+1)^{-1/2}-(A(t+1)-1)^{-1/2}}L,
$$
$$
G_t:=\frac{(At-1)^{-1/2}-(A(t+1)+1)^{-1/2}}L.
$$
Because $A>2$, $H_t>0$.

**Theorem 3 (quantitative mesh).** For every integer $t\ge1$,
$$
\boxed{\quad0<H_t<g_t<G_t.\quad} \tag{12}
$$
Moreover $G_t$ is strictly decreasing in $t$ and
$$
G_t\le \frac{A+2}{2L(At-1)^{3/2}}. \tag{13}
$$
Therefore, for every integer $T\ge1$, the set $\{a_t:t\ge T\}$ is a $(G_T/2)$-net of $[a_T,a_\infty)$: every point of that interval is within $G_T/2$ of some integer-indexed phase in the tail. The same statement holds for $\{a_T,\ldots,a_M\}$ and $[a_T,a_M]$ when $T<M$. A simpler sufficient condition for a prescribed $\tau>0$ is
$$
\boxed{\quad AT-1\ge\left(\frac{A+2}{4L\tau}\right)^{2/3}
\quad\Longrightarrow\quad \{a_t:t\ge T\}\text{ is a }\tau\text{-net of }[a_T,a_\infty).\quad} \tag{14}
$$
Also $G_T/2\sim C/(4T^{3/2})$.

**Proof.** The bounds in (12) are immediate from (6), applied at $t$ and $t+1$. Differentiation gives
$$
G_t'=\frac{A}{2L}\left((A(t+1)+1)^{-3/2}-(At-1)^{-3/2}\right)<0.
$$
For (13), apply the mean value theorem to $q(x)=x^{-1/2}$ between $x=At-1$ and $y=A(t+1)+1=x+A+2$:
$$
q(x)-q(y)=\frac{A+2}{2}\xi^{-3/2}
\le\frac{A+2}{2}x^{-3/2},\qquad x<\xi<y.
$$
For the net statement, if $a_t\le x<a_{t+1}$, then the closer of $a_t,a_{t+1}$ is within $g_t/2<G_t/2\le G_T/2$. Such a bracket exists for every $x\in[a_T,a_\infty)$ because $a_t$ is increasing and tends to $a_\infty$. The finite-grid statement is identical. Finally, (14) is (13) with $G_T/2\le\tau$ rearranged. $\square$

For example, at $\tau=0.0022$, direct evaluation of the sharper criterion $G_T/2\le\tau$ certifies $T=17$ ($G_{17}/2=0.002091590853959\ldots$). The slightly more conservative closed-form condition (14) certifies $T=18$. These are statements about the **tail only**; they say nothing that could fill gaps between early phases.

Since every positive lattice band is made from translates $j\Delta\pm a_t$, where $\Delta=2\pi/L$, Theorems 1–3 transfer verbatim to distances inside each band.

## 5. The empirical phase law is not uniform

The convergence $a_t\to a_\infty$ immediately gives
$$
\widehat\mu_M:=\frac1M\sum_{t=1}^M\delta_{a_t}
\longrightarrow\delta_{a_\infty}\qquad(M\to\infty) \tag{15}
$$
in the weak topology: just apply the definition to a bounded continuous test function and use Cesàro convergence. Thus an independent uniform distribution on the envelope $[\pi/(3L),\pi/(2L)]$ may be chosen as an external null hypothesis, but it is not the empirical law of the deterministic phases.

There is, nevertheless, a nondegenerate limit after the natural tail rescaling. Let
$$
\mathcal N(\delta):=\#\{t\ge1:d_t\ge\delta\},\qquad \delta>0.
$$
It is finite because $d_t\to0$. Since $d_t$ is strictly decreasing and $d_t\sim Ct^{-1/2}$,
$$
\boxed{\quad\mathcal N(\delta)\sim C^2\delta^{-2}\qquad(\delta\downarrow0).\quad} \tag{16}
$$
Now set $z_{t,M}=d_t/d_M$ for $1\le t\le M$. For each fixed $z\ge1$, (16) and $d_M\sim CM^{-1/2}$ imply
$$
\frac1M\#\{t\le M:z_{t,M}>z\}\longrightarrow \min(1,z^{-2}). \tag{17}
$$
Hence the empirical law of $z_{t,M}$, with $t$ uniform on $\{1,\ldots,M\}$, converges weakly to the law on $[1,\infty)$ having
$$
\boxed{\quad F(z)=0\ (z\le1),\qquad F(z)=1-z^{-2}\ (z>1),\qquad
f(z)=2z^{-3}\mathbf1_{z>1}.\quad} \tag{18}
$$
Along any deterministic subsequence with $t/M\to x\in(0,1]$, one has $z_{t,M}\to x^{-1/2}$. Thus, equivalently, the normalized empirical limit is the law of $X^{-1/2}$ with $X$ uniform on $(0,1]$. This heavy-tailed normalized law is the precise nonuniform asymptotic phase distribution.

## 6. Consistency warning about the stated $0.0022$-net assertion

The following is independent of the zeta/experimental issue. Under the literal definition in which $t$ ranges over **integers**, the full phase collection cannot be a $0.0022$-net within each whole band, regardless of how large $t_{\max}$ is.

Indeed, the first gap is present permanently. Theorem 3 gives the proof-only lower bound
$$
g_1>H_1=\frac{(A+1)^{-1/2}-(2A-1)^{-1/2}}L
=0.1074290926635737\ldots>0.0044.
$$
The midpoint of $[a_1,a_2]$ is therefore more than $H_1/2=0.0537145463\ldots$ from every integer-indexed phase. Later phases cannot enter this interval. Translations $j\Delta\pm a_t$ reproduce the same obstruction inside each band.

This is compatible with the tail-net theorem: increasingly many late $t$ values make late portions of the band fine, but cannot repair early holes. If “$0.0022$-net” was intended for a different sampling of $t$, or for a different notion of net, that sampling or notion must be stated separately. It is not valid for the integer-$t$ lattice as defined.

## 7. Reproducible computations (not used as proof substitutes)

`phase_asymptotics.py` uses only Python's standard library. It solves (1) by bisection, evaluates (2), and prints all constants and gaps quoted above. It also checks the strict root bounds (5), phase bounds (6), and two-sided gap bounds (12) for every integer $1\le t\le10000$, and evaluates the two $\tau=0.0022$ tail-net certificates. The recorded output is `verification.txt`.

Selected direct numerical values are
$$
v_1=0.1110842444644\ldots,\qquad
v_2=0.05721318541234\ldots,
$$
$$
a_1=1.775960717579\ldots,\qquad
a_2=1.917719572366\ldots,\qquad
g_1=0.1417588547867208\ldots,
$$
and
$$
g_{100}=0.0002457206462203\ldots,\qquad
\frac{d_t\sqrt t}{C}\longrightarrow1.
$$
The script obtained $-0.004864005\ldots$ for $(d_t-Ct^{-1/2})t^{3/2}$ at $t=100000$, agreeing with the proved second coefficient $-C/(12A)=-0.004864003968296\ldots$. These numerical checks reproduce formulas (1)–(2); they are not cited for any of the proof steps above.
