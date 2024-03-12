# Data Structure

# List
food = ['rice', 'beans', 'plantain', 'yam', 'garri'] 
print(food)
print(food[1])
print(food[-1])

food[1] = 'bread'
print(food[1])
print(food)

# Tuple
coordinates = (4.29, 5.35)
print(coordinates)
print(coordinates[0])

# Set
fruits = {'apple', 'banana', 'orange', 'mango', 'apple'}
print(fruits)
# print(fruits[1]) # This will throw an error because set is not indexable
fruits.add('grape')

# Dictionary
car = {
    'brand': 'Toyota',
    'model': 'Camry',
    'year': 2020
}
print(car)
print(car['brand'])
car['year'] = 2023
print(car)