#!/usr/bin/env python3
"""Numerical checks of the n+2-dimensional converse channel for n=3,4.

Requires NumPy. Exhaustively sums environmental Kraus labels for each of these
two finite cases and compares the resulting filtered state with the analytical
natural-permutation formula. This checks conventions, normalization, and a
nonabelian/abelian pair; it does not prove the theorem for arbitrary n.
"""

from fractions import Fraction
from itertools import product
import json
import numpy as np


def partial_transpose_target(a, dc, dt):
    return a.reshape(dc, dt, dc, dt).transpose(0, 3, 2, 1).reshape(dc*dt, dc*dt)


def channel_kraus(n, p):
    # Basis: empty, markers 0,...,n-1, fail.
    d = n+2
    k0 = np.zeros((d, d))
    k0[0, 0] = np.sqrt(1-p)
    k0[-1, -1] = 1
    for j in range(n):
        k0[1+(j+1)%n, 1+j] = np.sqrt(1-p)
    k1 = np.zeros((d, d))
    k1[1, 0] = np.sqrt(p)
    operators = [k0, k1]
    for j in range(n):
        f = np.zeros((d, d))
        f[-1, 1+j] = np.sqrt(p)
        operators.append(f)
    return operators


def switch_output(operators, orders):
    d = operators[0].shape[0]
    n = len(orders[0])
    m = len(orders)
    out = np.zeros((m*d, m*d))
    for labels in product(range(len(operators)), repeat=n):
        vector = []
        for order in orders:
            state = np.eye(d)[:, 0]
            for slot in order:
                state = operators[labels[slot]] @ state
            vector.extend(state/np.sqrt(m))
        out += np.outer(vector, vector)
    return out


def natural_permutation(order):
    n = len(order)
    u = np.zeros((n, n))
    for position, slot in enumerate(order):
        u[n-1-position, slot] = 1
    return u


def expected_marker_state(orders):
    n = len(orders[0])
    unitaries = [natural_permutation(order) for order in orders]
    return np.block([[u @ v.T/(n*len(orders)) for v in unitaries]
                     for u in unitaries])


def check_case(n, orders, should_entangle):
    d = n+2
    p = 1/n
    operators = channel_kraus(n, p)
    completeness_error = np.linalg.norm(sum(k.T@k for k in operators)-np.eye(d))
    output = switch_output(operators, orders)
    marker_indices = [c*d+1+j for c in range(len(orders)) for j in range(n)]
    subnormalized = output[np.ix_(marker_indices, marker_indices)]
    success = np.trace(subnormalized)
    normalized = subnormalized/success
    predicted = expected_marker_state(orders)
    formula_error = np.linalg.norm(normalized-predicted)
    exact_success = Fraction(n-1, n)**(n-1)
    min_pt_filtered = np.linalg.eigvalsh(partial_transpose_target(normalized, len(orders), n))[0]
    min_pt_unconditional = np.linalg.eigvalsh(partial_transpose_target(output, len(orders), d))[0]
    assert completeness_error < 1e-12
    assert abs(np.trace(output)-1) < 1e-12
    assert abs(success-float(exact_success)) < 1e-12
    assert formula_error < 1e-12
    if should_entangle:
        assert min_pt_filtered < -1e-3
        assert min_pt_unconditional < -1e-3
    else:
        assert min_pt_filtered > -1e-12
        assert min_pt_unconditional > -1e-12
    return {
        "n": n, "target_dimension": d, "orders_chronological": orders,
        "relative_family": "nonabelian" if should_entangle else "abelian",
        "completeness_error": float(completeness_error),
        "trace": float(np.trace(output)),
        "filter_success": float(success),
        "filter_success_exact": str(exact_success),
        "normalized_formula_error": float(formula_error),
        "min_eigenvalue_partial_transpose_filtered": float(min_pt_filtered),
        "min_eigenvalue_partial_transpose_unconditional": float(min_pt_unconditional),
    }


def main():
    records = []
    for n in [3, 4]:
        e = list(range(n))
        swap01, swap12 = e[:], e[:]
        swap01[0], swap01[1] = swap01[1], swap01[0]
        swap12[1], swap12[2] = swap12[2], swap12[1]
        records.append(check_case(n, [e, swap01, swap12], True))
        cyclic = [[(position+shift)%n for position in range(n)] for shift in range(3)]
        records.append(check_case(n, cyclic, False))
    print(json.dumps({"status": "all finite marker checks passed", "numpy": np.__version__,
                      "cases": records}, indent=2))


if __name__ == "__main__":
    main()
