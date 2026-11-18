from matrix_lib.interpolation import lerp
from matrix_lib.vector import Vector
from matrix_lib.matrix import Matrix

def main():
    print(lerp(0., 1., 0.))     # 0.0
    print(lerp(0., 1., 1.))     # 1.0
    print(lerp(0., 1., 0.5))   # 0.5
    print(lerp(21., 42., 0.3)) # 27.3
    assert lerp(0., 1., 0.5) == 0.5

    assert lerp(
        Vector([2., 1.]),
        Vector([4., 2.]),
        0.5
    ).data == [3., 1.5]

    assert lerp(
        Matrix([[2., 1.], [3., 4.]]),
        Matrix([[4., 2.], [5., 8.]]),
        0.5
    ).data == [[3., 1.5], [4., 6.]]

    print(lerp(0., 42., 0.5))      # 21.0
    print(lerp(-42., 42., 0.5))    # 0.0
    print(lerp(0., 1., 2.))        # 2.0 (t outside [0, 1])
    print(lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3))   # [2.6] / [1.3]
    print(lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20., 10.], [30., 40.]]), 0.5))
    # [11.0, 5.5] / [16.5, 22.0]

    print("All Exercise 02 tests passed!")

if __name__ == "__main__":
    main()