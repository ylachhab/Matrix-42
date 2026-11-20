from matrix_lib.vector import Vector

def main():
    u = Vector([0., 0., 0.])
    assert u.norm_1() == 0.
    assert u.norm() == 0.
    assert u.norm_inf() == 0.

    u = Vector([1., 2., 3.])
    assert u.norm_1() == 6.
    assert abs(u.norm() - 14 ** 0.5) < 1e-9
    assert u.norm_inf() == 3.

    u = Vector([-3., 4.])
    assert u.norm_1() == 7.
    assert u.norm() == 5.
    assert u.norm_inf() == 4.

    u = Vector([-10., 2.])
    assert u.norm_1() == 12.
    assert abs(u.norm() - 104 ** 0.5) < 1e-9
    assert u.norm_inf() == 10.

    print("All Exercise 04 tests passed!")

if __name__ == "__main__":
    main()