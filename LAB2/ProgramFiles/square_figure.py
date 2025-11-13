from rectangle import Rectangle
from shape_color import ShapeColor


class Square(Rectangle):
    def __init__(self, width,color):
        self.name = "Квадрат"
        self.width = width
        self.color = ShapeColor(color)
    def calculate_square(self):
        square = self.width ** 2
        return square
    def __repr__(self):
        return "Фигура: {}\nШирина: {}\nЦвет: {}\nПлощадь: {}\n".format(self.name,
                                                                                    self.width,
                                                                                    self.color.color,
                                                                                    self.calculate_square())
