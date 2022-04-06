
remainingGuesses = 7
guesses = set()
specialChars = {'~','`','!','@','#','$','%','^','&','*','(',')','-','_',
                '+','=','[',']','{','}','|','\\',':',';','\'','"','<','>',
                ',','.','?','/', '1','2','3','4','5','6','7','8','9',}
goalWord = 'Mississippi'
goalWord = list(goalWord.lower())
winCondition = 0
userInput = ''

#return 1 if single letter, 2 if word, 0 if any special chars
def getInput():         
    global userInput 
    userInput = input('Guess a letter or word: ')

    if set(userInput) & specialChars != set():
        return 0

    userInput = userInput.lower()

    if type(userInput) is str and len(userInput) == 1:
        return 1
    else:
        return 2

#Check guess, adjust remainingGuesses and winCondition appropriately
def doGuess():
    global userInput
    global goalWord
    global remainingGuesses
    global winCondition

    guessType = getInput()      #gets user input and stores whether it's a letter, word, or has illegal chars
    if guessType == 1:
        if userInput not in goalWord:
            remainingGuesses = remainingGuesses - 1
            print("That letter isn't in the word.")
        else:
            guesses.add(userInput)
    elif guessType == 2:
        if list(userInput) == goalWord:
            winCondition = 1
        else:
            print("Try again!")
            remainingGuesses = remainingGuesses -1
    else:
        print("Only letters or words allowed!")

while remainingGuesses > 0:
    doGuess()
    displayWord = ''

    for i in range(0,len(goalWord)):
        if goalWord[i] in guesses:
            displayWord = displayWord + goalWord[i]
        else:
            displayWord = displayWord + '_'
    if list(displayWord) == goalWord:
        winCondition = 1

    if winCondition == 1:
        break

    print("The word so far: %s" % displayWord)

if winCondition == 1:
    print("You won!")
else:
    print("You're out of guesses, you lost!")