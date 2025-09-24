import pytest

from rectangle import Rectangle
from triangle import Triangle


@pytest.mark.parametrize(
    "figure_1, expected_area",
    [
        pytest.param(Triangle(4,4,4), 6.93, id="Triangle area")
    ]
)
def test_triangle_area(figure_1, expected_area):
    assert round (figure_1.area, 2) == expected_area, f"{figure_1} must be {expected_area}"

@pytest.mark.parametrize(
    "figure_1, expected_perimeter",
    [
        pytest.param(Triangle(4,4,4), 12, id="Triangle area")
    ]
)
def test_triangle_perimeter(figure_1, expected_perimeter):
    assert figure_1.perimeter == expected_perimeter, f"{figure_1} must be {expected_perimeter}"

@pytest.mark.parametrize(
    "figure_1, figure_2, expected_area",
    [
        pytest.param(Triangle(4,4,4), Rectangle(2, 6), 18.93, id="Triangle and other figure"),
        pytest.param(Triangle(4,4,4), Triangle(3,4,5), 12.93, id="Triangle and other triangle"),
        pytest.param(Triangle(4,4,4), Triangle(4,4,4), 13.86, id="Triangle and same figure")
    ]
)
def test_add_area(figure_1, figure_2, expected_area):
    assert round (figure_1.add_area(figure_2), 2) == expected_area, f"Sum of areas should be {expected_area}"

@pytest.mark.parametrize(
    "a, b, c",
    [
        pytest.param(-1, 2, 3, id="negative side"),
        pytest.param(0, 4, 5, id="with zero side"),
        pytest.param(0, 0, 0, id="zero side")
    ],
)
def test_triangle_invalid_sides(a, b, c):
    """Проверяем, что нельзя создать треугольник с некорректными сторонами."""
    with pytest.raises(ValueError):
        Triangle(a, b, c)


@pytest.mark.parametrize(
    "a, b, c",
    [
        pytest.param(1, 2, 3, id="sum of two sides equals third"),
        pytest.param(2, 3, 10, id="sum of two sides less than third"),
    ],
)
def test_triangle_impossible(a, b, c):
    """Проверяем, что нельзя создать треугольник, нарушающий неравенство треугольника."""
    with pytest.raises(ValueError):
        Triangle(a, b, c)

@pytest.mark.skip(reason="known bug https://jira.com/BUG-0005")
def test_triangle_cannot_be_rectagle():
    with pytest.raises(ValueError):
        Triangle(4, 8)

@pytest.mark.skip(reason="known bug https://jira.com/BUG-0006")
def test_triangle_cannot_be_square():
    with pytest.raises(ValueError):
        Triangle(4, 4)
