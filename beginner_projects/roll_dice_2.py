import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    nums_player = int(input("ENter how many players: "))

    if nums_player % 2 != 0:
        print("numbe rof players need be even")


    score = [0] * nums_player
    # scores = [0 for _ in range(nums_player)]

    while True:
        for player in range(nums_player):
            input(f"Player [{player + 1}] press enter to roll dice")
            roll = roll_dice()
            print(f"Player  [{player + 1}]  rolled {roll} !")
            score[player] += roll
            print(f" PLayer  [{player + 1}] total score is {score[player]}")

        play_again = input("Wanna play ? Y or N")
        if play_again != "Y":
            break

    winner = score.index(max(score)) + 1
    print(f" winner is player [{winner}] who have the total score of {max(score)}")

play_game()