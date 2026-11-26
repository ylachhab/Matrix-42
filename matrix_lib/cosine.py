# exercise 5
from matrix_lib.field import Field
from matrix_lib.vector import Vector
from matrix_lib.complex import Complex

def angle_cos[K: Field](u: Vector[K], v: Vector[K]) -> float:
    if len(u.data) != len(v.data):
        raise ValueError("Vectors must have the same length")
    unorm = u.norm()
    vnorm = v.norm()
    if unorm == 0 or vnorm == 0:
        raise ValueError("Cannot calculate cosine with a zero vector")
    dot = u.dot(v)

    if isinstance(dot, complex):
        dot = Complex.magnitude(dot)
    return dot / ( unorm * vnorm)                  