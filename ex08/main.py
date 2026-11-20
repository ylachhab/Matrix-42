from matrix_lib.matrix import Matrix

def main():
    u = Matrix([[1., 0.], [0., 1.]])
    print(u.trace(),u.trace() == 2.)  

    u = Matrix([
        [2., -5., 0.],
        [4., 3., 7.],
        [-2., 3., 4.],
    ])
    print(u.trace(), u.trace() == 9.)

    u = Matrix([
        [-2., -8., 4.],
        [1., -23., 4.],
        [0., 6., 4.],
    ])
    print(u.trace(), u.trace() == -21.)

    u = Matrix([
        [1., 2., 3.],
        [4., 5., 6.],
        [7., 8., 9.]
    ])
    print(u.trace(), u.trace() == 15.)


if __name__ == "__main__":
    main()