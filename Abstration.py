#Abstraction  focus on the essential features of an object or system while ignoring the
# details that aren’t relevant to the current context. By reducing complexity and hiding
# unnecessary details, abstraction can make code more modular, easier to read, and easier to maintain.
#abstraction can be achieved by using abstract classes or interfaces.
#abstract class -  It often includes abstract methods that have no implementation, but provide a template for how the subclass should be implemented.
#interface - is a collection of method signatures that a class must implement in order to be considered
# “compatible” with the interface. Interfaces are often used to define a common set of methods
# that multiple classes can implement, allowing them to be used interchangeably in certain contexts.

# Import the abc (abstract base class) module to define abstract classes and methods
from abc import ABC, abstractmethod

# Define an abstract class called Shape that has an abstract method called area
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Define a Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implement the area method for Rectangles
    def area(self):
        return self.width * self.height

# Define a Circle class that also inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implement the area method for Circles
    def area(self):
        return 3.14 * self.radius ** 2

# Create a list of shapes that includes both Rectangles and Circles
shapes = [Rectangle(4, 5), Circle(7)]

# Loop through each shape in the list and print its area
for shape in shapes:
    print(shape.area())

