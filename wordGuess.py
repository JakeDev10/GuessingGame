"""
remainingGuesses = 7
guesses = empty set
goalWord = list('Mississippi')
displayWord = ''
winCondition = 0

def checkInput(input)
    If input is letter, return 1
    Else if input is word, return 2


def getGuess()
    Get user input, store in userInput

    if checkInput(userInput) is 1:
        if userInput is not in goalWord:
            subtract 1 from remainingGuesses
        else:
            add userInput to guesses
    else if checkInput(userInput) is 2:
        If userInput matches goalword:
            set winCondition to 1
        else:
            print "Try again!"
            Subtract 1 from remainingGuesses
    else:
        print "Only letters or words allowed!"

while remainingGuesses > 0:
    getGuess()
    displayWord = ''

    for i in length of goalWord:
        if goalWord[i] is in guesses:
            add goalWord[i] to displayWord
        else:
            add '_' to displayWord
    
    if winCondition is 1:
        break

    print displayWord

if winCondition is 1:
    print "You won!"
else:
    print "You're out of guesses, you lost!"

"""