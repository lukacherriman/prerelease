class Vectors:
    def __init__(self, x_value, y_value):
        self.x_value = x_value
        self.y_value = y_value

    def magnitude(self):
        magnitude = (self.x_value**2 + self.y_value**2)**(1/2)
        return magnitude

    def __add__(self, other):
        new_vector = Vectors(self.x_value + other.x_value , self.y_value + other.y_value)
        return new_vector

    def __sub__(self, other):
        new_vector = Vectors(self.x_value - other.x_value , self.y_value - other.y_value)
        return new_vector

    def get_x(self):
        return self.x_value

    def get_y(self):
        return self.y_value


a = Vectors(10, 5)
b = Vectors(7, 9)
c = a + b
d = a - b

print(c.get_x(), c.get_y())
print(d.get_x(), d.get_y())
