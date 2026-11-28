from __future__ import annotations
from types import NotImplementedType


class Complex:
    def __init__(
        self,
        real: float = 0.0,
        imag: float = 0.0
    ) -> None:
        self.real = real
        self.imag = imag

    @staticmethod
    def _to_complex(x: object) -> Complex | NotImplementedType:
        if isinstance(x, Complex):
            return x

        if isinstance(x, (int, float)):
            return Complex(x, 0.0)

        return NotImplemented

    def __repr__(self) -> str:
        return f"Complex({self.real}, {self.imag})"

    def __str__(self) -> str:
        sign = "+" if self.imag >= 0 else "-"
        imag = self.imag if self.imag >= 0 else -self.imag
        return f"{self.real} {sign} {imag}i"

    def __add__(self, other: object) -> Complex | NotImplementedType:
        other = self._to_complex(other)

        if other is NotImplemented:
            return NotImplemented

        return Complex(
            self.real + other.real,
            self.imag + other.imag
        )

    __radd__ = __add__

    def __sub__(self, other: object) -> Complex | NotImplementedType:
        other = self._to_complex(other)

        if other is NotImplemented:
            return NotImplemented

        return Complex(
            self.real - other.real,
            self.imag - other.imag
        )

    def __rsub__(self, other: object) -> Complex | NotImplementedType:
        other = self._to_complex(other)

        if other is NotImplemented:
            return NotImplemented

        return other - self

    def __mul__(self, other: object) -> Complex | NotImplementedType:
        other = self._to_complex(other)

        if other is NotImplemented:
            return NotImplemented

        real_part = (
            self.real * other.real
            - self.imag * other.imag
        )

        imag_part = (
            self.real * other.imag
            + self.imag * other.real
        )

        return Complex(real_part, imag_part)

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> Complex | NotImplementedType:
        other = self._to_complex(other)

        if other is NotImplemented:
            return NotImplemented

        denominator = other.magnitude_squared()

        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        real_part = (
            self.real * other.real
            + self.imag * other.imag
        ) / denominator

        imag_part = (
            self.imag * other.real
            - self.real * other.imag
        ) / denominator

        return Complex(real_part, imag_part)

    def __rtruediv__(self, other: object) -> Complex | NotImplementedType:
        other = self._to_complex(other)

        if other is NotImplemented:
            return NotImplemented

        return other / self

    def __eq__(self, other: object) -> bool | NotImplementedType:
        other = self._to_complex(other)

        if other is NotImplemented:
            return NotImplemented

        return (
            self.real == other.real
            and self.imag == other.imag
        )

    def conjugate(self) -> Complex:
        return Complex(self.real, -self.imag)

    def magnitude_squared(self) -> float:
        return self.real * self.real + self.imag * self.imag

    def __abs__(self) -> float:
        return self.magnitude_squared() ** 0.5


EPSILON = 1e-10


def magnitude(value: int | float | Complex) -> float:
    """|value| without calling abs(): sqrt for Complex, sign flip for reals."""
    if isinstance(value, Complex):
        return value.magnitude_squared() ** 0.5
    return value if value >= 0 else -value


def is_zero(
    value: int | float | Complex,
    scale: float = 1.0
) -> bool:
    tolerance = EPSILON * scale

    if isinstance(value, Complex):
        return value.magnitude_squared() <= tolerance * tolerance

    return -tolerance <= value <= tolerance