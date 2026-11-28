
from typing import Protocol, Self


class Field(Protocol):
    def __add__(self, other: Self) -> Self:
        ...

    def __sub__(self, other: Self) -> Self:
        ...

    def __mul__(self, other: Self) -> Self:
        ...

    def __truediv__(self, other: Self) -> Self:
        ...

    def __abs__(self) -> float:
        ...

    def conjugate(self) -> Self:
        ...

    @property
    def real(self) -> float:
        ...

    @property
    def imag(self) -> float:
        ...
