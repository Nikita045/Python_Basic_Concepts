# Escape characters: use backslash to insert special characters
# \n = newline, \' = single quote
print("Hello there!\nHow are you?\nI\'m doing fine.")
# Raw string (r prefix): treats backslashes as literal characters
#Multiline string
print(r"Hello there!\nHow are you?\nI\'m doing fine.")  # \n printed literally
print(
"""Dear Alice,

Eve's cat has been arrested for catnapping,
cat burglary, and extortion.

Sincerely,
Bob"""
)
#Indexing & Slicing
# String indexing: access characters by position (0-based)
spam = 'Hello world!'

print(f"Oth index value='{spam[0]}'")  # Returns first character: 'H'

# String slicing: extract substring using [start:end] syntax
spam = 'Hello world!'

print(spam[6:-1]) # Returns characters from index 0 to 4: 'Hello'
#reverse string
#start,end, step
print(spam[::-1])

#upper(), lower(),title()
str1="Hello world!"
print(str1.upper(),str1.lower(),str1.title())
#isupper(), islower(), istitle() returns true or false
spam = 'Hello World!'
print(spam.islower())
print(spam.istitle())
print('HELLO'.isupper())
#isalpha - only letters, isalnum -letter & numbers, isdecimal - only numbers, isspace() - only space,tab and new line
#startswith() & endswith()
print('Hello world, this is nikita kataria a beautiful women!'.startswith('Hello'))
print('Hello world, this is nikita kataria a beautiful women!'.endswith('women!'))

#join() & split()
#The join() method takes all the items in an iterable, like a list, dictionary, tuple or set,
# and joins them into a string. You can also specify a separator.

print(''.join(['My', 'name', 'is', 'Simon'])
)#no space no separator in this
print(', '.join(['cats', 'rats', 'bats'])
)
#The split() method splits a string into a list.
# By default, it will use whitespace to separate the items,

print('nikitakataria50@gmail.com'.split('@')
)

#Justifying text with rjust(), ljust() and center()
print('world'.rjust(20))
print('Hello'.ljust(10))
print('nikita'.center(50, '*'))

print('Hello'.rjust(20, '*'))
#Removing whitespace with strip(), rstrip(), and lstrip()
spam = '         Hello world!    '
print(spam.rstrip())
print(spam.lstrip())

#count method

sentence = 'one sheep two sheep three sheep four'
print(sentence.count('sheep'))
print(sentence.count('ee'))
# returns count of e after 'one sh' i.e 6 chars since beginning of string
print(
sentence.count('e', 6)
)

#replace method
#Replaces all occurences of a given substring with another substring.
# Can be optionally provided a third argument to limit the number of replacements.
text = "Hello, world!"
print(text.replace("world", "planet"))
fruits = "apple, banana, cherry, apple"
print(fruits.replace("apple", "orange", 1))
