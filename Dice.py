
from random import randint
from time import sleep

#Rolling two dice is assigned a value using randint

def Rolling():
    dice_roll1 = randint(1,6)
    dice_roll2 = randint(1,6)
    print("Rolling dice..")
    sleep(1)
    #print (dice_roll1, dice_roll2)
    return dice_roll1 + dice_roll2

# Ask the user to guess the sum of both rolling dice

def user_guess():
    guess = int(input("Enter user prediction: "))
    return guess

# Execute the methods and check if the user guessed the number correct!

def main():
    sum = Rolling()
    guess = user_guess()

    trial = 5
    while trial > 0:
        if guess == sum:
            print ("Matched")
            break
        elif guess > sum:
            print("Guess is higher than the sum of dice. Try again!")
            trial = trial - 1
            print("Tries left: ",trial)
            guess = user_guess()
        else:
            print("Guess is lower than the sum of dice. Try again!")
            trial = trial - 1
            print("Tries left: ", trial)
            guess = user_guess()

    print("Sum of rolled dice= ", sum)

main()