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
