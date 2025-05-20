import math

import turtle

class Circle:
    def __init__(self, radius):
        self.radius = radius
        # self.area = self.circle_area(radius)  # Older solution. Made "@property instead"

    @property
    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2
    
    def __str__(self):
        return f'Radius = {self.radius}, Area = {self.circle_area(self.radius)}'

    def __repr__(self):
        return f'Radius = {self.radius}, Area = {self.circle_area(self.radius)}'
    
    # Old versin:
    # def __add__(self, other):
    #     new_circle = Circle(other.radius)
    #     new_circle.radius = self.radius + other.radius
    #     return new_circle
    
    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __eq__(self, other):
        return self.radius == other.radius
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius
    
    @staticmethod
    def list_circles(*args):
        rounds_list = []
        for arg in args:
            rounds_list.append(arg)
        rounds_list = sorted(rounds_list)
        return rounds_list
    
    def draw(self):
        screen = turtle.getscreen()
        circle_image = turtle.Turtle()
        circle_image.circle(self.radius)
        turtle.done()


c_1 = Circle(5)
c_2 = Circle(10)
print(repr(c_1))
print(repr(c_2))
print(c_1)

c_3 = c_1 + c_2
print(repr(c_3))

print('=' * 50)

print(c_1 == c_2)
print(c_1 == c_1)

print('=' * 50)

print(c_1 < c_2)
print(c_3 < c_2)

print('=' * 50)

print(c_1 > c_2)
print(c_3 > c_2)

print('=' * 50)

sorted_circles = Circle.list_circles(c_1, c_2, c_3)
print(sorted_circles)
sorted_circles = Circle.list_circles(c_3, c_2, c_1)
print(sorted_circles)

print('=' * 50)

c_1.draw()

