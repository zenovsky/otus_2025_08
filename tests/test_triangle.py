import pytest

from rectangle import Rectangle
from triangle import Triangle


def test_triangle_area(triangle_integer):
    side_a, side_b, side_c = triangle_integer
    t = Triangle(side_a, side_b, side_c)
    assert t.area == 6.928203230275509, f"Area with sides {side_a}, {side_b} and {side_c} must be 6.928203230275509"

def test_triangle_perimeter(triangle_integer):
    side_a, side_b, side_c = triangle_integer
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == 12, f"Triangle perimeter with sides {side_a}, {side_b} and {side_c} must be 12"

def test_triangle_add_area_with_another_figure(triangle_integer):
    side_a, side_b, side_c = triangle_integer
    t = Triangle(side_a, side_b, side_c)
    r = Rectangle(2, 6)
    assert r.add_area(t) == 18.928203230275507, "Sum of areas should be 18.928203230275507"

def test_triangle_add_area_with_another_triangle(triangle_integer):
    side_a, side_b, side_c = triangle_integer
    t1 = Triangle(side_a, side_b, side_c)
    t2 = Triangle(3, 4, 5)
    assert t2.add_area(t1) == 12.928203230275509, "Sum of areas should be 12.928203230275509"

def test_triangle_add_area_with_same_triangle(triangle_integer):
    side_a, side_b, side_c = triangle_integer
    t1 = Triangle(side_a, side_b, side_c)
    t2 = Triangle(side_a, side_b, side_c)
    assert t1.add_area(t2) == 13.856406460551018, "Sum of areas should be 13.856406460551018"


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
