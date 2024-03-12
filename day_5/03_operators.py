x = 15 # int
y = 4 # int
z = 5.5 # float
xyz = "Hello" # string
xy = "Pooja" # string

# Addition
print(x+y)
print(xyz + ' ' + xy)

# Subtraction
print(x-y)
# print(xyz-y) # Error because it is a string not an integer or float
print(y-z)

# Multiplication
print(x*y)

# Division
print(x/y)
print(x//y) # Floor Division

# DMAS, PEMDAS, BODMAS -> Python follows PEMDAS rule.

# Comparison Operators
print(x>y) # True if x greater than y else False
print(x<y) # True if x less than y else False
print(x==y) # True if x equal to y else False
print(x!=y) # True if x not equal to y else False
print(x>=y) # True if x greater than or equal to y else False
print(x<=y) # True if x less than or equal to y else False

# Logical Operators AND OR NOT
print(x > y and y < x)
print(x > y or y < x)
print(x > y and not y < x)
print(not x == y)




