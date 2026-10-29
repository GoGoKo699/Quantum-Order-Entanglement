# Related work and proof ingredients

This project studies entanglement across the **retained controller and target** of a generalized switch, starting from a separable input. The slots are independent instances of one ordinary channel, every order uses each slot once, and no noise environment is accessible. The [model](../science/model.md) states the complete resource assumptions.

The result proved here is the [order-support criterion](../science/order_criterion.md): universal inability to generate this entanglement is equivalent to commutation of the relative permutations. Its converse is supplied by [explicit repeated-channel constructions](../science/channel_realizations.md), including one channel of target dimension $`n+2`$ that works for every nonabelian pure order support at a fixed number of calls. The [minimal qubit example](../science/qubit_example.md) and its [exact dephasing threshold](../science/robustness.md) provide a concrete realization and finite certificates.

The conditional-unitary entanglement criterion, the two-history obstruction, the generalized-switch resource, and prior uses of three identical channels are established ingredients. The comparisons below separate them from the constrained architecture statement. They are a targeted account of the closest inspected work, not an exhaustive priority claim.

The [noisy separation](../science/noisy_separation.md) adds a different statement: for a specified full-rank measure–prepare family and physical local phase noise, a retained three-order output is separable throughout a certified tilt interval while one accepted four-call reference–target output is entangled. This compares specified protocols and different bipartitions; it is not a universal retained-control obstruction or an equal-resource optimum.

## Comparison map

