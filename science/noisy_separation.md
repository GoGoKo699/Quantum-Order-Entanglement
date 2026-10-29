# Retained entanglement and heralded recovery under the same physical noise

The retained controller–target state and an accepted reference–target state answer different physical questions. This page gives a robust example in which a specified three-call retained-state protocol is separable, while a specified four-call recovery protocol produces an entangled accepted pair. Both use the same entanglement-breaking channel family and the same phase-flip probability per physical controller bit.

The result is uniform over a finite interval of channel-axis tilts. Its proof combines exact rational certificates at 83 angles with a continuity bound for the supplied controlled routing. The comparison keeps the two bipartitions, success probability and physical resources explicit. The [general order-support criterion](order_criterion.md) and the [global-dephasing threshold of the minimal example](robustness.md) remain separate results.

## Shared channel family

<a id="shared-family"></a>

Let $`\Delta(X)=\mathrm{Tr}(X)I_2/2`$ and define

```math
\begin{aligned}
|n_{\theta,+}\rangle&=\cos(\theta/2)|0\rangle+\sin(\theta/2)|1\rangle,\\
|n_{\theta,-}\rangle&=-\sin(\theta/2)|0\rangle+\cos(\theta/2)|1\rangle,\\
\mathcal M_\theta(X)&=X_{00}|n_{\theta,+}\rangle\langle n_{\theta,+}|+X_{11}|n_{\theta,-}\rangle\langle n_{\theta,-}|,\\
\mathcal N_{\epsilon,\theta}&=(1-\epsilon)\mathcal M_\theta+\epsilon\Delta.
\end{aligned}
```

Throughout this page,

```math
\epsilon=\frac1{100},\qquad \theta=\frac\pi2+\delta.
```

The map $`\mathcal M_\theta`$ measures the target in the $`Z`$ basis and prepares the corresponding state on the tilted axis. Every channel in this family is entanglement breaking. In the unnormalized Choi convention,

```math
J_{\mathcal N_{\epsilon,\theta}}\succeq\frac\epsilon2 I_4,
```

so every supplied slot has full Choi rank. At $`\delta=0`$, the measurement and preparation axes are orthogonal and $`\mathcal N_{\epsilon,\pi/2}^2=\Delta`$. That identity is absent at sufficiently small nonzero tilts; the proof below does not assume it.

Each slot is an independent instance of the same raw channel, with its own inaccessible environment. The controller starts independent of the target and any reference. Each order uses every supplied slot once. No per-slot unitary wrapper, intermediate target operation, target-carrying bypass, or access to an environment or noise flag is supplied. The recovery experiment permits its stated final target correction only. The sister project's [shared access contract](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/noisy_routing_model.md#shared-access) fixes the broader recovery model.

## Physical controller noise

<a id="physical-control-noise"></a>

Every physical control bit independently undergoes

```math
\mathcal Z_\gamma(X)=\frac{1+\gamma}{2}X+\frac{1-\gamma}{2}ZXZ,
\qquad \gamma=\frac45.
```

The phase-flip probability is therefore $`1/10`$ per bit. A controller matrix element between physical computational codewords $`b`$ and $`b'`$ is multiplied by

```math
\Gamma_{bb'}=\gamma^{d_H(b,b')},
```

where $`d_H`$ is Hamming distance. Noise acts immediately before or immediately after the supplied router, without intervening coherence restoration. These placements commute with routing because its Kraus operators are diagonal in the physical order basis. The noise event is unobserved.

