# Custom exception: create by inheriting from Exception class

class MyCustomException(Exception):
    pass

try:
    raise MyCustomException('A custom message for my custom exception')
except MyCustomException:
    print('My custom exception was raised')
