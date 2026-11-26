from matrix_lib.complex import Complex
from matrix_lib.vector import Vector
from matrix_lib.cosine import angle_cos
from matrix_lib.matrix import Matrix

def main():
    # print(Complex.magnitude(3 + 4j))
    # print(Complex.magnitude(-5))
    # print(Complex.magnitude(0j))

    # print(Complex.conjugate(2 + 3j))
    # print(Complex.conjugate(4 - 2j))
    # print(Complex.conjugate(5))

    # u = Vector([2 + 3j, 4 - 1j])
    # v = Vector([1 + 2j, 3 + 2j])

    # print(u.dot(v))
    # print(u.dot(u))
    # u = Vector([2 + 3j, 4 - 1j])
    # v = Vector([1 + 2j, 3 + 2j])

    # print("Dot product:", u.dot(v))
    # print("Dot with itself:", u.dot(u))
    # print("Norm 1:", u.norm_1())
    # print("Norm 2:", u.norm())
    # print("Norm inf:", u.norm_inf())

    # print("\nReal vector tests:")
    # r = Vector([3., 4.])

    # print("Dot product:", r.dot(r))
    # print("Norm 1:", r.norm_1())
    # print("Norm 2:", r.norm())
    # print("Norm inf:", r.norm_inf())

    # print(angle_cos(
    #     Vector([1 + 0j]),
    #     Vector([0 + 1j])
    # ))

    # print(angle_cos(
    #     Vector([1 + 1j, 0j]),
    #     Vector([0j, 2 + 1j])
    # ))

    # print(angle_cos(
    #     Vector([2 + 3j, 4 - 1j]),
    #     Vector([1 + 2j, 3 + 2j])
    # ))

    # print(angle_cos(
    #     Vector([1., 0.]),
    #     Vector([-1., 0.])
    # ))

    # print(Complex.is_zero(0))
    # print(Complex.is_zero(1e-16))
    # print(Complex.is_zero(1e-16 + 2e-16j))
    # print(Complex.is_zero(0.001))
    # print(Complex.is_zero(2 + 3j))

    # m = Matrix([
    #     [3 + 2j, 1 + 2j],
    #     [6 + 4j, 2 + 4j]
    # ])

    # print("Original matrix:")
    # print(m)

    # print("Row echelon:")
    # print(m.row_echelon())

    # print("Rank:", m.rank())


    m = Matrix([
        [3 + 2j, 1 + 2j],
        [6 + 4j, 2 + 4j]
    ])

    print("Row echelon:")
    print(m.row_echelon())

    print("Rank:", m.rank())

    m = Matrix([
        [1 + 1j, 2],
        [0, 1 - 1j]
    ])

    inv = m.inverse()

    print("Inverse:")
    print(inv)

    print("Matrix * Inverse:")
    print(m.mul_mat(inv))

    m = Matrix([
        [3 + 2j, 1 + 2j],
        [6 + 4j, 2 + 4j]
    ])

    try:
        print(m.inverse())
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()