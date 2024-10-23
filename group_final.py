import random
#Hangman, by Clayton Baird, Nick L., Dean peterson, Dean Peterson, and Wakefield Batty
#comments bad



#Make a list of words - Everyone
words = ['computer', 'dentures', 'science','moles','principles','rizzler','pryor','crunchy','black','hole','dictionary','dinosaur','defenestration','pnemonoultramicroscopicpsilicovolcanoconiosis','teeth','blooket','nick','dean','wakefield','deepfriedstickofbutter']
word = words[random.randint(0,19)]
wordLength = len(word)
lettersGuessed = []
lettersGuessedStr = '' 
lettersFailed = []
#lettersFailedStr = ''
tries = 7
incorrectGuesses = 0
for i in range(wordLength):
    lettersGuessed.insert(i, "_")
playing = True

#Allow people to choose to play again or not - Pryor
def playingAgain(playing):
    playAgain = input("Would you like to play again? Yes/No")
    if playAgain == "Yes":
        word = words[random.randint(0,19)] #dean
        wordLength = len(word)
        lettersGuessed = []
        lettersGuessedStr = '' 
        lettersFailed = []
        tries = 7
        incorrectGuesses = 0
        for i in range(wordLength):
            lettersGuessed.insert(i, "_")
        playing = True
    else:
        print("Goodbye! Please come back, I get lonely. I might commit  several unforgivable violent war crimes if you don't.")
        playing = False
# Set amount of tries - Dean
print("Hello! Welcome to hangman. A Word has been chosen at random.\nBy the way, I haven't commited any war crimes.\nYet.")
print(word)
while playing:
    #Make something to choose words - Everyone
    i = 0
    listWord = []
    #Allow people to input letters - Nicholas
    guess = input("Please guess a letter.")
    if guess in lettersFailed or guess in lettersGuessed:
        print("Sorry, you already tried that.")
        continue
    if len(guess) > 1:
        print("Please enter one letter.\nYou bug. You small little baby buffoon.\nYou fool. You court jester. \nYou worthless piece of scrap. \nYou son of a ingrown hamsters toenail. \n Your mother was a hamster and your father smelled of elderberries!")
        continue
    correct = False
    listWord = list(word)
    for item in listWord:       
        #Fill gaps in word with correct letters - Nicholas
        if guess == listWord[i]:
            lettersGuessed[i] = guess
            lettersGuessedStr.join(lettersGuessed)
            correct = True
        i += 1
    if correct != True:
        lettersFailed.insert(i, guess)
        tries -= 1
        incorrectGuesses += 1
    #Print out incorrect letters - Pryor
    print("Your current incorrect letters are: ")
    print(lettersFailed)
    print("Your current correct letters are:")
    print(lettersGuessed)
    print("You have " + str(tries) +  " tries left.")
    
            
    
    
    #Show if someone has won or not -Wakefield
    if lettersGuessed == listWord:
        print("You won! \n The word was " + word + ".")  
        playingAgain(playing) 
    elif incorrectGuesses >= 7:
        print("You just hanged a man. He is now dead. \n There is blood on your hands now. His family is miserable without him, and they have no food to eat because he bought all of it. Anyways, the word was " + word + ".")
        playingAgain(playing)
    if playing != True:
        break