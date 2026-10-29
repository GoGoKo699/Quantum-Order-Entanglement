# Scientific account

Every definite order of independent identical channels has the same target action. Coherent order control nevertheless retains off-diagonal correlations among the differently ordered Kraus products. This account identifies exactly which pure order supports can turn those correlations into entanglement between the retained controller and target.

## Reading route

1. [Model and resources](model.md): independent slots, chronological permutations, Kraus invariance and the retained bipartition.
2. [The order-support criterion](order_criterion.md): the abelian obstruction, its quantifiers, and the three-alternative minimum.
3. [Channel realizations](channel_realizations.md): the inherited conditional-unitary lemma, a linear-dimension converse and a separate complete-erasure construction.
4. [Minimal qubit example](qubit_example.md): three identical entanglement-breaking channels, the exact joint state and a local projection.
5. [Robustness](robustness.md): the exact controller-dephasing transition and a general sufficient output-distance bound.
6. [Shared physical noise](noisy_separation.md): specified retained-state/recovery protocols, exact certificates, uniform separation and charged costs.
7. [Interpretation and boundaries](interpretation.md): channel-specific obstructions, resource costs, and distinctions from communication and causal certification.

The [related-work account](../references/RELATED_WORK.md) attributes the standard generalized switch, Kraus-freedom arguments, conditional-unitary criterion and earlier multiorder settings. The [verification guide](../verification/README.md) gives commands and distinguishes exact finite certificates from the analytical theorem.

## Claim and proof map

| Claim | Authoritative proof or calculation |
|---|---|
| Commuting relative orders are universally separability preserving | [Theorem 1 and product-Kraus proof](order_criterion.md#theorem-1-the-order-support-criterion) |
| One $`n+2`$-level channel realizes every nonabelian support at fixed $`n`$ | [Marker construction](channel_realizations.md#the-linear-dimension-channel) |
| Nonabelian supports can work while every complete definite-order channel erases every input | [Shift/reset construction](channel_realizations.md#complete-erasure-in-every-definite-order) |
| Three calls and three coherent alternatives suffice with an entanglement-breaking qubit channel | [Exact output and witness](qubit_example.md#3-exact-output-from-the-kraus-sum) |
| Exact dephasing threshold for the minimal example | [Partial-transpose spectrum](robustness.md#exact-separability-transition) |
| Nonabelian support does not suffice for every channel or for an EB-only converse | [Channel-family boundaries](interpretation.md#channel-families-that-remain-nonentangling) |

The universal theorem concerns all finite target dimensions. Its converse uses pure controllers with nonzero amplitudes on their selected support. Arbitrary mixed-controller necessity and a fixed-target-dimension classification are not asserted.

## Shared physical noise and the recovery connection

The [uniform noisy separation](noisy_separation.md) extends the concrete channel story while keeping its operational tasks distinct. It defines the common tilted raw channel, physical phase noise and both specified protocols; reconstructs exact rational partial-transpose and Bell-witness certificates; and proves a Stinespring continuity bound that fills the intervals between grid points.

| Statement | Authoritative location |
|---|---|
| All three two-bit allocations of the retained protocol are separable for $\lvert\delta\rvert\le0.2$ | [Uniform theorem](noisy_separation.md#uniform-separation) and [exact grid](noisy_separation.md#exact-grid-certificate) |
| The specified accepted four-call pair is NPT with strictly positive probability and fidelity margins on the same interval | [Continuity proof](noisy_separation.md#continuity-proof) |
| Resource and conditioning differences remain charged | [Operational meaning](noisy_separation.md#operational-meaning) |
| Arbitrary-controller recovery optimum and its larger tilted interval | [Sister frontier](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/recovery_frontier.md) and [tilted readout theorem](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/tilted_readout.md) |

The separation proof is authoritative here. The common raw-slot/controller foundation and recovery optimization are authoritative in Quantum Order Distillation. These shared results are credited once across the family; the original universal order-support theorem and exact-recovery threshold retain their distinct hypotheses and conclusions.

## Learning route

The [Watrous bridge](../learning/WATROUS_BRIDGE.md) connects the selected textbook's channels, separable maps and permutation operators to this model. The [30-milestone map](../learning/MILESTONES.md) organizes the common understanding targets from local ingredients to the complete result. These explanations support the reading route above; the topic pages retain the authoritative statements and full proofs.