This is independent local phase noise. It differs from the single global visibility parameter in [the minimal-example threshold](robustness.md#exact-separability-transition). In particular, $`\gamma=4/5`$ is not a global dephasing visibility of $`4/5`$.

## The two specified protocols

<a id="specified-protocols"></a>

### Retain the controller and target

The target starts in $`|0\rangle`$. Prepare a uniform superposition of three occupied order states with chronological orders

```math
A=012,\qquad B=021,\qquad C=102.
```

Thus $`012`$ means slot 0 first, as in the [entanglement model](model.md#1-independent-slots-and-chronological-order). Encode these alternatives in three distinct computational basis states of two physical qubits. Any such three vertices of the two-bit square have distances $`1,1,2`$. Up to bit flips and interchange of the physical bits, exactly three assignments remain: the pair at distance two is $`AB`$, $`AC`$, or $`BC`$. Write this choice as $`\ell`$.

Let $`\rho_{CT}^{(\ell)}(\delta)`$ be the unconditional noisy output. No herald is accepted and no target correction is performed. The fourth controller codeword stays unoccupied. The relevant support is therefore $`\mathbb C^3\otimes\mathbb C^2`$. In this dimension, the [Peres–Horodecki criterion](../references/RELATED_WORK.md#partial-transpose) makes positivity of the target partial transpose sufficient for separability.

### Measure the controller and retain a reference–target pair

Prepare an untouched reference $`R`$ and target $`T`$ in the normalized Bell state

```math
|\Phi\rangle_{RT}=\frac{|00\rangle+|11\rangle}{\sqrt2}.
```

Use four raw slots with the following eight matrix words, physical three-bit codes, and accepted signs:

| Matrix word $`\pi`$ | Physical code $`b_\pi`$ | Sign $`s_\pi`$ |
|---|---|---:|
| 1234 | 000 | +1 |
| 1243 | 001 | −1 |
| 2134 | 010 | −1 |
| 2143 | 011 | +1 |
| 3412 | 100 | +1 |
| 3421 | 110 | −1 |
| 4312 | 101 | −1 |
| 4321 | 111 | +1 |

The **rightmost factor of a matrix word acts first**. This convention differs from the chronological labels above. The bits are ordered as outer block exchange, reversal of pair 12, and reversal of pair 34; the inner bits stay attached to their fixed physical pairs when the blocks exchange. Lexical binary numbering of the words would define a different local-noise model. See the [physical codebook](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/noisy_routing_model.md#physical-codebook).

Prepare and accept, respectively,

```math
|\alpha\rangle=\frac1{\sqrt8}\sum_\pi|\pi\rangle,
\qquad
|\beta\rangle=\frac1{\sqrt8}\sum_\pi s_\pi|\pi\rangle,
\qquad F_C=|\beta\rangle\langle\beta|.
```

Use identity as the final target correction. For the corresponding matrix-product Kraus word $`A_{\boldsymbol a,\pi}`$, the accepted target map is

```math
\mathcal E_\delta(X)=\frac1{64}\sum_{\pi,\sigma}
s_\pi s_\sigma\gamma^{d_H(b_\pi,b_\sigma)}
\sum_{\boldsymbol a} A_{\boldsymbol a,\pi}X A_{\boldsymbol a,\sigma}^\dagger.
```

This is the P2 branch. Its ideal-control polynomial is the inherited construction

```math
\frac{\{[X_1,X_2],[X_3,X_4]\}}8,
```

with $`[A,B]=AB-BA`$ and $`\{A,B\}=AB+BA`$. The [qubit construction](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/qubit.md) and [related-work account](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/references/RELATED_WORK.md) give its attribution. The result here concerns its noisy output and the robust comparison.

Define the subnormalized accepted state, probability, Bell overlap and witness by

```math
\begin{aligned}
\tau_{RT}(\delta)&=(\mathrm{id}_R\otimes\mathcal E_\delta)(|\Phi\rangle\langle\Phi|),\\
p(\delta)&=\mathrm{Tr}\tau_{RT}(\delta),\\
f(\delta)&=\langle\Phi|\tau_{RT}(\delta)|\Phi\rangle,\\
w(\delta)&=f(\delta)-\frac{p(\delta)}2.
\end{aligned}
```

The conditional Bell fidelity is $`F=f/p`$ for $`p>0`$. This real branch has input-independent acceptance: $`\mathcal E_\delta^\dagger(I)=pI`$. To prove it, the raw channel is real and covariant under conjugation by $`Y`$. Its switched cross maps and real coefficients preserve these properties. Hence $`\mathcal E_\delta^\dagger(I)`$ is real symmetric and commutes with $`Y`$, forcing it to be scalar; its normalized trace fixes the scalar to $`p`$. An arbitrary complex controller need not have this property. The sister project's [real-controller reduction](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/controller_optimization.md#real-controller-reduction) states the precise optimization result.

## Uniform separation theorem

<a id="uniform-separation"></a>

**Theorem.** For the channels, noise and two protocols just defined, every angular tilt $`|\delta|\le1/5`$ radians satisfies

```math
\left(\rho_{CT}^{(\ell)}(\delta)\right)^{\Gamma_T}
\succ\frac{I_6}{400}
\qquad\text{for every }\ell\in\{AB,AC,BC\},
```

and

```math
w(\delta)>\frac3{1000},\qquad
\frac7{200}<p(\delta)<\frac{19}{200},\qquad
F(\delta)>\frac{101}{190}.
```

All three retained $`C:T`$ outputs are separable. The accepted $`R:T`$ output of the fixed four-call branch is entangled and has a negative partial transpose.

The identity $`I_6`$ acts on the occupied $`3\times2`$ support. In the full two-bit-controller space the state has two unused zero eigenvalues; the displayed strict lower bound is not an $`I_8`$ bound. The interval here is **$`|\delta|\le0.2`$ radians**. The separate [tilted recovery-frontier theorem](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/tilted_readout.md#tilted-optimality) uses $`t=\tan(\delta/2)`$ and the larger interval $`|t|\le1/5`$; those two interval statements must not be interchanged.

## Exact grid certificate

<a id="exact-grid-certificate"></a>

The following rational construction specifies the finite obligations in the proof. It fixes state and Bell normalizations without using a floating-point eigensolver.

For each integer $`k=-41,\ldots,41`$, set

```math
\delta_k=2\arctan(k/400),\qquad
m_k=400-k,\qquad n_k=400+k,\qquad d_k=m_k^2+n_k^2.
```

At this angle define integer matrices

```math
L_0=\begin{pmatrix}m_k&0\\n_k&0\end{pmatrix},\qquad
L_1=\begin{pmatrix}0&-n_k\\0&m_k\end{pmatrix},\qquad
(L_2,L_3,L_4,L_5)=(E_{00},E_{01},E_{10},E_{11}),
```

where $`E_{ab}=|a\rangle\langle b|`$. The actual Kraus operators are $`\sqrt{(1-\epsilon)/d_k}\,L_0`$, $`\sqrt{(1-\epsilon)/d_k}\,L_1`$, and $`\sqrt{\epsilon/2}\,L_2,\ldots,\sqrt{\epsilon/2}\,L_5`$. They reproduce the stated tilted channel exactly. If an $`r`$-slot environmental history has $`q`$ labels from $`\{0,1\}`$, each ordering has the same squared scalar weight

```math
\omega_{r,q}=\frac{(1-\epsilon)^q\epsilon^{r-q}}{d_k^q2^{r-q}}.
```

### Retained-state rational matrices

For a three-slot label tuple $`\boldsymbol a\in\{0,\ldots,5\}^3`$, concatenate the target vectors

```math
L_{a_{\pi_3}}L_{a_{\pi_2}}L_{a_{\pi_1}}|0\rangle
```

for the three chronological orders into $`v_{\boldsymbol a}\in\mathbb Z^6`$. The joint state before physical dephasing is

```math
R_k=\frac13\sum_{\boldsymbol a\in\{0,\ldots,5\}^3}
\omega_{3,q(\boldsymbol a)}v_{\boldsymbol a}v_{\boldsymbol a}^{T}.
```

For allocation $`\ell`$, multiply controller block $`(i,j)`$ by $`(4/5)^{h_{ij}^{(\ell)}}`$, with diagonal exponent zero, exponent two for the selected long pair and exponent one for the other two pairs. Transpose each target block to obtain the exact rational matrix $`\left(\rho_{CT}^{(\ell)}(\delta_k)\right)^{\Gamma_T}`$.

### Accepted Bell contractions

For a four-slot label tuple, let $`P_{\boldsymbol a,\pi}`$ be its integer matrix word made from the $`L`$ matrices and put

```math
g_{\pi\sigma}=s_\pi s_\sigma(4/5)^{d_H(b_\pi,b_\sigma)}.
```

The exact accepted probability and unnormalized Bell overlap are

```math
p_k=\frac1{128}\sum_{\boldsymbol a}\omega_{4,q(\boldsymbol a)}
\sum_{\pi,\sigma}g_{\pi\sigma}
\mathrm{Tr}\left(P_{\boldsymbol a,\pi}^{T}P_{\boldsymbol a,\sigma}\right),
```

```math
f_k=\frac1{256}\sum_{\boldsymbol a}\omega_{4,q(\boldsymbol a)}
\sum_{\pi,\sigma}g_{\pi\sigma}
\mathrm{Tr}(P_{\boldsymbol a,\pi})\mathrm{Tr}(P_{\boldsymbol a,\sigma}).
```

The controller preparation and accepted effect contribute $`1/64`$. The normalized Bell-state trace adds $`1/2`$ in $`p_k`$ and the Bell overlap adds $`1/4`$ in $`f_k`$, giving the denominators 128 and 256.

The [complete rational ledger](../verification/certificates/joint_tilt_certificate_results.json) records these exact finite assertions:

| Object | Number of records | Strict assertion |
|---|---:|---|
| Retained-state partial transpose | 83 angles × 3 allocations = 249 | $`\rho^{\Gamma_T}(\delta_k)-I_6/100\succ0`$ |
| Accepted Bell witness | 83 | $`f_k-p_k/2>1/125`$ |
| Accepted probability | 83 | $`1/25<p_k<9/100`$ |

Positive definiteness is certified by exact $`LDL^T`$ factorization of each shifted six-dimensional matrix. Every diagonal pivot is positive, and the factorization reconstructs the matrix exactly. A pivot is not an eigenvalue lower bound; the shift $`I_6/100`$ is the rigorous eigenvalue margin. The smallest grid witness occurs at $`k=-41`$ and equals

```math
\frac{1203229770605757698272513236489}{136667717788247893824200000000000}>\frac1{125}.
```

The [independent verifier](../verification/audit_verify.py) reconstructs all 249 matrices and all 83 Bell contractions from integer Kraus words and rational weights, checks every factorization and compares the results with the ledger. From the repository root, run

```bash
python verification/audit_verify.py --root verification/certificates
```

The [verification guide](../verification/README.md) explains the full shared certificate bundle and the optional `--rebuild` command for the separate recovery-frontier polynomial identities. Numerical eigenvalues are diagnostics; the strict signs above are exact rational obligations.

## Continuity and proof of the uniform result

<a id="continuity-proof"></a>

**Lemma.** For either specified protocol using $`r`$ slots, let $`\Omega_\delta`$ be the normalized joint state after routing and physical control noise, before accepting or discarding any subsystem. For every input, including an untouched reference,

```math
\|\Omega_\delta-\Omega_{\delta'}\|_1
\le4r\sin\left(\frac{|\delta-\delta'|}{4}\right)
\le r|\delta-\delta'|
```

on the angular intervals used here.

**Proof of the lemma.** Let $`\mathcal D_Z`$ completely dephase the target in its $`Z`$ basis. The family factorizes exactly as

```math
\mathcal N_{\epsilon,\theta}
=\mathrm{Ad}_{R_y(\theta)}\circ\mathcal Q_\epsilon,
\qquad
\mathcal Q_\epsilon=(1-\epsilon)\mathcal D_Z+\epsilon\Delta.
```

For a fixed Stinespring isometry $`V`$ of $`\mathcal Q_\epsilon`$, choose $`V_\theta=(R_y(\theta)\otimes I)V`$. Output rotation preserves the depolarizing part, so this is a common dilation of the actual supplied channel family. Qubit rotations satisfy

```math
\|V_\theta-V_{\theta'}\|_\infty
\le2\sin\left(\frac{|\theta-\theta'|}{4}\right).
```

Keep all slot environments in fixed registers and telescope each product of $`r`$ slot isometries. Each ordered product differs in operator norm by at most $`2r\sin(|\theta-\theta'|/4)`$. The controlled direct sum has the same upper bound because its blocks act on orthogonal order labels. The trace-norm difference of the output states, with any purifying reference, is at most twice the isometry difference. Tracing environments and applying the same controller noise contract trace norm. Finally, $`4\sin(x/4)\le x`$ gives the stated linear bound.

**Proof of the theorem.** First, the grid covers the whole interval. The endpoint lies beyond $`1/5`$ because

```math
2\left[\frac{41}{400}-\frac13\left(\frac{41}{400}\right)^3\right]>\frac15,
\qquad \arctan x\ge x-\frac{x^3}{3}
```

for the nonnegative $`x`$ used here. Consecutive grid angles are at most $`1/200`$ apart, since the derivative of $`2\arctan x`$ is at most two. Every $`|\delta|\le1/5`$ therefore has a grid point satisfying $`|\delta-\delta_k|\le1/400`$.

For the retained experiment, the lemma with $`r=3`$ gives

```math
\|\rho(\delta)-\rho(\delta_k)\|_1\le\frac3{400}.
```

Partial transpose preserves the Hilbert–Schmidt norm. Hence

```math
\|[\rho(\delta)-\rho(\delta_k)]^{\Gamma_T}\|_\infty
\le\|\rho(\delta)-\rho(\delta_k)\|_2
\le\|\rho(\delta)-\rho(\delta_k)\|_1.
```

For each allocation, the exact grid margin thus implies

```math
\left(\rho_{CT}^{(\ell)}(\delta)\right)^{\Gamma_T}
\succ\left(\frac1{100}-\frac3{400}\right)I_6
=\frac{I_6}{400}.
```

The occupied support is $`3\times2`$, so the retained outputs are separable.

For the recovery experiment, the accepted witness equals the expectation in $`\Omega_\delta`$ of

```math
|\beta\rangle\langle\beta|_C\otimes
\left(|\Phi\rangle\langle\Phi|_{RT}-\frac{I_{RT}}2\right).
```

This observable has operator norm $`1/2`$. With $`r=4`$, the lemma gives

```math
|w(\delta)-w(\delta_k)|\le2|\delta-\delta_k|\le\frac1{200}.
```

The grid witness margin therefore yields

```math
w(\delta)>\frac1{125}-\frac1{200}=\frac3{1000}.
```

The success flag is an effect on normalized states. Since the difference of the states has trace zero, its probability changes by at most half their trace-norm difference. Therefore

```math
|p(\delta)-p_k|\le\frac1{200},\qquad
\frac1{25}-\frac1{200}<p(\delta)<\frac9{100}+\frac1{200},
```

which is $`7/200<p<19/200`$. Combining the two strict margins gives

```math
F=\frac12+\frac wp
>\frac12+\frac{3/1000}{19/200}
=\frac{101}{190}.
```

Every separable, possibly subnormalized, two-qubit state obeys $`\langle\Phi|\tau|\Phi\rangle\le\mathrm{Tr}(\tau)/2`$. One way to see this is that a product pure state has squared overlap at most $`1/2`$ with a normalized Bell state, and the inequality is preserved by positive sums. Thus $`w>0`$ proves entanglement. PPT is sufficient for separability in $`2\times2`$, so the accepted entangled state is also NPT. This proves the theorem.

## Operational meaning and resource accounting

<a id="operational-meaning"></a>

| Resource or output | Retained-state experiment | Recovery experiment |
|---|---|---|
| Channel slots | Three | Four |
| Physical controller bits | Two, with three occupied labels | Three, with eight occupied labels |
| Target input | Known $`\lvert0\rangle`$ | Half of a fresh Bell pair |
| Compared bipartition | $`C:T`$ | $`R:T`$ after controller measurement |
| Output | Unconditional | Accepted P2 branch |
| Uniform conclusion | Separable for all three code allocations | Entangled and NPT with stated $`p,F`$ bounds |

The probability bounds charge rejected trials. If a fresh Bell pair is supplied on each independent attempt, the expected number of slot calls per accepted pair satisfies

```math
\frac{800}{19}<\frac4p<\frac{800}{7}.
```

A failed attempt is not assumed to preserve an unknown input for another try. The conclusion is therefore a heralded entanglement-distribution statement with fresh-input costs, not an unassisted quantum-capacity statement.

This comparison establishes a simultaneous robust example for the two specified protocols. It does not classify every retained-controller protocol, optimize an equal-resource $`C:T`$ versus $`R:T`$ comparison, or make retained $`C:T`$ entanglement necessary for recovery. A Bell fidelity above $`1/2`$ is a sufficient witness here; a Bell fidelity at or below $`1/2`$ does not classify the entanglement of arbitrary complex-controller outputs. The separate [full recovery frontier](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/recovery_frontier.md#frontier-theorem) optimizes accepted Bell objectives over its stated controller class, rather than all retained-state protocols.

Useful noisy recovery here also differs from exact identity recovery. The positive-definite physical Schur noise and full-rank raw slots meet the [exact-recovery obstruction](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/noisy_recovery_obstruction.md#strict-schur-obstruction); the accepted state can remain entangled while exact unitary recovery is impossible under that access contract.
