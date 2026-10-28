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

## Read the science

Start with the [scientific account](science/README.md), or use a direct route below.

| To inspect | Read |
|---|---|
| Supplied process, independent slots and exact input assumptions | [Model](science/model.md) |
| The iff statement and product-Kraus impossibility proof | [Order criterion](science/order_criterion.md) |
| Linear-dimension converse and separate complete-erasure construction | [Channel realizations](science/channel_realizations.md) |
| Exact entanglement-breaking qubit construction and local projection | [Minimal example](science/qubit_example.md) |
| Noise model, exact threshold and conservative perturbation bound | [Robustness](science/robustness.md) |
| Channel-specific obstructions and operational meaning | [Interpretation](science/interpretation.md) |
| Inherited results and closest primary sources | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Reproducible finite certificates | [Verification](verification/README.md) |

The conditional-unitary commutation criterion is inherited from Roszak, and the two-slot identical-channel obstruction is explicit in Chiribella et al. Generalized switches, cyclic-coset organization and three-identical-channel metrology also have prior sources. The contribution here is the complete constrained order-support criterion, its repeated-channel realizations and the exact minimal example. The [comparison account](references/RELATED_WORK.md) identifies the source of each ingredient.

## Reproduce the finite checks

The main certificate uses Python's standard library:

```bash
python3 verification/verify_exact.py
```

Optional numerical checks of the marker construction use the pinned NumPy dependency:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_marker.py
```

The exact program reconstructs the qubit output from its Kraus definition, verifies the full channel-square identity and NPT certificates, and checks the noise-threshold algebra. The marker program checks finite instances at three and four calls. Neither replaces the analytical proof for arbitrary order supports and channel dimensions.

## Scope

Ideal coherent order control is supplied, with independent channel instances, inaccessible environments and no intermediate target operations or target-carrying bypass. The converse is existential over channels; a nonabelian support does not entangle every noise model. The universal constructions are not entanglement breaking, while the minimal qubit example is. The full-dephasing threshold is specific to its stated one-parameter noise family.

The retained controller–target entanglement task is distinct from heralded message recovery, communication capacity and device-independent causal certification. General mixed-controller necessity and an EB-only classification are outside the theorem.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
