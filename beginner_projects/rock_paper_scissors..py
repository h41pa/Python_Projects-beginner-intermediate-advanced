import random

user_points = 0
computer_points = 0

while True:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors, or exit: ")
    if user_input == "exit":
        print("Game ended")
        print(f"You won a total of {user_points} and computer won {computer_points}")
        break
    if user_input not in options:
        print("Invalid input")
        continue
    computer_input = random.choice(options)
    print(f"Your input is {user_input}")
    print(f"Computer input is {computer_input}")
    if user_input == computer_input:
        print("It's tie!")

    elif (user_input == "rock" and computer_input == "scissors") or \
         (user_input == "paper" and computer_input == "rock") or \
         (user_input == "scissors" and computer_input == "paper"):
        print('You Win!')
        user_points +=1
    else:
        print("computer wins")
        computer_points += 1

