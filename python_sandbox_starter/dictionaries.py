# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create Dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
person2 = dict(first_name='Sara', last_name='Williams')

# Get value
print(person['first_name'])
print(person.get('last_name'))

#ADD key/value
person['phone'] = '555-555-5555'

# get Dictionary keys
print(person.keys())

# Get dictionary items
print(person.items())

# Copy a Dictionary
person2 = person.copy()
person2['city'] = 'Boston'

# Remove an item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

#get length
print(len(person2))

# list of dictionaries
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])
