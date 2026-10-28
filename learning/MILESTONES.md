# Project understanding map: 30 milestones

This map organizes quantum order entanglement into exactly **30 milestones**, M01 through M30. Its targets, dependencies and order follow the scientific project and are common to every reader. The final milestones join the local ingredients into the complete contribution and its operational limits.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [Watrous bridge](WATROUS_BRIDGE.md) owns the source version, focused section pointers, notation translations and locally supplied explanations. Use it alongside this map and the canonical scientific pages linked below.

## Allocation and route

The allocation is **10 background/preliminaries milestones, followed by 20 narrative/innovation milestones**. The background moves from states and channels through separability and permutation operators to the complete supplied model. The narrative moves from the relative-order obstruction through a physically realizable converse and the minimal example to the whole contribution and its limits. Each phase ends in synthesis. The map identifies understanding targets; it does not replace the complete proofs or claim to cover every calculation.

The focused Watrous readings cover states and composite systems (§§2.1.2–2.1.3), channel representations (§2.2.2), separable states and maps (§§6.1.1–6.1.2), PPT (§6.2.3), and permutation operators (§7.1.1). The bridge identifies additional linear-algebra and norm facts where they are used, translates notation, and supplies the project-specific steps. Primary research papers provide attribution and proof dependencies, not additional educational anchors.

| Phase | Milestones | Connection established |
|---|---|---|
| Background/preliminaries | M01–M04 | States, channels, inaccessible environments and independent composition |
| Background/preliminaries | M05–M09 | Order coherence, separability, partial transpose and permutation representations |
| Background/preliminaries | M10 | The complete supplied process and entanglement task |
| Narrative/innovation | M11–M14 | Relative orders give the universal abelian obstruction and necessary minima |
| Narrative/innovation | M15–M20 | An inherited state criterion and the marker construction complete the converse |
| Narrative/innovation | M21–M24 | Complete-erasure and minimal qubit realizations expose distinct physical consequences |
| Narrative/innovation | M25–M28 | Noise tolerance, channel-specific restrictions and resource accounting |
| Narrative/innovation | M29–M30 | Attribution, evidence and the full scientific conclusion |

## Background/preliminaries: local objects to the complete model

### M01. States and the chosen bipartition

