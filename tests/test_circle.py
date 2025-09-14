import pytest

from circle import Circle
from triangle import Triangle


def test_circle_area(circle_integer):
    radius = circle_integer
    c = Circle(radius)
    assert c.area == 153.93804002589985, f"Circle area with radius {radius} must be 153.93804002589985"

def test_circle_perimeter(circle_integer):
    radius = circle_integer
    c = Circle(radius)
    assert c.perimeter == 43.982297150257104, f"Circle perimeter with radius {radius} must be 43.982297150257104"

def test_circle_add_area_with_another_figure(circle_integer):
    radius = circle_integer
    c = Circle(radius)
    t = Triangle(3, 4, 5)
    assert t.add_area(c) == 159.93804002589985, f"Circle perimeter with radius {radius} must be 159.93804002589985"

def test_circle_add_area_with_another_circle(circle_integer):
    c1 = Circle(circle_integer)
    c2 = Circle(5)
    assert c1.add_area(c2) == 232.4778563656447, "Sum of radius should be 232.4778563656447"

def test_circle_add_area_with_same_circle(circle_integer):
    c1 = Circle(circle_integer)
    c2 = Circle(circle_integer)
    assert c1.add_area(c2) == 307.8760800517997, "Sum of radius should be 307.8760800517997"


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
