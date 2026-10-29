# From quantum channels to entanglement from order

A target passes through three noisy devices. Each device implements the same channel, so changing their ordinary order leaves the final target channel unchanged. A quantum controller can instead retain a coherent superposition of routes. The process then produces a joint controller–target state, and the question becomes whether these initially independent systems have become entangled.

Equality of the ordinary target channels settles only part of that question. It fixes what remains after the controller is discarded. Correlations in the retained joint output also depend on how the same independent noise events appear in different chronological orders. This project classifies which order families can use those correlations to create entanglement, and constructs channels that realize the allowed cases. It also connects that retained-state task to heralded recovery through a shared noisy-channel experiment whose two outputs remain provably different under a finite axis tilt.

The [30-milestone map](MILESTONES.md) organizes this account. The [science pages](../science/README.md) remain the authoritative home for complete statements, proofs and exact matrices.

## 1. One anchor and a focused reading route

The educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018)**, [DOI 10.1017/9781316848142](https://doi.org/10.1017/9781316848142). The [author's page](https://jhwatrous.github.io/books-and-courses.html) dates publication to April 2018 and provides an online manuscript.

Section and equation pointers here refer to the **author-hosted prepublication manuscript**, marked ©2018, with a preface dated January 2018, accessed 28 October 2026. The [complete manuscript's front matter](https://jhwatrous.github.io/TQI.pdf) identifies it as a draft. The [author's errata dated 23 July 2025](https://jhwatrous.github.io/TQI.errata.pdf) corrects the published text; the correction relevant here replaces $`\Phi`$ by $`\Xi`$ in Proposition 6.18, Eq. (6.87). The operator denoting that separable map is therefore $`\Xi`$ throughout. Manuscript links provide access to the source; the book is not redistributed here.

| Foundation | Focused Watrous location | Connection to this project |
|---|---|---|
| States and reductions | [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), §§2.1.2–2.1.3; Definitions 2.4–2.5; Eqs. (2.30)–(2.34) | Joint states on $`C\otimes T`$ and discarding subsystems |
| Channels and Kraus freedom | Chapter 2, Definition 2.13; §2.2.2; Corollaries 2.23 and 2.27 | Valid noise maps and changes of their mathematical representation |
| Separability | [Chapter 6](https://jhwatrous.github.io/TQI.6.pdf), §§6.1.1–6.1.2; Proposition 6.18; Corollary 6.24 | Product Kraus operators preserve separable states |
| Partial transpose | Chapter 6, §6.2.3, Definition 6.39 | Exact entanglement certificates and their dimensional scope |
| Entanglement-breaking channels | Chapter 6, Exercise 6.1 | Measure-and-prepare form of the minimal qubit channel |
| Permutation operators | [Chapter 7](https://jhwatrous.github.io/TQI.7.pdf), §7.1.1, Eqs. (7.3)–(7.5) | Representing rearrangements of histories and target registers |
| Measurements and accepted operations | Chapter 2, §§2.3.1–2.3.2 | A measured controller and a subnormalized accepted reference–target state |
| Schur maps and norms | [Chapter 4](https://jhwatrous.github.io/TQI.4.pdf), §4.1.3; [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), §3.3 | Physical-bit dephasing and uniform interpolation from exact grid certificates |
| Positive-matrix optimization | Chapter 1, §1.2.3 | The sister recovery frontier and its operator bounds |
| Linear algebra and robustness | [Chapter 1](https://jhwatrous.github.io/TQI.1.pdf), §1.1.3; Theorem 1.5; Eqs. (1.164), (1.174), (1.181) | Common eigenbases, Schmidt coefficients and norm bounds |

The source supplies these foundations. The generalized-switch model, the conditional-unitary research lemma and the constrained channel realizations require the additional connections developed below. Primary papers in [Related work](../references/RELATED_WORK.md) provide research attribution and proof dependencies, while Watrous remains the single educational anchor.

## 2. States, channels and hidden noise labels

**Milestones M01–M04.** A system of dimension $`d`$ has $`d`$ independent basis states. A pure state is a normalized complex vector $`|\psi\rangle`$; its density operator is $`|\psi\rangle\langle\psi|`$. A mixture combines density operators with probabilities. These descriptions differ: a superposition retains relative amplitudes, whereas a mixture averages over alternatives without preserving their relative phases.

A density operator $`\rho`$ is positive semidefinite and has trace one. Positivity means every quadratic form $`\langle u|\rho|u\rangle`$ is nonnegative; trace one normalizes probabilities. The controller and target together occupy $`C\otimes T`$. Their joint state specifies both local states and correlations. Taking the partial trace over $`C`$ removes that subsystem and yields the target's reduced state.

A quantum channel is a linear map that preserves trace and is completely positive. Complete positivity requires valid positive outputs even when the input is correlated with an untouched reference. One useful representation is

```math
\mathcal N(X)=\sum_a K_aXK_a^\dagger,
\qquad \sum_aK_a^\dagger K_a=I_T.
```

The operators $`K_a`$ are Kraus operators. Their completeness relation makes the entire map trace preserving. An individual term can have trace below one; it is one contribution to the unconditional process.

An environment explains the label $`a`$. A pure target can undergo an enlarged evolution

```math
|\psi\rangle_T\longmapsto
\sum_a K_a|\psi\rangle_T\otimes|a\rangle_E.
```

Tracing out the environment gives the Kraus sum. The environment basis is not unique. Watrous's Corollary 2.23 relates two equal-length Kraus families by a unitary matrix of coefficients; unequal lengths can first be padded with zero operators. This changes the description of the same channel. It supplies no ability to observe or control the environment.

The project uses $`n`$ independent physical slots, all implementing $`\mathcal N`$. Each has its own inaccessible environment. A tuple $`\boldsymbol a=(a_0,\ldots,a_{n-1})`$ records one Kraus label per slot. Independence licenses the sum over these separate labels. Identical marginal channels sharing environmental memory would specify a different resource.

For a chronological order $`\pi=(\pi(0),\ldots,\pi(n-1))`$, the target operator is

```math
A_{\boldsymbol a,\pi}
=K_{a_{\pi(n-1)}}\cdots K_{a_{\pi(0)}}.
```

The rightmost operator acts first. For example, $`012`$ means slot 0 first, while the product is $`K_{a_2}K_{a_1}K_{a_0}`$. The label $`a_j`$ follows physical slot $`j`$ through every route; it is not reassigned to the same time position in different routes. Every definite order nevertheless implements $`\mathcal N^n`$.

## 3. Coherent orders and the retained output

**Milestones M05 and M10.** Let $`\Pi`$ be the selected set of orders. The controller has an orthonormal state $`|\pi\rangle`$ for each selected order and starts in

```math
|\alpha\rangle=\sum_{\pi\in\Pi}\alpha_\pi|\pi\rangle,
\qquad \sum_\pi|\alpha_\pi|^2=1.
```

The occupied support contains exactly those labels with nonzero amplitude. The existence theorem assumes every amplitude on $`\Pi`$ is nonzero. The target initially has an independent state $`\rho_T`$.

The supplied generalized switch has joint Kraus operators

```math
W_{\boldsymbol a}
=\sum_{\pi\in\Pi}|\pi\rangle\langle\pi|
\otimes A_{\boldsymbol a,\pi}.
```

For a fixed inaccessible noise tuple, this operator preserves coherence between the order alternatives. The joint output's $`(\pi,\tau)`$ block is

```math
\alpha_\pi\overline{\alpha_\tau}
\sum_{\boldsymbol a}
A_{\boldsymbol a,\pi}\rho_TA_{\boldsymbol a,\tau}^\dagger.
```

The diagonal blocks contain the ordinary channel $`\mathcal N^n`$. The off-diagonal blocks compare different chronological products with the same slot labels. Tracing out the controller deletes those off-diagonal blocks, explaining why the reduced target can look identical in all cases while the joint states differ.

The [model](../science/model.md) supplies ideal coherent order control, with every slot visited once per branch. It permits no interleaved target gates or target-carrying bypass. Changing a slot's Kraus basis leaves the joint channel unchanged because its coefficient appears once in every branch, independent of chronology. Retaining this common environmental labeling is essential to the process being defined.

## 4. Separable correlations and partial transpose

**Milestones M06–M07.** A product state has the form $`\rho_C\otimes\rho_T`$. A separable state is a probability mixture of product states:

```math
\sigma_{CT}=\sum_j p_j\sigma_C^{(j)}\otimes\sigma_T^{(j)},
\qquad p_j\ge0,
\qquad \sum_jp_j=1.
```

An entangled state has no such decomposition. Each product Kraus term $`X\mapsto(D_\ell\otimes L_\ell)X(D_\ell\otimes L_\ell)^\dagger`$ sends a positive product operator to another positive product operator. Summing these terms preserves separability, although their sum need not be a product state. This is the content used from Watrous's Proposition 6.18 and Corollary 6.24. It applies to all separable inputs, including classically correlated ones. The individual Kraus terms need not be trace-preserving product channels.

Partial transposition provides a different kind of certificate. In the fixed $`C\otimes T`$ basis, $`\Gamma_T`$ swaps target row and column indices while leaving controller indices in place. On a product operator it gives $`\sigma_C\otimes\sigma_T^T`$, which remains positive. Every separable mixture therefore has a positive partial transpose, or PPT. A vector with

```math
\langle v|\rho^{\Gamma_T}|v\rangle\lt0
```

certifies a negative partial transpose, or NPT, and hence entanglement. This is a mathematical test, not a physically supplied transpose operation.

PPT is sufficient for separability in $`2\times2`$ and $`2\times3`$, including reversed factor order. It is not sufficient in general. The project's [primary criteria](../references/RELATED_WORK.md#partial-transpose) credit Peres for necessity and the Horodeckis for that low-dimensional converse. Watrous's Definition 6.39 supplies the textbook framework. The general construction establishes NPT directly; the exact $`3\times2`$ noise transition can additionally use PPT sufficiency.

## 5. Notation across the source and project

The translations below keep several similar-looking objects separate.

| Watrous | Project | Meaning |
|---|---|---|
| $`u`$, $`uu^*`$, $`A^*`$, $`1_X`$ | $`\lvert u\rangle`$, $`\lvert u\rangle\langle u\rvert`$, $`A^\dagger`$, $`I_X`$ | Vectors, pure density operators, adjoints and identities |
| Tensor factors $`1,\ldots,n`$ | Physical slots $`0,\ldots,n-1`$ | A consistent relabeling, with the same function-composition law |
| Tensor-permutation $`W_\pi`$ | Formal-history $`Q_\pi`$ | The same representation in coefficient notation |
| Tensor-permutation $`W_\pi`$ | Joint Kraus operator $`W_{\boldsymbol a}`$ | Different objects on different spaces; $`W_{\boldsymbol a}`$ need not be unitary |
| Tensor-permutation $`W_g`$ | Shift/reset $`P_g`$, with $`V_\pi=P_{\pi^{-1}}`$ | $`P_g=W_g`$ on the register target; chronology introduces the inverse in $`V_\pi`$ |
| Tensor-permutation $`W_g`$ | Marker $`P_g\lvert r\rangle=\lvert g(r)\rangle`$ | The marker uses the natural representation on $`n`$ labels, not the full tensor representation |
| Depolarizer $`\Omega(X)=\mathrm{Tr}(X)I/d`$ | $`\Delta(X)=\mathrm{Tr}(X)I/d`$ | The same replacement channel |
| Dephaser $`\Delta`$ in Eq. (2.162) | Complete controller dephasing | Deletes off-diagonal entries; distinct from the project's depolarizer $`\Delta`$ |
| First-factor partial transpose | $`\Gamma_C`$ or $`\Gamma_T`$ | The two versions have identical spectra because they differ by a full transpose |
| Trace distance $`\lVert\rho-\sigma\rVert_1`$; spectral norm $`\lVert A\rVert`$ | $`D(\rho,\sigma)=\frac12\lVert\rho-\sigma\rVert_1`$; $`\lVert A\rVert_\infty`$ | An explicit factor of two for distance, and a subscript retained for operator norm |

## 6. Relative permutations identify the obstruction

**Milestones M08–M09 and M11–M13.** A permutation is a reversible rearrangement. Its inverse undoes that rearrangement; composition follows $`(\pi\tau)(j)=\pi(\tau(j))`$. A group contains the identity, compositions and inverses. A cyclic group is generated by powers of one element. An abelian group has commuting elements.

The selected set $`\Pi`$ need not be a group. Choosing a reference $`\pi_0`$ removes its common offset and defines

```math
G_\Pi=\left\langle\pi_0^{-1}\pi:\pi\in\Pi\right\rangle.
```

Angle brackets mean the group generated by those relative permutations. If it is abelian, the selected orders lie inside a left coset $`\pi_0H`$ of an abelian subgroup $`H`$. A coset is the subgroup translated by the same permutation; the selected orders themselves need not include its identity or be closed under composition. Conjugation, $`g\mapsto hgh^{-1}`$, relabels all elements consistently and preserves whether they commute. The [reference-independence argument](../science/order_criterion.md#relative-permutations) shows that changing $`\pi_0`$ leaves the generated relative group unchanged.

Any two alternatives have only one nonidentity relative generator. Their relative group is cyclic, so no pair of orders can create the entanglement in this project for any identical channel. This remains true with arbitrarily many slots. With at most two slots, there are at most two orders, giving a separate minimum on calls.

Three slots allow $`012,021,102`$. Relative to $`012`$, the other orders are $`a=(1\;2)`$ and $`b=(0\;1)`$. They fail to commute: $`(ab)(0)=2`$, whereas $`(ba)(0)=1`$. In contrast, $`012,120,201`$ are powers of one cycle and still face the obstruction. The number of alternatives alone is insufficient; their relative structure matters.

Watrous represents permutations by unitaries on tensor factors. Commuting unitaries have a common eigenbasis. Theorem 1.5 states this for two commuting normal operators, meaning operators that commute with their adjoints; unitaries satisfy that condition. A finite family follows by successively refining their common invariant eigenspaces. Diagonalizing each operator in a separately chosen basis would not provide the single basis needed below.

## 7. A common Kraus basis proves universal impossibility

For a target channel with $`r`$ Kraus operators, form an operator-valued vector with $`r^n`$ entries:

```math
B_{\boldsymbol a}=K_{a_{n-1}}\cdots K_{a_0},
\qquad
(Q_\pi x)_{\boldsymbol a}
=x_{(a_{\pi(0)},\ldots,a_{\pi(n-1)})}.
```

The vector's entries are target operators; its index is the environmental tuple. This formal index space is distinct from the target and provides no accessible memory. The physical order family satisfies $`A^\pi=Q_\pi B`$.

Watrous Eq. (7.3) sends a basis word to the word indexed by $`\pi^{-1}`$. Expressing that same action on coefficients gives the displayed formula with $`\pi`$. Thus $`Q_\pi=W_\pi`$ and $`Q_\pi Q_\tau=Q_{\pi\tau}`$. The inverse in the basis action must not be inserted a second time into the coefficient action.

Relative to $`B^{(0)}=Q_{\pi_0}B`$, the relevant matrices are

```math
R_\pi=Q_\pi Q_{\pi_0}^\dagger=Q_{\pi\pi_0^{-1}}.
```

These right-relative permutations are a common conjugate of the left-relative generators defining $`G_\Pi`$. If the group is abelian, one unitary matrix $`V`$ diagonalizes every $`R_\pi`$, with eigenvalues $`\lambda_{\pi,\ell}`$ of modulus one.

At each transformed index $`\ell`$, all branches now use the same target operator $`L_\ell`$, multiplied by branch-dependent phases $`\lambda_{\pi,\ell}`$. Those phases form a diagonal controller operator. Applying the same $`V`$ to the entire joint Kraus family therefore gives

```math
\widetilde W_\ell=D_\ell\otimes L_\ell,
\qquad
D_\ell=\sum_{\pi\in\Pi}\lambda_{\pi,\ell}
|\pi\rangle\langle\pi|,
\qquad
L_\ell=(VB^{(0)})_\ell.
```

Kraus freedom preserves the joint channel, and the product form preserves separability. The [full proof](../science/order_criterion.md#proof-of-abelian-sufficiency) therefore works for every target dimension, every channel and every separable input. Faithfulness, meaning that different group elements have different representing matrices, is unnecessary for this direction.

The converse is a different statement: nonabelian support must permit at least one legitimate identical channel to entangle. It does not assert that every chosen channel works. The [earlier two-history mechanisms](../references/RELATED_WORK.md#two-history-obstructions) and the textbook tools explain important ingredients, but do not provide this physical existence construction.

## 8. The inherited state criterion and the missing realization

**Milestone M14.** Suppose a controller could apply arbitrary target unitaries $`U_i`$ to an initially maximally mixed target of dimension $`D`$. Its joint output would be

```math
\sigma=\frac1D\sum_{i,j}
\alpha_i\overline{\alpha_j}|i\rangle\langle j|
\otimes U_iU_j^\dagger.
```

The blocks pair each unitary with another's adjoint. This controlled-unitary state is separable exactly when the relative unitaries $`U_iU_0^\dagger`$ commute; otherwise it is NPT. The result is inherited from [Roszak's pure-dephasing criterion](../references/RELATED_WORK.md#roszak2018), specialized to a maximally mixed target and a pure controller with nonzero supported amplitudes.

The [local proof](../science/channel_realizations.md#proof) explains why the boundary is sharp. A common right multiplication makes $`U_0=I`$ without changing the state. An invertible diagonal controller filter removes the nonzero amplitudes. The partial transpose then has an identity reference block. Eliminating that block through a Schur complement leaves zero diagonal blocks and off-diagonal commutators. A positive matrix cannot have a nonzero off-diagonal block alongside those zero diagonal blocks, so positivity forces commutation. Conversely, a common eigenbasis gives an explicit mixture of product states.

The invertibility requirement explains why zero amplitudes must be removed from the occupied support. It also shows why the lemma is not an arbitrary mixed-controller classification.

This result guides the converse, but arbitrary controlled target gates are not supplied by the project. Repeated instances of one channel must generate the required unitary-block state through their allowed noise histories. That realizability requirement is the substantive next step.

## 9. A marker converts time into a target state

**Milestones M15–M16.** For $`n\ge2`$ and $`0\lt p\lt1`$, the [marker channel](../science/channel_realizations.md#the-linear-dimension-channel) has an empty state, $`n`$ marker states and an absorbing failure state, giving target dimension $`n+2`$. It starts empty. One Kraus operator $`K_0`$ preserves the empty state and cyclically shifts markers, with amplitude $`\sqrt{1-p}`$; it leaves failure unchanged. Another, $`K_1`$, inserts marker 0 from the empty state with amplitude $`\sqrt{p}`$. Operators $`F_j`$ send marker $`j`$ to failure with amplitude $`\sqrt{p}`$.

The empty and marker sectors each have total squared amplitude $`(1-p)+p=1`$, and the failure sector has weight one. Their orthogonality gives the Kraus completeness relation. The marker is internal to the counted target; no external protected memory is added.

Exactly one insertion, followed by shifts without failure, reaches the final marker sector. No insertion leaves the target empty; a second insertion annihilates a surviving trajectory; failure cannot return. If slot $`r`$ carries the insertion, its time position is $`\pi^{-1}(r)`$. There are $`n-1-\pi^{-1}(r)`$ later shifts, so the final marker is

```math
U_\pi|r\rangle=|n-1-\pi^{-1}(r)\rangle.
```

For $`n=3`$, an insertion in physical slot 1 makes the chronology explicit:

| Order | Slot 1's time position | Later shifts | Final marker |
|---|---:|---:|---|
| $`012`$ | 1 | 1 | $`\lvert1\rangle`$ |
| $`021`$ | 2 | 0 | $`\lvert0\rangle`$ |
| $`102`$ | 0 | 2 | $`\lvert2\rangle`$ |

All surviving insertion tuples have squared amplitude $`p(1-p)^{n-1}`$. Summing over their inaccessible slot labels produces precisely the inherited conditional-unitary state after normalization, with $`D=n`$. Its total probability is $`q=np(1-p)^{n-1}`$; at $`n=3,p=1/3`$ this is $`4/9`$.

Write $`P_\pi|r\rangle=|\pi(r)\rangle`$ and let $`J`$ reverse the marker labels. Then $`U_\pi=JP_{\pi^{-1}}`$, and

```math
U_\pi U_{\pi_0}^\dagger
=J P_{(\pi_0^{-1}\pi)^{-1}}J^\dagger.
```

This natural representation is faithful: different permutations move some marker differently. Noncommuting relative orders therefore produce noncommuting relative unitaries, and the inherited lemma gives NPT.

The conclusion concerns the **unconditional output**. A local projection onto the marker sector cannot turn a PPT state into an NPT state: after partial transpose, the operation still sandwiches the previous matrix between an operator and its adjoint, which preserves positivity. The full output is also block diagonal in empty, marker and failure sectors, so the other sectors cannot cancel the negative marker block. Filtering reveals entanglement already present.

Choosing $`p=1/n`$ gives $`q=(1-1/n)^{n-1}\gt e^{-1}`$. One channel fixed by $`n`$ works for every nonabelian support and every pure controller occupying it. This probability does not bound the entanglement amount uniformly: supported amplitudes can approach zero. The marker channel itself is not entanglement breaking.

## 10. Complete definite-order erasure is a separate realization

**Milestone M16.** The [shift/reset channel](../science/channel_realizations.md#complete-erasure-in-every-definite-order) uses $`n`$ internal registers, each of dimension $`s\ge2`$:

```math
\mathcal N(\rho)=\mathrm{Tr}_1(\rho)\otimes I_s/s.
```

Each call discards the first register, shifts the rest and appends a maximally mixed register. After $`n`$ calls every original register has disappeared, so $`\mathcal N^n=\Delta`$ on every input operator.

Starting from $`|0\rangle^{\otimes n}`$, the fresh appended symbols appear in the chronological word $`a_{\pi(0)}\cdots a_{\pi(n-1)}`$. Their unitary is $`V_\pi=P_{\pi^{-1}}`$ in Watrous's tensor-permutation convention. Words with one 1 and otherwise zeros already distinguish all permutations, giving faithfulness and the same conditional-unitary criterion.

This target has dimension $`s^n`$. It establishes complete definite-order erasure, while the marker construction establishes linear dimension. These are distinct channels with distinct resource properties; neither single slot is entanglement breaking for $`n\ge2`$.

## 11. The minimal qubit example

**Milestones M17–M18.** A two-level target suffices at the minimum of three calls and three alternatives. The channel has

```math
K_0=|+\rangle\langle0|,
\qquad K_1=|-\rangle\langle1|,
\qquad |\pm\rangle=(|0\rangle\pm|1\rangle)/\sqrt2.
```

It measures in the computational basis and prepares the corresponding $`X`$-basis state. Applied to one part of any target–reference state, it gives a sum of positive reference operators tensored with the prepared states, so it is entanglement breaking. Watrous's Exercise 6.1 states this measure-and-prepare characterization.

For an arbitrary operator $`X`$,

```math
\mathcal N(X)=X_{00}|+\rangle\langle+|
+X_{11}|-\rangle\langle-|.
```

Both computational-basis diagonal entries are $`\mathrm{Tr}(X)/2`$. A second call therefore yields $`\mathrm{Tr}(X)I_2/2`$. The channel is unital, so a third call leaves that result unchanged. The equality holds on the full operator space, including off-diagonal matrix units. Every complete definite order therefore erases every target input state.

The target starts in $`|0\rangle`$ and the controller in the equal superposition of $`012,021,102`$. For the matrix representation, the controller labels mean

```math
|0\rangle_C=|012\rangle,
\qquad |1\rangle_C=|021\rangle,
\qquad |2\rangle_C=|102\rangle.
```

The joint basis is $`|0,0\rangle,|0,1\rangle,|1,0\rangle,|1,1\rangle,|2,0\rangle,|2,1\rangle`$, with controller first. There are eight independent binary Kraus tuples. Writing $`K_j=A_j/\sqrt2`$ with integer matrices $`A_j`$ makes their joint contributions exact. Tuple $`000`$ gives the integer vector $`(1,1,1,1,1,1)^T`$; tuple $`001`$ gives $`(1,-1,1,1,1,-1)^T`$. Each carries the common amplitude factor $`1/\sqrt{24}`$.

These environmental alternatives are summed as outer products, not added coherently to each other. Coherence remains among the three order components within each vector. The [complete tuple table and matrix](../science/qubit_example.md#3-exact-output-from-the-kraus-sum) give

```math
\rho=\frac1{24}\sum_{\boldsymbol i}
b_{\boldsymbol i}b_{\boldsymbol i}^T,
\qquad
v=\frac13(-2,0,2,0,0,-1)^T,
\qquad
\langle v|\rho^{\Gamma_T}|v\rangle=-\frac1{54}.
```

The normalized vector $`v`$ supplies an exact NPT certificate for the unconditional $`3\times2`$ output. Combined with the two-alternative obstruction, this proves attainability of both three-call and three-alternative minima. A one-dimensional target cannot be entangled, so the qubit also attains the nontrivial target-dimension minimum.

A [local controller projection](../science/qubit_example.md#5-a-local-projection-exposes-two-qubit-entanglement) onto the span of $`(|1\rangle-|0\rangle)/\sqrt2`$ and $`|2\rangle`$ succeeds with probability $`1/2`$. The resulting two-qubit state's partial transpose has a principal minor $`-1/72`$. It is a mixed entangled state, not a pure Bell pair obtained from one copy.

## 12. Noise tolerance has three different meanings

**Milestone M19.** For $`0\le\eta\le1`$, fully dephasing the uniform controller with probability $`1-\eta`$ gives $`\eta|+_3\rangle\langle+_3|+(1-\eta)I_3/3`$. Each diagonal target block is maximally mixed, so this example gives

```math
\rho_\eta=\eta\rho+(1-\eta)I_6/6.
```

Thus controller dephasing and joint output white noise describe the same state family here. They are not equivalent noise operations on arbitrary inputs.

The fixed vector $`v`$ gives expectation $`(9-10\eta)/54`$ and certifies entanglement for $`\eta\gt9/10`$. Optimizing through the full partial-transpose spectrum gives the exact transition at the unique root in $`[0,1]`$ of

```math
2\eta_*^3-7\eta_*^2+4=0,
\qquad \eta_*\simeq0.8724474860298.
```

Because the system is $`3\times2`$, PPT sufficiency proves separability for $`\eta\le\eta_*`$, including equality, and NPT for $`\eta\gt\eta_*`$. The tolerated specified admixture is therefore below approximately $`12.7553\%`$. The fixed witness's $`10\%`$ limit is sufficient but not exact for the state family. The [robustness derivation](../science/robustness.md) supplies the polynomial and exact rational bracket.

For arbitrary physical output perturbations, let $`W=(|v\rangle\langle v|)^{\Gamma_T}`$. Its operator norm is $`8/9`$. Watrous's Schatten Hölder inequality gives

```math
\mathrm{Tr}(W\widetilde\rho)
\le-\frac1{54}+\frac89\|\widetilde\rho-\rho\|_1.
```

Consequently $`\|\widetilde\rho-\rho\|_1\lt1/48`$ is another sufficient certificate. In the project's half-norm trace-distance convention, the radius is $`1/96`$. This is a conservative output-state bound. Relating it to errors in individual devices would require an additional implementation-specific analysis.

## 13. The order-support contribution and its boundaries

**Milestones M20 and M29–M30.** The [order-support theorem](../science/order_criterion.md#theorem-1-the-order-support-criterion) combines two directions. Abelian relative orders force a product Kraus representation for every identical channel and preserve every separable input. Nonabelian relative orders admit an explicit channel that produces NPT for every pure controller with that occupied support. The latter is an existence statement over channels and does not classify arbitrary mixed controllers.

Channel-specific restrictions remain meaningful. Depolarizer blocks share a target eigenbasis and yield separable outputs even on nonabelian supports. Pauli products change only by phases when reordered, again giving product Kraus operators. A common final entanglement-breaking slot destroys retained $`C:T`$ entanglement; for example, $`0123,0213,1023`$ all end in slot 3 despite their nonabelian relative structure. These [boundaries](../science/interpretation.md#channel-families-that-remain-nonentangling) exclude a universal converse restricted to entanglement-breaking channels.

Calls, occupied control labels and full target dimension are separate resources. Ideal coherent order is supplied, and the internal marker or register dimensions are counted. A final filter is a diagnostic of existing entanglement. The endpoint is retained $`C:T`$ entanglement from an independent input; recovering an unknown target's entanglement with a remote reference, increasing communication capacity and certifying causal structure are different tasks with different requirements.

The [claim map](../science/README.md#claim-and-proof-map) connects the general theorem to analytical proofs. [Exact verification](../verification/README.md#what-these-checks-establish) supports the finite qubit matrix, witness and noise polynomial, while numerical marker examples check consistency of the construction. These checks have different evidential roles and do not replace one another.

Watrous supplies channel representations, separability and permutation tools. The [primary literature](../references/RELATED_WORK.md) supplies the conditional-unitary criterion, earlier two-history obstructions and established switch settings. The project's additional step is the complete constrained boundary: relative order commutation gives universal impossibility, and its failure is realized by actual repeated identical channels. The minimal qubit example makes that distinction concrete even when each slot is entanglement breaking and every definite-order target output is completely erased.

<a id="shared-noise-bridge"></a>

## 14. From a Schur map to physical noisy orders

**Milestones M21–M22.** Global dephasing multiplies every pair of different order labels by the same number. Physical local noise instead acts on the bits that encode those labels. The distinction matters because different label pairs can disagree on different numbers of bits.

Watrous §4.1.3 supplies the entrywise, or Schur, map language. A phase flip Z occurs on each bit with probability $`z`$, independently and without an accessible error flag. Set $`\gamma=1-2z`$. A controller matrix element between physical codewords $`b_i,b_j`$ is multiplied by

```math
\Gamma_{ij}=\gamma^{d_H(b_i,b_j)}.
```

The exponent $`d_H`$ counts bit positions that differ. At $`\gamma=4/5`$, a single-bit disagreement retains factor .8 while a two-bit disagreement retains factor .64. This is 10% phase-flip probability *per physical bit*, not global dephasing with parameter .8.

Encode chronological orders A=012, B=021 and C=102 into three distinct basis states of two bits. Up to bit flips and interchange of the physical bits, exactly three assignments remain: the distance-two pair is AB, AC or BC. One unused codeword stays unoccupied. The joint output therefore has an occupied 3-by-2 support even though the physical register and target together have dimension eight. The [physical-noise definition](../science/noisy_separation.md#physical-control-noise) makes these assignments explicit.

The shared raw slot measures the target’s Z axis, prepares the opposite states of an axis at angle $`\theta=\pi/2+\delta`$, and adds depolarization:

```math
\mathcal N_{\epsilon,\theta}
=(1-\epsilon)\operatorname{Ad}_{R_y(\theta)}\circ\mathcal D_Z
+\epsilon\Delta.
```

This remains entanglement breaking at every angle and has full Choi rank when $`\epsilon>0`$. The orthogonal point is the earlier measure-Z/prepare-X example, with an admixture; the special squared-channel erasure identity does not persist for nonzero tilt. The experiment fixes $`\epsilon=1/100`$ and uses independent copies of the *raw* slot. A target unitary attached to each slot would change the supplied resource. These [shared family and access definitions](../science/noisy_separation.md#shared-family) make the later transfer test meaningful.

<a id="grid-continuity-bridge"></a>

## 15. From exact grid calculations to a uniform theorem

**Milestones M23–M25.** A rational grid and a continuity estimate perform different parts of the proof. A finite list of positive numerical eigenvalues would not by itself prove a statement at every angle.

Choose $`\delta_k=2\arctan(k/400)`$ for $`k=-41,\ldots,41`$. At each angle the two prepared columns are proportional to the integer vectors $`(400-k,400+k)`$ and $`(-400-k,400-k)`$. The denominators are known positive numbers, so the complete Kraus sums and control-noise factors can be contracted in rational arithmetic.

For the retained experiment, all 83 grid points and all three physical encodings give 249 exact certificates:

```math
\bigl(\rho_{CT}^{(\ell)}(\delta_k)\bigr)^{\Gamma_T}
-\frac{I_6}{100}\succ0.
```

An exact LDL decomposition proves this inequality by positive rational pivots. The $`I_6`$ is essential: the unused physical controller state supplies zero eigenvalues in the full eight-dimensional space. On occupied support, PPT is sufficient for separability because the bipartite dimension is 3-by-2.

The recovery experiment uses four raw slots, the sister project’s eight physical codes, uniform preparation and the fixed P2 signed herald. It keeps a reference R initially entangled with T. Its accepted, unnormalized Bell output is $`\tau`$. Define

```math
p=\operatorname{Tr}\tau,\qquad
f=\langle\Phi|\tau|\Phi\rangle,\qquad
w=f-\frac p2.
```

Every separable two-qubit output satisfies $`f\le p/2`$, so $`w>0`$ certifies entanglement. The real Y-covariant accepted branch has success effect $`pI`$; its normalized Bell fidelity is $`F=f/p`$ and success is input independent. This does not assert the same property for every possible complex controller. The 83 exact rational contractions certify $`w>1/125`$ and $`1/25<p<9/100`$ on the grid. The [certificate derivation](../science/noisy_separation.md#exact-grid-certificate) fixes the factors arising from controller amplitudes and Bell normalization.

To reach every angle, factor the slot through a common Stinespring isometry followed by $`R_y(\theta)`$. Telescoping the product of $`r`$ slot isometries, then tracing environments and applying the same control noise, gives

```math
\|\Omega_\delta-\Omega_{\delta'}\|_1
\le4r\sin(|\delta-\delta'|/4)
\le r|\delta-\delta'|.
```

The grid covers $`[-.2,.2]`$ radians with nearest-point distance at most $`1/400`$. The three-slot retained state loses at most $`3/400`$ of its partial-transpose operator margin: partial transpose preserves the Hilbert–Schmidt norm, which is bounded by trace norm. The four-slot accepted witness has observable norm one half, so its witness and acceptance bounds each lose at most $`1/200`$. The [continuity proof](../science/noisy_separation.md#continuity-proof) therefore establishes, uniformly for $`|\delta|\le .2`$,

```math
\bigl(\rho_{CT}^{(\ell)}(\delta)\bigr)^{\Gamma_T}
\succ\frac{I_6}{400},\qquad
w>\frac3{1000},\qquad
\frac7{200}<p<\frac{19}{200},\qquad
F>\frac{101}{190}.
```

All three specified retained outputs are separable, while the accepted R:T output is NPT. Exact finite arithmetic supplies the grid margins; the analytical bound pays for the angles between them. The [uniform theorem](../science/noisy_separation.md#uniform-separation) keeps both parts visible.

<a id="recovery-connection-bridge"></a>

## 16. What transfers to recovery, and what remains a different question

**Milestones M26–M30.** The two experiments share the channel family and independent physical-bit noise. They use different resources and ask about different outputs:

| Quantity | Retained experiment | Recovery experiment |
|---|---|---|
| Channel calls per attempt | Three | Four |
| Physical controller bits | Two | Three |
| Input | Independent controller and known target state | Independent controller and a Bell-correlated reference–target input |
| Output assessed | Unconditional C:T | Conditional R:T after the P2 herald |
| Uniform conclusion | Separable on occupied support | NPT, with explicit acceptance and fidelity bounds |

The accepted fresh-pair experiment costs $`4/p`$ slot calls on average. The probability bounds put that quantity between $`800/19`$ and $`800/7`$. They do not permit retrying the same failed unknown input or establish an unassisted communication rate. The theorem compares these specified protocols; it does not optimize equal resources or rule out every alternative retained-state protocol.

The sister [controller-feasibility theorem](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/controller_optimization.md#controller-feasibility) represents all permitted preparations, ancillas and final effects by one positive-matrix budget. Its [orthogonal recovery frontier](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/recovery_frontier.md#frontier-theorem) is attained by physical three-X readout with outcome-dependent target corrections. The [tilted theorem](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/tilted_readout.md#tilted-optimality) retains that optimum for $`|t|\le1/5`$, where $`t=\tan(\delta/2)`$. That interval means $`|\delta|\le2\arctan(1/5)\simeq .39479112`$ radians; it is wider than the $`.2`$-radian interval of the specified-protocol separation above and follows from a different certificate.

The frontier proof first bounds a Bell-input objective over arbitrary controllers and then proves a real input-independent attaining representative. Complex accepted branches need not have scalar success. In particular, a maximum Bell fidelity at most one half does not imply that every possible complex-controller Choi output is separable. The [real-controller reduction](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/controller_optimization.md#real-controller-reduction) supplies the precise statement.

Likewise, full-rank raw slots and a strictly positive unobserved Schur-noise floor obstruct finite exact recovery in the sister [no-go theorem](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/noisy_recovery_obstruction.md#strict-schur-obstruction). This does not cancel the positive noisy-fidelity frontier or classify every other controller-noise process. It shows which assumptions must be checked before transferring an exactness conclusion.

Watrous supplies the shared language of channels, instruments, positive operators, norms and separability. The project develops the order-support realization and the exact grid-plus-continuity experiment; the sister develops the full recovery optimization and tilted envelope certificate. Their common foundation is credited once, while each endpoint keeps its own proof and resource statement. The [verification guide](../verification/README.md) and [related-work account](../references/RELATED_WORK.md) distinguish analytical arguments, exact certificate obligations, numerical crosschecks and inherited ingredients.
