# Channels that realize the noncommuting side

The [order criterion](order_criterion.md) requires an existence proof: noncommuting permutations must be realized through repeated uses of one legitimate channel. Arbitrary controlled unitaries cannot simply be inserted as additional operations. This page gives that realization with a target of dimension $`n+2`$, and a separate construction whose complete definite-order channel erases every target input.

Both constructions use an established conditional-unitary entanglement criterion. Its short proof is included first to make the dependence explicit.

## The inherited conditional-unitary criterion

Let $`U_0,\ldots,U_{m-1}`$ be unitaries on $`\mathbb C^D`$, and let $`\alpha_i\ne0`$ with $`\sum_i|\alpha_i|^2=1`$. Consider

```math
\sigma=\frac1D\sum_{i,j=0}^{m-1}
\alpha_i\overline{\alpha_j}|i\rangle\langle j|
\otimes U_iU_j^\dagger.
\qquad\text{(1)}
```

This is the output of controlled unitaries applied to
$`|\alpha\rangle\langle\alpha|\otimes I_D/D`$.

**Lemma 2.** The state (1) is separable if and only if the relative unitaries $`U_iU_0^\dagger`$ commute pairwise. Otherwise it is NPT.

This is a special case of **Roszak's pure-dephasing separability theorem**, including its NPT conclusion. It is an inherited ingredient, not the new order-support classification; see [the source and exact comparison](../references/RELATED_WORK.md#roszak2018).

### Proof

Right-multiplying every $`U_i`$ by $`U_0^\dagger`$ leaves all blocks $`U_iU_j^\dagger`$ unchanged, so assume $`U_0=I`$. An invertible local diagonal filter on the controller removes the nonzero amplitudes $`\alpha_i`$. Such a filter preserves whether the partial transpose is positive: the partially transposed matrices are related by an invertible congruence.

After omitting a positive scalar, the filtered partial transpose on $`C`$ has blocks

```math
R^{\Gamma_C}_{ij}=U_jU_i^\dagger.
```

Its reference diagonal block is $`I_D`$. The Schur complement of that block has entries, for $`i,j>0`$,

```math
S_{ij}=U_jU_i^\dagger-U_i^\dagger U_j,
\qquad S_{ii}=0.
\qquad\text{(2)}
```

A positive semidefinite block matrix with zero diagonal blocks has every off-diagonal block zero. For example, each two-block principal submatrix would otherwise have the form
$`\left(\begin{smallmatrix}0&S_{ij}\\S_{ij}^\dagger&0\end{smallmatrix}\right)`$
with eigenvalues of both signs. Thus PPT requires $`[U_j,U_i^\dagger]=0`$ for all $`i,j`$, equivalently pairwise commutation of the unitaries.

Conversely, commuting unitaries have a common orthonormal eigenbasis $`\{|e_k\rangle\}_{k=1}^D`$, with $`U_i|e_k\rangle=\lambda_{ik}|e_k\rangle`$. Define
$`|\alpha^{(k)}\rangle=\sum_i\alpha_i\lambda_{ik}|i\rangle`$.
Then

```math
\sigma=\frac1D\sum_{k=1}^D
|\alpha^{(k)}\rangle\langle\alpha^{(k)}|
\otimes|e_k\rangle\langle e_k|,
\qquad\text{(3)}
```

which is separable. If commutation fails, (2) makes the partial transpose nonpositive. This proves the lemma.

## The linear-dimension channel

Fix $`n\ge2`$ and $`0\lt p\lt 1`$. Use target basis

```math
|\varnothing\rangle,\quad |0\rangle,\ldots,|n-1\rangle,
\quad |f\rangle.
```

The marker subspace is spanned by $`|0\rangle,\ldots,|n-1\rangle`$. Let $`S|j\rangle=|j+1\bmod n\rangle`$ on that subspace and let $`S`$ vanish on the other two states. Define the identical channel $`\mathcal N_{n,p}`$ by

