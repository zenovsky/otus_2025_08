import pytest

from rectangle import Rectangle
from square import Square


@pytest.mark.parametrize(
    "figure_1, expected_area",
    [
        pytest.param(Rectangle(10, 5), 50, id="Rectangle area")
    ]
)
def test_rectangle_area(figure_1, expected_area):
    assert figure_1.area == expected_area, f"{figure_1} must be {expected_area}"

@pytest.mark.parametrize(
    "figure_1, expected_perimeter",
    [
        pytest.param(Rectangle(10, 5), 20, id="Rectangle perimeter")
    ]
)
def test_rectangle_perimeter(figure_1, expected_perimeter):
    assert figure_1.perimeter == expected_perimeter, f"{figure_1} must be {expected_perimeter}"

@pytest.mark.parametrize(
    "figure_1, figure_2, expected_area",
    [
        pytest.param(Rectangle(10, 5), Rectangle(2, 3), 56, id="Rectangle and other rectangle"),
        pytest.param(Rectangle(10, 5), Rectangle(10, 5), 100, id="Rectangle and same rectangle"),
        pytest.param(Square(6), Rectangle(10, 5), 86, id="Rectangle and other figure")
    ]
)
def test_add_area(figure_1, figure_2, expected_area):
    assert figure_1.add_area(figure_2) == expected_area, f"Sum of areas should be {expected_area}"

@pytest.mark.parametrize(
    "side_a, side_b",
    [
        pytest.param(-1, 4, id="negative sides"),
        pytest.param(8, 0, id="negative sides with zero"),
        pytest.param(-4, -1, id="negative minor sides"),
        pytest.param(0, 0, id="negative zero sides")
    ]
)
def test_rectangle_invalid_sides(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)

@pytest.mark.skip(reason="known bug https://jira.com/BUG-0001")
def test_rectangle_cannot_be_square():
    with pytest.raises(ValueError):
        Rectangle(4, 4)

@pytest.mark.skip(reason="known bug https://jira.com/BUG-0002")
def test_rectangle_cannot_be_triangle():
    with pytest.raises(ValueError):
        Rectangle(4, 4, 8)
