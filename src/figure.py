from abc import ABC, abstractmethod


class Figure(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        raise ValueError('Argument figure must be rectagle or child class')
