# Traditional approach: create list using a for loop
names = ['Charles', 'Susan', 'Patrick', 'George']

x_list = []
for n in names:
    x_list.append(n)

print(x_list)


# Traditional approach: filter with if condition
names = ['Charles', 'Susan', 'Patrick', 'George', 'Carol','Shivi','Simran']

new_list = []
for n in names:
    if n.startswith('S'):  # Filter names starting with 'C'
        new_list.append(n)

print(new_list)

# List comprehension with condition: filter items
# Syntax: [expression for item in iterable if condition]
new_list = [n for n in names if n.startswith('C')]
print(new_list)

# List comprehension with if-else: conditional expression
# Syntax: [expression_if_true if condition else expression_if_false for item in iterable]
nums = [1, 2, 3, 4, 5, 6]
new_list = [num*2 if num % 2 == 0 else num for num in nums]  # Double even numbers
print(new_list)


# Set comprehension: create a set using comprehension syntax
# Syntax: {expression for item in iterable}
b = {"abc", "def"}
x={s.upper() for s in b}  # Convert all strings to uppercase
print(x)

# Dict comprehension: swap keys and values
# Syntax: {key_expression: value_expression for item in iterable}
c = {'name': 'Pooka', 'age': 5}
d={v: k for k, v in c.items()}  # Reverse key-value pairs
print(d)

# List comprehension from dictionary: create formatted strings
c = {'name': 'Pooka', 'age': 5}
e=["{}:{}".format(k.upper(), v) for k, v in c.items()]  # Format as "KEY:value"
print(e)