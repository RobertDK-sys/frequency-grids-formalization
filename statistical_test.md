# A valid statistical test of the frequency claims

## 1. Scope and verdict

This note concerns the inference from measured coherence curves to the statement that a fixed mathematical construction (zeta, or the proposed $b$-lattice) **predicts** the measured frequencies. It does not question the published measurements themselves.

There are two different assertions:

* **In-sample description:** a polynomial/interpolation rule gives minima close to $\gamma_1,\ldots,\gamma_5$ on the measured interval.
* **Out-of-sample prediction:** an algorithm fixed before looking at the new measurements predicts their minima, within a stated tolerance, with a controlled error rate.

Only the second tests that an algorithm explains the frequencies. A coincidence probability computed as though the targets, windows, interpolation and matching rule had been fixed in advance is not valid when those choices were made after seeing the same curves.

A defensible formulation $F_{\mathscr A,\delta,\alpha}$ is available:

> Lock an algorithm $\mathscr A$ and a one-to-one, ordered target map before acquiring confirmatory data. Acquire new raw replicates in pre-specified target and control windows. At familywise error $\alpha$, demonstrate that every predicted true minimum is within $\delta$ of its target, and apply a pre-specified false-positive/control criterion.

This is nonvacuous only if the noise and systematic finite-size shifts leave power at tolerance $\delta$. Passing it establishes predictive agreement at resolution $\delta$, not an exact spectral identity or a unique physical mechanism. The existing fitted curves can motivate such a protocol; without a complete account of the selection process or new held-out data, they cannot supply a retrospective confirmatory $p$-value.

## 2. Data and the quantity that must be estimated

For each fixed setting $a$ (including $\beta$ and the partial-sum construction), suppose the raw observations are

$$Y_{a,i,r}=y_a(t_{a,i})+\varepsilon_{a,i,r},\qquad i=1,\ldots,n_a,\quad r=1,\ldots,R_{a,i},$$

where $y_a(t)$ is the measured real component, imaginary component, or modulus of the coherence. The reported mean and standard deviation at $(a,i)$ are denoted $\bar Y_{a,i}$ and $s_{a,i}$. Under a stated normal model,

$$\bar Y_a\sim N(y_a,\Sigma_a),\qquad \Sigma_{a,ii}=\sigma_{a,i}^2.$$

If the $R_{a,i}$ replicates are independent and all other settings are fixed, $\sigma_{a,i}=s_{a,i}/\sqrt{R_{a,i}}$ is the standard error of the mean. A standard deviation of single replicates must not be substituted for this standard error.

The estimand for the $j$th predicted feature is $\tau_{a,j}$, the **true underlying** location of that feature, not the location recomputed from one noisy realization. A vertical error bar on $Y$ is not a standard error for $\tau$.

Repeated measurements at different times may share pulse-calibration and state-preparation errors. Thus diagonal $\Sigma_a$ is an assumption, not a consequence of plotting separate error bars. Ideally $\Sigma_a$ is estimated by resampling whole experimental runs. If $a^\top\bar Y$ is a linear estimator and only the marginal standard deviations are available, arbitrary correlations satisfy the conservative bound

$$\operatorname{Var}(a^\top\bar Y)
 =a^\top\Sigma a
 \leq \left(\sum_i |a_i|\sigma_{a,i}\right)^2. \tag{1}$$

Joint Gaussianity with conservative variance gives conservative normal intervals; marginal error bars alone do not specify a joint null distribution.

For reference, **if** 55 points are equally spaced from $12.63$ through $34.44$, their spacing is

$$h=\frac{34.44-12.63}{54}=0.403888888888\ldots . \tag{2}$$

This spacing alone says nothing about the uncertainty of an interpolated minimum.

## 3. From vertical noise to uncertainty in a minimum

### 3.1 An exact quadratic-regression/Fieller construction

Use a window fixed before seeing the confirmatory observations. Put $x=(t-t_0)/h$ and assume that on that window the underlying curve is

$$q(x)=\theta_0+\theta_1x+\theta_2x^2,\qquad \theta_2>0.$$

Its minimum is $x_*=-\theta_1/(2\theta_2)$ and $\tau=t_0+hx_*$. Write $X$ for the design matrix and use generalized least squares

$$\widehat\theta=(X^{\mathsf T}\Sigma^{-1}X)^{-1}X^{\mathsf T}\Sigma^{-1}\bar Y,
 \qquad V=\operatorname{Cov}(\widehat\theta)=(X^{\mathsf T}\Sigma^{-1}X)^{-1}. \tag{3}$$

