import random
# 0 is rock, 1 is paper, 2 is scissors, 3 is lizard, and 4 is spock.
running = True
while running:
    user1input = input("Rock, Paper, Scissors, Lizard, or Spock?")
    user2input = input("Rock, Paper, Scissors, Lizard, or Spock?")
    if user1input == "Rock":
        if user2input == 0:
            print("The computer played rock. It's a tie!")

        if user2input == 1:
            print("The computer played paper. You lost.")

        if user2input == 2:
            print("The computer played scissors. You won!")

        if user2input == 3:
            print("The computer played lizard. You won!")

        if user2input == 4:
            print("The computer played spock. You lost.")
        
    elif user1input == "Paper":
        if user2input == 0:
            print("The computer played rock. You won!")

        if user2input == 1:
            print("The computer played paper. It's a tie!")

        if user2input == 2:
            print("The computer played scissors. You lost.")

        if user2input == 3:
            print("The user2input played lizard. You lost.")

        if user2input == 4:
            print("The computer played spock. You won!")

    elif user1input == "Scissors":
        if user2input == 0:
            print("The computer played rock. You lost.")

        if user2input == 1:
            print("The computer played paper. You won!")

        if user2input == 2:
            print("The computer played scissors. It's a tie!")

        if user2input == 3:
            print("The computer played lizard. You won!")

        if user2input == 4:
            print("The computer played spock. You lost.")

    elif user1input == "Lizard":
        if user2input == 0:
            print("The computer played rock. You lost.")

        if user2input == 1:
            print("The computer played paper. You won!")

        if user2input == 2:
            print("The computer played scissors. You lost.")

        if user2input == 3:
            print("The computer played lizard. It's a tie!")

        if user2input == 4:
            print("The computer played spock. You won!")

    elif user1input == "Spock":
        if user2input == 0:
            print("The computer played rock. You won!")

        if user2input == 1:
            print("The computer played paper. You lost.")

        if user2input == 2:
            print("The computer played scissors. You won!")

        if user2input == 3:
            print("The computer played lizard. You lost.")
            
        if user2input == 4:
            print("The computer played spock. It's a tie!")
    playagain = input("Do you want to play again? Yes/No")
    if playagain == "Yes":
        pass
    elif playagain == "No":
        break