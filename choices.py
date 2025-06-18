#x = int(input("Enter your value: "))


#print(x)

#if x > 10:
  #print("Above ten,")
  #if x > 20:
    #print("and also above 20!")
  #else:
    #print("but not above 20.") 

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
print("The numbers are ",num1," and ",num2, "")

print("\nWhat would you like me to do next?\n")
print("[1] Addition [2]Subtraction [3]Multiplication [4]Division")
choice = int(input("Enter your value: "))

if choice==1:
    result = addition(num1,num2)
elif choice==2:
    result = subtraction(num1,num2)
elif choice==3:
    result =product(num1,num2)
elif choice==4:
    result =product(num1,num2)
print("The result is: "+ str(result))
