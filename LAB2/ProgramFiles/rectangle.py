from geometric_shape import Shape
from shape_color import ShapeColor
class Rectangle(Shape):
    def __init__(self, width, height, color):
        self.name = "Прямоугольник"
        self.width = width
        self.height = height
        self.color = ShapeColor(color)
    def calculate_square(self):
        square = self.width*self.height
        return square
    def __repr__(self):
        return "Фигура: {}\nВысота: {}\nШирина: {}\nЦвет: {}\nПлощадь: {}\n".format(self.name,
                                                                                    self.height,
                                                                                    self.width,
                                                                                    self.color.color,
                                                                                    self.calculate_square())

