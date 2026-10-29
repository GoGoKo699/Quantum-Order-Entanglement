# What the order criterion changes

Identical channels commute under ordinary composition: every definite order of $`n`$ copies implements $`\mathcal N^n`$. The [main theorem](order_criterion.md) nevertheless distinguishes their coherent order families. The distinction concerns the permutations of independent noise labels in the off-diagonal controller blocks, rather than a difference among the definite-order target channels.

## The criterion concerns order choices

The relative group $`G_\Pi`$ describes the selected slot permutations. It is not a group of target gates, a commutativity test on one chosen Kraus decomposition, or a claim that the identical channel fails to commute with itself.

When the relative permutations commute, one change of the formal Kraus-index basis diagonalizes all of them. The resulting product Kraus representation proves that the joint channel preserves separability. Increasing the number of alternatives within the same abelian family cannot remove that obstruction.

When the relative permutations do not commute, the marker channel converts their natural permutation representation into a retained controller–target state. The known conditional-unitary criterion then certifies entanglement. Thus noncommutation is both necessary for some identical channel to work and sufficient for an explicit one to do so.

The quantifier over channels matters. A nonabelian support permits the capability; it does not make every noise model entangling. The examples below show several distinctions that would be lost by suppressing that quantifier.

## Channel families that remain nonentangling

### Depolarizing channels

