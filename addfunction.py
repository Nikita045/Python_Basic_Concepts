
Var1="Nikita"

def add(a,b):
    print(f'Adding {a} and {b} = {a+b}')

add(10,20)

def add_test(a,b):
    return a+b

def modify_var():
    global Var1
    Var1 = "Hello"
    return Var1
print(modify_var())
print(Var1)
result=add_test(30,20)
print("Addition of a & b",result)

# Lambda function: anonymous function defined in one line
# Syntax: lambda arguments: expression
add = lambda x, y: x + y
print(add(5, 3))

def test(n):
    return lambda x:x+n

adding=test(5)
print(adding(10))

