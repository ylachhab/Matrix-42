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

    # exercise 3
    def dot(self, v: "Vector[K]", ) -> K:
        if len(v.data) != len(self.data):
            raise ValueError("Vectors must have the same size")
        if not self.data:
            raise ValueError("Vectors cannot be empty")
        result = self.data[0] * v.data[0]
        for i in range(1, len(self.data)):
            result = result + self.data[i] * v.data[i]
        return result

    # exercise 4
    @staticmethod
    def _abs(x: float) -> float:
        return x if x >= 0 else -x


    def norm_1(self) -> float:
        if not self.data:
            raise ValueError("Vectors cannot be empty")
        result = self._abs(self.data[0])
        for i in range(1, len(self.data)):
            result = result + self._abs(self.data[i])
        return result

    def norm(self) -> float:
        if not self.data:
            raise ValueError("Vectors cannot be empty")
        result = pow(self.data[0], 2)
        for i in range(1, len(self.data)):
            result = result + pow(self.data[i], 2)
        return pow(result, 0.5)

    def norm_inf(self) -> float:
        if not self.data:
            raise ValueError("Vectors cannot be empty")
        result = self._abs(self.data[0])
        for i in range(1, len(self.data)):
            result = max(result, self._abs(self.data[i]))
        return result 


    def __str__(self) -> str:
        return "\n".join(f"[{x}]" for x in self.data)


# uv venv --python 3.14 .venv
# source .venv/bin/activate