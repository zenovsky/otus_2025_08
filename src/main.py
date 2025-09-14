from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle


def main():
    # Прямоугольник
    rect = Rectangle(5, 10)
    print("Rectangle:")
    print("  sides:", rect.side_a, rect.side_b)
    print("  perimeter:", rect.perimeter)
    print("  area:", rect.area)
    print(rect.add_area(rect))

    # Треугольник
    tri = Triangle(4, 4, 4)
    print("Triangle:")
    print("  sides:", tri.side_a, tri.side_b, tri.side_c)
    print("  perimeter:", tri.perimeter)
    print("  area:", tri.area)
    print(tri.add_area(tri))

    # Круг
    circ = Circle(7)
    circ2 = Circle(7)
    print("Circle:")
    print("  radius:", circ.radius)
    print("  perimeter:", circ.perimeter)
    print("  area:", circ.area)
    print(circ2.add_area(circ))

    # Квадрат
    sq = Square(6)
    sq1 = Square(6)
    #rect = Rectangle(5, 10)
    print("Square:")
    print("  side:", sq.side_a)
    print("  perimeter:", sq.perimeter)
    print("  area:", sq.area)
    print(sq.add_area(sq1))


if __name__ == "__main__":
    main()
