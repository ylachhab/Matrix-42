from matrix_lib.complex import Complex
from matrix_lib.vector import Vector
from matrix_lib.matrix import Matrix
from matrix_lib.functions import linear_combination
from matrix_lib.interpolation import lerp
from matrix_lib.cosine import angle_cos
from matrix_lib.cross_product import cross_product


def close(a, b, eps=1e-10):
    return abs(a - b) < eps


def main() -> None:
    # Vector subtraction
    a = Vector([Complex(3, 5), Complex(7, 9)])
    b = Vector([Complex(1, 2), Complex(3, 4)])
    a.sub(b)
    assert a.data == [Complex(2, 3), Complex(4, 5)]
    print("[PASS] Complex vector subtraction")

    # Linear combination (complex coefficients)
    e1 = Vector([Complex(1, 0), Complex(0, 0)])
    e2 = Vector([Complex(0, 0), Complex(1, 0)])
    r = linear_combination([e1, e2], [Complex(2, 1), Complex(0, -3)])
    assert r.data == [Complex(2, 1), Complex(0, -3)]

    r = linear_combination(
        [Vector([Complex(1, 1)]), Vector([Complex(2, 0)])],
        [Complex(0, 1), Complex(1, 0)]
    )
    assert r.data == [Complex(1, 1)]   # i(1+i) + 2 = 1 + i
    print("[PASS] Complex linear combination")

    # Linear interpolation
    u = Vector([Complex(0, 0), Complex(2, 2)])
    v = Vector([Complex(2, 4), Complex(4, 2)])
    assert lerp(u, v, 0.0).data == u.data
    assert lerp(u, v, 1.0).data == v.data
    assert lerp(u, v, 0.5).data == [Complex(1, 2), Complex(3, 2)]
    assert lerp(Complex(0, 0), Complex(2, 4), 0.5) == Complex(1, 2)
    m = lerp(
        Matrix([[Complex(0, 0), Complex(2, 2)]]),
        Matrix([[Complex(2, 4), Complex(4, 2)]]),
        0.5
    )
    assert m.data == [[Complex(1, 2), Complex(3, 2)]]
    print("[PASS] Complex linear interpolation")

    # Cosine
    u = Vector([Complex(1, 1), Complex(2, 0)])
    assert close(angle_cos(u, u), 1.0)
    assert close(angle_cos(u, Vector([Complex(2, 2), Complex(4, 0)])), 1.0)
    orth = angle_cos(
        Vector([Complex(1, 0), Complex(0, 0)]),
        Vector([Complex(0, 0), Complex(0, 1)])
    )
    assert close(orth, 0.0)
    print("[PASS] Complex cosine")

    # Cross product (no conjugation)
    r = cross_product(
        Vector([Complex(0, 1), Complex(0, 0), Complex(0, 0)]),
        Vector([Complex(0, 0), Complex(1, 0), Complex(0, 0)])
    )
    assert r.data == [Complex(0, 0), Complex(0, 0), Complex(0, 1)]
    print("[PASS] Complex cross product")

    print("\nAll function tests passed!")


if __name__ == "__main__":
    main()
