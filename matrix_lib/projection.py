from matrix_lib.matrix import Matrix
from math import tan

def projection(
    fov: float,
    ratio: float,
    near: float,
    far: float
) -> Matrix[float]:

    if fov <= 0 or fov >= 3.141592653589793:
        raise ValueError("Field of view must be between 0 and π")
    if ratio <= 0:
        raise ValueError("Ratio must be greater than 0")
    if near <= 0:
        raise ValueError("Near must be greater than 0")
    if far <= near:
        raise ValueError("Far must be greater than near")

    f = 1 / tan(fov / 2)

    scale_y = f

    scale_x = scale_y / ratio

    # Right-handed camera: visible points have negative z.
    # Map the near/far planes to the viewer's depth range [0, 1].
    a = -far / (far - near)
    b = -(far * near) / (far - near)

    result = Matrix([
    [scale_x, 0., 0., 0.],
    [0., scale_y, 0., 0.],
    [0., 0., a, b],
    [0., 0., -1., 0.],
    ])

    return result
