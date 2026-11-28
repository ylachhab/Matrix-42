from matrix_lib.field import Field
from matrix_lib.complex import magnitude


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

    # Exercise 03
    def dot(self, v: "Vector[K]") -> K:
        if len(v.data) != len(self.data):
            raise ValueError("Vectors must have the same size")

        if not self.data:
            raise ValueError("Vectors cannot be empty")

        result = self.data[0].conjugate() * v.data[0]

        for i in range(1, len(self.data)):
            result = result + self.data[i].conjugate() * v.data[i]

        return result

    # Exercise 04
    def norm_1(self) -> float:
        if not self.data:
            raise ValueError("Vectors cannot be empty")

        result = 0.0

        for value in self.data:
            result += magnitude(value)

        return result

    def norm(self) -> float:
        if not self.data:
            raise ValueError("Vectors cannot be empty")

        result = 0.0

        for value in self.data:
            result += (
                value.real * value.real
                + value.imag * value.imag
            )

        return result ** 0.5

    def norm_inf(self) -> float:
        if not self.data:
            raise ValueError("Vectors cannot be empty")

        result = magnitude(self.data[0])

        for i in range(1, len(self.data)):
            result = max(result, magnitude(self.data[i]))

        return result

    def __str__(self) -> str:
        return "\n".join(f"[{x}]" for x in self.data)