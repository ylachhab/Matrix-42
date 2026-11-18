from matrix_lib.field import Field

class Vector[K: Field]:
    def __init__(self, data: list[K]) -> None:
        self.data = list(data)
    
    def add(self, v: "Vector[K]") -> None:
        if len(v.data) != len(self.data):
            raise ValueError("Vectors must have the same size")
        for i in range(len(self.data)):
            self.data[i] = self.data[i] + v.data[i]

    def sub(self, v: "Vector[K]") -> None:
        if len(v.data) != len(self.data):
            raise ValueError("Vectors must have the same size")
        for i in range(len(self.data)):
            self.data[i] = self.data[i] - v.data[i]

    def scl(self, a: K) -> None:
        for i in range(len(self.data)):
            self.data[i] = self.data[i] * a

    def __str__(self) -> str:
        return "\n".join(f"[{x}]" for x in self.data)