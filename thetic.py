numbers = [" ","1","2","3"]
board1 = ["A","","",""]
board2 = ["B","","",""]
board3 = ["C","","",""]
turn = "X"
def boardprint():
    print(numbers)
    print(board1)
    print(board2)
    print(board3)
playing = True
while playing: 
    if board1[1] == "X" and board1[2] == "X" and board1[3] == "X":
        print("X wins!")
        playing = False
        break
    elif  board2[1] == "X" and board2[2]  == "X"and board3[3] == "X":
        print("X wins!")
        playing = False
        break
    elif  board3[1] == "X" and board3[2] == "X" and board3[3] == "X":
        print("X wins!")
        playing = False
        break
    elif  board1[1] == "X" and board2[2] == "X" and board3[3] == "X":
        print("X wins!")
        playing = False
        break
    elif  board3[1] == "X" and board2[2] == "X" and board1[3] == "X":
        print("X wins!")
        playing = False
        break
    elif  board1[1] == "X" and board2[1] == "X" and board3[1] == "X":
        print("X wins!")
        playing = False
        break
    elif  board1[2] == "X" and board2[2] == "X" and board3[2] == "X":
        print("X wins!")
        playing = False
        break
    elif  board1[3 == "X"] and board2[3] == "X" and board3[3] == "X":
        print("X wins!")
        playing = False
        break
    elif  board1[1] == "O" and board1[2] == "O" and board1[3] == "O":
        print("O wins!")
        playing = False
        break
    elif  board2[1] == "O" and board2[2] == "O" and board3[3] == "O":
        print("O wins!")
        playing = False
        break
    elif  board3[1] == "O" and board3[2] == "O" and board3[3] == "O":
        print("O wins!")
        playing = False
        break
    elif  board1[1] == "O" and board2[2] == "O" and board3[3] == "O":
        print("O wins!")
        playing = False
        break
    elif  board3[1] == "O" and board2[2] == "O" and board1[3] == "O":
        print("O wins!")
        playing = False
        break
    elif  board1[1] == "O" and board2[1] == "O" and board3[1] == "O":
        print("O wins!")
        playing = False
        break
    elif  board1[2] == "O" and board2[2] == "O" and board3[2] == "O":
        print("O wins!")
        playing = False
        break
    elif  board1[3] == "O" and board2[3] == "O" and board3[3] == "O":
        print("O wins!")
        playing = False  
        break   
    print(numbers)
    print(board1)
    print(board2)
    print(board3)
    
    if turn == "X":
        playerx1 = (input("Player X, where on the board do you want to go? Enter it in like battleship coardinates. ie: A1, B2, C3"))
        if playerx1 == "A1" and board1[1] == "":
            board1[1] = "X"
            turn = "O"
            boardprint()      
        if playerx1 == "A2" and board1[2] == "":
            board1[2] = "X"
            turn = "O"
            boardprint()      
        if playerx1 == "A3" and board1[3] == "":
            board1[3] = "X"
            turn = "O"
            boardprint()
        if playerx1 == "B1" and board2[1] == "":
            board2[1] = "X"  
            turn = "O"
            boardprint()    
        if playerx1 == "B2" and board2[2] == "":
            board2[2] = "X"
            turn = "O"
            boardprint()        
        if playerx1 == "B3" and board2[3] == "":
            board2[3] = "X"
            turn = "O"
            boardprint()      
        if playerx1 == "C1" and board3[1] == "":
            board3[1] = "X"
            turn = "O"
            boardprint()       
        if playerx1 == "C2" and board3[2] == "":
            board3[2] = "X"
            turn = "O"
            boardprint()        
        if playerx1 == "C3" and board3[3] == "":
            board3[3] = "X"
            turn = "O"
            boardprint()        
    elif turn == "O":
        playero1 = (input("Player O, where do you want to go on the board?"))
        if playero1 == "A1" and board1[1] == "":
            board1[1] = "O"
            turn = "X"
            boardprint()      
        if playero1 == "A2" and board1[2] == "":
            board1[2] = "O"
            turn = "X"
            boardprint()      
        if playero1 == "A3" and board1[3] == "":
            board1[3] = "O"
            turn = "X"
            boardprint()
        if playero1 == "B1" and board2[1] == "":
            board2[1] = "O"  
            turn = "X"
            boardprint()    
        if playero1 == "B2" and board2[2] == "":
            board2[2] = "O"
            turn = "X"
            boardprint()        
        if playero1 == "B3" and board2[3] == "":
            board2[3] = "O"
            turn = "X"
            boardprint()      
        if playero1 == "C1" and board3[1] == "":
            board3[1] = "O"
            turn = "X"
            boardprint()       
        if playero1 == "C2" and board3[2] == "":
            board3[2] = "O"
            turn = "X"
            boardprint()        
        if playero1 == "C3" and board3[3] == "":
            board3[3] = "O"
            turn = "X"
            boardprint()     
    if board1[1] == "X" and board1[2] == "X" and board1[3] == "X":
        print("X wins!")
        playing = False
        break
    elif  board2[1] == "X" and board2[2]  == "X"and board3[3] == "X":
        print("X wins!")
        playing = False
        break
    elif  board3[1] == "X" and board3[2] == "X" and board3[3] == "X":
        print("X wins!")
        playing = False
        break
    elif  board1[1] == "X" and board2[2] == "X" and board3[3] == "X":
        print("X wins!")
        playing = False
        break
    elif  board3[1] == "X" and board2[2] == "X" and board1[3] == "X":
        print("X wins!")
        playing = False
        break
    elif  board1[1] == "X" and board2[1] == "X" and board3[1] == "X":
        print("X wins!")
        playing = False
        break
    elif  board1[2] == "X" and board2[2] == "X" and board3[2] == "X":
        print("X wins!")
        playing = False
        break
    elif  board1[3] == "X" and board2[3] == "X" and board3[3] == "X":
        print("X wins!")
        playing = False
        break
    elif  board1[1] == "O" and board1[2] == "O" and board1[3] == "O":
        print("O wins!")
        playing = False
        break
    elif  board2[1] == "O" and board2[2] == "O" and board3[3] == "O":
        print("O wins!")
        playing = False
        break
    elif  board3[1] == "O" and board3[2] == "O" and board3[3] == "O":
        print("O wins!")
        playing = False
        break
    elif  board1[1] == "O" and board2[2] == "O" and board3[3] == "O":
        print("O wins!")
        playing = False
        break
    elif  board3[1] == "O" and board2[2] == "O" and board1[3] == "O":
        print("O wins!")
        playing = False
        break
    elif  board1[1] == "O" and board2[1] == "O" and board3[1] == "O":
        print("O wins!")
        playing = False
        break
    elif  board1[2] == "O" and board2[2] == "O" and board3[2] == "O":
        print("O wins!")
        playing = False
        break
    elif  board1[3] == "O" and board2[3] == "O" and board3[3] == "O":
        print("O wins!")
        playing = False  
        break    
    