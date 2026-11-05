#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate paper/frequency-grids-formalization.tex.

The declaration-by-declaration table is generated from the single list `rows` below, which
mirrors the actual Lean sources of FrequencyGrids/.  Usage (from the repository root):

    python3 paper/tools/build_paper.py && (cd paper && latexmk -pdf frequency-grids-formalization.tex)
"""

# -*- coding: utf-8 -*-
rows = []
def row(name, kind, stmt, status, grp=None):
    rows.append((name, kind, stmt, status, grp))

# ---------- Basic ----------
row(r"\texttt{char}\lb\texttt{Poly}", "def",
    r"$\mathrm{charPoly}(s) = 8s^6-24s^4+24s^2-8$", "definition", "basic")
row(r"\texttt{char}\lb\texttt{Poly}\lb\texttt{eq}", "thm",
    r"$\mathrm{charPoly}(s) = 8(s^2-1)^3$", "proved", "basic")
row(r"\texttt{abs}\lb\texttt{cube}\lb\texttt{rpow}", "thm",
    r"$|8v^3|^{2/3} = 4v^2$ for $v\in\R$", "proved", "basic")
row(r"\texttt E", "def",
    r"$E=|\mathrm{charPoly}|^{2/3}\cdot P+4s^4$, with $P=24k_3^2s^6-72k_3^2s^4-24k_3^2$", "definition", "basic")
row(r"\texttt{E}\lb\texttt{eq}", "thm",
    r"$E(s,k_3) = 4\bigl(s^4+24k_3^2(s^2-1)^2(s^6-3s^4-1)\bigr)$", "proved", "basic")
row(r"\texttt{E}\lb\texttt{eq}'", "thm",
    r"$E(s,k_3)=4\bigl(s^4-24k_3^2(s^2-1)^2(3s^4-s^6+1)\bigr)$", "proved", "basic")
row(r"\texttt{continuous}\lb\texttt E", "thm",
    r"$s\mapsto E(s,k_3)$ is continuous", "proved", "basic")
row(r"\texttt{E}\lb\texttt{neg}\lb\texttt{one}", "thm", r"$E(-1,k_3)=4$", "proved", "basic")
row(r"\texttt{E}\lb\texttt{zero}", "thm", r"$E(0,k_3)=-96k_3^2$", "proved", "basic")
row(r"\texttt{exists}\lb\texttt{root}\lb\texttt{unit}", "thm",
    r"$k_3\neq0\Rightarrow\exists s\in(-1,0),\,E(s,k_3)=0$ \ (IVT)", "proved", "basic")
row(r"\texttt{E}\lb\texttt{right}\lb\texttt{neg}", "thm",
    r"$t\ge1\Rightarrow E(-10^{-4},-t)<0$", "proved", "basic")
row(r"\texttt{E}\lb\texttt{left}\lb\texttt{pos}", "thm",
    r"$t\le589\Rightarrow E(-0.9999,-t)>0$", "proved", "basic")
row(r"\texttt{E}\lb\texttt{left}\lb\texttt{neg}", "thm",
    r"$t\ge590\Rightarrow E(-0.9999,-t)<0$", "proved", "basic")
row(r"\texttt{s2}", "def",
    r"root selector: $E(s_2(t),-t)=0$, $s_2(t)\in(-0.9999,-0.0001)$ for $1\le t\le589$; $0$ otherwise", "definition", "basic")
row(r"\texttt{exists}\lb\texttt{root}\lb\texttt{grid}", "thm",
    r"$1\le t\le589\Rightarrow\exists s\in(-0.9999,-0.0001),\,E(s,-t)=0$", "proved", "basic")
row(r"\texttt{s2}\lb\texttt{spec}", "thm",
    r"$s_2(t)\in(-0.9999,-0.0001)\wedge E(s_2(t),-t)=0$ \ ($1\le t\le589$)", "proved", "basic")
row(r"\texttt{s2}\lb\texttt{mem}", "thm", r"$1\le t\le589\Rightarrow s_2(t)\in(-0.9999,-0.0001)$", "proved", "basic")
row(r"\texttt{s2}\lb\texttt{isRoot}", "thm", r"$1\le t\le589\Rightarrow E(s_2(t),-t)=0$", "proved", "basic")
row(r"\texttt{abs}\lb\texttt{s2}\lb\texttt{lt}\lb\texttt{one}", "thm", r"$1\le t\le589\Rightarrow|s_2(t)|<1$", "proved", "basic")

# ---------- Lattice ----------
row(r"\texttt b", "def",
    r"$b(t,k,\sigma)=(\arcsin(\sigma|s_2(t)|)-2k\pi)/\ln 2$, $k\in\Z$", "definition", "lattice")
row(r"\texttt{log}\lb\texttt{two}\lb\texttt{pos}", "thm", r"$0<\ln 2$", "proved", "lattice")
row(r"\texttt{log}\lb\texttt{two}\lb\texttt{ne}\lb\texttt{zero}", "thm", r"$\ln2\neq0$", "proved", "lattice")
row(r"\texttt{b}\lb\texttt{eq}\lb\texttt{affine}", "thm",
    r"$b=\arcsin(\sigma|s_2(t)|)/\ln2-(2\pi/\ln2)k$", "proved", "lattice")
row(r"\texttt{b}\lb\texttt{step}", "thm",
    r"$b(t,k+1,\sigma)-b(t,k,\sigma)=-2\pi/\ln2$", "proved", "lattice")
row(r"\texttt{b}\lb\texttt{step}\lb\texttt{uniform}", "thm",
    r"step independent of $t,t',k,k',\sigma,\sigma'$", "proved", "lattice")
row(r"\texttt{b}\lb\texttt{strict}\lb\texttt{Anti}", "thm",
    r"$k\mapsto b(t,k,\sigma)$ strictly antitone", "proved", "lattice")
row(r"\texttt{b}\lb\texttt{injective}", "thm",
    r"$k\mapsto b(t,k,\sigma)$ injective", "proved", "lattice")
row(r"\texttt{phase}\lb\texttt{Defect}", "def",
    r"$\delta b_{t,k,\sigma}=b(t,k+1,\sigma)-b(t,k,\sigma)+2\pi/\ln2$", "definition", "lattice")
row(r"\texttt{phase}\lb\texttt{Defect}\lb\texttt{eq}\lb\texttt{zero}", "thm",
    r"$\delta b_{t,k,\sigma}=0$ for all $t,k,\sigma$", "proved", "lattice")
row(r"\texttt{Nphase}", "def",
    r"$\#\{(t,k,\sigma)\in S:\delta b_{t,k,\sigma}\neq0\}$", "definition", "lattice")
row(r"\texttt{Nphase}\lb\texttt{eq}\lb\texttt{zero}", "thm",
    r"$N_{\mathrm{phase}}(S)=0$ for every truncation $S$", "proved", "lattice")

# ---------- Uniqueness ----------
row(r"\texttt{rootRat}", "def", r"$f(u)=u^2/((1-u)^2(1+3u^2-u^3))$", "definition", "unique")
row(r"\texttt{rootRat}\lb\texttt{denom}\lb\texttt{pos}", "thm", r"$u\in(0,1)\Rightarrow(1-u)^2(1+3u^2-u^3)>0$", "proved", "unique")
row(r"\texttt{rootRat}\lb\texttt{pos}", "thm", r"$u\in(0,1)\Rightarrow f(u)>0$", "proved", "unique")
row(r"\texttt{deriv}\lb\texttt{rootRat}", "thm",
    r"$f'(u)=u(1-u)(2+7u^3-3u^4)/((1-u)^2(1+3u^2-u^3))^2$", "proved", "unique")
row(r"\texttt{deriv}\lb\texttt{rootRat}\lb\texttt{log}", "thm",
    r"$f'(u)=f(u)\,(2/(u(1-u))-(6u-3u^2)/(1+3u^2-u^3))$", "proved", "unique")
row(r"\texttt{logDeriv}\lb\texttt{ge}\lb\texttt{five}", "thm",
    r"$2/(u(1-u))-(6u-3u^2)/(1+3u^2-u^3)\ge5$ \ (via $8$ and $3$)", "proved", "unique")
row(r"\texttt{rootRat}\lb\texttt{strictMonoOn}", "thm", r"$f$ strictly increasing on $(0,1)$", "proved", "unique")
row(r"\texttt{root}\lb\texttt{iff}", "thm",
    r"$E(s,-t)=0\iff f(s^2)=24t^2$ on $(-1,0)$", "proved", "unique")
row(r"\texttt{exists}\lb\texttt{unique}\lb\texttt{root}\lb\texttt{grid}", "thm",
    r"$\exists!\,s\in(-0.9999,-0.0001),\ E(s,-t)=0$", "proved", "unique")
row(r"\texttt{s2}\lb\texttt{unique}", "thm",
    r"any root in the bracket equals $s_2(t)$ \ (no dependence on `choose`)", "proved", "unique")
row(r"\texttt{abs}\lb\texttt{s2}\lb\texttt{strictMono}", "thm", r"$t\mapsto|s_2(t)|$ strictly increasing", "proved", "unique")
row(r"\texttt{s2}\lb\texttt{mem}\lb\texttt{of}\lb\texttt{sign}\lb\texttt{change}", "thm",
    r"sign change on $[lo,hi]\Rightarrow s_2(t)\in(lo,hi)$ \ (certificate)", "proved", "unique")

# ---------- Enclosure ----------
row(r"\texttt{s2}\lb\texttt{enclosure}\lb\texttt{1} \dots \texttt{10}", "thm",
    r"$s_2(t)\in(lo_t,hi_t)$, width $4\cdot10^{-6}$, $t=1,\dots,10$", "proved", "encl")

# ---------- Counting ----------
row(r"\texttt{natCast}\lb\texttt{toNat}\lb\texttt{eq}", "thm", r"cast bridge $\N\to\Z\to\R$ for \texttt{toNat}", "proved", "counting")
row(r"\texttt{card}\lb\texttt{le}\lb\texttt{of}\lb\texttt{forall}\lb\texttt{mem}\lb\texttt{Icc}", "thm",
    r"$S\subseteq[a,b]$ (integers) $\Rightarrow \#S\le b-a+1$", "proved", "counting")
row(r"\texttt{le}\lb\texttt{card}\lb\texttt{of}\lb\texttt{forall}\lb\texttt{Icc}\lb\texttt{mem}", "thm",
    r"$[a,b]\cap\Z\subseteq S\Rightarrow \#S\ge b-a-2$", "proved", "counting")
row(r"\texttt{bOf}", "def", r"$b_\alpha(k)=(\alpha-2k\pi)/\ln2$", "definition", "counting")
row(r"\texttt{b}\lb\texttt{eq}\lb\texttt{bOf}", "thm", r"$b(t,k,\sigma)=b_{\arcsin(\sigma|s_2(t)|)}(k)$", "proved", "counting")
row(r"\texttt{kLo}", "def", r"$(\alpha-T\ln2)/2\pi$", "definition", "counting")
row(r"\texttt{kHi}", "def", r"$(\alpha+T\ln2)/2\pi$", "definition", "counting")
row(r"\texttt{kSet}", "def", r"$\{k\in\Z:\ \lceil k_{lo}\rceil\le k\le\lfloor k_{hi}\rfloor,\ k\neq0\}$", "definition", "counting")
row(r"\texttt{kHi}\lb\texttt{sub}\lb\texttt{kLo}", "thm", r"$k_{hi}-k_{lo}=T\ln2/\pi$", "proved", "counting")
row(r"\texttt{mem}\lb\texttt{Icc}\lb\texttt{ceil}\lb\texttt{floor}", "thm", r"$\lceil k_{lo}\rceil\le k\le\lfloor k_{hi}\rfloor\iff k_{lo}\le k\le k_{hi}$", "proved", "counting")
row(r"\texttt{mem}\lb\texttt{Icc}\lb\texttt{iff}\lb\texttt{abs}\lb\texttt{bOf}", "thm", r"$k_{lo}\le k\le k_{hi}\iff|b_\alpha(k)|\le T$", "proved", "counting")
row(r"\texttt{mem}\lb\texttt{kSet}\lb\texttt{iff}", "thm", r"$k\in k_{Set}\iff k\neq0\wedge|b_\alpha(k)|\le T$", "proved", "counting")
row(r"\texttt{card}\lb\texttt{kSet}\lb\texttt{bounds}", "thm",
    r"$T\ge0\Rightarrow\bigl|\#k_{Set}(\alpha,T)-T\ln2/\pi\bigr|\le3$", "proved", "counting")
row(r"\texttt{sigmaSet}", "def", r"$\{-1,1\}\subset\R$", "definition", "counting")
row(r"\texttt{card}\lb\texttt{sigmaSet}", "thm", r"$\#\sigma_{Set}=2$", "proved", "counting")
row(r"\texttt{mem}\lb\texttt{sigmaSet}", "thm", r"$\sigma\in\{-1,1\}\iff\sigma=-1\vee\sigma=1$", "proved", "counting")
row(r"\texttt{phase}", "def", r"$\alpha(t,\sigma)=\arcsin(\sigma|s_2(t)|)$", "definition", "counting")
row(r"\texttt{latticeSet}", "def", r"$[1,100]\times\{-1,1\}$ (the $200$ lattices)", "definition", "counting")
row(r"\texttt{card}\lb\texttt{Icc}\lb\texttt{1}\lb\texttt{100}", "thm", r"$\#\{1,\dots,100\}=100$", "proved", "counting")
row(r"\texttt{card}\lb\texttt{latticeSet}", "thm", r"$\#\text{latticeSet}=200$", "proved", "counting")
row(r"\texttt{modeSet}", "def", r"triplets $(t,k,\sigma)$ with $1\le t\le100$, $\sigma=\pm1$, $k\neq0$, $|b|\le T$", "definition", "counting")
row(r"\texttt{mem}\lb\texttt{modeSet}", "thm", r"membership characterisation of the triplet set", "proved", "counting")
row(r"\texttt{Ntotal}", "def", r"$N_{\mathrm{tot}}(T)=\#\text{modeSet}(T)$", "definition", "counting")
row(r"\texttt{NR}", "def", r"$N_R(T)=\#\{b(t,k,\sigma):\ \text{triplets}\}$", "definition", "counting")
row(r"\texttt{Has}\lb\texttt{Collision}", "def", r"$\exists$ two distinct triplets with equal $b$", "definition", "counting")
row(r"\texttt{card}\lb\texttt{modeSet}", "thm", r"$\#\text{modeSet}=\sum_{(t,\sigma)}\#k_{Set}$", "proved", "counting")
row(r"\texttt{Ntotal}\lb\texttt{bounds}", "thm",
    r"$\bigl|N_{\mathrm{tot}}-200\,T\ln2/\pi\bigr|\le600$", "proved", "counting")
row(r"\texttt{NR}\lb\texttt{le}\lb\texttt{Ntotal}", "thm", r"$N_R(T)\le N_{\mathrm{tot}}(T)$", "proved", "counting")
row(r"\texttt{NR}\lb\texttt{eq}\lb\texttt{Ntotal}\lb\texttt{iff}", "thm",
    r"$N_R=N_{\mathrm{tot}}\iff$ no collisions", "proved", "counting")
row(r"\texttt{slope}\lb\texttt{bounds}", "thm", r"$44.12<200\ln2/\pi<44.14$", "proved", "counting")
row(r"\texttt{Ntotal}\lb\texttt{approx}", "thm", r"$|N_{\mathrm{tot}}-44.13\,T|\le600+T/100$", "proved", "counting")
row(r"\texttt{NR}\lb\texttt{le}\lb\texttt{slope}", "thm", r"$N_R(T)\le44.14\,T+600$", "proved", "counting")
row(r"\texttt{card}\lb\texttt{modeSet}\lb\texttt{eq}\lb\texttt{Ntotal}", "thm",
    r"$\#\mathrm{modeSet}\,T=N_{\mathrm{tot}}(T)$", "proved", "counting")
row(r"\texttt{NR}\lb\texttt{eq}\lb\texttt{Ntotal}\lb\texttt{of}\lb\texttt{noCollision}", "thm",
    r"no collision $\Rightarrow N_R(T)=N_{\mathrm{tot}}(T)$", "proved", "counting")

# ---------- Structure ----------
row(r"\texttt{s2}\lb\texttt{abs}\lb\texttt{pos}", "thm", r"$1\le t\le589\Rightarrow0<|s_2(t)|$", "proved", "structure")
row(r"\texttt{b}\lb\texttt{collision}\lb\texttt{structure}", "thm",
    r"$b(t,k,\sigma)=b(t',k',\sigma')\Rightarrow\sigma=\sigma'\wedge|s_2(t)|=|s_2(t')|\wedge k=k'$", "proved", "structure")
row(r"\texttt{collision}\lb\texttt{imp}\lb\texttt{duplicate}\lb\texttt{phase}", "thm",
    r"a collision forces $t\neq t'$ with $|s_2(t)|=|s_2(t')|$", "proved", "structure")
row(r"\texttt{abs}\lb\texttt{s2}\lb\texttt{injective}", "thm",
    r"$|s_2(t)|=|s_2(t')|\Rightarrow t=t'$ \ (same root $\Rightarrow$ $t^2=t'^2$)", "proved", "structure")
row(r"\texttt{not}\lb\texttt{hasCollision}", "thm", r"$\neg\,\mathrm{HasCollision}(T)$ for every $T$", "proved", "structure")
row(r"\texttt{NR}\lb\texttt{eq}\lb\texttt{Ntotal}", "thm", r"$N_R(T)=N_{\mathrm{tot}}(T)$, unconditionally", "proved", "structure")

# ---------- Resonance ----------
row(r"\texttt{gramCoeff}", "def",
    r"$G_{12}(T)=1$ if $b_1=b_2$, else $(e^{i(b_1-b_2)T}-1)/(i(b_1-b_2)T)$", "definition", "resonance")
row(r"\texttt{gramCoeff}\lb\texttt{self}", "thm", r"$G_{11}(T)=1$", "proved", "resonance")
row(r"\texttt{norm}\lb\texttt{exp}\lb\texttt{I}\lb\texttt{sub}\lb\texttt{one}\lb\texttt{le}\lb\texttt{two}", "thm",
    r"$\|e^{i\theta}-1\|\le2$", "proved", "resonance")
row(r"\texttt{gramCoeff}\lb\texttt{offdiag}\lb\texttt{bound}", "thm",
    r"$b_1\neq b_2,\ T>0\Rightarrow|G_{12}(T)|\le2/(T|b_1-b_2|)$", "proved", "resonance")
row(r"\texttt{hterm}", "def", r"$m^{-(1/2+ib)}$ as a complex power", "definition", "resonance")
row(r"\texttt{hsum}", "def", r"$S_f(N,b)=\sum_{m\le N}m^{-(1/2+ib)}$", "definition", "resonance")
row(r"\texttt{hterm}\lb\texttt{conj}", "thm", r"$\overline{m^{-(1/2+ib)}}=m^{-(1/2-ib)}$", "proved", "resonance")
row(r"\texttt{hsum}\lb\texttt{conj}", "thm", r"$\overline{S_f(N,b)}=S_f(N,-b)$", "proved", "resonance")
row(r"\texttt{hsum}\lb\texttt{re}\lb\texttt{even}", "thm", r"$\operatorname{Re}S_f(N,-b)=\operatorname{Re}S_f(N,b)$", "proved", "resonance")
row(r"\texttt{hsum}\lb\texttt{re}\lb\texttt{neg}\lb\texttt{iff}", "thm",
    r"$\operatorname{Re}S_f(N,-b)=c\iff\operatorname{Re}S_f(N,b)=c$", "proved", "resonance")

# ---------- Congruence ----------
row(r"\texttt{prime}\lb\texttt{mod}\lb\texttt{six}", "thm",
    r"$p$ prime, $p>3$ $\Rightarrow$ $p\equiv\pm1\ (6)$", "proved", "congruence")
row(r"\texttt{prime}\lb\texttt{zmod}\lb\texttt{six}", "thm",
    r"$(p:\mathrm{ZMod}\,6)\in\{1,5\}$", "proved", "congruence")
row(r"\texttt{converse}\lb\texttt{fails}", "thm", r"$25\%6=1\wedge\neg\,\mathrm{Prime}(25)$", "proved", "congruence")
row(r"\texttt{filter}\lb\texttt{not}\lb\texttt{sufficient}", "thm", r"$\exists n,\ n\%6=1\wedge\neg\,\mathrm{Prime}(n)$", "proved", "congruence")

# ---------- Eigen ----------
row(r"\texttt{cpow}\lb\texttt{conj}\lb\texttt{natCast}", "thm",
    r"$\overline{m^{w}}=m^{\bar w}$ for $m\in\N$", "proved", "eigen")
row(r"\texttt{conj}\lb\texttt{gram}\lb\texttt{exponent}", "thm",
    r"$\overline{-1-i(x-y)}=-1-i(y-x)$", "proved", "eigen")
row(r"\texttt{modeB}", "def", r"frequency $b_i$ of a mode $i\in\mathrm{modeSet}(T)$", "definition", "eigen")
row(r"\texttt{gramMatrix}", "def",
    r"$G_{ij}(X)=\sum_{n\le X}n^{-1-i(b_i-b_j)}$", "definition", "eigen")
row(r"\texttt{gramMatrix}\lb\texttt{isHermitian}", "thm",
    r"$G(X)^{\mathsf H}=G(X)$, so $(G+G^{\mathsf H})/2=G$", "proved", "eigen")
row(r"\texttt{eig}", "def",
    r"$\lambda_j$, the eigenvalues of $G(X)$ (spectral theorem)", "definition", "eigen")
row(r"\texttt{eigPos}", "def", r"$\max(\lambda_j,0)$ — the code's clamp", "definition", "eigen")
row(r"\texttt{eigMax}", "def", r"$\max_j\lambda_j^{+}$ (as $\sup$; $\sup\emptyset=0$)", "definition", "eigen")
row(r"\texttt{offSum}", "def", r"$I_j(X)=\sum_{i\neq j}|G_{ij}(X)|$", "definition", "eigen")
row(r"\texttt{offRatio}", "def", r"$r_j(X)=I_j(X)/|G_{jj}(X)|$", "definition", "eigen")
row(r"\texttt{Noff}", "def", r"$N_{\mathrm{off}}(T,X,\delta_X)=\#\{j:r_j(X)>\delta_X\}$", "definition", "eigen")
row(r"\texttt{Nvan}", "def",
    r"$N_{\mathrm{van}}(T,X,\delta_T)=\#\{j:\lambda_j^{+}\le\delta_T\max_j\lambda_j^{+}\}$", "definition", "eigen")
row(r"\texttt{card}\lb\texttt{univ}\lb\texttt{modeSet}", "thm", r"$\#\mathrm{univ}=N_{\mathrm{tot}}(T)$", "proved", "eigen")
row(r"\texttt{Noff}\lb\texttt{le}\lb\texttt{Ntotal}", "thm", r"$N_{\mathrm{off}}\le N_{\mathrm{tot}}$", "proved", "eigen")
row(r"\texttt{Nvan}\lb\texttt{le}\lb\texttt{Ntotal}", "thm", r"$N_{\mathrm{van}}\le N_{\mathrm{tot}}$", "proved", "eigen")
row(r"\texttt{eigPos}\lb\texttt{le}\lb\texttt{eigMax}", "thm", r"$\lambda_j^{+}\le\max_i\lambda_i^{+}$", "proved", "eigen")
row(r"\texttt{eigMax}\lb\texttt{nonneg}", "thm", r"$\mathrm{modeSet}(T)\neq\emptyset\Rightarrow 0\le\max_j\lambda_j^{+}$", "proved", "eigen")
row(r"\texttt{gramE}", "def",
    r"$E_{i,m}=(m+1)^{-1/2-i b_i}$, $m<\lfloor X\rfloor$", "definition", "eigen")
row(r"\texttt{conj}\lb\texttt{half}\lb\texttt{exponent}", "thm", r"$\overline{-1/2-ix}=-1/2+ix$", "proved", "eigen")
row(r"\texttt{sum}\lb\texttt{Icc}\lb\texttt{one}\lb\texttt{eq}\lb\texttt{sum}\lb\texttt{fin}", "thm",
    r"$\sum_{1\le n\le N}=\sum_{m:\mathrm{Fin}\,N}(m+1)$", "proved", "eigen")
row(r"\texttt{gramMatrix}\lb\texttt{eq}\lb\texttt{mul}\lb\texttt{conjTranspose}", "thm",
    r"$G(X)=E\,E^{\mathsf H}$", "proved", "eigen")
row(r"\texttt{gramMatrix}\lb\texttt{posSemidef}", "thm", r"$G(X)\succeq0$", "proved", "eigen")
row(r"\texttt{eigenvalues}\lb\texttt{congr}", "thm", r"eigenvalues independent of the hermitianity proof", "proved", "eigen")
row(r"\texttt{eig}\lb\texttt{nonneg}", "thm", r"$0\le\lambda_j$", "proved", "eigen")
row(r"\texttt{eigPos}\lb\texttt{eq}\lb\texttt{eig}", "thm", r"$\max(\lambda_j,0)=\lambda_j$ (clamp is the identity)", "proved", "eigen")
row(r"\texttt{zero}\lb\texttt{le}\lb\texttt{eigMax}", "thm", r"$0\le\max_j\lambda_j^{+}$, also with no modes", "proved", "eigen")
row(r"\texttt{rank}\lb\texttt{gramMatrix}\lb\texttt{le}", "thm", r"$\operatorname{rank}G(X)\le\lfloor X\rfloor$", "proved", "eigen")
row(r"\texttt{mulVec}\lb\texttt{eigenvectorBasis}\lb\texttt{eig}", "thm", r"$G v_j=\lambda_j v_j$ for the eigenbasis", "proved", "eigen")
row(r"\texttt{card}\lb\texttt{nonzero}\lb\texttt{eig}\lb\texttt{eq}\lb\texttt{rank}", "thm",
    r"$\#\{j:\lambda_j\ne0\}=\operatorname{rank}G(X)$", "proved", "eigen")
row(r"\texttt{card}\lb\texttt{nonzero}\lb\texttt{eig}\lb\texttt{le}\lb\texttt{rank}", "thm", r"$\#\{j:\lambda_j\ne0\}\le\operatorname{rank}G(X)$", "proved", "eigen")
row(r"\texttt{card}\lb\texttt{le}\lb\texttt{Nvan}\lb\texttt{add}", "thm",
    r"$\#\mathrm{modeSet}\le N_{\mathrm{van}}+X$ \ ($\delta\ge0$)", "proved", "eigen")
row(r"\texttt{Ntotal}\lb\texttt{sub}\lb\texttt{le}\lb\texttt{Nvan}", "thm",
    r"$N_{\mathrm{van}}\ge N_{\mathrm{tot}}-\lfloor X\rfloor$ \ ($\delta\ge0$)", "proved", "eigen")
row(r"\texttt{NR}\lb\texttt{sub}\lb\texttt{le}\lb\texttt{Nvan}", "thm",
    r"$N_{\mathrm{van}}\ge N_R-\lfloor X\rfloor$ \ ($\delta\ge0$, no hypothesis)", "proved", "eigen")
row(r"\texttt{Noff}\lb\texttt{eq}\lb\texttt{card}\lb\texttt{of}\lb\texttt{forall}\lb\texttt{gt}", "thm",
    r"$\forall j,\ \delta<r_j\Rightarrow N_{\mathrm{off}}=\#\mathrm{modeSet}$", "proved", "eigen")
row(r"\texttt{Noff}\lb\texttt{eq}\lb\texttt{card}\lb\texttt{of}\lb\texttt{gram}\lb\texttt{gt}", "thm",
    r"one neighbour with $\delta|G_{jj}|<|G_{ij}|$ for each $j$ $\Rightarrow N_{\mathrm{off}}=\#\mathrm{modeSet}$", "proved", "eigen")
row(r"\texttt{harmonicR}", "def", r"$H_N=\sum_{1\le n\le N}n^{-1}$ as a real", "definition", "eigen")
row(r"\texttt{harmonicR}\lb\texttt{eq}\lb\texttt{harmonic}", "thm", r"$H_N=(\mathrm{harmonic}\,N:\mathbb{Q})$", "proved", "eigen")
row(r"\texttt{harmonicR}\lb\texttt{pos}", "thm", r"$N>0\Rightarrow H_N>0$", "proved", "eigen")
row(r"\texttt{gramMatrix}\lb\texttt{diag}", "thm", r"$G_{ii}(X)=H_{\lfloor X\rfloor}$", "proved", "eigen")
row(r"\texttt{gramMatrix}\lb\texttt{diag}\lb\texttt{eq}\lb\texttt{harmonic}", "thm",
    r"$G_{ii}(X)$ is Mathlib's \texttt{harmonic}", "proved", "eigen")
row(r"\texttt{gramMatrix}\lb\texttt{diag}\lb\texttt{pos}", "thm", r"$\lfloor X\rfloor\ge1\Rightarrow|G_{ii}|>0$", "proved", "eigen")
row(r"\texttt{rank}\lb\texttt{gramMatrix}\lb\texttt{le}\lb\texttt{rank}\lb\texttt{gramE}", "thm",
    r"$\operatorname{rank}G\le\operatorname{rank}E$", "proved", "eigen")
row(r"\texttt{card}\lb\texttt{zero}\lb\texttt{eig}\lb\texttt{ge}", "thm",
    r"$\#\{j:\lambda_j=0\}\ge\#\mathrm{modeSet}-\lfloor X\rfloor$", "proved", "eigen")
row(r"\texttt{Noff}\lb\texttt{eq}\lb\texttt{card}\lb\texttt{of}\lb\texttt{gram}\lb\texttt{gt}'", "thm",
    r"the same, with $|G_{ii}|>0$ discharged by \texttt{gramMatrix\lb diag\lb pos}", "proved", "eigen")

# ---------- Parametric ----------
row(r"\texttt{latticeSetOf}", "def", r"$[1,t_{\max}]\times\{-1,1\}$", "definition", "param")
row(r"\texttt{card}\lb\texttt{latticeSetOf}", "thm", r"$\#\texttt{latticeSetOf}\,t_{\max}=2\,t_{\max}$", "proved", "param")
row(r"\texttt{modeSetOf}", "def", r"triplets for a truncation $t_{\max}$", "definition", "param")
row(r"\texttt{mem}\lb\texttt{modeSetOf}", "thm", r"membership: $t\le t_{\max}$, $\sigma=\pm1$, $k\ne0$, $|b|\le T$", "proved", "param")
row(r"\texttt{modeSet}\lb\texttt{eq}", "thm", r"$\texttt{modeSet}\,T=\texttt{modeSetOf}\,100\,T$", "proved", "param")
row(r"\texttt{NtotalOf}", "def", r"$N_{\mathrm{tot}}(t_{\max},T)$", "definition", "param")
row(r"\texttt{NtotalOf}\lb\texttt{bounds}", "thm",
    r"$|N_{\mathrm{tot}}-2t_{\max}T\ln2/\pi|\le6\,t_{\max}$", "proved", "param")

# ---------- GeneralGram ----------
row(r"\texttt{gramOf}", "def",
    r"$G_{ij}(X)=\sum_{n\le X}n^{-1-i(f_i-f_j)}$ for $f:\iota\to\R$", "definition", "general")
row(r"\texttt{evalOf}", "def", r"$E_{i,m}=(m+1)^{-1/2-if_i}$, index $\mathrm{Fin}\,\lfloor X\rfloor$", "definition", "general")
row(r"\texttt{evalFin}", "def", r"$E_{i,m}=(m+1)^{-1/2-if_i}$, index $\mathrm{Fin}\,X$ \ ($X:\N$)", "definition", "general")
row(r"\texttt{gramOf}\lb\texttt{eq}\lb\texttt{mul}\lb\texttt{conjTranspose}", "thm", r"$G=E\,E^{\mathsf H}$", "proved", "general")
row(r"\texttt{gramOf}\lb\texttt{nat}\lb\texttt{eq}\lb\texttt{mul}\lb\texttt{conjTranspose}", "thm",
    r"$G=E\,E^{\mathsf H}$ with $E$ indexed by $\mathrm{Fin}\,X$", "proved", "general")
row(r"\texttt{gramOf}\lb\texttt{isHermitian}", "thm", r"$G^{\mathsf H}=G$", "proved", "general")
row(r"\texttt{gramOf}\lb\texttt{posSemidef}", "thm", r"$G\succeq0$", "proved", "general")
row(r"\texttt{gramOf}\lb\texttt{diag}", "thm", r"$G_{ii}=H_{\lfloor X\rfloor}$", "proved", "general")
row(r"\texttt{eigOf}", "def", r"eigenvalues $\lambda_j$ of $G$", "definition", "general")
row(r"\texttt{eigOf}\lb\texttt{nonneg}", "thm", r"$0\le\lambda_j$", "proved", "general")
row(r"\texttt{rank}\lb\texttt{gramOf}\lb\texttt{le}\lb\texttt{rank}\lb\texttt{eval}", "thm", r"$\operatorname{rank}G\le\operatorname{rank}E$", "proved", "general")
row(r"\texttt{rank}\lb\texttt{gramOf}\lb\texttt{le}", "thm", r"$\operatorname{rank}G\le\lfloor X\rfloor$", "proved", "general")
row(r"\texttt{card}\lb\texttt{nonzero}\lb\texttt{eigOf}\lb\texttt{eq}\lb\texttt{rank}", "thm", r"$\#\{\lambda_j\ne0\}=\operatorname{rank}G$", "proved", "general")
row(r"\texttt{zero}\lb\texttt{le}\lb\texttt{sSup}\lb\texttt{clamped}", "thm", r"$0\le\max_j\lambda_j^{+}$ (also for $\iota=\emptyset$)", "proved", "general")
row(r"\texttt{vanishOf}", "def", r"$\#\{j:\lambda_j^{+}\le\delta\max_i\lambda_i^{+}\}$", "definition", "general")
row(r"\texttt{vanishOf}\lb\texttt{ge}", "thm", r"$\#\iota\le N_{\mathrm{van}}(f,X,\delta)+\lfloor X\rfloor$", "proved", "general")
row(r"\texttt{gramMatrix}\lb\texttt{eq}\lb\texttt{gramOf}", "thm", r"$\texttt{gramMatrix}\,T\,X=\texttt{gramOf}\,(\texttt{modeB}\,T)\,X$", "proved", "general")
row(r"\texttt{gramMatrix}\lb\texttt{nat}\lb\texttt{eq}\lb\texttt{mul}\lb\texttt{conjTranspose}", "thm",
    r"$\texttt{gramMatrix}\,T\,X=E\,E^{\mathsf H}$ with $E$ indexed by $\mathrm{Fin}\,X$", "proved", "general")
row(r"\texttt{freqSet}", "def", r"the distinct resonant frequencies", "definition", "general")
row(r"\texttt{card}\lb\texttt{freqSet}", "thm", r"$\#\texttt{freqSet}\,T=N_R(T)$", "proved", "general")
row(r"\texttt{gramFreq}", "def", r"$G$ indexed by $\texttt{freqSet}\,T$ \ ($\#\iota=N_R$)", "definition", "general")
row(r"\texttt{gramFreq}\lb\texttt{eq}\lb\texttt{mul}\lb\texttt{conjTranspose}", "thm", r"$G=E\,E^{\mathsf H}$", "proved", "general")
row(r"\texttt{gramFreq}\lb\texttt{isHermitian}", "thm", r"$G^{\mathsf H}=G$", "proved", "general")
row(r"\texttt{gramFreq}\lb\texttt{posSemidef}", "thm", r"$G\succeq0$", "proved", "general")
row(r"\texttt{rank}\lb\texttt{gramFreq}\lb\texttt{le}", "thm", r"$\operatorname{rank}G\le\lfloor X\rfloor$", "proved", "general")
row(r"\texttt{NvanFreq}", "def", r"$N_{\mathrm{van}}$ of the distinct-frequency matrix", "definition", "general")
row(r"\texttt{eigFreq}\lb\texttt{nonneg}", "thm", r"$0\le\lambda_j$", "proved", "general")
row(r"\texttt{NvanFreq}\lb\texttt{ge}", "thm", r"$N_R(T)\le N_{\mathrm{van}}(F,X,\delta)+\lfloor X\rfloor$ \ ($\delta\ge0$, no hypothesis)", "proved", "general")
row(r"\texttt{NvanFreq}\lb\texttt{sub}\lb\texttt{ge}", "thm", r"$N_{\mathrm{van}}(F,X,\delta)\ge N_R-\lfloor X\rfloor$", "proved", "general")

# ---------- Estimate ----------
row(r"\texttt{cos}\lb\texttt{155}\lb\texttt{ge}", "thm", r"$\cos 1.55\ge 1/50$", "proved", "estimate")
row(r"\texttt{re}\lb\texttt{cpow}\lb\texttt{gram}", "thm",
    r"$\operatorname{Re}(n^{-1-i\theta})=n^{-1}\cos(\theta\log n)$", "proved", "estimate")
row(r"\texttt{re}\lb\texttt{gramOf}", "thm",
    r"$\operatorname{Re}G_{ij}(X)=\sum_{n\le X}n^{-1}\cos((f_i-f_j)\log n)$", "proved", "estimate")
row(r"\texttt{re}\lb\texttt{gramOf}\lb\texttt{ge}", "thm",
    r"$|f_i-f_j|\log X\le1.55\Rightarrow H_{\lfloor X\rfloor}/50\le\operatorname{Re}G_{ij}$", "proved", "estimate")
row(r"\texttt{norm}\lb\texttt{gramOf}\lb\texttt{ge}", "thm",
    r"$|f_i-f_j|\log X\le1.55\Rightarrow H_{\lfloor X\rfloor}/50\le\|G_{ij}\|$", "proved", "estimate")
row(r"\texttt{offRatio}\lb\texttt{ge}\lb\texttt{of}\lb\texttt{close}", "thm",
    r"a close neighbour $\Rightarrow r_j\ge1/50$", "proved", "estimate")
row(r"\texttt{Noff}\lb\texttt{eq}\lb\texttt{card}\lb\texttt{of}\lb\texttt{close}", "thm",
    r"close neighbour for each $j$, $\delta<1/50$ $\Rightarrow N_{\mathrm{off}}=\#\mathrm{modeSet}$", "proved", "estimate")
row(r"\texttt{close}\lb\texttt{iff}\lb\texttt{div}", "thm",
    r"$|b_i-b_j|\log X\le1.55\iff|b_i-b_j|\le1.55/\log X$", "proved", "estimate")

# ---------- Conjectures ----------
row(r"\texttt{etaR}", "def", r"$\eta_R=1-(N_{\mathrm{phase}}+N_{\mathrm{off}}+N_{\mathrm{van}})/N_R$", "definition", "conj")
row(r"\texttt{etaR}\lb\texttt{eq}", "thm", r"$\eta_R=1-(N_{\mathrm{off}}+N_{\mathrm{van}})/N_R$ (uses $N_{\mathrm{phase}}=0$)", "proved", "conj")
row(r"\texttt{Eta}\lb\texttt{Tends}\lb\texttt{ToOne}", "def:Prop",
    r"$\eta_R(T,X(T),\delta(T))\to1$ for $\delta\to0$ \ ($X:\R\to\N$ a parameter)", "not proved", "conj")
row(r"\texttt{Noff}\lb\texttt{LittleO}", "def:Prop", r"$N_{\mathrm{off}}(T,X(T),\delta(T))=o(N_R)$, $X:\R\to\N$ a parameter", "not proved", "conj")
row(r"\texttt{Nvan}\lb\texttt{LittleO}", "def:Prop", r"$N_{\mathrm{van}}(T,X(T),\delta(T))=o(N_R)$, $X:\R\to\N$ a parameter", "not proved", "conj")
row(r"\texttt{Sf}", "def", r"$S_f$ summed over the $b$-grid of sign $\pm1$ and $0<|k|\le K$", "definition", "conj")
row(r"\texttt{Resonance}\lb\texttt{Predicate}", "def", r"$\operatorname{Re}(S_f(n-1)S_f(n+1))<0$", "definition", "conj")
row(r"\texttt{NvanFreq}\lb\texttt{LittleO}", "def:Prop",
    r"$N_{\mathrm{van}}(F,T,X(T),\delta(T))=o(N_R)$, $X:\R\to\N$ a parameter", "not proved", "conj")
row(r"\texttt{Primality}\lb\texttt{Criterion}\lb\texttt{Conjecture}", "def:Prop",
    r"$\operatorname{Re}(S_f(n-1)S_f(n+1))<0\iff n$ prime, for odd $n>3$", "not proved", "conj")

row(r"\texttt{eventually}\lb\texttt{Ntotal}\lb\texttt{pos}", "thm",
    r"$N_{\mathrm{tot}}>0$ eventually", "proved", "necessary")
row(r"\texttt{NvanLittleO}\lb\texttt{.eventually}\lb\texttt{le}\lb\texttt{Ntotal}", "thm",
    r"$N_{\mathrm{van}}=o(N_R)\Rightarrow\forall\varepsilon>0$, eventually $(1-\varepsilon)N_{\mathrm{tot}}\le X$", "proved", "necessary")
row(r"\texttt{NvanLittleO}\lb\texttt{.eventually}\lb\texttt{le}\lb\texttt{NR}", "thm",
    r"same with $N_R$, no hypothesis on collisions", "proved", "necessary")
row(r"\texttt{not}\lb\texttt{NvanLittleO}\lb\texttt{of}\lb\texttt{le}\lb\texttt{Ntotal}", "thm",
    r"$X\le c\,N_{\mathrm{tot}}$, $c<1$ $\Rightarrow$ $\neg N_{\mathrm{van}}=o(N_R)$", "proved", "necessary")
row(r"\texttt{not}\lb\texttt{NvanLittleO}\lb\texttt{of}\lb\texttt{le}\lb\texttt{NR}", "thm",
    r"$X\le c\,N_R$, $c<1$ $\Rightarrow$ $\neg N_{\mathrm{van}}=o(N_R)$, no hypothesis on collisions", "proved", "necessary")
row(r"\texttt{eventually}\lb\texttt{NR}\lb\texttt{pos}", "thm", r"$N_R>0$ eventually", "proved", "necessary")
row(r"\texttt{NvanFreqLittleO}\lb\texttt{.eventually}\lb\texttt{le}\lb\texttt{NR}", "thm",
    r"$N_{\mathrm{van}}(F)=o(N_R)\Rightarrow\forall\varepsilon>0$, eventually $(1-\varepsilon)N_R\le X$", "proved", "necessary")
row(r"\texttt{not}\lb\texttt{NvanFreqLittleO}\lb\texttt{of}\lb\texttt{le}\lb\texttt{NR}", "thm",
    r"$X\le c\,N_R$, $c<1$ $\Rightarrow$ $\neg N_{\mathrm{van}}(F)=o(N_R)$, no collision hypothesis", "proved", "necessary")

titles = {"basic": "\\texttt{FrequencyGrids/Basic.lean} — the characteristic equation and the root $s_2(t)$ (item 1)",
          "encl": "\\texttt{FrequencyGrids/Enclosure.lean} — certified rational enclosures of $s_2(1),\\dots,s_2(10)$",
          "unique": "\\texttt{FrequencyGrids/Uniqueness.lean} — strict monotonicity, uniqueness of $s_2(t)$, certified enclosures",
          "param": "\\texttt{FrequencyGrids/Parametric.lean} — $t_{\\max}$ as a parameter",
          "lattice": "\\texttt{FrequencyGrids/Lattice.lean} — the lattice step and $N_{\\mathrm{phase}}=0$ (item 2)",
          "counting": "\\texttt{FrequencyGrids/Counting.lean} — counting the resonant stratum, $N_R$ (item 3)",
          "structure": "\\texttt{FrequencyGrids/Structure.lean} — collision rigidity (item 3)",
          "resonance": "\\texttt{FrequencyGrids/Resonance.lean} — Gram bound and $b\\mapsto-b$ invariance (items 4, 5)",
          "eigen": "\\texttt{FrequencyGrids/Eigen.lean} — the Gram matrix, its spectrum, $N_{\\mathrm{off}}$, $N_{\\mathrm{van}}$",
          "congruence": "\\texttt{FrequencyGrids/Congruence.lean} — the $6n\\pm1$ filter (item 6)",
          "conj": "\\texttt{FrequencyGrids/Conjectures.lean} — stated, not proved",
          "estimate": "\\texttt{FrequencyGrids/Estimate.lean} — explicit lower bounds for the Gram entries",
          "general": "\\texttt{FrequencyGrids/GeneralGram.lean} — arbitrary frequency families $G=EE^{\\mathsf H}$, and the distinct-frequency lattice ($\\#\\iota=N_R$)",
          "necessary": "\\texttt{FrequencyGrids/Necessary.lean} — the growth of $X$ forced by $N_{\\mathrm{van}}=o(N_R)$"}

out = []
out.append(r"""\footnotesize
\begin{longtable}{@{}p{3.75cm}p{1.52cm}p{8.38cm}p{1.45cm}@{}}
\toprule
\textbf{Declaration} & \textbf{Kind} & \textbf{Statement} & \textbf{Status}\\
\midrule
\endfirsthead
\toprule
\textbf{Declaration} & \textbf{Kind} & \textbf{Statement} & \textbf{Status}\\
\midrule
\endhead
\bottomrule
\endlastfoot
""")
cur = None
for (name, kind, stmt, status, grp) in rows:
    if grp != cur:
        cur = grp
        out.append(r"\multicolumn{4}{@{}p{15.1cm}@{}}{\textit{%s}}\\" % titles[grp])
        out.append(r"\addlinespace[2pt]")
    out.append(r"%s & %s & %s & %s\\" % (name, kind, stmt, status))
out.append(r"\end{longtable}")
tbl = "\n".join(out)

# -*- coding: utf-8 -*-

prose_head = r"""\documentclass[11pt,a4paper]{article}

