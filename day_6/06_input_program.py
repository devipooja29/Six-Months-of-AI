# name = input("Enter your name:") # input() function is used to take input from the user
# print(name)

# print("Hello", name, ", How are you?")
# print(f"Hello {name}, How are you?")

# person_a = input("What is your name? \n")
# person_b = input("What is your friend's name? \n")
# age_a = int(input(f"{person_a}, What is your age? \n"))
# age_b = int(input(f"What is {person_b}'s age? \n"))

# if age_a < age_b:
#    print(f"{person_b} is {abs(age_b - age_a)} younger than {person_a}.")
# else:
#    print(f"{person_b} is {abs(age_b - age_a)} younger than {person_a}.")

# BMI Calculator
height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))
bmi = round(weight / height ** 2)
print(f"Your BMI is {bmi}.")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 >= bmi <= 25:
    print("You are healthy weight.")
elif 25.0 >= bmi <= 29.9:
    print("You are overweight.")
else:
    print("You are obese.")

    
    
