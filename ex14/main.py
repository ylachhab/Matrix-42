from matrix_lib.projection import projection
from math import pi
from pathlib import Path


def main():
    p = projection(70 * pi / 180, 16 / 9, 0.1, 100.)

    project_root = Path(__file__).resolve().parent.parent
    # Both display programs read the same column-major matrix format.
    contents = "".join(
        ", ".join(str(value) for value in row) + "\n"
        for row in p.transpose().data
    )

    print(p)
    for folder in ("display_macos", "matrix_display"):
        output_path = project_root / folder / "proj"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(contents)
        print(f"Projection saved to {output_path}")


if __name__ == "__main__":
    main()
