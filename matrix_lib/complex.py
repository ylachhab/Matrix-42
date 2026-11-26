EPSILON = 1e-10

class Complex:
    @staticmethod
    def magnitude(value: float | complex) -> float:
        return pow(pow(value.real, 2) + pow(value.imag, 2), 0.5)

    @staticmethod
    def conjugate(value: float | complex) -> float | complex:
        if isinstance(value, complex):
            return value.real - value.imag * 1j
        return value

    @staticmethod
    def is_zero(value: float | complex) -> bool:
        return Complex.magnitude(value) < EPSILON