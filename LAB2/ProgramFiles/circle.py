from geometric_shape import Shape
from shape_color import ShapeColor
import math as m

class Circle(Shape):
    def __init__(self, color, radius):
        self.name = "Круг"
        self.color = ShapeColor(color)
        self.radius = radius
    def calculate_square(self):
        square = self.radius*m.pi
        return square
    def __repr__(self):
        return "Фигура: {}\nРадиус: {}\nЦвет: {}\nПлощадь: {}\n".format(self.name,
                                                                                    self.radius,
                                                                                    self.color.color,
                                                                                    self.calculate_square())