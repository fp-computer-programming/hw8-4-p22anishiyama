# Author: ATN 12/9/21

import random

random_number = random.randint(0, 50)

while True:
    guess = int(input("Please guess a number from 0-50. "))
    if(guess > random_number):
        print("Too high!")
        continue
    elif(guess < random_number):
        print("Too low!")
        continue
    elif(guess == random_number):
        print("You guessed it!")
    break

