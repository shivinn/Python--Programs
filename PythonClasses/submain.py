import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):   # Operator Overloading
        if isinstance(other, Point):
            x = self.x + other.x    # Here, other is a referential object to other point
            y = self.y + other.y
            return Point(x, y)
        else:
            x = self.x + other
            y = self.y + other
            return Point(x, y)

    def plot(self):
        plt.scatter(self.x, self.y)


# a = Point(3, 4)
# a.plot()
# plt.show()

a = Point(1, 1)
b = Point(2, 2)
c = a + b

d = a + 5
e = a + Point(1, 1)
print(e.x, e.y)
print(d.x, d.y)
print(c.x, c.y)