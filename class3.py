#  Write a Circle class with a radius attribute.
# Add two methods:

# area() → returns area of the circle

# circumference() → returns circumference of the circle

# (Formula: area = π × r², circumference = 2 × π × r)

import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    
    def area(self):
        return math.pi * self.radius * self.radius  
    def circumference(self):
        return 2 * math.pi * self.radius
    
    
c1 = Circle(36)
c2 = Circle(4)

print("Circle 1 - Radius 36")
print("Area:", c1.area())
print("Circumference:", c1.circumference())

print("\nCircle 2 - Radius 4")
print("Area:", c2.area())
print("Circumference:", c2.circumference())

# OR


import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    
    def area(self):
        print(f"area is : {math.pi * self.radius * self.radius}")  
    def circumference(self):
        print(f"Circumference is {2 * math.pi * self.radius}")

    
    
c1 = Circle(36)
c2 = Circle(4)

c1.area()
c1.circumference()
c2.area()
c2.circumference() 
