# try-except: handle exceptions gracefully
def divide(dividend , divisor):
    try:  # Try to execute this code
        print(dividend / divisor)
    except ZeroDivisionError:  # Catch specific exception type
        print('You can not divide by 0')

divide(dividend=10, divisor=5)

# Handle multiple exceptions in one except block
def divide(dividend , divisor):
    try:
        if (dividend == 10):
          var = 'str' + 1  # This will raise TypeError
        else:
          print(dividend / divisor)
    except (ZeroDivisionError, TypeError) as error:  # Catch multiple exception types
        print(error)  # Print the error message

divide(dividend='nikki', divisor=2)

# finally block: always executes regardless of exceptions
def divide(dividend , divisor):
    try:
        print(dividend / divisor)
    except ZeroDivisionError:
        print('You can not divide by 0')
    finally:  # Always executes, even if exception occurs
        print('Execution finished')

divide(dividend=10, divisor=0)

