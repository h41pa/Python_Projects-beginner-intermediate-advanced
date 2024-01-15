import random


def play():
    user = input("What's your choice? 'r' for rock, 'p' for papper, 's' for scissors \n ").lower()
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        print("It's a tie!")

    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        print(f"You won! You chose {user} and computer {computer}")
    else:
        print(f"You lost, Computer won, you chose {user} and computer {computer}")


play()