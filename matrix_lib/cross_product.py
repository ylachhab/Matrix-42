# exercise 6
from matrix_lib.field import Field
from matrix_lib.vector import Vector

def cross_product[K: Field](u: Vector[K], v: Vector[K]) -> Vector[K]:
    if len(u.data) != 3 or len(v.data) != 3:
        raise ValueError("Vectors must be 3-dimensional")
    return Vector([
        u.data[1] * v.data[2] - u.data[2] * v.data[1],
        u.data[2] * v.data[0] - u.data[0] * v.data[2],
        u.data[0] * v.data[1] - u.data[1] * v.data[0]
    ])