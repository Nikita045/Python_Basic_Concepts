#classes are user defined blueprint or prototype
#methods, class variables, instance variables, constructor, etc.
#functions inside a class are called methods

class Calculator:
    num=100 #class variable
    def getData(self):
        print("I'm not executing as a method in class")
#default constructor
    def __init__(self,a,b):
        self.firstno=a
        self.secondno=b
        print("I'm a default constructor which is called automatically when object is created")
    def summation(self):
        return self.firstno+self.secondno+self.num+Calculator.num
#call method and variables of a class using object
obj=Calculator(2,3)
print(obj.summation())
obj.getData()

obj1=Calculator(4,5)
print(obj1.summation())