def display_greetings():
    print("Greetings Professor Falken.")

def display_game_start():
    print("Shall we play a game?")

def list_games():
    print("Here are the available games:")
    print("- Chess")
    print("- Poker")
    print("- Desert Warfare")
    print("- Global Thermonuclear War")
    print("- Tic-Tac-Toe")

def respond_to_game_choice(choice):
    if choice.lower() == "tic-tac-toe":
        print("A strange game.")
        print("The only winning move is not to play.")
        print("How about a nice game of chess?")
    elif choice.lower() == "global thermonuclear war":
        print("Wouldn't you prefer a nice game of chess?")
    else:
        print(f"Starting {choice}... (just kidding, this is a simulation!)")

# Main interaction
user_input = input("")

if user_input.lower() == "hello" or user_input.lower() == "hi":
    display_greetings()
    display_game_start()
    list_games()
    game_choice = input("Which game would you like to play? ")
    respond_to_game_choice(game_choice)
else:
    print("Unable to process request. Please say 'Hello'.")
