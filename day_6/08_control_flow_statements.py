# # Conditions can be > < >= <= == !=

# # if condition:
# x = 0
# if x > 0:
#     print('x is positive')
# elif x < 0:
#     print('x is negative')
# else:
#     print('x is zero')
    
# # Write a Python program that takes a list of numbers as input. For each number in the list, if the number is even, print the square of the number. If the number is odd, print the cube of the number.

# # Take a list of numbers as input
# numbers = input('Enter a list of numbers separated by spaces: ').split()
# print(numbers)

# # Convert each input to an integer
# numbers = [int(num) for num in numbers]
# print(numbers)

# # Iterate over each number in the list
# for number in numbers:
#     if number % 2 == 0:
#         print(number ** 2)  # Square the number if it's even
#     else:
#         print(number ** 3)  # Cube the number if it's odd

# # for loop
# fruits = {'apple', 'banana', 'orange', 'mango', 'apple'}

# for fruit in fruits:
#     print(fruit)
    
# # Write a Python program that takes a list of numbers as input. Use a for loop to iterate over the list and print each number multiplied by 2.

# numbers = input('Enter a list of numbers separated by spaces: ').split()
# print(numbers)
# numbers = [int(num) for num in numbers]
# print(numbers)

# for num in numbers:
#     print(num * 2)

# # while loop

# i = 1
# while i < 6:
#     print(i)
#     i += 1 # i = i + 1

# # Write a Python program that takes a positive integer as input and uses a while loop to print the squares of all numbers from 1 up to the square of the input number.

# # Take a positive integer as input
# num = int(input('Enter a positive integer: '))

# # Initialize a counter
# i = 1

# # Use a while loop to print the squares of numbers from 1 up to the square of the input number
# while i <= num:
#     print(i**2)
#     i += 1

# Control Flow Statements
## Control statement
for letters in "Python":
    if letters == "h":
        break
    print(letters)

## Continue Statement
for letters in "Python":
    if letters == "h":
        continue
    print(letters)

## Pass Statement
for letters in "Python":
    if letters == "h":
        pass
    print(letters)