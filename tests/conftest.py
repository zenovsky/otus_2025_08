import pytest


@pytest.fixture
def rectangle_integer():
    side_a = 5
    side_b = 10

    yield side_a, side_b

@pytest.fixture
def square_integer():
    side_a = 6

    yield side_a

@pytest.fixture
def triangle_integer():
    side_a = 4
    side_b = 4
    side_c = 4

    yield side_a, side_b, side_c

@pytest.fixture
def circle_integer():
    radius = 7

    yield radius
