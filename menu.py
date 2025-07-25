import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_console() 
        print("Welcome to my application")
        again = input("\nThere's not that much to do here, do you want to exit? y/n :").strip().lower()
        if again !='n':
            print("Lata beech")
            break

main()