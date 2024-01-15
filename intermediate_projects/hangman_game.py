import random
import time

print("\nWelcome to Hangman game !\n")
name = input("Enter your name: ")
print(f"Hello {name} ! Good luck!")
time.sleep(1)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(2)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage"
        , "plants"]

    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n").lower()
    while play_game not in ['y', 'n']:
        play_game = input("Do You want to play again? y = yes, n = no \n").lower()

    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

def hangman():
    global count
    global display
    global word
    global length
    global already_guessed
    global play_game
    limit = 5
    guess = input(f"This is the Hangman word: {display} Enter your guesses: \n")
    guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >=2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in already_guessed:
        print("Try another letter. \n")

    else:
        count +=1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f" Wrong guess. {str(limit - count)} guesses remaining\n")

        elif count == 2:
            time.sleep(2)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(f"Wrong guess. {str(limit - count)} guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print(f"The word was: {already_guessed} {word}")
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()

main()
hangman()





