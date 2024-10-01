import random
# 0 is rock, 1 is paper, 2 is scissors, 3 is lizard, and 4 is spock.
running = True
while running:
    userinput = input("Rock, Paper, Scissors, Lizard, or Spock?")
    computer = random.randint(0,4)
    if userinput == "Rock":
        if computer == 0:
            print("The computer played rock. It's a tie!")

        if computer == 1:
            print("The computer played paper. You lost.")

        if computer == 2:
            print("The computer played scissors. You won!")

        if computer == 3:
            print("The computer played lizard. You won!")

        if computer == 4:
            print("The computer played spock. You lost.")
        
    elif userinput == "Paper":
        if computer == 0:
            print("The computer played rock. You won!")

        if computer == 1:
            print("The computer played paper. It's a tie!")

        if computer == 2:
            print("The computer played scissors. You lost.")

        if computer == 3:
            print("The computer played lizard. You lost.")

        if computer == 4:
            print("The computer played spock. You won!")

    elif userinput == "Scissors":
        if computer == 0:
            print("The computer played rock. You lost.")

        if computer == 1:
            print("The computer played paper. You won!")

        if computer == 2:
            print("The computer played scissors. It's a tie!")

        if computer == 3:
            print("The computer played lizard. You won!")

        if computer == 4:
            print("The computer played spock. You lost.")

    elif userinput == "Lizard":
        if computer == 0:
            print("The computer played rock. You lost.")

        if computer == 1:
            print("The computer played paper. You won!")

        if computer == 2:
            print("The computer played scissors. You lost.")

        if computer == 3:
            print("The computer played lizard. It's a tie!")

        if computer == 4:
            print("The computer played spock. You won!")

    elif userinput == "Spock":
        if computer == 0:
            print("The computer played rock. You won!")

        if computer == 1:
            print("The computer played paper. You lost.")

        if computer == 2:
            print("The computer played scissors. You won!")

        if computer == 3:
            print("The computer played lizard. You lost.")
            
        if computer == 4:
            print("The computer played spock. It's a tie!")