import random
#Hangman, by Clayton Baird, Nick L., Dean peterson, and Wakefield Batty
#comments bad



#Make a list of words - Everyone
words = ['computer','science','moles','principles','rizzler','pryor','crunchy']   


word = words[random.randint(0,7)]
wordLength = len(word)

lettersGuessed = []
lettersGuessedStr = '' 
lettersFailed = []
lettersFailedStr = ''
incorrectGuesses = 0
for i in range(wordLength):
    lettersGuessed.insert(i, "_")


#Allow people to choose to play again or not - Pryor
def playingAgain():
    listWord = []
    playAgain = input("Would you like to play again? Yes/nuhuhuh")
    if playAgain == "Yes":
        incorrectGuesses = 0
        word = words[random.randint(0,7)] #dean 
    else:
        incorrectGuesses = 9
# Set amount of tries - Dean
while incorrectGuesses < 6:
    #Make something to choose words - Everyone
    i = 0
    listWord = []
    print("Hello! Welcome to hangman. A word has been selected randomly.")
    #Allow people to input letters - Nicholas
    guess = input("Please guess a letter.")
    correct = False
    listWord = str.split(word)
    for item in listWord:
        #Fill gaps in word with correct letters - Nicholas
        if guess == listWord[i]:
            lettersGuessed[i] = guess
            lettersGuessedStr.join(lettersGuessed)
            correct = True
    if correct != True:
        lettersFailed.insert(i, guess)
        lettersGuessedStr.join(lettersFailed)
    i += 1
    #Print out incorrect letters - Pryor
    print("Your current incorrect letters are: " + lettersFailedStr)
            
    incorrectGuesses += 1
    
    #Show if someone has won or not - Wakefield
    if lettersGuessed == listWord:
        print("You win!") 
    elif incorrectGuesses >= 6:
        print("You just hanged a man. He is now dead. There is blood on your hands now. His family is miserable without him, and they have no food to eat because he bought all of it. Anyways, the word was " + word)
        playingAgain()
