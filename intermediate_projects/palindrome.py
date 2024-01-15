def convertInputString():
    rawInput = input("\nPlease enter a word, phrase, or a sentence \nto check if it is a palindrome: ")
    rawString = rawInput.lower()
    rawList = list(rawString)
    return rawList


def stripAlphabetic(badlist: list):
    alphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""]
    for character in alphabeticList:
        if character in badlist:
            badlist.remove(character)
            return stripAlphabetic(badlist)
    return badlist


def runPalindromeCheck(straightList):
    reversedList = straightList[::-1]
    if reversedList == straightList:
        return "The text you have entered is a palindrome!"
    else:
        return "The text you have entered is not a palindrome."


def check_palindrome():
    print("\tWelcome to Palindrome checker!")
    original_list = convertInputString()
    original_list = stripAlphabetic(original_list)
    palindromecheck = runPalindromeCheck(original_list)
    print(palindromecheck)

check_palindrome()