```math
\begin{aligned}
K_0&=\sqrt{1-p}(|\varnothing\rangle\langle\varnothing|+S)
     +|f\rangle\langle f|,\\
K_1&=\sqrt{p}\,|0\rangle\langle\varnothing|,\\
F_j&=\sqrt{p}\,|f\rangle\langle j|,
\qquad 0\le j\lt n.
\qquad\text{(4)}
\end{aligned}
```

The target starts in $`|\varnothing\rangle`$. The controller is any pure state with occupied support $`\Pi`$ as in the [model](model.md#3-inputs-and-the-entanglement-task). No part of (4) depends on that support or its amplitudes.

### Complete positivity and trace preservation

Let $`P_M=\sum_{j=0}^{n-1}|j\rangle\langle j|`$. Orthogonality of the three target sectors gives

```math
\begin{aligned}
K_0^\dagger K_0
 &=(1-p)(|\varnothing\rangle\langle\varnothing|+P_M)
   +|f\rangle\langle f|,\\
K_1^\dagger K_1&=p|\varnothing\rangle\langle\varnothing|,\\
\sum_jF_j^\dagger F_j&=pP_M.
\end{aligned}
```

Their sum is the identity. These Kraus operators therefore define an ordinary finite-dimensional channel.

### Which environmental tuples reach the marker space?

Apply the switch for exactly $`n`$ calls and project the final target onto $`P_M`$. A surviving tuple contains **one $`K_1`$ and $`n-1`$ copies of $`K_0`$**:

- With no $`K_1`$, a nonzero trajectory remains in $`|\varnothing\rangle`$.
- A second $`K_1`$ annihilates the state, because the first one has left the empty sector permanently.
- Any nonzero $`F_j`$ sends the target to the absorbing failure sector, from which it cannot reach the markers.

Label a surviving tuple by the physical slot $`r`$ that contains its unique $`K_1`$. In chronological order $`\pi`$, this slot appears at time position $`\pi^{-1}(r)`$. The number of subsequent shifts is $`n-1-\pi^{-1}(r)`$. Its final marker and amplitude are therefore

```math
|n-1-\pi^{-1}(r)\rangle,
\qquad \sqrt{p(1-p)^{n-1}}.
\qquad\text{(5)}
```

Define an $`n\times n`$ permutation unitary by

```math
U_\pi|r\rangle=|n-1-\pi^{-1}(r)\rangle.
\qquad\text{(6)}
```

Summing over the inaccessible slot label $`r`$ gives the unnormalized marker block

```math
p(1-p)^{n-1}\sum_{\pi,\tau\in\Pi}
\alpha_\pi\overline{\alpha_\tau}|\pi\rangle\langle\tau|
\otimes U_\pi U_\tau^\dagger.
\qquad\text{(7)}
```

Its trace is

```math
q=np(1-p)^{n-1}.
\qquad\text{(8)}
```

The normalized marker state is exactly (1) with $`D=n`$.

### Faithfulness supplies the converse

Write $`P_\pi|r\rangle=|\pi(r)\rangle`$ for the natural permutation representation, and $`J|r\rangle=|n-1-r\rangle`$. Equation (6) becomes $`U_\pi=JP_{\pi^{-1}}`$, so

```math
U_\pi U_{\pi_0}^\dagger
=J P_{\pi^{-1}\pi_0}J^\dagger
=J P_{(\pi_0^{-1}\pi)^{-1}}J^\dagger.
\qquad\text{(9)}
```

The natural representation is faithful. Its relative matrices commute exactly when the relative permutations do. Lemma 2 therefore makes the marker state NPT whenever $`G_\Pi`$ is nonabelian.

A local filter cannot turn a PPT state into an NPT state. Consequently the **unconditional switch output is already NPT**. This proves the converse in [Theorem 1](order_criterion.md#theorem-1-the-order-support-criterion).

In fact, the unconditional output is block diagonal in the empty, marker and failure sectors. Each nonzero environmental tuple ends in the same type of sector in every branch where it survives. Its form is

```math
\rho_{CT}^{\mathrm{out}}
=(1-p)^n|\alpha\rangle\langle\alpha|
  \otimes|\varnothing\rangle\langle\varnothing|
 +q\sigma
 +R_C\otimes|f\rangle\langle f|,
\qquad\text{(10)}
```

where $`R_C\ge0`$ and $`\mathrm{Tr}R_C=1-(1-p)^n-q`$. Thus the NPT marker block is not canceled by other target sectors.

### Resources and the role of filtering

Choose $`p=1/n`$. Then

```math
q=\left(1-\frac1n\right)^{n-1}>e^{-1},
\qquad\text{(11)}
```

with $`q\to e^{-1}`$. The inequality follows, for example, from
$`\log(1-x)>-x/(1-x)`$ for $`0\lt x\lt 1`$. The target dimension is $`n+2`$, and the number of occupied control basis states is $`|\Pi|`$.

The probability (11) is a useful property of a local entanglement-revealing filter. It is not a uniform lower bound on the amount of entanglement: supported control amplitudes may approach zero. For $`n\ge2`$ and $`0\lt p\lt 1`$, channel (4) is not entanglement breaking. On inputs supported in the marker space, projecting the output back onto that space gives $`(1-p)S\rho S^\dagger`$. This nonzero local-unitary branch preserves entanglement with a reference. The [separate qubit construction](qubit_example.md) establishes that entanglement-breaking slots attain the minimum of three calls and three alternatives.

## Complete erasure in every definite order

A different construction realizes the same criterion while ensuring that $`\mathcal N^n`$ is completely depolarizing on **every** input. Its target dimension is exponential rather than linear.

Take $`T=(\mathbb C^s)^{\otimes n}`$ with $`s\ge2`$, and define

```math
\mathcal N(\rho)
=\mathrm{Tr}_1(\rho)\otimes\frac{I_s}{s}.
\qquad\text{(12)}
```

The first register is discarded, the remaining registers shift left, and a maximally mixed register is appended. One Kraus representation is

```math
K_{ab}=\frac1{\sqrt s}
\sum_{w\in\{0,\ldots,s-1\}^{n-1}}
|wa\rangle\langle bw|,
\qquad 0\le a,b\lt s.
\qquad\text{(13)}
```

It is immediate from (12), or from summing (13), that the map is trace preserving and

```math
\mathcal N^n(X)=\mathrm{Tr}(X)\frac{I_{s^n}}{s^n}.
\qquad\text{(14)}
```

Start the target in $`|0\rangle^{\otimes n}`$. During the first $`n`$ calls, every discarded register comes from this original input, so every nonzero tuple has all discarded labels $`b=0`$. For appended slot labels $`\boldsymbol a`$, order $`\pi`$ produces

```math
s^{-n/2}|a_{\pi(0)}\cdots a_{\pi(n-1)}\rangle.
```

Let $`V_\pi`$ rearrange words by this rule. The switch output is

```math
\rho_{CT}^{\mathrm{out}}
=s^{-n}\sum_{\pi,\tau\in\Pi}
\alpha_\pi\overline{\alpha_\tau}|\pi\rangle\langle\tau|
\otimes V_\pi V_\tau^\dagger.
\qquad\text{(15)}
```

To make the representation convention explicit, define

```math
P_g|a_0\cdots a_{n-1}\rangle
=|a_{g^{-1}(0)}\cdots a_{g^{-1}(n-1)}\rangle.
```

Then $`P_gP_h=P_{gh}`$ and $`V_\pi=P_{\pi^{-1}}`$. This representation is faithful when $`s\ge2`$: the words with one symbol 1 and all other symbols 0 already distinguish every permutation. Its relative matrices satisfy

```math
V_\pi V_{\pi_0}^\dagger
=P_{(\pi_0^{-1}\pi)^{-1}},
```

so they commute exactly when $`G_\Pi`$ is abelian. Lemma 2 applies again.

The complete definite-order channel (14) discards all target information, but its coherently ordered realization can have an NPT joint output. The internal registers are explicitly part of the $`s^n`$-dimensional target; no external target-carrying memory is supplied. A single use of (12) is not entanglement breaking for $`n\ge2`$. This construction and the linear-dimension channel establish different resource statements and should not be combined into a claim that both properties are achieved by one channel.