- **Phase:** Background/preliminaries.
- **Central question:** What mathematical object describes the joint controller and target, and which division defines their entanglement?
- **Understanding target:** Distinguish a pure state vector from its density operator, a mixture from a superposition, and a joint state on $`C\otimes T`$ from either reduced state. Recognize positivity and unit trace as state conditions.
- **Dependencies and story role:** No earlier milestone. Establishes the objects and the retained $`C:T`$ cut used throughout both phases.
- **Conceptual connection:** The same physical systems can support different questions depending on which systems are retained and compared.
- **Source pointers:** Watrous §§2.1.2–2.1.3 for states and composite systems, with the local state primer in the [bridge](./WATROUS_BRIDGE.md); [model inputs and bipartition](../science/model.md#3-inputs-and-the-entanglement-task).

### M02. What makes a map a quantum channel?

- **Phase:** Background/preliminaries.
- **Central question:** Which properties make a state transformation valid even when the target is correlated with another system?
- **Understanding target:** Explain complete positivity and trace preservation at the level needed here. Distinguish a channel acting on density operators from one chosen Kraus operator, which can describe a single unnormalized contribution.
- **Dependencies and story role:** M01. Introduces the local physical transformations before considering their arrangement or coherent control.
- **Conceptual connection:** Complete positivity protects compatibility with untouched systems; trace preservation accounts for all outcomes of an unconditional process.
- **Source pointers:** Watrous §2.2.2 through the [bridge](./WATROUS_BRIDGE.md); [channel definition](../science/model.md#1-independent-slots-and-chronological-order) and [switch normalization](../science/model.md#2-normalization-and-kraus-independence).

### M03. Kraus operators and inaccessible environments

- **Phase:** Background/preliminaries.
- **Central question:** Why can different lists of Kraus operators describe the same noise without giving the controller extra access?
- **Understanding target:** Interpret the Kraus sum as a representation of an unconditional channel. Separate a mathematical change of Kraus basis from measuring or controlling the environment, and explain why a Kraus label is not an available classical input.
- **Dependencies and story role:** M02. Prevents representation choices from being mistaken for supplied physical resources in the later proof.
- **Conceptual connection:** Environmental information can be useful if accessible, but its appearance in an equation does not make it operationally available.
- **Source pointers:** Watrous §2.2.2, Corollary 2.23 and Eqs. (2.99)-(2.100), via the [bridge](./WATROUS_BRIDGE.md); [Kraus independence](../science/model.md#2-normalization-and-kraus-independence).

### M04. Sequential composition and independent slots

- **Phase:** Background/preliminaries.
- **Central question:** How are noise labels assigned when several independent channels act in a specified chronological order?
- **Understanding target:** Read a product of Kraus operators with the rightmost operation acting first. Distinguish a label attached to a physical slot from its position in time, and distinguish fresh independent channel instances from equal marginals with shared noise.
- **Dependencies and story role:** M02-M03. Builds the ordinary sequential process that every coherent order branch must reproduce.
- **Conceptual connection:** Identical slot maps give the same definite-order channel, while independence determines which environmental tuples are summed.
- **Source pointers:** Watrous §2.2.2 for channel representation language, with the chronological derivation in the [bridge](./WATROUS_BRIDGE.md); [independent slots and Eq. (1)](../science/model.md#1-independent-slots-and-chronological-order).

### M05. Coherence over order labels

- **Phase:** Background/preliminaries.
- **Central question:** What changes when the controller is a superposition of orders rather than a classical choice among them?
- **Understanding target:** Relate pure controller amplitudes to diagonal and off-diagonal blocks of the joint output. Explain why the diagonal target blocks can all agree while the retained joint state still contains additional information.
- **Dependencies and story role:** M01 and M04. Adds coherent control to the sequential model without yet deciding whether the resulting correlations are entanglement.
- **Conceptual connection:** Discarding the controller removes the off-diagonal blocks that distinguish coherent routing from an ordinary mixture.
- **Source pointers:** The local order-control discussion in the [bridge](./WATROUS_BRIDGE.md), using Watrous §6.1.1 state language; [controller input and output blocks](../science/model.md#3-inputs-and-the-entanglement-task).

### M06. Separable states and product Kraus maps

- **Phase:** Background/preliminaries.
- **Central question:** Which correlations remain separable, and why can product Kraus operators not create entanglement from them?
- **Understanding target:** Distinguish a product state, a separable mixture of product states, and an entangled state. Explain why each product Kraus term $`D_\ell\otimes L_\ell`$ sends a positive product operator to a positive product operator, and why summing those terms preserves separability for every separable input.
- **Dependencies and story role:** M01-M03. Provides the form of impossibility certificate that the main proof will construct.
- **Conceptual connection:** A structural property of a channel can settle an entanglement question for all separable inputs at once.
- **Source pointers:** Watrous §§6.1.1-6.1.2 through the [bridge](./WATROUS_BRIDGE.md); [product Kraus operators](../science/order_criterion.md#product-kraus-operators).

### M07. What partial transposition can certify

- **Phase:** Background/preliminaries.
- **Central question:** What does a negative partial transpose prove, and when does a positive one settle separability?
- **Understanding target:** Explain why NPT certifies entanglement in every finite dimension. Keep that implication separate from PPT sufficiency in $`2\times2`$ and $`2\times3`$, and distinguish an exact witness from a small numerical eigenvalue.
- **Dependencies and story role:** M01 and M06. Supplies the diagnostic used by both the general converse and the finite qubit example.
- **Conceptual connection:** The dimension of the bipartition changes what a positivity test can conclude.
- **Source pointers:** Watrous §6.2.3, Definition 6.39, via the [bridge](./WATROUS_BRIDGE.md); [model's PPT scope](../science/model.md#3-inputs-and-the-entanglement-task) and [primary criteria](../references/RELATED_WORK.md#partial-transpose).

### M08. Permutations, groups and cosets

- **Phase:** Background/preliminaries.
- **Central question:** How can a family of chronological orders be described without treating each order as an unrelated list?
- **Understanding target:** Read permutation composition and inverses, distinguish a selected set from the group it generates, and understand cyclic and abelian groups. Interpret containment in a coset without assuming the selected orders form a subgroup themselves.
- **Dependencies and story role:** M04. Introduces the language needed to compare order families structurally.
- **Conceptual connection:** Group structure organizes relations among routes even when the ordinary channel action is identical on every route.
- **Source pointers:** Watrous §7.1.1, Eqs. (7.3)-(7.5), for permutation operators; the [bridge](./WATROUS_BRIDGE.md) supplies group and coset preparation; [relative permutations](../science/order_criterion.md#relative-permutations).

### M09. Commuting representations and a common basis

- **Phase:** Background/preliminaries.
- **Central question:** Why is one basis that diagonalizes an entire family stronger than diagonalizing its members separately?
- **Understanding target:** Distinguish a permutation from a unitary matrix representing it. Explain the role of pairwise commutation and simultaneous diagonalization, and why faithfulness is needed to recover a group relation from represented matrices but not to diagonalize a commuting family.
- **Dependencies and story role:** M03 and M08. Connects the operator and group viewpoints that meet in the no-go proof.
- **Conceptual connection:** A common basis can turn a family of coupled descriptions into aligned scalar phases.
- **Source pointers:** Watrous Theorem 1.5 and §7.1.1 through the [bridge](./WATROUS_BRIDGE.md), which extends the two-operator diagonalization statement to a finite commuting family; [common Kraus-index space](../science/order_criterion.md#a-common-kraus-index-space).

### M10. Assemble the supplied process and question

- **Phase:** Background/preliminaries.
- **Central question:** What exactly is supplied, retained and forbidden in the entanglement question this project answers?
- **Understanding target:** Combine the preceding objects into the generalized-switch model: independent identical slots, a pure occupied order support for existence claims, inaccessible environments, no interleaved target operations, and retained $`C:T`$ output. Distinguish that task from access to arbitrary controlled target gates.
- **Dependencies and story role:** M01-M09. Integrates the background into one physical and mathematical contract before beginning the contribution.
- **Conceptual connection:** Correct resource accounting makes a structural theorem meaningful rather than a statement about an unrestricted processor.
- **Source pointers:** The [Watrous-to-project bridge](./WATROUS_BRIDGE.md), combining the verified channel, separability and permutation sections; [full model](../science/model.md) and [supplied resources](../science/model.md#4-supplied-resources-and-scope).

## Narrative/innovation: local mechanism to the complete contribution

### M11. Relative orders and reference independence

- **Phase:** Narrative/innovation.
- **Central question:** Which comparison between selected orders matters, and why does choosing a different reference leave the answer unchanged?
- **Understanding target:** Form $`G_\Pi=\langle\pi_0^{-1}\pi\rangle`$, explain reference independence of the generated group, and relate left-relative to right-relative permutations by common conjugation. Understand why individual orders need not commute for their relative family to do so.
- **Dependencies and story role:** M08-M10. Identifies the precise structural object on which the contribution depends.
- **Conceptual connection:** The geometry of differences between routes is more informative than the names assigned to the routes.
- **Source pointers:** Watrous §7.1.1 through the [bridge](./WATROUS_BRIDGE.md); [relative group and reference proof](../science/order_criterion.md#relative-permutations).

### M12. Orders act on formal Kraus histories

- **Phase:** Narrative/innovation.
- **Central question:** Where does a permutation act in the proof if no target permutation gate is available?
- **Understanding target:** Trace the passage from a chronological slot order to a permutation of the common operator-valued Kraus vector. Keep the formal index space distinct from both the physical target and an accessible environment, and follow the representation's composition convention.
- **Dependencies and story role:** M03-M04, M09 and M11. Supplies the mathematical mechanism connecting order structure to a channel statement.
- **Conceptual connection:** Reindexing the same independent noise tuples exposes a symmetry without adding a physical operation.
- **Source pointers:** Watrous §2.2.2 and §7.1.1 through the [bridge](./WATROUS_BRIDGE.md); [common Kraus-index representation](../science/order_criterion.md#a-common-kraus-index-space).

### M13. The abelian product-Kraus obstruction

- **Phase:** Narrative/innovation.
- **Central question:** How does commutation of relative orders force every identical channel to preserve separability?
- **Understanding target:** Explain the chain from commuting index unitaries to one common diagonalizing basis, then to $`D_\ell\otimes L_\ell`$ Kraus factors. Identify why the same basis change must be applied to the entire joint Kraus family.
- **Dependencies and story role:** M06, M09 and M12. Completes the universal impossibility half, moving from a local index-space relation to all separable inputs.
- **Conceptual connection:** Mathematical Kraus freedom becomes a physical no-entanglement certificate through product structure.
- **Source pointers:** Watrous Corollary 2.23 and §§6.1.1-6.1.2 via the [bridge](./WATROUS_BRIDGE.md); [product-Kraus proof](../science/order_criterion.md#product-kraus-operators) and [inherited two-history mechanism](../references/RELATED_WORK.md#two-history-obstructions).

### M14. Quantifiers and necessary minima

- **Phase:** Narrative/innovation.
- **Central question:** What does the no-go establish for every channel, and what still requires an existence construction?
- **Understanding target:** Distinguish universal impossibility from failure of one selected noise model. Derive the obstruction for any two alternatives and all cyclic supports, and separate the number of calls from the number of occupied control labels. Recognize that necessary minima do not yet prove attainability.
- **Dependencies and story role:** M11-M13. Synthesizes the no-go and defines the missing converse before introducing it.
- **Conceptual connection:** The meaning of “for every channel” determines which architectural conclusion a proof supports.
- **Source pointers:** The [bridge](./WATROUS_BRIDGE.md), using Watrous §§6.1.1-6.1.2; [Theorem 1](../science/order_criterion.md#theorem-1-the-order-support-criterion) and [two-alternative consequence](../science/order_criterion.md#any-two-alternatives-are-nonentangling).

### M15. The inherited conditional-unitary state

- **Phase:** Narrative/innovation.
- **Central question:** What established state family can convert noncommuting relative unitaries into an entanglement statement?
- **Understanding target:** Interpret the block state with entries $`\alpha_i\overline{\alpha_j}U_iU_j^\dagger/D`$ as controlled unitaries acting on a maximally mixed target. Explain the harmless reference-unitary choice and the requirement that occupied control amplitudes be nonzero.
- **Dependencies and story role:** M05-M07 and M14. Introduces the inherited mathematical ingredient needed by the converse without assuming it is physically realizable by identical slots.
- **Conceptual connection:** A known state criterion can guide a construction while leaving its constrained physical realization unresolved.
- **Source pointers:** Watrous §6.1.1 via the [bridge](./WATROUS_BRIDGE.md); [Lemma 2](../science/channel_realizations.md#the-inherited-conditional-unitary-criterion) and [Roszak attribution](../references/RELATED_WORK.md#roszak2018).

### M16. Why commutation is the exact state criterion

- **Phase:** Narrative/innovation.
- **Central question:** Why do the conditional-unitary states become NPT precisely when the relative unitaries fail to commute?
- **Understanding target:** Follow the conceptual roles of invertible local filtering, the reference identity block and its Schur complement. Explain why positive blocks with zero diagonal force vanishing off-diagonal blocks, and why common eigenvectors give a separable decomposition in the commuting case.
- **Dependencies and story role:** M07, M09 and M15. Completes the inherited lemma and identifies exactly what a channel realization must reproduce.
- **Conceptual connection:** Positivity converts a matrix commutator into a sharp entanglement boundary.
- **Source pointers:** Watrous Definition 6.39 through the [bridge](./WATROUS_BRIDGE.md); [local Schur-complement proof](../science/channel_realizations.md#proof) and [inherited result](../references/RELATED_WORK.md#roszak2018).

### M17. Build one legitimate marker channel

- **Phase:** Narrative/innovation.
- **Central question:** How can a single channel store the time of a noise event inside the counted target system?
- **Understanding target:** Identify the empty, marker and failure sectors, the roles of $`K_0`$, $`K_1`$ and $`F_j`$, and the reason their completeness relation defines a CPTP map. Keep the internal marker states distinct from an external protected memory.
- **Dependencies and story role:** M02-M04, M10 and M16. Begins the constructive converse with a locally specified physical channel rather than arbitrary controlled unitaries.
- **Conceptual connection:** A coherent marker inside the target converts chronology into a readable representation while respecting the supplied resources.
- **Source pointers:** Watrous §2.2.2 through the [bridge](./WATROUS_BRIDGE.md); [marker channel](../science/channel_realizations.md#the-linear-dimension-channel) and [CPTP check](../science/channel_realizations.md#complete-positivity-and-trace-preservation).

### M18. Count the histories that reach the marker

- **Phase:** Narrative/innovation.
- **Central question:** Why do exactly-one-insertion environmental tuples produce the useful marker block?
- **Understanding target:** Explain which trajectories remain empty, which vanish, and which enter the absorbing failure sector. Relate the slot carrying the unique $`K_1`$ to its chronological position and the number of later shifts, including the inverse-permutation convention.
- **Dependencies and story role:** M04, M12 and M17. Turns the channel's local transition rules into an exact expression for its order-dependent output.
- **Conceptual connection:** Independent inaccessible outcomes are summed, but their different chronological positions can still shape coherent cross-order blocks.
- **Source pointers:** Watrous §2.2.2 and §7.1.1 via the [bridge](./WATROUS_BRIDGE.md); [surviving tuples and marker formula](../science/channel_realizations.md#which-environmental-tuples-reach-the-marker-space).

### M19. Faithfulness connects the marker to the group

- **Phase:** Narrative/innovation.
- **Central question:** Why can the marker output detect the actual commutation relations of the selected relative permutations?
- **Understanding target:** Recognize the normalized marker block as the state from M15. Explain how its relative unitaries are conjugated natural permutation matrices and why faithfulness prevents a nontrivial group commutator from disappearing in this representation.
- **Dependencies and story role:** M09, M11, M15-M16 and M18. Joins the inherited state criterion to the new constrained channel construction.
- **Conceptual connection:** A representation must preserve the relevant distinction, not merely assign matrices to order labels.
- **Source pointers:** Watrous §7.1.1 through the [bridge](./WATROUS_BRIDGE.md); [faithful marker representation](../science/channel_realizations.md#faithfulness-supplies-the-converse) and [Lemma 2](../science/channel_realizations.md#the-inherited-conditional-unitary-criterion).

### M20. Complete the unconditional converse

- **Phase:** Narrative/innovation.
- **Central question:** Why does an entangled marker sector prove unconditional entanglement, and what does its nonvanishing probability mean?
- **Understanding target:** Explain why local filtering cannot turn PPT into NPT and why the empty, marker and failure sectors do not cancel the negative block. State the $`n+2`$ target dimension, support-independent channel and filter probability, without converting that probability into a uniform entanglement amount.
- **Dependencies and story role:** M07, M14 and M17-M19. Completes the iff theorem and its physical realization.
- **Conceptual connection:** A local diagnostic can reveal an unconditional resource while its success probability remains a separate quantity.
- **Source pointers:** Watrous Definition 6.39 and §6.1.2 via the [bridge](./WATROUS_BRIDGE.md); [unconditional converse](../science/channel_realizations.md#faithfulness-supplies-the-converse) and [resource statement](../science/channel_realizations.md#resources-and-the-role-of-filtering).

### M21. Erase every definite-order input

- **Phase:** Narrative/innovation.
- **Central question:** Can the same order criterion be realized when the full definite-order channel destroys all target information?
- **Understanding target:** Explain the shift/reset channel on $`n`$ registers, why its $`n`$-fold composition is completely depolarizing, and how the fresh appended symbols realize a faithful word permutation. Keep this exponential-dimension construction separate from the linear-dimension marker channel.
- **Dependencies and story role:** M04, M16 and M19-M20. Adds a complementary physical consequence of the theorem without changing its quantifiers.
- **Conceptual connection:** Erasure by the composed target channel does not determine the entanglement of the retained coherent-order output.
- **Source pointers:** Watrous §2.2.2 and §7.1.1 via the [bridge](./WATROUS_BRIDGE.md); [complete-erasure construction](../science/channel_realizations.md#complete-erasure-in-every-definite-order).

### M22. The minimal entanglement-breaking channel

- **Phase:** Narrative/innovation.
- **Central question:** How can slots that individually break entanglement still attain the smallest entangling order architecture?
- **Understanding target:** Interpret measure-$`Z`$/prepare-$`X`$ as an entanglement-breaking channel, establish the meaning of $`\mathcal N^2=\Delta`$, and identify the three selected orders and their two noncommuting relative transpositions. Distinguish an EB channel's action on one target from the supplied joint coherent-order process.
- **Dependencies and story role:** M02, M06, M14 and M20. Moves from general existence to a two-level target that can attain the necessary minima.
- **Conceptual connection:** A restriction on each channel instance need not survive the addition of coherent order as a higher-order resource.
- **Source pointers:** Watrous §2.2.2 and Exercise 6.1 on measure-and-prepare channels through the [bridge](./WATROUS_BRIDGE.md); [qubit channel](../science/qubit_example.md#1-the-channel) and [input orders](../science/qubit_example.md#2-input-and-coherent-orders).

### M23. An exact joint-state witness

- **Phase:** Narrative/innovation.
- **Central question:** What certifies that the minimal example produces entanglement rather than merely nonclassical-looking correlations?
- **Understanding target:** Connect the sum over eight independent Kraus tuples to the explicit $`3\times2`$ output. Explain the significance of its negative partial-transpose quadratic form, distinguish that certificate from reduced-controller decoherence, and combine it with the no-go to justify the attained minima.
- **Dependencies and story role:** M04, M07, M14 and M22. Closes the minimal example with a finite exact certificate rather than an inference from the architecture alone.
- **Conceptual connection:** A channel-independent permission theorem and a channel-specific witness answer different parts of the existence question.
- **Source pointers:** Watrous Definition 6.39 via the [bridge](./WATROUS_BRIDGE.md); [exact output](../science/qubit_example.md#3-exact-output-from-the-kraus-sum), [witness](../science/qubit_example.md#4-an-exact-entanglement-certificate) and [minimality](../science/qubit_example.md#6-what-is-minimal).

### M24. Reveal a two-qubit entangled subspace

- **Phase:** Narrative/innovation.
- **Central question:** What does the local controller projection reveal, and what does its success not establish?
- **Understanding target:** Identify the two-dimensional controller subspace, the success probability $`1/2`$, and the negative principal minor of the normalized projected state. Explain why the filter reveals existing entanglement and why the resulting mixed two-qubit state is not a pure Bell pair after one copy.
- **Dependencies and story role:** M06-M07, M20 and M23. Connects the unconditional certificate to a simpler accessible bipartition while preserving the operational limits.
- **Conceptual connection:** Local postselection changes the state and its normalization, but cannot create entanglement from a separable input.
- **Source pointers:** Watrous §§6.1.1-6.1.2 and Definition 6.39 through the [bridge](./WATROUS_BRIDGE.md); [local projection](../science/qubit_example.md#5-a-local-projection-exposes-two-qubit-entanglement).

### M25. Specify the noise before its tolerance

- **Phase:** Narrative/innovation.
- **Central question:** Why does full controller dephasing become output white noise for this particular example?
- **Understanding target:** Relate the retained-coherence parameter to the initial controller mixture and the identical diagonal target blocks. Explain the exact family $`\rho_\eta=\eta\rho+(1-\eta)I_6/6`$ and distinguish a fixed-witness sufficient threshold from the state's actual separability transition.
- **Dependencies and story role:** M05, M07 and M23. Introduces robustness through a specified physical noise model rather than an unspecified error percentage.
- **Conceptual connection:** The same numerical noise parameter can have different meanings unless the map and affected subsystem are fixed.
- **Source pointers:** The [bridge](./WATROUS_BRIDGE.md), using Watrous Definition 6.39; [dephasing family](../science/robustness.md#controller-dephasing-and-output-white-noise) and [fixed witness](../science/robustness.md#a-simple-fixed-witness).

### M26. Exact threshold and conservative perturbation bounds

- **Phase:** Narrative/innovation.
- **Central question:** Which parts of the robustness result are exact, and which are sufficient bounds for a broader perturbation class?
- **Understanding target:** Explain how the lowest partial-transpose eigenvalue determines the dephasing transition and why $`3\times2`$ PPT sufficiency makes it an exact separability boundary. Distinguish that threshold from the conservative output trace-norm ball and from unproved tolerances on individual gates or slots.
- **Dependencies and story role:** M07 and M25. Integrates spectrum, dimensional scope and error model into one appropriately qualified robustness statement.
- **Conceptual connection:** Exactness is always relative to a specified state family and criterion.
- **Source pointers:** Watrous Definition 6.39 and §1.1.3 on norms through the [bridge](./WATROUS_BRIDGE.md); [exact transition](../science/robustness.md#exact-separability-transition), [perturbation bound](../science/robustness.md#a-bound-for-arbitrary-output-perturbations) and [PPT research sources](../references/RELATED_WORK.md#partial-transpose).

### M27. Channels that still cannot entangle

- **Phase:** Narrative/innovation.
- **Central question:** Why can a nonabelian support fail for a particular channel, or for a restricted class of channels?
- **Understanding target:** Explain the shared-eigenbasis obstruction for depolarizers, the phase-only reordering of Pauli products, and the effect of a common final EB slot. Use these examples to reject a universal EB-only converse and the assertion that every channel works on every nonabelian support.
- **Dependencies and story role:** M06, M14, M20 and M22. Tests the theorem's quantifiers against physically different obstructions.
- **Conceptual connection:** Architecture supplies a possibility boundary; channel structure can impose further restrictions within it.
- **Source pointers:** Watrous §§6.1.1-6.1.2 through the [bridge](./WATROUS_BRIDGE.md); [channel-specific boundaries](../science/interpretation.md#channel-families-that-remain-nonentangling).

### M28. Separate tasks and count resources

- **Phase:** Narrative/innovation.
- **Central question:** Which operational conclusions follow from retained controller-target entanglement, and which require a different task definition?
- **Understanding target:** Separate $`C:T`$ entanglement creation from target-reference recovery, asymptotic communication capacity and causal certification. Count calls, occupied order labels and full target dimension separately, and recognize ideal coherent order as a supplied resource rather than a free implementation.
- **Dependencies and story role:** M10, M20-M21 and M23-M27. Integrates the constructions into a common operational comparison without transferring advantages between different endpoints.
- **Conceptual connection:** The chosen bipartition and allowed operations determine what a physical result means.
- **Source pointers:** The [bridge](./WATROUS_BRIDGE.md), using Watrous channel and separable-map language; [task distinctions](../science/interpretation.md#communication-and-entanglement-are-different-tasks) and [resource comparison](../science/interpretation.md#resources-of-the-constructions).

### M29. Connect claims to proofs and antecedents

- **Phase:** Narrative/innovation.
- **Central question:** Which evidence supports each central claim, and which parts of the argument come from earlier work?
- **Understanding target:** Map the general iff to analytical proofs, the finite qubit and threshold values to exact certificates, and the marker examples to numerical consistency checks. Attribute the conditional-unitary lemma, two-history obstruction and earlier switch settings without treating those antecedents as the full constrained realization theorem.
- **Dependencies and story role:** M13-M28. Integrates the logical and bibliographic support before the final scientific synthesis.
- **Conceptual connection:** Reproducibility, proof, attribution and novelty each answer a distinct question about a research result.
- **Source pointers:** The [Watrous bridge](./WATROUS_BRIDGE.md) separates anchor foundations from research dependencies; [claim map](../science/README.md#claim-and-proof-map), [related work](../references/RELATED_WORK.md) and [verification scope](../verification/README.md#what-these-checks-establish).

### M30. Synthesize the full order-entanglement result

- **Phase:** Narrative/innovation.
- **Central question:** What does the completed project establish about identical noise, coherent order and entanglement?
- **Understanding target:** Explain the complete chain: commuting relative orders force a product-Kraus obstruction; noncommuting relatives admit an explicit physical converse; a minimal EB-qubit example attains the capability even with erased definite-order output. State the pure-support quantifier, resource costs, robustness scope and remaining boundaries together.
- **Dependencies and story role:** M11-M29. Concludes the narrative by joining mechanism, theorem, realization, evidence and physical interpretation into one account.
- **Conceptual connection:** Equality of ordinary target channels leaves room for distinct coherent-order capabilities, governed here by relative permutation structure.
- **Source pointers:** The [single-anchor bridge](./WATROUS_BRIDGE.md), [scientific entrypoint](../science/README.md), [Theorem 1](../science/order_criterion.md#theorem-1-the-order-support-criterion) and [scientific conclusion](../science/interpretation.md#scientific-conclusion).
