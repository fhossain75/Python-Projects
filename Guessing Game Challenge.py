#  Guessing Game Challenge
#Author: Faisal Hossain

#  Let's use `while` loops to create a guessing game.

#  The Challenge:
#
#  Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

#  1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
#  2. On a player's first turn, if their guess is
#   * within 10 of the number, return "WARM!"
#   * further than 10 away from the number, return "COLD!"
#  3. On all subsequent turns, if a guess is 
#   * closer to the number than the previous guess return "WARMER!"
#   * farther from the number than the previous guess, return "COLDER!"
#  4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!

#  You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!

## Introduction
print("[] Welcome to PLAY THE PONIES! []")
print("~Guess the right number the 1st time and win a PONY!\n ...anything after, you get to take home a goldfish.")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S ...")
print(".----------------.  .----------------.  .----------------.  .----------------. \n| .--------------. || .--------------. || .--------------. || .--------------. |\n| |   ______     | || |   _____      | || |      __      | || |  ____  ____  | |\n| |  |_   __ \   | || |  |_   _|     | || |     /  \     | || | |_  _||_  _| | |\n| |    | |__) |  | || |    | |       | || |    / /\ \    | || |   \ \  / /   | |\n| |    |  ___/   | || |    | |   _   | || |   / ____ \   | || |    \ \/ /    | |\n| |   _| |_      | || |   _| |__/ |  | || | _/ /    \ \_ | || |    _|  |_    | |\n| |  |_____|     | || |  |________|  | || ||____|  |____|| || |   |______|   | |\n| |              | || |              | || |              | || |              | |\n| '--------------' || '--------------' || '--------------' || '--------------' |\n '----------------'  '----------------'  '----------------'  '----------------'") 

##Sets the random guessing-number
import random
chosen = random.randint(1,101)
##
guess = [0]
num_guess = 0
while guess[-1] < chosen or guess[-1] > chosen:
    guess.append(int(input("Guess a number: ")))
    num_guess +=1
    if num_guess == 1:
        if (chosen-10 <= guess[-1] <= chosen+10):
            print("WARM!")
        else:
            print("COLD!")
    elif guess[-1] == chosen-1 or guess[-1] == chosen+1:
        print("OUT OF BOUNDS")
    elif guess[-1] == chosen:
        print(f"You guesssed it with only {num_guess} guesses!")
        break
    else:
        if ((abs(chosen-guess[-2])) > (abs(chosen-guess[-1]))):
            print("WARMER, try again!")
        else:
            print("COLDER, try again!")
