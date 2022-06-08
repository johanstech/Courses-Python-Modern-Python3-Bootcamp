from random import randint

player_win_statement = "Player wins this round!\n"
computer_win_statement = "Computer wins this round!\n"

player_score = 0
computer_score = 0
best_of = 3

playing = True

print(f"Rock, paper, scissors...\nBest of {best_of}!")

while playing:
    print("Player, make your move!")
    player = input().lower()

    randNum = randint(1, 30)
    if randNum > 20:
        computer = "rock"
    elif randNum > 10:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"Computer plays {computer} ({randNum})")

    if player == computer:
        print("It's a tie!\n")
    elif player == "rock":
        if computer == "scissors":
            print(player_win_statement)
            player_score += 1
        else:
            print(computer_win_statement)
            computer_score += 1
    elif player == "paper":
        if computer == "rock":
            print(player_win_statement)
            player_score += 1
        else:
            print(computer_win_statement)
            computer_score += 1
    elif player == "scissors":
        if computer == "paper":
            print(player_win_statement)
            player_score += 1
        else:
            print(computer_win_statement)
            computer_score += 1
    else:
        print("Please, enter a valid move...")

    if (player_score + computer_score >= best_of):
        if player_score > computer_score:
            print(
                f"Player won this game with {player_score} against {computer_score}!")
        else:
            print(
                f"Computer won this game with {computer_score} against {player_score}!")

        play_again = input("\nDo you want to play again? (y/n) ")
        if play_again == "n":
            playing = False
        else:
            player_score = 0
            computer_score = 0
            print("\n\n\n")
            print(f"Rock, paper, scissors...\nBest of {best_of}!")

print("\nThank you for playing!")
