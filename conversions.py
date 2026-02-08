#int to str
num_int=123
str_val=str(num_int)
print(f"Integer {num_int} as String: '{str_val}'")


#tuple to list
my_tuple=('a','b','c')
my_list=list(my_tuple)
print(f"Tuple {my_tuple} as list: {my_list}")

my_tuple = ('a', 'b', 'c')

my_dict = dict.fromkeys(my_tuple, 1)

print(my_dict)


#list to dict()
my_pairs=[('x',1),('y',2)]
my_dict=dict(my_pairs)
print(f"List of pairs {my_pairs} as dict: {my_dict}")
#return type of an object
print(f"Type of num_int: {type(num_int)}")
#return true if the object is an instance of a class
is_list=isinstance(my_list, list)
print(f"Is my_list an instance of list? {is_list}")

