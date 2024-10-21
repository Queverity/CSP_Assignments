import random
words = ["computer","science","principles","python","programming"]
wordindex = random.randint(0,4)
lettersguessed = []
word = words[wordindex]
wordlength = len(word)
playing = True
while playing:
    tries = 0
    print("This is a game of hangman. You have " + str(wordlength) + " tries to guess the word.")
    for i in range(wordlength):
        print("_", end=" ")
    letter = print("Type a letter.")
    
    tries += 1
    if tries == wordlength:
        print("You are out of tries! The word was " + word + ".")
        playagain = print("Would you like to play again? Yes/No")
        if playagain == "Yes":
            continue
        elif playagain == "No":
            print("Goodbye!")
            break