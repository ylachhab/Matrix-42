from matrix_lib.projection import projection
from math import pi
from pathlib import Path


def main():
    p = projection(70 * pi / 180, 16 / 9, 0.1, 100.)

    project_root = Path(__file__).resolve().parent.parent
    display_dir = project_root / "matrix_display"
    if not display_dir.is_dir():
        display_dir = project_root / "display_macos"
    output_path = display_dir / "proj"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w") as file:
        # The viewer reads the file in column-major order.
        for row in p.transpose().data:
            file.write(", ".join(str(value) for value in row))
            file.write("\n")

    print(p)
    print(f"Projection saved to {output_path}")


if __name__ == "__main__":
    main()
