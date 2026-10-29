# Quantum Order Entanglement

**Which coherent orders of identical noisy channels can generate entanglement between the order controller and the target?**

Every definite order of $`n`$ independent copies of a channel $`\mathcal N`$ implements $`\mathcal N^n`$. This project gives an exact criterion for when coherent control over those orders can nevertheless produce entanglement across the retained controller–target bipartition.

For an occupied pure-control support $`\Pi\subseteq S_n`$, choose any reference $`\pi_0\in\Pi`$ and form

```math
G_\Pi=\left\langle\pi_0^{-1}\pi:\pi\in\Pi\right\rangle.
```

The order family is **nonentangling for every finite-dimensional identical channel if and only if $`G_\Pi`$ is abelian**. In the abelian case the joint channel has product Kraus operators and preserves every separable input. In the nonabelian case an explicit channel produces a negative-partial-transpose (NPT) output for every pure controller with nonzero amplitudes on that support.

| Result | Supported consequence |
|---|---|
| Exact order-support criterion | A channel-independent test of which coherent order families can ever generate the entanglement |
| Linear-dimension converse | One fixed $`n+2`$-level channel works for every nonabelian support at a given $`n`$ |
| Minimal example | Three calls and three coherent alternatives suffice with an entanglement-breaking qubit channel |
| Complete definite-order erasure | In the qubit example, $`\mathcal N^2=\Delta`$, yet the three-call coherent output is entangled |
| Exact robustness for that example | Entanglement survives a full-controller-dephasing admixture below approximately $`12.7553\%`$ |

The minimal channel measures in the $`Z`$ basis and prepares the corresponding $`X`$-basis state:

```math
K_0=|+\rangle\langle0|,
\qquad K_1=|-\rangle\langle1|.
```

A uniform controller on chronological orders $`012,021,102`$ and target $`|0\rangle`$ gives an unconditional $`3\times2`$ state with an exact partial-transpose witness value $`-1/54`$. Any two order alternatives are universally nonentangling for identical channels, even when more than two slots are available. The [full example](science/qubit_example.md) proves the attained minima and gives the output matrix.

## A robust connection to heralded recovery

