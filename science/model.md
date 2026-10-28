# Identical channels in coherently controlled orders

The target passes through several independent instances of the same noisy channel. A quantum controller chooses their order coherently. Every definite order therefore implements the same target channel. The question is whether retaining the controller can nevertheless produce entanglement between it and the target.

This page defines the supplied process and its resources. The [order criterion](order_criterion.md) gives a complete answer at the level of the selected permutations. The [qubit example](qubit_example.md) realizes the smallest possible numbers of calls and coherent alternatives.

## 1. Independent slots and chronological order

Let $`T\simeq\mathbb C^d`$ be a finite-dimensional target, and let

```math
\mathcal N(X)=\sum_{a=0}^{r-1}K_a X K_a^\dagger,
\qquad \sum_a K_a^\dagger K_a=I_T
```

be a completely positive trace-preserving map. There are $`n\ge1`$ independent slots, numbered $`0,\ldots,n-1`$, each implementing $`\mathcal N`$. Independence refers to the joint supplied resource: each slot has its own inaccessible noise environment. Equal marginal channels with shared environmental memory are a different resource.

A permutation $`\pi\in S_n`$ lists slots in **physical chronological order**:

```math
\pi=(\pi(0),\ldots,\pi(n-1)).
```

Thus $`012`$ means slot 0 first and slot 2 last. For an environmental index tuple $`\boldsymbol a=(a_0,\ldots,a_{n-1})`$, the target operator in this order is

```math
A_{\boldsymbol a,\pi}
=K_{a_{\pi(n-1)}}\cdots K_{a_{\pi(0)}}.
\qquad\text{(1)}
```

The tuple is indexed by physical slots, not by positions in time. The same slot index appears in every coherent branch. Summing over independent tuples traces out the separate noise environments; it does not provide the controller with their outcomes.

Choose a nonempty set of distinct orders $`\Pi\subseteq S_n`$. The controller $`C`$ has basis $`\{|\pi\rangle:\pi\in\Pi\}`$. The supplied generalized switch is the joint channel

```math
\mathfrak S_{\Pi,\mathcal N}(X)
=\sum_{\boldsymbol a}W_{\boldsymbol a}XW_{\boldsymbol a}^\dagger,
\qquad
W_{\boldsymbol a}
=\sum_{\pi\in\Pi}|\pi\rangle\langle\pi|
 \otimes A_{\boldsymbol a,\pi}.
\qquad\text{(2)}
```

The tensor-factor order throughout is $`C\otimes T`$. This is the standard generalized-switch resource; see the [primary-source comparisons](../references/RELATED_WORK.md#generalized-switches).

## 2. Normalization and Kraus independence

For each fixed order, its product operators form a Kraus family for $`\mathcal N^n`$. Orthogonality of the control projectors gives

```math
\sum_{\boldsymbol a}W_{\boldsymbol a}^\dagger W_{\boldsymbol a}
=\sum_{\pi\in\Pi}|\pi\rangle\langle\pi|
 \otimes\sum_{\boldsymbol a}A_{\boldsymbol a,\pi}^\dagger
 A_{\boldsymbol a,\pi}
=I_C\otimes I_T.
```

Equation (2) is independent of each slot's Kraus representation. To see this, write an alternative family in slot $`j`$ as

```math
\widetilde K^{(j)}_{b_j}
=\sum_{a_j}u^{(j)}_{b_j a_j}K_{a_j},
\qquad u^{(j)\dagger}u^{(j)}=I,
```

padding families by zero operators when needed. Each branch uses every slot exactly once, so the coefficient

```math
u_{\boldsymbol b\boldsymbol a}
=\prod_{j=0}^{n-1}u^{(j)}_{b_j a_j}
```

is independent of the order. Consequently
$`\widetilde W_{\boldsymbol b}=\sum_{\boldsymbol a}u_{\boldsymbol b\boldsymbol a}W_{\boldsymbol a}`$,
and the tensor-product isometry $`u`$ leaves the joint channel unchanged. Choosing a convenient Kraus basis in a proof supplies no additional environmental access.

## 3. Inputs and the entanglement task

The main existence statements use an independent input

```math
|\alpha\rangle\langle\alpha|_C\otimes\rho_T,
\qquad
|\alpha\rangle=\sum_{\pi\in\Pi}\alpha_\pi|\pi\rangle,
\qquad \sum_\pi|\alpha_\pi|^2=1,
\qquad \alpha_\pi\ne0.
\qquad\text{(3)}
```

The set $`\Pi`$ is the occupied support of this pure controller. Zero amplitudes are removed before applying the criterion. The output blocks are

```math
\rho_{CT}^{\mathrm{out}}
=\sum_{\pi,\tau\in\Pi}
\alpha_\pi\overline{\alpha_\tau}|\pi\rangle\langle\tau|
\otimes\sum_{\boldsymbol a}
A_{\boldsymbol a,\pi}\rho_T A_{\boldsymbol a,\tau}^\dagger.
\qquad\text{(4)}
```

Every diagonal target block is proportional to $`\mathcal N^n(\rho_T)`$. Tracing out the controller also gives $`\mathcal N^n(\rho_T)`$. The off-diagonal blocks contain correlations among differently ordered products and need not be determined by that diagonal channel.

Entanglement is evaluated across **the retained controller and target**, $`C:T`$. The positive-partial-transpose (PPT) condition is necessary for separability in every finite dimension. A negative partial transpose (NPT) therefore certifies entanglement. In $`2\times2`$ and $`2\times3`$, PPT is also sufficient; the [robustness calculation](robustness.md) uses that stronger low-dimensional fact. These are [established entanglement criteria](../references/RELATED_WORK.md#partial-transpose).

The impossibility half of the [main theorem](order_criterion.md#theorem-1-the-order-support-criterion) is stronger than (3): it preserves separability for every separable input, including initially classically correlated inputs and mixed controllers. The converse is an existence statement for pure controllers with the stated support. It is not a classification of arbitrary mixed controller states.

## 4. Supplied resources and scope

Ideal coherent order control is supplied. Every branch traverses every channel slot once. The controller and target start unentangled, and the noise environments are inaccessible. No target operations or target-carrying bypass are inserted between slots. The target's full Hilbert-space dimension is counted, including the internal registers or marker states used in the constructions.

The main output is unconditional: neither a control measurement nor a successful herald is part of the entanglement-generation claim. A final local filter may demonstrate entanglement already present. Its probability is stated separately.

This task differs from preserving an unknown target's entanglement with a remote reference or recovering an identity channel after measuring the controller. Entanglement across $`C:T`$ alone also does not certify indefinite causal order against unrestricted implementations. The [interpretation](interpretation.md) explains these distinctions and the channel families that remain nonentangling even with noncommuting order supports.
