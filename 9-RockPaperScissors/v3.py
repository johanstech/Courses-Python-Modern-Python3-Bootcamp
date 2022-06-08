from random import randint

playerWins = "Player wins!"
computerWins = "Player wins!"

print("Rock, paper, scissors...")
print("Player, make your move!")

player = input().lower()

randNum = randint(0, 2)
if randNum == 0:
    computer = "rock"
elif randNum == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"Computer plays {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print(playerWins)
    else:
        print(computerWins)
elif player == "paper":
    if computer == "rock":
        print(playerWins)
    else:
        print(computerWins)
elif player == "scissors":
    if computer == "paper":
        print(playerWins)
    else:
        print(computerWins)
else:
    print("Please, enter a valid move...")
