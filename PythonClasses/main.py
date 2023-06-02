"""
Object-oriented Programming (classes) by Keith Galli
Code should be:

1. Easy to Understand
2. Safe from Bugs
3. Ready for Change
"""

import turtle


class Polygon:
    def __init__(self, sides, name, size=100, color="black", thick=3):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.thick = thick
        # maths formulas for interior angles
        self.interior_angles = (self.sides - 2) * 180
        self.angle = self.interior_angles / self.sides

    # class method
    def draw(self):
        turtle.pensize(self.thick)
        turtle.color(self.color)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)
        # turtle.done()


# square = Polygon(4, "Square")
# pentagon = Polygon(5, "Pentagon")
# hexagon = Polygon(6, "Hexagon", 150, color="red")
#
# print(square.sides)
# print(square.sides)
# print(square.interior_angles)
# print(square.angle)
#
# # square.draw()
# # pentagon.draw()
# hexagon.draw()


# Inheritance - Subclassing
class Square(Polygon):
    def __init__(self, size=100, color="black", thick=3):
        super().__init__(4, "Square", size, color, thick)

    def draw(self): # overwriting the draw() method
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()


square = Square(color="#111aca", size=200)
print(square.sides)
print(square.angle)

print(square.draw())

turtle.done()




















