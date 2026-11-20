from matrix_lib.field import Field
from matrix_lib.vector import Vector


class Matrix[K: Field]:
    def __init__(self, data: list[list[K]]) -> None:
        if data:
            for row in data:
                if len(row) != len(data[0]):
                    raise ValueError("All rows must have the same length")
        self.data = [list(row) for row in data]

    def shape(self) -> tuple[int, int]:
        """(rows, columns)"""
        if not self.data:
            return (0, 0)
        return (len(self.data), len(self.data[0]))

    def add(self, v: "Matrix[K]") -> None:
        if v.shape() != self.shape():
            raise ValueError("Matrices must have the same shape")
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] = self.data[i][j] + v.data[i][j]

    def sub(self, v: "Matrix[K]") -> None:
        if v.shape() != self.shape():
            raise ValueError("Matrices must have the same shape")
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] = self.data[i][j] - v.data[i][j]

    def scl(self, a: K) -> None:
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] = self.data[i][j] * a

    # exercise 07
    def mul_vec(self, vec: Vector[K]) -> Vector[K]:
        if not self.data:
            raise ValueError("Matrix should not be empty")
        if len(vec.data) != len(self.data[0]):
            raise ValueError("Matrix columns must equal the vector length")
        result = [0.] * len(self.data)
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                result[i] += self.data[i][j] * vec.data[j]
        return Vector(result)

    def mul_mat(self, mat: "Matrix[K]") -> "Matrix[K]":
        if not self.data or not mat.data:
            raise ValueError("Matrices must not be empty")
        if len(self.data[0]) != len(mat.data):
            raise ValueError(
                "Columns of the first matrix must equal rows of the second"
            )

        result = []
        for _ in range(len(self.data)):
            result.append([0.] * len(mat.data[0]))
            
        for i in range(len(self.data)):
            for j in range(len(mat.data[0])):
                for k in range(len(self.data[0])):
                    result[i][j] += self.data[i][k] * mat.data[k][j]
        return Matrix(result)

    def __str__(self) -> str:
        return "\n".join(
            f"[{', '.join(str(x) for x in row)}]" for row in self.data
        )