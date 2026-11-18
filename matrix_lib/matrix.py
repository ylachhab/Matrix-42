from matrix_lib.field import Field

class Matrix[K: Field]:
    def __init__(self, data: list[list[K]]) -> None:
        # if data and any(len(row) != len(data[0]) for row in data):
        if data:
            for row in data:
                if len(row) != len(data[0]):
                    raise ValueError("Matrices must have the same shape")
        self.data = [list(row) for row in data]
    

    def shape(self) -> tuple[int, int]:
        if not self.data:
            return (0, 0)
        return (len(self.data), len(self.data[0]))

    def add(self, v: "Matrix[K]") -> None:
        if v.shape() != self.shape():
            raise ValueError("Matrixs must have the same size")
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] = self.data[i][j] + v.data[i][j]

    def sub(self, v: "Matrix[K]") -> None:
        if v.shape() != self.shape():
            raise ValueError("Matrixs must have the same size")
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] = self.data[i][j] - v.data[i][j]
    def scl(self, a: K) -> None:
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] = self.data[i][j] * a

    def __str__(self) -> str:
        return "\n".join(f"[{', '.join(str(x) for x in col)}]" for col in self.data)