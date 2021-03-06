# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

 # Create tuple
 fruits = ('Apples', 'Oranges', 'Grapes')
 #fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs a trailing comma
fruits2 = ('Apples')

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

print(len(fruits2))





# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# check if in Set
print('Apples' in fruits_set)

# add duplicate
fruits_set.add('Apples')

# Add to set
fruits_set.add('Grape')

# Remove
fruits_set.remove('Grape')

# Clear Set
fruits_set.clear()



print(fruits_set)
