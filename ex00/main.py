from matrix_lib.vector import Vector
from matrix_lib.matrix import Matrix

def main():
    # u = Vector([2., 3.])
    # v = Vector([5., 7.])
    # u.add(v)
    # print(u)

    u = Matrix([[1., 2.], [3., 4.]])
    v = Matrix([[7., 4.], [-2., 2.]])
    u.add(v)
    print(u)
    # [8.0, 6.0]
    # [1.0, 6.0]

if __name__ == "__main__":
    main()
