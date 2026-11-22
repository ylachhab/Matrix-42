from matrix_lib.matrix import Matrix

def main():
    # Test 1: Square matrix
    a = Matrix([
        [1., 2.],
        [3., 4.]
    ])

    print(a.transpose().data, a.transpose().data == [
        [1., 3.],
        [2., 4.]
    ])

    # Test 2: Rectangular matrix
    a = Matrix([
        [1., 2., 3.],
        [4., 5., 6.]
    ])

    print(a.transpose().data, a.transpose().data == [
        [1., 4.],
        [2., 5.],
        [3., 6.]
    ])

    # Test 3: Single row
    a = Matrix([[1., 2., 3.]])

    print(a.transpose().data, a.transpose().data == [
        [1.],
        [2.],
        [3.]
    ]
    )
    # Test 4: Double transpose
    a = Matrix([[1., 2.], [3., 4.]])
    print(a.transpose().transpose().data, a.transpose().transpose().data == a.data)

if __name__ == "__main__":
    main()