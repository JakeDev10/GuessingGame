import random

usedWords = set()
specialChars = {'~','`','!','@','#','$','%','^','&','*','(',')','-','_',
                '+','=','[',']','{','}','|','\\',':',';','\'','"','<','>',
                ',','.','?','/', '1','2','3','4','5','6','7','8','9'}
goalWord = ''
winCount = 0
loseCount = 0

file = open('words_alpha.txt')
words = file.read().splitlines()
file.close()

def initializeGame():
    global remainingGuesses
    global guesses
    global winCondition

    remainingGuesses = 7
    guesses = set()
    winCondition = 0

    chooseWord()

#choose a random word, ensure it is new
def chooseWord():
    global goalWord
    global usedWords
    global goalWordList

    usedWords.add(goalWord)

    while goalWord in usedWords:
        goalWord = words[random.randrange(0, 370103)]       #there are 370103 words in words_alpha.txt
    
    goalWordList = list(goalWord)

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
    global remainingGuesses
    global winCondition

    guessType = getInput()      #gets user input and stores whether it's a letter, word, or has illegal chars
    if guessType == 1:
        if userInput not in goalWordList:
            remainingGuesses = remainingGuesses - 1
            print("That letter isn't in the word.")
        else:
            guesses.add(userInput)
    elif guessType == 2:
        if list(userInput) == goalWordList:
            winCondition = 1
        else:
            print("Try again!")
            remainingGuesses = remainingGuesses -1
    else:
        print("Only letters or words allowed!")

initializeGame()

while 1:
    if remainingGuesses != 0 and winCondition == 0:
        doGuess()
    displayWord = ''
    playAgain = ''

    for i in range(0,len(goalWordList)):            #This shows the word in progress based on previous guesses
        if goalWordList[i] in guesses:
            displayWord = displayWord + goalWordList[i]
        else:
            displayWord = displayWord + '_'
    if list(displayWord) == goalWordList:
        winCondition = 1

    print(f"The word so far: {displayWord} Guesses remaining: {remainingGuesses}")
    if winCondition == 1:
        print(f"You won! You have {winCount+1} win(s) and {loseCount} loss(es)")
        playAgain = input("Would you like to play again? y/n ")
        if playAgain == 'y':
            initializeGame()
            winCount = winCount + 1
        elif playAgain == 'n':
            break

    if remainingGuesses == 0:
        print(f"You lost! You have {winCount} win(s) and {loseCount+1} loss(es)")
        print("The word was %s " % goalWord)
        playAgain = input("Would you like to play again? y/n ")
        if playAgain == 'y':
            initializeGame()
            loseCount = loseCount + 1
        elif playAgain == 'n':
            break


print("Thanks for playing!")