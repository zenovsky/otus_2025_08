from rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_a: int):
        if side_a <= 0:
            raise ValueError(f'square should have side great than 0, actual {side_a}')

        super().__init__(side_a, side_a)