\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[margin=2.4cm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{booktabs,longtable,array}
\usepackage[colorlinks=true,linkcolor=black,citecolor=black,urlcolor=black]{hyperref}
\usepackage{microtype}
\usepackage{enumitem}
\emergencystretch=1.5em

\newcommand{\R}{\mathbb{R}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\lname}[1]{\texttt{#1}}
\newcommand{\lb}{\_\allowbreak}
\newcommand{\code}[1]{\texttt{#1}}
\newcommand{\itemization}[1]{\begin{itemize}[leftmargin=1.4em,itemsep=1pt,topsep=2pt]#1\end{itemize}}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{conjecture}[theorem]{Conjecture (stated, not proved)}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

\title{Algebraic Frequency Grids, Harmonic Resonances and Primality (vf4)\\[3pt]
\large A Lean~4 / Mathlib formalization of the unconditional part}
\author{\texttt{FrequencyGrids} Lean development\\[2pt]
\small Lean 4.33.1 (\texttt{leanprover/lean4:v4.33.1}) with Mathlib}
\date{\today}

\begin{document}

\maketitle

\begin{abstract}
\noindent
This document reports a formalization, in Lean~4 with Mathlib, of the six unconditional
claims of \emph{Algebraic Frequency Grids, Harmonic Resonances and Primality} (vf4): the
existence of the degree-6 root $s_2(t)$ for the characteristic equation, the exact lattice
step $b(t,k+1,\sigma)-b(t,k,\sigma)=-2\pi/\ln 2$ (hence $N_{\mathrm{phase}}=0$), the $O(T)$
counting of the resonant stratum with the observed slope $200\ln2/\pi\approx44.127$ and the
distinct-versus-total dichotomy $N_R\le N_{\mathrm{tot}}$ (equality iff no collisions), the
off-diagonal Gram bound $|G_{ij}(T)|\le 2/(T|b_i-b_j|)$, the invariance of
$\operatorname{Re}S_f(N,b)$ under $b\mapsto-b$, and the $6n\pm1$ filter with its failing
converse.  The conjectural claims ($\eta_R(T)\to1$, $N_{\mathrm{off}}=o(N_R)$,
$N_{\mathrm{van}}=o(N_R)$, and the primality criterion
$\operatorname{Re}(S_f(n-1)S_f(n+1))<0$) are \emph{stated only}, each as a
\code{def \dots{} : Prop} with no proof; nothing in the development assumes them.  The two
diagnostics they mention, $N_{\mathrm{off}}$ and $N_{\mathrm{van}}$, are the paper's own
concrete objects (\S\ref{sec:eigen}): the off-diagonal Gram interference and the count of
clamped eigenvalues of the Gram matrix of the resonant modes below the relative threshold
$\delta_T$.  Implementing them faithfully has a consequence worth stating up front: at the
paper's own parameters those two counts are \emph{not} small compared with $N_R$
(\S\ref{sec:eigen-num}), so the experiments of vf4 \S6.4.8 do not support the conjectures
they are meant to support.  Making the diagnostics concrete also settles what the conjecture
\emph{demands}: $G=E E^{\mathsf H}$ is positive semidefinite of rank at most $X$, so at least
$\#\mathrm{modeSet}(T)-X$ modes have zero eigenvalue and are counted by $N_{\mathrm{van}}$.
Hence $N_{\mathrm{van}}=o(N_R)$ forces $X(T)\ge(1-\varepsilon)N_{\mathrm{tot}}(T)$ for every
$\varepsilon>0$, and any truncation with $X\le c\,N_R$, $c<1$, refutes the conjecture
(\S\ref{sec:necessary}).  The factorisation is proved for an \emph{arbitrary} frequency family
$f:\iota\to\R$ (\S\ref{sec:eigen-general}), which yields two instances: the triplet-indexed
matrix of the construction, and the matrix indexed by the \emph{distinct} resonant frequencies,
whose index type has cardinality $N_R(T)$.  For the latter the bound
$N_{\mathrm{van}}\ge N_R-\lfloor X\rfloor$ holds unconditionally, so the refutation needs no
hypothesis on collisions.

Two discrepancies with the paper's numerics are proved or checked and reported in
\S\ref{sec:item1} and \S\ref{sec:item3}: (i) the bracketing interval
$(-0.9999,-0.0001)$ carries a sign change only for $1\le t\le 589$ and loses it from
$t=590$ onward --- the root exists for all $t\ge1$ but leaves the interval; (ii) the value
$s_2=-0.99941091795$ hard-coded in vf4 \S7.3--7.4 is the root at $t=100$, not at $t=1$.
The development is \code{sorry}-free and depends only on the three standard axioms
\code{propext}, \code{Classical.choice}, \code{Quot.sound}.
\end{abstract}

\tableofcontents

\section{Scope and result}

\subsection*{What is formalized}

\code{FrequencyGrids} is a self-contained Lean~4 development on top of Mathlib.  It has no
project-specific axioms and no \code{sorry}.  The six items of the task map onto the files
as follows.

\itemization{
\item \textbf{Item 1} (\code{FrequencyGrids/Basic.lean}). The characteristic equation
  \[
    E(s,k_3)=\bigl|8s^6-24s^4+24s^2-8\bigr|^{2/3}\bigl(24k_3^2s^6-72k_3^2s^4-24k_3^2\bigr)+4s^4
  \]
  is shown to be a \emph{polynomial} in $s$ (the fractional power cancels a perfect cube),
  whence its continuity and a real root $s_2(t)\in(-1,0)$ of $E(\cdot,-t)$ for every $t\ge1$;
  the narrow interval $(-0.9999,-0.0001)$ of the paper's \code{brentq} call is analysed
  exactly, with the sign change verified for $1\le t\le589$ and proved to fail for
  $t\ge590$.
\item \textbf{Item 2} (\code{FrequencyGrids/Lattice.lean}). The $b$-lattice has constant step
  $-2\pi/\ln2$ independent of $t,k,\sigma$, the map $k\mapsto b(t,k,\sigma)$ is strictly
  antitone (hence injective), and the phase defect vanishes identically, so that
  $N_{\mathrm{phase}}=0$ for \emph{every} truncation.
\item \textbf{Item 3} (\code{FrequencyGrids/Counting.lean},
  \code{FrequencyGrids/Structure.lean}). A finite set of integers in a real interval
  $[a,b]$ has at most $b-a+1$ elements and, if it contains all of $[a,b]\cap\Z$, at least
  $b-a-2$; this gives
  $\bigl|\#\{k\neq0:|b(t,k,\sigma)|\le T\}-T\ln2/\pi\bigr|\le3$ for each of the $200$
  lattices and hence $\bigl|N_{\mathrm{tot}}(T)-200\,T\ln2/\pi\bigr|\le600$.  The distinct
  count satisfies $N_R\le N_{\mathrm{tot}}$, with equality exactly when there is no
  collision, and collisions themselves are rigid: they force equal sign, equal index and
  equal $|s_2|$.
\item \textbf{Item 4} (\code{FrequencyGrids/Resonance.lean}). The Gram coefficient
  $G_{12}(T)$ is defined as in vf4 \S6.5.2.1 and shown to satisfy
  $|G_{12}(T)|\le2/(T|b_1-b_2|)$ for $b_1\neq b_2$, $T>0$.
\item \textbf{Item 5} (\code{FrequencyGrids/Resonance.lean}). $\overline{S_f(N,b)}=S_f(N,-b)$
  for the partial harmonic sums $S_f(N,b)=\sum_{m\le N}m^{-(1/2+ib)}$, hence
  $\operatorname{Re}S_f(N,\cdot)$ is even.
\item \textbf{Item 6} (\code{FrequencyGrids/Congruence.lean}). Every prime $p>3$ is
  $\equiv\pm1\pmod 6$, the converse fails at $25$, and the filter is therefore not a
  primality test.
\item \textbf{The diagnostics} (\code{FrequencyGrids/Eigen.lean}). The Gram matrix of the
  resonant modes, its spectrum, the relative interference $r_j$ and the counts
  $N_{\mathrm{off}}$, $N_{\mathrm{van}}$ are the paper's own objects; $G=E E^{\mathsf H}$ is
  proved, whence positive semidefiniteness, nonnegative eigenvalues, the identity
  $\max(\lambda,0)=\lambda$, the rank bound $\operatorname{rank}G\le\operatorname{rank}E\le
  \lfloor X\rfloor$, the diagonal $G_{ii}=H_{\lfloor X\rfloor}$, and
  $N_{\mathrm{van}}\ge N_{\mathrm{tot}}-\lfloor X\rfloor$ (\S\ref{sec:eigen-factor}).
\item \textbf{The general family} (\code{FrequencyGrids/GeneralGram.lean}). The same is proved
  for an arbitrary finite frequency family $f:\iota\to\R$, with $E$ indexed either by
  $\mathrm{Fin}\,\lfloor X\rfloor$ (real cutoff) or by $\mathrm{Fin}\,X$ (natural cutoff).
  Instantiating at the \emph{distinct} resonant frequencies --- an index type of cardinality
  $N_R(T)$ --- gives $N_{\mathrm{van}}(F)\ge N_R-\lfloor X\rfloor$ with no collision
  hypothesis (\S\ref{sec:eigen-general}).
\item \textbf{The truncation} (\code{FrequencyGrids/Necessary.lean}). With $X$ a parameter of
  the conjecture, $N_{\mathrm{van}}=o(N_R)$ implies $X(T)\ge(1-\varepsilon)N_{\mathrm{tot}}(T)$
  eventually for every $\varepsilon>0$, so a truncation with $X\le c\,N_R$, $c<1$, refutes it
  (\S\ref{sec:necessary}).
}

\subsection*{What is not formalized, and why}

\itemization{
\item The conjectures $\eta_R\to1$, $N_{\mathrm{off}}=o(N_R)$,
  $N_{\mathrm{van}}=o(N_R)$ and the primality criterion are \code{def \dots{} : Prop} in
  \code{FrequencyGrids/Conjectures.lean}.  No theorem in the development mentions them;
  \code{\#print axioms} on those declarations returns nothing but the three standard
  axioms, because there is nothing to check.
\item $N_{\mathrm{off}}$ and $N_{\mathrm{van}}$ are now the paper's own diagnostics
  (\S\ref{sec:eigen}): the Gram matrix of the resonant modes, its eigenvalues via the
  spectral theorem for Hermitian matrices, the relative interference $r_j(X)$ and the
  relative eigenvalue threshold $\delta_T\max_j\lambda_j$.  The one idealisation left is
  numerical: the eigenvalues are exact real numbers (Mathlib's spectral theorem) where the
  paper uses floating point.  The factorisation $G=EE^{\mathsf H}$, the positive
  semidefiniteness, the identity $\max(\lambda_j,0)=\lambda_j$ and the rank bound
  $\operatorname{rank}G\le X$ are all proved (\S\ref{sec:eigen-factor}).
\item The numerical statement $N_{\mathrm{off}}=\#\mathrm{modeSet}$ at the parameters of
  vf4 \S6.4.8 is \emph{not} proved.  The reduction to what would suffice is formalized
  (\code{Noff\lb eq\lb card\lb of\lb gram\lb gt}); \S\ref{sec:eigen-num} reports the two
  obstructions.
\item The integral representation $G_{ij}(T)=\frac1T\int_0^Te^{i(b_i-b_j)t}\,dt$ is quoted in
  the paper as the \emph{definition} of $G_{ij}$; we take its closed form as the definition
  and prove the bound.  The equality of the two was not formalized.
\item The deduction ``$N_{\mathrm{phase}},N_{\mathrm{off}},N_{\mathrm{van}}=o(N_R)$
  $\Rightarrow$ $\eta_R\to1$'' is elementary but is not formalized: it would be a theorem
  about the conjectures' \emph{consequences}, and stating it without the conjectures risks
  reading as a proof of them.
\item Uniqueness of the root $s_2(t)$, and injectivity of $t\mapsto|s_2(t)|$, are not
  proved.  Only existence (in $(-1,0)$, and in $(-0.9999,-0.0001)$ for $t\le589$) is.
}

\section{Setting: making the equation algebraic}\label{sec:setup}

The single most useful observation for the whole development is that the degree-6
polynomial of vf4 \S5.1 is a perfect cube:
\begin{equation}\label{eq:cube}
  8s^6-24s^4+24s^2-8 \;=\; 8\,(s^2-1)^3 .
\end{equation}
Since $|8v^3|^{2/3}=4v^2$ for real $v$ (\code{abs\lb cube\lb rpow}), the awkward
$2/3$-power in $E$ is a polynomial after all.

\begin{theorem}[\code{E\lb eq}]\label{thm:Eeq}
For all $s,k_3\in\R$,
\[
  E(s,k_3) \;=\; 4\Bigl(s^4+24\,k_3^2\,(s^2-1)^2\,(s^6-3s^4-1)\Bigr),
\]
and equivalently, with $u=s^2$ and $g(u)=3u^2-u^3+1$,
\[
  E(s,k_3) \;=\; 4\Bigl(s^4-24\,k_3^2\,(s^2-1)^2\,(3s^4-s^6+1)\Bigr)
  \;=\; 4\bigl(u^2-24\,k_3^2\,(1-u)^2 g(u)\bigr).
\]
\end{theorem}

Everything about signs of $E$ is therefore rational arithmetic in $s$ and $k_3^2$, and
$E(\cdot,k_3)$ is continuous (\code{continuous\lb E}, proved by rewriting with
Theorem~\ref{thm:Eeq} and \code{fun\lb prop}).  In particular the paper's transcendental
looking equation hides no transcendental behaviour: $k_3$ enters only through $k_3^2$.

\section{Item 1: the root $s_2(t)$}\label{sec:item1}

\subsection{Existence in $(-1,0)$}

\begin{theorem}[\code{exists\lb root\lb unit}]
For every $k_3\neq0$ there is $s\in(-1,0)$ with $E(s,k_3)=0$.
\end{theorem}
\begin{proof}
By Theorem~\ref{thm:Eeq}, $E(-1,k_3)=4>0$ (\code{E\lb neg\lb one}) and
$E(0,k_3)=-96k_3^2<0$ (\code{E\lb zero}).  Continuity on $[-1,0]$ and the intermediate
value theorem (\code{intermediate\lb value\lb Ioo'}, the decreasing-orientation form) give a
zero in the open interval.
\end{proof}

This is unconditional in $t$: the root the paper's \code{brentq} looks for exists for every
$t\ge1$, indeed for every real $k_3\neq0$.

\subsection{The narrow interval of the paper, exactly}

Write $u=s^2$, $u_0=(0.9999)^2=99980001/10^8$, $u_1=(10^{-4})^2=10^{-8}$, and
$g(u)=3u^2-u^3+1>0$ on $(0,1)$.  By Theorem~\ref{thm:Eeq},
\[
  E(s,k_3)>0 \iff u^2>24\,k_3^2(1-u)^2 g(u).
\]
At the two endpoints of the paper's bracket:
\itemization{
\item $s=-10^{-4}$: $u=10^{-8}$, so the left side of the criterion is $10^{-16}$ while the
  right side is at least $24\,t^2\,(1-10^{-8})^2\cdot 1$, which exceeds $10^{-16}$ for every
  $t\ge1$.  Hence $E(-10^{-4},-t)<0$ for all $t\ge1$ (\code{E\lb right\lb neg}).
\item $s=-0.9999$: the inequality is $t^2 < u_0^2/(24(1-u_0)^2g(u_0))$, and the right-hand
  side equals $347\,187.6\ldots$, whose square root is $589.2261\ldots$ .  Since $g$ and
  $u\mapsto u/(1-u)$ are increasing, the criterion is monotone in $t^2$, so
  $E(-0.9999,-t)>0$ holds exactly for $t\le589$: \code{E\lb left\lb pos} for $t\le589$
  and \code{E\lb left\lb neg} for $t\ge590$.
}
Consequently:

\begin{theorem}[\code{exists\lb root\lb grid}, \code{s2\lb spec}]
For every integer $t$ with $1\le t\le589$ there is $s\in(-0.9999,-0.0001)$ with
$E(s,-t)=0$; the root selector \code{s2} returns such an $s$ and satisfies
$E(s_2(t),-t)=0$ and $|s_2(t)|<1$.
\end{theorem}

\begin{remark}[The reported failure]\label{rem:failure}
The paper's prose asserts the root lies in $(-0.9999,-0.0001)$ for all $t\ge1$
(\S7.2, \S6.5.2.1).  As a statement about the \emph{bracketing interval} this is false from
$t=590$ on: both endpoint values are then negative, so \code{brentq} on
$[-0.9999,-0.0001]$ has no sign change to work with.  This is
\code{E\lb left\lb neg}; the endpoint values are
\[
  E(-0.9999,-589)=0.0030691\ldots>0,\qquad E(-0.9999,-590)=-0.0105088\ldots<0 .
\]
The mechanism is transparent: the root satisfies $1-u\approx(24\,t^2g(u))^{-1/2}$, so it
drifts to $s=-1$ like $1-\frac{1}{4.9\,t}$ and leaves $(0.9999,1)$ in modulus at
$t\approx589.23$.  A bisection check over $t=590,\dots,2000$ finds no zero of
$E(\cdot,-t)$ in the interval at all, and the monotonicity of $u\mapsto u^2/((1-u)^2g(u))$
on $(0,1)$ (log-derivative $2/(u(1-u))-(6u-3u^2)/g>0$) proves the same on paper; only the
failure of the \emph{sign change} is formalized.

None of this affects the paper's computations, which use $t\le t_{\max}=100$; the theorem
above covers $1\le t\le589$ and hence the entire computational range with a factor $5.9$ of
margin.
\end{remark}

\begin{remark}[A numerical discrepancy in vf4 \S7.3--7.4]\label{rem:s2value}
The examples of vf4 \S7.3 and \S7.4 set \code{t = 1} but hard-code
\code{s2 = -0.99941091795}.  That value is the root at $t=100$:
$s_2(100)=-0.999410917960\ldots$, whereas $s_2(1)=-0.942823289665\ldots$ .  The hard-coded
number is therefore inconsistent with the stated \code{t}; all quantitative statements in
those two examples are unaffected only if one reads them at $t=100$.
\end{remark}

\begin{table}[h]
\centering
\small
\begin{tabular}{rrrr}
\toprule
$t$ & $E(-0.9999,-t)$ & $E(-10^{-4},-t)$ & root $s_2(t)$ (bisection, 30 digits)\\
\midrule
$1$ & $3.99839$ & $-95.999998$ & $-0.94282328966545949605$\\
$10$ & $3.99725$ & $-9599.99981$ & $-0.99412480603916912785$\\
$100$ & $3.88323$ & $-959999.98$ & $-0.99941091796026781277$\\
$589$ & $0.00307$ & $-3.3304\cdot10^{7}$ & $-0.9998999616\ldots$\\
$590$ & $-0.01051$ & $-3.3418\cdot10^{7}$ & none in $(-0.9999,-10^{-4})$\\
\bottomrule
\end{tabular}
\caption{The sign change of the paper's bracket.  Left endpoint positive up to $t=589$,
negative from $t=590$; right endpoint always negative.}\label{tab:signs}
\end{table}

\section{Item 2: the lattice step and $N_{\mathrm{phase}}=0$}\label{sec:item2}

\begin{theorem}[\code{b\lb eq\lb affine}, \code{b\lb step}, \code{b\lb step\lb uniform}]
For all $t\in\N$, $k\in\Z$ and $\sigma\in\R$,
\[
  b(t,k,\sigma)=\frac{\arcsin(\sigma|s_2(t)|)}{\ln2}-\frac{2\pi}{\ln2}\,k,
  \qquad
  b(t,k+1,\sigma)-b(t,k,\sigma)=-\frac{2\pi}{\ln2},
\]
and the right-hand step is the same for all $t,t',k,k',\sigma,\sigma'$.
\end{theorem}

\begin{theorem}[\code{b\lb strict\lb Anti}, \code{b\lb injective}]
For fixed $t,\sigma$ the map $k\mapsto b(t,k,\sigma)$ is strictly antitone, hence
injective.
\end{theorem}
\begin{proof}
By the affine form the map is $k\mapsto c-\lambda k$ with $\lambda=2\pi/\ln2>0$.
\end{proof}

The phase defect is $\delta b_{t,k,\sigma}=b(t,k+1,\sigma)-b(t,k,\sigma)+2\pi/\ln2$; it is
zero by the previous theorem, so the paper's $N_{\mathrm{phase}}$ vanishes identically:

\begin{theorem}[\code{phase\lb Defect\lb eq\lb zero}, \code{Nphase\lb eq\lb zero}]
$\delta b_{t,k,\sigma}=0$ for all $t,k,\sigma$, and for every finite set $S$ of triplets the
count $N_{\mathrm{phase}}(S)=\#\{(t,k,\sigma)\in S:\delta b_{t,k,\sigma}\neq0\}$ is $0$.
\end{theorem}

\section{Item 3: counting the resonant stratum}\label{sec:item3}

\subsection{Two elementary counting lemmas}

Both are statements about finite sets of \emph{integers} in a real interval, and both are
proved from \code{Int.card\lb Icc} plus the floor/ceiling estimates
$\lfloor b\rfloor\le b<\lfloor b\rfloor+1$ and $\lceil a\rceil-1<a\le\lceil a\rceil$.

\begin{lemma}[\code{card\lb le\lb of\lb forall\lb mem\lb Icc}]
If $S\subseteq\Z$ is finite and $S\subseteq[a,b]$, then $\#S\le b-a+1$.
\end{lemma}
\begin{lemma}[\code{le\lb card\lb of\lb forall\lb Icc\lb mem}]
If $S\subseteq\Z$ is finite and contains every integer of $[a,b]$, then $\#S\ge b-a-2$.
\end{lemma}

\subsection{One lattice}

For a phase $\alpha$ put $b_\alpha(k)=(\alpha-2k\pi)/\ln2$ and
\[
  k_{\mathrm{lo}}=\frac{\alpha-T\ln2}{2\pi},\qquad
  k_{\mathrm{hi}}=\frac{\alpha+T\ln2}{2\pi},\qquad
  k_{\mathrm{hi}}-k_{\mathrm{lo}}=\frac{T\ln2}{\pi}.
\]
The index set is \code{kSet}$(\alpha,T)=\{k\in\Z:\lceil k_{\mathrm{lo}}\rceil\le k\le
\lfloor k_{\mathrm{hi}}\rfloor,\ k\neq0\}$, and \code{mem\lb Icc\lb iff\lb abs\lb bOf}
records the exact equivalence $k_{\mathrm{lo}}\le k\le k_{\mathrm{hi}}\iff|b_\alpha(k)|\le
T$ (no side condition on $T$, only $\ln2>0$, $\pi>0$).

\begin{theorem}[\code{card\lb kSet\lb bounds}]\label{thm:kSet}
For every phase $\alpha$ and $T\ge0$,
\[
  \Bigl|\#\{k\neq0:\ |b_\alpha(k)|\le T\}-\frac{T\ln2}{\pi}\Bigr|\le3 .
\]
\end{theorem}
\begin{proof}
Upper bound from Lemma~1 applied to $k_{Set}\subseteq[k_{lo},k_{hi}]$; lower bound from
Lemma~2 applied to $\{0\}\cup k_{Set}$, which contains all of $[k_{lo},k_{hi}]\cap\Z$, and
$\#(\{0\}\cup k_{Set})\le\#k_{Set}+1$.  The constant $3$ absorbs the floor, the ceiling and
the excluded index $k=0$.
\end{proof}

\subsection{The $200$ lattices and the slope}

The family is $1\le t\le100$, $\sigma\in\{-1,1\}$, i.e. $200$ lattices
(\code{card\lb latticeSet}).  The triplet set \code{modeSet}$(T)$ and the two counts
\[
  N_{\mathrm{tot}}(T)=\#\mathrm{modeSet}(T),\qquad
  N_R(T)=\#\{b(t,k,\sigma):(t,k,\sigma)\in \mathrm{modeSet}(T)\}
\]
are defined exactly as in vf4 \S6.4.2.

\begin{theorem}[\code{Ntotal\lb bounds}]
For $T\ge0$, $\bigl|N_{\mathrm{tot}}(T)-200\,T\ln2/\pi\bigr|\le600$.
\end{theorem}
\begin{theorem}[\code{slope\lb bounds}, \code{Ntotal\lb approx}, \code{NR\lb le\lb slope}]
$44.12<200\ln2/\pi<44.14$; for $T\ge0$,
\[
  \bigl|N_{\mathrm{tot}}(T)-44.13\,T\bigr|\le600+\tfrac{T}{100},
  \qquad
  N_R(T)\le44.14\,T+600 .
\]
\end{theorem}

The numerical constants are the standard rational enclosures
$3.141592<\pi<3.141593$ and $0.6931471803<\ln2<0.6931471808$.

\subsection{Distinct count versus mode count}

\begin{theorem}[\code{NR\lb le\lb Ntotal}, \code{NR\lb eq\lb Ntotal\lb iff}]
$N_R(T)\le N_{\mathrm{tot}}(T)$ for every $T$, and
\[
  N_R(T)=N_{\mathrm{tot}}(T)\iff \text{no two distinct triplets of } \mathrm{modeSet}(T)
  \text{ have the same } b .
\]
\end{theorem}
\begin{proof}
$\mathrm{modeSet}(T)$ is finite; $N_R$ is the cardinality of its image under
$(t,k,\sigma)\mapsto b(t,k,\sigma)$, so this is \code{Finset.card\lb image\lb le} and
\code{Finset.card\lb image\lb iff} (equality iff the map is injective on the set).
\end{proof}

The interesting point is that the lattice itself cannot collide.  Formalizing this makes
the equality criterion informative rather than vacuous.

\begin{theorem}[\code{b\lb collision\lb structure}, \code{collision\lb imp\lb duplicate\lb phase}]
Suppose $1\le t,t'\le589$, $\sigma,\sigma'\in\{-1,1\}$ and
$b(t,k,\sigma)=b(t',k',\sigma')$.  Then
\[
  \sigma=\sigma',\qquad |s_2(t)|=|s_2(t')|,\qquad k=k' .
\]
In particular a collision in \code{modeSet}$(T)$ forces two distinct $t\neq t'$ with
$|s_2(t)|=|s_2(t')|$.
\end{theorem}
\begin{proof}
Multiplying the equality by $\ln2$ and using the affine form,
$\arcsin(\sigma|s_2 t|)-\arcsin(\sigma'|s_2 t'|)=2\pi(k-k')$.  Each arcsine lies in
$[-\pi/2,\pi/2]$, so the left side has modulus at most $\pi$; hence
$|k-k'|\le1/2$, and as $k-k'\in\Z$ we get $k=k'$.  Then the two arcsines are equal, and
$\arcsin$ is injective on $[-1,1]$, so $\sigma|s_2t|=\sigma'|s_2 t'|$; as
$|s_2|>0$ (\code{s2\lb abs\lb pos}) and $\sigma,\sigma'=\pm1$, this forces
$\sigma=\sigma'$ and $|s_2t|=|s_2t'|$.
\end{proof}

\begin{remark}[Reproducing the paper's table]
Evaluating the definitions of this section with the true roots $s_2(t)$ reproduces vf4
\S6.4.3 exactly, and with \emph{zero} collisions, so that $N_R=N_{\mathrm{tot}}$ there:
\[
\begin{array}{r|rrrrr}
T & 100 & 500 & 1000 & 5000 & 10000\\\hline
N_{\mathrm{tot}}=N_R & 4200 & 21800 & 44000 & 220400 & 441000\\
N_R/T & 42.0 & 43.6 & 44.0 & 44.08 & 44.10
\end{array}
\]
The two smallest rows are below the asymptotic constant $44.127$ because of the $O(1)$
correction of Theorem~\ref{thm:kSet}, not because of a modelling difference.  The paper
de-duplicates by \code{round(b,12)}; we use exact equality of real numbers.  Since the
lattice is collision-free by the rigidity theorem, the two agree here.
\end{remark}

\section{Item 4: the off-diagonal Gram bound}\label{sec:item4}

The Gram coefficient of vf4 \S6.5.2.1 is defined as
\[
  G_{12}(T)=\begin{cases}1,& b_1=b_2,\\[2pt]
  \dfrac{e^{i(b_1-b_2)T}-1}{i(b_1-b_2)T},& b_1\neq b_2.\end{cases}
\]

\begin{theorem}[\code{gramCoeff\lb offdiag\lb bound}]
For $b_1\neq b_2$ and $T>0$,
\[
  |G_{12}(T)|\ \le\ \frac{2}{T\,|b_1-b_2|}.
\]
\end{theorem}
\begin{proof}
$\|e^{i\theta}-1\|\le\|e^{i\theta}\|+1=2$ (\code{norm\lb exp\lb I\lb sub\lb one\lb le\lb two},
from $\|e^{i\theta}\|=1$), and $\|i\theta\|=|\theta|=T|b_1-b_2|$; divide.
\end{proof}

\begin{remark}
The diagonal case is $G_{11}(T)=1$ (\code{gramCoeff\lb self}).  The bound is the paper's
Lemma~2 and is what makes the off-diagonal terms summable in $1/(T\delta_X)$; we do not
formalize the summation, only the estimate, as requested.
\end{remark}

\section{Item 5: invariance of $\operatorname{Re}S_f$ under $b\mapsto-b$}\label{sec:item5}

For $N\ge1$ and real $b$ let
\[
  S_f(N,b)=\sum_{m=1}^{N} m^{-(1/2+ib)},
\]
formalized as \code{hsum} with the complex power \code{Complex.cpow} on the natural cast
$m\mapsto(m:\C)$; the summand is \code{hterm m b}.

\begin{theorem}[\code{hterm\lb conj}, \code{hsum\lb conj}, \code{hsum\lb re\lb even}]
For all $N\ge1$ and $b\in\R$,
\[
  \overline{S_f(N,b)}=S_f(N,-b),
  \qquad\text{hence}\qquad
  \operatorname{Re}S_f(N,-b)=\operatorname{Re}S_f(N,b).
\]
\end{theorem}
\begin{proof}
$\overline{m^{z}}=m^{\bar z}$ for the positive real $m$, because conjugation is continuous
and fixes $m$ (\code{Complex.cpow\lb conj}, applicable since $\arg(m:\C)=0\neq\pi$);
$\overline{1/2+ib}=1/2-ib$; sum over $m\le N$ using that conjugation is an additive map.
\end{proof}

The consequence is the one the paper uses when it treats $\sigma=\pm1$ symmetrically: the
sign parameter only reflects the grid, and the real part of the partial sums cannot
distinguish $b$ from $-b$.

\section{Item 6: the $6n\pm1$ filter}\label{sec:item6}

\begin{theorem}[\code{prime\lb mod\lb six}, \code{prime\lb zmod\lb six}]
If $p$ is prime and $p>3$, then $p\equiv1$ or $p\equiv5\pmod 6$; equivalently the class of
$p$ in $\Z/6$ is $1$ or $5$.
\end{theorem}
\begin{proof}
$p$ is odd, so $2\nmid p$, and $3\nmid p$; hence $p\bmod6\notin\{0,2,3,4\}$ (each of those
residues is divisible by $2$ or by $3$), leaving $1$ or $5$ among $0,\dots,5$.  In Lean:
\code{Nat.Prime.eq\lb one\lb or\lb self\lb of\lb dvd} converts $2\mid p$ and $3\mid p$ into
$p=2$ resp. $p=3$, contradicting $p>3$; \code{omega} then finishes.
\end{proof}

\begin{theorem}[\code{converse\lb fails}, \code{filter\lb not\lb sufficient}]
$25\equiv1\pmod6$ and $25$ is not prime; thus the filter alone is not a primality test.
\end{theorem}


\section{The Gram matrix, $N_{\mathrm{off}}$ and $N_{\mathrm{van}}$}\label{sec:eigen}

vf4 \S6.4.4--6.4.8 defines the two spectral diagnostics numerically, from the Gram matrix of
the resonant modes.  \code{FrequencyGrids/Eigen.lean} formalizes exactly those objects.

\subsection*{The matrix}

The modes are the triplets of \code{modeSet}$(T)$ (\S\ref{sec:item3}); since collisions are
rigid (Theorem 5.7), distinct triplets carry distinct frequencies, so indexing by triplets
and by distinct frequencies agree.  Write $b_i$ for the frequency of the mode $i$
(\code{modeB}).

\begin{definition}[\code{gramMatrix}]
\[
  G_{ij}(X)=\sum_{n\le X} n^{-1-i(b_i-b_j)},\qquad i,j\in\mathrm{modeSet}(T),
\]
as a matrix over $\C$ indexed by the (finite) triplet set; the sum runs over
$1\le n\le\lfloor X\rfloor$.
\end{definition}

\begin{theorem}[\code{gramMatrix\lb isHermitian}]\label{thm:herm}
$G(X)^{\mathsf H}=G(X)$.  Hence the symmetrisation $(G+G^{\mathsf H})/2$ of the code is the
identity on $G$.
\end{theorem}
\begin{proof}
$\overline{G_{ji}}=\sum_n\overline{n^{-1-i(b_j-b_i)}}=\sum_n n^{-1+i(b_j-b_i)}
=\sum_n n^{-1-i(b_i-b_j)}=G_{ij}$, using $\overline{m^{w}}=m^{\bar w}$ for $m\in\N$
(\code{cpow\lb conj\lb natCast}, from \code{Complex.cpow\lb conj} with
$\arg(m)=0\ne\pi$) and $\overline{-1-i(x-y)}=-1-i(y-x)$.
\end{proof}

\subsection*{The spectrum}

\begin{definition}[\code{eig}, \code{eigPos}, \code{eigMax}]
$\lambda_j$ are the eigenvalues of the Hermitian matrix $G(X)$ given by the spectral theorem
(\code{Matrix.IsHermitian.eigenvalues}), hence real; $\lambda_j^{+}=\max(\lambda_j,0)$ is
the clamped eigenvalue, exactly \code{np.maximum(eigenvalues, 0)} of vf4 \S6.4.7; and
$\max_j\lambda_j^{+}$ is the supremum of the range, with $\sup\emptyset=0$ matching the
code's empty-matrix branch.
\end{definition}

\begin{remark}
The clamp is the code's protective maximum, and it is now \emph{proved} to be the identity:
Theorem~\ref{thm:posSemidef} below factors $G=E E^{\mathsf H}$, so the eigenvalues are
nonnegative and $\max(\lambda_j,0)=\lambda_j$ (\code{eigPos\lb eq\lb eig}).  The definition
keeps the maximum, but it never fires.
\end{remark}

\subsection*{The two counts}

\begin{definition}[\code{offSum}, \code{offRatio}, \code{Noff}]
$I_j(X)=\sum_{i\ne j}|G_{ij}(X)|$, $r_j(X)=I_j(X)/|G_{jj}(X)|$, and
\[
  N_{\mathrm{off}}(T,X,\delta_X)=\#\{j:\ r_j(X)>\delta_X\}.
\]
(As $G$ is Hermitian, $|G_{ij}|=|G_{ji}|$, so the orientation of the sum is immaterial.)
\end{definition}

\begin{definition}[\code{Nvan}]
\[
  N_{\mathrm{van}}(T,X,\delta_T)=\#\{j:\ \lambda_j^{+}\le\delta_T\cdot\max_i\lambda_i^{+}\}.
\]
\end{definition}

\begin{theorem}[\code{Noff\lb le\lb Ntotal}, \code{Nvan\lb le\lb Ntotal}]
Both counts are at most the number of modes: $N_{\mathrm{off}}(T,X,\delta)\le N_{\mathrm{tot}}(T)$
and $N_{\mathrm{van}}(T,X,\delta)\le N_{\mathrm{tot}}(T)$.  Moreover
$\lambda_j^{+}\le\max_i\lambda_i^{+}$ for every $j$, and the threshold is nonnegative when
there is at least one mode (\code{eigPos\lb le\lb eigMax}, \code{eigMax\lb nonneg}).
\end{theorem}

\begin{theorem}[\code{etaR\lb eq}]
With these definitions and the proved $N_{\mathrm{phase}}=0$,
\[
  \eta_R(T,X,\delta)=1-\frac{N_{\mathrm{off}}(T,X,\delta)+N_{\mathrm{van}}(T,X,\delta)}{N_R(T)} .
\]
\end{theorem}

\subsection{The factorisation, the spectrum and the rank}\label{sec:eigen-factor}

\begin{definition}[\code{gramE}]
$E:\ \mathrm{modeSet}(T)\times\{0,\dots,\lfloor X\rfloor-1\}\to\C$, \quad
$E_{i,m}=(m+1)^{-1/2-i\,b_i}$.
\end{definition}

\begin{theorem}[\code{gramMatrix\lb eq\lb mul\lb conjTranspose}]\label{thm:EEH}
$G(X)=E\,E^{\mathsf H}$; that is, $G_{ij}(X)=\sum_{m<\lfloor X\rfloor}E_{i,m}\overline{E_{j,m}}$.
\end{theorem}
\begin{proof}
$E_{i,m}\overline{E_{j,m}}=n^{-1/2-ib_i}n^{-1/2+ib_j}=n^{-1-i(b_i-b_j)}$ with $n=m+1$, using
$\overline{n^{w}}=n^{\bar w}$ and $n^{a}n^{b}=n^{a+b}$ for $n\ne0$.
\end{proof}

\begin{theorem}[\code{gramMatrix\lb posSemidef}, \code{eig\lb nonneg}, \code{eigPos\lb eq\lb eig},
\code{rank\lb gramMatrix\lb le}]\label{thm:posSemidef}
$G(X)$ is positive semidefinite; every eigenvalue is $\ge0$; the clamp is the identity; and
$\operatorname{rank}G(X)\le\lfloor X\rfloor$.
\end{theorem}
\begin{proof}
$EE^{\mathsf H}\succeq0$ (\code{Matrix.posSemidef\lb self\lb mul\lb conjTranspose}), and
$\operatorname{rank}(EE^{\mathsf H})\le\operatorname{rank}E\le\lfloor X\rfloor$ since $E$ has
$\lfloor X\rfloor$ columns.  Eigenvalues are those of the Hermitian matrix, so the
nonnegativity is \code{PosSemidef.eigenvalues\lb nonneg} --- transported along proof
irrelevance of the hermitianity witness, since the eigenvalue map has a proof-independent
value type.
\end{proof}

\begin{theorem}[\code{card\lb nonzero\lb eig\lb eq\lb rank}]
The number of nonzero eigenvalues is the rank: $\#\{j:\lambda_j\ne0\}=\operatorname{rank}G(X)$.
Equivalently, the zero eigenvalues number exactly $\#\mathrm{modeSet}(T)-\operatorname{rank}G(X)$.
\end{theorem}

\begin{theorem}[\code{card\lb le\lb Nvan\lb add}, \code{Ntotal\lb sub\lb le\lb Nvan},
\code{NR\lb sub\lb le\lb Nvan}]\label{thm:Nvanrank}
For every $\delta\ge0$,
\[
  \#\mathrm{modeSet}(T)\ \le\ N_{\mathrm{van}}(T,X,\delta)+\lfloor X\rfloor,
  \qquad\text{i.e.}\qquad
  N_{\mathrm{van}}(T,X,\delta)\ \ge\ N_{\mathrm{tot}}(T)-\lfloor X\rfloor .
\]
The same holds with $N_R$ in place of $N_{\mathrm{tot}}$, because $N_R=N_{\mathrm{tot}}$
(Theorem~\ref{thm:nocollision}).
\end{theorem}
\begin{proof}
Every zero eigenvalue satisfies $0\le\delta\max_j\lambda_j^{+}$ (the threshold is
nonnegative), so the vanishing count contains the zero-eigenvalue count; the nonzero
eigenvalues are exactly $\operatorname{rank}G(X)\le\lfloor X\rfloor$ many.
\end{proof}

\subsection{The general frequency family, and the distinct-frequency lattice}
\label{sec:eigen-general}

Nothing in the factorisation uses that the frequencies come from triplets: it only uses that
column $m$ of $E$ is $(m+1)^{-1/2-i f_i}$.  So the whole spectral package is proved once for an
arbitrary finite family.

\begin{definition}[\code{gramOf}, \code{evalOf}, \code{evalFin}]
For $f:\iota\to\R$ with $\iota$ finite,
\[
  G_{ij}(X)=\sum_{n\le X} n^{-1-i(f_i-f_j)},\qquad
  E_{i,m}=(m+1)^{-1/2-i\,f_i},
\]
the latter with index $m:\mathrm{Fin}\,\lfloor X\rfloor$ (\code{evalOf}) or
$m:\mathrm{Fin}\,X$ for a natural cutoff (\code{evalFin}).
\end{definition}

\begin{theorem}[\code{gramOf\lb eq\lb mul\lb conjTranspose}, \code{gramOf\lb isHermitian},
\code{gramOf\lb posSemidef}, \code{gramOf\lb diag}]
$G=E E^{\mathsf H}$ (and, with the natural cutoff, \code{gramOf\lb nat\lb eq\lb mul\lb
conjTranspose} gives the same with $E$ indexed by $\mathrm{Fin}\,X$); $G$ is Hermitian and
positive semidefinite; and the diagonal is the harmonic number, $G_{ii}=H_{\lfloor X\rfloor}$.
\end{theorem}

\begin{theorem}[\code{eigOf\lb nonneg}, \code{rank\lb gramOf\lb le\lb rank\lb eval},
\code{rank\lb gramOf\lb le}, \code{card\lb nonzero\lb eigOf\lb eq\lb rank},
\code{vanishOf\lb ge}]
All eigenvalues are $\ge0$; $\operatorname{rank}G\le\operatorname{rank}E\le\lfloor X\rfloor$;
the nonzero eigenvalues number exactly the rank; hence for every $\delta\ge0$
\[
  \#\iota\ \le\ N_{\mathrm{van}}(f,X,\delta)+\lfloor X\rfloor .
\]
\end{theorem}

\paragraph{Two instances.}  First, `\code{gramMatrix\lb eq\lb gramOf}' records that the
triplet-indexed matrix of \S\ref{sec:eigen-factor} \emph{is} the instance $f=\code{modeB}\,T$
(definitionally).  Second, and this is the point of the generalisation, take
\[
  \iota=\code{freqSet}(T)=\{b(t,k,\sigma)\}\ \text{(distinct values)},\qquad
  \#\iota=N_R(T),
\]
which is the indexation the paper's code actually uses after de-duplication.  Collision
rigidity (Theorem 5.7) says that distinct triplets have distinct frequencies unless
$t\mapsto|s_2(t)|$ repeats, so the two indexings differ only in that degenerate case.

\begin{theorem}[\code{card\lb freqSet}, \code{gramFreq\lb isHermitian},
\code{gramFreq\lb posSemidef}, \code{rank\lb gramFreq\lb le},
\code{NvanFreq\lb ge}, \code{NvanFreq\lb sub\lb ge}]
Let $G_{\mathrm{freq}}(T,X)$ be the Gram matrix indexed by $\code{freqSet}(T)$.  Then
$\#\iota=N_R(T)$, $G_{\mathrm{freq}}$ is Hermitian and positive semidefinite,
$\operatorname{rank}G_{\mathrm{freq}}\le\lfloor X\rfloor$, and for every $\delta\ge0$
\[
  N_{\mathrm{van}}(F,T,X,\delta)\ \ge\ N_R(T)-\lfloor X\rfloor
\]
\emph{with no hypothesis on collisions}.  This strictly improves
Theorem~\ref{thm:Nvanrank}, whose $N_R$-form had to assume that no collision occurs.
\end{theorem}

\subsection{Collisions are impossible}\label{sec:nocollision}

Rigidity (\code{b\lb collision\lb structure}) reduces a collision to $\sigma=\sigma'$,
$k=k'$ and $|s_2(t)|=|s_2(t')|$.  The last equality cannot hold for $t\ne t'$: both roots are
negative, so it makes them one real number $s$, and then $E(s,-t)=0=E(s,-t')$ reads
\[
  u^2 \;=\; 24\,t^2(1-u)^2(1+3u^2-u^3) \;=\; 24\,t'^2(1-u)^2(1+3u^2-u^3),
  \qquad u=s^2\in(0,1),
\]
and $(1-u)^2(1+3u^2-u^3)>0$, so $t^2=t'^2$.

\begin{theorem}[\code{abs\lb s2\lb injective}, \code{not\lb hasCollision},
\code{NR\lb eq\lb Ntotal}]\label{thm:nocollision}
For $1\le t,t'\le589$, $|s_2(t)|=|s_2(t')|$ implies $t=t'$.  Hence
$\neg\mathrm{HasCollision}(T)$ for every $T$, and $N_R(T)=N_{\mathrm{tot}}(T)$
unconditionally.
\end{theorem}

\noindent
This removes every ``no collision'' hypothesis from the earlier statements
(\code{NR\lb sub\lb le\lb Nvan}, \code{NvanLittleO.eventually\lb le\lb NR},
\code{not\lb NvanLittleO\lb of\lb le\lb NR}).  Note what is \emph{not} claimed: uniqueness of the
root $s_2(t)$ itself.  The argument above only needs that two parameters cannot share one root,
which is weaker than uniqueness for each parameter, and needs no monotonicity and no calculus.

\subsection{A numerical remark: the diagnostics are not small}\label{sec:eigen-num}

The point of replacing opaque symbols by the real definitions is that the numbers can now be
computed.  Evaluating them with the paper's own parameters for the yield experiment
(vf4 \S6.4.8: $t_{\max}=10$, $X=5000$, $\delta=10^{-2}$) gives:

\begin{center}
\small
\begin{tabular}{rrrrr}
\toprule
$T$ & $N_R$ & $N_{\mathrm{off}}$ & $N_{\mathrm{off}}/N_R$ & $N_{\mathrm{van}}/N_R$\\
\midrule
$50$  & $200$  & $200$  & $1.000$ & $0.865$\\
$100$ & $420$  & $420$  & $1.000$ & $0.890$\\
$200$ & $860$  & $860$  & $1.000$ & $0.898$\\
$500$ & $2180$ & $2180$ & $1.000$ & $0.900$\\
\bottomrule
\end{tabular}
\end{center}

\noindent
At $T=100$ the ratio $N_{\mathrm{van}}/N_R$ is stable under $X$: $0.898,\,0.898,\,0.890,\,0.883$
for $X=200,\,10^3,\,5\cdot10^3,\,2\cdot10^4$.  In other words the sequences
$a_T=N_{\mathrm{phase}}/N_R$, $b_T=N_{\mathrm{off}}/N_R$, $c_T=N_{\mathrm{van}}/N_R$ of
vf4 \S6.4.8 read $0$, $1.000$ and $\approx0.9$ here, not $0,0,0$; the conjecture
$N_{\mathrm{off}},N_{\mathrm{van}}=o(N_R)$ is not what these definitions produce at the
paper's parameters.

Two mechanisms, both elementary, explain the numbers.  Neither is formalized; both are
checked numerically.

\itemization{
\item \emph{Why $N_{\mathrm{off}}=N_R$.}  The normalisation is the harmonic sum
  $|G_{jj}|=H_X=\sum_{n\le X}n^{-1}\approx\ln X$ (here $9.09$) --- this is
  Theorem~\ref{thm:herm} of \S\ref{sec:eigen-factor} again: the diagonal entry is exactly
  $H_{\lfloor X\rfloor}$ (\code{gramMatrix\lb diag}, and Mathlib's \code{harmonic} in
  \code{gramMatrix\lb diag\lb eq\lb harmonic}) --- while the numerator
  $I_j=\sum_{i\ne j}|G_{ij}|$ is a sum of \emph{absolute values} --- there is no cancellation
  to exploit.  For a neighbour at frequency distance $\delta_b$ with
  $\delta_b\ln X\ll1$ one has $|G_{ij}|\approx\log(1/\delta_b)+O(1)\approx H_X$; with density
  $\approx2t_{\max}\ln2/\pi\approx4.4$ modes per unit frequency the typical gap is $0.017$
  and the typical nearest-neighbour entry is $|G_{ij}|\approx8.5$.  Measured at
  $T=100$, $X=5000$: $\min_j r_j=64.3$, so every mode exceeds a fixed tolerance
  $\delta<1$.
\item \emph{Why $N_{\mathrm{van}}$ is large.}  Since $G=AA^{*}$, $\operatorname{rank}G\le X$,
  so at least $N_R-X$ eigenvalues vanish identically: $N_{\mathrm{van}}\ge N_R-X$ whenever
  $\delta_T\ge0$.  Measured at $T=100$, $X=300$ ($N_R=4200$): $N_{\mathrm{van}}=4158\ge3900
  =N_R-X$.  When $X>N_R$ no such bound applies, but $A$ is a modulated Vandermonde matrix
  in the points $\log_2 n$ whose spectrum decays quickly, so most eigenvalues still sit below
  $\delta_T\max_j\lambda_j$; at $T=100$, $X=5000$, $336$ of the $420$ clamped eigenvalues
  (80\%) are below $10^{-3}\max_j\lambda_j$, and $374$ (89\%) below the paper's
  $\delta_T=10^{-2}$.
}

\paragraph{The statement $N_{\mathrm{off}}=\#\mathrm{modeSet}$ is not proved --- but its analytic
input now is.}  At the parameters of vf4 \S6.4.8 the numbers above say $r_j(X)>10^{-2}$ for
every mode.  Section~\ref{sec:estimate} proves, with no asymptotics, that a \emph{single}
neighbour within $1.55/\log X$ already forces $r_j\ge1/50$, hence
$N_{\mathrm{off}}=\#\mathrm{modeSet}$ for every $\delta<1/50$ (\code{Noff\lb eq\lb card\lb of\lb
close}).  What is missing is the finite geometric verification: that every mode at
$t_{\max}=10$, $X=5000$ has such a neighbour (within $\approx0.182$ in frequency).  That needs
two things this development does not yet have: certified rational enclosures of
$s_2(1),\dots,s_2(10)$ (see Remark~\ref{rem:status-s2}) and a parameterized $t_{\max}$.

\medskip
\noindent
None of this proves the conjectures false: they quantify over $T\to\infty$ together with
$X(T)\to\infty$ and $\delta_T\to0$, and a differently scaled tolerance could change the
counts.  But it does mean the numerical evidence adduced in vf4 \S6.4.8--6.4.10 is not
evidence for them, and that any repair must change the definitions (for $N_{\mathrm{off}}$
the tolerance would have to grow with $N_R$; for $N_{\mathrm{van}}$ the threshold must be
tied to the conditioning or $X$ must dominate $N_R$).


\section{The truncation cannot grow slowly}\label{sec:necessary}

Theorem~\ref{thm:Nvanrank} is the whole content of the next result: since a mode with zero
Gram eigenvalue is always counted by $N_{\mathrm{van}}$, and there are at least
$\#\mathrm{modeSet}(T)-X$ of those, the vanishing count can only be negligible if the
truncation is not.

\begin{theorem}[\code{NvanLittleO.eventually\lb le\lb Ntotal}]\label{thm:necessary}
If $N_{\mathrm{van}}(T,X(T),\delta(T))=o(N_R(T))$, then for every $\varepsilon>0$ and all
sufficiently large $T$,
\[
  X(T)\ \ge\ (1-\varepsilon)\,N_{\mathrm{tot}}(T).
\]
\end{theorem}
\begin{proof}
Fix $\varepsilon>0$ (for $\varepsilon\ge1$ there is nothing to prove).  Take $\delta\equiv0$
in the little-o hypothesis and $c=\varepsilon/2$: eventually
$N_{\mathrm{van}}(T,X(T),0)\le c\,N_R(T)$.  By Theorem~\ref{thm:Nvanrank},
\[
  N_{\mathrm{tot}}(T)\ \le\ N_{\mathrm{van}}(T,X(T),0)+X(T)\ \le\ c\,N_R(T)+X(T)
  \ \le\ c\,N_{\mathrm{tot}}(T)+X(T),
\]
using $N_R\le N_{\mathrm{tot}}$.  Hence $(1-c)N_{\mathrm{tot}}(T)\le X(T)$, and
$1-\varepsilon\le1-c$.
\end{proof}

\begin{theorem}[\code{NvanLittleO.eventually\lb le\lb NR}]
Under the same hypothesis, $X(T)\ge(1-\varepsilon)N_R(T)$ for all large $T$, for every
$\varepsilon>0$ --- with no hypothesis on collisions, since there are none
(Theorem~\ref{thm:nocollision}).
\end{theorem}

The contrapositive is the quantitative statement the paper's conjecture is committed to:

\begin{theorem}[\code{not\lb NvanLittleO\lb of\lb le\lb Ntotal},
\code{not\lb NvanLittleO\lb of\lb le\lb NR}]\label{thm:refute}
Let $c<1$.  If $X(T)\le c\,N_{\mathrm{tot}}(T)$ for all sufficiently large $T$, then
$N_{\mathrm{van}}\ne o(N_R)$.  Since $N_R=N_{\mathrm{tot}}$ (\code{NR\lb eq\lb Ntotal}), the
same conclusion holds with $N_R$ in place of $N_{\mathrm{tot}}$.
\end{theorem}
\begin{proof}
Otherwise Theorem~\ref{thm:necessary} with $\varepsilon=(1-c)/2$ gives
$(1-\varepsilon)N\le X\le c\,N$ with $1-\varepsilon>c$ and $N>0$ eventually
(\code{eventually\lb Ntotal\lb pos}), a contradiction.
\end{proof}

For the distinct-frequency count of \S\ref{sec:eigen-general} the same conclusion holds with
no hypothesis at all, because its lower bound is unconditional:

\begin{theorem}[\code{NvanFreqLittleO.eventually\lb le\lb NR},
\code{not\lb NvanFreqLittleO\lb of\lb le\lb NR}]
If $N_{\mathrm{van}}(F,T,X(T),\delta(T))=o(N_R(T))$ then, for every $\varepsilon>0$,
$X(T)\ge(1-\varepsilon)N_R(T)$ for all large $T$.  Consequently, if $c<1$ and
$X(T)\le c\,N_R(T)$ eventually, then $N_{\mathrm{van}}(F)\neq o(N_R)$.  Neither statement
assumes anything about collisions (they use \code{NvanFreq\lb ge} and
\code{eventually\lb NR\lb pos}).
\end{theorem}

\noindent
Since $N_{\mathrm{tot}}(T)\sim200\,T\ln2/\pi\approx44.13\,T$ (\S\ref{sec:item3}), the
conjecture of vf4 \S6.4.13 therefore requires a truncation growing at least linearly in $T$,
with constant at least $44.13$: no fixed cutoff $X$ can work, and neither can any $X=o(T)$.
This is consistent with, and explains, the numbers of \S\ref{sec:eigen-num}: at $X=5000$
and $T=500$ one has $N_R=2180$, and indeed $N_{\mathrm{van}}/N_R=0.9$.

\section{The conjectures: stated, not proved}\label{sec:conj}

We reproduce the paper's conjectural layer verbatim as \code{def \dots{} : Prop}, so that
the statements are machine-checked formulations while remaining unproved.  The two
diagnostics occurring in them are the concrete definitions of \S\ref{sec:eigen}.

\begin{definition}[\code{etaR}]
\[
  \eta_R(T,X,\delta)=1-\frac{N_{\mathrm{phase}}+N_{\mathrm{off}}(T,X,\delta)
  +N_{\mathrm{van}}(T,X,\delta)}{N_R(T)},
\]
with $N_{\mathrm{off}},N_{\mathrm{van}}$ as in \S\ref{sec:eigen} and $N_{\mathrm{phase}}=0$
by Theorem 4.3, so that $\eta_R=1-(N_{\mathrm{off}}+N_{\mathrm{van}})/N_R$
(\code{etaR\lb eq}).
\end{definition}

\begin{conjecture}[\code{Eta\lb Tends\lb To\lb One}]
For every $X,\delta:\R\to\R$ with $X(T)\to\infty$ and $\delta(T)\to0$,
$\eta_R(T,X(T),\delta(T))\to1$ as $T\to\infty$.
\end{conjecture}
\begin{conjecture}[\code{Noff\lb LittleO}]
Along the same double limit, $N_{\mathrm{off}}(T,X(T),\delta(T))=o(N_R(T))$.
\end{conjecture}
\begin{conjecture}[\code{Nvan\lb LittleO}]
Along the same double limit, $N_{\mathrm{van}}(T,X(T),\delta(T))=o(N_R(T))$.
\end{conjecture}
\begin{conjecture}[\code{Primality\lb Criterion\lb Conjecture}]
For odd $n>3$, with
\[
  S_f(N)=\sum_{\sigma\in\{-1,1\}}\ \sum_{0<|k|\le10}\ \sum_{m\le N}
  m^{-(1/2+\,i\,b(1,k,\sigma))},
\]
one has $\operatorname{Re}\bigl(S_f(n-1)\,S_f(n+1)\bigr)<0$ if and only if $n$ is prime.
\end{conjecture}

\begin{remark}
Nothing in the development proves, assumes or uses these four propositions.  In
particular no theorem is stated conditionally on them, and \code{\#print axioms} on the
corresponding \code{def}s reports only \code{propext}, \code{Classical.choice},
\code{Quot.sound} --- the definitions are inert.
\end{remark}


\section{An explicit estimate for the Gram entries}\label{sec:estimate}

The numerical remark of \S\ref{sec:eigen-num} explains the size of $N_{\mathrm{off}}$ but proves
nothing about it.  The following estimate is elementary and unconditional --- no asymptotics, no
Euler--Maclaurin.

\begin{theorem}[\code{cos\lb 155\lb ge}]
$\cos 1.55 \ge 1/50$.
\end{theorem}
\begin{proof}
$1.55 < \pi/2$ and $\cos 1.55 = \sin(\pi/2-1.55)$; with
$x = \pi/2 - 1.55 \in (0.0207, 0.025)$ the Taylor bound
\code{Real.sin\lb gt\lb sub\lb cube} gives $\sin x > x - x^3/6 > 0.0207 - 3\cdot10^{-6} > 1/50$,
using $3.1415 < \pi < 3.15$.
\end{proof}

\begin{theorem}[\code{re\lb cpow\lb gram}, \code{re\lb gramOf}]
$\operatorname{Re}\bigl(n^{-1-i\theta}\bigr) = n^{-1}\cos(\theta\log n)$, hence
\[
  \operatorname{Re}G_{ij}(X) = \sum_{n\le X\le}\frac{\cos((f_i-f_j)\log n)}{n}.
\]
\end{theorem}

\begin{theorem}[\code{re\lb gramOf\lb ge}, \code{norm\lb gramOf\lb ge}]
If $|f_i-f_j|\cdot\log X\le1.55$ and $X\ge1$, then
\[
  \operatorname{Re}G_{ij}(X)\ \ge\ \tfrac1{50}\,H_{\lfloor X\rfloor},
  \qquad\text{and hence}\qquad
  \|G_{ij}(X)\|\ \ge\ \tfrac1{50}\,H_{\lfloor X\rfloor}.
\]
\end{theorem}
\begin{proof}
Termwise: $|\theta\log n|\le|\theta|\log X\le1.55<\pi/2$ for $n\le\lfloor X\rfloor$, and $\cos$
decreases on $[0,\pi/2]$, so $\cos(\theta\log n)\ge\cos1.55\ge1/50$; multiply by $1/n>0$ and
sum.  For the norm, $|\operatorname{Re}z|\le\|z\|$.
\end{proof}

\begin{theorem}[\code{offRatio\lb ge\lb of\lb close}, \code{Noff\lb eq\lb card\lb of\lb close}]
If every mode $j$ has another mode $i\ne j$ with $|b_i-b_j|\cdot\log X\le1.55$, then
$r_j(X)\ge1/50$ for every $j$, and consequently
\[
  N_{\mathrm{off}}(T,X,\delta)\ =\ \#\mathrm{modeSet}(T)
  \qquad\text{for every } \delta<1/50,
\]
in particular for $\delta=10^{-2}$.
\end{theorem}
\begin{proof}
$r_j=I_j/H_{\lfloor X\rfloor}\ge|G_{ij}|/H_{\lfloor X\rfloor}\ge1/50$ by the previous theorem and
the harmonic diagonal; then every mode passes the threshold.
\end{proof}

\begin{remark}
At $X=5000$ the geometric hypothesis reads $|b_i-b_j|\le1.55/\log X\approx0.182$
(\code{close\lb iff\lb div}).  What is \emph{not} proved is that this hypothesis holds at the
parameters of vf4 \S6.4.8: that is a finite verification over the $420$ modes at $T=100$ (and
$2180$ at $T=500$), which needs certified rational enclosures of $s_2(1),\dots,s_2(10)$ and a
parameterized $t_{\max}$.  The reduction is formalized; the finite computation is not.  See
\code{paper/phase-status.md}.  \label{rem:status-s2}
\end{remark}


\section{Uniqueness of the root, and $t_{\max}$ as a parameter}\label{sec:unique}

\subsection{Strict monotonicity and uniqueness}

Write $u=s^2$.  By \code{E\lb eq'}, $E(s,-t)=0$ on $(-1,0)$ is equivalent to $f(u)=24t^2$ for
\[
  f(u)=\frac{u^2}{(1-u)^2(1+3u^2-u^3)},\qquad u\in(0,1).
\]

\begin{theorem}[\code{deriv\lb rootRat}, \code{logDeriv\lb ge\lb five},
\code{rootRat\lb strictMonoOn}]
On $(0,1)$ (the identity for $f'/f$ is \code{deriv\lb rootRat\lb log}),
\[
  f'(u)=\frac{u(1-u)(2+7u^3-3u^4)}{\bigl((1-u)^2(1+3u^2-u^3)\bigr)^2}
  \quad\text{and}\quad
  \frac{f'}{f}(u)=\frac{2}{u(1-u)}-\frac{6u-3u^2}{1+3u^2-u^3}\ \ge\ 8-3\ =\ 5\ >\ 0 .
\]
Hence $f$ is strictly increasing on $(0,1)$.
\end{theorem}
\begin{proof}
The two crude bounds are $2/(u(1-u))\ge8$ (since $u(1-u)\le1/4$) and
$(6u-3u^2)/(1+3u^2-u^3)\le3$ (numerator $\le3$, denominator $\ge1$).  Strict monotonicity
follows from \code{strictMonoOn\lb of\lb deriv\lb pos}.
\end{proof}

\begin{theorem}[\code{root\lb iff}, \code{exists\lb unique\lb root\lb grid}, \code{s2\lb unique},
\code{abs\lb s2\lb strictMono}]
For $1\le t\le589$ the equation $E(\cdot,-t)=0$ has exactly one root in the paper's bracket
$(-0.9999,-0.0001)$; any such root equals $s_2(t)$, so the definition of $s_2$ involves no
genuine choice; and $t\mapsto|s_2(t)|$ is strictly increasing.
\end{theorem}

\begin{theorem}[\code{s2\lb mem\lb of\lb sign\lb change}]
If $lo<hi$ in the bracket and $E(lo,-t)>0>E(hi,-t)$, then $s_2(t)\in(lo,hi)$.  This is how a
rational bracket, checked by \code{norm\lb num} on $E$, becomes a certified enclosure of
$s_2(t)$.
\end{theorem}

\begin{theorem}[\code{s2\lb enclosure\lb 1, \dots, s2\lb enclosure\lb 10}]
$s_2(t)$ is bracketed by two rationals at distance $4\cdot10^{-6}$, for $t=1,\dots,10$:
\[
  s_2(1)\in(-0.942826,-0.942822),\quad \dots,\quad
  s_2(10)\in(-0.994127,-0.994123).
\]
Each bracket is checked by \code{norm\lb num} on the polynomial $E$ at the two ends, and
transported to $s_2(t)$ by \code{s2\lb mem\lb of\lb sign\lb change}.
\end{theorem}

\subsection{The truncation $t_{\max}$}

\begin{theorem}[\code{latticeSetOf}, \code{card\lb latticeSetOf}, \code{modeSetOf},
\code{mem\lb modeSetOf}, \code{modeSet\lb eq}, \code{NtotalOf}, \code{NtotalOf\lb bounds}]
For a parameter $t_{\max}$, the lattice $[1,t_{\max}]\times\{-1,1\}$ has $2t_{\max}$ elements,
the triplet set is characterised by $t\le t_{\max}$, $\sigma=\pm1$, $k\ne0$, $|b|\le T$, and
\[
  \Bigl|N_{\mathrm{tot}}(t_{\max},T) - 2\,t_{\max}\,\frac{T\ln2}{\pi}\Bigr|\ \le\ 6\,t_{\max}.
\]
$t_{\max}=100$ is the instance used throughout (\code{modeSet\lb eq}, \code{rfl}), so the paper's
two experiments ($t_{\max}=100$ in \S6.4.3, $t_{\max}=10$ in \S6.4.8) are the two ends of one
statement.
\end{theorem}

\section{Verification notes}\label{sec:verif}

\paragraph{Axioms.} For every theorem of items 1--6, \code{\#print axioms} returns a subset
of \{\code{propext}, \code{Classical.choice}, \code{Quot.sound}\}.  In particular the
obvious question --- does the development lean on \code{N\lb off}, on choice principles
beyond the classical ones, or on \code{sorry} --- has a clean answer: no.  There is no
\code{sorry} and no \code{axiom} declaration in the sources.

\paragraph{Build.} The files are compiled with the pre-built Mathlib of the environment:
\begin{verbatim}
export LEAN_PATH=$PWD:$LEAN_PATH
lean -o FrequencyGrids/Basic.olean -i FrequencyGrids/Basic.ilean \
     FrequencyGrids/Basic.lean
...                    # one line per module, see scripts/build.sh
./scripts/build.sh
\end{verbatim}
The declaration table of \S\ref{sec:table} is generated by
\code{paper/tools/build\lb paper.py} from a single list of rows, so that it can be kept in
step with the sources.

\code{scripts/build.sh} compiles the modules in dependency order
(\code{Basic} $\to$ \code{Lattice} $\to$ \code{Counting} $\to$ \code{Structure} $\to$
\code{Resonance} $\to$ \code{Congruence} $\to$ \code{Conjectures} $\to$ root).  There is no
Lake project: the development is a set of modules over Mathlib's own build.

\paragraph{Design choices worth knowing.}
\itemization{
\item \code{s2} is a \emph{selector}, defined by classical choice from the existence
  theorem, and equals $0$ outside $1\le t\le589$.  Every statement that uses its
  properties carries the hypotheses $1\le t\le589$ explicitly; no statement silently
  assumes them.  (The paper's computational range is $t\le100$.)
\item The triplet type is $\N\times\Z\times\R$: $t$ is a natural, $k$ an integer, $\sigma$
  a real constrained by $\sigma\in\{-1,1\}$ (\code{sigmaSet}).  Integers for $k$ matter:
  injectivity of $k\mapsto b$ and the $\lceil\cdot\rceil/\lfloor\cdot\rfloor$ counting live
  on $\Z$.
\item \code{latticeSet} hard-codes $t_{\max}=100$; the paper's $t_{\max}$ is not a
  parameter.  Making it a variable is a mechanical change (the constants $200$ and $600$
  would become $2t_{\max}$ and $6t_{\max}$).
\item The two counting lemmas are stated for arbitrary finite $S\subseteq\Z$ rather than for
  \code{kSet}, which keeps the floor/ceiling arithmetic out of the application.
\item The positive-semidefiniteness of $G$ is stated in Mathlib's sense, which needs an order
  on $\C$: the file opens the \code{ComplexOrder} scope for that, giving $\C$ its star-order
  (``$z\le w$ iff $w-z$ is a nonnegative real'').  This is a scoped instance, so the
  surrounding development is unaffected.
\item The spectral diagnostics are indexed by the triplet set $\mathrm{modeSet}(T)$ itself
  rather than by $\mathrm{Fin}\,N_R$: this avoids building an enumeration, and the
  permutation-invariance of the spectrum makes the choice immaterial.  Eigenvalues come from
  \code{Matrix.IsHermitian.eigenvalues}, i.e. from the spectral theorem, so they are exact
  reals --- a diagonalisation cannot be computed in Lean, and nothing in the definitions
  needs it to be.
}

\paragraph{What a reader should not conclude.}  That vf4's spectral programme is validated.
The formalization certifies the bookkeeping around the construction --- the lattice step,
the counting, the Gram estimate, the symmetry, the arithmetic filter, and the existence of
the root --- and proves two of the paper's implicit numerical claims false as stated
(Remark~\ref{rem:failure}, Remark~\ref{rem:s2value}).  It proves nothing about
$\eta_R(T)\to1$ or about primality detection.  What it does now settle is the \emph{vocabulary}:
the conjectures are stated about the paper's actual diagnostics (\S\ref{sec:eigen}), and those
diagnostics, evaluated at the paper's own parameters, are far from negligible
(\S\ref{sec:eigen-num}).  The conjectures are therefore open statements whose published
evidence does not survive reimplementation --- which is a different, and weaker, position
than the paper claims, not a refutation.

\section{Declaration-by-declaration table}\label{sec:table}

Every declaration of the development is listed below with its kind, its statement and its
status.  ``proved'' means a closed Lean proof with no \code{sorry}; ``definition'' means a
definition; ``not proved'' means a \code{def \dots{} : Prop} that intentionally has no
proof.

\begingroup
\small
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.15}
"""

prose_tail = r"""
\endgroup

\end{document}
"""


open('paper/frequency-grids-formalization.tex','w').write(prose_head + tbl + prose_tail)
print("rows:", len(rows))
print("written paper/frequency-grids-formalization.tex")
