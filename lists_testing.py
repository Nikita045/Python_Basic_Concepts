# Slicing creates a copy: [:] creates a shallow copy of the list
spam = ['cat', 'bat', 'rat', 'elephant']
spam2 = spam[:]  # Create a copy, not a reference
print(spam2)

spam2.append('dog')
print(spam2)
print(spam)

# len() returns the number of items in a list
furniture = ['table', 'chair', 'rack', 'shelf']
print(len(furniture))  # Returns 4

# Modify list elements by assigning new values to indexes
furniture = ['table', 'chair', 'rack', 'shelf']

furniture[2] = 'desk'  # Replace first element
print(furniture)

#concatenation
my_list = [1, 2, 3]
my_list = my_list + ['A', 'B', 'C']
print(my_list)

# Iterate over list elements using for loop
furniture = ['table', 'chair', 'rack', 'shelf']

for item in furniture:  # Loop through each item
    print(item)

# enumerate() returns both index and value in a loop
furniture = ['table', 'chair', 'rack', 'shelf']

for index, item in enumerate(furniture):  # Get index and item together
    print(f'index: {index} - item: {item}')

my_tuple = ('a', 'b', 'c')

for index, value in enumerate(my_tuple):
    print(index, value)

# zip() combines multiple lists element-wise in a loop
furniture = ['table', 'chair', 'rack', 'shelf']
price = [100, 50, 80, 40]

for item, amount in zip(furniture, price):  # Pair elements from both lists
    print(f'The {item} costs ${amount}')
# in operator: check if an item exists in a list
'rack' in ['table', 'chair', 'rack', 'shelf']  # Returns True

furniture = ['table', 'chair', 'rack', 'shelf']
'bed' not in furniture
furniture = ['table', 'chair', 'rack', 'shelf']
print(furniture.index('chair'))


furniture.append('bed')
print(furniture)

furniture.insert(1, 'sofa')
print(furniture)

del furniture[2]
print(furniture)

numbers = [2, 5, 3.14, 1, -7]
numbers.sort()
print(numbers)
print(furniture)
furniture.sort(reverse=False)
print(furniture)


letters = ['a', 'z', 'A', 'Z']
letters.sort(key=str.lower)
print(letters)

