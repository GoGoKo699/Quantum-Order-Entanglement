# Verification

The exact three-slot certificate requires Python 3.10 or later and only its standard library:

```bash
python3 verification/verify_exact.py
```

The program constructs the output by summing all eight independent environmental Kraus tuples. Every order tuple is chronological: its first listed slot acts first. It verifies the channel-square identity on all four matrix units, the full rational output, the negative partial-transpose witness, the local projection probability and negative principal minor, and the exact characteristic-polynomial and noise-threshold algebra. A successful run reports `all exact certificates passed`.

The optional finite marker checks require NumPy:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/verify_marker.py
```

These checks sum all Kraus tuples for the linear-dimension witness at three and four calls. In each dimension they compare the projected state with the natural-permutation formula, check its success probability, and contrast a nonabelian order family with a cyclic family. A successful run reports `all finite marker checks passed`. Matrix residuals should be below `1e-12`; tiny negative eigenvalues of order `1e-16` in the abelian examples are floating-point roundoff.

## Expected scientific certificates

| Quantity | Result |
|---|---|
| Three-slot output | The [stated integer matrix](../science/qubit_example.md#3-exact-output-from-the-kraus-sum) divided by 12 |
| Negative witness expectation | `-1/54` |
| Partial-transpose determinant | `-1/248832` |
| Local control projection success probability | `1/2` |
| Normalized projected partial-transpose principal minor | `-1/72` |
| Retained controller coherence threshold | Unique root of `2 eta^3 - 7 eta^2 + 4` in `[0,1]` |
| Threshold bracket | `0.8724474860298 < eta_star < 0.8724474860299` |
| Three-call marker success probability | `4/9` |
| Four-call marker success probability | `27/64` |

The committed [exact output](exact_results.json) contains rational certificates. The [marker output](marker_results.json) records finite numerical residuals and partial-transpose eigenvalues using NumPy 2.3.5. Numerical values can vary in their last digits across platforms; the analytical values and stated tolerances control the check.

## What these checks establish

The exact program establishes finite algebraic certificates by reconstructing the channel action. The marker program checks normalization and chronological order conventions in two finite cases. The [general theorem](../science/order_criterion.md) and its [converse](../science/channel_realizations.md) rest on the written analytical arguments; finite enumeration does not prove them for arbitrary dimensions or supports.

The [noise threshold](../science/robustness.md) concerns the specified mixture with full controller dephasing, equivalently output white noise for this example. Its exact separability interpretation uses the cited PPT criterion in dimension $`3\times2`$. It is not a threshold for arbitrary channel noise or general experimental imperfections.

The local controller projection exposes a mixed entangled two-qubit state. The calculation does not claim a pure Bell pair after one copy. Numerical PPT in the larger marker examples is a consistency check of the abelian theorem, not an independent proof of separability in those dimensions.

## Shared noisy-controller certificates

The two sister projects use the same [finite-certificate verifier](audit_verify.py)
and byte-identical copies of the six files in [certificates/](certificates/).
They implement the common four-slot raw-channel model, the physical order-code
map `[0,1,2,3,4,6,5,7]`, and unobserved controller phase noise. The shared
implementation uses Python 3.11 or later and the NumPy version pinned above;
it performs no network calls, imports no certificate-producing program, and
writes no files.

From the repository root:

```bash
python3 verification/audit_verify.py --root verification/certificates
python3 verification/audit_verify.py --root verification/certificates --rebuild
```

Both commands return a nonzero status if an exact equality or required bound
fails. The second includes everything in the first and additionally rebuilds
all tilted polynomial coefficients with Python integers. These commands read
the committed data; they do not regenerate a failed certificate in place.

| Certificate file | Contents and checked role |
|---|---|
| [family8_polynomials.npz](certificates/family8_polynomials.npz) | Orthogonal-family coefficient arrays: `Bp` has shape `(5,8,8)`, `Gp` has shape `(5,4,4,8,8)`, and `Aends` has shape `(4,5,8,8)`. All 6,720 coefficient entries, the eight orders, and their normalization are reconstructed from the 1,296 Kraus tuples. |
| [family8_local_polynomials.npz](certificates/family8_local_polynomials.npz) | Local-noise arrays `Bl` of shape `(5,4,8,8)` and `Al` of shape `(4,5,4,8,8)`: 6,400 coefficients together with the Hamming-distance masks and physical codes. The verifier checks these arrays against the independently reconstructed orthogonal coefficients. |
| [tilt_exact_polynomials.npz](certificates/tilt_exact_polynomials.npz) | Tilted coefficient arrays `Gx` of shape `(9,4,4,8,8)` and `Bx` of shape `(9,8,8)`: 9,792 entries, plus the physical Walsh matrix, the 17 coefficients of the degree-16 margin polynomial, and its common integer factor. The default checks the stored identities; `--rebuild` reconstructs every `Gx` and `Bx` entry. |
| [joint_tilt_certificate_results.json](certificates/joint_tilt_certificate_results.json) | All 249 exact retained-state records (83 grid points times three control encodings), including six rational LDL pivots each, and all 83 exact recovery probability, overlap, and witness records. Every record is recomputed and compared. |
| [local_physical_frontier.json](certificates/local_physical_frontier.json) | Readable summary of the physical local-noise example. The verifier independently reconstructs its mode capacities, optimal rewards, and deterministic endpoint from the polynomial arrays; it does not use this summary as input. |
| [separation_claims.json](certificates/separation_claims.json) | Readable summary of the specified-protocol separation and its limitations. The exact ledger and the analytical continuity argument establish the claims; this summary is not a proof input. |

The default command verifies the following exact obligations:

- The physical Walsh transformation; every coefficient of the tilted block
  identities; the degree-16 Bernstein positivity certificate on
  `-1/5 <= t <= 1/5`; and an independent rational Kraus contraction at `t=1/10`.
- All 249 controller–target partial-transpose certificates and all 83
  reference–target recovery certificates. It also checks the rational
  constants used to extend the grid to `|delta| <= 1/5` radians. The occupied
  controller–target space has dimension six.
- All orthogonal-family coefficients; 100 masked coefficient matrices that
  must be Walsh diagonal; the zero harmonics and cross-sector identities;
  the six-class reward table and its dominance on the full unit interval;
  and the exact physical local-noise frontier example.

A successful run prints `PASS` for the Walsh matrix, exact block identities,
and independent rational contraction, followed by JSON reports containing
`CT_exact_records_verified: 249`, `RT_exact_records_verified: 83`, and
`coefficient_matrices_Walsh_diagonal: 100`. The physical example has exact
maximum conditional Bell fidelity `1566163803/2065458803` and deterministic
endpoint fidelity `23664816609/50000000000`. With `--rebuild`, it additionally
prints `Python-integer coefficient reconstruction: PASS` and
`All stored polynomial coefficients: PASS`; the reconstructed absolute
intermediate bounds are `276540930048000` and `305648793600000`, both below
`2^63`.

These exact finite checks support the coefficient identities, positivity
margins, and stated examples. The controller-feasibility theorem, the
all-controller upper bound, the diagonal-envelope argument, the strict
Schur-noise obstruction, and the continuity estimate remain analytical proof
obligations in the linked scientific account. In particular, numerical Bell
fidelity at or below one half does not establish separability for every
possible complex controller. The retained and recovery experiments use
different call counts, control sizes, bipartitions, and conditioning; the
certificate suite does not turn them into an optimized equal-resource
comparison.

This repository owns the complete [retained-C:T/recovered-R:T separation proof](../science/noisy_separation.md).
The sister repository owns the shared [routing and noise model](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/noisy_routing_model.md),
[controller optimization](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/controller_optimization.md),
[orthogonal frontier](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/recovery_frontier.md), and
[tilted optimality proof](https://github.com/GoGoKo699/Quantum-Order-Distillation/blob/main/science/tilted_readout.md).
