
from matrix_lib.complex import Complex
from matrix_lib.matrix import Matrix
from matrix_lib.vector import Vector


def assert_matrix_close(actual, expected, epsilon=1e-10):
    assert actual.shape() == expected.shape()

    rows, cols = actual.shape()

    for i in range(rows):
        for j in range(cols):
            assert abs(
                actual.data[i][j] - expected.data[i][j]
            ) < epsilon, f"Mismatch at ({i}, {j})"


def main() -> None:
    # Real matrix tests
    a = Matrix([
        [1.0, 2.0],
        [3.0, 4.0]
    ])

    assert a.shape() == (2, 2)
    assert a.trace() == 5.0
    assert a.determinant() == -2.0
    assert a.rank() == 2

    assert a.transpose().data == [
        [1.0, 3.0],
        [2.0, 4.0]
    ]

    print("[PASS] Real matrix operations")

    # Complex matrix addition
    a = Matrix([
        [Complex(1, 2), Complex(3, 4)],
        [Complex(5, 6), Complex(7, 8)]
    ])

    b = Matrix([
        [Complex(1, 1), Complex(1, 1)],
        [Complex(1, 1), Complex(1, 1)]
    ])

    a.add(b)

    assert a.data == [
        [Complex(2, 3), Complex(4, 5)],
        [Complex(6, 7), Complex(8, 9)]
    ]

    print("[PASS] Complex matrix addition")

    # Complex matrix subtraction
    a.sub(b)

    assert a.data == [
        [Complex(1, 2), Complex(3, 4)],
        [Complex(5, 6), Complex(7, 8)]
    ]

    print("[PASS] Complex matrix subtraction")

    # Complex matrix scaling
    a.scl(Complex(2, 0))

    assert a.data == [
        [Complex(2, 4), Complex(6, 8)],
        [Complex(10, 12), Complex(14, 16)]
    ]

    print("[PASS] Complex matrix scaling")

    # Matrix-vector multiplication
    a = Matrix([
        [Complex(1, 1), Complex(2, 0)],
        [Complex(0, 0), Complex(1, -1)]
    ])

    v = Vector([
        Complex(1, 0),
        Complex(0, 1)
    ])

    result = a.mul_vec(v)

    assert result.data == [
        Complex(1, 3),
        Complex(1, 1)
    ]

    print("[PASS] Complex matrix-vector multiplication")

    # Matrix-matrix multiplication
    identity = Matrix([
        [Complex(1, 0), Complex(0, 0)],
        [Complex(0, 0), Complex(1, 0)]
    ])

    assert a.mul_mat(identity).data == a.data

    print("[PASS] Complex matrix-matrix multiplication")

    # Trace
    assert a.trace() == Complex(2, 0)

    print("[PASS] Complex trace")

    # Transpose
    assert a.transpose().data == [
        [Complex(1, 1), Complex(0, 0)],
        [Complex(2, 0), Complex(1, -1)]
    ]

    print("[PASS] Complex transpose")

    # Conjugate transpose
    assert a.conjugate_transpose().data == [
        [Complex(1, -1), Complex(0, 0)],
        [Complex(2, 0), Complex(1, 1)]
    ]

    print("[PASS] Complex conjugate transpose")

    # Determinant
    assert a.determinant() == Complex(2, 0)

    print("[PASS] Complex determinant")

    # Row echelon
    assert_matrix_close(a.row_echelon(), identity)

    print("[PASS] Complex row echelon")

    # Inverse
    inverse = a.inverse()

    expected_inverse = Matrix([
        [Complex(0.5, -0.5), Complex(-1, 0)],
        [Complex(0, 0), Complex(0.5, 0.5)]
    ])

    assert_matrix_close(inverse, expected_inverse)

    print("[PASS] Complex inverse")

    # A * A^-1 = I
    assert_matrix_close(a.mul_mat(inverse), identity)

    print("[PASS] Complex inverse verification")

    # Rank
    assert a.rank() == 2

    singular = Matrix([
        [Complex(3, 2), Complex(1, 2)],
        [Complex(6, 4), Complex(2, 4)]
    ])

    assert singular.rank() == 1

    print("[PASS] Complex rank")

    # Singular matrix
    try:
        singular.inverse()
    except ValueError:
        pass
    else:
        raise AssertionError("Expected singular matrix error")

    print("[PASS] Singular matrix detection")

    # Original matrix remains unchanged
    assert a.data == [
        [Complex(1, 1), Complex(2, 0)],
        [Complex(0, 0), Complex(1, -1)]
    ]

    print("[PASS] Original matrix unchanged")

    print("\nAll Matrix tests passed!")


if __name__ == "__main__":
    main()