| Source | Established result used or compared | Relation to the present result |
|---|---|---|
| [Roszak (2018)](#roszak2018) | Conditional-unitary commutation criterion for pure-dephasing entanglement, including NPT when it fails | Supplies the abstract state criterion; the identical-channel realization must still be constructed |
| [Chiribella et al. (2021)](#chiribella2021) | Explicit separability of an identical two-slot self-switch | Supplies the two-call obstruction; more than two permutation orders are outside that paper's stated scope |
| [Das and Bandyopadhyay (2022)](#das-bandyopadhyay2022) | A switch of two switches can increase the probability of perfect heralded qubit communication | Establishes the broader communication mechanism; the fixed three-call frontier and mixed-budget optimum require their own converse |
| [Aslanbaş et al. (2026)](#aslanbas2026) | Product Kraus representation when two coherently controlled composed channels coincide | Supplies the two-history Kraus-freedom mechanism |
| [Procopio et al. (2019)](#procopio2019) | Generalized permutation switching and depolarizer interference blocks | Supplies the resource formalism and a channel-specific class that remains controller–target separable |
| [Sazim et al.; Wilson–Chiribella (2021)](#permutation-structure-for-depolarizers) | Cyclic cosets and permutation-cycle structure for depolarizer communication | Group organization and cyclic/noncyclic distinctions are already established |
| [Goldberg et al. (2023)](#goldberg2023) | Three identical noisy channels in three coherent order alternatives for metrology | The three-slot setup alone is not new; the retained entanglement question is different |
| [Kechrimparis et al. (2024, 2025)](#nested-switch-recovery) | Nested four-slot architecture and Pauli-channel purification | Supplies the recovery router and ideal branch; the noisy raw-slot optimization is developed in the sister project |
| [Molitor et al. (2024)](#control-noise) | Open-control two-slot switching, with noise-dependent accepted states and probabilities | Establishes prior control-noise analysis; its protected outcomes prevent a blanket noisy-control no-go claim |
| [Regula and Takagi (2021)](#positive-components) | An unwanted positive component that survives acceptance obstructs perfect distillation | Supplies the obstruction principle; the sister project's routing proof establishes that survival for strict Schur noise |

<a id="roszak2018"></a>

## Conditional-unitary entanglement

**Katarzyna Roszak**, *Criteria for system-environment entanglement generation for systems of any size in pure-dephasing evolutions*, **Physical Review A 98**, 052344 (2018). [DOI](https://doi.org/10.1103/PhysRevA.98.052344); [arXiv:1808.08112v1](https://arxiv.org/abs/1808.08112v1).

Sections IV.C and V, Eqs. (30)–(32), and Appendix B give the relevant separability conditions for a pure system coherently controlling unitaries on a mixed environment. For a maximally mixed environment, the criterion reduces to commutation of the relative conditional unitaries. Failure yields a negative partial transpose. The generic distinction between two and three control levels is also present there.

[Lemma 2](../science/channel_realizations.md#the-inherited-conditional-unitary-criterion) reproduces that special case with a Schur-complement proof. Neither the conditional-unitary criterion nor its NPT conclusion is claimed as new. The construction then realizes a faithful permutation representation using repeated instances of one channel, whose environments remain inaccessible. This constrained realizability step is what connects the inherited state criterion to the order-support theorem.

<a id="two-history-obstructions"></a>

## Two-history obstructions

<a id="chiribella2021"></a>

**Giulio Chiribella, Manik Banik, Some Sankar Bhattacharya, Tamal Guha, Mir Alimuddin, Arup Roy, Sutapa Saha, Sristy Agrawal and Guruprasad Kar**, *Indefinite causal order enables perfect quantum communication with zero capacity channels*, **New Journal of Physics 23**, 033039 (2021). [DOI](https://doi.org/10.1088/1367-2630/abe7a0); [arXiv:1810.10457v4](https://arxiv.org/abs/1810.10457v4), revised 5 September 2022.

Equation (3) decomposes the identical two-slot self-switch into commutator and anticommutator target branches, each multiplied by a controller state. The following paragraph explicitly states controller–target separability. This holds for general channels and target dimensions, and predates the present work. The closing paragraph of Section III leaves more than two permutation orders outside its scope. The paper's arbitrary-finite-number path theorem concerns spatial alternatives rather than a general permutation switch.

Its communication results also show why controller–target entanglement and preservation of a message's entanglement with a reference are different tasks.

<a id="aslanbas2026"></a>

**Beyza Aslanbaş, Bedirhan Alkan and Göktuğ Karpat**, *Entangling capability of coherently controlled quantum processes*, [arXiv:2609.00168v1](https://arxiv.org/html/2609.00168v1), 31 August 2026. This source is a preprint.

Section III.4, Eqs. (62)–(70), uses unitary freedom of Kraus representations when the two composed channels agree. Diagonalizing the relative Kraus transformation gives product Kraus operators for the coherently controlled process. Applying this reasoning to two orders of identical slots is an inherited implication.

The [abelian sufficiency proof](../science/order_criterion.md#proof-of-abelian-sufficiency) simultaneously diagonalizes a family of relative Kraus-index permutations. The converse requires an explicit channel realizing the noncommuting side; equality of the definite-order target channels does not supply that construction.

The two-slot commuting-channel result also does not determine the three-order noisy retained state used in [the separation theorem](../science/noisy_separation.md). Its separability is established directly for the stated input, uniform preparation and each of the three two-bit encodings. The accepted four-call reference–target state is a separate experiment with a different bipartition and conditioning.

<a id="generalized-switches"></a>

## Generalized switches and depolarizing channels

<a id="procopio2019"></a>

**Lorenzo M. Procopio, Francisco Delgado, Marco Enríquez, Nadia Belabas and Juan Ariel Levenson**, *Communication Enhancement through Quantum Coherent Control of N Channels in an Indefinite Causal-Order Scenario*, **Entropy 21**, 1012 (2019). [DOI](https://doi.org/10.3390/e21101012); [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7514224/); [arXiv:1902.01807v3](https://arxiv.org/abs/1902.01807v3).

The paper treats coherent permutations of independently supplied channels, with each slot visited once. Equation (7) and the following text state that the target blocks for depolarizing channels lie in the span of the input state and identity for arbitrary channel count.

Their controller–target separability is an immediate **inference from that formula**: all target blocks can be diagonalized in the eigenbasis of the input, and positivity makes each remaining controller block positive. The [explicit deduction](../science/interpretation.md#depolarizing-channels) explains why nonabelian order support does not make every channel entangling.

<a id="permutation-structure-for-depolarizers"></a>

## Permutation structure for depolarizers

**Sk Sazim, Michal Sedlak, Kratveer Singh and Arun Kumar Pati**, *Classical communication with indefinite causal order for N completely depolarizing channels*, **Physical Review A 103**, 062610 (2021). [DOI](https://doi.org/10.1103/PhysRevA.103.062610); [published full text](https://www.quantum.physics.sk/rcqi/research/publications/2021/rcqi2021sedlak_PhysRevA.103.062610.pdf); [arXiv:2004.14339v2](https://arxiv.org/abs/2004.14339v2).

The introduction and Section IV organize order choices by cosets of the cyclic permutation subgroup. Table I and Eq. (14) give the relevant depolarizer blocks. Cyclic versus noncyclic organization and the use of group cosets therefore precede this project. Their task is classical communication through a specified noise family, rather than universal separability for every identical channel.

**Matt Wilson and Giulio Chiribella**, *A Diagrammatic Approach to Information Transmission in Generalised Switches*, **Electronic Proceedings in Theoretical Computer Science 340**, 333–348 (2021). [DOI](https://doi.org/10.4204/EPTCS.340.17); [arXiv:2003.08224v3](https://arxiv.org/abs/2003.08224v3).

Theorem 2, Corollaries 3–5 and Eq. (31) determine depolarizer interference terms through permutation cycles and diagram connectivity. The diagrammatic factorization condition should not be identified with separability across the retained $`C:T`$ bipartition. This work supplies an important permutation-based precursor, but not the arbitrary-channel criterion proved here.

<a id="goldberg2023"></a>

## Three identical channels in metrology

**Aaron Z. Goldberg, Luis L. Sánchez-Soto and Khabat Heshami**, *Evading noise in multiparameter quantum metrology with indefinite causal order*, **Physical Review Research 5**, 033198 (2023). [DOI](https://doi.org/10.1103/PhysRevResearch.5.033198); [arXiv:2309.07220v1](https://arxiv.org/abs/2309.07220v1).

Section V, Eq. (5.3), already studies three identical noisy-unitary channels with three noncommuting order alternatives and evaluates reduced-controller interference statistics. The physical setup of three identical slots and three coherent alternatives is therefore established prior work.

Those reduced-controller statistics do not by themselves supply a joint entanglement witness or a universal order-support boundary. The [interpretation](../science/interpretation.md#communication-and-entanglement-are-different-tasks) gives a product-state example with reduced control coherence. This distinction concerns the inference from local statistics to joint entanglement; it does not invalidate the paper's metrological use of those statistics.

<a id="partial-transpose"></a>

## Partial-transpose criteria

**Asher Peres**, *Separability Criterion for Density Matrices*, **Physical Review Letters 77**, 1413–1415 (1996). [DOI](https://doi.org/10.1103/PhysRevLett.77.1413); [arXiv:quant-ph/9604005v2](https://arxiv.org/abs/quant-ph/9604005v2).

Separability implies a positive partial transpose. This necessary condition certifies entanglement whenever the explicit output has a negative partial transpose.

**Michał Horodecki, Paweł Horodecki and Ryszard Horodecki**, *Separability of mixed states: necessary and sufficient conditions*, **Physics Letters A 223**, 1–8 (1996). [DOI](https://doi.org/10.1016/S0375-9601(96)00706-2); [arXiv:quant-ph/9605038v2](https://arxiv.org/abs/quant-ph/9605038v2).

PPT is also sufficient for separability in $`2\times2`$ and $`2\times3`$. The [exact robustness threshold](../science/robustness.md#exact-separability-transition) uses this inherited result for the $`3\times2`$ output. The larger-dimensional construction relies on NPT to establish entanglement and does not infer separability from numerical PPT checks.

<a id="nested-switch-recovery"></a>

## Nested-switch recovery and the raw-slot boundary

**Spiros Kechrimparis, James Moran, Athena Karsa, Changhyoup Lee and Hyukjoon Kwon**, *Enhancing quantum state discrimination with indefinite causal order*, **New Journal of Physics 26**, 123030 (2024). [DOI](https://doi.org/10.1088/1367-2630/ada05e); [arXiv:2406.19373v1](https://arxiv.org/html/2406.19373v1).

Section IV, Eqs. (28)–(30), of the identified preprint defines the inherited four-slot nested-switch architecture. The branch-diagonal form following it uses a Kraus commutator/anticommutator exclusivity condition satisfied by Pauli channels. This condition is not automatic for the raw measure–prepare family used in the noisy comparison. Appendix D studies a particular entangled control construction rather than arbitrary-controller optimality.

**Spiros Kechrimparis, James Moran and Hyukjoon Kwon**, *Probabilistic channel distillation via indefinite causal order*, **Physical Review Research 7**, 043257 (2025). [DOI](https://doi.org/10.1103/mvrg-yj3l); [published full text](https://harvest.aps.org/v2/journals/articles/10.1103/mvrg-yj3l/fulltext); [arXiv:2501.13696v1](https://arxiv.org/abs/2501.13696v1).

Section IV of the journal version, published 5 December 2025, gives the inherited four-call Pauli purification branch. Appendix A compares selected permutation constructions; it does not establish the arbitrary-controller fidelity frontier. Section VII's extension by twirling changes the supplied channel resource. The present comparison retains the raw slots, excludes per-slot wrappers, and allows only a final herald-dependent target unitary.

The sister repository [Quantum Order Distillation](https://github.com/GoGoKo699/Quantum-Order-Distillation) owns the complete [controller reduction](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/controller_optimization.md), [orthogonal frontier](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/recovery_frontier.md), and [tilted readout proof](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/tilted_readout.md). Those conclusions optimize accepted corrected Bell fidelity on the specified physical eight-order architecture. Here the [separation theorem](../science/noisy_separation.md) uses one fixed real recovery branch and directly certifies the retained state; the optimum does not classify every possible retained output. Fidelity at or below one half is not used as a converse entanglement test for arbitrary complex-controller outputs.

<a id="das-bandyopadhyay2022"></a>

## Fixed-channel recovery and randomized call budgets

**Debarshi Das and Somshubhro Bandyopadhyay**, *Quantum communication using a quantum switch of quantum switches*, **Proceedings of the Royal Society A 478**(2266), 20220231 (2022). [DOI](https://doi.org/10.1098/rspa.2022.0231); [arXiv:2111.08266v3](https://arxiv.org/abs/2111.08266v3), revised 6 October 2022 and identified by its authors as the published version; [institutional record](https://discovery.ucl.ac.uk/id/eprint/10156914/).

This work shows that coherently ordering two quantum switches can increase the success probability of perfect qubit communication over their individual use; it also identifies cases without an advantage. Together with [Chiribella et al.](#chiribella2021), it establishes the earlier communication mechanism. Neither the presence of extra coherent orders nor heralded recovery alone is the additional conclusion claimed here.

The sister project's [native three-call frontier](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/native_three_call_frontier.md) fixes the rank-deficient channel $`K_0=|+\rangle\langle0|`$, $`K_1=|-\rangle\langle1|`$ and global logical order dephasing, with all six three-slot orders available. It gives a complete success–half-diamond-error frontier and matching controller converse. Its [randomized cost theorem](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/randomized_call_cost.md) optimizes expected noisy calls across fresh one-, two- and three-call trials, including unequal logical noise. Total accepted success is input independent even though arbitrary fine outcomes need not be.

These are fixed-channel target-only recovery results. They do not classify retained controller–target entanglement or replace this repository's three-order versus four-call [noisy separation](../science/noisy_separation.md). The rank-deficient three-call benchmark, full-rank four-call theory and physical-local-noise Bell-fidelity frontier have different hypotheses. Conditional scalar-dephasing duration comparisons are not hardware or capacity certifications, and the primary-source comparison does not establish publication priority.

<a id="control-noise"></a>

## Control noise and protected conditional outcomes

**Otavio A. D. Molitor, André H. A. Malavazi, Roberto Dobal Baldijão, Alexandre C. Orthey Jr., Ismael L. Paiva and Pedro R. Dieguez**, *Quantum switch instabilities with an open control*, **Communications Physics 7**, 373 (2024). [DOI](https://doi.org/10.1038/s42005-024-01843-y); [published full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11576514/); [arXiv:2405.09631v1](https://arxiv.org/abs/2405.09631v1).

The two-slot collisional model shows that the bath can affect conditional states and their probabilities differently. In the zero-temperature limit one selected state is shielded while its postselection becomes less likely. These results establish control-noise sensitivity without implying that every noisy controller destroys exact recovery.

The present [local-noise theorem](../science/noisy_separation.md) instead fixes an unobserved phase-flip channel on each physical controller bit and its placement relative to routing. The retained experiment uses two bits and three calls; the accepted experiment uses three bits and four calls. Matching per-bit noise does not make these experiments an equal-resource comparison. The retained PPT bound applies to the occupied six-dimensional support, whose 3 × 2 structure permits the inherited PPT sufficiency theorem to be used.

<a id="positive-components"></a>

## Positive-component distillation obstructions

**Bartosz Regula and Ryuji Takagi**, *Fundamental limitations on distillation of quantum channel resources*, **Nature Communications 12**, 4411 (2021). [DOI](https://doi.org/10.1038/s41467-021-24699-0); [published article](https://www.nature.com/articles/s41467-021-24699-0); [arXiv:2010.11942v3](https://arxiv.org/abs/2010.11942v3).

The probabilistic result around main-text Eq. (34), with Supplementary Note 5, Theorem 21, makes an unwanted component's accepted weight decisive. Postselection can evade the obstruction when it removes that component. The sister project's [strict Schur-noise proof](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/noisy_recovery_obstruction.md) establishes an unavoidable diagonal accepted contribution for every nonzero feasible controller effect under its assumptions. This is a model-specific use of the inherited principle, rather than a claim that full Choi rank alone forbids heralded recovery.

The supported addition in this repository is the stated retained-C:T/accepted-R:T protocol separation with exact certificates and an interval proof. The comparison identifies the inherited architecture, state criteria and obstruction principles; it does not infer priority from search silence.

## Educational anchor

**John Watrous**, *The Theory of Quantum Information*, Cambridge University Press (2018). [DOI](https://doi.org/10.1017/9781316848142); [author's book page and manuscript chapters](https://jhwatrous.github.io/books-and-courses.html).

This is the single educational anchor. Its treatment of channels, Kraus representations, separable maps and permutation operators supplies the foundations used in the [learning bridge](../learning/WATROUS_BRIDGE.md). The generalized-switch model, the inherited conditional-unitary lemma and the project-specific realization arguments are identified separately. The textbook is not cited as a source for the new order-support theorem or as a substitute for the primary research dependencies above.

Structured records, inspected versions and equation pointers are collected in [references.bib](references.bib).
