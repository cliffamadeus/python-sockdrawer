def display_name(name):
    print(name)

def display_num(num):
    print(num)

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