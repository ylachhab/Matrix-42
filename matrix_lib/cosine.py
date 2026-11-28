# exercise 5
from matrix_lib.field import Field
from matrix_lib.vector import Vector
from matrix_lib.complex import Complex, magnitude


def angle_cos[K: Field](
    u: Vector[K],
    v: Vector[K]
) -> float:

    if len(u.data) != len(v.data):
        raise ValueError("Vectors must have the same length")

    # ||u||^2 and ||v||^2 are the dot product of a vector with itself.
    # Taking one square root of the product (instead of two separate
    # square roots) keeps results like 1.0 exact.
    uu = u.dot(u).real
    vv = v.dot(v).real

    if uu == 0 or vv == 0:
        raise ValueError(
            "Cannot calculate cosine with a zero vector"
        )

    dot = u.dot(v)

    # For complex vectors <u|v> is complex: use its modulus so that the
    # result stays a real number.
    if isinstance(dot, Complex):
        dot = magnitude(dot)

    result = dot / ((uu * vv) ** 0.5)

    # Guard against rounding pushing the result slightly outside [-1, 1].
    if result > 1.0:
        return 1.0
    if result < -1.0:
        return -1.0
    return result