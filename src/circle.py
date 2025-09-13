import math

from figure import Figure


class Circle(Figure):

    def __init__(self, radius: int):
        if radius <= 0:
            raise ValueError(f"circle should have radius greater than 0, actual {radius}")
        self.radius = radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * self.radius ** 2
