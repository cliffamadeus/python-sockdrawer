import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_name(name):
    print("Your name is: "+name)

def display_num(num):
    print("Your jersey number is: " + str(num))

def main():
    while True:
        clear_console() 
        
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

        again = input("\nDo you want to start again? y/n :").strip().lower()
        if again !='y':
            print("Lata beech")
            break

main()