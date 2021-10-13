class rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_area(self):
        area = self._width*self._height
        return area

    def get_perimeter(self):
        perimeter = 2*self._width + 2*self._height
        return perimeter

    def get_diagonal(self):
        diagonal = (self._width**2 + self._height**2)**(1/2)
        return diagonal


rect1 = rectangle(20, 50)
rect2 = rectangle(30, 40)
square1 = rectangle(50,50)

print(f"rect1 area is {rect1.get_area()}")
print(f"rect2 permimeter is {rect2.get_perimeter()}")
print(f"square1 diagonal length is {square1.get_diagonal()}")