For generalized switches of depolarizing channels, the target blocks lie in the linear span of $`\rho`$ and $`I`$. This is supplied by [Procopio et al.](../references/RELATED_WORK.md#procopio2019); the fully depolarizing specialization is also treated by [Sazim et al. and Wilson–Chiribella](../references/RELATED_WORK.md#permutation-structure-for-depolarizers).

Controller–target separability follows directly from that old block formula. Diagonalize the independent input target state as $`\rho=\sum_t r_t|t\rangle\langle t|`$. Every target block is diagonal in the same basis, so the positive joint output can be written

```math
\rho_{CT}^{\mathrm{out}}
=\sum_t C_t\otimes|t\rangle\langle t|,
\qquad C_t\ge0.
\qquad\text{(1)}
```

After absorbing each nonzero $`\mathrm{Tr}C_t`$ into a probability, this is a separable decomposition. This inference holds even for nonabelian supports and arbitrarily many orders. It is not a new depolarizer formula or a denial of their communication advantages.

### Pauli channels

Consider a qubit Pauli channel with Kraus operators
$`K_a=\sqrt{p_a}\sigma_a`$, where $`\sigma_a\in\{I,X,Y,Z\}`$.
For a fixed environmental tuple, changing the order of its Pauli factors changes their product only by a scalar phase. The probability factor $`\prod_j\sqrt{p_{a_j}}`$ is independent of the order. Consequently every joint Kraus operator factors into a diagonal controller operator and a fixed target Pauli product.

The switch therefore preserves separability for arbitrary order supports and all separable controller–target inputs. The minimal measure-$`Z`$/prepare-$`X`$ channel is outside this common-input/output-axis Pauli form. Its entanglement-breaking property alone does not force the product-Kraus factorization.

### A common final entanglement-breaking slot

Suppose every selected order places the same physical slot last, and that slot's channel is entanglement breaking. Then the joint process factors as

```math
(\mathrm{id}_C\otimes\mathcal N)\circ\mathfrak S_{\mathrm{earlier}},
```

so the final local target channel destroys all $`C:T`$ entanglement. The earlier relative orders can still be nonabelian. For example, $`0123,0213,1023`$ all end in slot 3 while their relative permutations on the first three slots do not commute.

This is why the general theorem is **not** an if-and-only-if classification restricted to entanglement-breaking channels. The [qubit example](qubit_example.md) proves that such channels attain the smallest possible entangling architecture, not that they realize every nonabelian support.

## Communication and entanglement are different tasks

Three bipartitions or outputs must be kept distinct:

| Task | Relevant systems and endpoint |
|---|---|
| This project | Retain $`C`$ and $`T`$; create entanglement across $`C:T`$ from an independent input |
| Heralded message recovery | Measure the controller and recover an unknown target, including its entanglement with an untouched reference $`R`$ |
| Communication capacity | Optimize an asymptotic communication protocol under a specified assistance model |

The identical two-channel self-switch in [Chiribella et al.](../references/RELATED_WORK.md#chiribella2021) illustrates the distinction: its controller–target output is separable, yet appropriate channels and a control measurement permit perfect message transmission. Conversely, the present entangled output from a known target input does not by itself establish any channel-capacity advantage.

Coherent cyclic orders are likewise useful in communication while the universal abelian obstruction applies to retained controller–target entanglement. These results describe different capabilities of the same supplied higher-order process.

Reduced controller decoherence is also insufficient to certify joint entanglement. For example, switching two completely depolarizing channels with a maximally mixed target gives a product $`C:T`$ state, although the controller coherence is reduced. The exact witnesses in this project assess the joint state directly. The related [metrology literature](../references/RELATED_WORK.md#goldberg2023) uses reduced-controller statistics for a different purpose.

## Resources of the constructions

| Construction | Calls | Target dimension | Slot channel | Additional property |
|---|---:|---:|---|---|
| [Marker channel](channel_realizations.md#the-linear-dimension-channel) | $`n`$ | $`n+2`$ | One channel fixed by $`n`$ | Works for every nonabelian pure order support; marker filter probability exceeds $`e^{-1}`$ |
| [Shift/reset channel](channel_realizations.md#complete-erasure-in-every-definite-order) | $`n`$ | $`s^n`$, $`s\ge2`$ | Discard one register, shift, append maximally mixed register | $`\mathcal N^n=\Delta`$ on every input |
| [Minimal qubit channel](qubit_example.md) | 3 | 2 | Measure $`Z`$, prepare $`X`$ | Every slot is entanglement breaking and $`\mathcal N^2=\Delta`$ |

The number of coherent alternatives is a separate resource from the number of calls. The marker and shift/reset constructions allow any specified support; the minimal example uses three alternatives. The marker filter's nonvanishing probability does not imply a uniform entanglement amount for arbitrarily small supported amplitudes.

The generalized switch itself is supplied as a nontrivial controller–target process. These results do not compare it with unrestricted circuits containing arbitrary controlled gates or protected target memories. They also do not infer device-independent causal nonseparability from output entanglement. The [model](model.md#4-supplied-resources-and-scope) states exactly which operations are being compared.

## The shared-noise comparison

The [uniform separation theorem](noisy_separation.md#uniform-separation) makes one part of this distinction quantitative. With a 1% depolarizing admixture, 10% independent phase flips per physical controller bit and $|\delta|\le0.2$ radians, the fixed three-order retained experiment is separable for all three inequivalent two-bit allocations. On the same channel/noise interval, a fixed four-call accepted branch produces an NPT reference–target pair with $0.035<p<0.095$ and $F>101/190$.

The [proof](noisy_separation.md#continuity-proof) combines exact rational certificates with a continuity estimate. Its retained-state positive lower bound acts on the occupied six-dimensional support; unused physical codewords retain zero eigenvalues. The [resource table](noisy_separation.md#operational-meaning) charges three versus four calls and two versus three controller bits, as well as unconditional versus accepted outputs. Rejected attempts require fresh inputs for the stated recovery cost.

The sister project's [frontier theorem](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/recovery_frontier.md#frontier-theorem) optimizes a different task: corrected Bell fidelity at a specified accepted probability over arbitrary physical controllers in the fixed four-call architecture. It does not optimize retained $C:T$ entanglement. In particular, a Bell-fidelity bound at or below one half is not a separability classification for arbitrary complex-controller outputs. The comparison here remains specific to the stated retained protocol, rather than a universal three-call impossibility claim.

## Scientific conclusion

The obstruction is a property of the order family, while its violation must be converted into a physical channel realization. Abelian relative orders always admit a product-Kraus description. Nonabelian relative orders admit an explicit NPT realization, and the smallest example survives even when each slot is entanglement breaking and the complete definite-order target channel is fully depolarizing.

The general result relies on established Kraus freedom, simultaneous diagonalization and conditional-unitary entanglement criteria. Its content is the complete constrained order-support boundary and the channels that attain it. The [related-work account](../references/RELATED_WORK.md) separates those statements from their inherited ingredients.
