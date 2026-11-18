from matrix_lib.field import Field
from matrix_lib.vector import Vector

def linear_combination[K: Field](u: list[Vector[K]], coefs: list[K]) -> Vector[K]:
    if len(u) != len(coefs):
        raise ValueError("vectors and coefficients must have the same length")
    if not u:
        raise ValueError("vectors list cannot be empty")
    size = len(u[0].data)
    for vec in u:
        if len(vec.data) != size:
            raise ValueError("all vectors must have the same size")

    result = [u[0].data[j] * coefs[0] for j in range(size)]
    for i in range(1, len(u)):
        for j in range(size):
            result[j] = result[j] + u[i].data[j] * coefs[i]
    return Vector(result)