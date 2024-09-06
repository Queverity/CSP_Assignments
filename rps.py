import random
running = True
# 0 = Rock, 1 = Paper, 2 = Scissors, 3 = Lizard, 4 = Spock

while running:
  player_input = input("Rock, Paper, Scissors, Lizard, or Spock?")
  computer_input = random.randint(0,4)

  if player_input == "Rock":
    if computer_input == 0:
     print("The computer played rock. It's a tie!")
    elif computer_input == 1:
      print("The computer played paper. You lost.")
    elif computer_input == 2:
      print("The computer played scissors. You won!")
    elif computer_input == 3:
      print("The computer played lizard. You won!")
    elif computer_input == 4:
      print("The computer played spock. You lost.")

  elif player_input == "Paper":
    if computer_input == 0:
     print("The computer played rock. You won!")
    elif computer_input == 1:
      print("The computer played paper. It's a tie!")
    elif computer_input == 2:
      print("The computer played scissors. You lost.")
    elif computer_input == 3:
      print("The computer played lizard. You lost.")
    elif computer_input == 4:
      print("The computer played spock. You won!")

  elif player_input == "Scissors":
    if computer_input == 0:
     print("The computer played rock. You lost.")
    elif computer_input == 1:
      print("The computer played paper. You won!")
    elif computer_input == 2:
      print("The computer played scissors. It's a tie.")
    elif computer_input == 3:
      print("The computer played lizard. You won!")
    elif computer_input == 4:
      print("The computer played spock. You lost.")

  elif player_input == "Lizard":
    if computer_input == 0:
      print("The computer played rock. You lost.")
    elif computer_input == 1:
      print("The computer played paper. You won!")
    elif computer_input == 2:
      print("The computer played scissors. You lost.")
    elif computer_input == 3:
      print("The computer played lizard. It's a tie!")
    elif computer_input == 4:
      print("The computer played spock. You won!")

  elif player_input == "Spock":
    if computer_input == 0:
      print("The computer played rock. You won!")
    elif computer_input == 1:
      print("The computer played paper. You lost.")
    elif computer_input == 2:
      print("The computer played scissors. It's a won!")
    elif computer_input == 3:
      print("The computer played lizard. You lost.")
    elif computer_input == 4:
      print("The computer played spock. It's a tie!")
      
  else:
    print("Invalid Answer")
  player_input = input("Do you want to play again?")
  if player_input == "Yes":
    pass
  elif player_input == "No":
    break