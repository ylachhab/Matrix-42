
from matrix_lib.complex import Complex, is_zero
from matrix_lib.vector import Vector
from matrix_lib.matrix import Matrix


# Real vector tests
u = Vector([3.0, 4.0])

assert u.dot(u) == 25.0
assert u.norm_1() == 7.0
assert u.norm() == 5.0
assert u.norm_inf() == 4.0

print("[PASS] Real vector tests")


# Complex vector tests
u = Vector([
    Complex(2, 3),
    Complex(4, -1)
])

v = Vector([
    Complex(1, 2),
    Complex(3, 2)
])

assert u.dot(v) == Complex(18, 12)
assert u.dot(u) == Complex(30, 0)

assert abs(u.norm_1() - 7.728656901081649) < 1e-10
assert abs(u.norm() - 5.477225575051661) < 1e-10
assert abs(u.norm_inf() - 4.123105625617661) < 1e-10

print("[PASS] Complex vector tests")

# Addition
a = Vector([Complex(2, 3), Complex(4, 5)])
b = Vector([Complex(1, 2), Complex(3, 4)])

a.add(b)

assert a.data == [
    Complex(3, 5),
    Complex(7, 9)
]

print("[PASS] Complex vector addition")

# Scaling
a = Vector([Complex(2, 3), Complex(4, 5)])
a.scl(Complex(2, 0))

assert a.data == [
    Complex(4, 6),
    Complex(8, 10)
]

assert is_zero(1e-12) == True
assert is_zero(1e-12, 1e-12) == False
assert is_zero(0.0, 1e-12) == True

assert is_zero(Complex(0, 0)) == True
assert is_zero(Complex(1e-12, 0), 1e-12) == False

print("[PASS] Zero detection tests")

print("[PASS] Complex vector scaling")

print("\nAll Vector tests passed!")
