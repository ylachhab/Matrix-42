class Complex:
    def __init__(self, real: float = 0.0, imag: float = 0.0) -> None:
        self.real = real
        self.imag = imag

    def __repr__(self) -> str:
        return f"Complex({self.real}, {self.imag})"

    def __add__(self, other: "Complex") -> "Complex":
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other: "Complex") -> "Complex":
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other: "Complex") -> "Complex":
        r = self.real * other.real - self.imag * other.imag
        i = self.real * other.imag + other.real * self.imag
        return Complex(r, i)

    def conjugate(self) -> "Complex":
        return Complex(self.real, -self.imag)

    def __truediv__(self, other: "Complex") -> "Complex":
        # Calculate the denominator
        # Check division by zero
        # Calculate the real part
        # Calculate the imaginary part
        # Return a new Complex object
        pass

    def __str__(self) -> str:
        return f"{self.real} {'+' if self.imag >= 0 else '-'} {abs(self.imag)}i"