from matrix_lib.vector import Vector


def main():
    tests = [
        ([0., 0.], [0., 0.], 0.),
        ([1., 0.], [0., 0.], 0.),
        ([1., 0.], [1., 0.], 1.),
        ([1., 0.], [0., 1.], 0.),
        ([1., 1.], [1., 1.], 2.),
        ([4., 2.], [2., 1.], 10.),
        ([0., 0.], [1., 1.], 0.),
        ([-1., 6.], [3., 2.], 9.),
    ]
    for a, b, expected in tests:
        result = Vector(a).dot(Vector(b))
        print(f"{a} . {b} = {result} (expected {expected})")
        assert result == expected, f"dot({a}, {b}) != {expected}"

    print("All Exercise 03 tests passed!")


if __name__ == "__main__":
    main()