Under the normal model, $\widehat\theta$ is exactly jointly normal with mean $\theta$ and covariance $V$. (For ordinary least squares, replace $V$ by $(X^{\mathsf T}X)^{-1}X^{\mathsf T}\Sigma X(X^{\mathsf T}X)^{-1}$.)

For a proposed $x$, let $a_x=(0,1,2x)^{\mathsf T}$. The true vertex satisfies $a_{x_*}^{\mathsf T}\theta=0$, and hence

$$\frac{a_x^{\mathsf T}\widehat\theta}{\sqrt{a_x^{\mathsf T}Va_x}}
 \sim N(0,1)\quad\text{when }x=x_*.$$

Consequently an exact $(1-\alpha)$ Fieller confidence set is

$$\mathcal C_{x_*}=\left\{x:
 (a_x^{\mathsf T}\widehat\theta)^2
 \leq \chi^2_{1,1-\alpha}\,a_x^{\mathsf T}Va_x\right\},
 \qquad \mathcal C_\tau=t_0+h\mathcal C_{x_*}. \tag{4}$$

Indeed, coverage fails exactly when the inequality at the true $x_*$ fails, an event of probability $\alpha$. The set can be an interval, a union of rays, or all of $\mathbb R$. That is desirable: near-zero fitted curvature means that the data do not identify a finite minimum precisely. Replacing (4) automatically by a small symmetric interval would hide this problem.

The delta-method variance, useful only when the curvature is well determined, is

$$\widehat{\operatorname{Var}}(\widehat x_*)\approx g^{\mathsf T}Vg,
 \qquad g=\left(0,-\frac1{2\widehat\theta_2},
 \frac{\widehat\theta_1}{2\widehat\theta_2^2}\right)^{\mathsf T}. \tag{5}$$

If $\Sigma$ or $V$ is estimated from replicates, (4) with a normal quantile is generally approximate, not exact. One should then use a studentized whole-run bootstrap or another justified replicate model, and report its finite-sample limitations. Pre-specification of the fit window remains essential.

### 3.2 The common three-point formula makes the scale explicit

For three equally spaced observations $(Y_-,Y_0,Y_+)$ at $(t_0-h,t_0,t_0+h)$, three-point parabolic interpolation gives

$$\widehat\tau-t_0=\frac{h}{2}\frac{N}{D},\qquad
 N=Y_--Y_+,\qquad D=Y_--2Y_0+Y_+. \tag{6}$$

Under a true quadratic with curvature $q''$, the mean of $D$ is $q''h^2$. At a vertex centered at $t_0$, independent observations give the local linear approximation

$$\operatorname{SE}(\widehat\tau)\approx
 \frac{\sqrt{\sigma_-^2+\sigma_+^2}}{2|q''|h}
 =\frac{\sigma}{\sqrt2\,|q''|h}
 \quad\text{if }\sigma_-=\sigma_+=\sigma. \tag{7}$$

Thus the horizontal precision depends on both the curvature and the time spacing; it cannot be read from $\sigma$ alone. More generally the delta calculation for (6) uses

$$\operatorname{Var}(N)=\sigma_-^2+\sigma_+^2,\qquad
 \operatorname{Var}(D)=\sigma_-^2+4\sigma_0^2+\sigma_+^2,$$

and $\operatorname{Cov}(N,D)=\sigma_-^2-\sigma_+^2$ in the independent case.

Equation (6) always describes the three-point parabolic interpolant, but it estimates the true vertex without systematic error only under the quadratic model; (7) additionally uses a local normal approximation. Polynomial interpolation of a nonquadratic curve has deterministic bias which repeated-experiment error bars do not measure. Moreover, at an exact zero of a smooth complex amplitude, $|L(t)|$ generically behaves like $C|t-\tau|$, not like a smooth positive-curvature quadratic. In that regime one should fit the real and imaginary components (or an explicitly justified two-sided modulus model), rather than assume that a parabola on $|L|$ is unbiased.

## 4. A confirmatory test: equivalence, not non-rejection

Let $\lambda_{a,j}$ be the $j$th target produced by the locked algorithm. For zeta validation these may be pre-specified $\gamma_j$; for a lattice test they must be lattice points computed without reference to confirmatory measurements. Include any theoretically known finite-truncation shift in $\lambda_{a,j}$, or account for it in $\delta$. Otherwise the test confuses device error with an already predictable finite-$N$ approximation error.

For an ordered, pre-assigned set of $J$ targets, define

$$H_0(\delta):\ \exists j\ \text{with}\ |\tau_{a,j}-\lambda_{a,j}|\geq\delta,
 \qquad
 H_1(\delta):\ \forall j\ \text{with}\ |\tau_{a,j}-\lambda_{a,j}|<\delta.$$

