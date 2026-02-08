# str.format() method: modern string formatting (Python 2.7+)
name = 'Nikita'
age = 28
height = 5.4

print("Hello I'm {}, my age is {} and my height is {} inches".format(name, age, height))  # {} = placeholder

# f-string: recommended way to format strings (Python 3.6+)
name = 'Elizabeth'
print(f'Hello {name}!')  # f prefix allows expressions in {}
# f-strings support expressions: can include calculations inside {}
a = 5
b = 10
#inline arithmetic
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.') # Evaluates expressions
#Multiline f-Strings
name = 'Robert'
messages = 12
print(
f'Hi, {name}. '
f'You have {messages} unread messages'
)
# = specifier: prints both variable name and value (Python 3.8+)
from datetime import datetime
now = datetime.now().strftime("%b/%d/%Y - %H:%M:%S")
print(f'date and time: {now=}')  # Prints "now='Nov/14/2022 - 20:50:01'"

#Adding spaces or characters
name = 'Robert'
print(f"{name.upper() = :-^20}")


a = 1000000
print(f"{a:,}")
#rounding
a = 3.1415926
print(f"{a:.2f}")
#Template string
from string import Template
name = 'Elizabeth'
t = Template('Hey $name!')
print(t.substitute(name=name))
