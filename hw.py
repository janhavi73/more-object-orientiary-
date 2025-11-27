import math

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


user_radius = float(input("Enter the radius of the circle: "))

my_circle = circle(user_radius)
print(f"Area: {my_circle.area():.2f}")

