# If Statement Prompt:

## "Write a Python program that takes a number as input and checks if it is positive, negative, or zero. Print the result."

# number = input ("Enter a number: ")
# print(number)

# if number > 0:
#     print('The number is positive')
# elif number < 0:
#     print('The number is negative')
# else:
#     print('The number is zero')
    
# For Loop Prompt:
## "Write a Python program that takes a list of numbers as input. Use a for loop to iterate over the list and calculate the sum of all numbers in the list. Print the sum."

# lists_of_numbers = input('Enter a list of numbers separated by spaces: ').split()
# print(lists_of_numbers)

# number = [int(num) for num in lists_of_numbers]
# print(number)

# total_sum = 0
# for num in number:
#     total_sum += num

# print("The sum of the numbers is:", total_sum)

number = int(input("Enter a number: "))
print(number)

i = 1
while i <= number:
    print(f"{i} ")
    i += 1
