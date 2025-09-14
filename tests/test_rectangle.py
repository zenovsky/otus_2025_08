import pytest

from rectangle import Rectangle
from square import Square


def test_rectangle_area(rectangle_integer):
    side_a, side_b = rectangle_integer
    r = Rectangle(side_a, side_b)
    assert r.area == 50, f"Rectangle area with sides {side_a} and {side_b} must be 50"

def test_rectangle_perimeter(rectangle_integer):
    side_a, side_b = rectangle_integer
    r = Rectangle(side_a, side_b)
    assert r.perimeter == 25, f"Perimeter with sides {side_a} and {side_b} must be 25"

def test_rectangle_add_area_with_another_figure(rectangle_integer):
    side_a, side_b = rectangle_integer
    s = Square(6)
    r = Rectangle(side_a, side_b)
    assert s.add_area(r) == 86, "Sum of areas should be 86"

def test_rectangle_add_area_with_another_rectangle(rectangle_integer):
    side_a, side_b = rectangle_integer
    r1 = Rectangle(side_a, side_b)
    r2 = Rectangle(2, 3)
    assert r1.add_area(r2) == 56, "Sum of areas should be 56"

def test_rectangle_add_area_with_same_rectangle(rectangle_integer):
    side_a, side_b = rectangle_integer
    r1 = Rectangle(side_a, side_b)
    r2 = Rectangle(side_a, side_b)
    assert r1.add_area(r2) == 100, "Sum of areas should be 100"

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