Non-rejection of the point null $\tau_{a,j}=\lambda_{a,j}$ is **not** evidence for $H_1$: an imprecise experiment also fails to reject. The appropriate decision is an equivalence test.

Construct simultaneous $1-\alpha$ confidence sets $C_{a,j}$ for the $\tau_{a,j}$. Declare the tolerance prediction confirmed only if

$$C_{a,j}\subset(\lambda_{a,j}-\delta,\lambda_{a,j}+\delta)
 \qquad\text{for every }j=1,\ldots,J, \tag{8}$$

and all pre-specified control requirements also pass. A Fieller set that is unbounded automatically fails (8), as it should. If control tests are random as well, allocate separate budgets $\alpha_{\rm loc}$ and $\alpha_{\rm ctrl}$ to the location and control families; the total familywise level is $\alpha=\alpha_{\rm loc}+\alpha_{\rm ctrl}$ by the union bound.

**Level proof.** Under $H_0(\delta)$ choose $j_0$ whose true error is at least $\delta$. If (8) passes, $C_{a,j_0}$ lies strictly inside the tolerance interval and cannot contain $\tau_{a,j_0}$. Therefore a false confirmation implies failure of the simultaneous coverage event, whose probability is at most $\alpha$. No independence between targets is required.

In the simpler normal location approximation $\widehat\tau_j\sim N(\tau_j,s_j^2)$, simultaneous intervals can be written

$$C_j=\widehat\tau_j\pm z_\star s_j.$$

For independent targets the exact Šidák choice is

$$z_\star=\Phi^{-1}\!\left(\frac{1+(1-\alpha)^{1/J}}2\right). \tag{9}$$

Without independence the Bonferroni choice

$$z_\star=\Phi^{-1}\!\left(1-\frac{\alpha}{2J}\right) \tag{10}$$

is valid. If a **single future noisy observation**, rather than the underlying minimum, is required to land in a tolerance window, a prediction interval must include the new measurement variance as well: $s_{\rm pred}^2=s_{\rm fit}^2+s_{\rm new}^2$.

A genuine implementation must also define specificity. Pre-register target-free/control windows and the treatment of additional minima, and use an equivalence test for a declared negligible-dip threshold where absence is claimed. Merely failing to detect an extra zero does not establish its absence. If real and imaginary zero crossings are two channels for the same physical minimum, their pairing and common-root rule must be fixed before unblinding.

## 5. Exact power calculations and a numerical benchmark

The following numerical statements are illustrations of the formulas, not estimates from the published error bars. Assume the normal location model, all five targets pre-assigned, $\alpha=0.05$, and no analysis search. Bonferroni gives

$$J=5,\qquad z_\star=2.575829303549.$$

If $\delta=0.1$, a necessary condition for a nonempty acceptance region at target $j$ is

$$s_j<\frac{\delta}{z_\star}=0.038822448313. \tag{11}$$

If $s_j=0.02$ and the true errors are zero, acceptance for target $j$ occurs when

$$|s_jZ|\leq r:=\delta-z_\star s_j=0.048483413929,\qquad Z\sim N(0,1).$$

Its probability is

$$p_j=2\Phi(r/s_j)-1=0.984656608348.$$

Thus the power for all five is $p_j^5=0.925601393312$ under independence; without independence it is at least

$$1-5(1-p_j)=0.923283041738. \tag{12}$$

More generally, put $r_j=\delta-z_\star s_j$, and let $b_j=\tau_j-\lambda_{a,j}$. If $r_j>0$,

$$p_j=\Phi\!\left(\frac{r_j-b_j}{s_j}\right)
     -\Phi\!\left(\frac{-r_j-b_j}{s_j}\right). \tag{13}$$

Independence gives power $\prod_jp_j$; arbitrary dependence gives the rigorous lower bound $\max\{0,1-\sum_j(1-p_j)\}$. If any $r_j\leq0$, the corresponding symmetric-interval acceptance event is empty (apart from a measure-zero boundary convention), so the experiment has no useful confirmatory power at that setting.

## 6. Look-elsewhere effect

### 6.1 A finite, auditable search

Let $\mathcal A$ be the **complete** collection of analyses actually available to selection: values of $\beta$, $t_{\max}$, $k$-range, partial-sum base set, target tolerance, interpolation rule, and any other choice affecting a reported match. Choices made after inspecting the data belong to this collection whether or not they appear in the final report.

