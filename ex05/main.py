from matrix_lib.cosine import angle_cos
from matrix_lib.vector import Vector

def main():

    print(angle_cos(Vector([1., 0.]), Vector([1., 0.])))
    print(angle_cos(Vector([1., 0.]), Vector([0., 1.])))
    print(angle_cos(Vector([-1., 1.]), Vector([1., -1.])))
    print(angle_cos(Vector([2., 1.]), Vector([4., 2.])))
    print(angle_cos(Vector([1., 2., 3.]), Vector([4., 5., 6.])))
    print(angle_cos(Vector([8., 7.]), Vector([3., 2.])))
    print(angle_cos(Vector([3., 2.]), Vector([8., 7.])))

if __name__ == "__main__":
    main()