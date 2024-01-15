
def convertPhasetoListOfChar():

    phrase = input("\nPlease enter a word, phrase, or a sentence: ")
    rawString = phrase.lower()
    rawlist = list(rawString)
    print(rawlist)
    specialchar = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] # for removering from list of letters

    for char in specialchar:
        if char in rawlist:
            rawlist.remove(char)

    print(f"New formated string  = {rawlist}")


convertPhasetoListOfChar()