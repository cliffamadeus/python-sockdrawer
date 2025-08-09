import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_title():
    print("Welcome to my application")

def display_name(name):
    print("It is nice to meet you "+name)

def display_number(number_input):
    print("Oh your favorite number is " +number_input)

def main():

    while True:

        clear_console()
        name = input("Enter your name: ")

        while True:
            number_input = input("Enter your favorite number: ")
            try:
                num = int(number_input)
                break
            except ValueError:
                print("Invalid input, please input a valid number")


        display_title()
        display_name(name)
        display_number(number_input)
        again = input("\nThere's not that much to do here, do you want to exit? y/n :").strip().lower()
        if again !='n':
            print("Lata beech")
            break

main()