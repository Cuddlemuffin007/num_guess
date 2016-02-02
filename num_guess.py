from sys import exit
from random import randint
import math

def get_input(prompt):
    return input("%s\n>> " % prompt)

def guess_num():
    return int(get_input("Please enter your guess."))

def set_game_range():
    lower_bound = get_input("Please enter game's lower bound.")
    upper_bound = get_input("Please enter game's upper bound.")
    print("Game range is from %s to %s." % (lower_bound, upper_bound))
    return int(lower_bound), int(upper_bound)

def play_again():
        play_again = get_input("Would you like to play again? (Enter Y or N)")
        while play_again != 'Y' and play_again != 'N':
            play_again = get_input("Would you like to play again? (Enter Y or N)")
        if play_again == 'Y':
            select_game_type()
        elif play_again == 'N':
            print("OK. See you later!")
            exit(0)

def game_won(player_guess, secret_number):
    if player_guess == secret_number:
        print("Congratulations, you won! The secret number was %s." % secret_number)
        return True
    return False

def start():
    lower, upper = set_game_range()
    secret_number = randint(lower, upper)
    # for testing
    #print("Secret number: ", secret_number)
    player_guess = guess_num()

    # for testing
    #print("Player number: ", player_guess)

    while not game_won(player_guess, secret_number):
        if player_guess < secret_number:
            print("Secret number is higher.")
        elif player_guess > secret_number:
            print("Secret number is lower.")
        player_guess = guess_num()
    play_again()

def computer_start():
    print("Provide a range of numbers for the computer.")
    lower, upper = set_game_range()
    secret_number = randint(lower, upper)
    computer_number = (upper - lower) // 2
    print(computer_number, secret_number)
    guesses = 1
    floor = lower
    max = upper

    while computer_number != secret_number:
        if computer_number < secret_number:
            floor = computer_number
            computer_number += math.floor((max - floor)/2)
        elif computer_number > secret_number:
            max = computer_number
            computer_number = math.floor((max - floor)/2)
        guesses += 1

    print("Computer solved in %d guesses." % guesses)
    play_again()

def select_game_type():
    player = get_input("Would you like to play? Enter 'H',\nOr test the computer ('C').")

    if player == 'H':
        start()
    elif player == 'C':
        computer_start()

new_game = select_game_type

new_game()