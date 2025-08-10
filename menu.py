import os

#Terminal
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#Title
def display_title():
    print("Welcome to my application")

#Name Function
def display_name(name):
    print("It is nice to meet you "+name)

#Number
def display_number(number_input):
    print("Oh your favorite number is " +number_input)

def main():

    while True:

        #Clear console instance
        clear_console()

        #Name input
        name = input("Enter your name: ")

        #Number input with error correction
        while True:
            number_input = input("Enter your favorite number: ")
            try:
                num = int(number_input)
                break
            except ValueError:
                print("Invalid input, please input a valid number")

        #Display title instance
        display_title()

        #Display name instance
        display_name(name)

        #Display number instance
        display_number(number_input)

        
        again = input("\nThere's not that much to do here, do you want to exit? y/n :").strip().lower()
        if again !='n':
            print("Lata beech")
            break

main()