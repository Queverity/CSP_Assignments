import random
#Hangman, by Clayton Baird, Nick L., Dean peterson, and Wakefield Batty

#Make a list of words - Everyone
words = ["computer","science","moles","principles","rizzler","pryor","crunchy","love muffin"]



word = words[random.randint(0,6)]
wordLength = len(word)

lettersGuesssed = []
lettersGuesssedStr = ""
lettersFailed = []
lettersFailedStr = ""
incorrectGuesses = 0
#Allow people to input letters - Nicholas
while incorrectGuesses > 6:
    #Make something to choose words - Everyone
    
    print("Hello! Welcome to hangman. A word has been selected randomly.")
    guess = input("Please enter a letter to guess.")
    listWord = str.split(word)
    for item in listWord:
        if guess == listWord[item]:
            lettersGuesssed.insert(item, guess)
            lettersGuesssedStr.join(lettersGuesssed)
            correct = True
    if correct != True:
        lettersFailed.insert(item, guess)
        lettersGuesssedStr.join(lettersFailed)
        incorrectGuesses += 1
    if incorrectGuesses == 6:
        playingAgain()
            
#Set an amount of tries - Dean

#Print out incorrect letters - Pryor

#Fill gaps in word with correct letters - Nicholas

#Show if someone has won or not - Wakefield
if x == y:
    print("You win!") #make a variable that is either one thing or another to tell the code whether they win or lose.
else:
    print("Why are you so bad at this?")
#Allow people to choose to play again or not - Pryor
def playingAgain():
    playAgain = input("Would you like to play again? Yes/No")
    if playAgain == "Yes":
        incorrectGuesses = 0
        word = words[random.randint(0,6)]
    elif:
        break
    
