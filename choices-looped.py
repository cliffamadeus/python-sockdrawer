def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def product(num1, num2):
    return num1 * num2

def quotient(num1, num2):
    return num1 / num2 if num2 != 0 else "Undefined (division by zero)"

print("Arithmetic with Two Numbers")
num1 = int(input("Enter first value: "))
num2 = int(input("Enter second value: "))
print("The numbers are", num1, "and", num2)

while True:
    print("\nWhat would you like me to do next?")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[5] Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        result = addition(num1, num2)
    elif choice == 2:
        result = subtraction(num1, num2)
    elif choice == 3:
        result = product(num1, num2)
    elif choice == 4:
        result = quotient(num1, num2)
    elif choice == 5:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        continue

    print("The result is:", result)

    cont = input("\nWould you like to perform another operation? (y/n): ").lower()
    if cont != 'y':
        print("Thank you for using the program!")
        break
