# A List is a collection which is ordered and changeable. Allows duplicate members.
#Similar to an array in JS

# Create List
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])

# Get length of a list
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Change value
fruits[0] = 'Blueberries'

# Remove
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Remove with pop
fruits.pop(2)

#Reverse list
fruits.reverse()

# Sort list
fruits.sort()


print(fruits)
