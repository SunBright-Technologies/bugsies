import math

import pytest

from bugsies.ecs.transform import Transform

NULL_TRANSFORM = Transform()
TRANSLATION = Transform(x=10, y=15)
SCALING = Transform(scale_x=2, scale_y=3)
ROTATION_30 = Transform(rotation=30)
ROTATION_90 = Transform(rotation=90)

TRANSLATE_AND_SCALE = Transform(x=10, y=15, scale_x=2, scale_y=3)
TRANSLATE_AND_ROTATE = Transform(x=10, y=15, rotation=90)
SCALE_AND_ROTATE = Transform(scale_x=2, scale_y=3, rotation=90)
ALL_TRANSFORMS = Transform(x=10, y=15, scale_x=2, scale_y=3, rotation=90)


@pytest.mark.parametrize(
    "t1, t2, expected",
    [
        pytest.param(NULL_TRANSFORM, NULL_TRANSFORM, NULL_TRANSFORM, id="null transforms"),
        pytest.param(NULL_TRANSFORM, TRANSLATION, TRANSLATION, id="null + translation"),
        pytest.param(NULL_TRANSFORM, SCALING, SCALING, id="null + scale"),
        pytest.param(NULL_TRANSFORM, ROTATION_90, ROTATION_90, id="null + rotation"),
        pytest.param(NULL_TRANSFORM, ALL_TRANSFORMS, ALL_TRANSFORMS, id="null + all"),
        pytest.param(TRANSLATION, NULL_TRANSFORM, TRANSLATION, id="translation + null"),
        pytest.param(SCALING, NULL_TRANSFORM, SCALING, id="scale + null"),
        pytest.param(ROTATION_90, NULL_TRANSFORM, ROTATION_90, id="rotation + null"),
        pytest.param(ALL_TRANSFORMS, NULL_TRANSFORM, ALL_TRANSFORMS, id="all + null"),
        pytest.param(TRANSLATION, TRANSLATION, Transform(20, 30), id="translation + translation"),
        pytest.param(TRANSLATION, SCALING, Transform(10, 15, 2, 3), id="translation + scale"),
        pytest.param(TRANSLATION, ROTATION_90, Transform(10, 15, rotation=90), id="translation + rotation"),
        pytest.param(TRANSLATION, ALL_TRANSFORMS, Transform(20, 30, 2, 3, 90), id="translation + all"),
        pytest.param(SCALING, TRANSLATION, Transform(20, 45, 2, 3), id="scale + translation"),
        pytest.param(SCALING, SCALING, Transform(scale_x=4, scale_y=9), id="scale + scale"),
        pytest.param(SCALING, ROTATION_90, Transform(scale_x=2, scale_y=3, rotation=90), id="scale + rotation"),
        pytest.param(SCALING, ALL_TRANSFORMS, Transform(20, 45, 4, 9, 90), id="scale + all"),
        pytest.param(ROTATION_90, TRANSLATION, Transform(-15, 10, rotation=90), id="rotation + translation"),
        pytest.param(ROTATION_90, SCALING, Transform(scale_x=2, scale_y=3, rotation=90), id="rotation + scale"),
        pytest.param(ROTATION_90, ROTATION_90, Transform(rotation=180), id="rotation + rotation"),
        pytest.param(ROTATION_90, ALL_TRANSFORMS, Transform(-15, 10, 2, 3, 180), id="rotation + all"),
        pytest.param(ALL_TRANSFORMS, TRANSLATION, Transform(-35, 35, 2, 3, 90), id="all + translation"),
        pytest.param(ALL_TRANSFORMS, SCALING, Transform(10, 15, 4, 9, 90), id="all + scale"),
        pytest.param(ALL_TRANSFORMS, ROTATION_90, Transform(10, 15, 2, 3, 180), id="all + rotation"),
        pytest.param(ALL_TRANSFORMS, ALL_TRANSFORMS, Transform(-35, 35, 4, 9, 180), id="all + all"),
    ],
)
def test_combining_simple_transforms(t1: Transform, t2: Transform, expected: Transform) -> None:
    result = t1 + t2
    assert expected == result


@pytest.mark.parametrize(
    "t1, t2, expected",
    [
        pytest.param(
            Transform(0, 0, rotation=30),
            Transform(0.5, math.sqrt(3) / 2),
            Transform(0, 1, rotation=30),
            id="trans (0, 0), rot 30 + line in 60º",
        ),
        pytest.param(
            Transform(1, 0, rotation=30),
            Transform(0.5, math.sqrt(3) / 2),
            Transform(1, 1, rotation=30),
            id="trans (1, 0), rot 30 + line in 60º",
        ),
        pytest.param(
            ROTATION_30 + Transform(1),
            ROTATION_30 + Transform(1),
            Transform(0.5 + math.sqrt(3) / 2, 0.5 + math.sqrt(3) / 2, rotation=60),
            id="rot 30, trans (1, 0), rot 30, trans (1,0)",
        ),
    ],
)
def test_combining_transforms_with_rotation(t1: Transform, t2: Transform, expected: Transform) -> None:
    result = t1 + t2
    assert expected == result
