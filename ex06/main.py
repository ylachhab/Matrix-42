from matrix_lib.cross_product import cross_product
from matrix_lib.vector import Vector

def main():
    u = Vector([0., 0., 1.])
    v = Vector([1., 0., 0.])
    assert cross_product(u, v).data == [0., 1., 0.]

    u = Vector([1., 0., 0.])
    v = Vector([0., 1., 0.])
    assert cross_product(u, v).data == [0., 0., 1.]

    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    assert cross_product(u, v).data == [-3., 6., -3.]

    print("All Exercise 06 tests passed!")

if __name__ == "__main__":
    main()