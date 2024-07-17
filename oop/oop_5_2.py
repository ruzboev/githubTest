class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def area(self):
        return self.height * self.width

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        return NotImplemented


rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 6)

print(f"Rect1 yuza: {rect1.area}")
print(f"Rect2 yuza: {rect2.area}")
print(f"Rect1 == Rect2: {rect1 == rect2}")
