from matrix_lib.projection import projection
from math import pi


def main():
    p = projection(70 * pi / 180, 16 / 9, 0.1, 100.)

    with open("matrix_display/proj", "w") as file:
        for row in p.data:
            file.write(", ".join(str(value) for value in row))
            file.write("\n")

    print(p)


if __name__ == "__main__":
    main()