The [shared-noise theorem](science/noisy_separation.md#uniform-separation) compares two specified protocols on the same raw measure–prepare channel family with a 1% depolarizing admixture. Every physical control bit has an independent 10% phase-flip probability. Uniformly over axis tilts $`|\delta|\le0.2`$ radians:

| Protocol | Certified output |
|---|---|
| Three chronological orders $`012,021,102`$, uniform controller, target $`\lvert0\rangle`$, any three occupied two-bit codewords | The unconditional retained $`C:T`$ state is separable for every assignment of the three orders to those codewords. |
| Four raw calls, the specified eight orders and three-bit physical encoding, fixed P2 accepted branch, Bell input | The accepted $`R:T`$ state is NPT, with $`0.035\lt p\lt 0.095`$ and Bell fidelity $`F>101/190`$. |

The proof reconstructs 249 exact retained-state partial-transpose certificates and 83 exact recovery witnesses, then extends the strict margins to the whole interval. Its positive lower bound acts on the occupied $`3\times2`$ support. The [full statement and proof](science/noisy_separation.md) keep the bipartitions, conditioning and resources explicit: three versus four calls, two versus three controller bits, and unconditional versus accepted outputs. This establishes a simultaneous robust example for these protocols.

The sister repository [Quantum Order Distillation](https://github.com/GoGoKo699/Quantum-Order-Distillation) owns the [common raw-slot model](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/noisy_routing_model.md), [controller characterization](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/controller_optimization.md), [full recovery frontier](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/recovery_frontier.md) and [tilted optimality proof](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/tilted_readout.md). Both tracks use the same Watrous educational anchor. Retained controller–target entanglement and recovered reference–target entanglement remain separate tasks.

The sister track also gives a [complete six-order three-call recovery frontier](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/native_three_call_frontier.md) for the fixed rank-two measure-$`Z`$/prepare-$`X`$ channel under global logical dephasing, with an [exact randomized one-/two-/three-call cost envelope](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/randomized_call_cost.md). It evaluates the accepted target-only channel after corrected fine labels are averaged. That half-diamond recovery task is separate from retaining $`C:T`$, and from the four-call full-rank family with physical local noise.

## Read the science

Start with the [scientific account](science/README.md), or use a direct route below.

| To inspect | Read |
|---|---|
| Supplied process, independent slots and exact input assumptions | [Model](science/model.md) |
| The iff statement and product-Kraus impossibility proof | [Order criterion](science/order_criterion.md) |
| Linear-dimension converse and separate complete-erasure construction | [Channel realizations](science/channel_realizations.md) |
| Exact entanglement-breaking qubit construction and local projection | [Minimal example](science/qubit_example.md) |
| Noise model, exact threshold and conservative perturbation bound | [Robustness](science/robustness.md) |
| Retained entanglement and accepted recovery under physical controller noise | [Uniform separation theorem and proof](science/noisy_separation.md) |
| Channel-specific obstructions and operational meaning | [Interpretation](science/interpretation.md) |
| Inherited results and closest primary sources | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Reproducible finite certificates | [Verification](verification/README.md) |

The conditional-unitary commutation criterion is inherited from Roszak, and the two-slot identical-channel obstruction is explicit in Chiribella et al. Generalized switches, cyclic-coset organization and three-identical-channel metrology also have prior sources. The contribution here is the complete constrained order-support criterion, its repeated-channel realizations and the exact minimal example. The [comparison account](references/RELATED_WORK.md) identifies the source of each ingredient.

## Learn the project

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [Watrous bridge](learning/WATROUS_BRIDGE.md) identifies focused readings, translates the source's notation, and develops the connections to coherent order control. The [30-milestone map](learning/MILESTONES.md) organizes the project's understanding targets and their dependencies.

Begin with the bridge's physical question, then use the map alongside the linked scientific pages. Its background phase assembles states, channels, entanglement and permutation representations into the precise model. Its narrative phase connects the order-support theorem and minimal example to noisy retained states, accepted recovery witnesses, continuity and charged success costs. The map is shared by all readers; it is defined by the science rather than by an assumed level of prior knowledge.

| Reading purpose | Route |
|---|---|
| Understand the scientific story | [Model](science/model.md), [criterion](science/order_criterion.md), [realizations](science/channel_realizations.md), then [interpretation](science/interpretation.md) |
| Build the conceptual foundations | [Watrous bridge](learning/WATROUS_BRIDGE.md) alongside [M01–M30](learning/MILESTONES.md) |
| Inspect a concrete entanglement certificate | [Qubit example](science/qubit_example.md), [noise threshold](science/robustness.md), then [verification](verification/README.md) |
| Locate a claim or proof dependency | [Scientific claim map](science/README.md#claim-and-proof-map), [related work](references/RELATED_WORK.md), and [LLM reading guide](llms.txt) |

## Reproduce the finite checks

The main certificate uses Python's standard library:

```bash
python3 verification/verify_exact.py
```

Optional numerical checks of the marker construction use the pinned NumPy dependency:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_marker.py
python3 verification/audit_verify.py --root verification/certificates --rebuild
```

The original exact program reconstructs the qubit output from its Kraus definition, verifies the full channel-square identity and NPT certificates, and checks the noise-threshold algebra. The shared verifier additionally reconstructs all 249 noisy retained-state and 83 recovery certificates, along with the sister recovery-frontier identities. The marker program checks finite instances at three and four calls. Neither replaces the analytical proof for arbitrary order supports and channel dimensions.

## Scope

The order-support theorem supplies ideal coherent order control; the shared-noise theorem instead fixes its explicit unobserved physical phase noise. Both use independent channel instances, inaccessible environments and no intermediate target operations or target-carrying bypass.

The converse is existential over channels; a nonabelian support does not entangle every noise model. The universal constructions are not entanglement breaking, while the minimal qubit example is. The full-dephasing threshold is specific to its stated one-parameter noise family.

The retained controller–target entanglement task is distinct from heralded message recovery, communication capacity and device-independent causal certification. General mixed-controller necessity and an EB-only classification are outside the theorem.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
