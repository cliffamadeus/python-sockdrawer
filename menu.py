import os
import random

#Terminal
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#Title
def display_title():
    print("Welcome to my application")

#Name Function
def greet_name(name):
    print("It is nice to meet you "+name)

def show_name(name):
    print(name)
#Number
def display_number(number_input):
    print("Oh your favorite number is " +number_input)

#Random Quotes
def get_random_quote():
    quotes = [
        "Believe you can and you're halfway there.",
        "Do one thing every day that scares you.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Happiness is not something ready-made. It comes from your own actions.",
        "Your limitation—it's only your imagination.",
        "Push yourself, because no one else is going to do it for you."
    ]
    return random.choice(quotes)

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

        clear_console()

        #Display title instance
        #display_title()

        #Display name instance
        greet_name(name)

        #Display number instance
        display_number(number_input)

        #Print Random Quote
        print ("Hello %s" % name)
        print ("Here is a random quote for you:\n%s"%get_random_quote())

        again = input("\nThere's not that much to do here, do you want to exit? y/n :").strip().lower()
        if again !='n':
            print("Lata beech")
            clear_console()
            break

main()