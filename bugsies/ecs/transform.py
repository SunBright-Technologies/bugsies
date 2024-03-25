import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Transform:
    x: float = 0
    y: float = 0
    scale_x: float = 1
    scale_y: float = 1
    rotation: float = 0  # in degrees?

    @property
    def rotation_rad(self) -> float:
        return math.radians(self.rotation)

    def __add__(self, other: object) -> "Transform":
        if not isinstance(other, Transform):
            raise TypeError(f"unsupported operand type(s) for +: 'Transform' and '{type(other)}'")
        return combine(self, other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Transform):
            return False
        rotation_diff = math.fmod(self.rotation - other.rotation, 360)
        return (
            self.isclose(self.x, other.x)
            and self.isclose(self.y, other.y)
            and self.isclose(self.scale_x, other.scale_x)
            and self.isclose(self.scale_y, other.scale_y)
            and self.isclose(rotation_diff, 0)
        )

    @staticmethod
    def isclose(x1: float, x2: float) -> bool:
        if x1 == 0 or x2 == 0:
            return math.isclose(x1, x2, abs_tol=1e-9)
        return math.isclose(x1, x2)


def combine(t1: Transform, t2: Transform) -> Transform:
    # the new x and y need to take into account the rotation of t1 and the scale of t1
    # Precompute sine and cosine
    cos_theta = math.cos(t1.rotation_rad)
    sin_theta = math.sin(t1.rotation_rad)

    # Combine transformations
    new_x = t1.x + t2.x * cos_theta * t1.scale_x - t2.y * sin_theta * t1.scale_y
    new_y = t1.y + t2.x * sin_theta * t1.scale_x + t2.y * cos_theta * t1.scale_y
    new_scale_x = t1.scale_x * t2.scale_x
    new_scale_y = t1.scale_y * t2.scale_y
    new_rotation = math.fmod(t1.rotation + t2.rotation, 360)

    return Transform(x=new_x, y=new_y, scale_x=new_scale_x, scale_y=new_scale_y, rotation=new_rotation)
