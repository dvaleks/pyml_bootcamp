#!/bin/env python3.9

'''
Задание:
Разработать класс Shape для математического описания плоских фигур:
круга, квадрата и равностороннего треугольника. Каждая из геометрических

фигур должна представляться своим классом (Circle, Square, Triangle), кото-
рый наследуется от Shape.

Конструктор класса (Circle, Square, Triangle) должен принимать два зна-
чения: геометрический центр плоской фигуры и радиус (сторона фигуры).

Геометрический центр должен быть атрибутом класса Shape (по умолчанию
– начало координат 0; 0), а радиус (сторона) – атрибуты дочерних классов
(по умолчанию 1).
В дочерних классах предусмотреть наличие следующих методов:
– get_center() – возвращает геометрический центр фигуры;

– get_vertex() – возвращает вершины фигуры (для квадрата и треуголь-
ника);

– get_area() – возвращает площадь фигуры;
– move(x, y) – перемещает геометрический центр фигуры в точку (x, y).
В базовом классе предусмотреть метод get_distance(figure_1, figure_2),

вычисляющий расстояние между фигурами figure_1 и figure_2 (геометриче-
скими центрами).

Положение фигуры рассматривать в декартовой системе координат (см.

рисунок), поворот фигур относительно геометрического центра не прини-
мать во внимание (см. рисунок).

Произвести демонстрацию всех возможностей классов на примерах.
'''
import math
from typing import Tuple, List


class Shape:

    def __init__(self, center: Tuple[float, float], radius: float):
        self.center = center
        self.radius = radius

    def get_center(self) -> Tuple[float, float]:
        return self.center

    def get_vertex(self) -> List[Tuple[float, float]]:
        raise NotImplementedError()

    def get_area(self) -> float:
        raise NotImplementedError()

    def move(self, x: float, y: float):
        x = self.center[0] + x
        y = self.center[1] + y
        self.center = (x, y)

    @staticmethod
    def get_distance(figure_1: 'Shape', figure_2: 'Shape') -> float:
        a = abs(figure_1.center[0] - figure_2.center[0])
        b = abs(figure_1.center[1] - figure_2.center[1])
        return math.sqrt(math.pow(a, 2) + math.pow(b, 2))


class IrrelevantMethodException(Exception):
    def __str__(self):
        return 'Method is irrelevant for this Shape'


class Circle(Shape):
    pi = 3.14159265359

    def get_vertex(self):
        raise IrrelevantMethodException()

    def get_area(self):
        return self.pi * self.radius * self.radius


class Square(Shape):

    def get_vertex(self):
        x, y = self.center
        half_side = self.radius / 2
        upper_left = (x - half_side, y + half_side)
        upper_right = (x + half_side, y + half_side)
        bottom_right = (x + half_side, y - half_side)
        bottom_left = (x - half_side, y - half_side)
        return [upper_left, upper_right, bottom_right, bottom_left]

    def get_area(self):
        return self.radius * self.radius


class Triangle(Shape):

    def get_vertex(self):
        x, y = self.center
        side = self.radius
        R = (side * math.sqrt(3)) / 3
        r = R / 2
        bottom_left = (x - side / 2, y - r)
        center_top = (x, y + R)
        bottom_right = (x + side / 2, y - r)
        return [bottom_left, center_top, bottom_right]

    def get_area(self):
        return (math.pow(self.radius, 2) * math.sqrt(3)) / 4


def main():
    circle_center = (5, 5)
    circle_radius = 4
    c = Circle(circle_center, 4)
    assert c.get_center() == circle_center
    assert c.get_area() == Circle.pi * math.pow(circle_radius, 2)
    print(f'Spawned circle at {circle_center} and radius {circle_radius}')
    print(f'Circle area: {c.get_area()}')
    print('-' * 8)

    square_center = (8, 7)
    square_radius = 4
    s = Square((0, 0), square_radius)
    print(f'Spawned square at (0, 0) with side {square_radius}')
    s.move(*square_center)
    print(f'Moved square to {square_center}')
    assert s.get_center() == square_center
    s_area = s.get_area()
    print(f'Square area: {s_area}')
    assert s_area == math.pow(square_radius, 2)
    distance = Shape.get_distance(c, s)
    print(f'Square vertex: {s.get_vertex()}')
    print(f'Distance between circle{circle_center} and square{square_center}: {distance}')
    print('-' * 8)

    triangle_center = (11, 5)
    triangle_radius = 4.2
    t = Triangle(triangle_center, triangle_radius)
    assert t.get_center() == triangle_center
    print(f'Spawned triangle at {triangle_center} with side {triangle_radius}')
    print(f'Triangle area: {t.get_area()}')
    print(f'Triangle vertex: {t.get_vertex()}')
    print(f'Distance between circle{circle_center} and triangle{triangle_center}: {Shape.get_distance(c, t)}')


if __name__ == '__main__':
    main()
