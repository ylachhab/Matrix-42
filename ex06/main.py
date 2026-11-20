from matrix_lib.cross_product import cross_product
from matrix_lib.vector import Vector

def main():
    u = Vector([0., 0., 1.])
    v = Vector([1., 0., 0.])
    print(cross_product(u, v).data, cross_product(u, v).data == [0., 1., 0.])
    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(cross_product(u, v).data, cross_product(u, v).data == [-3., 6., -3.])
    u = Vector([4., 2., -3.])
    v = Vector([-2., -5., 16.])
    print(cross_product(u, v).data, cross_product(u, v).data == [17., -58., -16.])    

if __name__ == "__main__":
    main()