#Inheritance promotes code reuse and allows you to create a hierarchy of classes that
# share common attributes and methods. It helps in creating clean and organized code by
# keeping related functionality in one place and promoting the concept of modularity.
# The base class from which a new class is derived is also known as a parent class,
# and the new class is known as the child class or subclass.

# Define a class named Animal
class Animal:

    # Constructor method that initializes the class object with a name attribute
    def __init__(self, name):
        self.name = name

    # Method that is defined in the Animal class but does not have a body
    # This method will be overridden in the subclasses of Animal
    def speak(self):
        print("Animal sounds")

# Define a subclass named Dog that inherits from the Animal class
class Dog(Animal):

    # Override the speak method of the Animal class
    def speak(self):
        super().speak() #Call parent method
        print("Woof!")

# Define a subclass named Cat that inherits from the Animal class
class Cat(Animal):

    # Override the speak method of the Animal class
    def speak(self):
        print("Meow!")

# Create a Dog object with a name attribute "Rover"
dog = Dog("Rover")
print(dog.name)

# Create a Cat object with a name attribute "Whiskers"
cat = Cat("Whiskers")
print(cat.name)


# Call the speak method of the Dog class and print the output
# The speak method of the Dog class overrides the speak method of the Animal class
# Therefore, when we call the speak method of the Dog object, it will print "Woof!"
dog.speak()   # output: Woof!

# Call the speak method of the Cat class and print the output
# The speak method of the Cat class overrides the speak method of the Animal class
# Therefore, when we call the speak method of the Cat object, it will print "Meow!"
cat.speak()   # output: Meow!
