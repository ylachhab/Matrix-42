from matrix_lib.vector import Vector

def main():
    assert Vector([0., 0.]).dot(Vector([1., 1.])) == 0.
    assert Vector([1., 1.]).dot(Vector([1., 1.])) == 2.
    assert Vector([-1., 6.]).dot(Vector([3., 2.])) == 9.

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

    print("All Exercise 03 tests passed!")

if __name__ == "__main__":
    main()