import random

fruits = ["apple", "banana", "cherry", "grape",]
print("My list of fruits", fruits)
incorrect = True

while incorrect:
    choice = random.choice(fruits)
    picked = input("Guess which fruit I am thinking of: ")
    if picked == choice:
        print("You guessed it right!")
        incorrect = False
    else:
        print("You guessed it wrong. I was thinking of", choice)
        print("You guessed it wrong. Try again!")