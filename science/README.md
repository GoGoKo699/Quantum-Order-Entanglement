# Scientific account

Every definite order of independent identical channels has the same target action. Coherent order control nevertheless retains off-diagonal correlations among the differently ordered Kraus products. This account identifies exactly which pure order supports can turn those correlations into entanglement between the retained controller and target.

## Reading route

1. [Model and resources](model.md): independent slots, chronological permutations, Kraus invariance and the retained bipartition.
2. [The order-support criterion](order_criterion.md): the abelian obstruction, its quantifiers, and the three-alternative minimum.
3. [Channel realizations](channel_realizations.md): the inherited conditional-unitary lemma, a linear-dimension converse and a separate complete-erasure construction.
4. [Minimal qubit example](qubit_example.md): three identical entanglement-breaking channels, the exact joint state and a local projection.
5. [Robustness](robustness.md): the exact controller-dephasing transition and a general sufficient output-distance bound.
6. [Interpretation and boundaries](interpretation.md): channel-specific obstructions, resource costs, and distinctions from communication and causal certification.

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

## Learning route

The [Watrous bridge](../learning/WATROUS_BRIDGE.md) connects the selected textbook's channels, separable maps and permutation operators to this model. The [30-milestone map](../learning/MILESTONES.md) organizes the common understanding targets from local ingredients to the complete result. These explanations support the reading route above; the topic pages retain the authoritative statements and full proofs.
