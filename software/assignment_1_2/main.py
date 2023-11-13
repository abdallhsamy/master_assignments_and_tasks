import math

def calculate_circle_area(radius):
    return math.pi * radius**2

radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"The area of the circle is: {area}")