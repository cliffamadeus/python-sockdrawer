def display_name(name):
    print("Your name is: "+name)

def display_num(num):
    print("Your jersey number is: " + str(num))

#name = "Cliffmeister"
#num = 16

name = input("Enter your name: ")

while True:
    num_input = input("Enter a number: ")
    try:
        num = int(num_input)
        break  
    except ValueError:
        print("Invalid input. Please enter a valid number.")


display_name(name)
display_num(num)