from matrix_lib.vector import Vector
from matrix_lib.matrix import Matrix

def main():
    #  Test Vector operations
    # Addition
    print("Vector operations: ")
    v1 = Vector([2., 3.])
    v2 = Vector([5., 7.])
    v1.add(v2)
    print(v1)

    # Subtraction
    v3 = Vector([2., 3.])
    v4 = Vector([5., 7.])
    v3.sub(v4)
    print(v3)

    # Scaling
    v5 = Vector([2., 3.])
    v5.scl(2.)
    print(v5)
    print("\nMatrix operations: ")

    # Test Matrix operations
    # Addition
    m1 = Matrix([[1., 2.], [3., 4.]])
    m2 = Matrix([[7., 4.], [-2., 2.]])
    m1.add(m2)
    print(m1)

    # Subtraction
    m3 = Matrix([[1., 2.], [3., 4.]])
    m4 = Matrix([[7., 4.], [-2., 2.]])
    m3.sub(m4)
    print(m3)

    # Scaling
    m5 = Matrix([[1., 2.], [3., 4.]])
    m5.scl(2.)
    print(m5)

if __name__ == "__main__":
    main()
