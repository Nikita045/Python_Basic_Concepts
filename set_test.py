# Create set using curly braces or set() function
s = {1, 2, 3, 4, 3, 5}  # Using curly braces
s = set([1, 2, 3, 4, 3, 5])  # Using set() constructor
print(s)
# Warning: empty {} creates a dictionary, not a set
t = {}  # this will create a dictionary instead of a set
print(type(t))  # Returns <class 'dict'>

#And as an unordered data type, they can’t be indexed.

s.add(88)
print(s)
#to add multiple values at once
s.update([76,54,11,22])
print(s)

#remove & discard
s.remove(76)
print(s)
s.discard(11)
print(s)

# union(): combine all elements from multiple sets (no duplicates)
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))  # or 's1 | s2' - returns {1, 2, 3, 4, 5}

# intersection(): return elements common to all sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
print(s1.intersection(s2, s3))  # or 's1 & s2 & s3' - returns {3}
print(s1 & s2)

# difference(): return elements in first set but not in others
s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(s1.difference(s2)) # or 's1 - s2' - returns {1}


# symmetric_difference(): return elements in either set, but not both
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.symmetric_difference(s2)) # or 's1 ^ s2' - returns {1, 4}

