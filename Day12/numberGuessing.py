import random

def welcome_message():
    print("Welcome to number guessing game")
    print("I am thinking of a number between 1 and 100")

arr = [x for x in range(1, 101)]
lives = 5 
def player_turn(guessed_number):
    global lives
    print(f"You have {lives} lives left")
    number = int(input("Enter the number you feel the computer guessed"))
    if (number != guessed_number):
        lives -= 1
        print("Oops, you lost one life.Its a wrong number. Try guessing again")
    elif number == guessed_number:
        print("Winner winner chicken dinner, you guessed the word right")
        print(f"Your score: {100 - ((5-lives)*25)}")
        exit()
def play_game():
    global lives
    welcome_message()
    guessed_number =  random.choice(arr)
    print(guessed_number)
    while lives > 0:
        player_turn(guessed_number)
    print("Oops you lost the game")
    # exit()

while input("\n \n Do you want to play number guessing game, Type yes or no: ").strip().lower() == "yes":
    lives = 5
    play_game()