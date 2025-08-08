import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_title():
    print("Welcome to my application")

def main():

    while True:
        clear_console() 
        display_title()
        again = input("\nThere's not that much to do here, do you want to exit? y/n :").strip().lower()
        if again !='n':
            print("Lata beech")
            break

main()