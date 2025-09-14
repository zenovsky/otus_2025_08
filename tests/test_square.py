import pytest

from rectangle import Rectangle
from square import Square


def test_square_area(square_integer):
    side_a = square_integer
    s = Square(side_a)
    assert s.area == 36, f"Square area with side {side_a} must be 36"

def test_square_perimeter(square_integer):
    side_a = square_integer
    s = Square(side_a)
    assert s.perimeter == 18, f"Square with side {side_a} must be 18"

def test_square_add_area_with_another_figure(square_integer):
    side_a = square_integer
    s = Square(side_a)
    r = Rectangle(5, 10)
    assert r.add_area(s) == 86, "Sum of areas should be 86"

def test_square_add_area_with_another_square(square_integer):
    side_a = square_integer
    s1 = Square(side_a)
    s2 = Square(10)
    assert s1.add_area(s2) == 136, "Sum of areas should be 136"

def test_square_add_area_with_same_square(square_integer):
    side_a = square_integer
    s1 = Square(side_a)
    s2 = Square(side_a)
    assert s1.add_area(s2) == 72, "Sum of areas should be 72"

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
