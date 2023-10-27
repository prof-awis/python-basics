from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        area = 22 / 7 * self.radius ** 2
        print(f"Area is {area}")

    def calc_circumference(self):
        circum = pi * self.radius * 2
        print(f"Circumference is {circum}")


c1 = Circle(7)
c2 = Circle(14)

c1.calc_circumference()
c1.calc_area()
