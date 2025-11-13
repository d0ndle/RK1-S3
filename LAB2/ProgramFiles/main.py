import rectangle
import circle
import square_figure
from art import art,tprint
if __name__ == '__main__':
    rectangle = rectangle.Rectangle(12,12,"Синий")
    circle = circle.Circle("Зеленый",12)
    square_figure = square_figure.Square(12,"Красный")

    print(rectangle)
    print(circle)
    print(square_figure)
    print("\n\n\n\n\n")
    print(art("cat"))
    tprint("HELLO")