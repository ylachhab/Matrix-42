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

if __name__ == "__main__":
    main()
