from random import randint

player_win_statement = "Player wins!"
computer_win_statement = "Computer wins!"

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
        print(player_win_statement)
    else:
        print(computer_win_statement)
elif player == "paper":
    if computer == "rock":
        print(player_win_statement)
    else:
        print(computer_win_statement)
elif player == "scissors":
    if computer == "paper":
        print(player_win_statement)
    else:
        print(computer_win_statement)
else:
    print("Please, enter a valid move...")