For analysis $a$, suppose there are $Q_a$ eligible observed features and $J=5$ targets. If the target-to-feature map is pre-assigned, there is one mapping. If one merely reports the best five in order, there are

$$\binom{Q_a}{5}$$

ordered mappings; if arbitrary injective relabelling is allowed, there are

$$(Q_a)_5=Q_a(Q_a-1)(Q_a-2)(Q_a-3)(Q_a-4).$$

At $Q_a=10$ these counts are $252$ and $30240$, respectively. (If the ten crossings are pre-paired real/imaginary channels, those pairs must be formed first; one cannot claim this larger freedom after the fact.) This counting addresses only the enumerated target/map choice. It does not make an unmodelled data-dependent choice of fit windows or feature definitions valid; those choices require selective inference or fresh locked data.

For notational simplicity in this subsection, $\alpha$ denotes the location budget $\alpha_{\rm loc}$; any separately randomized controls add $\alpha_{\rm ctrl}$ to the total level. A direct, dependence-robust way to control the whole search is to construct every location confidence set at level $1-\alpha/M$, where

$$M=5\sum_{a\in\mathcal A}|\mathcal M_a| \tag{14}$$

and $\mathcal M_a$ is the set of allowed mappings. Then, with probability at least $1-\alpha$, **all** sets cover their true parameters simultaneously. Declare a match only if there exists an allowed $(a,m)$ for which all five sets are contained in their tolerance intervals and all locked controls pass.

**Global level proof.** Under the global non-equivalence null, every allowed $(a,m)$ has at least one target whose true error is at least $\delta$. A reported match for that $(a,m)$ therefore entails at least one noncoverage event. The union bound over the $M$ individual constraints limits this probability to $\alpha$. Correlation among analyses does not affect validity.

For a symmetric normal interval the conservative critical value replaces (10) by (the numerical examples below concern the location family only)

$$z_M=\Phi^{-1}\!\left(1-\frac{\alpha}{2M}\right). \tag{15}$$

With no search and a fixed mapping, $M=5$ and $z_M=2.575829303549$. Purely as an audit illustration, if $120$ candidate settings had actually been tried with a fixed mapping, $M=600$ and

$$z_{600}=3.934605861560,\qquad \delta/z_{600}=0.025415506284
 \quad(\delta=0.1).$$

With one analysis and unrestricted selection of an ordered five-tuple from ten candidates, $M=151200$ and

$$z_{151200}=5.105060997068,\qquad \delta/z_{151200}=0.019588404538
 \quad(\delta=0.1).$$

Thus $s=0.02$ has useful power in the first setting, but its acceptance intervals cannot meet the same $0.1$ tolerance in the last. If $120$ settings and monotone best-five selection from ten are combined, (14) also gives $M=120\times5\times252=151200$. These are explicit sensitivity calculations, not assertions about how many analyses any experiment actually performed.

### 6.2 Do not count nested searches as independent opportunities

Some naïve multipliers overstate the look-elsewhere effect. Fix an observed estimate $\widehat\tau$ and tolerance $r$, and let target sets $\Lambda_1\subseteq\Lambda_2$. For

$$D_j=\min_{\lambda\in\Lambda_j}|\widehat\tau-\lambda|,$$

we have $\{D_1\leq r\}\subseteq\{D_2\leq r\}$. Hence the event of any hit over a nested family is exactly the event for the largest set. Increasing $t_{\max}$ or a $k$-range need not add a Bonferroni factor when it only enlarges a nested deterministic target set and everything else is fixed. It does add freedom when it changes the fitted data, interpolation, normalization, tolerance or selection rule, because then the estimates and events are no longer nested.

### 6.3 Correlation can be used instead of Bonferroni

For standardized Gaussian estimation errors, write

$$G_m=\frac{\widehat\eta_m-\eta_m}{s_m},\qquad
 G=(G_1,\ldots,G_M)\sim N(0,R).$$

(If $\eta_m=\tau_m$, these errors are approximations unless a linear normal location model is exact.) The sharp simultaneous threshold $c_R$ is defined by

$$\Pr_{G\sim N(0,R)}\left(\max_m|G_m|\leq c_R\right)=1-\alpha. \tag{16}$$

It gives simultaneous intervals $\widehat\eta_m\pm c_Rs_m$, and also a max-statistic test of a point null for the $\eta_m$. The threshold can be computed from the full covariance by a fixed, reproducible numerical integration or simulation. The Bonferroni threshold (15) is valid without knowing $R$, generally conservatively. If the search is genuinely continuous and unrecorded, no finite $M$ can be invented retrospectively: one needs a justified maximum-Gaussian-process calculation, an exact geometric reduction to the largest target set, or new data with a locked finite analysis.

