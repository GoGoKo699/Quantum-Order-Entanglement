# Three entanglement-breaking calls suffice

The [general theorem](order_criterion.md) requires at least three calls and at least three coherent order alternatives. Both minima are attained with a qubit target and a channel that individually breaks entanglement. Moreover, every complete definite order is completely depolarizing.

## 1. The channel

Let $`|\pm\rangle=(|0\rangle\pm|1\rangle)/\sqrt2`$, and define

```math
K_0=|+\rangle\langle0|,
\qquad K_1=|-\rangle\langle1|.
\tag{1}
```

The channel measures the target in the computational basis and prepares the corresponding $`X`$-basis state:

```math
\mathcal N(X)
=X_{00}|+\rangle\langle+|
 +X_{11}|-\rangle\langle-|.
\tag{2}
```

It is trace preserving because $`K_0^\dagger K_0+K_1^\dagger K_1=I_2`$. Its measure-and-prepare form makes it entanglement breaking: when applied to one part of any target–reference state, the output is a sum of positive reference operators tensored with the prepared pure target states.

Both computational-basis diagonal entries of $`\mathcal N(X)`$ equal $`\operatorname{Tr}(X)/2`$. Therefore

```math
\mathcal N^2(X)=\operatorname{Tr}(X)\frac{I_2}{2}
=\Delta(X).
\tag{3}
```

The channel is also unital, so $`\mathcal N^3=\Delta`$. Equation (3) holds on the full operator space, including off-diagonal input operators; it is not merely agreement on selected states.

## 2. Input and coherent orders

Use three independent slots implementing (1), with inaccessible noise environments. Initialize the target in $`|0\rangle`$ and the controller in

```math
|+_3\rangle
=\frac{|012\rangle+|021\rangle+|102\rangle}{\sqrt3}.
\tag{4}
```

The words are chronological. For example, $`012`$ corresponds to $`K_{i_2}K_{i_1}K_{i_0}`$. Relative to $`012`$, the other two orders are the transpositions of positions $`(1\;2)`$ and $`(0\;1)`$. They do not commute.

For compact matrix notation, identify these three order labels with controller states $`|0\rangle_C,|1\rangle_C,|2\rangle_C`$, in the displayed order. The joint basis is

```math
|0,0\rangle,|0,1\rangle,
|1,0\rangle,|1,1\rangle,
|2,0\rangle,|2,1\rangle.
```

## 3. Exact output from the Kraus sum

Write $`K_j=A_j/\sqrt2`$, where

```math
A_0=\begin{pmatrix}1&0\\1&0\end{pmatrix},
\qquad
A_1=\begin{pmatrix}0&1\\0&-1\end{pmatrix}.
```

For each physical-slot tuple $`\boldsymbol i=(i_0,i_1,i_2)`$, concatenate the three vectors
$`A_{i_{\pi(2)}}A_{i_{\pi(1)}}A_{i_{\pi(0)}}|0\rangle`$
into a six-component integer vector $`b_{\boldsymbol i}`$. The common amplitude factor is $`1/\sqrt{24}`$: three factors $`1/\sqrt2`$ from the channel and one $`1/\sqrt3`$ from the control.

| Slot labels | Integer vector $`b_{\boldsymbol i}`$ |
|---|---|
| $`000`$ | $`(1,1,1,1,1,1)^T`$ |
| $`001`$ | $`(1,-1,1,1,1,-1)^T`$ |
| $`010`$ | $`(1,1,1,-1,0,0)^T`$ |
| $`011`$ | $`(-1,1,-1,1,0,0)^T`$ |
| $`100`$ | $`(0,0,0,0,1,1)^T`$ |
| $`101`$ | $`(0,0,0,0,-1,1)^T`$ |
| $`110,111`$ | $`0`$ |

Summing the inaccessible noise outcomes gives

```math
\rho=\frac1{24}\sum_{\boldsymbol i}
b_{\boldsymbol i}b_{\boldsymbol i}^T
=\frac1{12}
\begin{pmatrix}
2&0&2&0&1&0\\
0&2&0&0&0&1\\
2&0&2&0&1&0\\
0&0&0&2&1&0\\
1&0&1&1&2&0\\
0&1&0&0&0&2
\end{pmatrix}.
\tag{5}
```

Each diagonal controller block is $`I_2/6`$, as required by the completely depolarizing definite-order channel. Equation (5) is the unconditional output.

## 4. An exact entanglement certificate

For the normalized vector

```math
v=\frac13(-2,0,2,0,0,-1)^T,
```

direct partial transposition of the target gives

```math
\langle v|\rho^{\Gamma_T}|v\rangle=-\frac1{54}.
\tag{6}
```

Thus the output is NPT and entangled. An additional exact certificate is

```math
\det(\rho^{\Gamma_T})=-\frac1{248832}.
\tag{7}
```

Neither conclusion conditions on a measurement result. The [exact-arithmetic program](../verification/verify_exact.py) reconstructs (5) from the eight independent Kraus tuples and verifies (3), (6) and (7).

## 5. A local projection exposes two-qubit entanglement

Define orthonormal controller vectors

```math
|a\rangle=\frac{|1\rangle-|0\rangle}{\sqrt2},
\qquad |b\rangle=|2\rangle.
```

Project the controller onto their span and identify that two-dimensional subspace with a qubit. The success probability is $`1/2`$. In basis $`a0,a1,b0,b1`$, the normalized output is

```math
\sigma=
\begin{pmatrix}
0&0&0&0\\
0&\frac13&\frac1{6\sqrt2}&-\frac1{6\sqrt2}\\
0&\frac1{6\sqrt2}&\frac13&0\\
0&-\frac1{6\sqrt2}&0&\frac13
\end{pmatrix}.
\tag{8}
```

The principal minor of $`\sigma^{\Gamma_T}`$ on $`\{a0,b1\}`$ is

```math
\det\begin{pmatrix}
0&1/(6\sqrt2)\\
1/(6\sqrt2)&1/3
\end{pmatrix}
=-\frac1{72}.
\tag{9}
```

This local operation reveals an entangled two-qubit state. It is not a pure Bell pair in one copy. The unconditional certificate (6) remains the main entanglement-generation result.

## 6. What is minimal

Any two distinct order alternatives have a cyclic relative group, so the [universal obstruction](order_criterion.md#any-two-alternatives-are-nonentangling) rules out this capability for every identical channel and every separable input. With at most two channel slots there are at most two distinct permutations. Construction (1)–(5) therefore attains both necessary minima:

| Resource | Attained minimum for the existence of an entangling identical-channel switch |
|---|---:|
| Independent channel calls | 3 |
| Occupied coherent order alternatives | 3 |
| Nontrivial target dimension | 2 |

The target-dimension minimum simply reflects that a one-dimensional target cannot be entangled. The nontrivial content is that a qubit suffices while every individual slot is entanglement breaking and every complete definite-order channel is $`\Delta`$.

These minima are existence statements. Three cyclic orders still obey the obstruction, and many channel families remain nonentangling even on nonabelian supports. The [interpretation](interpretation.md) gives those boundaries. The [robustness page](robustness.md) derives an exact noise threshold for this particular output and controller-dephasing model.
