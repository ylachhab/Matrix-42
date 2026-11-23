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

    # exercise 08
    def trace(self) -> K:
        if not self.data:
            raise ValueError("Matrix should not be empty")
        if len(self.data) != len(self.data[0]):
            raise ValueError("Matrix must be square")
        result = self.data[0][0]
        for i in range(1, len(self.data)):
            result = result + self.data[i][i]
        return result
        # return sum(self.data[i][i] for i in range(len(self.data)))

    # exercise 09
    # def transpose(self) -> "Matrix[K]":
    #     if not self.data:
    #         raise ValueError("Matrix should not be empty")
    #     result = []
    #     for j in range(len(self.data[0])):
    #         result.append([0.] * len(self.data))
    #     for i in range(len(self.data)):
    #         for j in range(len(self.data[i])):
    #             result[j][i] = self.data[i][j]
    #     return Matrix(result)
    def transpose(self) -> "Matrix[K]":
        if not self.data:
            raise ValueError("Matrix should not be empty")
        rows, cols = self.shape()
        return Matrix([[self.data[i][j] for i in range(rows)] for j in range(cols)])

    # exercise 10
    def row_echelon(self) -> "Matrix[K]":
        if not self.data:
            raise ValueError("Matrix should not be empty")
        rows, cols = self.shape()
        result = [row.copy() for row in self.data]

        pivot_row = 0
        for col in range(cols):
            if pivot_row >= rows:
                break

            if result[pivot_row][col] == 0:
                for r in range(pivot_row + 1, rows):
                    if result[r][col] != 0:
                        result[pivot_row], result[r] = result[r], result[pivot_row]
                        break
                
            if result[pivot_row][col] == 0:
                continue

            pivot_value = result[pivot_row][col]

            for c in range(col, cols):
                result[pivot_row][c] /= pivot_value

            for r in range(rows):
                if r == pivot_row:
                    continue
                factor = result[r][col]
                for c in range(col, cols):
                    result[r][c] -= factor * result[pivot_row][c]

            pivot_row += 1

        return Matrix(result)

    # exercise 11
    def determinant(self) -> K:
        rows, cols = self.shape()
        if rows != cols or rows == 0:
            raise ValueError("Matrix must be non-empty and square")
        if rows == 1:
            return self.data[0][0]
        if rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        if rows == 3:
            return (self.data[0][0] *(self.data[1][1] * self.data[2][2] - self.data[1][2] * self.data[2][1])
            - self.data[0][1] * (self.data[1][0] * self.data[2][2] - self.data[1][2] * self.data[2][0])
            + self.data[0][2] * (self.data[1][0] * self.data[2][1] - self.data[1][1] * self.data[2][0]))
        if rows == 4:
            def minor_of(col: int) -> "Matrix[K]":
                return Matrix([
                    [self.data[r][c] for c in range(4) if c != col]
                    for r in range(1, 4)
                ])

            result = self.data[0][0] * minor_of(0).determinant()
            sign = -1
            for col in range(1, 4):
                result += sign * (self.data[0][col] * minor_of(col).determinant())
                sign = -sign
            return result
        raise NotImplementedError("Determinant not implemented for matrices larger than 4x4")


    def __str__(self) -> str:
        return "\n".join(
            f"[{', '.join(str(x) for x in row)}]" for row in self.data
        )