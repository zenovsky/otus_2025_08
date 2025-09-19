import pytest

from rectangle import Rectangle
from square import Square


@pytest.mark.parametrize(
    "figure_1, expected_area",
    [
        pytest.param(Square(6), 36, id="Square area")
    ]
)
def test_square_area(figure_1, expected_area):
    assert figure_1.area == expected_area, f"{figure_1} must be {expected_area}"

@pytest.mark.parametrize(
    "figure_1, expected_perimeter",
    [
        pytest.param(Square(6), 18, id="Square perimeter")
    ]
)
def test_square_perimeter(figure_1, expected_perimeter):
    assert figure_1.perimeter == expected_perimeter, f"{figure_1} must be {expected_perimeter}"

@pytest.mark.parametrize(
    "figure_1, figure_2, expected_area",
    [
        pytest.param(Square(6), Rectangle(5, 10), 86, id="Square and other figure"),
        pytest.param(Square(6), Square(10), 136, id="Square and other square"),
        pytest.param(Square(6), Square(6), 72, id="Square and same figure")
    ]
)
def test_add_area(figure_1, figure_2, expected_area):
    assert figure_1.add_area(figure_2) == expected_area, f"Sum of areas should be {expected_area}"

@pytest.mark.parametrize(
    "side_a",
    [
        pytest.param(-1, id="negative side"),
        pytest.param(0, id="zero side"),
    ]
)
def test_square_invalid_sides(side_a):
    with pytest.raises(ValueError):
        Square(side_a)

@pytest.mark.skip(reason="known bug https://jira.com/BUG-0003")
def test_square_cannot_be_rectagle():
    with pytest.raises(ValueError):
        Square(4, 8)

@pytest.mark.skip(reason="known bug https://jira.com/BUG-0004")
def test_square_cannot_be_triangle():
    with pytest.raises(ValueError):
        Square(4, 4, 4)
