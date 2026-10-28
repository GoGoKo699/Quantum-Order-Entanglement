# Related work and proof ingredients

This project studies entanglement across the **retained controller and target** of a generalized switch, starting from a separable input. The slots are independent instances of one ordinary channel, every order uses each slot once, and no noise environment is accessible. The [model](../science/model.md) states the complete resource assumptions.

The result proved here is the [order-support criterion](../science/order_criterion.md): universal inability to generate this entanglement is equivalent to commutation of the relative permutations. Its converse is supplied by [explicit repeated-channel constructions](../science/channel_realizations.md), including one channel of target dimension $`n+2`$ that works for every nonabelian pure order support at a fixed number of calls. The [minimal qubit example](../science/qubit_example.md) and its [exact dephasing threshold](../science/robustness.md) provide a concrete realization and finite certificates.

The conditional-unitary entanglement criterion, the two-history obstruction, the generalized-switch resource, and prior uses of three identical channels are established ingredients. The comparisons below separate them from the constrained architecture statement. They are a targeted account of the closest inspected work, not an exhaustive priority claim.

## Comparison map

| Source | Established result used or compared | Relation to the present result |
|---|---|---|
| [Roszak (2018)](#roszak2018) | Conditional-unitary commutation criterion for pure-dephasing entanglement, including NPT when it fails | Supplies the abstract state criterion; the identical-channel realization must still be constructed |
| [Chiribella et al. (2021)](#chiribella2021) | Explicit separability of an identical two-slot self-switch | Supplies the two-call obstruction; more than two permutation orders are outside that paper's stated scope |
| [Aslanbaş et al. (2026)](#aslanbas2026) | Product Kraus representation when two coherently controlled composed channels coincide | Supplies the two-history Kraus-freedom mechanism |
| [Procopio et al. (2019)](#procopio2019) | Generalized permutation switching and depolarizer interference blocks | Supplies the resource formalism and a channel-specific class that remains controller–target separable |
| [Sazim et al.; Wilson–Chiribella (2021)](#permutation-structure-for-depolarizers) | Cyclic cosets and permutation-cycle structure for depolarizer communication | Group organization and cyclic/noncyclic distinctions are already established |
| [Goldberg et al. (2023)](#goldberg2023) | Three identical noisy channels in three coherent order alternatives for metrology | The three-slot setup alone is not new; the retained entanglement question is different |

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

Structured records, inspected versions and equation pointers are collected in [references.bib](references.bib).
