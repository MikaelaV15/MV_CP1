# MV 1st Fix the game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print ("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: "))
        #this needed to be an integer or it wouldn't recognize that it is a number
        attempts =+ 1 
        #the game would never end because the number of attempts wasn't increasing 
        if attempts > max_attempts:
        #If it is also equal to it wouldn't give you an extra attempt 
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            game_over = False 
        elif guess < number_to_guess:
            print("Too low! Try again.") 
            game_over = False
        continue
    print("Game Over. Thanks for playing!")
start_game()
