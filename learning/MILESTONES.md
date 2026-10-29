# Thirty milestones for quantum order entanglement

This map organizes the project into exactly **30 milestones**, M01–M30, common to every reader. The story moves from the structure of coherent order supports to actual identical-channel realizations, then to a robust comparison between retained controller–target entanglement and heralded reference–target recovery.

The sole educational anchor, shared with the sister project, is **John Watrous, *The Theory of Quantum Information* (2018)**. The [Watrous bridge](WATROUS_BRIDGE.md) supplies the source version, focused section pointers, notation translations and project-specific missing steps. Primary research sources provide attribution and proof dependencies rather than additional educational anchors.

## Allocation and route

The **10 + 20 allocation** follows the project’s scientific structure. The background joins local states, channels, separability and permutation representations into the supplied-process question. The narrative combines the obstruction and converse, their explicit realizations, and the controller-noise connection into the whole contribution. Each phase ends in synthesis. Specialist calculations remain in the canonical science pages.

| Phase | Milestones | Connection established |
|---|---|---|
| Background/preliminaries | [M01](#m01)–[M04](#m04) | States, channels, inaccessible environments and independent slots |
| Background/preliminaries | [M05](#m05)–[M10](#m10) | Coherence, separability, permutations and the complete task |
| Narrative/innovation | [M11](#m11)–[M16](#m16) | Universal obstruction, inherited state criterion and constrained converse |
| Narrative/innovation | [M17](#m17)–[M20](#m20) | Minimal qubit realization, witnesses, robustness and channel-specific limits |
| Narrative/innovation | [M21](#m21)–[M26](#m26) | Physical noise, shared tilted family, exact certificates and uniform comparison |
| Narrative/innovation | [M27](#m27)–[M30](#m30) | Sister optimization, normalization, evidence and whole-project synthesis |

Watrous’s relevant foundations include §§2.1.2–2.1.3, §2.2.2, §§6.1.1–6.1.2, §6.2.3 and §7.1.1. The noisy comparison also uses measurement, norm and Schur-map tools in §§2.3, 3.3 and 4.1.3. The [bridge](WATROUS_BRIDGE.md) explains their roles; it is a focused route, not an assignment to read the whole book.

## Background/preliminaries: local objects to the complete model

<a id="m01"></a>

### M01. States and the chosen bipartition

- **Phase:** Background/preliminaries.
- **Central question:** What mathematical object describes the joint controller and target, and which division defines their entanglement?
- **Understanding target:** Distinguish a pure state vector from its density operator, a mixture from a superposition, and a joint state on $`C\otimes T`$ from either reduced state. Recognize positivity and unit trace as state conditions.
- **Dependencies and story role:** No earlier milestone. Establishes the objects and the retained $`C:T`$ cut used throughout both phases.
- **Conceptual connection:** The same physical systems can support different questions depending on which systems are retained and compared.
- **Source pointers:** Watrous §§2.1.2–2.1.3 for states and composite systems, with the local state primer in the [bridge](./WATROUS_BRIDGE.md); [model inputs and bipartition](../science/model.md#3-inputs-and-the-entanglement-task).

<a id="m02"></a>

### M02. What makes a map a quantum channel?

- **Phase:** Background/preliminaries.
- **Central question:** Which properties make a state transformation valid even when the target is correlated with another system?
- **Understanding target:** Explain complete positivity and trace preservation at the level needed here. Distinguish a channel acting on density operators from one chosen Kraus operator, which can describe a single unnormalized contribution.
- **Dependencies and story role:** M01. Introduces the local physical transformations before considering their arrangement or coherent control.
- **Conceptual connection:** Complete positivity protects compatibility with untouched systems; trace preservation accounts for all outcomes of an unconditional process.
- **Source pointers:** Watrous §2.2.2 through the [bridge](./WATROUS_BRIDGE.md); [channel definition](../science/model.md#1-independent-slots-and-chronological-order) and [switch normalization](../science/model.md#2-normalization-and-kraus-independence).

<a id="m03"></a>

### M03. Kraus operators and inaccessible environments

- **Phase:** Background/preliminaries.
- **Central question:** Why can different lists of Kraus operators describe the same noise without giving the controller extra access?
- **Understanding target:** Interpret the Kraus sum as a representation of an unconditional channel. Separate a mathematical change of Kraus basis from measuring or controlling the environment, and explain why a Kraus label is not an available classical input.
- **Dependencies and story role:** M02. Prevents representation choices from being mistaken for supplied physical resources in the later proof.
- **Conceptual connection:** Environmental information can be useful if accessible, but its appearance in an equation does not make it operationally available.
- **Source pointers:** Watrous §2.2.2, Corollary 2.23 and Eqs. (2.99)-(2.100), via the [bridge](./WATROUS_BRIDGE.md); [Kraus independence](../science/model.md#2-normalization-and-kraus-independence).

<a id="m04"></a>

### M04. Sequential composition and independent slots

- **Phase:** Background/preliminaries.
- **Central question:** How are noise labels assigned when several independent channels act in a specified chronological order?
- **Understanding target:** Read a product of Kraus operators with the rightmost operation acting first. Distinguish a label attached to a physical slot from its position in time, and distinguish fresh independent channel instances from equal marginals with shared noise.
- **Dependencies and story role:** M02-M03. Builds the ordinary sequential process that every coherent order branch must reproduce.
- **Conceptual connection:** Identical slot maps give the same definite-order channel, while independence determines which environmental tuples are summed.
- **Source pointers:** Watrous §2.2.2 for channel representation language, with the chronological derivation in the [bridge](./WATROUS_BRIDGE.md); [independent slots and Eq. (1)](../science/model.md#1-independent-slots-and-chronological-order).

<a id="m05"></a>

### M05. Coherence over order labels

- **Phase:** Background/preliminaries.
- **Central question:** What changes when the controller is a superposition of orders rather than a classical choice among them?
- **Understanding target:** Relate pure controller amplitudes to diagonal and off-diagonal blocks of the joint output. Explain why the diagonal target blocks can all agree while the retained joint state still contains additional information.
- **Dependencies and story role:** M01 and M04. Adds coherent control to the sequential model without yet deciding whether the resulting correlations are entanglement.
- **Conceptual connection:** Discarding the controller removes the off-diagonal blocks that distinguish coherent routing from an ordinary mixture.
- **Source pointers:** The local order-control discussion in the [bridge](./WATROUS_BRIDGE.md), using Watrous §6.1.1 state language; [controller input and output blocks](../science/model.md#3-inputs-and-the-entanglement-task).

<a id="m06"></a>

### M06. Separable states and product Kraus maps

- **Phase:** Background/preliminaries.
- **Central question:** Which correlations remain separable, and why can product Kraus operators not create entanglement from them?
- **Understanding target:** Distinguish a product state, a separable mixture of product states, and an entangled state. Explain why each product Kraus term $`D_\ell\otimes L_\ell`$ sends a positive product operator to a positive product operator, and why summing those terms preserves separability for every separable input.
- **Dependencies and story role:** M01-M03. Provides the form of impossibility certificate that the main proof will construct.
- **Conceptual connection:** A structural property of a channel can settle an entanglement question for all separable inputs at once.
- **Source pointers:** Watrous §§6.1.1-6.1.2 through the [bridge](./WATROUS_BRIDGE.md); [product Kraus operators](../science/order_criterion.md#product-kraus-operators).

<a id="m07"></a>

### M07. What partial transposition can certify

- **Phase:** Background/preliminaries.
- **Central question:** What does a negative partial transpose prove, and when does a positive one settle separability?
- **Understanding target:** Explain why NPT certifies entanglement in every finite dimension. Keep that implication separate from PPT sufficiency in $`2\times2`$ and $`2\times3`$, and distinguish an exact witness from a small numerical eigenvalue.
- **Dependencies and story role:** M01 and M06. Supplies the diagnostic used by both the general converse and the finite qubit example.
- **Conceptual connection:** The dimension of the bipartition changes what a positivity test can conclude.
- **Source pointers:** Watrous §6.2.3, Definition 6.39, via the [bridge](./WATROUS_BRIDGE.md); [model's PPT scope](../science/model.md#3-inputs-and-the-entanglement-task) and [primary criteria](../references/RELATED_WORK.md#partial-transpose).

<a id="m08"></a>

### M08. Permutations, groups and cosets

- **Phase:** Background/preliminaries.
- **Central question:** How can a family of chronological orders be described without treating each order as an unrelated list?
- **Understanding target:** Read permutation composition and inverses, distinguish a selected set from the group it generates, and understand cyclic and abelian groups. Interpret containment in a coset without assuming the selected orders form a subgroup themselves.
- **Dependencies and story role:** M04. Introduces the language needed to compare order families structurally.
- **Conceptual connection:** Group structure organizes relations among routes even when the ordinary channel action is identical on every route.
- **Source pointers:** Watrous §7.1.1, Eqs. (7.3)-(7.5), for permutation operators; the [bridge](./WATROUS_BRIDGE.md) supplies group and coset preparation; [relative permutations](../science/order_criterion.md#relative-permutations).

<a id="m09"></a>

### M09. Commuting representations and a common basis

- **Phase:** Background/preliminaries.
- **Central question:** Why is one basis that diagonalizes an entire family stronger than diagonalizing its members separately?
- **Understanding target:** Distinguish a permutation from a unitary matrix representing it. Explain the role of pairwise commutation and simultaneous diagonalization, and why faithfulness is needed to recover a group relation from represented matrices but not to diagonalize a commuting family.
- **Dependencies and story role:** M03 and M08. Connects the operator and group viewpoints that meet in the no-go proof.
- **Conceptual connection:** A common basis can turn a family of coupled descriptions into aligned scalar phases.
- **Source pointers:** Watrous Theorem 1.5 and §7.1.1 through the [bridge](./WATROUS_BRIDGE.md), which extends the two-operator diagonalization statement to a finite commuting family; [common Kraus-index space](../science/order_criterion.md#a-common-kraus-index-space).

<a id="m10"></a>

### M10. Assemble the supplied process and question

- **Phase:** Background/preliminaries.
- **Central question:** What exactly is supplied, retained and forbidden in the entanglement question this project answers?
- **Understanding target:** Combine the preceding objects into the generalized-switch model: independent identical slots, a pure occupied order support for existence claims, inaccessible environments, no interleaved target operations, and retained $`C:T`$ output. Distinguish that task from access to arbitrary controlled target gates.
- **Dependencies and story role:** M01-M09. Integrates the background into one physical and mathematical contract before beginning the contribution.
- **Conceptual connection:** Correct resource accounting makes a structural theorem meaningful rather than a statement about an unrestricted processor.
- **Source pointers:** The [Watrous-to-project bridge](./WATROUS_BRIDGE.md), combining the verified channel, separability and permutation sections; [full model](../science/model.md) and [supplied resources](../science/model.md#4-supplied-resources-and-scope).

## Narrative/innovation: local mechanism to the complete contribution

<a id="m11"></a>

### M11. Relative orders and formal histories

**Phase:** Narrative/innovation.

**Central question:** How do relative permutations act on the same independent noise histories?

**Understanding target:** Choose a reference order, form the generated relative group and explain reference independence. Represent each route by a permutation of the formal Kraus-index tuple, keeping that mathematical space distinct from accessible target memory.

**Dependencies and story role:** M03–M05 and M08–M10. Connects the supplied routing process to the representation used in the proof.

**Conceptual connection:** Ordinary equality of channel compositions leaves a nontrivial relationship among off-diagonal history amplitudes.

**Source pointers:** Watrous §7.1.1 and §2.2.2 through the [bridge](WATROUS_BRIDGE.md); [relative permutations](../science/order_criterion.md#relative-permutations); [common Kraus-index space](../science/order_criterion.md#a-common-kraus-index-space).

<a id="m12"></a>

### M12. A common basis yields a product-Kraus obstruction

**Phase:** Narrative/innovation.

**Central question:** Why does an abelian relative group forbid retained entanglement for every identical channel?

**Understanding target:** Use simultaneous diagonalization of the relative history permutations to obtain one common target Kraus operator per transformed index and diagonal controller phase factors. Explain why this product-Kraus form preserves every separable input without requiring a faithful representation.

**Dependencies and story role:** M06, M09 and M11. Produces the universal impossibility direction from the local commutation condition.

**Conceptual connection:** A common environmental coordinate change proves a physical channel property without granting access to that environment.

**Source pointers:** Watrous Theorem 1.5, Corollary 2.23 and §§6.1.1–6.1.2; [abelian sufficiency proof](../science/order_criterion.md#proof-of-abelian-sufficiency).

<a id="m13"></a>

### M13. Quantifiers, two alternatives and cyclic families

**Phase:** Narrative/innovation.

**Central question:** Which order families are ruled out, and what does failure of that obstruction promise?

**Understanding target:** Explain why every two-alternative support is cyclic and nonentangling, why arbitrarily many cyclic alternatives still fail, and why nonabelian support means some channel can work rather than every channel. Distinguish the pure-support theorem from the stated sufficient condition for mixed controllers.

**Dependencies and story role:** M08, M11 and M12. Turns the obstruction into necessary minima while fixing the quantifiers of the converse.

**Conceptual connection:** Counting alternatives alone misses their relative algebra; a mixed controller is not classified only by its nonzero matrix pattern.

**Source pointers:** Watrous permutation and convexity foundations via the [bridge](WATROUS_BRIDGE.md); [theorem and consequences](../science/order_criterion.md#theorem-1-the-order-support-criterion); [mixed-controller condition](../science/order_criterion.md#mixed-controllers-a-sufficient-condition).

<a id="m14"></a>

### M14. The inherited conditional-unitary state criterion

**Phase:** Narrative/innovation.

**Central question:** When does a coherent family of unitaries on a maximally mixed target create NPT?

**Understanding target:** Explain the state built from blocks U_i U_j-adjoint and why its separability is equivalent to commutation of the relative unitaries. Trace the Schur-complement argument and the commuting product-state decomposition. Identify this criterion as inherited from Roszak rather than the project’s channel realization.

**Dependencies and story role:** M06–M09 and M13. Supplies the entanglement criterion that a legitimate repeated channel must physically realize.

**Conceptual connection:** An abstract controlled-unitary state is a useful proof target; inserting arbitrary controlled gates would leave the supplied-slot model.

**Source pointers:** Watrous §§1.1.3, 6.1.1 and 6.2.3; [conditional-unitary criterion and proof](../science/channel_realizations.md#the-inherited-conditional-unitary-criterion); [source attribution](../references/RELATED_WORK.md#roszak2018).

<a id="m15"></a>

### M15. One marker channel realizes every nonabelian support

**Phase:** Narrative/innovation.

**Central question:** How can a single ordinary channel turn time position into the needed target permutation?

**Understanding target:** Build the empty, marker and absorbing-failure sectors, check Kraus completeness, and isolate histories with one insertion. Relate the insertion’s physical slot to its final marker, use the faithful natural representation, and explain why a local NPT marker filter proves the unconditional output was already NPT.

**Dependencies and story role:** M03–M04 and M11–M14. Completes the physically constrained converse with target dimension n+2.

**Conceptual connection:** The channel encodes the order relation through its own dynamics; it supplies no extra intermediate controlled target operation.

**Source pointers:** Watrous §2.2.2 and §6.2.3; [linear-dimension channel and full converse](../science/channel_realizations.md#the-linear-dimension-channel).

<a id="m16"></a>

### M16. Filter probability and complete-erasure realization

**Phase:** Narrative/innovation.

**Central question:** Which resource statements belong to the marker construction, and which require a different channel?

**Understanding target:** Explain the marker filter probability n p (1-p)^(n-1), its constant lower bound at p=1/n, and why this does not bound entanglement uniformly over tiny supported amplitudes. Separately explain the shift/reset realization with dimension s^n and complete definite-order erasure on every input.

**Dependencies and story role:** M14–M15. Integrates the converse’s costs and distinguishes two constructions with different physical strengths.

**Conceptual connection:** The linear target dimension, filter probability, complete erasure and entanglement-breaking property must not be combined into an unsupported single construction.

**Source pointers:** Watrous §1.2.2, §2.2.2 and §7.1.1; [marker resources](../science/channel_realizations.md#resources-and-the-role-of-filtering); [complete-erasure realization](../science/channel_realizations.md#complete-erasure-in-every-definite-order).

<a id="m17"></a>

### M17. The minimal three-call entanglement-breaking example

**Phase:** Narrative/innovation.

**Central question:** How can entanglement-breaking slots attain the smallest entangling architecture?

**Understanding target:** Specify the measure-Z/prepare-X qubit channel, show that two ordinary uses depolarize, and choose chronological orders 012, 021 and 102 with a uniform pure controller. Combine the two-alternative obstruction with the explicit example to justify three calls and three alternatives as separate minima.

**Dependencies and story role:** M10, M13 and M15. Makes the general boundary concrete with the smallest nontrivial target.

**Conceptual connection:** An entanglement-breaking slot need not factor as a final local entanglement-breaking operation in a coherent superposition of different complete orders.

**Source pointers:** Watrous §2.2.2 and Chapter 6’s measure-and-prepare foundations; [minimal qubit channel](../science/qubit_example.md#1-the-channel); [minimality](../science/qubit_example.md#6-what-is-minimal).

<a id="m18"></a>

### M18. An exact retained-state entanglement witness

**Phase:** Narrative/innovation.

**Central question:** What proves that the minimal example’s unconditional joint state is entangled?

**Understanding target:** Follow the finite Kraus contraction to the exact 6-by-6 output and evaluate its rational negative-partial-transpose witness. Explain the optional local projection exposing a two-qubit entangled subspace without confusing the filtered diagnostic with the unconditional task.

**Dependencies and story role:** M07 and M17. Joins the construction to an inspectable exact entanglement certificate.

**Conceptual connection:** A local filter reveals existing entanglement; it does not supply the entanglement claimed for the unconditional state.

**Source pointers:** Watrous §6.2.3; [exact output](../science/qubit_example.md#3-exact-output-from-the-kraus-sum); [witness](../science/qubit_example.md#4-an-exact-entanglement-certificate); [local projection](../science/qubit_example.md#5-a-local-projection-exposes-two-qubit-entanglement).

<a id="m19"></a>

### M19. Noise tolerance, witness thresholds and separability

**Phase:** Narrative/innovation.

**Central question:** Which noise conclusions follow from one witness, the full spectrum and a norm perturbation bound?

**Understanding target:** Distinguish the fixed-witness threshold eta>9/10, the exact global-dephasing transition at the root of 2 eta^3-7 eta^2+4, and the conservative trace-norm perturbation radius. Explain why PPT sufficiency applies on the occupied 3-by-2 space and why these are distinct noise statements.

**Dependencies and story role:** M07 and M18. Converts the exact example into a robust but carefully specified physical result.

**Conceptual connection:** A sufficient witness, an exact state-family boundary and an arbitrary-output norm ball answer different questions.

**Source pointers:** Watrous §§1.1.3, 3.3 and 6.2.3; [robustness derivation](../science/robustness.md).

<a id="m20"></a>

### M20. Nonabelian support is not a channel-specific guarantee

**Phase:** Narrative/innovation.

**Central question:** Why do some channels remain nonentangling even when their order support is nonabelian?

**Understanding target:** Explain the shared target eigenbasis for depolarizer blocks, Pauli reorderings by phases, and the common-final-entanglement-breaking-slot example. Keep these channel-specific obstructions distinct from the existential converse over all identical channels.

**Dependencies and story role:** M12–M13 and M17–M19. Tests the theorem’s quantifiers against important boundary examples.

**Conceptual connection:** A necessary architecture can support a capability without making every allowed channel attain it.

**Source pointers:** Watrous §§6.1.1–6.1.2; [nonentangling channel families](../science/interpretation.md#channel-families-that-remain-nonentangling).

<a id="m21"></a>

### M21. A physical controller encoding changes local noise

**Phase:** Narrative/innovation.

**Central question:** What information must be specified before comparing noisy coherent-order protocols?

**Understanding target:** Define independent phase flips on actual controller bits with gamma=1-2z and the Schur factor gamma to the Hamming distance. For three occupied orders in a two-bit register, distinguish the three allocations by which pair has distance two. Separate gamma=4/5 from a global dephasing parameter of the same numerical value.

**Dependencies and story role:** M04–M05, M10 and M19. Establishes the physical noise model used by the new shared experiment.

**Conceptual connection:** A code assignment changes which order pairs decohere fastest; order names and scalar coherence summaries do not determine that geometry.

**Source pointers:** Watrous §4.1.3; [physical control noise](../science/noisy_separation.md#physical-control-noise); [sister physical codebook](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/noisy_routing_model.md#physical-codebook).

<a id="m22"></a>

### M22. A tilted, full-rank entanglement-breaking family

**Phase:** Narrative/innovation.

**Central question:** How can the retained and recovery experiments use the same raw noisy slots away from a special orthogonal point?

**Understanding target:** Specify N_epsilon,theta as a depolarizing admixture of the measure-Z/prepare-tilted-axis channel. Explain entanglement breaking, full Choi rank for positive epsilon, theta=pi/2+delta, and the loss of the special squared-channel erasure identity under tilt. Keep raw slots distinct from per-slot unitary wrappers.

**Dependencies and story role:** M02–M04, M17 and M21. Supplies the matched family whose robustness can be proved rather than inferred from one point.

**Conceptual connection:** A final correction is allowed in recovery; wrapping each supplied slot would change the channel resource and the comparison.

**Source pointers:** Watrous §2.2.2 and Chapter 6; [shared family](../science/noisy_separation.md#shared-family); [shared raw-slot access](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/noisy_routing_model.md#shared-access).

<a id="m23"></a>

### M23. Exact rational certificates for the retained outputs

**Phase:** Narrative/innovation.

**Central question:** How can finitely many computations establish a strict PPT margin without relying on floating-point eigenvalues?

**Understanding target:** Construct the rational angle grid delta_k=2 arctan(k/400), the integer Kraus columns and weighted history sums. Explain the 249 exact shifted LDL certificates for three encodings at 83 grid points, and why the strict matrix bound concerns occupied 6-dimensional support rather than the unused 8-dimensional physical space.

**Dependencies and story role:** M07, M18 and M21–M22. Establishes the finite exact obligation behind the uniform retained-state result.

**Conceptual connection:** Exact positivity on occupied support plus the dimensional PPT theorem yields separability at grid points; interpolation is still needed between them.

**Source pointers:** Watrous §§1.1.3 and 6.2.3; [exact grid certificate](../science/noisy_separation.md#exact-grid-certificate); [verification guide](../verification/README.md).

<a id="m24"></a>

### M24. The fixed recovery branch and its entanglement witness

**Phase:** Narrative/innovation.

**Central question:** What does the four-call sister experiment accept, and what certifies entanglement with a reference?

**Understanding target:** Specify the eight physical codes, signed P2 effect and identity final correction. Define accepted Bell output tau, acceptance p, Bell reward f and witness w=f-p/2. Explain the 83 rational positive-witness certificates, the real branch’s input-independent success, and the fresh-pair cost 4/p.

**Dependencies and story role:** M06–M07, M21–M23. Defines the comparison endpoint with its success condition and charged resources.

**Conceptual connection:** The accepted reference–target cut R:T differs from the retained controller–target cut C:T, even with identical raw slot channels.

**Source pointers:** Watrous §§2.3.2, 3.2 and 6.2.3; [specified protocols](../science/noisy_separation.md#specified-protocols); [exact certificate](../science/noisy_separation.md#exact-grid-certificate).

<a id="m25"></a>

### M25. From a rational grid to a uniform angular interval

**Phase:** Narrative/innovation.

**Central question:** What prevents an entanglement or PPT certificate from failing between checked grid points?

**Understanding target:** Use a common Stinespring dilation and a telescoping bound for r-slot controlled routing to obtain trace-norm variation at most r times the angular difference. Apply the occupied-support partial-transpose bound, witness norm and success-effect bound to derive the strict margins for every abs(delta) at most .2 radians.

**Dependencies and story role:** M03, M07, M23 and M24. Completes the uniform theorem by joining finite exact certificates to an analytical continuity argument.

**Conceptual connection:** A finite grid alone proves a finite statement; a quantitative interpolation bound pays for the untested angles.

**Source pointers:** Watrous §§2.2.2 and 3.3; [continuity proof](../science/noisy_separation.md#continuity-proof); [uniform separation](../science/noisy_separation.md#uniform-separation).

<a id="m26"></a>

### M26. What the robust separation does and does not compare

**Phase:** Narrative/innovation.

**Central question:** What operational conclusion survives once both bipartitions and every resource are stated?

**Understanding target:** Explain the uniform result: the specified three-call unconditional C:T outputs are separable for every two-bit allocation, while the four-call accepted R:T output is NPT with .035<p<.095 and F>101/190. Keep three versus four slots, two versus three bits, and unconditional versus heralded outputs explicit.

**Dependencies and story role:** M16, M20 and M24–M25. Integrates the new comparison into a precise operational statement.

**Conceptual connection:** This separates two specified experiments under shared noise; it is not an equal-resource optimized separation or a universal no-go for retained protocols.

**Source pointers:** Watrous §§2.3.2, 6.1.1 and 6.2.3; [uniform theorem](../science/noisy_separation.md#uniform-separation); [operational meaning](../science/noisy_separation.md#operational-meaning).

<a id="m27"></a>

### M27. The sister recovery frontier and its evidence boundary

**Phase:** Narrative/innovation.

**Central question:** How does optimizing recovery relate to, but differ from, classifying retained entanglement?

**Understanding target:** Describe the sister project’s complete controller feasible set, physical three-X readout frontier, and certified tilted optimality interval. Distinguish a fidelity upper bound from a separability theorem: optimized Bell fidelity at most one half does not prove every complex-controller Choi output separable.

**Dependencies and story role:** M07, M21–M22 and M26. Places the entanglement track beside the independently proved recovery optimization.

**Conceptual connection:** An optimized scalar objective can settle a recovery tradeoff without classifying every possible entanglement output.

**Source pointers:** Watrous §§1.2.3 and 3.2; [controller feasibility](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/controller_optimization.md#controller-feasibility); [frontier theorem](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/recovery_frontier.md#frontier-theorem); [tilted optimality](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/tilted_readout.md#tilted-optimality).

<a id="m28"></a>

### M28. Real branches, complex controllers and exactness

**Phase:** Narrative/innovation.

**Central question:** Which structural facts justify normalized-channel and exact-recovery conclusions?

**Understanding target:** Explain why real Y-covariant accepted branches have scalar success effects, while arbitrary complex controllers need not. Place the sister’s strict Schur-noise exact-recovery obstruction alongside its real attaining noisy frontier, retaining the full-rank, raw-slot and unobserved-noise assumptions.

**Dependencies and story role:** M03, M21–M22, M24 and M27. Checks that normalization and theorem transfers use their actual hypotheses.

**Conceptual connection:** A Bell-input optimization can provide a tight bound when an input-independent attaining representative is proved; that does not make every feasible branch input independent.

**Source pointers:** Watrous §§2.2.2, 2.3.2 and 4.1.3; [real-controller reduction](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/controller_optimization.md#real-controller-reduction); [strict Schur obstruction](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/noisy_recovery_obstruction.md#strict-schur-obstruction).

<a id="m29"></a>

### M29. Connect each claim to its proof and antecedents

**Phase:** Narrative/innovation.

**Central question:** Which scientific conclusions are inherited, analytically proved, exactly certified or numerically checked?

**Understanding target:** Credit the conditional-unitary criterion, earlier two-history results and established PPT theorem. Separate the project’s constrained realizations and order-support classification from the new exact grid-plus-continuity comparison. Explain what original verification and the independent joint rebuild establish, including the limits of sampled examples and bounded literature review.

**Dependencies and story role:** M12–M28. Integrates the source and evidence structure before the final synthesis.

**Conceptual connection:** Attribution concerns what conclusion is inherited; verification concerns which assertion was actually checked. Neither is supplied by shared terminology or numerical agreement.

**Source pointers:** Watrous foundations through the [bridge](WATROUS_BRIDGE.md); [related work](../references/RELATED_WORK.md); [verification guide](../verification/README.md); [scientific overview](../science/README.md).

<a id="m30"></a>

### M30. The complete entanglement and recovery connection

**Phase:** Narrative/innovation. **Phase synthesis.**

**Central question:** What complete story connects relative order structure, physical realization and robustly different endpoints?

**Understanding target:** Explain the abelian universal obstruction, the nonabelian existential realization, the minimal entanglement-breaking example and its robustness, and the tilted shared-family separation. State why retained C:T entanglement, conditional R:T recovery, communication capacity and causal-structure certification remain distinct tasks.

**Dependencies and story role:** M10–M29. Phase synthesis: joins algebra, realizability, minimality, controller-noise geometry, evidence and the limits of transfer.

**Conceptual connection:** A common foundation supports two distinct capabilities; the scientific connection is established through specified models and proofs rather than assumed from the word entanglement.

**Source pointers:** Watrous channel, separability and permutation sections through the [bridge](WATROUS_BRIDGE.md); [order-support theorem](../science/order_criterion.md#theorem-1-the-order-support-criterion); [uniform separation](../science/noisy_separation.md#uniform-separation); [scientific route](../science/README.md).
