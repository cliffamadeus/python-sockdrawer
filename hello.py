print("Hello World")

num1=4
num2=5

#Addition
print("The sum of ",num1," and ",num2, " is ",num1+num2)

#Subtraction
print("The difference of ",num1," and ",num2, " is ",num1-num2)

#Multiplication
print("The product of ",num1," and ",num2, " is ",num1*num2)

#Division
print("The quotient of ",num1," and ",num2, " is ",num1/num2)

print(" ")
print("Via Function Block")

# Define the functions
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def product(num1, num2):
    return num1 * num2

def quotient(num1, num2):
    return num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# List of functions
operations = [addition, subtraction, product, quotient]

# Loop through and call each function
for operation in operations:
    result = operation(num1, num2)
    print(f"The {operation.__name__} of {num1} and {num2} is {result}")