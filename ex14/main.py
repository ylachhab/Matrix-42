from matrix_lib.projection import projection
from math import pi
from pathlib import Path


def main():
    p = projection(70 * pi / 180, 16 / 9, 0.1, 100.)

    output_path = Path(__file__).resolve().parent.parent / "display_macos" / "proj"
    with output_path.open("w") as file:
        # The viewer reads the file in column-major order.
        for row in p.transpose().data:
            file.write(", ".join(str(value) for value in row))
            file.write("\n")

    print(p)


if __name__ == "__main__":
    main()
