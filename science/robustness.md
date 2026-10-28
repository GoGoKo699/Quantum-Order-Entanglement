# Noise tolerance of the minimal example

The [three-call qubit output](qubit_example.md#3-exact-output-from-the-kraus-sum) has a finite negative partial-transpose margin. This page gives an exact separability transition for one specified noise family and a conservative bound for arbitrary output perturbations. These statements concern the minimal example, not a uniform entanglement amount for all nonabelian order supports.

## Controller dephasing and output white noise

Replace the initial uniform pure controller by

```math
\omega_C(\eta)
=\eta|+_3\rangle\langle+_3|
 +(1-\eta)\frac{I_3}{3},
\qquad 0\le\eta\le1.
\qquad\text{(1)}
```

This channel fully dephases the controller in its order basis with probability $`1-\eta`$. The parameter $`\eta`$ multiplies every off-diagonal controller element.

Every definite-order target output in the example is $`I_2/2`$. Hence the joint output is exactly

```math
\rho_\eta=\eta\rho+(1-\eta)\frac{I_6}{6},
\qquad\text{(2)}
```

where $`\rho`$ is the noiseless joint state. The same calculation therefore describes white noise added to the joint output. It does not give a threshold for arbitrary errors in the three channel slots.

## A simple fixed witness

Use the normalized vector $`v=(-2,0,2,0,0,-1)^T/3`$ from the exact example. Then

```math
\langle v|\rho_\eta^{\Gamma_T}|v\rangle
=-\frac\eta{54}+\frac{1-\eta}{6}
=\frac{9-10\eta}{54}.
\qquad\text{(3)}
```

This witness certifies entanglement for $`\eta>9/10`$, or a dephasing/white-noise admixture below $`10\%`$. That is a sufficient condition supplied by one fixed witness. The exact transition is less restrictive.

## Exact separability transition

Set $`M=12\rho`$. Its partially transposed characteristic polynomial factors as

```math
\det(xI_6-M^{\Gamma_T})
=(x-1)(x-2)(x-3)(x^3-6x^2+5x+2).
\qquad\text{(4)}
```

The cubic has one root in each of $`(-1,0)`$, $`(1,2)`$ and $`(4,5)`$, as follows from its signs at the endpoints and its degree. Thus $`M^{\Gamma_T}`$ has exactly one negative eigenvalue, denoted $`x_-`$. Because the noise in (2) is proportional to the identity, the partial-transpose eigenvalues become

```math
\frac{1-\eta}{6}+\frac{\eta x_j}{12}.
```

Only the branch from $`x_-`$ can turn negative. It vanishes at

```math
\eta_* =\frac{2}{2-x_-}.
\qquad\text{(5)}
```

Equivalently,

```math
\det(12\rho_\eta^{\Gamma_T})
=4(4-\eta^2)(4-7\eta^2+2\eta^3),
```

so the threshold is the unique root in $`[0,1]`$ of

```math
2\eta_*^3-7\eta_*^2+4=0,
\qquad
0.8724474860298<\eta_*<0.8724474860299.
\qquad\text{(6)}
```

The polynomial is strictly decreasing on $`(0,1)`$ and changes sign between the endpoints. The displayed decimal bracket is certified by exact rational substitution in the [verification program](../verification/verify_exact.py).

The system has dimension $`3\times2`$. The established [Peres–Horodecki criterion](../references/RELATED_WORK.md#partial-transpose) makes PPT necessary and sufficient for separability in this dimension. Therefore the exact result, including the boundary, is

```math
\begin{aligned}
\rho_\eta\text{ is separable}&\iff 0\le\eta\le\eta_*,\\
\rho_\eta\text{ is NPT}&\iff \eta_*<\eta\le1.
\qquad\text{(7)}
\end{aligned}
```

The admissible admixture is consequently

```math
1-\eta<1-\eta_*
\simeq0.127552513970178.
```

The example remains entangled below approximately **12.7553%** of the specified noise admixture. The $`10\%`$ value from (3) is the threshold of a particular rational witness, while (7) is the exact state-separability boundary. PPT positivity alone would not establish separability in the larger dimensions of the general construction.

## A bound for arbitrary output perturbations

Let

```math
W=(|v\rangle\langle v|)^{\Gamma_T}.
```

For every separable state $`\sigma`$, $`\operatorname{Tr}(W\sigma)\ge0`$. The Schmidt weights of $`v`$ are $`8/9`$ and $`1/9`$, so $`\|W\|_\infty=8/9`$. For any physical perturbed output $`\widetilde\rho`$, Hölder's inequality gives

```math
\operatorname{Tr}(W\widetilde\rho)
\le-\frac1{54}+\frac89\|\widetilde\rho-\rho\|_1.
```

It follows that

```math
\|\widetilde\rho-\rho\|_1<\frac1{48}
\qquad\text{(8)}
```

is a sufficient entanglement certificate. With trace distance defined as
$`D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$,
the corresponding radius is $`1/96`$.

This norm ball is conservative; it is not claimed to be largest possible. It is also distinct from an implementation-specific bound on gate errors or channel imperfections. Such a bound would require relating those physical errors to the final joint state distance.
