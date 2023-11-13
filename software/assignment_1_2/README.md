## Assignment 1_2

### Question 

Apply Software Maintenance (Categories of Activities) on your own simple python  program (you can use any programming language)

### Answer

Software maintenance involves several activities such as bug fixing, enhancing existing features, optimizing code, and updating documentation. Let's consider a simple Python program and run through these activities.

Imagine we have a basic program that calculates the area of a circle:

```python
import math

def calculate_circle_area(radius):
    return math.pi * radius**2

radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"The area of the circle is: {area}")
```

Now, let's break down how we might apply software maintenance activities:

1- **Bug Fixing**: Imagine a bug where entering a negative radius crashes the program. We can fix this by adding a validation check.

```python
def calculate_circle_area(radius):
    if radius < 0:
        return "Invalid input: Radius cannot be negative"
    else:
        return math.pi * radius**2
```

2- **Enhancements**: Let's enhance this by allowing the user to choose between calculating the area or circumference of the circle.

```python
def calculate_circle_circumference(radius):
    return 2 * math.pi * radius

choice = input("Calculate area (A) or circumference (C) of the circle? ").upper()
if choice == 'A':
    area = calculate_circle_area(radius)
    print(f"The area of the circle is: {area}")
elif choice == 'C':
    circumference = calculate_circle_circumference(radius)
    print(f"The circumference of the circle is: {circumference}")
else:
    print("Invalid choice. Please enter 'A' for area or 'C' for circumference.")
```

3- **Optimizing Code**: We could optimize this by reducing repetitive code.

```python
def calculate_circle_properties(radius, property='area'):
    if radius < 0:
        return "Invalid input: Radius cannot be negative"
    if property == 'area':
        return math.pi * radius**2
    elif property == 'circumference':
        return 2 * math.pi * radius
    else:
        return "Invalid property. Please choose 'area' or 'circumference'."

choice = input("Calculate area (A) or circumference (C) of the circle? ").upper()
if choice == 'A':
    result = calculate_circle_properties(radius, 'area')
    print(f"The area of the circle is: {result}")
elif choice == 'C':
    result = calculate_circle_properties(radius, 'circumference')
    print(f"The circumference of the circle is: {result}")
else:
    print("Invalid choice. Please enter 'A' for area or 'C' for circumference.")
```
4- **Updating Documentation**: Finally, updating comments or docstrings to reflect changes made and add any necessary information for future maintenance.

By implementing these steps, we've performed software maintenance on the simple Python program, improving its functionality and readability while addressing potential issues.