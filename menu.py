import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_title():
    print("Welcome to my application")

def display_name(name):
    print("It is nice to meet you "+name)

def main():

    while True:
        clear_console()
        name = input("Enter your name: ")
        display_title()
        display_name(name)
        again = input("\nThere's not that much to do here, do you want to exit? y/n :").strip().lower()
        if again !='n':
            print("Lata beech")
            break

main()