A numerical coincidence null (for example, random target phases) is a separate modelling choice. The procedure above tests predictive location errors directly and does not silently assume that zeta ordinates or lattice phases are uniform random variables.

## 7. Why the published fitted curves cannot confirm the extrapolation twice

Suppose the same 55-point curve is used to (i) choose minima, (ii) choose the interpolation/recurrence, and (iii) evaluate how well that rule agrees with zeta or predicts $]0,10[$. Then the prediction and its apparent validation are functions of the same noise. The usual normal/Fieller coverage statement is unconditional on such data-dependent selection and does not automatically remain valid conditionally on “this was the most successful-looking rule.”

There are three statistically sound options:

1. **New confirmatory runs (preferred).** Freeze targets, windows, raw-data pipeline, fit rule and $\delta$; then acquire independent replicates. For zeta, a useful out-of-range test can use $\gamma_6,\ldots,\gamma_{10}$. For a lattice low-frequency claim, the new measurements must include the claimed region below $12.63$; extrapolating the old interpolation and checking it against the old points is not such a test.
2. **A genuine holdout.** Split raw experimental runs before any minima or recurrence have been inspected. Use the training part for every modelling choice and run the locked pipeline once on the holdout. Withholding a few already-used summary ordinates is not enough if their selection influenced the model.
3. **Selective inference.** Condition on the fully specified selection event and derive its actual distribution. This is possible only with a much more explicit algorithm and probability model than a verbal description of polynomial fitting; ordinary intervals applied after selection are not selective inference.

Accordingly, the existing reported agreement remains a descriptive experimental result, while a numerical $p$-value for the later lattice/extrapolation claim cannot be reconstructed from the point counts and plotted standard deviations alone. The numerical calculation requires the raw $(t,\bar Y,s)$ tables, replicate dependence model, fitted curvature or covariance $V$, and a complete search history.

## 8. Recommended protocol and precise interpretation

A concise implementable protocol is:

1. **Lock the mathematical algorithm.** Publish code and parameter files for the characteristic equation, phase map, $t$-range, $k$-range, base set, and target map. Compute all $\lambda_j$ before unblinding. No nearest-target relabelling is allowed unless it and its multiplicity were locked.
2. **Lock the experimental design.** Use fresh raw replicates in disjoint ordered windows around each predicted feature and in pre-specified controls. Include a low-$t$ window when testing a low-$t$ extrapolation. Choose $R_{a,i}$ from the power formula (13), including known systematic shifts.
3. **Lock the estimator.** Pre-specify component/modulus, fit windows, covariance treatment, interpolation, and controls. Use (4), or a justified whole-run max-$t$ bootstrap; do not turn vertical error bars directly into horizontal errors.
4. **Unblind once.** Evaluate all simultaneous sets and tolerance inclusion (8). Include every admissible analysis in (14), or use the covariance threshold (16). Report all attempted analyses and all extra features.
5. **State the conclusion at its actual resolution.** A pass supports $F_{\mathscr A,\delta,\alpha}$: frozen predictions agree with fresh measurements at resolution $\delta$ with familywise error $\alpha$. A failure can mean wrong frequencies, excessive noise, or an omitted finite-size shift; these cases should be distinguished by the confidence sets and power calculation.

For the $b$-lattice, this is a defensible statistical meaning of “the lattice explains the observed frequencies” without making a false exact-identity claim. It is mathematically well posed and compatible with the band facts. It does not evade those facts: if no lattice target lies in a pre-specified tolerance interval, the prediction fails deterministically before any statistical test. Nor would a successful finite-tolerance test by itself identify the lattice as the mechanism; a comparison with the already specified quantum coherence model would require a separately locked out-of-sample predictive comparison with the same search budget.

## 9. Primary-source check and reproducibility

The arXiv version of Wei et al., *The Riemann Hypothesis Emerges in Dynamical Quantum Phase Transitions* ([arXiv:2511.11199](https://arxiv.org/html/2511.11199)), states in Section II.3 that its five coherence-zero estimates were “extracted through polynomial fitting of the experimental data.” Its Figure 3 caption states that error bars are $1\sigma$ intervals from repeated experiments. These primary-source statements motivate, but do not replace, the horizontal-error and selection calculations above. No unpublished numerical data are used in this note.

The numerical constants in Sections 5 and 6 are regenerated by `analysis_constants.py`; the checked output is in `analysis_constants.txt`. The script uses only the formulas displayed here, SciPy's normal CDF/inverse CDF, and NumPy for the optional Fieller coefficient example.
