from matrix_lib.vector import Vector
from matrix_lib.matrix import Matrix

def  lerp(u: float | Vector | Matrix, v: float | Vector | Matrix, t: float) -> float | Vector | Matrix:
    if isinstance(u, Vector) and isinstance(v, Vector):
        if len(u.data) != len(v.data):
            raise ValueError("Vectors must have the same size")
        result = []
        for i in range(len(u.data)):
            value = u.data[i] + (v.data[i] - u.data[i]) * t
            result.append(value)
        return Vector(result)
    if isinstance(u, Matrix) and isinstance(v, Matrix):
        if u.shape() != v.shape():
            raise ValueError("Matrixs must have the same size")
        result = []
        for i in range(len(u.data)):
            row = []
            for j in range(len(u.data[i])):
                value = u.data[i][j] + (v.data[i][j] - u.data[i][j]) * t
                row.append(value)
            result.append(row)
        return Matrix(result)
    if isinstance(u, (Vector, Matrix)) or isinstance(v, (Vector, Matrix)):
        raise TypeError("u and v must have the same type")
    return u + (v - u) * t