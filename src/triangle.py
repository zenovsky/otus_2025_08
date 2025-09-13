from figure import Figure


class Triangle(Figure):

    def __init__(self, side_a: int, side_b: int, side_c: int):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError(f'triangle should have sides great than 0, actual {side_a}, {side_b}, {side_c}')

        if (side_a + side_b <= side_c or
            side_a + side_c <= side_b or
            side_b + side_c <= side_a):
            raise ValueError(f'sides {side_a}, {side_b}, {side_c} do not form a triangle')

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        s = self.perimeter / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5

