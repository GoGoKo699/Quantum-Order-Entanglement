#!/usr/bin/env python3
"""Exact finite certificates for the three-slot entanglement-breaking example.

Python 3.10+; standard library only.  Matrices use controller-major order.
Each order tuple lists the slots in chronological order, first call first.
This verifies a finite construction and its one-parameter robustness algebra;
it is not a substitute for the architecture theorem's analytical proof.
"""

from fractions import Fraction as F
from itertools import product
import json


def zeros(rows, cols=None):
    return [[F(0) for _ in range(rows if cols is None else cols)] for _ in range(rows)]


def identity(n):
    out = zeros(n)
    for i in range(n):
        out[i][i] = F(1)
    return out


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, x):
    return [[x * y for y in row] for row in a]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def outer(v):
    return [[x * y for y in v] for x in v]


def quadratic(a, v):
    return sum((v[i] * a[i][j] * v[j]
                for i in range(len(v)) for j in range(len(v))), F(0))


def partial_transpose_target(a, dc, dt):
    return [[a[(i // dt) * dt + (j % dt)][(j // dt) * dt + (i % dt)]
             for j in range(dc * dt)] for i in range(dc * dt)]


def determinant(a):
    work = [row[:] for row in a]
    answer = F(1)
    for k in range(len(work)):
        pivot = next((i for i in range(k, len(work)) if work[i][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            work[k], work[pivot] = work[pivot], work[k]
            answer = -answer
        diagonal = work[k][k]
        answer *= diagonal
        for i in range(k + 1, len(work)):
            ratio = work[i][k] / diagonal
            for j in range(k + 1, len(work)):
                work[i][j] -= ratio * work[k][j]
    return answer


def characteristic_coefficients(a):
    """Descending coefficients via Newton identities and exact power traces."""
    n = len(a)
    powers = []
    current = identity(n)
    for _ in range(n):
        current = matmul(current, a)
        powers.append(trace(current))
    coefficients = [F(1)]
    for k in range(1, n + 1):
        coefficients.append(-sum((coefficients[k-j] * powers[j-1]
                                  for j in range(1, k + 1)), F(0)) / k)
    return coefficients


def multiply_polynomials(a, b):
    """Multiply arrays using one shared ascending or descending convention."""
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def channel(x):
    # K_j = A_j / sqrt(2), avoiding every floating-point square root.
    kraus_numerators = [
        [[F(1), F(0)], [F(1), F(0)]],
        [[F(0), F(1)], [F(0), F(-1)]],
    ]
    out = zeros(2)
    for a in kraus_numerators:
        out = add(out, scale(matmul(matmul(a, x), transpose(a)), F(1, 2)))
    return out


def build_output():
    kraus_numerators = [
        [[F(1), F(0)], [F(1), F(0)]],
        [[F(0), F(1)], [F(0), F(-1)]],
    ]
    orders = [(0, 1, 2), (0, 2, 1), (1, 0, 2)]
    out = zeros(6)
    for labels in product(range(2), repeat=3):
        vector = []
        for order in orders:
            state = [[F(1)], [F(0)]]
            for slot in order:
                state = matmul(kraus_numerators[labels[slot]], state)
            vector.extend([state[0][0], state[1][0]])
        # Three factors 1/sqrt(2), and controller amplitude 1/sqrt(3).
        out = add(out, scale(outer(vector), F(1, 24)))
    return out


def verify():
    # Full operator-basis check: this proves N^2(X)=Tr(X) I/2 by linearity.
    for i in range(2):
        for j in range(2):
            e = zeros(2)
            e[i][j] = F(1)
            expected = scale(identity(2), F(int(i == j), 2))
            assert channel(channel(e)) == expected
    assert channel(identity(2)) == identity(2)

    rho = build_output()
    expected_m = [
        [2, 0, 2, 0, 1, 0], [0, 2, 0, 0, 0, 1],
        [2, 0, 2, 0, 1, 0], [0, 0, 0, 2, 1, 0],
        [1, 0, 1, 1, 2, 0], [0, 1, 0, 0, 0, 2],
    ]
    assert rho == scale(expected_m, F(1, 12))
    assert trace(rho) == 1
    assert rho == transpose(rho)
    pt = partial_transpose_target(rho, 3, 2)
    v = [F(x, 3) for x in [-2, 0, 2, 0, 0, -1]]
    assert sum((x*x for x in v), F(0)) == 1
    witness_value = quadratic(pt, v)
    assert witness_value == -F(1, 54)
    assert determinant(pt) == -F(1, 248832)

    mpt = scale(pt, F(12))
    char = characteristic_coefficients(mpt)
    factor = [F(1)]
    for term in [[1, -1], [1, -2], [1, -3], [1, -6, 5, 2]]:
        factor = multiply_polynomials(factor, list(map(F, term)))
    assert char == factor

    # The physical projection has rows a=(-1,1,0)/sqrt(2), b=(0,0,1).
    # Use the rational unscaled a row, and retain its 1/sqrt(2) factors
    # symbolically: block 00 scales by 1/2; blocks 01 and 10 by 1/sqrt(2).
    q = [[-1, 0, 1, 0, 0, 0], [0, -1, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
    raw = matmul(matmul(q, rho), transpose(q))
    success = (raw[0][0] + raw[1][1])/2 + raw[2][2] + raw[3][3]
    assert success == F(1, 2)
    assert raw == [
        [F(0), F(0), F(0), F(0)],
        [F(0), F(1, 3), F(1, 12), -F(1, 12)],
        [F(0), F(1, 12), F(1, 6), F(0)],
        [F(0), -F(1, 12), F(0), F(1, 6)],
    ]
    # In normalized projected state the off-diagonal element is
    # raw[1][2]/(sqrt(2)*success)=1/(6sqrt(2)).
    filter_minor = -(raw[1][2]/success)**2 / 2
    assert filter_minor == -F(1, 72)

    # Complete controller dephasing gives I_6/6. A retained-coherence
    # parameter eta therefore produces eta*rho + (1-eta)*I_6/6.
    dephased = [[rho[i][j] if i//2 == j//2 else F(0)
                 for j in range(6)] for i in range(6)]
    assert dephased == scale(identity(6), F(1, 6))
    a = add(mpt, scale(identity(6), -F(2)))
    char_a = characteristic_coefficients(a)
    # det(2I+eta A) = eta^6 chi_A(-2/eta); ascending eta coefficients.
    determinant_eta = [coefficient * (-2)**(6-i)
                       for i, coefficient in enumerate(char_a)]
    assert determinant_eta == list(map(F, [64, 0, -128, 32, 28, -8, 0]))
    # Factorization: 4*(4-eta^2)*(4-7eta^2+2eta^3).
    factored_eta = multiply_polynomials([F(4), F(0), -F(1)],
                                        [F(4), F(0), -F(7), F(2)])
    assert determinant_eta == [4*x for x in factored_eta] + [F(0)]
    # The same rational witness has value (9-10eta)/54.
    assert quadratic(scale(identity(6), F(1, 6)), v) == F(1, 6)

    def threshold_polynomial(eta):
        return 2*eta**3 - 7*eta**2 + 4

    eta_lower = F(8724474860298, 10**13)
    eta_upper = F(8724474860299, 10**13)
    assert threshold_polynomial(eta_lower) > 0
    assert threshold_polynomial(eta_upper) < 0

    # Schmidt weights of v are 8/9 and 1/9. Thus ||(|v><v|)^Gamma||inf=8/9.
    # Hölder's inequality certifies entanglement whenever ||rho'-rho||_1<1/48.
    witness_operator_norm = F(8, 9)
    trace_norm_radius = -witness_value / witness_operator_norm
    assert trace_norm_radius == F(1, 48)

    return {
        "status": "all exact certificates passed",
        "channel_square": "X -> Tr(X) I_2/2 on all four matrix units",
        "rho_numerator_M": expected_m,
        "rho_denominator": 12,
        "partial_transpose_determinant": str(determinant(pt)),
        "normalized_witness_value": str(witness_value),
        "characteristic_polynomial_M_partial_transpose": [str(x) for x in char],
        "characteristic_factorization": "(x-1)(x-2)(x-3)(x^3-6x^2+5x+2)",
        "local_projection_success": str(success),
        "projected_partial_transpose_principal_minor": str(filter_minor),
        "coherence_threshold_polynomial": "2 eta^3 - 7 eta^2 + 4",
        "exact_threshold_bracket": [str(eta_lower), str(eta_upper)],
        "coherence_threshold_approx": 0.872447486029822,
        "noise_admixture_threshold_approx": 0.127552513970178,
        "simple_witness_certification": "eta > 9/10 (noise admixture < 1/10)",
        "sufficient_output_trace_norm_radius_strict": str(trace_norm_radius),
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
