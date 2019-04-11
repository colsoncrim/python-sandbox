# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Colson'
age = 26

# Concatenate (insert a variable into a string)
#print('Hello, my name is ' + name + ' and I am ' + str(age))


# String Formatting

# Arguements by Position
#print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-strings
#print(f'Hello, my name is {name} and I am {age}')


# String Methods

s = 'hello world'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count (counts the number of h's inside of a string)
sub = 'h'
print(s.count(sub))

# Find position 
print(s.find('r'))
