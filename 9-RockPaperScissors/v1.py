player1_win_statement = "Player 1 wins!"
player2_win_statement = "Player 2 wins!"

print("Rock, paper, scissors...")
print("Player 1, make your move!")
player1 = input()
player1 = player1.lower()

print("Player 2, make your move!")
player2 = input()
player2 = player2.lower()

if player1 == "rock" and player2 == "scissors":
    print(player1_win_statement)
elif player1 == "rock" and player2 == "paper":
    print(player2_win_statement)
elif player1 == "paper" and player2 == "rock":
    print(player1_win_statement)
elif player1 == "paper" and player2 == "scissors":
    print(player2_win_statement)
elif player1 == "scissors" and player2 == "paper":
    print(player1_win_statement)
elif player1 == "scissors" and player2 == "rock":
    print(player2_win_statement)
elif player1 == player2:
    print("It's a tie!")
else:
    print("Something went wrong!")
