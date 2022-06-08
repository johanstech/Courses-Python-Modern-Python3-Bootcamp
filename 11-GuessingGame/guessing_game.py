from random import randint

playing = True
randNum = randint(1, 10)

while playing:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < randNum:
        print("Too low, try again!")
    elif guess > randNum:
        print("Too high, try again!")
    else:
        print("You guessed it, you won!")
        playAgain = input("Do you want to keep playing? (y/n) ")
        if playAgain == "n":
            playing = False
        else:
            randNum = randint(1, 10)

print("Thank you for playing!")
