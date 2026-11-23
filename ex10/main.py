from matrix_lib.matrix import Matrix


def main():
    u = Matrix([
        [1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.],
        ])
    print(u.row_echelon(), u.row_echelon().data == [[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])

    u =  Matrix([
        [1., 2.],
        [3., 4.],
        ])
    print(u.row_echelon(), u.row_echelon().data == [[1., 0.], [0., 1.]])

    u =  Matrix([[1., 2.],
                 [2., 4.],])
    print(u.row_echelon(), u.row_echelon().data == [[1., 2.], [0., 0.]])

    u = Matrix([
        [8., 5., -2., 4., 28.],
        [4., 2.5, 20., 4., -4.],
        [8., 5., 1., 4., 17.],
        ])
    print(u.row_echelon().data)


if __name__ == "__main__":
    main()