# Define a function that accepts any number of positional and keyword arguments
def some_function(*args, **kwargs):
    return sum(args)

# Call with any number of positional arguments
print(some_function(2, 4, 6))
print(some_function(2,8,7.8, 4, 6,3.14))
# *args collects positional arguments into a tuple
def test_func_multiple_args(*args):
    print(f'Arguments passed: {args} as {type(args)}')

# Pass multiple arguments - they'll be collected into args tuple
test_func_multiple_args('arg1', 'arg2', 'arg3')

# Call with any number of keyword arguments
# **kwargs collects keyword arguments into a dictionary
def test_keyword_args(**kwargs):
    print(f'keywords: {kwargs} as {type(kwargs)}')

# Pass keyword arguments - they'll be collected into kwargs dict
test_keyword_args(key1='arg1', key2='arg2')


test_keyword_args(key1='arg1', key2='arg2', key3='arg3')

