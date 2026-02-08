import re

#digit \d, word \w, space \s
# re.compile(): create regex pattern object (use raw string r'' to avoid escaping)
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # Pattern: 3 digits-3 digits-4 digits

mo = phone_num_regex.search('My number is 415-555-4245')  # Search for pattern

print(f'Phone number found: {mo.group()}')  # group() returns matched text
#Grouping with parenthesis
# Parentheses create groups: group(1) returns first group, group(2) returns second
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  # Two groups in parentheses
mo = phone_num_regex.search('My number is 415-555-4242.')

print(mo.group(1))  # Returns first group: '415'
print(mo.group(2))  # Returns first group: '555-4242'

ha_regex = re.compile(r'(Ha){3}')

mo1 = ha_regex.search('HaHaHa what are you saying lol')
print(mo1.group())

#Greedy and non- greedy (? shortest string possible)
#Python’s regular expressions are greedy by default: in ambiguous situations
# they will match the longest string possible. The non-greedy version of the
# curly brackets, which matches the shortest string possible, has the closing
# curly bracket followed by a question mark.
greedy_ha_regex = re.compile(r'(Ha){3,5}')

mo1 = greedy_ha_regex.search('HaHaHaHaHa')
print(mo1.group())

non_greedy_ha_regex = re.compile(r'(Ha){3,5}?')
mo2 = non_greedy_ha_regex.search('HaHaHaHaHa')
print(mo2.group())

#The findall() method will return the strings of every match in the searched string.
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups

print(phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000'))


#^ match must occur at the beginning of the searched text, $ at the end
begins_with_hello = re.compile(r'^Hello$')
mp=begins_with_hello.search('Hello') #match object
print(mp.group()) #returns matched string

whole_string_is_num = re.compile(r'^\d+$')

print(whole_string_is_num.search('1234567890'))

#Wildcard character (.) Dot
at_regex = re.compile(r'..at')

print(at_regex.findall('The cat in the hat sat on the flat mat.'))
#Matching everything with Dot-Star .* uses greedy mode and .*? - non greedy
name_regex = re.compile(r'(First Name:.*) Last Name: (.*)')

mo = name_regex.search('First Name: Nikita Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

#To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second
# argument to re.compile():
robocop = re.compile(r'robocop', re.IGNORECASE)

print(robocop.search('RoboCop is part man, part machine, all cop.').group())
#Substituting strings with the sub() method
# The sub() method for Regex objects is passed two arguments:
# The first argument is a string to replace any matches.
# The second is the string for the regular expression.
names_regex = re.compile(r'Agent \w+')

print(names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
#function to ignore whitespace and comments inside the regular expression string,
# “verbose mode” can be enabled by
# passing the variable re.VERBOSE as the second argument to re.compile().
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
test_string = "(415) 555-2671 ext. 123"

match = phone_regex.search(test_string)
print(match.group() if match else "No match")