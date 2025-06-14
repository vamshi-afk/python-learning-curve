# Implement the following classes to understand abstraction in Python :

# Class Name: Shape (Abstract Class)
# Attributes: color (String)
# Constructor: Shape(c) -> assign value of c to color attribute
# Methods: get_color() -> returns value of color
#          get_area() -> abstract method with float return type
         
# Class Name: Square (extends Shape)
# Attributes: side (float)
# Constructor: Square(c, side) -> calls super(c) to initialize the color and assigns the value to side.
# Methods: get_area() -> returns the area of the square (side * side). 

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color =  color
    
    def get_color(self):
        return self.color
    
    @abstractmethod
    def get_area(self):
        pass
    
class Square(Shape):
    
    def __init__(self, color, side):
        super().__init__(color)
        self.side=side
    
    def get_area(self):
        return self.side*self.side

s= Square("red", 4)
print(s.get_color())
print(s.get_area())