from matrix_lib.matrix import Matrix
from matrix_lib.vector import Vector

def main():
    a = Matrix([
        [1., 0.],
        [0., 1.]
    ])
    u = Vector([4., 2.])
    print(a.mul_vec(u).data, a.mul_vec(u).data == [4., 2.])

    a = Matrix([
        [2., 0.],
        [0., 2.]
    ])
    print(a.mul_vec(u).data, a.mul_vec(u).data == [8., 4.])

    a = Matrix([
        [2., -2.],
        [-2., 2.]
    ])
    u = Vector([4., 2.])
    print(a.mul_vec(u).data, a.mul_vec(u).data == [4., -4.])

    a = Matrix([
        [1., 2.],
        [3., 4.]
    ])
    u = Vector([5., 6.])
    print(a.mul_vec(u).data, a.mul_vec(u).data == [17., 39.])

    # matrix multiplication tests
    a = Matrix([
        [1., 0.],
        [0., 1.]
    ])
    b = Matrix([
        [1., 0.],
        [0., 1.]
    ])
    print(a.mul_mat(b).data, a.mul_mat(b).data == [[1., 0.], [0., 1.]])

    u = Matrix([
        [1., 0.],
        [0., 1.]
    ])
    v = Matrix([
        [2., 1.],
        [4., 2.]
    ])
    print(u.mul_mat(v).data, u.mul_mat(v).data == [[2., 1.], [4., 2.]])

    a = Matrix([
        [3., -5.],
        [6., 8.]
    ])

    b = Matrix([
        [2., 1.],
        [4., 2.]
    ])
    print(a.mul_mat(b).data, a.mul_mat(b).data == [[-14., -7.], [44., 22.]])

    a = Matrix([[1., 2.], [3., 4.]])
    b = Matrix([[5., 6.], [7., 8.]])
    r = a.mul_mat(b)
    print(r.data, r.data == [[19., 22.], [43., 50.]])

    a = Matrix([[1., 2., 3.], [4., 5., 6.]])
    b = Matrix([[7., 8.], [9., 10.], [11., 12.]])
    r = a.mul_mat(b)
    print(r.data, r.data == [[58., 64.], [139., 154.]])


if __name__ == "__main__":
    main()