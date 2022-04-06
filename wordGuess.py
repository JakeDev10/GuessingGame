
remainingGuesses = 7
guesses = set()
specialChars = {'~','`','!','@','#','$','%','^','&','*','(',')','-','_',
                '+','=','[',']','{','}','|','\\',':',';','\'','"','<','>',
                ',','.','?','/', '1','2','3','4','5','6','7','8','9',}
goalWord = 'Mississippi'
goalWord = list(goalWord.lower())
displayWord = ''
winCondition = 0
userInput = ''

#return 1 if single char, 2 if word, 3 if any special chars
def getInput():         
    global userInput 
    userInput = input('Guess a letter or word: ')

    if set(userInput) & specialChars != set():
        return 3

    userInput = userInput.lower()

    if type(userInput) is str and len(userInput) == 1:
        return 1
    else:
        return 2

print(getInput())
print(userInput)

"""
def getGuess()
    global userInput

    if getInput(userInput) is 1:
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