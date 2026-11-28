from matrix_lib.matrix import Matrix


def main():
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.],
    ])
    print(u.inverse(), u.inverse().data == u.data)

    u = Matrix([
        [2., 0., 0.],
        [0., 2., 0.],
        [0., 0., 2.],
    ])
    expected = Matrix([
        [0.5, 0.0, 0.0],
        [0.0, 0.5, 0.0],
        [0.0, 0.0, 0.5],
    ])
    print(u.inverse(), u.inverse().data == expected.data)

    u = Matrix([
        [8., 5., -2.],
        [4., 7., 20.],
        [7., 6., 1.],
    ])
    print(u.inverse())

    u = Matrix([
        [1., 2.],
        [3., 4.],
    ])
    print(u.inverse(), u.inverse().data == [[-2., 1.], [1.5, -0.5]])

    # A * A^-1 should give (approximately) the identity
    print(u.mul_mat(u.inverse()))

    # Singular matrix: an error is expected, not a crash
    singular = Matrix([
        [1., 2.],
        [2., 4.],
    ])
    try:
        singular.inverse()
    except ValueError as error:
        print(f"Singular matrix correctly rejected: {error}")
    else:
        raise AssertionError("Singular matrix should have raised")


if __name__ == "__main__":
    main()