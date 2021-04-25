from math import pi


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, x):
        self.radius = x / 2

    @property
    def area(self):
        return self.radius ** 2 * pi

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, x):
        if x < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self.__radius = x

