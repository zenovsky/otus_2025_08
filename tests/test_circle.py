import pytest

from circle import Circle
from triangle import Triangle


@pytest.mark.parametrize(
    "figure_1, expected_area",
    [
        pytest.param(Circle(7), 153.94, id="Circle area")
    ]
)
def test_circle_area(figure_1, expected_area):
    assert round (figure_1.area, 2) == expected_area, f"Circle with radius {figure_1} must be {expected_area}"

@pytest.mark.parametrize(
    "figure_1, expected_perimeter",
    [
        pytest.param(Circle(7), 43.98, id="Circle perimeter")
    ]
)
def test_circle_perimeter(figure_1, expected_perimeter):
    assert round(figure_1.perimeter, 2) == expected_perimeter, f"Circle perimeter {figure_1} must {expected_perimeter}"

@pytest.mark.parametrize(
    "figure_1, figure_2, expected_area",
    [
        pytest.param(Circle(7), Triangle(3, 4, 5), 159.94, id="Circle and other figure"),
        pytest.param(Circle(7), Circle(5), 232.48, id="Circle and other square"),
        pytest.param(Circle(7), Circle(7), 307.88, id="Circle and same figure")
    ]
)
def test_add_area(figure_1, figure_2, expected_area):
    assert round (figure_1.add_area(figure_2), 2) == expected_area, f"Sum of areas should be {expected_area}"

@pytest.mark.parametrize(
    "radius",
    [
        pytest.param(-1, id="negative radius"),
        pytest.param(0, id="zero radius"),
    ],
)
def test_circle_invalid_radius(radius):
    with pytest.raises(ValueError):
        Circle(radius)
